Quickstart
================

.. note:: 

    Type hinting is used in all examples to increase readability.

UNIX commands in python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To get started using ``commandio`` in either a python project or just in python:

.. code-block:: python

    from commandio.logutil import LogFile
    from commandio.command import Command

    # Create log file object
    log_file: LogFile = LogFile("example.log", level="info")

    # Command to be run on the command line
    cmd: Command = Command("touch test.txt")

    # Check if the required dependency is installed
    # This will raise a DependencyError if touch is 
    #   not installed or in your system PATH variable.
    cmd.check_dependency()

    # The command was executed in a subshell
    # There should now be a file in the working 
    #   directory called test.txt
    cmd.run(log=log_file)


Similarly, the above commands could also be used without creating a ``LogFile`` object
for the sake of convenience:

.. code-block:: python

    from commandio.command import Command

    # Command to be run on the command line
    cmd: Command = Command("touch test.txt")

    # Check if the required dependency is installed
    # This will raise a DependencyError if touch is 
    #   not installed or in your system PATH variable.
    cmd.check_dependency()

    # The command was executed in a subshell
    # There should now be a file in the working 
    #   directory called test.txt
    cmd.run(log=log_file)

Logging
~~~~~~~~~

Writing log files can also be done easily by just performing the following:

.. code-block:: python

    from commandio.logutil import LogFile

    # Create log file object
    log_file: LogFile = LogFile("example.log", level="info")

    log_file.info("This is a test.")

    log_file.warning("This is a warning.")
