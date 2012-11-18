# -*- coding: utf-8 -*-
""" Terminal view. """

# system
from blessings import Terminal
import sys

# color codes
TERM_ORANGE = 0
TERM_RED = 1
TERM_GREEN = 2
TERM_YELLOW = 3
TERM_BLUE = 4
TERM_PINK = 5
TERM_CYAN = 6



class TerminalView:
    """ Terminal view to basic CLI information. """

    def __init__(self):
        self.term = Terminal()


    def print_error_and_exit(self, message):
        """ Print an error in red and exits the program. """
        sys.exit(self.term.bold_red('[ERROR] ' + message))


    def print_info(self, message):
        """ Print an informational text. """
        print(message)


    def text_in_color(self, message, color_code):
        """ Print with a beautiful color. See codes at the top of this file. """
        return self.term.color(color_code) + message + self.term.normal


    def format_question(self, message):
        """ Return an info-formatted string. """
        return self.term.bold(message)
