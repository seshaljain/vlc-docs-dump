.. raw:: mediawiki

   {{Historical}}

   *Replaced with*\ `Git <Git>`__

Introduction to SVN
-------------------

Some VideoLAN's repositories are using `Subversion <https://subversion.apache.org>`__, which is a classical VCS, like CVS. It also provides a better control over the repository compared to CVS.

Note that some project, like or x264 are using Git. You can read more about VideoLAN's git repository in our `Git wiki page <Git>`__.

**Currently the Subversion repositories are discontinued on VideoLAN.**

How to use it
~~~~~~~~~~~~~

To use it, you have to download the `official command line Subversion client <https://subversion.apache.org>`__. You can also use alternative clients, such as the graphical `TortoiseSVN <http://tortoisesvn.tigris.org/>`__ for Windows.

When using `Cygwin <Cygwin>`__ as compilation environment it is recommended to use the SVN package that comes with it (using the Cygwin setup). Using an "external" SVN application might otherwise cause problems with so called DOS versus UNIX "line endings" when creating files.

Subversion's command-line interface is generally pretty similar to CVS. This is a **basic** and partial guide of the most useful commands. For a complete guide, use the book `Version Control with Subversion <http://svnbook.red-bean.com/en/1.2/index.html>`__. If you have a write access to the server, it's very recommended that you read it and know about the advanced features of Subversion, because you might use them sooner or later.

Anonymous use
-------------

If you don't have a write access to the repository, you have to access it anonymously, via regular SVN. However, most of the techniques shown here may be useful also for developer use, so please read it even if you don't have to access the server anonymously.

Check out
~~~~~~~~~

First, you have to check out the code of libdvbpsi. Use the following syntax:

``{{%}} svn checkout svn://svn.videolan.org/libdvbpsi/trunk libdvbpsi-trunk``

You can browse the code structure using on the `SVN webviewer <http://svn.videolan.org>`__ Use the three folders there for different purposes:

-  

   .. raw:: mediawiki

      {{SVNSourceFile|name=trunk|repo=libdvbpsi}}

   is the main development branch.

-  The are used for stable versions and for the development of complex features.
-  The are used to track the released versions.

The URL structure is:

transport : svn://svn.videolan.org
project repository : /libdvbpsi
branch/tag : /trunk, or /branches/0.8.6, or /tags/0.8.5
files : /README

You can also checkout a portion of the SVN using the URL.

**Don't leave off the "trunk" or branch part!** If you leave that off you check out every revision of every file in the repo, which is pretty silly.

Projects on VideoLAN's SVN
~~~~~~~~~~~~~~~~~~~~~~~~~~

All projects from VideoLAN SVN are moved to gitlab on code.videolan.org.

Updating the working copy
~~~~~~~~~~~~~~~~~~~~~~~~~

To update your working copy and get the latest files, use the following command:

``{{%}} svn update``

Note that SVN, unlike CVS, doesn't need to be told to prune removed files or create new directories. This is automagic.

Making a diff
~~~~~~~~~~~~~

Diffs, or patches, are text files which include all the changes done in the working copy. If you suggest a new feature or like to suggest a change, send a patch to the mailing-list with [PATCH] in the subject.

To create a diff from the current repository, use the following command:

``{{%}} svn diff``

Normally, unlike CVS, you don't have to tell SVN which files you changed; however, you may like to diff only a part of the repository. To do that, specify the files to diff:

``{{%}} svn diff modules/gui/qt4/qt4.hpp``

Note that SVN defaults to the "unified" diff format, so the "-u" option doesn't have to be passed.

Applying a diff
~~~~~~~~~~~~~~~

Subversion does not contain a built in command to apply diffs to the current working copy (for example, to review or commit diffs published in Bugzilla); instead, you can use the regular `patch <wikipedia:patch_(Unix)>`__ unix utility:

``{{%}} patch -p0 < patch``

TortoiseSVN has a built-in support for applying a diff.

.cvsignore / Ignoring files
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can ignore some files, using metadata:

``{{%}} svn propedit ``\ ```svn:ignore`` <svn:ignore>`__\ `` mydirectory``

Changing file structure
~~~~~~~~~~~~~~~~~~~~~~~

Add a file
^^^^^^^^^^

You can add files or folders to the working copy, to be included in the next diff or commit, using the command:

``{{%}} svn add file.name``

If file.name is a text-based document, you should do

``{{%}} svn propset ``\ ```svn:eol-style`` <svn:eol-style>`__\ `` native file.name``

If you add a folder, it will add all the files included in the folder, except for files in the ignored list.

Delete a file
^^^^^^^^^^^^^

You can delete files or folders from the working copy, to be deleted in the next commit or marked as such in the next diff, using the command (which will automatically **delete** the files from the working copy, but won't delete folders in such way):

``{{%}} svn delete file.name``

Make sure the file or folder do not have local modifications, else they won't be deleted unless you force the deletion.

Move a file
^^^^^^^^^^^

You no longer create new files from scratch when moving files!

``{{%}} svn mv file1 file2``

You can also do it with entire folders.

Reverting your changes
~~~~~~~~~~~~~~~~~~~~~~

If your changes in the working copy are not useful in your opinion, you can revert them using the following command:

``{{%}} svn revert``

You must use parameters for this command. To revert all your changes in the working copy, use:

``{{%}} svn revert -R .``

To revert the changes in a specific file, use:

``{{%}} svn revert file.name``

Reverting can also remove added files (they won't be deleted, just removed and considered "unknown files", just like you didn't use ``svn add`` at first), and restore deleted files (both deleted by hand and deleted by ``svn delete``).

Checking the status of the working copy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can check the status of your working copy using the following command:

``{{%}} svn status``

These are several important letters in the first column of the item, which show the status:

-  M = the item was modified by you
-  A = the item was added by you (using ``svn add``)
-  D = the item was deleted by you (using ``svn delete``)
-  ? = the item is not under the version control, but exist
-  ! = the item is missing (under the version control, but not exist - probably deleted without using ``svn delete``) or incomplete

Checking out specific revision number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can check specific repository revision using following command :

``{{%}} svn checkout -r 12345 ``\ ```svn://svn.videolan.org/libdvbpsi/trunk`` <svn://svn.videolan.org/libdvbpsi/trunk>`__\ `` libdvbpsi-trunk``

Developer use
-------------

If you have a write access for the server, you can use an SSH access instead of HTTP access.

Commits
~~~~~~~

Commits, or check ins, are the action of applying your changes from the working copy to the web repository. Use the following command to do that:

``{{%}} svn commit``

Using the command without the parameters will fail, unless you've configured an editor, because you have to enter a comment for the file logs. You can use one of the following forms:

| ``{{%}} svn commit --message="This is the log comment."``
| ``{{%}} svn commit --file=file_with_log_comment``

Other commands
~~~~~~~~~~~~~~

| ``{{%}} svn export``
| ``{{%}} svn propedit``

Are documented in the `SVN Book <http://svnbook.red-bean.com/en/1.2/index.html>`__ that you should definitively read.

External links
--------------

-  `Subversion Web access <http://svn.videolan.org>`__
-  `Version Control with Subversion <http://svnbook.red-bean.com/en/1.2/index.html>`__ book (SVN version 1.2)

`Category:Building <Category:Building>`__ `Category:Coding <Category:Coding>`__
