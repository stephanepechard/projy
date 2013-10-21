#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Deployment of Projy. """

# system
import os, re
# fabric
from fabric.api import cd, env, execute, local, run, sudo, prefix
# projy
from projy import __version__

COMMON_COMMIT_MESSAGE = u"Fast commit through Fabric"


def commit(message=COMMON_COMMIT_MESSAGE, capture=True):
    """ git commit with common commit message when omit. """
    env.warn_only = True
    local(u'git commit -am"{}"'.format(message))


def push():
    """ Local git push. """
    local("git push")


def deploy(message=COMMON_COMMIT_MESSAGE):
    """ Commit and push to git servers. """
    execute(commit, message)
    execute(push)


def reinstall():
    """ Reinstall the project to local virtualenv. """
    local('if [ $(pip freeze | grep Projy | wc -w ) -eq 1 ]; then '
          './venv/bin/pip uninstall -q -y Projy ; fi')
    local('./venv/bin/python setup.py sdist')
    local('./venv/bin/pip install -q dist/Projy-' + __version__ + '.tar.gz')
    local('rm -rf dist/ Projy.egg-info/')


def install():
    """ Install the project. """
    local('./venv/bin/python setup.py install')
    local('rm -rf build')


def md2rst(in_file, out_file, pipe):
    """ Generate reStructuredText from Makrdown. """
    local("pandoc -f markdown -t rst %s %s > %s" % (in_file, pipe, out_file))


def readme():
    md2rst('README.md', 'README.txt', '| head -n -8 | tail -n +3')


def build_doc():
    """ Build the html documentation. """
    local('cd docs/ && make html')
    local('cd docs/_build/html && zip -9 -T -r ../Projy-' + __version__ + '.zip *')
    local('cat docs/changelog.rst | tail -n +3 > CHANGES.txt')


def watch_doc():
    local('venv/bin/watchmedo shell-command --patterns="docs/*.rst" --command="fab build_doc" ./docs/')


def tests():
    """ Launch tests. """
    local("nosetests")
    # local("coverage html -d /tmp/coverage-projy --omit='projy/docopt.py'")
    # local("coverage erase")


def clean():
    """ Remove temporary files. """
    local('rm -rf docs/_build/ dist/ Projy.egg-info/')
    local('find . -name "*.pyc" | xargs rm')


def upload():
    """ Upload Pypi. """
    local("python setup.py sdist upload")
