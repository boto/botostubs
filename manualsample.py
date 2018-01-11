import botocore.session

sess = botocore.session.get_session()
client = sess.create_client('sts')
assert isinstance(client, botocore.client.STS)

response = client.get_caller_identity()
foo = response['bar']
