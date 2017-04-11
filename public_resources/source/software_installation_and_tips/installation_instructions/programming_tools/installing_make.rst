.. _installation_programming_tools_make:

Installing Make
===============

*Written by PChan on 2017-04-06*

* :ref:`installation_programming_tools_make_linux`
* :ref:`installation_programming_tools_make_mac_osx`
* :ref:`installation_programming_tools_make_windows`

  .. highlight:: none

.. _installation_programming_tools_make_linux:

Linux
-----
* On Ubuntu/Debian/Mint
  ::

     $ sudo apt-get install build-essential

* On Fedora 21
  ::

     // minimalist approach
     $ sudo yum install make automake gcc gcc-c++ kernel-devel

     // full-blown approach, so that you do not have to bother with this again (takes up more space)
     $ sudo yum groupinstall "DevelopmentTools" "Development Libraries"

* On Fedora 23
  ::

     // try
     $ sudo dnf install @development-tools

     // otherwise
     $ sudo dnf group install "C Development Tools and Libraries"
     
.. _installation_programming_tools_make_mac_osx:

Mac OSX
-------
Generally, Mac OSX comes with make preinstalled.  To check to see if this is the case, run the following
command in the terminal:
::

   $ make --version

If you do not get an error, you are good to go.  Otherwise, run the following command:
::

   $ xcode-select --install

.. _installation_programming_tools_make_windows:

Windows
-------
* Download the `MinGW installation app <https://sourceforge.net/projects/mingw/files/latest/download>`_
* Run the executable
* Read and accept the license agreement
* Select **Current Package**
* When choosing the components to install, you'll need:

  * **MinGW base tools**
  * **g++ compiler**
  * **MinGW Make**
* Read the :ref:`tutorials_system_windows_path_modifying_windows_path` guide and add ``C:\MinGW\bin`` to
  your path
* Run the following command in a command prompt with administrative privileges:
  ::

     C:\Users\Username> copy C:\MinGW\bin\mingw32-make.exe C:\MinGW\bin\make.exe

.. highlight:: python
