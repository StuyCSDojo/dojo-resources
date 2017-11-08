.. |br| raw:: html

   <br />

Introduction to Arraylists
==========================

*Written by PChan on 2017-09-02*

* :ref:`tutorial_apcs_ap_arraylists_overview`
* :ref:`tutorial_apcs_ap_arraylists_declaring_arraylists`
* :ref:`tutorial_apcs_ap_arraylists_printing_arraylists`
* :ref:`tutorial_apcs_ap_arraylists_adding_to_arraylists`
* :ref:`tutorial_apcs_ap_arraylists_accessing_elements`
* :ref:`tutorial_apcs_ap_arraylists_modifying_arraylists`
* :ref:`tutorial_apcs_ap_arraylists_looping_over_arraylists`
* :ref:`tutorial_apcs_ap_arraylists_autoboxing_and_unboxing`
* :ref:`tutorial_apcs_ap_arraylists_arraylists_as_parameters`
* :ref:`tutorial_apcs_ap_arraylists_searching_for_an_element`
* :ref:`tutorial_apcs_ap_arraylists_arraylists_vs_arrays`
* :ref:`tutorial_apcs_ap_arraylists_essential_methods_reference`

.. highlight:: java

.. _tutorial_apcs_ap_arraylists_overview:

Brief Overview
--------------
After learning about arrays, you might be annoyed with their limitation and the need to resize them
after they are filled. Like arrays, ArrayLists can only hold one type of items with the further
restriction of limiting the items to objects.  However, they are dynamic in length [#]_.

.. [#] Note: ArrayLists is essentially a wrapper class for arrays that resize the underlying array for you
       when necessary.

.. _tutorial_apcs_ap_arraylists_declaring_arraylists:

Declaring ArrayLists
--------------------
Unlike arrays, you need to import ArrayList before you can use it:
::

   // Insert this at the top of the file
   import java.utils.ArrayList;

The syntax for declaring an ArrayList is as follows: ``ArrayList<type> name = new
ArrayList<type>();``.  Here ``type`` refers to an Object type.  For example:
::

   // Declare an ArrayList of Integers
   ArrayList<Integer> a = new ArrayList<Integer>();

ArrayLists may **only** hold objects and so the following declaration is invalid:
::

   // Attempt to declare an ArrayList of ints
   ArrayList<int> a = new ArrayList<int>();

.. _tutorial_apcs_ap_arraylists_printing_arraylists:

Printing ArrayLists
-------------------
Since ArrayLists are objects, you can see their contents by invoking their toString methods.  Use
the following syntax:
::

   System.out.println(object)

.. _tutorial_apcs_ap_arraylists_adding_to_arraylists:

Adding to ArrayLists
--------------------
There are three ways to add a new element: insert it at the beginning, insert it in the middle, or
insert it at the end.  This is accomplished via the ``add()`` method which takes two form:
::

   // Appending to the end
   arraylist_name.add(E element)

   // Insert at an index
   arraylist_name.add(int index, E element)

**Exercise:** Take these two methods for a test drive.  Here are a few guidelines:

1) How would you insert at the beginning?  The middle?  The end?
2) What happens when you insert at a non-existing index?
3) What if you specify a negative index?

.. _tutorial_apcs_ap_arraylists_accessing_elements:

Accessing Elements
------------------
ArrayLists use the ``get()`` method instead of the bracket notation.  The syntax is:
``arraylist_name.get(index)``.  Here are a few examples:
::

   ArrayList<String> a = new ArrayList<String>();
   a.add("hello");
   a.add("bye");
   a.get(0);         // "hello"
   a.get(1);         // "bye"

.. _tutorial_apcs_ap_arraylists_modifying_arraylists:

Modifying ArrayLists
--------------------
There are two ways of modifying ArrayLists: *changing* an element and *removing* an element.  We
will discuss how to change an element first.

To change an element, you would simply invoke the ``set()`` method.  Here is the syntax along with a
few examples:
::

   // Syntax
   arraylist_name.set(int index, E element)

   // Examples
   list.set(0, "Bye")    // Change the first element of list to "Bye"
   list.set(1, "Hello")  // Change the second element of the list to "Hello"

To remove an element, you would need to invoke one of the ``remove()`` methods.  Here are the
syntax for both methods along with a few examples:
::

   // Syntax
   arraylist_name.remove(int index)     // Remove the element at specified index
   arraylist_name.remove(Object o)      // Remove the first occurence of that element

   // Examples
   list.remove(0)                       // Remove the first element in list
   list.remove("hello")                 // Remove the first occurence of "hello" in list

.. _tutorial_apcs_ap_arraylists_looping_over_arraylists:

Looping Over ArrayLists
-----------------------
Many operations you do with ArrayLists would involve looping over them. Whether you are populating
an ArrayList or modifying an ArrayList, knowing how to loop over them can make it easier and the
impossible possible.

One important bit of information is the length of the ArrayList which can be accessed with
``<arraylist_name>.size()``. For example:
::

   ArrayList<String> list = new ArrayList<String>();
   System.out.println("The size is " + list.size())  // The size is 0

   list.add("hello");
   list.add("bye");
   list.add("food");
   System.out.println("The size is " + list.size())  // The size is 3

**Exercise:** Now that we know how to retrieve the size of an ArrayList, how would you use that
information to loop over the ArrayList?

.. warning::
   Arrays has ``array_name.length`` while ArrayLists utilizes ``arraylist_name.size()``.  This is
   one of the most common errors.

.. _tutorial_apcs_ap_arraylists_autoboxing_and_unboxing:

Autoboxing and Unboxing
-----------------------
While ArrayLists can only store objects, Java is smart enough to convert primitives into their
corresponding wrapper classes and vice versa under certain circumstances.  These mechanisms are
known as auto-boxing and unboxing respectively.

**Auto-boxing** is the concept of "boxing" the primitive into the wrapper class when the Java
compiler encounters a primitive, but expects an instance of the wrapper class.  This automatic
conversion explains why the following code compiles without errors:
::

   ArrayList<Integer> a = new ArrayList<Integer>();
   for(int i = 0; i < 10; i++){
       a.add(i);
   }

**Tip:** Try it out for yourself and see if it compiles.

Here we are able to add *ints* to an ArrayList of *Integers*.  During runtime, the Java compiler
creates an *Integer* object from *i* and adds that to *a*.

Similarly when the Java compiler encounters an instance of the wrapper class but expects a
primitive, it would convert the instance of the wrapper class to a primitve.  This conversion is
known as **unboxing** and explains why the following code also compiles without errors:
::

   // Assume we have an ArrayList, list, filled with Integers
   int sum = 0
   for(Integer i: list){
       sum += i;
   }

**Tip:** Try it out for yourself and see if it compiles.

Here we are able to add *Integers* as if they are *ints* because during runtime, the Java compiler
generates an *int* from *i* by invoking the ``intValue()`` method.

.. _tutorial_apcs_ap_arraylists_arraylists_as_parameters:

ArrayLists as Parameters
------------------------
Now that you know how to modify ArrayLists, let us look at the effects of modifying an ArrayList
when you pass it through a function. This would be left as an exercise for you, but here are some
guidelines:

1) Write a function that takes an ArrayList as a parameter. Inside the function, modify the
   ArrayList but do not return it.
2) Inside the main method, initialize an ArrayList. Print the ArrayList and then call the function
   giving it the ArrayList you just initalized as the argument.
3) Try printing out the ArrayList afterward. Did anything change?

**Reflection:** Compare your findings with what happens if you passed a primitive (boolean, int, etc)
through a function. What does this tells you about ArrayList? What benefits does this offer? Cons?

.. _tutorial_apcs_ap_arraylists_searching_for_an_element:

Searching for an Element
------------------------
Sometimes you might want to check to see if an element exists in the ArrayList or maybe you want to
find the position of an element.

One way to do this is via a linear search.  A linear search involves looping through every element
of the ArrayList and checking to see if the element at each position matches what you are looking
for.  Once found, the position or the element at that position can be returned.

**Exercise:** Try implementing a linear search for the ArrayList that would return the position of
the element that you are trying to find.

While ArrayLists also have a method for finding the index of an element, it would deepen your
learning experience if you try the exercise above first.  Here is the syntax and a few examples of
the method:
::

   // Syntax
   arraylist_name.indexOf(Object o)

   // Examples
   ArrayList<Integer> list = new ArrayList<Integer>();
   list.add(3);
   list.add(2);
   list.add(1);

   list.indexOf(3);        // 0
   list.indexOf(1);        // 2
   list.indexOf(4);        // -1 (searching for elements not in the ArrayLists would result in -1)

.. warning::
   Remember that in Computer Science, we start counting at 0.  Hence the first element is at index 0.

.. _tutorial_apcs_ap_arraylists_arraylists_vs_arrays:

ArrayLists vs Arrays
--------------------
ArrayLists and arrays are both containers for one data type.  However, there are many differences
between them that you should be aware of when choosing which data structure to use:

+--------------------+------------------------+------------------------+
|                    | ArrayLists             | Arrays                 |
+====================+========================+========================+
| Data Type          | may only store Objects | may store Objects or   |
|                    |                        | primitives             |
+--------------------+------------------------+------------------------+
| Length             | are dynamic in length  | have fixed length      |
+--------------------+------------------------+------------------------+
| Size               | have the ``size()``    | have the ``length``    |
|                    | method                 | property               |
+--------------------+------------------------+------------------------+
| Accessing Elements | have the ``get()``     | have the bracket       |
|                    | method                 | notation: ``[]``       |
+--------------------+------------------------+------------------------+

.. _tutorial_apcs_ap_arraylists_essential_methods_reference:

Essential Methods Reference
---------------------------
``boolean`` add(*E e*)
    Appends element *e* to the end of the list.  Returns true if successful.

``void`` add(*int index, E e*)
    Inserts element *e* at specified index of the list.

``void`` clear()
    Removes all elements from the list.

``boolean`` contains(*Object o*)
    Returns true if *o* is the list.
    Example: ``l.contains("string");``

``E`` get(*int index*)
    Gets element at the specified index of the list.

``int`` indexOf(*Object o*)
    Gets the first instance of *o* in the list.

``int`` lastIndexOf(*Object o*)
    Gets the last instance of *o* in the list.

``E`` remove(*int index*)
    Removes and returns the element at the specified index of the list.

``boolean`` remove(*Object o*)
    Removes the first instance of *o* in the list.  Returns true if successful.

``E`` set(*int index, E element*)
    Replaces the element at specified index with new element.  Returns the original element.

``int`` size()
    Returns how many elements are in the list

``Object[]`` toArray()
    Returns an array with the exact elements of the list.
