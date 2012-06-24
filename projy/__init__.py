# -*- coding: utf-8 -*-
""" Common stuff. """


PROJY_ERROR = 0
PROJY_INFO = 1
PROJY_OK = 2
PROJY_DIR = 3
PROJY_PROJ = 4
PROJY_FILE = 5


def projy_style(string, status):
    """ Return a shell-colored text. """
    style_code = '2'
    if (status == PROJY_ERROR):
        style_code = '31' # red
    elif (status == PROJY_OK or status == PROJY_DIR):
        style_code = '32' # green
    elif (status == PROJY_FILE):
        style_code = '33' # yellow
    elif (status == PROJY_PROJ):
        style_code = '35' # pink
    return '\x1b[{0}m{1}\x1b[0m'.format(style_code, string)


def projy_info(string):
    """ Format a string into an information shell line. """
    return "{0} {1}".format(projy_style('[INFO]', PROJY_INFO), string)


def projy_error(string):
    """ Format a string into an error shell line. """
    return "{0} {1}".format(projy_style('[ERROR]', PROJY_ERROR), string)

