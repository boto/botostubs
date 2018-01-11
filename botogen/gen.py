from mypy_extensions import TypedDict
from botocore.session import get_session
from jinja2 import Environment, PackageLoader


class ClientClass(object):
    def __init__(self, class_name, operations, structures):
        self.class_name = class_name
        self.operations = operations
        self.structures = structures


class ClientOperation(object):
    def __init__(self, method_name, output_type, required_params,
                 optional_params):
        self.method_name = method_name
        self.output_type = output_type
        self.required_params = required_params
        self.optional_params = optional_params


class ClientParam(object):
    def __init__(self, name, param_type):
        self.name = name
        self.type = param_type


class Shape(object):
    @property
    def type_hint(self):
        raise NotImplementedError('type_hint')


class StructureShape(Shape):
    def __init__(self, class_name, required_params, optional_params):
        self.class_name = class_name
        self.required_params = required_params
        self.optional_params = optional_params

    def type_hint(self):
        return self.class_name

class ListShape(Shape):
    def __init__(self, member_shape):
        self.member_shape = member_shape

    def type_hint(self):
        return 'List[%s]' % self.member_shape.type_hint


class MapShape(Shape):
    def __init__(self, key_shape, value_shape):
        self.key_shape = key_shape
        self.value_shape = value_shape

    def type_hint(self):
        return 'Dict[%s, %s]' % (
            self.key_shape.type_hint, self.value_shape.type_hint
        )


class StringShape(Shape):
    def type_hint(self):
        return 'str'


class TimestampShape(Shape):
    def type_hint(self):
        return 'datetime.datetime'


class BlobShape(Shape):
    def type_hint(self):
        return 'bytes'


class IntegerShape(Shape):
    def type_hint(self):
        return 'int'


class FloatShape(Shape):
    def type_hint(self):
        return 'float'


class ServiceTypeGenerator(object):
    def __init__(self, client):
        self._client = client
        self._class_name = type(self._client).__name__
        self._model = client.meta.service_model
        self._shapes = {}

    def generate(self):
        mapping = self._client.meta.method_to_api_mapping
        operations = []
        for method_name, operation_name in mapping.items():
            operation_model = self._model.operation_model(operation_name)
            operation = self._generate_operation(method_name, operation_model)
            operations.append(operation)

        structure_shapes = [s for s in self._shapes if isinstance(s, StructureShape)]
        return ClientClass(self._class_name, operations, structure_shapes)

    def _generate_operation(self, method_name, operation_model):
        input_model = operation_model.input_shape
        required_params = []
        optional_params = []

        if input_model is not None:
            input_shape = self._generate_shape(input_model)
            required_params = input_shape.required_params
            optional_params = input_shape.optional_params

        output_model = operation_model.output_shape
        output_shape = None
        if output_shape is not None:
            output_shape = self._generate_shape(output_model)

        return ClientOperation(
            method_name=method_name,
            required_params=required_params,
            optional_params=optional_params,
            output_type=output_shape
        )


    def _generate_shape(self, shape_model):
        shape_name = shape_model.name
        if shape_name in self._shapes:
            return self._shapes[shape_name]

        fun = getattr(self, '_generate_%s_shape' % shape_model.type_name, None)
        if fun is None:
            raise Exception('Nothing doing for %s' % shape_model.type_name)

        shape = fun(shape_model)
        self._shapes[shape_name] = shape
        return shape

    def _generate_structure_shape(self, shape_model):
        required_members = []
        optional_members = []
        for member_name, member_model in shape_model.members.items():
            member_shape = self._generate_shape(member_model)
            if member_name in shape_model.required_members:
                required_members.append(member_shape)
            else:
                optional_members.append(member_shape)

        class_name = self._class_name + shape_model.name
        return StructureShape(class_name, required_members, optional_members)

    def _generate_list_shape(self, shape_model):
        member_shape = self._generate_shape(shape_model.member)
        return ListShape(member_shape)

    def _generate_map_shape(self, shape_model):
        key_shape = self._generate_shape(shape_model.key)
        value_shape = self._generate_shape(shape_model.value)
        return  MapShape(key_shape, value_shape)

    def _generate_string_shape(self, shape_model):
        return StringShape()

    def _generate_blob_shape(self, shape_model):
        return BlobShape()

    def _generate_integer_shape(self, shape_model):
        return IntegerShape()

    def _generate_float_shape(self, shape_model):
        return FloatShape()

    def _generate_timestamp_shape(self, shape_model):
        return TimestampShape()


def render_client(client_class):
    env = Environment(
        loader=PackageLoader('templates')
    )
    client_template = env.get_template('client.py')


def main():
    sess = get_session()
    client = sess.create_client('sts')
    generator = ServiceTypeGenerator(client)
    client_class = generator.generate()
    render_client(client_class)


if __name__ == "__main__":
    main()
