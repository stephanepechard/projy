# -*- coding: utf-8 -*-
""" First thing to do: parse user-given arguments. """

# system
import os
import sys
# local [--with=<key,value> ...]
from projy import projy_style, projy_error, projy_info
from projy import PROJY_DIR, PROJY_PROJ, PROJY_FILE


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
    print(projy_info("These are the available templates:"))
    import pkgutil, projy.templates
    pkgpath = os.path.dirname(projy.templates.__file__)
    templates = [name for _, name, _ in pkgutil.iter_modules([pkgpath])]
    for name in templates:
        # the father of all templates, not a real usable one
        if (name != 'ProjyTemplate'):
            print('\t' + projy_style(template_name_from_class_name(name),
                                     PROJY_PROJ))


def run_info(template):
    """ Print information about a specific template. """
    template.project_name = 'TowelStuff' # fake project name, always the same
    name = template_name_from_class_name(template.__class__.__name__)
    print(projy_info("Content of template " +
          projy_style(name, PROJY_PROJ) +
          " with an example project name 'TowelStuff':"))

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
            print('\n\t' + projy_style(directory + '/', PROJY_DIR))
            dir_name = directory

        print('\t\t' + projy_style(file_name, PROJY_FILE) + template_name)

    # print substitutions
    try:
        subs = template.substitutes().keys()
        if len(subs) > 0:
            subs.sort()
            print('\n' + projy_info("Included substitutions are: "))
            max_len = 0
            for key in subs:
                if max_len < len(key):
                    max_len = len(key)
            for key in subs:
                print("\t{0:{1}} -> {2}".
                format(key, max_len, template.substitutes()[key]))
    except AttributeError:
        pass


def template_class_from_name(name):
    """ Return the template class object from agiven name. """
    # import the right template module
    template_name = name + 'Template'
    try:
        __import__('projy.templates.' + template_name)
        template_mod = sys.modules['projy.templates.' + template_name]
    except ImportError:
        sys.exit(projy_error("Unable to find {0}".format(name)))

    # import the class from the module
    try:
        template_class = getattr(template_mod, template_name)
    except AttributeError:
        sys.exit(projy_error("Unable to create a template {0}".format(name)))
    return template_class()


def execute():
    """ Main function. """
    args = docopt_arguments()

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
            sys.exit(projy_error("Please specify a template"))
        return

    # launch the template
    template.create(args['<project>'],
                    args['<template>'],
                    args['<substitution>'])
    print(projy_info("Done!"))
