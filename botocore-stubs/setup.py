import codecs
import os.path

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(HERE, *parts), "r").read()


setup(
    name="botocore-stubs",
    version="0.0.1",
    description="Type hints for botocore.",
    long_description=read("README.rst"),
    author="Amazon Web Services",
    url="https://github.com/boto/stubs",
    packages=["botocore-stubs"],
    package_data={
        "botocore-stubs": ["__init__.pyi", "session.pyi", "client.pyi"]
    },
    include_package_data=True,
    install_requires=read("requirements", "base.txt"),
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
