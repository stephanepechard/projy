# -*- coding: utf-8 -*-
""" Projy template for a fabfile project. """

# parent class
from projy.templates.ProjyTemplate import ProjyTemplate


class FabfileTemplate(ProjyTemplate):
    """ Projy template for a fabfile project. """

    def __init__(self):
        ProjyTemplate.__init__(self)


    def files(self):
        """ Return the names of files to be created. """
        files_description = [
            [ None,
              'fabfile.py',
              'FabfileFileTemplate'
            ],
        ]
        return files_description

    def substitutes(self):
        """ Return the substitutions for the templating replacements. """
        substitute_dict = dict(
            project = self.project_name,
        )
        return substitute_dict
