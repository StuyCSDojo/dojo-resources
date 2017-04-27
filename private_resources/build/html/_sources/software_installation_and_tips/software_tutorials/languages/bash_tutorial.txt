Introduction to Bash
====================

*Written by Shakil Rafi on 2017-01-26*

* :ref:`tutorials_languages_bash_what_is_bash`
* :ref:`tutorials_languages_bash_how_to_get_bash`
* :ref:`tutorials_languages_bash_using_bash`

  * :ref:`tutorials_languages_bash_running_bash_script`
  * :ref:`tutorials_languages_bash_utilizing_path_variable`
* :ref:`tutorials_languages_bash_writing_bash_scripts`

  * :ref:`tutorials_languages_bash_comments`
  * :ref:`tutorials_languages_bash_variables`
* :ref:`tutorials_languages_bash_controlling_flow`

  * :ref:`tutorials_languages_bash_conditionals`
  * :ref:`tutorials_languages_bash_for_loops`
  * :ref:`tutorials_languages_bash_while_loops`
* :ref:`tutorials_languages_bash_context`

.. _tutorials_languages_bash_what_is_bash:
  
What is Bash
------------
Bash is the language of the terminal. Whenever you enter a command into the terminal it is executed using
Bash.

.. _tutorials_languages_bash_how_to_get_bash:

How to get Bash
---------------
Bash is readily available to use on any Linux and Mac OSX machine. Windows has a similar toolset powering
its line and PowerShell, however it is not as comprehensive as Bash.

.. _tutorials_languages_bash_using_bash:

Using Bash
----------
Bash is generally used to make custom scripts for anything you do often. For example, let's say you always
generate a file to start your CS homework in the format:
::
   
   John Smith
   APCS1
   Period 11
   2016-01-20
   
You could write a bash script to make that file for you and then you could easily run that script each
time you start your homework instead of manually typing the template.

.. _tutorials_languages_bash_running_bash_script:

Running a Bash script
^^^^^^^^^^^^^^^^^^^^^
To run a Bash script, simply write the name of script preceded by './'. For example: ``./myscript``

.. _tutorials_languages_bash_utilizing_path_variable:

Utilizing your PATH variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
As previously stated, everything you use in your terminal is run using bash. So why don't you have to use
'./' every time you run ``ls`` to list all files and directories or ``python`` to enter a Python shell?
Well there are a bunch of scripts that are located in various directories specified in your PATH variable.
The PATH variable is held by the terminal in the format ``dir1:dir2:dir3``. Each time you open a new
terminal, these directories are scanned for scripts and they are made readily available for your use
without typing './'. For the sake of custom scripts being available in the same way, you can make a new
directory to hold your scripts and then modify your PATH variable to look through that directory using the
following commands:
::
   
   $ mkdir custom_scripts
   $ echo "export PATH=$PATH:$PWD/custom_scripts" >> ~/.bashrc

At this point, you might be asking "Why can't I just add all directories to the PATH variable?" Well, the
simple answer is that it would greatly slow down your terminal to have to look through your entire
computer for a script that would only possibly be located in a few directories. On top of that duplicate
filenames would create a larger issue. If you have two files named 'starthw' in different directories,
which one should the terminal run?

.. _tutorials_languages_bash_writing_bash_scripts:

Writing bash scripts
--------------------
Writing a bash script is fairly simple. To start off, you have to write the header of the file:
::
   
   #! /bin/bash
   
As for the rest, it is essentially just a list of commands for the terminal to run. For example, the
script below would make a directory named 'foo' and then print out 'bar'.
::
   
   #! /bin/bash
   mkdir foo
   echo bar

.. _tutorials_languages_bash_comments:
   
Comments
^^^^^^^^
To write a comment in bash, simply add a '#' preceding the comment like so:
::
   
   foo
   bar #this is a comment

.. _tutorials_languages_bash_variables:
   
Storing and accessing variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To store a variable, simply write the variable name and value with an equal sign between them like so:
::

   varName=value
   
.. note::
   When storing a variable, you may not change the spacing; there must be no whitespace on either side of the
   equal sign.

You can also store the output of a command using the following format:
::

   varName=$(command)

To access a variable you have stored, you can't simply write its name like you could in most languages.
Instead, you have to add a '$' before the variable name like so:
::

   echo $varName

.. _tutorials_languages_bash_controlling_flow:
   
Controlling flow
----------------
You might find yourself requiring different functionality depending on the usage of your script. For
example, you might only want to run the command ``foo`` if the current directory has a file named ``bar``.
Well Bash has conditionals and loops just like any programming language to help you out with that.

.. _tutorials_languages_bash_conditionals:

If statements
^^^^^^^^^^^^^
In bash, the syntax for an if statement is:
::
   
   if [ condition ]
   then
   #do stuff
   fi

Replace 'condition' in the above code with something that will evaluate to a boolean (true or false)
value.

Some useful operators:
::
   
   Operator      What it does            Examples
   =             Checks for equality     1 = 1 --> true
                                         "foo" = "bar" --> false
   
   !=            Checks for inequality   1 != 1 --> false
                                         "foo" != "bar" --> true
					 
   <             "Less than" operator    1 < 2 --> true
                                         2 < 1 --> false
   
   >             "Greater than" operator 1 > 2 --> true
                                         2 > 1 --> false
   
   -d dirName    Checks if dirName       -d "home/"
                 exists and if it is a
                 directory
		 
   -f fileName   Checks if fileName      -d "file.txt"
                 exists and if it is a
                 file
		 
You can also expand your conditionals using 'elif' and end them with a default 'else' statement like so:
::
   
   if [ condition1 ]
   then
   #do stuff
   elif [ condition2 ]
   then
   #do stuff
   elif [ condition3 ]
   then
   #do stuff
   else
   #do stuff
   fi

.. _tutorials_languages_bash_for_loops:
   
For loops
^^^^^^^^^
For loops in Bash work a lot like they do in Python. Their main functionality is to cycle through some
group or list like so:
::
   
   for i in $(seq 10)
   do
   #do stuff
   done
   
In the above example, ``$(seq 10)`` creates an array holding all values from 1 through 10. For loops are
generally used to complete a set of tasks a certain number of times, so using ``$(seq n)`` is the most
common way to use it.

.. _tutorials_languages_bash_while_loops:

While loops
^^^^^^^^^^^
While loops in Bash work just like they would in any programming language with the following syntax:
::
   
   while [ condition ]
   do
   #do stuff
   done

.. _tutorials_languages_bash_context:
   
It's all about context
----------------------
You can use the ``cd`` command at any point in your code for a bash script, but remember that you will
only change the directory while that script is running. In other words, you have only changed the working
directory in the context of the script. When the script is done running and it exits, all of its effects
to files and directories will remain, but any variables made or any changes to the working directory will
revert back to what they were before running the script.
