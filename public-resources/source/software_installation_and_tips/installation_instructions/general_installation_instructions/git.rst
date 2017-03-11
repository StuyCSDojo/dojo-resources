Installing Git
==============

.. |br| raw:: html

   <br />

What Operating System Are You Using?
------------------------------------
  * :ref:`git_linux`
  * :ref:`git_mac_osx`
  * :ref:`git_windows`

.. _git_linux:

Linux
^^^^^
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
  
.. _git_mac_osx:

Mac OSX
^^^^^^^
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
    
.. _git_windows:

Windows
^^^^^^^
For Windows, we are going to install Git Bash which provides a Bash emulation with Git prebundled.

* Download the `installer for Git Bash <https://git-for-windows.github.io/>`_
* Run the executable; if you are not sure, follow the pointers below

  * On the page with four checkboxes, checking at least one of the first two is recommended; the last two
    checkboxes are useful, but not necessary
  * On the screen for adjusting path environment, select the third one
  * On the screen for choosing CR/LF, select the first one
* Run Git Bash
* Configure your Git username and email
  ::

     $ git config --global user.name "<your name>"    // your name in quotes
     $ git config --global user.email "<your email>"  // your git email in quotes
