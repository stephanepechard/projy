# -*- coding: utf-8 -*-
""" AuthorCollector class
    Tries to find the program user name, as accuratly as possible.

    Put the functions alphabetical order in the same order as their importance.
    For example here, author_from_git should be taken before author_from_system
    as it is probably better.
"""

# system
import getpass
import os
from subprocess import Popen, PIPE, CalledProcessError
# parent class
from projy.collectors.Collector import Collector


class AuthorCollector(Collector):
    """ The AuthorCollector class. """

    def __init__(self):
        self.author = None


    def author_from_git(self):
        """ Get the author name from git information. """
        self.author = None
        try:
            # launch git command and get answer
            cmd = Popen(["git", "config", "--get", "user.name"], stdout=PIPE)
            stdoutdata = cmd.communicate()
            if (stdoutdata[0]):
                self.author = stdoutdata[0].rstrip(os.linesep)
        except ImportError:
            pass
        except CalledProcessError:
            pass
        except OSError:
            pass

        return self.author


    def author_from_system(self):
        """ Get the author name from system information.
            This is just the user name, not the real name.
        """
        self.author = getpass.getuser()
        return self.author
