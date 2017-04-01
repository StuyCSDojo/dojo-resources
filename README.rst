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
Please adhere to the following rules:

* Use "=" for title of documents, "-" for title of sections, and "^" for title of subsections
* Use the |br| custom directive to move text to the next line
* Insert a newline when you want an actual line break
* For the software tips section, use the following format for labels:
  ::
    
     tutorial_<foldername>_<topic>_<description>

  Example: ``tutorial_programming_tools_emacs_emacs_tutorial``
* For the installation tips section, use the following format for labels:
  ::
  
     installation_<foldername>_<topic>

  Example: ``installation_programming_tools_emacs``
* For the stuycs section, use the following format for labels:
  ::
  
     <course>_<topic>_<heading_title>
  Example: ``intro_cs1_recursion_definitions``


Basic Structure:
::

   .. Custom directives goes here
   
   .. Title of the document goes here, underlined with "="

   .. The author's name and the date in italics

   .. Page outline in bullet point format

   .. Section label
   
   .. Section title underlined with '-'
   
   .. (Optional) Subsection label
   
   .. Subsection title underlined with '^'

Example:
::

   .. |br| raw:: html
   
      <br />
      
   Example Document
   ================

   *Written by <author name> on <year-month-day>*
   
   * :ref:`section_name_1`
   * :ref:`section_name_2`

     * :ref:`subsection_of_section_2_name_1`
     * :ref:`subsection_of_section_2_name_2`
   * :ref:`section_name_3`

   .. _section_name_1:

   Section Name 1
   --------------
   Text for Section 1
   
   .. _section_name_2:
   
   Section Name 2
   --------------
   Text for Section 2

   .. _subsection_of_section_2_name_1:
   
   Section 2 Subsection 1
   ^^^^^^^^^^^^^^^^^^^^^^
   Text for subsection of Section 2
