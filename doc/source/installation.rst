Installation
================

.. caution:: 

    Although this package is installable on Windows platforms, the pairity of ``commandio``'s utilities
    is not one-to-one in comparision to UNIX platforms.

    This is becuase `shlex <https://docs.python.org/3/library/shlex.html#shlex.quote>`_ (one of ``commandio``'s dependencies) is primarily designed for UNIX shells,
    and thus is not guaranteed to be safe (i.e. prevent/mitigate command injection vulnerabilities) on non-POSIX compliant shells (e.g. Windows).

    Use this package with caution on Windows platforms.

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
    
    1. It assumes that the project is also a ``git`` repository.
    2. The import path of ``commandio``'s modules will be slightly different if not setup from ``pip``.

