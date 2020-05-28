This page is the central coordination point of the 0.9.0 QT4 Strings review campaign, part of `Things to be done for the QT Interface <QtIntfTODO>`__

See the `ticket on trac <http://trac.videolan.org/vlc/ticket/1214>`__.

People interested
-----------------

Please sign with three tildes (~~~)

-  `tonsofpcs <User:Tonsofpcs>`__
-  `jb <User:J-b>`__
-  `Plouj <User:Plouj>`__

Discussion
----------

We have a new QT4 interface and it needs to be in English. Discuss any issues here.

-  Check the English of all strings. Fix it. Have someone else do it again to be sure you didn't mess something up or make something too ambiguous.
-  There is no need to change error-output strings, as it is probably best that they remain in their original form so that they can still be found easily. If you find any repeated error-outputs (same text for different events), inform a developer.
-  If you find any code being sent to stderr via fprintf(stderr) rather than msg_Error, inform a developer (unless you know how to fix it).

Subversion
~~~~~~~~~~

-  subversion command for checking out just the QT4 code:

``svn checkout``\ ```svn://svn.videolan.org/vlc/trunk/modules/gui/qt4`` <svn://svn.videolan.org/vlc/trunk/modules/gui/qt4>`__\ ``QT4Strings``

Nightlies
~~~~~~~~~

-  You can also use a nightly build to spot errors

What to do
~~~~~~~~~~

-  `jb <User:J-b>`__ says dialogs are free to work on at this point. --`tonsofpcs <User:Tonsofpcs>`__ 01:17, 27 June 2007 (CEST)

-  Menus and systray Menu too. `jb <User:J-b>`__ 08:11, 27 June 2007 (CEST)

-  Menus, then main interface, then tooltips, then anything remaining. --`tonsofpcs <User:Tonsofpcs>`__ 02:34, 25 October 2007 (CEST) (via j-b on IRC)

Progress
--------

-  When you begin working on a file, if necessary add it to the table, then assign your name to it. Once you finish it, mark it appropriately.

/modules/gui/qt4/util
~~~~~~~~~~~~~~~~~~~~~

================= ============================== ===== =============== ===== ===============================================================================
File              First reviewer                 Done? Second reviewer Done? Current status
================= ============================== ===== =============== ===== ===============================================================================
customwidgets.cpp `tonsofpcs <User:Tonsofpcs>`__ \*    \*              \*    No Strings -`tonsofpcs <User:Tonsofpcs>`__ 15:47, 13 August 2008 (CEST)
customwidgets.hpp `tonsofpcs <User:Tonsofpcs>`__ \*    \*              \*    No Strings -`tonsofpcs <User:Tonsofpcs>`__ 15:47, 13 August 2008 (CEST)
input_slider.cpp  `tonsofpcs <User:Tonsofpcs>`__ \*    \*              \*    No Strings -`tonsofpcs <User:Tonsofpcs>`__ 15:47, 13 August 2008 (CEST)
input_slider.hpp  `tonsofpcs <User:Tonsofpcs>`__ \*    \*              \*    No Strings -`tonsofpcs <User:Tonsofpcs>`__ 15:47, 13 August 2008 (CEST)
qvlcframe.hpp     `tonsofpcs <User:Tonsofpcs>`__ \*    \*              \*    Only Debug Strings -`tonsofpcs <User:Tonsofpcs>`__ 15:47, 13 August 2008 (CEST)
registry.cpp      `tonsofpcs <User:Tonsofpcs>`__ \*    \*              \*    No Strings -`tonsofpcs <User:Tonsofpcs>`__ 15:47, 13 August 2008 (CEST)
registry.hpp      `tonsofpcs <User:Tonsofpcs>`__ \*    \*              \*    No Strings -`tonsofpcs <User:Tonsofpcs>`__ 15:47, 13 August 2008 (CEST)
\                                                                           
================= ============================== ===== =============== ===== ===============================================================================

/modules/gui/qt4/
~~~~~~~~~~~~~~~~~

==================== ================= ===== ============================== ===== =============================================================================================================================================
File                 First reviewer    Done? Second reviewer                Done? Current status
==================== ================= ===== ============================== ===== =============================================================================================================================================
main_interface.cpp   `jb <User:J-b>`__ FX    `tonsofpcs <User:Tonsofpcs>`__ L     Copy edited the Privacy & Network Warning message -`tonsofpcs <User:Tonsofpcs>`__ 20:41, 13 August 2008 (CEST)
main_interface.hpp   `jb <User:J-b>`__ \*    \*                             \*    No strings `jb <User:J-b>`__ 22:32, 9 July 2008 (CEST)
input_manager.cpp    `jb <User:J-b>`__ \*    \*                             \*    No strings `jb <User:J-b>`__ 22:32, 9 July 2008 (CEST)
input_manager.hpp    `jb <User:J-b>`__ \*    \*                             \*    No strings `jb <User:J-b>`__ 22:32, 9 July 2008 (CEST)
dialogs_provider.cpp `jb <User:J-b>`__ FX    `tonsofpcs <User:Tonsofpcs>`__ L     Changed playlist open and save dialog titles, change subtitles open dialog title -`tonsofpcs <User:Tonsofpcs>`__ 20:41, 13 August 2008 (CEST)
dialogs_provider.hpp `jb <User:J-b>`__ \*    \*                             \*    No strings `jb <User:J-b>`__ 22:32, 9 July 2008 (CEST)
menus.cpp            `jb <User:J-b>`__ FX    `tonsofpcs <User:Tonsofpcs>`__ L     Changed subtitles submenu "Load file..." to "Open file..." -`tonsofpcs <User:Tonsofpcs>`__ 20:41, 13 August 2008 (CEST)
menus.hpp            `jb <User:J-b>`__ \*    \*                             \*    No strings `jb <User:J-b>`__ 22:32, 9 July 2008 (CEST)
qt4.hpp              `jb <User:J-b>`__ \*    \*                             \*    No strings `jb <User:J-b>`__ 22:32, 9 July 2008 (CEST)
qt4.cpp              `jb <User:J-b>`__ \*    \*                             \*    No strings `jb <User:J-b>`__ 22:32, 9 July 2008 (CEST)
\                                                                                
==================== ================= ===== ============================== ===== =============================================================================================================================================

/modules/gui/qt4/dialogs
~~~~~~~~~~~~~~~~~~~~~~~~

=============== ============================== ===== ============================== ===== ======================================================================================================================================================================================================================================================================
File            First reviewer                 Done? Second reviewer                Done? Current status
=============== ============================== ===== ============================== ===== ======================================================================================================================================================================================================================================================================
errors.cpp      `tonsofpcs <User:Tonsofpcs>`__ FX    `Plouj <User:Plouj>`__         F     1 string, changed --`tonsofpcs <User:Tonsofpcs>`__ 01:58, 27 June 2007 (CEST)
errors.hpp      `tonsofpcs <User:Tonsofpcs>`__ \*    \*                             \*    No strings --`tonsofpcs <User:Tonsofpcs>`__ 01:58, 27 June 2007 (CEST)
extended.cpp    `tonsofpcs <User:Tonsofpcs>`__ FX    `Plouj <User:Plouj>`__         FX    3 Strings, 1 change ("Synchro."->"Synchronisation") `Plouj <User:Plouj>`__ 04:14, 13 Apr 2008 (CEST)
extended.hpp    `tonsofpcs <User:Tonsofpcs>`__ \*    \*                             \*    No strings --`tonsofpcs <User:Tonsofpcs>`__ 02:06, 27 June 2007 (CEST)
gototime.cpp    `tonsofpcs <User:Tonsofpcs>`__ FX    `Plouj <User:Plouj>`__         F     6 strings, 3 left, 2 changed ("Go to time:" instead of long sentence, lowercase "time" in title), 1 removed (name of 'groupbox' is redundant) --`tonsofpcs <User:Tonsofpcs>`__ 02:12, 27 June 2007 (CEST)
gototime.hpp    `tonsofpcs <User:Tonsofpcs>`__ \*    \*                             \*    No strings --`tonsofpcs <User:Tonsofpcs>`__ 02:13, 27 June 2007 (CEST)
help.cpp        `tonsofpcs <User:Tonsofpcs>`__ PX    `Plouj <User:Plouj>`__         FX    11 strings, 2 are paths, 4 changes `Plouj <User:Plouj>`__ 04:14, 13 Apr 2008 (CEST)
help.hpp        `tonsofpcs <User:Tonsofpcs>`__ \*    \*                             \*    No strings `tonsofpcs <User:Tonsofpcs>`__ 17:27, 13 July 2007 (CEST)
interaction.cpp `tonsofpcs <User:Tonsofpcs>`__ PX    `Plouj <User:Plouj>`__         F     4 strings (2 were error), [STRIKEOUT:changed Login >> Username], replaced a fprintf(stderr) with a msg_Error `tonsofpcs <User:Tonsofpcs>`__ 17:47, 13 July 2007 (CEST)
interaction.hpp `tonsofpcs <User:Tonsofpcs>`__ \*    \*                             \*    No Strings
bookmarks.cpp   `jb <User:J-b>`__              PX    `tonsofpcs <User:Tonsofpcs>`__ \*    No Strings --`tonsofpcs <User:Tonsofpcs>`__ 03:21, 20 August 2008 (CEST)
bookmarks.hpp   `jb <User:J-b>`__              \*    \*                             \*    No strings `jb <User:J-b>`__ 22:18, 9 July 2008 (CEST)
messages.cpp    `jb <User:J-b>`__              PX    `tonsofpcs <User:Tonsofpcs>`__ L     Changed one dialog title, one dialog box error message, one hotkey (both close and clear used &C, changed clear to &l) --`tonsofpcs <User:Tonsofpcs>`__ 03:21, 20 August 2008 (CEST)
messages.hpp    `jb <User:J-b>`__              \*    \*                             \*    No strings `jb <User:J-b>`__ 22:18, 9 July 2008 (CEST)
open.cpp        `jb <User:J-b>`__              PX    `tonsofpcs <User:Tonsofpcs>`__ \*    No strings --`tonsofpcs <User:Tonsofpcs>`__ 03:21, 20 August 2008 (CEST)
open.hpp        `jb <User:J-b>`__              \*    \*                             \*    No strings `jb <User:J-b>`__ 22:18, 9 July 2008 (CEST)
playlist.cpp    `jb <User:J-b>`__              PX    `tonsofpcs <User:Tonsofpcs>`__ \*    No strings worth changing (only "Playlist" as title) --`tonsofpcs <User:Tonsofpcs>`__ 03:21, 20 August 2008 (CEST)
playlist.hpp    `jb <User:J-b>`__              \*    \*                             \*    No strings `jb <User:J-b>`__ 22:18, 9 July 2008 (CEST)
podcast.cpp     `jb <User:J-b>`__              PX    `tonsofpcs <User:Tonsofpcs>`__ L     Delete >> Deletes for tooltip --`tonsofpcs <User:Tonsofpcs>`__ 03:21, 20 August 2008 (CEST)
podcast.hpp     `jb <User:J-b>`__              \*    \*                             \*    No strings `jb <User:J-b>`__ 22:18, 9 July 2008 (CEST)
preferences.cpp `jb <User:J-b>`__              PX    `tonsofpcs <User:Tonsofpcs>`__ L     Change Reset preferences question to be more succinct; tooltips: complete >> full, "Switch to [] preferences" >> "Switch to [] preferences view" --`tonsofpcs <User:Tonsofpcs>`__ 03:21, 20 August 2008 (CEST)
preferences.hpp `jb <User:J-b>`__              \*    \*                             \*    No strings `jb <User:J-b>`__ 22:18, 9 July 2008 (CEST)
sout.cpp        `jb <User:J-b>`__              PX    `tonsofpcs <User:Tonsofpcs>`__ L     tooltips: update >> change; "Save file" >> "Save file..."; \*\* NOTE: NOT CHANGED, BUT I THINK IT SHOULD BE: "WAV" audio codec >> "PCM" with an option for big or little endian and even 8/16/32 maybe?) --`tonsofpcs <User:Tonsofpcs>`__ 03:21, 20 August 2008 (CEST)
sout.hpp        `jb <User:J-b>`__              \*    \*                             \*    No strings `jb <User:J-b>`__ 22:18, 9 July 2008 (CEST)
vlm.cpp         `jb <User:J-b>`__              PX    `tonsofpcs <User:Tonsofpcs>`__ L     buttons: Import / Export >> I&mport / E&xport; "Choose a filename to save the VLM configuration..." >> "Save VLM configuration as..."; "Open a VLM Configuration File" >> "Open VLM configuration..." --`tonsofpcs <User:Tonsofpcs>`__ 03:21, 20 August 2008 (CEST)
vlm.hpp         `jb <User:J-b>`__              \*    \*                             \*    No strings `jb <User:J-b>`__ 22:18, 9 July 2008 (CEST)
                                                                                         
                                                                                          <!-- EXAMPLE LINE:
filename.Xpp    ~~~                                                                       -->
=============== ============================== ===== ============================== ===== ======================================================================================================================================================================================================================================================================

/modules/gui/qt4/components
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Done. `jb <User:J-b>`__ 22:38, 9 July 2008 (CEST)

/modules/gui/qt4/ui
~~~~~~~~~~~~~~~~~~~

Done. `jb <User:J-b>`__ 22:38, 9 July 2008 (CEST)

For the done columns:

   L = Done locally, not submitted
   S = SVN Checked in
   P = patch submitted
   F = entire file submitted (in other words, no changes were needed)
   PX = Patch submitted, checked in
   FX = File submitted, checked in

\* No strings, nothing to do

`Category:Dev Discussions <Category:Dev_Discussions>`__
