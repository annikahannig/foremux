#!/usr/bin/env python
import os
from setuptools import setup, find_packages

long_description = open(
    os.path.join(
        os.path.dirname(__file__),
        'README.md'
    )
).read()


setup(
    name='foremux',
    author='Matthias Hannig',
    version='0.1.1',
    license='MIT',
    url='https://github.com/mhannig/foremux',
    description='Launch a Procfile using tmux',
    long_description=long_description,
    packages=find_packages('.'),
    entry_points={
        'console_scripts': [
            'foremux = foremux.launcher:main',
        ]
    },
)

