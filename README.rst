Dojo Resources
==============

* `What is Here`_
* `RST Convention`_


What is Here
------------
This repository contains the files behind the Dojo Website resources section. There are three directories:

* **app/**

  * Contains a standalone Flask app for accessing the pages of the private resources section and public
    resources section
* **private_resources/**

  * Contains the rst source files and the html files for the private version
  * This is meant to be accessible by teachers and the developers because it contains beta content
* **public_resources/**

  * Contains the rst source files and the html files for the public version
  * The latest "stable" version whose content are accessible to the general public

RST Convention
--------------

::

   The first line should be the title of the document, underlined with "="

   Next, is any custom directives such as:
   .. |br| raw:: html

      <br />

   Next, in italics is the author's name and date written like the following:
   *Written by <author name> on <year-month-day>*

   Then, we have an outline for the page in the following format:
   * :ref:`section_name_1`
   * :ref:`section_name_2`

     * :ref:`subsection_of_section_2_name_1`
     * :ref:`subsection_of_section_2_name_2`
   * :ref:`section_name_3`

   This is followed by the reference label for section 1:
   .. _section_name_1:

   Afterward is the heading for section 1, underlined with "-"

   Any subsections should be preceded with the corresponding reference label; the subsection
   heading should be underlined with "^"
   
