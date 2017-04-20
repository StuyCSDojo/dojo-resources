Introducing Sequential vs Binary Search
=======================================

*Written by PChan on 2017-04-14*

* :ref:`tutorial_apcs_ap_sequential_binary_search_introduction_sequential_search`
* :ref:`tutorial_apcs_ap_sequential_binary_search_introduction_binary_search`
* :ref:`tutorial_apcs_ap_sequential_binary_search_introduction_summary`

.. _tutorial_apcs_ap_sequential_binary_search_introduction_sequential_search:

Sequential Search
-----------------
Sequential search, sometimes called linear search, is the most basic searching algorithm.  Start at either
end of the list and traverse the list sequentially (one-by-one) until you have found your element or until
there are no more elements to examine.

.. _tutorial_apcs_ap_sequential_binary_search_introduction_binary_search:

Binary Search
-------------
If the list that you are examining is already sorted, we can use a faster algorithm: the binary search.

1. Start searching in the middle of the array
2. Stop if you have found your element.
3. Otherwise...

   a. If the element you are looking for is greater than the middle element, examine the middle element of
      the right sublist
   b. If the element you are looking for is less than the middle element, examine the middle element of
      the left sublist
4. Repeat step 3 until you have either found your element or the sublist that you are looking for contains
   no elements

.. figure:: ../../images/apcs/ap/binary-and-linear-search.gif
   :align: center
   :width: 400

   A comparison of binary search and sequential search (linear search)
   
.. _tutorial_apcs_ap_sequential_binary_search_introduction_summary:

Summary
-------
Here are some questions to ponder over (in order of ascending difficulty):

1. When can you use the binary search?  When would you need to use the sequential search?
2. What is the best case scenario for sequential search?  Worst case scenario?
3. What is the best case scenario for binary search?  Worst case scenario?
4. Determine the runtime of the sequential search algorithm.  What is the ratio of the time it takes to
   search the list and the size of the list?
5. Determine the runtime of the binary search algorithm.  What is the ratio of the time it takes to search
   the list and the size of the list?  How does it compare with the sequential search?
