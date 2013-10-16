# -*- coding: utf-8 -*-
""" First thing to do: parse user-given arguments. """

# system
import os
import sys
# local [--with=<key,value> ...]
from projy.TerminalView import *


def docopt_arguments():
    """ Creates beautiful command-line interfaces.
        See https://github.com/docopt/docopt """
    doc = """Projy: Create templated project.

    Usage: projy <template> <project> [<substitution>...]
           projy -i | --info <template>
           projy -l | --list
           projy -h | --help
           projy -v | --version

    Options:
        -i, --info      Print information on a specific template.
        -l, --list      Print available template list.
        -h, --help      Show this help message and exit.
        -v, --version   Show program's version number and exit.
    """
    from docopt import docopt
    return docopt(doc, argv=sys.argv[1:], version='0.1')


def template_name_from_class_name(class_name):
    """ Remove the last 'Template' in the name. """
    suffix = 'Template'
    output = class_name
    if (class_name.endswith(suffix)):
        output = class_name[:-len(suffix)]
    return output


def run_list():
    """ Print the list of all available templates. """
    term = TerminalView()
    term.print_info("These are the available templates:")
    import pkgutil, projy.templates
    pkgpath = os.path.dirname(projy.templates.__file__)
    templates = [name for _, name, _ in pkgutil.iter_modules([pkgpath])]
    for name in templates:
        # the father of all templates, not a real usable one
        if (name != 'ProjyTemplate'):
            term.print_info(term.text_in_color(template_name_from_class_name(name), TERM_PINK))


def run_info(template):
    """ Print information about a specific template. """
    template.project_name = 'TowelStuff' # fake project name, always the same
    name = template_name_from_class_name(template.__class__.__name__)
    term = TerminalView()
    term.print_info("Content of template {} with an example project " \
          "named 'TowelStuff':".format(term.text_in_color(name, TERM_GREEN)))

    dir_name = None
    for file_info in sorted(template.files(), key=lambda dir: dir[0]):
        directory = file_name = template_name = ''
        if file_info[0]:
            directory = file_info[0]
        if file_info[1]:
            file_name = file_info[1]
        if file_info[2]:
            template_name = '\t\t - ' + file_info[2]
        if (directory != dir_name):
            term.print_info('\n\t' + term.text_in_color(directory + '/', TERM_PINK))
            dir_name = directory

        term.print_info('\t\t' + term.text_in_color(file_name, TERM_YELLOW) + template_name)

    # print substitutions
    try:
        subs = template.substitutes().keys()
        if len(subs) > 0:
            subs.sort()
            term.print_info("\nSubstitutions of this template are: ")
            max_len = 0
            for key in subs:
                if max_len < len(key):
                    max_len = len(key)
            for key in subs:
                term.print_info(u"\t{0:{1}} -> {2}".
                format(key, max_len, template.substitutes()[key]))
    except AttributeError:
        pass


def template_class_from_name(name):
    """ Return the template class object from agiven name. """
    # import the right template module
    term = TerminalView()
    template_name = name + 'Template'
    try:
        __import__('projy.templates.' + template_name)
        template_mod = sys.modules['projy.templates.' + template_name]
    except ImportError:
        term.print_error_and_exit("Unable to find {}".format(name))

    # import the class from the module
    try:
        template_class = getattr(template_mod, template_name)
    except AttributeError:
        term.print_error_and_exit("Unable to create a template {}".format(name))
    return template_class()


def execute():
    """ Main function. """
    args = docopt_arguments()
    term = TerminalView()

    # print list of installed templates
    if args['--list']:
        run_list()
        return

    # instanciate the class
    if args['<template>']:
        template = template_class_from_name(args['<template>'])

    # print info on a template
    if args['--info']:
        if args['<template>']:
            run_info(template)
        else:
            term.print_error_and_exit("Please specify a template")
        return

    # launch the template
    template.create(args['<project>'],
                    args['<template>'],
                    args['<substitution>'])
    term.print_info("Done!")
