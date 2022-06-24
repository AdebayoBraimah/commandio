Installation
================

Using ``pip``
~~~~~~~~~~~~~~~~~~~~~

The ``commandio`` package can be installed via pip using the command:

.. code-block:: bash

    pip install commandio [--user]


The command line flag ``--user`` may need to be included depending on one's level
of access on the intended device.


Git submodule
~~~~~~~~~~~~~~~~~~~~~

Should one wish to use this package in a python project, and do not wish to install
``commandio``, then following could also be done:

.. code-block:: bash

    git submodule add https://github.com/AdebayoBraimah/commandio.git

.. warning:: 
    
    The above approach is not recommend because:
    
    1. It assumes that the project is also a git repository.
    2. The import path of ``commandio``'s modules will be slightly different if not setup from ``pip``.

.. note:: 
    
    This package only uses python built-in modules and packages and thus has no external dependencies.
