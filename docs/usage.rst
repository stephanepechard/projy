.. _usage-label:

Usage
=====
As an example, let's create a Python package. The Projy template mostly
follows recommandations from `The Hitchhiker’s Guide to Packaging
<http://guide.python-distribute.org/>`_.


An example
----------
Use simply::

    $ projy PythonPackage TowelStuff

In the same directory as you typed this command, you now have a
*TowelStuff* directory, with the following structure::


    TowelStuff/
        bin/
        bootstrap
        CHANGES.txt
        docs/
            index.rst
        LICENSE.txt
        MANIFEST.in
        README.txt
        setup.py
        towelstuff/
            __init__.py


Each file has been created with a specific template, so the package is fully
functional, yet empty. Now, let's give a little explanation on each file.
You can find `further information here <http://guide.python-distribute.org/creation.html>`_.


*bin/*, *docs/* and *towelstuff/* directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Three directories are created by default:
 * `bin/ <http://guide.python-distribute.org/creation.html#bin-description>`_
   contains your package's scripts ;
 * `docs/ <http://guide.python-distribute.org/creation.html#docs-description>`_,
   contains the documentation you write for the package. A primary *index.rst*
   file waits for you to write into it. Yes, it uses
   `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ format.
 * `towelstuff/ <http://guide.python-distribute.org/creation.html#towelstuff-description>`_,
   is where you put the files of your package. It is the lower case version
   of the project name. By default, it already contains an empty *__init__.py* file.

See the links for more information.


bootstrap
^^^^^^^^^
This file is a little treat, not present in `The Hitchhiker’s Guide to Packaging
<http://guide.python-distribute.org/>`_. Using the ``BootstrapScriptFileTemplate``
template, it is a simple bash file creating a virtual environment easily.
Use it with a simple::

    $ source bootstrap

By default, it installs three packages from `pypi <http://pypi.python.org/>`_:
 * `nose <http://nose.readthedocs.org/en/latest/>`_ is "nicer testing for Python" ;
 * `pylint <http://pypi.python.org/pypi/pylint>`_, a Python code static checker ;
 * `sphinx <http://sphinx.pocoo.org>`_, the Python documentation generator.

Everything you need to write quality code :-) Of course, you can add any other
package you may need, it's up to you. You can even externalize this list of package to a
`requirement file <http://www.pip-installer.org/en/latest/requirements.html>`_.


CHANGES.txt
^^^^^^^^^^^
The template of the `CHANGES.txt file <http://guide.python-distribute.org/creation.html#changes-txt-description>`_
simply contains::

    v<version>, <date> -- Initial release.


LICENSE.txt
^^^^^^^^^^^
By default, the Python package template contains the GPL v3 as *LICENSE.txt*.
Change it as your convenience.


MANIFEST.in
^^^^^^^^^^^
The `manifest <http://guide.python-distribute.org/creation.html#manifest-in-description>`_
is an important file that contains this::

    include CHANGES.txt
    include LICENSE.txt
    include MANIFEST.in
    include README.txt
    recursive-include bin *
    recursive-include docs *
    recursive-include towelstuff *


README.txt
^^^^^^^^^^
The usual `README file <http://guide.python-distribute.org/creation.html#readme-txt-description>`_,
written in `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ format.


setup.py
^^^^^^^^
The `setup.py <http://guide.python-distribute.org/creation.html#setup-py-description>`_
file created from the template contains:

.. code-block:: python
    :linenos:

    # -*- coding: utf-8 -*-
    """ $project setup.py script """

    # system
    from distutils.core import setup
    from os.path import join, dirname


    setup(
        name='TowelStuff',
        version='0.1.0',
        author='Stéphane Péchard',
        author_email='stephanepechard@provider.com',
        packages=['towelstuff','towelstuff.test'],
        url='http://',
        license='LICENSE.txt',
        long_description=open(join(dirname(__file__), 'README.txt')).read(),
        install_requires=[''],
        test_suite='towelstuff.test',
    )


Options
-------
Projy comes also with one command line option.


Listing templates
^^^^^^^^^^^^^^^^^
Type::

    $ projy -l

and you'll see the list of available templates in your installation.
That's an easy way to copy/paste the name of the template you want to use next.

