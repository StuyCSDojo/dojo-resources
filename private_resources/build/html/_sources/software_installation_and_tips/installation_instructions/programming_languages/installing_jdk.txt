Installing Java JDK
===================

*Written by PChan on 2017-05-13*

* :ref:`installation_programming_languages_java_linux`
* :ref:`installation_programming_languages_java_mac_osx`
* :ref:`installation_programming_languages_java_windows`

.. _installation_programming_languages_java_linux:

Linux
-----
Writing Java programs would require you to install the **Java JDK (Java Development Kit)** while running
Java programs would require you to install the **Java JRE (Java Runtime)**.  This guide would cover how to
install the **Java JDK**.

.. highlight:: none

* Ubuntu/Mint/Debian
  ::

     sudo apt-get install openjdk-8-jdk openjdk-8-jre

* Fedora
  ::

     su -c "yum install java-1.8.0-openjdk-devel java-1.8.0-openjdk"

* Other Distros, you probably know how...

.. highlight:: python

.. note::
   The current version of this guide assumes you want to install Java 8.  To install a different version
   of Java, simply replace the ``8`` in ``openjdk-8-jdk`` and the ``8`` in ``openjdk-8-jre`` for Debian
   system with the latest version of Java.

   For Fedora, replace the ``8`` in ``java-1.8.0-openjdk-devel`` and the ``8`` in ``java-1.8.0-openjdk``
   with the latest version of Java.

.. _installation_programming_languages_java_mac_osx:

Mac OSX
-------

.. highlight:: none

Writing Java programs would require you to install the **Java JDK (Java Development Kit)** while running
Java programs would require you to install the **Java JRE (Java Runtime)**.  This guide would cover how to
install the **Java JDK**.

We are going to be installing the **Java JDK** via Homebrew:

1. Install Homebrew following the :ref:`installation_system_tools_homebrew` guide if it is not already
   installed (near the bottom, you will also find instructions for installing cask and brew-cask-upgrade)
2. Install Java by executing the following command in the terminal:
   ::

      $ brew cask install java

Note: In the future, update Java with the following command:
::

   $ brew update
   $ brew cu

.. highlight:: python

.. _installation_programming_languages_java_windows:

Windows
-------
Writing Java programs would require you to install the **Java JDK (Java Development Kit)** while running
Java programs would require you to install the **Java JRE (Java Runtime)**.  This guide would cover how to
install the **Java JDK**.

Download the JDK
^^^^^^^^^^^^^^^^
1. Go to `Java SDK download site <http://www.oracle.com/technetwork/java/javase/downloads/index.html>`_
2. Under the heading: "Java Platform, Standard Edition", click on the download button for JDK.

   .. figure:: ../../images/installation_instructions/programming_languages/java/java-se-downloads.png
      :align: center
      :width: 450

      The heading has been underlined in orange, while the download button for the JDK is circled in
      green.

.. tip::
   To find out whether you are using x32 or x64 bit OS, check out `this guide from Microsoft <http://support.microsoft.com/kb/827218/en-US>`_.

3. The latest version of the **Java JDK** is found right underneath the description at the top.  Accept
   the license agreement and download the appropriate version for your operating system.

   .. figure:: ../../images/installation_instructions/programming_languages/java/java-jdk-download.png
      :align: center
      :width: 450

      Make sure to accept the license agreement (in orange).  The Windows download links are underlined in
      blue.

.. warning::
   Note that the version number in the screenshot may differ from the ones you see.

4. Run the executable that you just downloaded.  The installer would install both the **Java JDK** and the
   **Java JRE**.
5. Add the **Java JRE** and the **Java JDK** to your system path.  If you are not sure how to do so...

   * Using Windows Explorer, navigate to ``C:\Program Files\Java`` where you will find a directory for the
     **Java JDK** and a directory for **Java JRE**.
   * Read the :ref:`tutorials_system_windows_path_modifying_windows_path` guide and then add the following
     two folders to your path:

     * ``C:\Program Files\Java\<jdk_directory>\bin`` (<jdk_directory> is the name of the jdk directory)
     * ``C:\Program Files\Java\<jre_directory>\bin`` (<jre_directory> is the name of the jre directory)


5. Add the **Java JRE** and the **Java JDK** to your system path.

   If you are not sure how to do so, read
   the :ref:`tutorials_system_windows_path_modifying_windows_path` guide and then add the bin folders of
   the two folders in ``C:\Program Files\Java`` to your path.
6. Fire up a new command prompt and try the following commands: ``javac --version`` and ``java --version``
7. If you did not get a commmand not found error, congratulations!!!
