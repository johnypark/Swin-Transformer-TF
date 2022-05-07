import os
import sys

from distutils.core import setup
from setuptools import find_packages
import setuptools


# List of runtime dependencies required by this built package
install_requires = []
#if sys.version_info <= (2, 7):
    #install_requires += ['future', 'typing']
install_requires += ['numpy', 'tensorflow']#'numpy', 'protobuf', 'crc32c']

# read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setuptools.setup(
    name='swintransformer',
    version='0.0.1',
    description='swintransformer-TF',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="rishigami",
    author_email='',
    url="https://github.com/johnypark/Swin-Transformer-TF",
    packages=find_packages(),
    license='MIT',
    install_requires=install_requires
)


