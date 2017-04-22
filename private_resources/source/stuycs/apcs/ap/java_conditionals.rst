Conditionals
============

*Written by PChan on 2017-04-15*

* :ref:`tutorial_apcs_ap_java_conditionals_if_statements`
* :ref:`tutorial_apcs_ap_java_conditionals_if_statements_tips_and_warnings`

  * :ref:`tutorial_apcs_ap_java_conditionals_if_statements_tips_and_warnings_nested_if_statements`
  * :ref:`tutorial_apcs_ap_java_conditionals_if_statements_tips_and_warnings_conditionals_without_braces`
* :ref:`tutorial_apcs_ap_java_conditionals_extended_if_statements`

.. highlight:: java
  
.. _tutorial_apcs_ap_java_conditionals_if_statements:

The Basic if Statement
----------------------
The general structure of the ``if`` statement...
::

   if (Boolean Expression){
       // Code to run if Boolean Expression is true
   }

The body of the ``if`` statement would only be evaluated if *Boolean Expression* is true. While the
following snippet is legal, it is typically bad practice:
::

   if (true){
       // Your code here...
   }

Since the code would always evaluate, you can move the body of the ``if`` statement outside of the ``if``
statement.  Similarly, don't write ``if (false){}``.
   
Next, we would take a look at the ``if ... else`` statement:
::

   if (BE){
       // Code to evaluate if BE is true
   }
   else{
       // Code to evaluate if BE is false
   }

.. note::
   *BE* is simply an abbreviation for *Boolean Expression*

If the BE is true, the body of the ``if`` statement would be evaluated, but the body of the ``else``
statement would be ignored.  If the BE is false, the body of the ``if`` statement would be ignored, and
the body of the ``else`` statement would be evaluated.

.. _tutorial_apcs_ap_java_conditionals_if_statements_tips_and_warnings:

Tips and Warnings
-----------------

.. _tutorial_apcs_ap_java_conditionals_if_statements_tips_and_warnings_nested_if_statements:

Nested if Statements
^^^^^^^^^^^^^^^^^^^^
Here is a tip when writing nested ``if`` statements:
::

   if (Boolean Expr1){
       if (Boolean Expr2){
            // Code to evaluate if Boolean Expr1 and Boolean Expr2 are true
       }
   }

The above snippet of code can be rewritten as:
::

   if (Boolean Expr1 && Boolean Expr2){
       // Code to evaluate if Boolean Expr1 and Boolean Expr2 are true
   }

.. _tutorial_apcs_ap_java_conditionals_if_statements_tips_and_warnings_conditionals_without_braces:
   
Conditionals Without Braces
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sometimes you might find some Java code written like the following:
::

   if (BE)
       //singular statement to run

When there is only one statement in the body of a conditional, you can leave out the braces.  Do note that
any statements indented similarly would be evaluated every single time.

.. warning::
   The usage of this feature is not recommended as it can introduce errors later when you add more
   statements to the body.  Always use braces and save yourself hours of headaches.

.. _tutorial_apcs_ap_java_conditionals_extended_if_statements:

Extended if Statements
----------------------
Do you remember the ``cond`` statement in Scheme?

.. highlight:: racket

::

   (cond
     ((<BE>) <things to do>)
     ((<BE>) <things to do>)
     ((<BE>) <things to do>)
     (else (<things to do>)))

.. highlight:: python
     
Or maybe the ``elif`` statement in Python...
::

   if <BE>:
       <things to do>
   elif <BE>:
       <things to do>
   elif <BE>:
       <things to do>
   else:
       <things to do>
       
.. highlight:: java
     
The ``cond`` statement in Scheme or the ``elif`` statement in Python allows you to test multiple
conditionals without nesting if statements.

The Java equivalence would be:
::

   if (Boolean Expr){
       // Code to execute if Boolean Expr is true
   }
   else if (Boolean Expr1){
       // Code to execute if Boolean Expr1 is true
   }
   else{
       // Code to execute if none of the previous BEs is true
   }

Between the ``if`` statement and the ``else`` statement, you can add as many ``else if`` statements as you
wish.  As soon as one of the conditional in the chain is triggered, the body of that conditional would be
evaluated and control is passed to the first statement after the else block.  If none of the conditionals
are triggered, the ``else`` block would be evaluated.

.. note::
   If you want all the conditionals to be evaluated, you would utilize a series of ``if`` statements
   rather than ``if`` and ``else if`` statements.   

.. highlight:: python
