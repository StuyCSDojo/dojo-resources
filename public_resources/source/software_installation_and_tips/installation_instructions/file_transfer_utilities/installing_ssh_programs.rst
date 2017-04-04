.. _installation_file_transfer_utilities_ssh_programs:

Installing SSH Programs
=======================

*Written by PChan on 2017-03-17*
   
* :ref:`installation_file_transfer_utilities_ssh_programs_installing_git_bash`
* :ref:`installation_file_transfer_utilities_ssh_programs_installing_winscp`
* :ref:`installation_file_transfer_utilities_ssh_programs_installing_filezilla`

  * :ref:`installation_file_transfer_utilities_ssh_programs_installing_filezilla_linux`
  * :ref:`installation_file_transfer_utilities_ssh_programs_installing_filezilla_mac_osx`

.. _installation_file_transfer_utilities_ssh_programs_installing_git_bash:

Installing Git Bash
-------------------
.. note::
   Git Bash is a terminal based program that is recommended to APCS students (and beyond) along with
   others who wish to practice their terminal skills on Windows.

* Download the `installer for Git Bash <https://git-for-windows.github.io/>`_
* Run the executable; if you are not sure, follow the pointers below

  * On the page with five checkboxes, check everything but **Git GUI Here**
  * On the screen for adjusting path environment, select the third one
  * On the screen for choosing CR/LF, select the first one
  * On the screen for choosing the terminal emulator, select **Use MinTTY**
  * On the screen for configuring extra options, check all three
  * Click Install

.. _installation_file_transfer_utilities_ssh_programs_installing_winscp:

Installing WinSCP
-----------------
.. note::
   WinSCP is a graphical program and is recommended for Intro students.
   
WinSCP is a file-transfer program that is only available on Windows.  If you need a graphical program on a
Unix machine, you would need to follow the :ref:`installation_file_transfer_utilities_ssh_programs_installing_filezilla` guide.

1. Download the `WinSCP program <https://winscp.net/eng/download.php>`_ by choosing the
   **Installation package** link
2. Execute the program that you have just downloaded
3. Select the language the program should utilize and click *OK*
4. After reviewing the license on the **License Agreement** screen, click *Accept*
5. Select *Next* on the User interface style page
6. On the **Ready to Install screen**, click *Install* to begin the installation process
7. Restart the machine when it is done for full functionality of WinSCP.

.. _installation_file_transfer_utilities_ssh_programs_installing_filezilla:

Installing FileZilla
--------------------
.. note::
   FileZilla is a graphical program and is recommended for Intro students.

FileZilla is a cross-platform graphical file-transfer program.  For Windows Users, it is recommended to
install WinSCP instead of FileZilla because it takes care of Unix LF vs Windows CRLF.

.. _installation_file_transfer_utilities_ssh_programs_installing_filezilla_linux:

Linux
^^^^^
We will provide instructions for Fedora and Debian systems.  We are assuming that users of other distros would know how to install Filezilla themselves.

* For Ubuntu/Debian/Mint, run the following command in the terminal:
  ::

     $ sudo apt-get install filezilla

  To run FileZilla after the installation is complete, press the ``win`` button (key with floating window picture), type filezilla, and click on the first option.

* For Fedora, run the following command in the terminal:
  ::

     $ sudo dnf install filezilla    // on Fedora 22 and higher
     $ sudo yum install filezilla    // on Fedora 21 and lower

.. note::
   Users of Fedora 21 and lower might need to enable the `RPM Fusion repo <https://rpmfusion.org/>`_.

.. _installation_file_transfer_utilities_ssh_programs_installing_filezilla_mac_osx:

Mac OSX
^^^^^^^
To install FileZilla on Mac...

1. Download the `package for Mac OSX users <https://filezilla-project.org/download.php?platform=osx>`_
2. If you are using Safari, the package will automatically be extracted
   If you are not using Safari, you will have to manually extract the archive if you are using a different browser.
3. Run FileZilla by double-clicking on the extracted application bundle
