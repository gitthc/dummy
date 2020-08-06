#!/usr/bin/env python  
# -*- coding: utf-8 -*-

from setuptools import setup
import torch

setup(
    name='dummy',
    version='1.0.1',
    packages=['puppet'],
    install_requires=[
        "torch>=1.6.0",
        "torchvision>=0.7.0",
    ],
    platforms='any',
    # person
    author='thc',
    description='useless',
    long_description='useless',
    license='MIT',
    keywords='useless',
    url='https://github.com/gitthc/dummy.git',
)
