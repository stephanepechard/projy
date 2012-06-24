.. _extend-label:

Extending Projy
===============
Writing new templates and data collectors is easy. Let's continue reviewing our example.


Project templates
-----------------
Here is the project template used to create a Python package:


.. literalinclude:: ../projy/templates/PythonPackageTemplate.py
   :linenos:


To write a new template, you have to specify four parts:
    * the name of the template, which is the name of the class ;
    * the ``directories``, ``files`` and ``substitutes`` functions.

When writing a new template, you can use the ``self.project_name`` variable
which contains the name of the project as you typed it.
In our example, it is ``TowelStuff``.


Name of the template
^^^^^^^^^^^^^^^^^^^^
Here it is simply ``PythonPackageTemplate``. This is the name you
type in the command line plus ``Template`` at the end. The created template
inherits from the father of all templates, the ``ProjyTemplate`` class.


The *directories* function
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. function:: directories()

    Returns a tuple containing all the names of the directories to be created.

   :rtype: list of directory names

In our example, the created directories are ``TowelStuff``, ``TowelStuff/towelstuff`` and ``TowelStuff/docs``.


The *files* function
^^^^^^^^^^^^^^^^^^^^
.. function:: files()

    This function should return a tuple containing three informations for each file:
        * the directory the file is in. It is defined as in `the directories function`_ ;
        * the name of the file ;
        * the template of the file, which is not the same as the project template.
          See `File templates`_.

   :rtype: list of file names

In our example, eight files are created:
    * ``bootstrap`` created from ``BootstrapScriptFileTemplate`` ;
    * ``CHANGES.txt`` created from ``PythonPackageCHANGESFileTemplate`` ;
    * ``LICENSE.txt`` created from ``GPL3FileTemplate`` ;
    * ``MANIFEST.in`` created from ``PythonPackageMANIFESTFileTemplate`` ;
    * ``README.txt`` created from ``READMEReSTFileTemplate`` ;
    * ``setup.py`` created from ``PythonPackageSetupFileTemplate`` ;
    * ``__init__.py`` into the ``TowelStuff/towelstuff`` directory, created from ``PythonPackageSetupFileTemplate`` ;
    * ``index.rst`` into the ``TowelStuff/docs`` directory, created empty.

Details on the content of each file is given on :ref:`usage-label`.


The *substitutes* function
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. function:: substitutes()

    This function should return a dictionary containing the string substitutions
    used in the template.

   :rtype: list of file names

In our example, the substitutions made in all the created files are:
    * ``$project`` is replaced by ``TowelStuff`` ;
    * ``$project_lower`` is replaced by ``towelstuff`` ;
    * ``$date`` is replaced by the current date, in the format 2012-11-23 ;
    * ``$author`` is replaced by what returns the ``AuthorCollector`` ;
    * ``$author_email`` is replaced by what returns the ``AuthorMailCollector`` ;


File templates
--------------
From all the templated files we created, let's see how the
``PythonPackageSetupFileTemplate`` is made. Here is its content:

.. literalinclude:: ../projy/templates/PythonPackageSetupFileTemplate.txt
   :linenos:

It is simply the file you want to create with the variables that will
be substitute in the creation process. Each variable should begin
by ``$`` as described in the `Template
<http://docs.python.org/library/string.html?highlight=template#string.Template>`_
mechanism. Nothing fancy on this side, as you can see.


Data collectors
---------------
A data collector, as its name suggest, collects data. It is used by
Projy to complete the `File templates`_. Here is the data collector
for the author data:

.. literalinclude:: ../projy/collectors/AuthorCollector.py
   :linenos:

A data collector defines as many functions as necessary. In the
case of the author, two ways of finding it are written. The first uses
`git <http://git-scm.com/>`_. As many users of Projy would probably
use it, chances are that its configuration will reflect the author's
information. As a fallback in case `git <http://git-scm.com/>`_ does
not return the wanted data, the user name is taken as
the system current user name. There are probably other methods
to find it, so feel free to propose some more.

Functions are treated in the alphabetical order, which means that the
most accurate functions should come before the least accurate ones.
Of course, one may not always know what the most accurate way of finding
a particular data is. Be smart then!

