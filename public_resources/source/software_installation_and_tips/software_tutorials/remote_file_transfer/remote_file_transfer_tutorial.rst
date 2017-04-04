Introduction to Remote File Transfer
====================================

*Written by PChan on 2017-03-18*

* :ref:`network_remote_file_transfer_using_filezilla`

  * :ref:`network_remote_file_transfer_filezilla_authentication`
  * :ref:`network_remote_file_transfer_filezilla_session`
* :ref:`network_remote_file_transfer_using_winscp`

  * :ref:`network_remote_file_transfer_winscp_authentication`
  * :ref:`network_remote_file_transfer_winscp_session`
  
.. _network_remote_file_transfer_using_filezilla:

Using FileZilla
---------------
FileZilla is a graphical program that is used primarily for transferring files between a local machine and
a remote machine.  If you have not done so already, install the program following the
:ref:`installation_file_transfer_utilities_ssh_programs_installing_filezilla` guide.

.. _network_remote_file_transfer_filezilla_authentication:

Authenticating Yourself
^^^^^^^^^^^^^^^^^^^^^^^
After executing the program, the first step to connecting is to enter your credentials.  Near the top of
the program, you should see a bar like the following (yours would not have text):

.. image:: ../../images/software_tutorials/remote_file_transfer/ssh_programs/filezilla_login.png

Fill in the following information:

  * **Host**: clyde.stuycs.org
  * **Username**: the username for your StuyCS account
  * **Password**: the password for your StuyCS account
  * **Port**: 22

Lastly, click on the **Quick Connect** button. Below that, you should see the progress similar to the
image below.

.. image:: ../../images/software_tutorials/remote_file_transfer/ssh_programs/filezilla_connecting.png

.. _network_remote_file_transfer_filezilla_session:

Transferring Files with FileZilla
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
After you have successfully connected, the multi-pane panel near the bottom of the screen should be
populated similar to the following image:

.. image:: ../../images/software_tutorials/remote_file_transfer/ssh_programs/filezilla_session.png

To copy from the local machine to the remote machine, locate the file on the left pane and then simply
drag the file from the left pane to the right pane.  To copy from the remote machine to the local machine,
locate the file on the right pane and then simply drag the file from the right pane to the left pane.

.. note::
   In the file listing, ``..`` refers to the parent directory.  Click on it to go up one directory.

.. _network_remote_file_transfer_using_winscp:

Using WinSCP
------------
WinSCP is a third-party Windows-only program that is used primarily for transferring files between a local
machine and a remote machine.  If you have not done so already, install the program by following the
:ref:`installation_file_transfer_utilities_ssh_programs_installing_winscp` guide.

When you execute the program, you should see a pop up similar to the one below:

.. image:: ../../images/software_tutorials/remote_file_transfer/ssh_programs/winscp_login.jpg

.. _network_remote_file_transfer_winscp_authentication:

Authenticating Yourself
^^^^^^^^^^^^^^^^^^^^^^^
To log in, you need to fill in the following fields:

  * **Host name**: clyde.stuycs.org
  * **User name**: the username for your StuyCS account
  * **Password**: the password for your StuyCS account

Lastly, click on the Login button near the bottom of the window.  As the program attempts to connect to
the remote machine, you would see the following window detailing the progress...

.. image:: ../../images/software_tutorials/remote_file_transfer/ssh_programs/winscp_connecting.png

.. _network_remote_file_transfer_winscp_session:

Transferring Files with WinSCP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
After you successfully authenticated yourself, you should see something like the window below (with
different filenames):

.. image:: ../../images/software_tutorials/remote_file_transfer/ssh_programs/winscp_session.png

The left panel is the file listing of your local machine and the right panel is the file listing of the
remote machine.

To move files from your local machine to the remote machine, simply look for the file in the left panel
and drag it over to the right panel.  To get a file from the remote machine, simply drag the file from the
right panel to the left panel.

.. note::
   In the file listing, ``..`` refers to the parent directory.  Click on it to go up one directory.
