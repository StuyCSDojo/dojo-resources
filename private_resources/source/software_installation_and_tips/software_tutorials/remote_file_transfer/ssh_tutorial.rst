Introduction to SSH
===================

*Written by PChan on 2017-03-16*

* :ref:`tutorial_remote_file_transfer_ssh_what_is_ssh`
* :ref:`tutorial_remote_file_transfer_ssh_syntax_of_ssh`
* :ref:`tutorial_remote_file_transfer_ssh_stuycs_ssh_credentials`
* :ref:`tutorial_remote_file_transfer_ssh_stuycs_ssh_hostname`
* :ref:`tutorial_remote_file_transfer_ssh_stuycs_examples`

.. _tutorial_remote_file_transfer_ssh_what_is_ssh:

What is SSH
-----------
SSH stands for **S**\ ecure **SH**\ ell.  It allows you to access files and programs on remote computers
securely.  While the ssh executable is preinstalled on Unix machines, you would need to install a
third-party program on Windows machines.  Follow the instructions in the
:ref:`installation_file_transfer_utilities_ssh_programs` guide to install Git Bash.

.. _tutorial_remote_file_transfer_ssh_syntax_of_ssh:

Syntax of SSH
-------------
The most basic syntax for the ``ssh`` command is:
::

   $ ssh username@hostname

.. _tutorial_remote_file_transfer_ssh_stuycs_ssh_credentials:

StuyCS SSH Credentials
----------------------
When accessing your StuyCS account remotely, you will need to know your username and password:
  * Username

    * If you are Class of 2019 or later, your username is the first part of your stuy.edu email address
      (everything before the '@')
    * If you are Class of 2018 or earlier, your username is your *firstname.lastname*
  * Password

    * This is simply the password to your StuyCS account

.. _tutorial_remote_file_transfer_ssh_stuycs_ssh_hostname:

StuyCS SSH Hostname
-------------------      
Due to a change in ISP, access from outside is not restricted to ``clyde.stuy.edu``.  Therefore, from
outside the school, you would run the following command:
::

   $ ssh <username>@clyde.stuy.edu

In the case that the DNS server is messed up, the IP address for ``clyde.stuy.edu`` is ``24.103.0.186``.
   
After you have connected to ``clyde.stuy.edu``, it is in your best interest to ssh into one of the lab
machines.  Here are the hostnames for the four main servers along with their IP address (in the case that
the DNS server is messed up)
::

   homer.stuy.edu  (149.89.150.100)
   bart.stuy.edu   (149.89.151.100)
   lisa.stuy.edu   (149.89.160.100)
   marge.stuy.edu  (149.89.161.100)

.. warning::
   Never **EVER** do your work directly on ``clyde.stuy.edu``.  Make sure to switch to a different machine
   as soon as you are connected.
   
In addition to the four aforementioned hostnames, you can also access the first five machines in each room
where x is in the range of 1-5 (inclusive)
::

   149.89.150.10x
   149.89.151.10x
   149.89.160.10x
   149.89.161.10x

.. important::
   Do **NOT** keep the ssh connection alive longer than you need to!!

.. _tutorial_remote_file_transfer_ssh_stuycs_examples:

StuyCS Examples
---------------
.. note::
   Comments begin after ``//`` and are used to explain the command on that line.

Here are some examples:
::

   $ ssh patrick.chan@clyde.stuy.edu      // To connect from outside
   $ ssh homer.stuy.edu                   // Switch to different lab machine

::

   $ ssh patrick.chan@clyde.stuy.edu      // To connect from the outside
   $ ssh 149.89.150.100                   // Connect to homer with IP address
   
