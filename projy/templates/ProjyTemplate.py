# -*- coding: utf-8 -*-
""" Main ProjyTemplate class. """

# system
import errno
import io
import os
from os.path import join, dirname
import shutil
import tempfile
from string import Template
# local
from projy.TerminalView import *



class ProjyTemplate:
    """ Base template class for a Projy project creation. """

    def __init__(self):
        self.project_name = None
        self.template_name = None
        self.substitutes_dict = {}
        self.term = TerminalView()


    def create(self, project_name, template_name, substitutions):
        """ Launch the project creation. """
        self.project_name = project_name
        self.template_name = template_name

        # create substitutions dictionary from user arguments
        # TODO: check what is given
        for subs in substitutions:
            current_sub = subs.split(',')
            current_key = current_sub[0].strip()
            current_val = current_sub[1].strip()
            self.substitutes_dict[current_key] = current_val

        self.term.print_info(u"Creating project '{0}' with template {1}"
            .format(self.term.text_in_color(project_name, TERM_PINK), template_name))

        self.make_directories()
        self.make_files()
        self.make_posthook()


    def make_directories(self):
        """ Create the directories of the template. """

        # get the directories from the template
        directories = []
        try:
            directories = self.directories()
        except AttributeError:
            self.term.print_info(u"No directory in the template.")

        working_dir = os.getcwd()
        # iteratively create the directories
        for directory in directories:
            dir_name = working_dir + '/' + directory
            if not os.path.isdir(dir_name):
                try:
                    os.makedirs(dir_name)
                except OSError, error:
                    if error.errno != errno.EEXIST:
                        raise
            else:
                self.term.print_error_and_exit(u"The directory {0} already exists."
                         .format(directory))

            self.term.print_info(u"Creating directory '{0}'"
                                 .format(self.term.text_in_color(directory, TERM_GREEN)))


    def make_files(self):
        """ Create the files of the template.  """

        # get the files from the template
        files = []
        try:
            files = self.files()
        except AttributeError:
            self.term.print_info(u"No file in the template. Weird, but why not?")

        # get the substitutes intersecting the template and the cli
        try:
            for key in self.substitutes().keys():
                if key not in self.substitutes_dict:
                    self.substitutes_dict[key] = self.substitutes()[key]

        except AttributeError:
            self.term.print_info(u"No substitute in the template.")

        working_dir = os.getcwd()
        # iteratively create the files
        for directory, name, template_file in files:
            if directory:
                filepath = working_dir + '/' + directory + '/' + name
                filename = directory + '/' + name
            else:
                filepath = working_dir + '/' + name
                filename = name

            # open the file to write into
            try:
                output = open(filepath, 'w')
            except IOError:
                self.term.print_error_and_exit(u"Can't create destination"\
                                                " file: {0}".format(filepath))

            # open the template to read from
            if template_file:
                input_file = join(dirname(__file__), template_file + '.txt')

                # write each line of input file into output file,
                # templatized with substitutes
                try:
                    with open(input_file, 'r') as line:
                        template_line = Template(line.read())
                        output.write(template_line.
                                safe_substitute(self.substitutes_dict))
                    output.close()
                except IOError:
                    self.term.print_error_and_exit(u"Can't create template file"\
                                                   ": {0}".format(input_file))
            else:
                output.close() # the file is empty, but still created

            self.term.print_info(u"Creating file '{0}'"
                             .format(self.term.text_in_color(filename, TERM_YELLOW)))


    def make_posthook(self):
        """ Run the post hook into the project directory. """
        if self.posthook:
            os.chdir(self.project_name) # enter the project main directory
            self.posthook()


    def replace_in_file(self, file_path, old_exp, new_exp):
        """ In the given file, replace all 'old_exp' by 'new_exp'. """
        self.term.print_info(u"Making replacement into {}"
                                 .format(self.term.text_in_color(file_path,
                                                                 TERM_GREEN)))
        # write the new version into a temporary file
        tmp_file = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
        for filelineno, line in enumerate(io.open(file_path, encoding="utf-8")):
            if old_exp in line:
                line = line.replace(old_exp, new_exp)
            tmp_file.write(line.encode('utf-8'))

        name = tmp_file.name # keep the name
        tmp_file.close()
        shutil.copy(name, file_path) # replace the original one
        os.remove(name)

        # old version, not suitable with utf-8...
        #for line in fileinput.input(file_path, inplace=1):
            #if old_exp in line:
                #line = line.replace(old_exp, new_exp)
            ## write inline into the file (comma at the end is Python2 specific!)
            #print(line),


    def touch(self, filename):
        """ A simple equivalent of the well known shell 'touch' command. """
        with file(filename, 'a'):
            os.utime(filename, None)

