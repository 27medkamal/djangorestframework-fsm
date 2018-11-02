#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='djangorestframework-fsm',
    version='0.1.1',
    description='Automatically hook your Django-FSM transitions up to Django REST Framework',
    author='Ahmed Kamal',
    author_email='27madkamal@gmail.com',
    url='https://github.com/27medkamal/djangorestframework-fsm',
    packages=find_packages(),
    install_requires=['django', 'django_fsm', 'djangorestframework'],
)
