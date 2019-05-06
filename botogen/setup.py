#!/usr/bin/env python
import codecs
import os.path
import re
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(HERE, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='botogen',
    version=find_version('botogen', '__init__.py'),
    description='Generated type hints for botocore.',
    long_description=read('README.rst'),
    author='Amazon Web Services',
    packages=find_packages(exclude=['tests']),
    install_requires=read('requirements', 'base.txt'),
    license='Apache License 2.0',
    keywords='aws botocore boto boto3',
    entry_points={
        'console_scripts': [
            'botogen = botogen.cli:main'
        ]
    },
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ),
    python_requires='>=3.7.0',
)
