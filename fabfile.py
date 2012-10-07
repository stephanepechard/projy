#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Deployment of Projy. """

# system
import os, re
# fabric
from fabric.api import cd, env, execute, local, run, sudo, prefix


def projy_version():
    """ Get version from setup.py file. """
    version = '0.1'
    with open(os.path.abspath('setup.py')) as f:
        regex = re.compile(r"    'version': '(.*?)',", re.DOTALL)
        for matched in regex.finditer(f.read()):
            version = matched.group(1)
    return version


def build_doc():
    """ Build the html documentation. """
    local('cd docs/ && make html')


def clean():
    """ Remove temporary files. """
    local('rm -rf docs/_build/ dist/ Projy.egg-info/')
    local('find . -name "*.pyc" | xargs rm')


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


def install():
    """ Reinstall the project to local virtualenv. """
    local('if [ $(pip freeze | grep Projy | wc -w ) -eq 1 ]; then '
          'pip uninstall -q -y Projy ; fi')
    local('python setup.py sdist')
    local('pip install -q dist/Projy-' + projy_version() + '.tar.gz')
    local('rm -rf dist/ Projy.egg-info/')


def upload_pypi():
    """ Upload current version to pypi. """
    local("python setup.py sdist register upload")
