# -*- coding: utf-8 -*-
""" Main Collector class. """

# system
import inspect


class Collector:
    """ The Collector class. """

    def __init__(self):
        pass


    def collect(self):
        """ Select the best suited data of all available in the subclasses.
            In each subclass, the functions alphabetical order should
            correspond to their importance.
            Here, the first non null value is returned.
        """
        class_functions = []
        for key in self.__class__.__dict__.keys():
            func = self.__class__.__dict__[key]
            if (inspect.isfunction(func)):
                class_functions.append(func)

        functions = sorted(class_functions, key=lambda func: func.__name__)
        for function in functions:
            value = function(self)
            if value:
                return value
