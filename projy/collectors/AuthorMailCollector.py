# -*- coding: utf-8 -*-
""" AuthorMailCollector class
    Tries to find the program user mail, as accuratly as possible.

    Put the functions alphabetical order in the same order as their importance.
"""

# system
import getpass
import os
import socket
from subprocess import Popen, PIPE, CalledProcessError
# parent class
from projy.collectors.Collector import Collector


class AuthorMailCollector(Collector):
    """ The AuthorMailCollector class. """

    def __init__(self):
        self.author_mail = None


    def author_mail_from_git(self):
        """ Get the author mail from git information. """
        try:
            # launch git command and get answer
            cmd = Popen(["git", "config", "--get", "user.email"], stdout=PIPE)
            stdoutdata = cmd.communicate()
            if (stdoutdata[0]):
                self.author_mail = stdoutdata[0].rstrip(os.linesep)
        except ImportError:
            pass
        except CalledProcessError:
            pass
        except OSError:
            pass

        return self.author_mail


    def author_mail_from_system(self):
        """ Get the author mail from system information.
            It is probably often innacurate.
        """
        self.author_mail = getpass.getuser() + '@' + socket.gethostname()
        return self.author_mail
