#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Projy setup.py script """

# system
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from os.path import join, dirname


config = {
    'name': 'Projy',
    'version': '0.2',
    'packages': ['projy', 'projy.templates', 'projy.collectors'],
    'description': 'Projy is a template-based skeleton generator.',
    'long_description': open(join(dirname(__file__), 'README')).read(),
    'author': 'Stéphane Péchard',
    'url': 'https://github.com/stephanepechard/projy',
    'download_url': 'https://github.com/stephanepechard/projy',
    'author_email': 'stephanepechard@gmail.com',
    'install_requires': [],
    'scripts': ['bin/projy'],
    'include_package_data': True,
}

setup(**config)

