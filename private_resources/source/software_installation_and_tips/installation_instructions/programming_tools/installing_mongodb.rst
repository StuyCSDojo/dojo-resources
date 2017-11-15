Installing MongoDB
==================

*Written by PChan on 2017-04-09*

* :ref:`installation_programming_tools_mongodb_linux`

  * :ref:`installation_programming_tools_mongodb_linux_debian_based`
  * :ref:`installation_programming_tools_mongodb_linux_fedora`
* :ref:`installation_programming_tools_mongodb_mac_osx`
* :ref:`installation_programming_tools_mongodb_windows`

MongoDB is a popular, document-oriented NoSQL database that is taught in second semester of Software
Development.

.. highlight:: none

.. _installation_programming_tools_mongodb_linux:

Linux
-----
We will only be covering Debian, Ubuntu, Mint, and Fedora in this tutorial.  We trust that users of other
distros will be able to install MongoDB without much issues.

.. _installation_programming_tools_mongodb_linux_debian_based:

Debian/Ubuntu/Mint
^^^^^^^^^^^^^^^^^^
* Import the public key for the MongoDB apt repository
  ::

     $ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6

* Add the repository url to the list of sources to pull packages from:

  * On Ubuntu 12.04 & 14.04:
    ::

       $ echo "deb [ arch=amd64 ] http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-3.4.list

  * On Ubuntu 16.04:
    ::

       $ echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-3.4.list

  * On Debian 7 & 8:
    ::

       $ echo "deb http://repo.mongodb.org/apt/debian "$(lsb_release -sc)"/mongodb-org/3.4 main" | sudo tee /etc/apt/sources.list.d/mongodb-3.4.list

* Install MongoDB
  ::

     $ sudo apt-get update
     $ sudo apt-get install mongodb-org

* Start the MongoDB service
  ::

     $ sudo service mongodb start

.. important::
   The above step needs to be run each time you boot the machine (should you wish to use mongodb for that
   session)!

* Test the connection
  ::

     $ mongo
     MongoDB shell version: 3.4.2
     >> //you are now in the mongo shell

.. _installation_programming_tools_mongodb_linux_fedora:

Fedora
^^^^^^
* Add the MongoDB Yum Repository

  * Create and open the file ``/etc/yum.repos.d/mongodb.repo`` with your favorite text editor (you will
    need sudo)
    ::

       $ sudo nano /etc/yum.repos.d/mongodb.repo

  * Insert the following content
    ::

       [MongoDB]
       name=MongoDB Repository
       baseurl=http://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.2/x86_64/
       gpgcheck=0
       enabled=1

* Install MongoDB
  ::

     $ sudo yum install mongodb-org

* Start MongoDB
  ::

     $ sudo /etc/init.d/mongod restart

     // Configure MongoDB to auto start on boot
     $ sudo chkconfig mongod on

* Check the connection to the server
  ::

     $ mongo
     MongoDB shell version: 3.4.2
     >> //you are now in the mongo shell

.. _installation_programming_tools_mongodb_mac_osx:

Mac OSX
-------
* Install Homebrew if you have not already done so; check the :ref:`installation_system_tools_homebrew`
  guide
* Update Homebrew's package list
  ::

     $ brew update

* Install MongoDB
  ::

     $ brew install mongodb --with-openssl

* Configure MongoDB
  ::

     $ sudo mkdir -p /data/db
     $ sudo chmod 755 /data/db
     $ sudo chown $(whoami) /data/db
     $ sudo chgrp staff /data/db

* Run the MongoDB server and try connecting to it
  ::

     $ mongod
     $ mongo
     MongoDB shell version: 3.4.2
     >> //you are now in the mongo shell

.. _installation_programming_tools_mongodb_windows:

Windows
-------
* Download the appropriate version for your platform.  Not sure?  Check `here
  <https://support.microsoft.com/en-us/help/13443/windows-which-operating-system>`_:

  * On x86 platforms, download the `x86 version here <http://downloads.mongodb.org/win32/mongodb-win32-i386-v3.0-latest.zip>`_
  * On x64 platforms, download the latest version of `MongoDB here <https://www.mongodb.org/dl/win32/x86_64-2008plus-ssl>`_ (zip version)
* Extract the contents of the zip file to ``C:\mongodb`` and remove everything but the bin folder

  * Right click on the zip file and choose *Extract...*
  * When you are prompted to choose the destination, enter ``C:\mongodb``
  * Navigate to ``C:\mongodb`` and remove everything but the bin folder
* Read the instructions in the :ref:`tutorials_system_windows_path_modifying_windows_path` guide and add
  ``C:\mongodb\bin`` to your path
* Create a MongoDB config file located at: ``C:\mongodb\mongo.config`` and add the following:
  ::

     ## store data here
     dbpath=C:\mongodb\data

     ## all output go here
     logpath=C:\mongodb\log\mongo.log

     ## log read and write operations
     diaglog=3

.. important::
   The following steps require running command prompt or powershell with administrative privileges.  Right
   click command prompt or powershell and select *run as administrator*

* Create the log folder and the database folder
  ::

     C:\Users\Username> mkdir C:\mongodb\data
     C:\Users\Username> mkdir C:\mongodb\log

* Run MongoDB as Windows Service so that it starts up with the system
  ::

     C:\Users\Username> mongod --config C:\mongodb\mongo.config --install

* Start the MongoDB service
  ::

     C:\Users\Username> net start mongodb

* Test the server connection with mongo.exe
  ::

     C:\Users\Username> mongo
     MongoDB shell version: 3.4.2
     connecting to: test
     > //you are now in the mongodb shell

.. highlight:: python
