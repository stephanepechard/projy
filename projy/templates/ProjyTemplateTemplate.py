# -*- coding: utf-8 -*-
""" Projy template for Projy template. Kinda meta, isn't it? """

# parent class
from projy.templates.ProjyTemplate import ProjyTemplate


class ProjyTemplateTemplate(ProjyTemplate):
    """ Projy template class for ProjyTemplate. """

    def __init__(self):
        ProjyTemplate.__init__(self)


    def files(self):
        """ Return the names of files to be created. """
        files_description = [
            [ None,
              self.project_name + 'Template.py',
              'ProjyTemplateFileTemplate' ],
            [ None,
              self.project_name + 'FileTemplate.txt',
              None ],
        ]
        return files_description


    def substitutes(self):
        """ Return the substitutions for the templating replacements. """
        substitute_dict = dict(
            project = self.project_name,
            template = self.project_name + 'Template',
            file = self.project_name + 'FileTemplate',
        )
        return substitute_dict

