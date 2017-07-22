Tutorial: Fixing Commits Linked to No one
=========================================

*Written by PChan on 2017-07-22*

* :ref:`tutorials_programming_tools_git_fix_commit_tutorial_the_issue`
* :ref:`tutorials_programming_tools_git_fix_commit_tutorial_solution`

.. _tutorials_programming_tools_git_fix_commit_tutorial_the_issue:

The Issue
---------
When you check the commit history, at least some of your commits are not linked to you (gray octocats as profile
pictures).

.. figure:: ../../images/software_tutorials/programming_tools/git_fix_commit/gray-octocat.png
   :align: center

   A gray octocat image instead of your profile picture

.. note::
   Ensure that this is your issue before trying the solution.

.. _tutorials_programming_tools_git_fix_commit_tutorial_solution:

Solution
--------

.. danger::
   This solution can seriously screw things over for you (and your partners) if you mistype something. Follow the steps
   with care.

Before you start...

a. Talk to your teacher about your situation.  If your teacher wants you to proceed with fixing the issue, talk to your
   partners and make sure they understand the possible consquences.  **Proceed only with your teacher consent and make
   sure your partners are aware!**
b. Do this at the Dojo with someone skilled in Git watching you.  I am **NOT** to blame if you mess up.

Instructions:

1. Make a backup of the current state of your repository.  Use ``cp`` to make a copy:

   .. code-block:: shell-session

      $ cp -r /path/to/your/repo /path/for/your/backup

2. Navigate to the root of your repository.  We will need to locate the name and email associated
   with the commits that were not linked to you.  You can do this by running:

   .. code-block:: shell-session

      $ git log

3. This will show you the history of your repository.  Press enter until you see one of your old
   commits that was done under the wrong name or email.
4. Copy down the name (next to *Author:*) and the email address (in the *<>* next to the name)
   exactly the way you see it.  Hit ``q`` when you are done.
5. Now copy (``Ctrl-C``) and paste (``Ctrl-Shift-V`` or ``Shift-Insert``) the following command into the terminal:

   .. code-block:: bash

      $ git filter-branch --env-filter '
	    oldname="(old name)"
	    oldemail="(old email)"
	    newname="(new name)"
	    newemail="(new email)"
	    [ "$GIT_AUTHOR_EMAIL"="$oldemail" ] && GIT_AUTHOR_EMAIL="$newemail"
	    [ "$GIT_COMMITTER_EMAIL"="$oldemail" ] && GIT_COMMITTER_EMAIL="$newemail"
	    [ "$GIT_AUTHOR_NAME"="$oldname" ] && GIT_AUTHOR_NAME="$newname"
	    [ "$GIT_COMMITTER_NAME"="$oldname" ] && GIT_COMMITTER_NAME="$newname"
	    ' HEAD

6. Replace *old name* in the line, ``oldname="(old name)"`` with the name that you copied down.
7. Replace *old email* in the line, ``oldemail="(old email)"`` with the email that you copied down.
8. Replace *new name* in the line, ``newname="(new name)"`` with your Github username.
9. Replace *new email* in the line, ``newemail="(new email)"`` with your Github email address.
10. Double check that you type in everything correctly.  Press enter to execute the command.
11. Run ``git log`` to review the history of the repository.  Ensure that everything looks the way it should.  **This is
    the last chance for you to correct any mistakes**

.. warning::
   Correcting mistakes after this last step is very difficult.  Make sure you are certain there are no errors.

12. Run this command to rewrite the history for the upstream repository (located at github.com):

    .. code-block:: shell-session

       $ git push -f origin

13. If everything works out, you have just successfully fixed the issue!!
