Boto Stubs
==========

This repo contains a generator that produces type hints for botocore as well as
the generated output. These type hints can be used both for the purpose of
static type analysis and for dot completion support. The latter is relevant
because botocore's classes don't exist until runtime, and therefore IDEs cannot
know all the methods that will be available without this.

Installation / Usage
--------------------

To make use of the type hints, install the ``botocore-stubs`` package. mypy
will automatically pick up on the type hints for botocore, even without
expclitit annotations in your code. Other tools compatible with PEP561_ style
packages should also work.

Currently only botocore is supported. If you are using boto3 you will need to
annotate your calls to ``boto3.client`` like so::

    s3 = boto3.client('s3')  # type: botocore.client.S3

There is a known issue where boto3-specific methods, such as ``upload_file``
are not present in the stub files.

Development
-----------

This project uses black_ and pre-commit_ to enforce sytle on python code. On
macOS you can do the following to get started::

    brew install pre-commit
    pre-commit install

That will set up the hooks to run black on every commit.

Structure
~~~~~~~~~

This repo contains multiple packages:

* ``botocore-stubs`` is the stubs-only package that provides type hints for
  botocore. Most of it is generated code.
* ``botogen`` is the code generator for the stubs packages.

When boto3 support is added, it will be under its own package, ``boto3-stubs``.

.. _black: https://github.com/python/black
.. _pre-commit: https://pre-commit.com/
.. _PEP561: https://www.python.org/dev/peps/pep-0561/
