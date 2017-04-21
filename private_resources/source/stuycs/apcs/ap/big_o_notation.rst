Big O Notation
==============

*Written by PChan on 2017-04-20*

* :ref:``

Brief Overview
--------------
When comparing the performance of different algorithms, one of the most important concept to understand is
**Big O Notation**.

Mathematical Context
--------------------
In this section, we will take a more mathematical approach to explaining the behavior of Big O Notation.
Let's take a look at a few equations:

.. math::

   y &= 5x + 2 \\
   y &= 6x + 3 \\
   y &= x + 2 \\
   y &= x^2 + 4x + 9

Categorize each of the equation above (logarithmic, quadratic, cubic, linear, etc...).  Explain your
reasoning.

Aside from the last equation, we can all agree that the rest are linear equations.  Drawing any of them
would produce a line.  Now suppose we were to superimpose the last equation on top of the graph of any of
the other equations and zoom out such that the x and y values are very large.  You would notice that for
any value of x after a certain point would always yield a larger y value.  No matter how steep we make our
linear equations, they can never match the growth of a quadratic equation.  If you are ever confused about
why we are ignoring the coefficients, think back to why you categorize the first three as linear
equations.
