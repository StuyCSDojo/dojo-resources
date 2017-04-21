QuickSort
=========

*Written by PChan on 2017-04-14*

* :ref:`tutorial_apcs_ap_quicksort_introduction_key_idea`
* :ref:`tutorial_apcs_ap_quicksort_introduction_the_general_algorithm`
* :ref:`tutorial_apcs_ap_quicksort_introduction_exercises`

.. _tutorial_apcs_ap_quicksort_introduction_key_idea:
  
Key Idea: Partitioning
----------------------
.. glossary::

   Pivot
      The element you would be comparing against while partitioning or sorting via quicksort.  This can be
      any element from the list.
   
One of the key component to quicksort is the partitioning algorithm.  The goal of the algorithm is to
group all elements less than a chosen pivot to the left of the pivot and all the elements greater than the
pivot to the right of the pivot.

Given the list:
::

   A = [1, 6, 3, 7, 2, 4]

Here is how you would partition the list:

1. Start with the last element as the pivot
2. Declare two variables: left and right; they would store the index as you move from the left and the
   index as you move from the right respectively
3. Set them to *0* and *n - 2* (for the second to last element) respectively
4. Increment the left variable for each element that is smaller than the pivot or until it crosses with
   the right variable
5. Decrement the right variable for each element that is greater than the pivot or until it crosses with
   the left variable
6. If the two variables do not cross, swap the values at those indices
7. Repeat steps 4 through 6 until the variables do cross
8. Swap the pivot with the value at the index in which the variables cross
   
.. _tutorial_apcs_ap_quicksort_introduction_the_general_algorithm:

The General Algorithm
---------------------
Once you have mastered the partitioning algorithm, the rest of quicksort is very easy.

1. If the size of the list is 1, return the list
2. Otherwise, pick a pivot and partition the list around the pivot
3. Repeat the above steps for the left sublist and the right sublist

.. figure:: ../../images/apcs/ap/quicksort.gif
   :align: center
   :width: 400

   The animation above shows one iteration of quicksort.  To sort the rest of the list, quicksort each
   sublist.   

.. _tutorial_apcs_ap_quicksort_introduction_exercises:

Exercises
---------
Here are some questions to ponder over (in order of ascending difficulty):

1. Is there a best case scenario?  A worst case scenario?
2. How many times do you need to partition the list before the list is sorted?
3. Determine the runtime of this algorithm.  What is the ratio of the time it takes to sort the list and
   the size of the list?

Optional) How can you improve the basic quicksort algorithm?

.. hint::
   Trace the quicksort algorithm when the pivot is the smallest or biggest element.   What about when
   the pivot is the median of the list?  Reflect on how this affects the performance of quicksort.
