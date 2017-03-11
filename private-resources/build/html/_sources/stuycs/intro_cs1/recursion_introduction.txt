Introduction to Recursion
=========================

.. |br| raw:: html

   <br />

Outline
-------
  * :ref:`what_is_recursion`
  * :ref:`base_case`
  * :ref:`tips_for_base_case`
  * :ref:`tips_for_recursive_reduction`
  * :ref:`what_is_head_recursion`
  * :ref:`tips_for_head_recursion`
  * :ref:`sample_workflow_for_head_recursion`
  * :ref:`what_is_tail_recursion`
  * :ref:`what_are_state_variables`
  * :ref:`tips_for_tail_recursion`
  * :ref:`sample_workflow_for_tail_recursion`

.. _what_is_recursion:

What is Recursion
^^^^^^^^^^^^^^^^^
**Recursive reduction** is the process of breaking down a larger problem into smaller pieces each time the
function is called.  A **recursive function** is a function that calls itself using recursive reduction
until it has reached a base case. 

.. _base_case:

What is a Base Case
^^^^^^^^^^^^^^^^^^^
A **base case** is sometimes refer to as the exit case.  It should:

  * **NOT** call the recursive function (should not be expressed in a recursive manner)
  * Typically return a constant of some form (a number, a string, etc)

    * Sample values for integers: 0, 1, 2
    * Sample values for strings: " ", "a", ""
    * Sample values for Scheme lists: (), (0)
    * Sample values for NetLogo lists: [], [0]

.. warning::
   These sample values are not the only possible values for base cases.
  
.. _tips_for_base_case:

Tips for Finding the Base Case
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  * Define the problems in spoken English/mathematical terms first
  * Trace through an example, at what point can you not define the function in terms of itself
  * Remember that a base case should not involve any unknown variables
  * Think about the data types that the problem uses

    * Examples include, but are not limited to: floating-point numbers, Strings, Arrays, integers
  
  * Use the simplest value in the data type and see if you can derive a base case out of it

    * Sample values for integers: 0, 1, 2
    * Sample values for Strings: " ", "a", ""
    * Sample values for Arrays: [], [0]

.. _tips_for_recursive_reduction:

Tips for Finding the Recursive Reduction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  * Draw a trace diagram and think of how you can break the problem into smaller pieces with each
    recursive call
  * Use the base case to help you deduce the recursive reduction
    
    * Figure out the base case first, using the tips above
    * Think about a problem that is slightly more complex than the base case.  How can you reduce it to
      the base case?

.. _what_is_head_recursion:

What is a Head Recursive Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The first form of recursion you learn this semester was head recursion and is characterized by:

  * Deferred operations: operations that cannot be computed yet because there are still unknown components

    * This causes the stack to grow until we reach the base case

  * No wrapper functions: We do not need to keep track of additional variables
  * The recursive call is the first statement to be evaluated after the base case
  * May be more memory intensive

.. _tips_for_head_recursion:

Tips for Writing Head Recursive Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  * Formulate the base case and the recursive reduction first
  * Draw a few flowcharts or trace through a few examples to solidify your algorithm and your
    understanding of how everything fits together
  * Write your algorithm in pseudocode, this gives you a solid outline to build up without worrying about
    the syntax and also tests your understanding of your own algorithm

.. _sample_workflow_for_head_recursion:

Sample Workflow for Head Recursion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Let us try tackling the classic factorial problem: write a head recursive function that takes an integer,
n, as the parameter and returns n!

  * Start by tracing through the process of finding n! with a numerical value of n.  Let's choose 6! for
    instance.

    .. highlight:: none

    ::

       So, what is (6!)?
           It is 6*5*4*3*2*1.
	   
       Great!  Now what is the simplest factorial that you can think of?  And what does it equal?
           Wait what?  What does this have to do with 6!?
	   
       Bear with me.  This will help you solve the problem.  So, what is the simplest factorial?
           1! which is 1.  (If you answer 0, just think of 1 being the simplest for now).
	   
       Now what is a factorial that is slightly more complex?
           That would be 2!
	   
       How can we rewrite 2! in terms of 1!?
           That would be 2*1!
	   
       Notice how we have just reduced a slightly more complicated problem into a simpler problem
       involving something we already know...  Ponder over the significance of this...  How would you
       solve 3! in this manner?
           Hint: 3*2! which is 3*(...)
	   
       Now take some time to rewrite 6!
           That will be: 6*5!
                           5*4!
                             4*3!
                               3*2!
                                 2*1!
                                   1     
       Ponder over the case of n!
           Hint: How can you rewrite n! in terms of a smaller factorial?  How can you rewrite the smaller
	   factorial into an even smaller one?
	   
       By now, you might have deduce that 1! can serve as your base case.  A pseudocode might be:
           if n is equal to 1
               then the answer is 1
           otherwise
               then the answer is ?
	       
       Here is a hint to fill in the last blank: Look at the trace diagram of 6!...  Notice how each step,
       the factorial that we are computing shrinks.
    
       Now, one last thing before I leave you...  Something you should be aware of is that 0! is by
       definition 1.  The modified pseudocode might look like:
           if n is less than or equal to 1
               then the answer is ?
           otherwise
               the answer is ?

    .. highlight:: python

.. _what_is_tail_recursion:

What is a Tail Recursive Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The second form of recursion that you might have covered is characterized by:

  * **NO** deferred operations
  * Usage of state variables
  * The recursive call is the last operation to be performed, all computations come before it

.. _what_are_state_variables:
   
What are State Variables
^^^^^^^^^^^^^^^^^^^^^^^^
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

.. _tips_for_tail_recursion:

Tips for Writing Tail Recursive Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Writing a tail recursive function is very similar to writing a head recursive function, so start by coming
up with the recursive reduction and the base case.  Afterward:

  * Remember that tail recursion differs from head recursion in that it modifies the parameter with each
    recursive call
  * Instead of performing the operation on the recursive call, do it directly to the parameter

.. _sample_workflow_for_tail_recursion:

Sample Workflow for Tail Recursion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Let us try tackling the classic factorial problem: write a tail recursive function that takes an integer,
n, as the parameter and returns n!

  * Start by tracing through the process of finding n! with a numerical value of n.  Let's choose 6! for
    instance.

    .. highlight:: none

    ::

       So, what is (6!)?
           It is 6*5*4*3*2*1.
	   
       Great!  Now what is the simplest factorial that you can think of?  And what does it equal?
           Wait what?  What does this have to do with 6!?
	   
       Bear with me.  This will help you solve the problem.  So, what is the simplest factorial?
           1! which is 1.  (If you answer 0, just think of 1 being the simplest for now).
	   
       Now what is a factorial that is slightly more complex?
           That would be 2!
	   
       How can we rewrite 2! in terms of 1!?
           That would be 2*1!
	   
       Notice how we have just reduced a slightly more complicated problem into a simpler problem
       involving something we already know...  Ponder over the significance of this...  How would you
       solve 3! in this manner?
           Hint: First, rewrite 3! as 3*2!  How do we write that in terms of 1!?
	   
       Now take some time to rewrite 6!
           That will be: 6*5!
                           5*4!
                             4*3!
                               3*2!
                                 2*1!
                                   1     
       Ponder over the case of n!
           Hint: How can you rewrite n! in terms of a smaller factorial?  How can you rewrite the smaller
	   factorial into an even smaller one?
	   
       By now, you might have deduce that 1! can serve as your base case.  Now how can we incorporate
       the usage of state variables, one of the distinguishing factors of tail recursion?

       Remember that two of the main usage of state variables are to store the answer that you have
       calculated so far and to act as a counter.

       So let us start by adding a variable for our current answer.  The function header would look like:

       (define factorial (lambda (n product)
              ...
	      )

       Notice that in addition to n (the number to calculate the factorial for), we have product.  This
       allows us to keep track of the current product as we progress from one function call to another.

       But, how would we know when to stop?  It might be useful to have a counter that counts up to n.  A
       trace of (factorial n) when n is 6 is shown below:
       
       -----------------------------------------------------------------------
       | Function Call       | Current Value of n | Counter | Current Answer |
       -----------------------------------------------------------------------
       | (factorial 6 1 1)   |          6         |    1    |        1       |
       -----------------------------------------------------------------------
       | (factorial 6 2 2)   |          6         |    2    |        2       |
       -----------------------------------------------------------------------
       | (factorial 6 3 6)   |          6         |    3    |        6       |
       -----------------------------------------------------------------------
       | (factorial 6 4 24)  |          6         |    4    |       24       |
       -----------------------------------------------------------------------
       | (factorial 6 5 120) |          6         |    5    |      120       |
       -----------------------------------------------------------------------
       | (factorial 6 6 720) |          6         |    6    |      720       |
       -----------------------------------------------------------------------

       The actual code is left as an exercise for you to complete.  Remember to take into account 0!

    .. A pseudocode might be:
           if n is equal to 1
               then the answer is 1
           otherwise
               then the answer is ?
       Here is a hint to fill in the last blank: Look at the trace diagram of 6!...  Notice how each step,
       the factorial that we are computing shrinks.
    
       
       
..
       Something you should also be aware of is that 0! is by definition 1.  The modified pseudocode might
       look like (fill in the ? parts yourself):
           if n is less than or equal to 1
               then the answer is ?
           otherwise
               the answer is ?

       Now this might remind you of head recursion and that is OK...  I will show you how to convert this
       to tail recursion.

       Currently, the solution is...

	       
    .. highlight:: python
