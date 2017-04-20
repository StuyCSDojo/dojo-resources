.. |br| raw:: html

   <br />

.. _installation_programming_tools_emacs:

Installing Emacs
================

*Written by PChan on 2017-03-14*

* :ref:`installation_programming_tools_emacs_linux`
* :ref:`installation_programming_tools_emacs_mac_osx`
* :ref:`installation_programming_tools_emacs_windows`

  * :ref:`installation_programming_tools_emacs_windows_x86`
  * :ref:`installation_programming_tools_emacs_windows_x64`
  
.. _installation_programming_tools_emacs_linux:

Linux
-----
We will provide instructions for Fedora and Debian systems.  We are assuming that users of other distros
would know how to install Emacs themselves.

* For Ubuntu/Debian/Mint:

  * For the latest stable version:
    ::

       $ sudo apt-get install emacs

  * For the latest development version (Ubuntu only):

    * Try to add the Ubuntu Elisp ppa:
      ::

	 $ sudo add-apt-repository ppa:ubuntu-elisp/ppa

    * If you get ``sudo: add-apt-repostiory: command not found``, run the following:
      ::

	 $ sudo apt-get install software-properties-common

      Try to add the Ubuntu Elisp ppa again
    * Execute the following commands to update the package listing and install Emacs
      ::
	 
	 $ sudo apt-get update
	 $ sudo apt-get install emacs-snapshot emacs-snapshot-el
    * Optional: Allow you to execute ``emacs-snapshot`` by running ``emacs``
      ::

	 $ sudo ln -s /usr/bin/emacs-snapshot /usr/bin/emacs
    * Run Emacs via the following command:
      |br|
      Do note that the ``&`` is only necessary when running the program in the background.
      ::

	 $ emacs-snapshot &     // if you did not run the optional step
	 $ emacs &              // if you did run the optional step

    * Check out the :ref:`tutorials_programming_tools_emacs_introduction_to_emacs` guide for pointers on
      using Emacs
	 
* For Fedora:

  * Install Emacs 24 via the following commands:
    ::

       $ sudo dnf install emacs     // on Fedora 22 and higher
       $ sudo yum install emacs     // on Fedora 21 and lower
  * Run Emacs via the following command:
    |br|
    Do note that the ``&`` is only necessary when running the program in the background.
    ::

       $ emacs &

  * Check out the :ref:`tutorials_programming_tools_emacs_introduction_to_emacs` guide for pointers on
    using Emacs
  
.. _installation_programming_tools_emacs_mac_osx:

Mac OSX
-------
We will be installing Emacs via Homebrew.  For instructions on how to install Homebrew, check the
:ref:`installation_system_tools_homebrew` guide.

After you have installed Homebrew:
::

   $ brew update
   $ brew tap railwaycat/emacsmacport
   $ brew install emacs-mac

Run Emacs via the following command:
::

   $ emacs-mac &

Check out the :ref:`tutorials_programming_tools_emacs_introduction_to_emacs` guide for pointers on using
Emacs.
   
.. _installation_programming_tools_emacs_windows:

Windows
-------
Check the `OS version that you are running <http://support.microsoft.com/kb/827218/en-US>`_, then
determine which set of instructions to follow.

.. _installation_programming_tools_emacs_windows_x86:

32-bit (x86)
^^^^^^^^^^^^
1. Download Emacs from `here <https://ftp.gnu.org/gnu/emacs/windows/>`_.  Choose the latest version ending
   with: ``i686-w64-mingw32.zip``.
2. Right click on the zip file, and choose the ``Extract All`` option
3. To run Emacs, navigate to ``emacs/bin`` under the newly extracted folder and double-click on
   runemacs.exe.
4. Check out the :ref:`tutorials_programming_tools_emacs_introduction_to_emacs` guide for pointers on
   using Emacs
   
.. _installation_programming_tools_emacs_windows_x64:

64-bit
^^^^^^
1. Download `Emacs <https://github.com/zklhp/emacs-w64/releases>`_.  Any of the links under the
   download section should be fine, but if you are not sure, pick the one ending with ``-Og.7z``
2. Extract the downloaded file, here is `a free archiver <http://www.7-zip.org/>`_.
3. To run Emacs, navigate to ``emacs/bin`` under the newly extracted folder and double-click on
   runemacs.exe.
4. Check out the :ref:`tutorials_programming_tools_emacs_introduction_to_emacs` guide for pointers on
   using Emacs
