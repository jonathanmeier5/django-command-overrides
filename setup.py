#!/usr/bin/env python
import os

from setuptools import setup


setup(
    name='django-command-overrides',
    url='https://github.com/jonathanmeier5/django-command-overrides',
    version='0.0.0',
    author='jonathan meier',
    author_email='jonathan.w.meier@gmail.com',
    package_dir={'': 'src'},
    packages=['command_overrides'],
)
