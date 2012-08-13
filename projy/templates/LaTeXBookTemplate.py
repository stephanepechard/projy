# -*- coding: utf-8 -*-
""" Projy template for a LaTeX project. """

# system
from datetime import date
# parent class
from projy.templates.ProjyTemplate import ProjyTemplate
# collectors
from projy.collectors.AuthorCollector import AuthorCollector


class LaTeXBookTemplate(ProjyTemplate):
    """ Projy template for a LaTeX project. """

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
              self.project_name + '.tex',
              'LaTeXBookFileTemplate'
            ],
            [ self.project_name,
              'references.bib',
              'BibTeXFileTemplate'
            ],
            [ self.project_name,
              'Makefile',
              'LaTeXMakefileFileTemplate'
            ],
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
