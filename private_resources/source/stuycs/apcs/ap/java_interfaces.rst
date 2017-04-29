Interfaces
==========

*Written by PChan on 2017-04-25*

* :ref:`tutorial_apcs_ap_java_interfaces_overview`
* :ref:`tutorial_apcs_ap_java_interfaces_defining_interfaces`
* :ref:`tutorial_apcs_ap_java_interfaces_using_an_interface`
* :ref:`tutorial_apcs_ap_java_interfaces_calling_methods_of_interfaces`
* :ref:`tutorial_apcs_ap_java_interfaces_key_takeaway`
* :ref:`tutorial_apcs_ap_java_interfaces_the_comparable_interface`

.. highlight:: java
  
.. _tutorial_apcs_ap_java_interfaces_overview:

Overview
--------

.. glossary::
   
   Interface
      A collection of abstract methods and/or constant variables.
   
An *interface* is a contract stating that any non-abstract classes using it must define all methods in the
interface.  This provides some uniformity between all your classes without making one class a subclass of
another.

.. _tutorial_apcs_ap_java_interfaces_defining_interfaces:

Defining Interfaces
-------------------
To define an interface, you would use the ``interface`` keyword.  Here is an example:
::

   public interface Speakable{

       public String greeting = "Hello World!";
       public void speak();  // No need to add ``abstract`` as it is implicitly stated
       
   }

.. important::
   The methods you declare in the interface should have no body and typically ends with a semicolon
   instead of braces.
   
An interface is normally used to enforce the implementation of a specific set of methods.  We will
go into more details later...

.. _tutorial_apcs_ap_java_interfaces_using_an_interface:

Using an Interface
------------------
Instead of using the ``extends`` keyword, we use the ``implements`` keyword when working with interfaces.
Here is an example:
::

   public class Human implements Speakable{
   
   }

.. important::
   All methods of an implemented interface must be defined in that class unless the class is abstract.
   
If we were to use the Speakable interface defined above, then ``Human`` must define the ``speak()``
method.  Notice the similarities between *abstract classes* and interfaces where unless the class is
abstract, you need to implement all abstract methods.

.. important::
   Should you choose to have a class ``extends`` another class while implementing interfaces, make sure
   that the ``extends`` clause is before the ``implements`` clause.

Here are two examples:
::

   public class Teacher extends Human implements Speakable{
       // This is OK
   }

   public class Teacher implements Speakable extends Human{
       // This is BAD; NO GOOD!
   }

.. note::
   A class might only extend **one** class, but may implement multiple interfaces...

::

   public class Student extends Human implements Speakable, Teachable{
   
   }

When doing so, make sure to separate the interfaces with a comma.  In the example above, ``Student`` would
need to implement all the methods inside ``Speakable`` and ``Teachable``.

.. _tutorial_apcs_ap_java_interfaces_calling_methods_of_interfaces:

Calling Methods of An Interface
-------------------------------
When we talk about inheritance, we mention how you can do something like:
::

   SuperClass objectName = new SubClass();

This is possible because ``SubClass`` *is-a* ``SuperClass``.  We can do something similar with interfaces:
::

   InterfaceName object = new Class();

where ``InterfaceName`` is the name of the interface and ``Class`` is the name of the class that
implements the interface.  If we were to do ``object.method()`` and the signature for ``method()`` is
defined in the interface, it would call ``method()`` using the definition in ``Class``.  If the signature
is not in the interface, Java will throw a compiler error.

.. _tutorial_apcs_ap_java_interfaces_key_takeaway:

Key Takeaways
-------------
* Interfaces may **NOT** be instantiated
* Interfaces do **NOT** have constructors
* The subclasses of a class that implements an interface would inherit the methods of the interface
* Methods of an interface is automatically abstract; no need to specify ``abstract``
* Any variables declared in interfaces are automatically ``static`` and ``final``
* You may implement more than one interfaces
* Use the ``implements`` keyword and not the ``extends`` keyword when used with a class
* An interface may extend one or more interfaces
  ::

     public interfaceOne extends interfaceTwo, interfaceThree{
     
     }

.. _tutorial_apcs_ap_java_interfaces_the_comparable_interface:

The Comparable Interface
------------------------
For the AP, you would need to know the ``Comparable`` interface.  An example of the ``Comparable``
interface is as followed:
::

   public interface Comparable{

       int compareTo(Object obj);
       
   }

Recall that the ``compareTo()`` method provides a mean of comparing two objects and may return three type
of values: negative, 0, and positive which means that the current instance is less than, equal to, or
greater than the parameter respectively.  Any classes that implement ``Comparable`` **must** defines the
``compareTo()`` method.

.. note::
   ``Object`` is the superclass for all objects, hence the ``compareTo()`` may be used to compare the
   current instances with any objects.

.. highlight:: python
