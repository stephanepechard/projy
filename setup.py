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
    'version': '0.1',
    'packages': ['projy', 'projy.templates', 'projy.collectors', 'projy.tests'],
    'description': 'My projy Project',
    'long_description': open(join(dirname(__file__), 'README.txt')).read(),
    'author': 'Stéphane Péchard',
    'url': 'http://s13d.fr/',
    'download_url': 'Where to download it.',
    'author_email': 'stephanepechard@gmail.com',
    'install_requires': ['nose'],
    'scripts': ['bin/projy'],
    'test_suite': 'projy.test',
    'include_package_data': True,
}

setup(**config)

