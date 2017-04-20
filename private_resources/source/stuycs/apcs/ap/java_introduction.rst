.. _tutorial_apcs_ap_java_introduction:

Introducing Java
================

*Written by WX on 2017-04-12*

* :ref:`tutorial_apcs_ap_java_introduction_what_is_java`
* :ref:`tutorial_apcs_ap_java_introduction_jvm_and_java_bytecode`
* :ref:`tutorial_apcs_ap_java_introduction_writing_and_compiling_java_source_files`
* :ref:`tutorial_apcs_ap_java_introduction_running_java_files`

.. _tutorial_apcs_ap_java_introduction_what_is_java:
  
What is Java
------------
In IntroCS, you’ve learned Scheme and Netlogo, both of which are procedural programming languages
(meaning everything you’re coding is a procedure trying to accomplish a certain task). Java is different
from these languages in that the main building blocks are *objects* instead of functions/procedures. Each
**object** is a bundle of *fields* (properties, attributes) and *methods* (actions, what the object can
do).

.. _tutorial_apcs_ap_java_introduction_jvm_and_java_bytecode:

JVM and Java Bytecode
---------------------
Java is platform-independent, meaning it works on pretty much any platform (e.g. Linux, Windows, Mac OS,
etc.). To achieve this, the Java source code you write is first compiled into *Java bytecode* by the Java
compiler. The resulting ``.class`` file can then be ran on any platform if the *Java Virtual Machine*
(*JVM*) is installed on that computer.

.. _tutorial_apcs_ap_java_introduction_writing_and_compiling_java_source_files:

Writing and Compiling Java Source Files
---------------------------------------
All your Java source files should end with ``.java``. These files can be created by any text editor, but
you should avoid the usage of word processors such as LibreOffice Writer, Pages or Microsoft Word (avoid
them in general for programming, they’re not meant for this). To run your ``.java`` files, they must be
compiled into ``.class`` files with the following command:
::

   $ javac filename.java

.. _tutorial_apcs_ap_java_introduction_running_java_files:
   
Running Java Files
------------------
After compiling your ``.java`` files to produce ``.class`` files, you can run your Java program with the
following command:
::
   
   $ java filename

.. note::
   Do not include the .class extension when using this command!
