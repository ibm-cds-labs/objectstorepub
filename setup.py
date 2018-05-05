"""
A web app that serves files out of your IBM Object Storage.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='openobjectstore',
    version='1.0.0',
    description='A web app that serves files out of your IBM Object Storage',
    long_description=long_description,
    url='https://github.com/ibm-cds-labs/openobjectstore',
    license='Apache-2.0')
