Introduction to Arrays
======================

*Written by PChan on 2017-08-28*

* :ref:`tutorial_apcs_ap_arrays_overview`
* :ref:`tutorial_apcs_ap_arrays_declaring_arrays`
* :ref:`tutorial_apcs_ap_arrays_accessing_elements`
* :ref:`tutorial_apcs_ap_arrays_looping_over_arrays`
* :ref:`tutorial_apcs_ap_arrays_modifying_arrays`
* :ref:`tutorial_apcs_ap_arrays_arrays_as_parameters`
* :ref:`tutorial_apcs_ap_arrays_searching_for_an_element`
* :ref:`tutorial_apcs_ap_arrays_extending_arrays`

.. highlight:: java

.. _tutorial_apcs_ap_arrays_overview:

Brief Overview
--------------
In Intro to CS2, you have probably encountered Python lists, which is a data structure that allows
you to store multiple values in one variable.  Likewise, Java arrays serve as a container of a fixed
length for holding values of a single type.

.. warning::
   Unlike Python, arrays in Java have a **fixed length** and *all* values have to be of the **same type**!

Arrays are denoted with brackets and follows this general format: ``<type>[]``. The ``<type>``
before the brackets restricts the type of values the array may hold.  For example: ``int[]`` may
only hold integers, specifically *int*\ s.

.. _tutorial_apcs_ap_arrays_declaring_arrays:

Declaring Arrays
----------------
There are two ways of declaring arrays.  If you know all the values of the array beforehand, you can
use the braces notation.  For example:
::

   int[] a = {3, 4, 5};

If you would like to populate the array at a separate time or would like to do so with a loop,
declare the array first:
::

   <type>[] <name> = new <type>[<size>];

   // Example
   int[] a = new int[3];

An array declared in this manner would automatically be populated with the default value of the
type of the array.  An array declared as ``int[]`` would be filled with *0*\ s, the default value
for *int*.  However, it is still recommended and good practice to not rely on this mechanism in
your code.

We will discuss how to populate the array later after we discuss how to access values of an array.

.. _tutorial_apcs_ap_arrays_accessing_elements:

Accessing Elements
------------------
Accessing elements of the array is done with the bracket notation much like how it is done in
Python.
::

   // General Syntax
   array_name[index]

   // Example: to access the first element of array, a
   a[0]

.. warning::
   In CS, we start counting at **zero**.  The *first* element is at *index 0*, the *second* is at *index 1*,
   and so on.

.. _tutorial_apcs_ap_arrays_looping_over_arrays:

Looping Over Arrays
-------------------
Many operations you do with arrays would involve looping over them.  Whether you are populating an
array or modifying an array, knowing how to loop over them can make it easier and the impossible
possible.

One important bit of information is the length of the array which can be accessed with
``<array_name>.length``.  For example:
::

   int[] a = {1, 2, 3, 4, 5, 6};
   System.out.println("The size is " + a.length)  // The size is 6

   int[] b = new int[3];
   System.out.println("The size is " + b.length)  // The size is 3

**Exercise:** Now that we know how to retrieve the length of an array, how would you use that
information to loop over the array?  How can you print out an array?

.. _tutorial_apcs_ap_arrays_modifying_arrays:

Modifying Arrays
----------------
Modifying an array involves the bracket notation we used for accessing an element.  The general
syntax is as follows:
::

   <array_name>[<index>] = <new_value>;

For example:
::

   // Declare an array
   int[] a = {1, 2, 3};

   // Modify the array
   a[0] = 2;

   // a is now {2, 2, 3}

To remove an element from an array, you would need to create a new array and copy every elements
except for the element you wish to delete.  Then bind the new array to the original variable.

Before, we discussed how if you were to declare an array using the format, ``<type>[] <name> =
new <type>[<size>]``, the array would automatically be populated with default values.  Therefore, to
populate the array with values of your choice, you are merely modifying each entry of the array.
::

   // Populating an array
   int[] a = new int[3]

   a[0] = 1;
   a[1] = 2;
   a[2] = 3;

   // a is now {1, 2, 3}

.. _tutorial_apcs_ap_arrays_arrays_as_parameters:

Arrays as Parameters
--------------------
Now that you know how to modify arrays, let us look at the effects of modifying an array when you
pass it through a function.  This would be left as an exercise for you, but here are some
guidelines:

1) Write a function that takes an array as a parameter.  Inside the function, modify the array but
   do not return it.
2) Inside the main method, initialize an array.  Print the array and then call the function giving
   it the array you just initalized as the argument.
3) Try printing out the array afterward.  Did anything change?

**Reflection:** Compare your findings with what happens if you passed a primitive (boolean, int,
etc) through a function.  What does this tells you about arrays?  What benefits does this offer?
Cons?

.. _tutorial_apcs_ap_arrays_searching_for_an_element:

Searching for an Element
------------------------
Sometimes you might want to check to see if an element exists in arrays or maybe you want to find
the position of an element.

One way to do this is via a linear search.  A linear search involves looping through every element
of the array and checking to see if the element at each position matches what you are looking for.
Once found, the position or the element at that position can be returned.

**Exercise:** Try implementing a linear search for arrays that would return the position of the
element that you are trying to find.

.. _tutorial_apcs_ap_arrays_extending_arrays:

Extending Arrays
----------------
If you remember, an array is a container of fixed length.  This means that even if you need more
space, you cannot extend it.  In such cases, you would need to create a new array, copy the values
over, and bind the new array to the original variable.  We would leave this as an exercise.

.. highlight:: python
