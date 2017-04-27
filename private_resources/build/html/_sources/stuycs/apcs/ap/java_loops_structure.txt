Basic Loops Structure
=====================

*Written by PChan on 2017-04-15*

* :ref:`tutorial_apcs_ap_java_loops_structure_overview`
* :ref:`tutorial_apcs_ap_java_loops_structure_while_loop`

  * :ref:`tutorial_apcs_ap_java_loops_structure_while_loop_example`
* :ref:`tutorial_apcs_ap_java_loops_structure_for_loop`

  * :ref:`tutorial_apcs_ap_java_loops_structure_for_loop_example`
* :ref:`tutorial_apcs_ap_java_loops_structure_comparison`

.. highlight:: java

.. _tutorial_apcs_ap_java_loops_structure_overview:

Loops Overview
--------------
In Java, repetitive tasks can be simplified through the usage of loops.  In this tutorial, we will look at
``while`` loops and ``for`` loops.
	       
.. _tutorial_apcs_ap_java_loops_structure_while_loop:

While Loops
-----------
The basic ``while`` loop structure is as follows:
::

   while (BE){
       // Code to run while BE is true
   }

Some key points to note:

* If the *boolean test* is false when the while loop is first encountered, the entire ``while`` block
  would be skipped
* After the execution of the loop body, the *boolean test* is evaluated again and the loop is only
  executed again if the *boolean test* is true
* Inside the ``while`` loop, you generally want to modify the test so that it will eventually lead to
  termination

.. _tutorial_apcs_ap_java_loops_structure_while_loop_example:

Example
^^^^^^^
To print out ``Hello World`` ten times, you might write something like this:
::

   i = 0;
   while (i < 10){
       System.out.println("Hello World");
       i++;
   }
  
.. _tutorial_apcs_ap_java_loops_structure_for_loop:

For Loops
---------
The general structure of a for loop is:
::

   for(initialization; test; update){
        // code to run inside the for loop
   }

*initialization*, *test*, and *update* must be valid Java statements.  They can
be omitted.

Breaking it down:

* *initialization* is where you initialize variables with a starting value
* *test* is a boolean expression that checks to see if the body of the loop should be evaluated
* *update* is where you modify the variables so that they will eventually fail the *test*

When the loop is first entered, the *initialization* statement is evaluated.  Before each iteration of the
loop, the *test* statement is evaluated to see if the body of the loop should be executed.  The *update*
statement is executed after the last statement in the body.

.. _tutorial_apcs_ap_java_loops_structure_for_loop_example:

Example
^^^^^^^
To print out ``Hello World`` ten times with a for loop:
::

   for(int i = 0; i < 10; i++){
       System.out.println("Hello World");
   }

.. _tutorial_apcs_ap_java_loops_structure_comparison:

For Loop vs While Loop
----------------------
After understanding the ``for`` loop and the ``while`` loop, the next step is to understand when to use
one and when to use the other.

.. note::
   All ``for`` loops can be written as ``while`` loops and all ``while`` loops can be written as ``for``
   loops.

==========================  ==================================================
Advantages of For Loop      Advantages of While Loop
==========================  ==================================================
Best used with counters     Best used when the number of iterations is unknown
==========================  ==================================================

.. highlight:: python
