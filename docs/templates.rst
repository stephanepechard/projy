Available templates
===================
Here is a list of all the templates, but also collectors, integrated into
Projy at the moment. Of course, anyone can propose new templates,
they'll be integrated into Projy.


Project templates
-----------------
Project templates are used to create a files/directories structure. That's the
second argument of the command line. For this list, the projects we create are
all called ``TowelStuff``. They are ordered by the programming
language they use.


LaTeX
^^^^^
These are `LaTeX <http://www.latex-project.org/>`_ templates.


LaTeX book
""""""""""
The command::

    $ projy LaTeXBook TowelStuff

produces::

    TowelStuff/
        TowelStuff.tex          - LaTeXBookFileTemplate
        references.bib          - BibTeXFileTemplate
        Makefile                - LaTeXMakefileFileTemplate

Note: the ``Makefile`` uses `Latexmk
<http://www.phys.psu.edu/~collins/software/latexmk-jcc/>`_.


Python
^^^^^^
These are `Python <http://python.org>`_ templates.


Python package
""""""""""""""
The command::

    $ projy PythonPackage TowelStuff

produces::

    TowelStuff/
        bootstrap               - BootstrapScriptFileTemplate
        CHANGES.txt             - PythonPackageCHANGESFileTemplate
        LICENSE.txt             - GPL3FileTemplate
        MANIFEST.in             - PythonPackageMANIFESTFileTemplate
        README.txt              - READMEReSTFileTemplate
        setup.py                - PythonPackageSetupFileTemplate

    TowelStuff/docs/
        index.rst

    TowelStuff/towelstuff/
        __init__.py


Python script
"""""""""""""
The command::

    $ projy PythonScript TowelStuff

produces::

    TowelStuff/
        TowelStuff.py           - PythonScriptFileTemplate


Bootstrap
^^^^^^^^^
The command::

    $ projy Bootstrap TowelStuff

produces::

    /
        bootstrap               - BootstrapScriptFileTemplate

Yes, the name has no impact on the produced file.
Don't hesitate to make it short!


Projy itself!
^^^^^^^^^^^^^
Finally, a bit of a special template, which lets you create a Projy template
and an empty file template from Projy itself. Call it meta if you want :-)
See :ref:`extend-label` to know how such templates are meant to be written.

The command::

    $ projy ProjyTemplate TowelStuff

produces::

    /
        TowelStuffTemplate.py       - ProjyTemplateFileTemplate
        TowelStuffFileTemplate.txt


File templates
--------------

LaTeX files
^^^^^^^^^^^
* :download:`BibTeXFileTemplate <../projy/templates/BibTeXFileTemplate.txt>`
* :download:`LaTeXBookFileTemplate <../projy/templates/LaTeXBookFileTemplate.txt>`
* :download:`LaTeXMakefileFileTemplate <../projy/templates/LaTeXMakefileFileTemplate.txt>`


Python files
^^^^^^^^^^^^
* :download:`ProjyTemplateFileTemplate <../projy/templates/ProjyTemplateFileTemplate.txt>`
* :download:`PythonPackageCHANGESFileTemplate <../projy/templates/PythonPackageCHANGESFileTemplate.txt>`
* :download:`PythonPackageMANIFESTFileTemplate <../projy/templates/PythonPackageMANIFESTFileTemplate.txt>`
* :download:`PythonPackageSetupFileTemplate <../projy/templates/PythonPackageSetupFileTemplate.txt>`
* :download:`PythonScriptFileTemplate <../projy/templates/PythonScriptFileTemplate.txt>`


Bash files
^^^^^^^^^^
* :download:`BootstrapScriptFileTemplate <../projy/templates/BootstrapScriptFileTemplate.txt>`


Text files
^^^^^^^^^^
* :download:`READMEReSTFileTemplate <../projy/templates/READMEReSTFileTemplate.txt>`


Licenses
^^^^^^^^
* :download:`AGPL3FileTemplate <../projy/templates/AGPL3FileTemplate.txt>`
* :download:`ApacheLicenseFileTemplate <../projy/templates/ApacheLicenseFileTemplate.txt>`
* :download:`BSDLicenseFileTemplate <../projy/templates/BSDLicenseFileTemplate.txt>`
* :download:`DWTFYWTPLFileTemplate <../projy/templates/DWTFYWTPLFileTemplate.txt>`
* :download:`GPL2FileTemplate <../projy/templates/GPL2FileTemplate.txt>`
* :download:`GPL3FileTemplate <../projy/templates/GPL3FileTemplate.txt>`
* :download:`LaTeX3LicenseFileTemplate <../projy/templates/LaTeX3LicenseFileTemplate.txt>`
* :download:`LGPL3FileTemplate <../projy/templates/LGPL3FileTemplate.txt>`
* :download:`MITLicenseFileTemplate <../projy/templates/MITLicenseFileTemplate.txt>`
* :download:`MPL2FileTemplate <../projy/templates/MPL2FileTemplate.txt>`
* :download:`PythonLicense2FileTemplate <../projy/templates/PythonLicense2FileTemplate.txt>`


Collectors
----------
Here is the list of currently available collectors:

* :download:`AuthorCollector <../projy/collectors/AuthorCollector.py>`
* :download:`AuthorMailCollector <../projy/collectors/AuthorMailCollector.py>`

