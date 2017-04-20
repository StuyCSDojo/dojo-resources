Introducing MergeSort
=====================

*Written by PChan on 2017-04-14*

* :ref:`tutorial_apcs_ap_mergesort_introduction_key_idea_splitting`
* :ref:`tutorial_apcs_ap_mergesort_introduction_key_idea_merging`
* :ref:`tutorial_apcs_ap_mergesort_introduction_the_general_algorithm`
* :ref:`tutorial_apcs_ap_mergesort_introduction_exercises`

.. _tutorial_apcs_ap_mergesort_introduction_key_idea_splitting:

Key Idea: Splitting a List
--------------------------


.. _tutorial_apcs_ap_mergesort_introduction_key_idea_merging:
  
Key Idea: Sorting Two Sorted Lists
----------------------------------
In this section, we would discuss how to sort two given lists that are already sorted.  The goal here is
to take advantage that the two lists are already sorted; we want to avoid sorting the combined list.

Given the following lists:
::

   A = [1, 3, 5, 7, 9]
   B = [2, 4, 6, 8, 10]

Jot down on a piece of paper an algorithm for sorting the two lists.  Test out your algorithm and revise
it if necessary.

**Answer:** 

1. Compare the first element of both lists
2. Remove the smaller of the two and insert it into a new list
3. Repeat steps 1 and 2 while both lists are non-empty
4. If one list is empty, append its remaining element to the new list in the exact same order
5. Once both lists are empty, the new list should contain the elements of both lists in ascending order

.. _tutorial_apcs_ap_mergesort_introduction_the_general_algorithm:
   
The General Algorithm
---------------------
Once you have gotten down the merging routine, the rest of the mergesort algorithm is very simple.

1. If the size of the given list is 1, return that list
2. Otherwise, split the given list in half
3. Repeat steps 1 and 2 for each sublist until they are of size 1
4. Merge each half together using the algorithm discussed above

.. image:: ../../images/apcs/ap/mergesort.gif
   :align: center
   :width: 400

.. _tutorial_apcs_ap_mergesort_introduction_exercises:

Exercises
---------
Here are some questions to ponder over (in order of ascending difficulty):

1. Is there a best case scenario?  A worst case scenario?
2. How many times do you need to half the list before you can start merging
3. What disadvantage(s) does mergesort have compared to other sorting algorithms?
4. Determine the runtime of this algorithm.  What is the ratio of the time it takes to sort the list and
   the size of the list?
