Selection Sort
==============

*Written by PChan on 2017-04-13*

* :ref:`tutorial_apcs_ap_selection_sort_key_idea`
* :ref:`tutorial_apcs_ap_selection_sort_the_general_algorithm`
* :ref:`tutorial_apcs_ap_selection_sort_exercises`

.. _tutorial_apcs_ap_selection_sort_key_idea:
  
Key Idea: Finding the Minimum
-----------------------------
Before we look at the actual sorting algorithm, let us start with an algorithm for finding the index of
the minimum element in a list.  Keep in mind that you cannot simply call ``Collections.min()`` or make any
assumptions regarding the state of the given list.

Think over this simpler problem: Given a list of three elements, how would you determine the smallest of
the three?  Use the following list: [3, 1, 2]

**Answer:**

1. Declare a temporary variable (we would name it currentValue)
2. Start with the first element; set currentValue to the first element

   * currentValue is now 3.
3. Compare the second element to the currentValue.  If the second element is smaller than the
   currentValue, set currentValue to the second element

   * Is 1 less than 3?  Yes!  So, set currentValue to 1.
4. Compare the third element to the currentValue.  If the third element is smaller than the currentValue,
   set currentValue to the third element

   * Is 2 less than 1?  No, so leave currentValue alone.
5. The minimum of the list is simply currentValue: 1!
   
Now generalize this approach to work with a list of n elements.  How can we modify this approach to keep
track of the index of the smallest element?  Solve this last issue before proceeding to the next section.

.. _tutorial_apcs_ap_selection_sort_the_general_algorithm:

The General Algorithm
---------------------
Selection sort involves repeatedly searching for the minimum element of the list and swapping it to the
correct position.

1. Use the algorithm discussed above to find the minimum element
2. Swap that element with the first element of the list
3. Find the next smallest element of the list (or the minimum element of the list starting  from the first
   element)
4. Swap that element with the second element of the list
5. Repeat this process until you have place the n - 1 element in the correct spot where *n* is the length
   of the list

.. image:: ../../images/apcs/ap/selection-sort.gif
   :align: center
   :width: 400
   
.. _tutorial_apcs_ap_selection_sort_exercises:

Exercises
---------
Here are some questions to ponder over (in order of ascending difficulty):

1. Is there a best case scenario?  A worst case scenario?
2. How many passes would you need to make to sort an array of size 10?  100?  1000?
3. Determine the runtime of this algorithm.  What is the ratio of the time it takes to sort the list and
   the size of the list?   
