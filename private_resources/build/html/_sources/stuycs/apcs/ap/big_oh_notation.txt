Big Oh Notation
===============

*Written by PChan on 2017-04-20*

* :ref:`tutorial_apcs_ap_big_oh_notation_overview`
* :ref:`tutorial_apcs_ap_big_oh_notation_mathematical_context`
* :ref:`tutorial_apcs_ap_big_oh_notation_big_oh_notation_description`

  * :ref:`tutorial_apcs_ap_big_oh_notation_o1`
  * :ref:`O(n) <tutorial_apcs_ap_big_oh_notation_on>`
  * :ref:`O(n^2) <tutorial_apcs_ap_big_oh_notation_on2>`
  * :ref:`O(2^n) <tutorial_apcs_ap_big_oh_notation_o2n>`
  * :ref:`O(logn) <tutorial_apcs_ap_big_oh_notation_ologn>`
  * :ref:`O(nlogn) <tutorial_apcs_ap_big_oh_notation_onlogn>`
* :ref:`tutorial_apcs_ap_big_oh_notation_guide_to_runtime_analysis`
  
.. highlight:: java
  
.. _tutorial_apcs_ap_big_oh_notation_overview:
  
Brief Overview
--------------
When comparing the performance of different algorithms, one of the most important concept to understand is
**Big Oh Notation**.  By looking at the asymptotic behavior of the algorithm, we can ignore factors such
as the speed of the machine used to time the algorithm while simplifying the process.

.. _tutorial_apcs_ap_big_oh_notation_mathematical_context:

Mathematical Context
--------------------
In this section, we will take a more mathematical approach to explaining the behavior of Big Oh Notation.
Let's take a look at a few equations:

.. math::

   y &= 5x + 2 \\
   y &= 6x + 3 \\
   y &= x + 2 \\
   y &= x^2 + 4x + 9

**Exercise:** Categorize each of the equation above (logarithmic, quadratic, cubic, linear, etc...) and
explain your reasoning.

We can all agree that the first three equations are linear. Now if we were to superimpose the last
equation on top of the graph of the other equations and zoom out such that the x and y values are very
large...

.. figure:: ../../images/apcs/ap/big-oh-notation-equation-graph.png
   :align: center
   :width: 450

   For very large values of x, the growth of the quadratic function is always faster than the linear
   functions.

.. tip::
   If you are ever confused about why we are ignoring the coefficients, think back to why you categorize
   the first three equations as linear.

.. _tutorial_apcs_ap_big_oh_notation_big_oh_notation_description:
   
Big Oh Notation Description
---------------------------

.. figure:: ../../images/apcs/ap/big-oh-notation-graph.png
   :align: center
   :width: 400

   A graph showing the growth for different Big Oh notation.

.. _tutorial_apcs_ap_big_oh_notation_o1:

O(1)
^^^^
O(1) is used to describe an algorithm that will always run in constant time regardless of the size of the
given data.
::

   public boolean isEqualFive(int number){
       return number == 5;
   }

Note here that no matter how big the given number is, the comparison will always take the same amount of
time.

.. _tutorial_apcs_ap_big_oh_notation_on:

O(:math:`n`)
^^^^^^^^^^^^
O(:math:`n`) is used to describe an algorithm that grows linearly in relationship to the given data.
::

   public boolean containsUppercaseA(String password){
       for(int i = 0; i < password.length() - 1; i++){
           String letter = password.substring(i, i + 1);
	   if letter.equals("A"){
	       return true;
	   }
       }
       return false;
   }

While it is possible for the loop to terminate after looking at the first letter, the Big Oh notation for
an algorithm/function is usually determined by looking at the worst-case scenario.  In this case, the
longer the password string, the longer it can take to determine if the string contains uppercase A.

.. _tutorial_apcs_ap_big_oh_notation_on2:

O(:math:`n^2`)
^^^^^^^^^^^^^^
O(:math:`n^2`) is used to describe an algorithm that grows directly in proportion to the square of the
size of the given data.  This is common among algorithms utilizing nested loops.  Increasing the depth of
the nested loop may result in O(:math:`n^3`), O(:math:`n^4`), and etc.
::

   public int calculate(int n){
       int s = 0;
       for(int i = 0; i < n; i++){
           for(int j = 0; j < n; j++){
	       s += 1;
	   }
       }
       return s;
   }

Here the inner loop is running in linear time and the outer loop is also running in linear time.  Since we
are performing a linear operation :math:`n` times, it would be O(:math:`n^2`).

.. warning::
   Note that nested loops do **NOT** always means O(:math:`n^2`) or O(:math:`n^k`) for some constant
   :math:`k`.  This is only true when each loop construct is performing a linear operation.         

Nested loops, but not O(:math:`n^2`) runtime:
::

   public notQuadraticRuntime(int n){
       int s = 0;
       for(int i = 1; i < n; i *= 2){
           for(int j = 1; j < i; j++){
	       s++;
	   }
       }
   }
   
.. _tutorial_apcs_ap_big_oh_notation_o2n:
   
O(:math:`2^n`)
^^^^^^^^^^^^^^
O(:math:`2^n`) is used to describe an algorithm whose growth doubles with each increment in the size of
the given data (exponential growth).  An example of this is the naive recursive calculation of the
:math:`n^{th}` term in the Fibonacci sequence.
::

   public int fib(int n){
       if (n < 2){
           return n;
       }
       return fib(n - 1) + fib(n - 2);
   }

.. _tutorial_apcs_ap_big_oh_notation_ologn:
   
O(:math:`log N`)
^^^^^^^^^^^^^^^^
O(:math:`log N`) is used to describe an algorithm where you are discarding large chunks of data with each
iteration.

.. note::
   The base of the logarithm does not matter because the difference between bases is a minor constant that
   we ignore anyway.
   
::

   public int getNumOfHalves(int[] data){
       int count = 0;
       int dataLength = data.length;
       while (dataLength > 1){
           dataLength = dataLength / 2;
	   count++;
       }
       return count;
   }

In the algorithm above, we are calculating how many times you can halve the length of a given array before
we reach a size of 1 or 0.  Note how quickly ``dataLength`` shrinks as you give it an array of size 10.
What about 100?  1000? 10000?

.. _tutorial_apcs_ap_big_oh_notation_onlogn:

O(:math:`n log N`)
^^^^^^^^^^^^^^^^^^
O(:math:`n log N`) is used to describe an algorithm that usually repeats a linear operation :math:`log N`
times, but the algorithm may repeat a logarithmic operation :math:`n` times instead.  A typical example
would be merge sort or quick sort.  Here is a different example:
::

   public int getNumOfHalves(int[] data){
       // implementation is shown in the example for O(log n)
   }

   public int getTotalNumOfHalves(int[][] data){
       totalNumOfHalves = 0;
       for(int i = 0; i < data.length; i++){
           totalNumOfHalves += getNumOfHalves(data[i]);
       }
       return totalNumOfHalves;
   }

In this example, we are calling ``getNumOfHalves()`` :math:`n` times.  Since ``getNumOfHalves()`` is
O(:math:`log N`), the total runtime is O(:math:`n log N`).
   
.. _tutorial_apcs_ap_big_oh_notation_guide_to_runtime_analysis:

Guide to Runtime Analysis
-------------------------
1. Break the algorithm or function that you are analyzing into steps
2. Analyze each step and determine the Big Oh notation for that step
3. Sum up the Big Oh notation of each step and find the dominating term
4. Drop all coefficients for the dominating term and you have found the Big Oh notation for that
   algorithm/function

Let's take a look how we can use the steps above to determine the Big Oh notation for a ``addLinear``
function that takes a single argument and insert it in the proper location of a sorted list:

1. Write out the steps for ``addLinear()``

   1. Search for the index where it would be inserted
   2. Possibly shift all the elements starting at that index to the right
   3. Insert the new element into the unoccupied index
2. Analyze the runtime for each step

   1. What is the runtime for the linear search?
   2. What is the runtime for shifting n elements?
   3. What is the runtime for inserting a new element?
3. Sum up the Big Oh notation of each step

   1. Let's say the runtime is O(:math:`n^2`)
   2. Let's say the runtime is O(:math:`n^3`)
   3. Let's say the runtime is O(:math:`n`)

   The sum is O(:math:`n^3`) + O(:math:`n^2`) + O(:math:`n`), but you only care for the dominating term.
   Hence the Big Oh notation for ``addLinear()`` in this case would be O(:math:`n^3`).

.. highlight:: python
