.. |br| raw:: html

   <br />

Basic Java Features
===================

*Written by PChan on 2017-04-12*

* :ref:`tutorial_apcs_ap_introductory_java_features_types`
* :ref:`tutorial_apcs_ap_introductory_java_features_identifiers`
* :ref:`tutorial_apcs_ap_introductory_java_features_operators`

  * :ref:`tutorial_apcs_ap_introductory_java_features_arithmetic_operators`
  * :ref:`tutorial_apcs_ap_introductory_java_features_relational_operators`
  * :ref:`tutorial_apcs_ap_introductory_java_features_logical_operators`
  * :ref:`tutorial_apcs_ap_introductory_java_features_assignment_operator`
  * :ref:`tutorial_apcs_ap_introductory_java_features_operator_precedence`

.. highlight:: java

.. _tutorial_apcs_ap_introductory_java_features_types:

Data Types
----------
Java is a statically typed language.  This means that not only does each variable have to be declared with
a type, it may only store values of that type. The type may fall under one of two categories: primitives
and objects.

Primitives
^^^^^^^^^^
Primitives are predefined by Java with the usage of reserved keywords.  There are 8 in total:

+----------+--------------+---------------------+
| Integers | Memory Space | Range               |
+==========+==============+=====================+
| byte     | 8 bits       | [-2^7, (2^7) - 1]   |
+----------+--------------+---------------------+
| short    | 16 bits      | [-2^15, (2^15) + 1] |
+----------+--------------+---------------------+
| int      | 32 bits      | [-2^31, (2^31) + 1] |
+----------+--------------+---------------------+
| long     | 64 bits      | [-2^63, (2^63) + 1] |
+----------+--------------+---------------------+

+----------------+--------------+
| Floating Point | Memory Space |
+================+==============+
| float          | 32 bits      |
+----------------+--------------+
| double         | 64 bits      |
+----------------+--------------+

+---------+--------------+--------------------------+
| Other   | Memory Space | Possible Values          |
+=========+==============+==========================+
| boolean | Varies       | true, false              |
+---------+--------------+--------------------------+
| char    | 16 bits      | single Unicode character |
+---------+--------------+--------------------------+

.. important::
   By the standard Java naming convention, primitives are composed **only** of lowercase letters.
   
Objects
^^^^^^^
Everything that is not a primitive is an object which is composed of what it can do (action) and what it
knows (data).  For now, just know that names of Objects in Java are camel-cased.  Therefore, the first
letter of each word is capitalized and spaces between words are eliminated.

For example:

* donut --> Donut
* little sister --> LittleSister

.. note::
   Notice how we do not insert underscores, hypens, or spaces in between each word. Spaces are completely
   forbidden in names of Objects and identifers in general.

.. _tutorial_apcs_ap_introductory_java_features_identifiers:
   
Identifiers
-----------
In computer science, identifiers refer to any user-defined word.  This may include variable names,
function names, and etc.  The rules of Java identifiers are simple:

* Case-Sensitive
* Must **NOT** be a Java reserved keyword
* The first letter of an identifier may be a underscore (``_``) or an alphabetic character
* The rest of the identifier must be alphanumeric characters

Here are some examples:
  
=================  ===================
Valid Identifiers  Invalid Identifiers
=================  ===================
_abc               123
abc                1_a2
bc123              %a2
_123               a#24
_a1                for
a_2                hello world
=================  ===================

.. important::
   There are no spaces in Java identifiers and they are case-sensitive.  ``For`` is valid while ``for`` is
   not.

.. _tutorial_apcs_ap_introductory_java_features_operators:

Operators
---------

.. _tutorial_apcs_ap_introductory_java_features_arithmetic_operators:

Arithmetic Operators
^^^^^^^^^^^^^^^^^^^^
We will start with the most basic type of operators: *arithmetic operators*.  The four basic operators
should look familiar to you, but the modulus operator might be new to you:

========  ================================================================================
Operator  Meaning
========  ================================================================================
\+        Add or concatenate the two operands
\-        Subtract the second value from the first value
\*        Multiply the two operand
/         Divide the first value by the second value
%         Remainder of left-hand operand divided by right-hand operator (Modulus operator)
========  ================================================================================

.. note::
   Java does not have a exponent operator; you need to make a function call instead.

.. _tutorial_apcs_ap_introductory_java_features_relational_operators:
   
Relational Operators
^^^^^^^^^^^^^^^^^^^^
Next, we will take a look at *relational operators*.  These operators are used to make a comparison and
return a boolean value:

========  =====================================================================
Operator  Meaning
========  =====================================================================
==        Check if two values are equal (``=`` is reserved for assignment)
!=        Check if two values are not equal
>=        Check if the first value is greater than or equal to the second value
<=        Check if the first value is less than or equal to the second value
>         Check if the first value is *strictly* greater than the second value
<         Check if the first value is *strictly* less than the second value
========  =====================================================================

.. warning::
   These operators would only work with primitives and may give the wrong answers for Objects.

Due to the way how floating-point values are stored, you might not always get the correct answer if you
used the relational opeators incorrectly due to round-off errors.  Instead, you should test to see if they
are close enough in precision to be considered equal:

.. math::

   \mathopen|x - y\mathclose| \leq \epsilon max(\mathopen|x\mathclose|, \mathopen|y\mathclose|)

where :math:`\epsilon` is a very small number.

.. _tutorial_apcs_ap_introductory_java_features_logical_operators:
	
Logical Operators
^^^^^^^^^^^^^^^^^
The next type of operators we would look at is: *logical operators*.  These are used to chain boolean
expression together.

========  ================================================================  ======
Operator  Meaning                                                           Usage
========  ================================================================  ======
&&        Logical AND operator, return true if both operands are true       A && B
||        Logical OR operator, return true if at least one operand is true  A || B
!         Logical NOT operator, return true if operand is false             !(A)
^         Logical XOR operator, return true only if one operand is true     A ^ B
========  ================================================================  ======

.. tip::
   The pipe (``|``) character can be accessed with ``Shift-\``.

Java uses **short-circuit evaluation** for logical operators.  This means that it would try to do as
little work as possible:

* For ``&&``...
  
  If the first operand of ``&&`` is false, then it would skip the evaluation of the second operand as the
  value of the second operand would not affect the result of the expression (false)
* For ``||``...
  
  If the first operand of ``||`` is true, then it would skip the evaluation of the second operand as the
  value of the second operand would not affect the result of the expression (true)
  

.. _tutorial_apcs_ap_introductory_java_features_assignment_operator:
   
Assignment Operator
^^^^^^^^^^^^^^^^^^^   
The last type of operators we would look at is: *assignment operator*.  It is used to bind a value to a
variable.

========  ================================================================
Operator  Meaning 
========  ================================================================
=         Bind the right hand value to the left hand variable
========  ================================================================

.. note::
   There are a few others which we will cover later...

.. _tutorial_apcs_ap_introductory_java_features_operator_precedence:
   
Operator Precedence
^^^^^^^^^^^^^^^^^^^
It is important to know the precedence of Java operators.  In the table below, the smaller the level, the
higher the precedence:

+----------+-------+---------------+
| Operator | Level | Associativity |
+==========+=======+===============+
| !        |   1   | Right to left |
+----------+-------+---------------+
| \*       |   2   | Left to right |
| |br|     |       |               |
| /        |       |               |
| |br|     |       |               |
| %        |       |               |
+----------+-------+---------------+
| \+       |   3   | Left to right |
| |br|     |       |               |
| \-       |       |               |
+----------+-------+---------------+
| >=, >    |   4   | Left to right |
| |br|     |       |               |
| <=, <    |       |               |
+----------+-------+---------------+
| ==       |   5   | Left to right |
| |br|     |       |               |
| !=       |       |               |
+----------+-------+---------------+
| ^        |   6   | Left to right |
+----------+-------+---------------+
| &&       |   7   | Left to right |
+----------+-------+---------------+
| ||       |   8   | Left to right |
+----------+-------+---------------+

.. note::
   To change the order of precedence and/or make your code more readable, wrap your expressions around
   parentheses which has a higher precedence than everything else.
