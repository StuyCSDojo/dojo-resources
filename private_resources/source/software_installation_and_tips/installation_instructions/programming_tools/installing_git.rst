.. _installation_programming_tools_git:

Installing Git
==============

*Written by PChan on 2017-03-11*

* :ref:`installation_programming_tools_git_linux`
* :ref:`installation_programming_tools_git_mac_osx`
* :ref:`installation_programming_tools_git_windows`

.. _installation_programming_tools_git_linux:

Linux
-----
We will provide instructions for Fedora and Debian systems.  We are assuming that users of other distros
would know how to install Git themselves.

* For Ubuntu/Debian/Mint:

  * Try to add the Git ppa:
    ::

       $ sudo add-apt-repository ppa:git-core/ppa
  * If you get ``sudo: add-apt-repository: command not found``, run the following:
    ::

       $ sudo apt-get install software-properties-common
  * Run the command to add the Git ppa again
    ::

       $ sudo add-apt-repository ppa:git-core/ppa
  * Update your package listing
    ::

       $ sudo apt-get update
  * Install Git
    ::

       $ sudo apt-get install git
  * Verify that Git is installed successfully
    ::

       $ git --version
       git version 2.11.0        // sample output
  * Configure your Git username and email
    ::

       $ git config --global user.name "<your name>"    // your name in quotes
       $ git config --global user.email "<your email>"  // your git email in quotes
  * Check out the :ref:`tutorials_programming_tools_git_introduction_to_git` guide for pointers on using
    Git

* For Fedora:

  * Check if Git is installed
    ::

       $ git --version
       git version 2.11.0        // sample output if Git is installed
       git: command not found    // sample output if Git is not installed
  * Install Git if necessary
    ::

       $ sudo dnf install git    // on Fedora 22 and higher
       $ sudo yum install git    // on Fedora 21 and lower
  * Verify that Git is installed successfully
    ::

       $ git --version
       git version 2.11.0        // sample output

  * Configure your Git username and email
    ::

       $ git config --global user.name "<your name>"    // your name in quotes
       $ git config --global user.email "<your email>"  // your git email in quotes
  * Check out the :ref:`tutorials_programming_tools_git_introduction_to_git` guide for pointers on using
    Git

.. _installation_programming_tools_git_mac_osx:

Mac OSX
-------
Depending on your setup, Git may already already be installed.  To check, run the following command in the
terminal:

::

   $ git --version
   git version 2.7.0 (Apple Git-66)  // sample output

.. note::
   Even if Git is already installed, you might want to install a newer version of Git which may have new
   features, security fixes, and etc.

There are a couple of ways to installing Git:

* Homebrew

  If you are not sure if Homebrew is installed, check :ref:`installation_system_tools_homebrew`.

  * Install Git via Homebrew
    ::

       $ brew install git
  * Verify that Git is installed
    ::

       $ git --version
       git version 2.9.2        // sample output
  * Configure your Git username and email
    ::

       $ git config --global user.name "<your name>"    // your name in quotes
       $ git config --global user.email "<your email>"  // your git email in quotes
  * Check out the :ref:`tutorials_programming_tools_git_introduction_to_git` guide for pointers on using
    Git

* MacPort

  * Update MacPorts
    ::

       $ sudo port selfupdate
  * Search for Git and variants
    ::

       $ port search git
       $ port variants git
  * Install Git with bash completion and docs
    ::

       $ sudo port install git +bash_completion+doc
  * Verify that Git is installed
    ::

       $ git --version
       git version 2.9.2        // sample output
  * Configure your Git username and email
    ::

       $ git config --global user.name "<your name>"    // your name in quotes
       $ git config --global user.email "<your email>"  // your git email in quotes
  * Check out the :ref:`tutorials_programming_tools_git_introduction_to_git` guide for pointers on using
    Git

.. _installation_programming_tools_git_windows:

Windows
-------
For Windows, we are going to install Git Bash which provides a Bash emulation with Git prebundled.

* Check the `version of your OS
  <https://support.microsoft.com/en-us/help/13443/windows-which-operating-system>`_ and
  download the appropriate `installer for Git Bash <https://git-for-windows.github.io/>`_
* Run the executable; if you are not sure, follow the pointers below

  * On the page with five checkboxes, check everything, "but Git GUI HERE"
  * On the screen for adjusting path environment, select the third one
  * On the screen for choosing CR/LF, select the first one
  * On the screen for choosing the terminal emulator, select "Use MinTTY"
  * On the screen for configuring extra options, check all three
  * Click Install
* Run Git Bash
* Configure your Git username and email
  ::

     $ git config --global user.name "<your name>"    // your name in quotes
     $ git config --global user.email "<your email>"  // your git email in quotes
* Check out the :ref:`tutorials_programming_tools_git_introduction_to_git` guide for pointers on using
  Git
