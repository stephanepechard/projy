#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Deployment of Projy. """

# system
import os, re
# fabric
from fabric.api import cd, env, execute, local, run, sudo, prefix
# projy
from projy import __version__


def fast_commit(capture=True):
    """ Perform fast commit. """
    env.warn_only = True
    local('git commit -am"fast commit through Fabric"')


def push():
    """ Local git push. """
    local("git push all")


def deploy():
    """ Commit and push to git servers. """
    execute(fast_commit)
    execute(push)


def reinstall():
    """ Reinstall the project to local virtualenv. """
    local('if [ $(pip freeze | grep Projy | wc -w ) -eq 1 ]; then '
          'pip uninstall -q -y Projy ; fi')
    local('python setup.py sdist')
    local('pip install -q dist/Projy-' + __version__ + '.tar.gz')
    local('rm -rf dist/ Projy.egg-info/')


def install():
    """ Install the project. """
    local('python setup.py install')
    local('rm -rf build')


def build_doc():
    """ Build the html documentation. """
    local('cd docs/ && make html')


def clean():
    """ Remove temporary files. """
    local('rm -rf docs/_build/ dist/ Projy.egg-info/')
    local('find . -name "*.pyc" | xargs rm')


def upload():
    """ Upload Pypi. """
    local("python setup.py sdist upload")


def md2rst(in_file, out_file, pipe):
    """ Generate reStructuredText from Makrdown. """
    local("pandoc -f markdown -t rst %s %s > %s" % (in_file, pipe, out_file))


def readme():
    md2rst('README.md', 'README.txt', '| head -n -7')
