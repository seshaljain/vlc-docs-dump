This page is the central coordination point of the 0.9.0 QT4 Strings
review campaign, part of [[QtIntfTODO|Things to be done for the QT
Interface]]

See the [http://trac.videolan.org/vlc/ticket/1214 ticket on trac]. ==
People interested == Please sign with three tildes
<nowiki>(~~~)</nowiki> \* [[User:Tonsofpcsjb]] \* [[User:Plouj|Plouj]]

== Discussion == We have a new QT4 interface and it needs to be in
English. Discuss any issues here. \* Check the English of all strings.
Fix it. Have someone else do it again to be sure you didn't mess
something up or make something too ambiguous. \* There is no need to
change error-output strings, as it is probably best that they remain in
their original form so that they can still be found easily. If you find
any repeated error-outputs (same text for different events), inform a
developer. \* If you find any code being sent to stderr via
fprintf(stderr) rather than msg_Error, inform a developer (unless you
know how to fix it).

=== Subversion === \* subversion command for checking out just the QT4
code: <code> svn checkout
svn://svn.videolan.org/vlc/trunk/modules/gui/qt4 QT4Strings </code>

=== Nightlies === \* You can also use a nightly build to spot errors

=== What to do ===

-  [[User:J-btonsofpcs]] 01:17, 27 June 2007 (CEST)
-  Menus and systray Menu too. [[User:J-b|jb]] 08:11, 27 June 2007
   (CEST)
-  Menus, then main interface, then tooltips, then anything remaining.
   --[[User:Tonsofpcs|tonsofpcs]] 02:34, 25 October 2007 (CEST) (via j-b
   on IRC)

== Progress == \* When you begin working on a file, if necessary add it
to the table, then assign your name to it. Once you finish it, mark it
appropriately.

=== /modules/gui/qt4/util === {\| border="1" cellspacing="0" ! File \|\|
First reviewer \|\| Second reviewer \|\| Current status
customwidgets.cpp|tonsofpcs]]|tonsofpcs]] 15:47, 13 August 2008 (CEST)
input_slider.cpp|tonsofpcs]]|tonsofpcs]] 15:47, 13 August 2008 (CEST)
qvlcframe.hpp|tonsofpcs]]|tonsofpcs]] 15:47, 13 August 2008 (CEST)
registry.hpp|tonsofpcs]]|tonsofpcs]] 15:47, 13 August 2008 (CEST) }

=== /modules/gui/qt4/ === {\| border="1" cellspacing="0" ! File \|\|
First reviewer \|\| Second reviewer \|\| Current status
main_interface.cpp|\| [[User:J-b\| FX \|\| [[User:Tonsofpcs\| L \|\|
Copy edited the Privacy & Network Warning message -[[User:Tonsofpcs-\|
[[User:J-b\| No strings [[User:J-b-\| [[User:J-b\| No strings
[[User:J-b-\| [[User:J-b\| FX \|\| [[User:Tonsofpcs\| L \|\| Changed
subtitles submenu "Load file..." to "Open file..." -[[User:Tonsofpcs-\|
[[User:J-b\| No strings [[User:J-b-\| [[User:J-b\| No strings
[[User:J-b-|}

=== /modules/gui/qt4/dialogs === {\| border="1" cellspacing="0" ! File
\|\| First reviewer \|\| Second reviewer \|\| Current status
errors.cpp|\| [[User:Tonsofpcs\| [[User:Plouj\| 1 string, changed
--[[User:Tonsofpcs-\| [[User:Tonsofpcs\| No strings
--[[User:Tonsofpcs-\| [[User:Tonsofpcs\| [[User:Plouj\| 6 strings, 3
left, 2 changed ("Go to time:" instead of long sentence, lowercase
"time" in title), 1 removed (name of 'groupbox' is redundant)
--[[User:Tonsofpcs-\| [[User:Tonsofpcs\| No strings [[User:Tonsofpcs-\|
[[User:Tonsofpcs\| [[User:Plouj\| 4 strings (2 were error), <del>changed
Login >> Username</del>, replaced a fprintf(stderr) with a msg_Error
[[User:Tonsofpcs-\| [[User:Tonsofpcs\| No Strings --[[User:Tonsofpcs-\|
[[User:J-b\| \* \|\| \* \|\| No strings [[User:J-b-\| [[User:J-b\|
[[User:Tonsofpcs\| L \|\| Changed one dialog title, one dialog box error
message, one hotkey (both close and clear used &C, changed clear to &l)
--[[User:Tonsofpcs-\| [[User:J-b\| \* \|\| \* \|\| \* \|\| No strings
[[User:J-b-\| [[User:J-b\| [[User:Tonsofpcs\| \* \|\| No strings
--[[User:Tonsofpcs-\| [[User:J-b\| \* \|\| \* \|\| No strings
[[User:J-b-\| [[User:J-b\| [[User:Tonsofpcs\| \* \|\| No strings worth
changing (only "Playlist" as title) --[[User:Tonsofpcs-\| [[User:J-b\|
\* \|\| \* \|\| No strings [[User:J-b-\| [[User:J-b\| [[User:Tonsofpcs\|
L \|\| Delete >> Deletes for tooltip --[[User:Tonsofpcs-\| [[User:J-b\|
\* \|\| \* \|\| No strings [[User:J-b-\| [[User:J-b\| [[User:Tonsofpcs\|
L \|\| Change Reset preferences question to be more succinct; tooltips:
complete >> full, "Switch to [] preferences" >> "Switch to []
preferences view" --[[User:Tonsofpcs-\| [[User:J-b\| \* \|\| \* \|\| No
strings [[User:J-b-\| [[User:J-b\| [[User:Tonsofpcs\| L \|\| tooltips:
update >> change; "Save file" >> "Save file..."; \*\* NOTE: NOT CHANGED,
BUT I THINK IT SHOULD BE: "WAV" audio codec >> "PCM" with an option for
big or little endian and even 8/16/32 maybe?) --[[User:Tonsofpcs-\|
[[User:J-b\| \* \|\| \* \|\| No strings [[User:J-b-\| [[User:J-b\|
[[User:Tonsofpcs\| L \|\| buttons: Import / Export >> I&mport / E&xport;
"Choose a filename to save the VLM configuration..." >> "Save VLM
configuration as..."; "Open a VLM Configuration File" >> "Open VLM
configuration..." --[[User:Tonsofpcs-\| [[User:J-b\| \* \|\| \* \|\| No
strings [[User:J-b|jb]] 22:18, 9 July 2008 (CEST)

<!-- EXAMPLE LINE: filename.Xpp|\| ~~~ \|\| \|\| \|\| \|\| --> \|}

=== /modules/gui/qt4/components === Done. [[User:J-b|jb]] 22:38, 9 July
2008 (CEST)

=== /modules/gui/qt4/ui === Done. [[User:J-b|jb]] 22:38, 9 July 2008
(CEST)

For the done columns: :L = Done locally, not submitted :S = SVN Checked
in :P = patch submitted :F = entire file submitted (in other words, no
changes were needed) :PX = Patch submitted, checked in :FX = File
submitted, checked in

<nowiki>*</nowiki> No strings, nothing to do

[[Category:Dev Discussions]]
