# -*- coding: utf-8 -*-
""" Projy template for a bootstrap project. """

# parent class
from projy.templates.ProjyTemplate import ProjyTemplate


class BootstrapTemplate(ProjyTemplate):
    """ Projy template for a bootstrap project. """

    def __init__(self):
        ProjyTemplate.__init__(self)


    def files(self):
        """ Return the names of files to be created. """
        files_description = [
            [ None,
              'bootstrap',
              'BootstrapScriptFileTemplate'
            ],
        ]
        return files_description

