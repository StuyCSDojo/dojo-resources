Insertion Sort
==============

*Written by PChan on 2017-04-13*

* :ref:`tutorial_apcs_ap_insertion_sort_definitions`
* :ref:`tutorial_apcs_ap_insertion_sort_key_idea`
* :ref:`tutorial_apcs_ap_insertion_sort_the_general_algorithm`
* :ref:`tutorial_apcs_ap_insertion_sort_exercises`

.. _tutorial_apcs_ap_insertion_sort_definitions:

Definitions
-----------
First, let us go over a few definitions:

.. glossary::

   Correct Position
      Position in a list where an element may be placed such that it is sorted relative to the other
      elements of the list.

   Sorted List
      A list is considered sorted if its element are ordered in a particular manner.  Unless specified
      otherwise, we would assume it is ordered in ascending order.

   Unsorted List
      A list is considered unsorted if its element are placed in no particular order.

.. _tutorial_apcs_ap_insertion_sort_key_idea:

Key Idea: Sorting a Hand of Cards
---------------------------------
Let us first take a look at how one would sort a hand of cards in ascending order.  For the purpose of
this exercise, we would consider ascending order to be: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, and K.

Given the following hand of cards: 2, A, 10, Q, J, and K, jot down on a piece of paper an algorithm for
sorting them in ascending order.  Test your algorithm and revise if necessary.

**Answer:** Most people would select a card that is out of place, scan through the hand for the *correct
position* and insert it there.  Repeat this process until the hand is sorted.

.. _tutorial_apcs_ap_insertion_sort_the_general_algorithm:

The General Algorithm
---------------------
Insertion sort is a more systemic approach to the algorithm discussed above.

1. Start at the beginning of the list, consider the first element to be sorted with respect to itself.
2. The list now consists of two parts: the *sorted list* (currently the first element) and the *unsorted
   list* (everything but the first element)
3. Select the first element of the unsorted list and compare it with each element to its left until you
   find an element that is smaller
4. Shift all elements to the right of this smaller element and insert the selected element in the now
   vacant spot (in the sorted list)
5. Repeat steps 3 and 4 until there are no elements left in the unsorted list.

.. image:: ../../images/apcs/ap/insertion-sort.gif
   :align: center
   :width: 300

.. _tutorial_apcs_ap_insertion_sort_exercises:

Exercises
---------
Here are some questions to ponder over (in order of ascending difficulty):

1. Is there a best case scenario?  A worse case scenario?
2. What can be said about the list about *n* passes?
3. How many passes does it take to sort a list?
4. Determine the runtime of this algorithm.  What is the ratio of the time it takes to sort the list and
   the size of the list?
   
