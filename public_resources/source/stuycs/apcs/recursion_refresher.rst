Recursion: A Refresher
======================

.. |br| raw:: html

   <br />

*Written by PChan on 2017-03-11*
   
  * :ref:`apcs_definitions`
  * :ref:`apcs_tips_for_recursive_reduction`
  * :ref:`apcs_tips_for_base_case`
  * :ref:`apcs_what_is_recursion`
  * :ref:`apcs_recursion_example`
  * :ref:`apcs_what_is_iterative_style_recursion`
  * :ref:`apcs_what_are_state_variables`
  * :ref:`apcs_iterative_style_recursion_example`

.. _apcs_definitions:

Definitions
-----------
* **Recursive reduction** is the process of breaking down a larger problem into smaller pieces each time
  the function is called
* **Recursive function** is a function that calls itself using recursive reduction until it has reached a
  base case
* A **base case** is sometimes refer to as the exit case.  It should **NOT** make a call to the recursive
  function

.. _apcs_tips_for_recursive_reduction:

Tips for Finding the Recursive Reduction
----------------------------------------
  * Draw a trace diagram and think of how you can reduce the problem into smaller pieces with each
    recursive call
  * Use the base case to help you deduce the recursive reduction

    * **ON PAPER**, find out the base case first using the tips below
    * Think about a problem that is slightly more complex than the base case.  How can you reduce it to
      the base case?

.. _apcs_tips_for_base_case:

Tips for Finding the Base Case
------------------------------
  * Define the problems in spoken English/mathematical terms first
  * Trace through an example, at what point can you not define the function in terms of itself
  * Remember that a base case should not involve any unknown variables
  * Think about the data types that the problem uses

    * Examples include, but are not limited to: floating-point numbers, strings, lists, integers
  
  * Use the simplest value in the data type and see if you can derive a base case out of it

    * Sample values for integers: 0, 1, 2
    * Sample values for strings: " ", "a", ""
    * Sample values for Scheme lists: (), (0)
    * Sample values for Netlogo lists: [], [0]

.. important::
   These sample values are not the only possible values for base cases.
      
.. _apcs_what_is_recursion:

What is a Recursive Function
----------------------------
Recursion, sometimes referred to as "head recursion", is characterized by the following:

  * Deferred operations: operations that cannot be computed yet because there are still unknown components

    * This causes the stack to grow until we reach the base case

  * The recursive call is the first statement to be evaluated after the base case
  * May be more memory intensive

.. _apcs_recursion_example:

Example of Recursion
--------------------
.. highlight:: java

::

   public static int factorial(int n){
       if (n < 2){
           return n;
       }else{
           return n * factorial(n - 1);
	   // assuming you are not returning above...
           // the rest of the computation will go here if there are any
       }
   }

.. highlight:: python
   
.. _apcs_what_is_iterative_style_recursion:

What is an Iterative-Style Recursive Function
---------------------------------------------
Another style of recursion that you may have covered is characterized by the following:

  * **NO** deferred operations
  * Usage of state variables
  * Typically used with wrapper functions because of extra parameters

    * **Wrapper functions** are functions whose sole purpose is to call another function
  * The recursive call is the last operation to be performed, all computations come before it

.. _apcs_what_are_state_variables:
   
What are State Variables
------------------------
State variables are variables that serve a specific role in a function.  They allow us to:

  * Keep track of properties of the function as it is running, such as a counter 
  * Use the aforementioned data to continue an interrupted recursive call

Some of the most commonly asked questions about state variables are:

  * How many state variables should you use?

    * Answer: There is no definite answer. Generally, you will need one to keep track of the answer and
      maybe another for a counter.  Use however many you feel is necessary.

  * Am I doing it wrong if I use more state variables than my classmate?

    * Answer: The most important attribute of a good program is that it works correctly.  Do not worry if
      your classmate uses less state variables (especially if their solution is wrong).  With more
      practice, you will realize how to trim away unnecessary state variables.

.. tip::
   Keep in mind that more state variables can improve the readability of your code.

.. _apcs_iterative_style_recursion_example:

Example of Iterative Style Recursion
------------------------------------
.. highlight:: java

::

   public static int factorial(int n){
       return factorialHelper(n, 1);
   }
   
   public static int factorialHelper(int n, int product){
       if (n < 2){
           return product;
       }else{
           // any other computation will go here before the recursive call
           return factorial(n - 1, product * n);
       }
   }

.. highlight:: python
