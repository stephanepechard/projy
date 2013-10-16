# -*- coding: utf-8 -*-
""" Projy template for PythonPackage. """

# system
from datetime import date
from os import mkdir, rmdir
from shutil import move
from subprocess import call
# parent class
from projy.templates.ProjyTemplate import ProjyTemplate
# collectors
from projy.collectors.AuthorCollector import AuthorCollector
from projy.collectors.AuthorMailCollector import AuthorMailCollector


class DjangoProjectTemplate(ProjyTemplate):
    """ Projy template class for PythonPackage. """

    def __init__(self):
        ProjyTemplate.__init__(self)


    def directories(self):
        """ Return the names of directories to be created. """
        directories_description = [
            self.project_name,
            self.project_name + '/conf',
            self.project_name + '/static',
        ]
        return directories_description


    def files(self):
        """ Return the names of files to be created. """
        files_description = [
            # configuration
            [ self.project_name,
              'Makefile',
              'DjangoMakefileTemplate' ],
            [ self.project_name + '/conf',
              'requirements_base.txt',
              'DjangoRequirementsBaseTemplate' ],
            [ self.project_name + '/conf',
              'requirements_dev.txt',
              'DjangoRequirementsDevTemplate' ],
            [ self.project_name + '/conf',
              'requirements_production.txt',
              'DjangoRequirementsProdTemplate' ],
            [ self.project_name + '/conf',
              'nginx.conf',
              'DjangoNginxConfTemplate' ],
            [ self.project_name + '/conf',
              'supervisord.conf',
              'DjangoSupervisorConfTemplate' ],
            [ self.project_name,
              'fabfile.py',
              'DjangoFabfileTemplate' ],
            [ self.project_name,
              'CHANGES.txt',
              'PythonPackageCHANGESFileTemplate' ],
            [ self.project_name,
              'LICENSE.txt',
              'GPL3FileTemplate' ],
            [ self.project_name,
              'README.txt',
              'READMEReSTFileTemplate' ],
            [ self.project_name,
              '.gitignore',
              'DjangoGitignoreTemplate' ],
            # django files
            [ self.project_name,
              'dev.py',
              'DjangoSettingsDevTemplate' ],
            [ self.project_name,
              'prod.py',
              'DjangoSettingsProdTemplate' ],
        ]
        return files_description


    def substitutes(self):
        """ Return the substitutions for the templating replacements. """
        author_collector = AuthorCollector()
        mail_collector = AuthorMailCollector()
        substitute_dict = {
            'project': self.project_name,
            'project_lower': self.project_name.lower(),
            'date': date.today().isoformat(),
            'author': author_collector.collect(),
            'author_email': mail_collector.collect(),
        }
        return substitute_dict


    def posthook(self):
        # build the virtualenv
        call(['make'])

        # create the Django project
        call(['./venv/bin/django-admin.py', 'startproject', self.project_name])

        # transform original settings files into 3 files for different env
        mkdir('{p}/settings'.format(p=self.project_name))
        self.touch('{p}/settings/__init__.py'.format(p=self.project_name))
        move('dev.py', '{p}/settings'.format(p=self.project_name))
        move('prod.py', '{p}/settings'.format(p=self.project_name))
        move('{p}/{p}/settings.py'.format(p=self.project_name), '{p}/settings/base.py'.format(p=self.project_name))

        # organize files nicely
        mkdir('{p}/templates'.format(p=self.project_name))
        move('{p}/manage.py'.format(p=self.project_name), 'manage.py')
        move('{p}/{p}/__init__.py'.format(p=self.project_name), '{p}/'.format(p=self.project_name))
        move('{p}/{p}/urls.py'.format(p=self.project_name), '{p}/'.format(p=self.project_name))
        move('{p}/{p}/wsgi.py'.format(p=self.project_name), '{p}/'.format(p=self.project_name))
        rmdir('{p}/{p}'.format(p=self.project_name))

        # create empty git repo
        call(['git', 'init'])

        # replace some lines
        self.replace_in_file('{p}/wsgi.py'.format(p=self.project_name),
                             '"{p}.settings"'.format(p=self.project_name),
                             '"{p}.settings.production"'.format(p=self.project_name))
        self.replace_in_file('{p}/settings/base.py'.format(p=self.project_name),
                             u"    # ('Your Name', 'your_email@example.com'),",
                             u"    ('{}', '{}'),".format(self.substitutes()['author'],
                                                         self.substitutes()['author_email']))

