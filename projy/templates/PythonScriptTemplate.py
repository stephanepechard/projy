# -*- coding: utf-8 -*-
""" Projy template for Python script. """

# system
from datetime import date
# parent class
from projy.templates.ProjyTemplate import ProjyTemplate
# collectors
from projy.collectors.AuthorCollector import AuthorCollector


class PythonScriptTemplate(ProjyTemplate):
    """ Projy template for a Python script. """

    def __init__(self):
        ProjyTemplate.__init__(self)


    def directories(self):
        """ Return the names of directories to be created. """
        directories_description = [
            self.project_name,
        ]
        return directories_description


    def files(self):
        """ Return the names of files to be created. """
        files_description = [
            [ self.project_name,
              self.project_name + '.py',
              'PythonScriptFileTemplate' ],
        ]
        return files_description


    def substitutes(self):
        """ Return the substitutions for the templating replacements. """
        author_collector = AuthorCollector()
        substitute_dict = dict(
            project = self.project_name,
            date = date.today().isoformat(),
            author = author_collector.collect()
        )
        return substitute_dict
