# -*- coding: utf-8 -*-
""" Projy template for PythonPackage. """

# system
from datetime import date
# parent class
from projy.templates.ProjyTemplate import ProjyTemplate
# collectors
from projy.collectors.AuthorCollector import AuthorCollector
from projy.collectors.AuthorMailCollector import AuthorMailCollector


class PythonPackageTemplate(ProjyTemplate):
    """ Projy template class for PythonPackage. """

    def __init__(self):
        ProjyTemplate.__init__(self)


    def directories(self):
        """ Return the names of directories to be created. """
        directories_description = [
            self.project_name,
            self.project_name + '/' + self.project_name.lower(),
            self.project_name + '/docs',
        ]
        return directories_description


    def files(self):
        """ Return the names of files to be created. """
        files_description = [
            [ self.project_name,
              'bootstrap',
              'BootstrapScriptFileTemplate' ],
            [ self.project_name,
              'CHANGES.txt',
              'PythonPackageCHANGESFileTemplate' ],
            [ self.project_name,
              'LICENSE.txt',
              'GPL3FileTemplate' ],
            [ self.project_name,
              'MANIFEST.in',
              'PythonPackageMANIFESTFileTemplate' ],
            [ self.project_name,
              'README.txt',
              'READMEReSTFileTemplate' ],
            [ self.project_name,
              'setup.py',
              'PythonPackageSetupFileTemplate' ],
            [ self.project_name + '/' + self.project_name.lower(),
              '__init__.py',
              None ],
            [ self.project_name + '/docs',
              'index.rst',
              None ],
        ]
        return files_description


    def substitutes(self):
        """ Return the substitutions for the templating replacements. """
        author_collector = AuthorCollector()
        mail_collector = AuthorMailCollector()
        substitute_dict = dict(
            project = self.project_name,
            project_lower = self.project_name.lower(),
            date = date.today().isoformat(),
            author = author_collector.collect(),
            author_email = mail_collector.collect(),
        )
        return substitute_dict
