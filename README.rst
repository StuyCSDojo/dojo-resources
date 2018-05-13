Dojo Resources
==============

.. contents::

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
  * The latest "stable" version whose content are accessible to the general public (password protected
    while under testing)

Setting Things Up
-----------------

During Development
^^^^^^^^^^^^^^^^^^
This repository contains a standalone Flask app that is used to test your changes before pushing them to
upstream.  Before modifying files in this repo, you should prepare the developer environment as per the
instructions found at `Dojo Documentation <https://dojo.stuycs.org/docs>`_.

Before running the Flask app, make sure you:

* Activate the virtualenv

  .. code-block:: bash

     $ cd path/to/virtualenv
     $ cd virtualenv
     $ source bin/activate

* Install and start up Mongod, instructions can be found `here <https://dojo.stuycs.org/resources/software_installation_and_tips/installation_instructions/programming_tools/installing_mongodb.html>`_.

Run the Flask app by:

.. code-block:: bash

   $ cd path/to/dojo-resources
   $ cd dojo-resources/app
   $ python api.py

The first time you run the Flask app, make sure you:

* Register an account at <http://localhost:5000/testing/register/>
* Stop the Flask app
* Promote yourself to developer privileges

  .. code-block:: bash

     $ cd lib/security
     $ python
     >>> from AuthManager import AuthManager
     >>> auth_manager = AuthManager('dojo_website')
     >>> auth_manager.make_developer(<your username>)
     (True, 'User is now a developer!')
     >>> exit()

* Run the Flask app again

  .. code-block:: bash

     $ cd ../..
     $ python api.py

Production Server
^^^^^^^^^^^^^^^^^
On the local machine:

.. code-block:: bash

   $ cd path/to/virtualenv
   $ cd virtualenv
   $ source bin/activate
   $ cd ..
   $ mkdir testing_directory
   $ cd testing_directory
   $ git clone git@github.com:StuyCSDojo/dojo-resources
   $ cd dojo-resources/app/
   $ python api.py

**Double check that the version accessible at** http://localhost:5000 **is what you want on the server.**
**The general public will be seeing what you see at** http://localhost:5000/testing/public/resources\ **.**

On the production server:

.. code-block:: bash

   $ cd /projects/
   $ source dojo/bin/activate
   $ cd dojo-website/app/resources
   $ git reset --hard && git pull
   $ cd ..
   $ ./start_server

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
