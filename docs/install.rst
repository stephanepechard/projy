Installation
============
If you are familiar with Python, it is strongly suggested that you install
Projy in `virtualenv <http://pypi.python.org/pypi/virtualenv>`_.


Pip and Distribute
------------------
To install Projy system-wide, just type::

    $ sudo pip install projy

If no pip available, try ``easy_install``::

    $ sudo easy_install projy


Play the game
-------------
If you want to code, hack, enhance or just understand Projy, you can get
the latest code at `Github <http://github.com/stephanepechard/projy>`_::

    $ git clone http://github.com/stephanepechard/projy

Then create the local virtualenv and install Projy into it::

    $ cd projy && make && ./venv/bin/fab install

There's also an easy::

    $ ./venv/bin/fab reinstall

to reinstall the local version of Projy, for quick testing.


Read the full manual
--------------------

To build the manual::

    $ ./venv/bin/fab build_doc

The HTML pages are then in the ``projy/docs/_build/html/`` directory.
