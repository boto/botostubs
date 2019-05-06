import os
import sys
from pathlib import Path

from mypy_extensions import TypedDict
from botocore.session import get_session
from jinja2 import Environment, FileSystemLoader

import botogen


# These services have parameters that are keywords
BLACKLIST = [
    'cloudsearchdomain',
    'logs',
]


class ClientClass(object):
    def __init__(self, service_name, class_name, operations, structures):
        self.service_name = service_name
        self.class_name = class_name
        self.operations = operations
        self.structures = structures


class ClientOperation(object):
    def __init__(
        self, method_name, output_type, required_params, optional_params
    ):
        self.method_name = method_name
        self.output_type = output_type
        self.required_params = required_params
        self.optional_params = optional_params


class ClientParam(object):
    def __init__(self, name, param_type):
        self.name = name
        self.type = param_type


class Shape(object):
    def __init__(self, name):
        self.name = name

    @property
    def type_hint(self):
        raise NotImplementedError("type_hint")


class StructureShape(Shape):
    def __init__(self, name, class_name, required_params, optional_params):
        super(StructureShape, self).__init__(name)
        self.class_name = class_name
        self.required_params = required_params
        self.optional_params = optional_params

    def type_hint(self):
        return self.class_name


class ListShape(Shape):
    def __init__(self, name, member_shape):
        super(ListShape, self).__init__(name)
        self.member_shape = member_shape

    def type_hint(self):
        return "List[%s]" % self.member_shape.type_hint()


class MapShape(Shape):
    def __init__(self, name, key_shape, value_shape):
        super(MapShape, self).__init__(name)
        self.key_shape = key_shape
        self.value_shape = value_shape

    def type_hint(self):
        return "Dict[%s, %s]" % (
            self.key_shape.type_hint(),
            self.value_shape.type_hint(),
        )


class StringShape(Shape):
    def type_hint(self):
        return "str"


class TimestampShape(Shape):
    def type_hint(self):
        return "datetime.datetime"


class BlobShape(Shape):
    def type_hint(self):
        return "bytes"


class IntegerShape(Shape):
    def type_hint(self):
        return "int"


class FloatShape(Shape):
    def type_hint(self):
        return "float"


class LongShape(Shape):
    def type_hint(self):
        return "int"


class DoubleShape(Shape):
    def type_hint(self):
        return "float"


class BooleanShape(Shape):
    def type_hint(self):
        return "bool"


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

        structure_shapes = [
            s for s in self._shapes.values() if isinstance(s, StructureShape)
        ]
        return ClientClass(
            self._client.meta.service_model.service_name,
            self._class_name,
            operations,
            structure_shapes,
        )

    def _generate_operation(self, method_name, operation_model):
        input_model = operation_model.input_shape
        required_params = []
        optional_params = []

        if input_model is not None:
            required_params, optional_params = self._generate_operation_input(
                input_model
            )

        output_model = operation_model.output_shape
        output_shape = None
        if output_model is not None:
            output_shape = self._generate_shape(output_model)

        return ClientOperation(
            method_name=method_name,
            required_params=required_params,
            optional_params=optional_params,
            output_type=output_shape,
        )

    def _generate_operation_input(self, input_model):
        required_params = []
        optional_params = []
        for param_name, param_model in input_model.members.items():
            param_shape = self._generate_shape(param_model)
            param = ClientParam(param_name, param_shape)

            if param_name in input_model.required_members:
                required_params.append(param)
            else:
                optional_params.append(param)

        return required_params, optional_params

    def _generate_shape(self, shape_model):
        shape_name = shape_model.name
        if shape_name in self._shapes:
            return self._shapes[shape_name]

        fun = getattr(self, "_generate_%s_shape" % shape_model.type_name, None)
        if fun is None:
            raise Exception("Nothing doing for %s" % shape_model.type_name)

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
        return StructureShape(
            shape_model.name, class_name, required_members, optional_members
        )

    def _generate_list_shape(self, shape_model):
        member_shape = self._generate_shape(shape_model.member)
        return ListShape(shape_model.name, member_shape)

    def _generate_map_shape(self, shape_model):
        key_shape = self._generate_shape(shape_model.key)
        value_shape = self._generate_shape(shape_model.value)
        return MapShape(shape_model.name, key_shape, value_shape)

    def _generate_string_shape(self, shape_model):
        return StringShape(shape_model.name)

    def _generate_blob_shape(self, shape_model):
        return BlobShape(shape_model.name)

    def _generate_integer_shape(self, shape_model):
        return IntegerShape(shape_model.name)

    def _generate_float_shape(self, shape_model):
        return FloatShape(shape_model.name)

    def _generate_double_shape(self, shape_model):
        return DoubleShape(shape_model.name)

    def _generate_long_shape(self, shape_model):
        return LongShape(shape_model.name)

    def _generate_timestamp_shape(self, shape_model):
        return TimestampShape(shape_model.name)

    def _generate_boolean_shape(self, shape_model):
        return BooleanShape(shape_model.name)


def render(service_names=None):
    services = _get_service_structure(service_names)
    templates_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "templates")
    )
    env = Environment(loader=FileSystemLoader(templates_dir))

    stubs_package = Path(botogen.__file__).parent.parent.parent
    stubs_module = stubs_package / "botocore-stubs" / "botocore-stubs"

    with open(stubs_module / "client.pyi", "w") as f:
        f.write(render_client(services, env))
    with open(stubs_module / "session.pyi", "w") as f:
        f.write(render_session(services, env))


def render_session(services, env):
    template = env.get_template("session.pyi.j2")
    return template.render(services=services)


def render_client(services, env):
    template = env.get_template("client.pyi.j2")
    return template.render(services=services)


def _get_service_structure(service_names=None):
    sess = get_session()
    if not service_names:
        service_names = [s for s in sess.get_available_services() if s not in
                         BLACKLIST]

    services = []
    for service in service_names:
        client = sess.create_client(service)
        try:
            client_class = ServiceTypeGenerator(client).generate()
            services.append(client_class)
        except RecursionError:
            sys.stderr.write("Recursion issue in %s\n" % service)

    return services
