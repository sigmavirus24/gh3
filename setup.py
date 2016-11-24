"""Packaging logic for gh3"""
import os.path
import sys

import setuptools

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))  # noqa

import gh3

requirements = [
    'attrs >= 16.3',
    'requests[security] >= 2.12.1',
    'uritemplate >= 3.0',
]


setuptools.setup(
    name='gh3',
    license='Apache 2.0',
    version=gh3.__version__,
    description='Python GitHub API wrapper',
    long_description='',
    author='Ian Cordasco',
    author_email='graffatcolmingov@gmail.com',
    url='https://github.com/sigmavirus24/gh3',
    package_dir={'': 'src'},
    packages=[
        'gh3',
    ],
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
