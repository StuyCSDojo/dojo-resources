Abstract Classes and Methods
============================

*Written by PChan on 2017-04-25*

* :ref:`tutorial_apcs_ap_java_abstract_classes_and_methods_overview`
* :ref:`tutorial_apcs_ap_java_abstract_classes_and_methods_defining_abstract_classes_and_methods`
* :ref:`tutorial_apcs_ap_java_abstract_classes_and_methods_key_takeaways`

.. _tutorial_apcs_ap_java_abstract_classes_and_methods_overview:

Overview
--------

.. glossary::

   Abstract Method
      A method without a body (merely the return type and the signature).

   Abstract Class
      A class that represents something *abstract* like an idea.
   
Some of the methods inside an abstract class may be undefined because there is no valid definition for
them.  These methods must be defined in the subclasses unless the subclass is *abstract* as well.  This
enforces a degree of uniformity between your classes.

.. _tutorial_apcs_ap_java_abstract_classes_and_methods_defining_abstract_classes_and_methods:

Defining Abstract Classes and Methods
-------------------------------------
An *abstract method* is declared by adding the ``abstract`` keyword after the visibility and before the
return type:
::

   // General Syntax
   public abstract returnType methodName();

   // Example
   public abstract double area();

Generally, an abstract method would not have an body as you would need to override the definition anyway.
But, adding a body would not cause an error.

If you have at least one *abstract method* in a class, you must make the class *abstract* like so:
::

   // General Syntax
   public abstract class AbstractClass{
   
   }

   // Example
   public abstract class Quadralateral{
   
   }

.. warning::
   An *abstract method* must be inside an *abstract class*.  However, an *abstract class* does **NOT**
   have to contain an *abstract method*.

You would extend an *abstract class* the way you would extend any other classes:
::

   public class SubClass extends AbstractClass{
   
   }

.. _tutorial_apcs_ap_java_abstract_classes_and_methods_key_takeaways:

Key Takeaways
-------------
* Unless the subclass of an *abstract class* is declared *abstract*, it must implement all methods in the
  *abstract class*
* An *abstract class* **CAN NOT** be instantiated directly; it may be used as the type of a variable
* The keyword ``abstract`` is used to declare *abstract methods* and *abstract classes*
* *Abstract methods* typically do not have any valid definitions and each subclass would have its own
  implementation
* *Abstract classes* may include constructors, but they **CAN NOT** be used to create an instance of the
  class
* *Abstract methods* must be inside *abstract classes*, but *abstract classes* need not contain *abstract
  method*
