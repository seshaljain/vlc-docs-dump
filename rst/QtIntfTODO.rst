{{Historical}} = TODO 07/07 = by [[User:J-b|jb]] 22:27, 3 July 2007
(CEST)

-  [[QT4StringsReview|Strings Review]]

== Menus == \* Callbacks for checking playlist/extended
settings/advanced controls in the menu. Only playlist to do
[[User:J-bjb]] 06:27, 8 November 2007 (CET) \* Show / Hide interface
implementation Done.[[User:J-b|jb]] 22:46, 10 October 2007 (CEST)

== Dialogs == \* Open Qt4.3 fixing. Done [[User:J-bjb]] 00:13, 10
January 2008 (CET) \* DVD Win32 support. done [[User:J-bjb]] 12:54, 6
September 2007 (CEST) \* Open/Preferences Modules_Exist uses. Done
[[User:J-bjb]] 06:25, 8 November 2007 (CET) \* Extended settings
repairing. done [[User:J-b|jb]] 19:38, 3 August 2007 (CEST)

-  VLM write. Mostly Done [[User:J-b|jb]] 05:46, 20 December 2007 (CET)
-  Bookmarks write Done [[User:J-b|jb]] 00:53, 11 January 2008 (CET)
-  Help and about write. mainly done [[User:J-bjb]] 06:25, 8 November
   2007 (CET)

== Playlist == \* Choose column and remember it... done [[User:J-bjb]]
22:00, 2 August 2007 (CEST) \* Dockable. Done [[User:J-b|jb]] 22:47, 10
October 2007 (CEST)

== Main Interface == \* Dock Playlist. done [[User:J-bjb]] 05:46, 20
December 2007 (CET) \* Buttons update

== Skins2 == \* Bug fixes. see
http://mailman.videolan.org/pipermail/vlc-devel/2007-August/033930.html

= Main interface =

== Icons == === Controller Icons ===

\* ''Playback:'' \*\* Play / Pause / Stop / Next / Previous \*\* Faster
/ Slower (not urgent, unused at the time)

\* ''Volume Control:'' \*\* Sound (and sound muted if clicked)

\* Open \*\* Open File \*\* Open URL \*\* Open Disc

\* ''Other:'' \*\* Playlist \*\* Open extended GUI / Equalizer ( 1 ? 2
?) \*\* FullScreen (not urgent, unused at the time)

\* ''Playlist :'' \*\* Add file <br /> \*\* Add Folder <br /> \*\*
Shuffle <br /> \*\* Repeat One / Repeat All / Search

\* Playlist item types \*\* File \*\* Folder/Node \*\* Playlist \*\*
Network stream \*\* Disc \*\* Acquisition card

Size is up to you to decide as long as it doesn't look too big (or too
small) ...

=== Prefs Icons ===

Approx size: 50x50 pixels for Simple prefs 25x25 pixels for normal prefs
(like what we have in current wxWidgets) \* why not use 24x24 and 48x48
? [[User:Funman|funman]]

Icons needed: \* "Video" \* "Audio" \* "Input and Codecs" \* "Playlist"
\* "Interface" \* "Subtitles"

''DONE'' on March 14th.[[User:J-b|jb]] 20:15, 14 March 2007 (CET)

== General missing things ==

=== Open === \* Open file and advanced Open file merging \*\* =>
Integration of a QFileDialog ? ''Done [[User:J-b]]'' \* Open rep and
Open file merging \*\* ''Done [[User:J-b]]'' \* Generic stuff \*\*
''Done [[User:J-b]]'' \* Acquisition tabs \*\* TODO

=== Other === \* VLM \*\* \* extended dialogs \* Done by
[User:dionoeajb]] 23:48, 1 July 2007 (CEST) \* Help \* \* Bookmarks \*
Systray icon. Done [[User:J-b|jb]] 22:54, 1 July 2007 (CEST)

== Dialogs to check == \* Messages (verbosity and Save) - ''Done
[http://trac.videolan.org/vlc/changeset/18673 R18673]'' \* Information
Stats to be better - ''Done
[http://trac.videolan.org/vlc/changeset/18669 R18669]''

== Main design == \* Subclass of buttons ?

= Playlist =

-  Finish Popup handling \*\* (especially to move things between PL and
   ML)
-  A -> B repeat (loops from point to point B) \*
-  Go to time \*\* Done.[[User:J-b|jb]] 00:53, 2 April 2007 (CEST)

= Preferences =

-  Widgets \**\* Mostly done by [[User:J-b]]

Missing : \* DIRECTORY_ITEMS ''Done in''
[http://trac.videolan.org/vlc/changeset/19229 19229] \* FONT items \*
debug \* tootltip \* icons centering

= Streaming =

-  Profiles
-  We have to find an intelligent way to deal with recording

= Machine State =

There are three entry states to Qt Interface

\* Mode Integrated In this state, you start {{VLC}} as a MPC or WMP.
When you start VLC, you have a black video with a cone in the interface,
like this one
([http://www.softpedia.com/screenshots/Media-Player-Classic-for-Win2kXP_1.png]).
Your playlist is integrated in the interface like WMP. When you play
music, the video_plugins are integrated in the intf. Extended GUI is
separated (?)

\* Mode Desintegrated In this states, you start {{VLC}} as a vlc -Iwx
--no-wx-embed, everything is separated, Video, playlist, etc... You can
stack the extended GUI.

\* Mode Minimal This is the same mode as the Mode Integrated, but has no
menu, no control at all. Everything is controlled by right click ! A
hotkey combinaison can lead you to show the menu and the controls and
you are back to Mode Integrated.

\* ASCII schema <pre> MM ↑ ↓ MI <====> MI_pl_detached ↑ ↑ ↓ ↓
MI_video_detached <=> MD <====> MD_extended_GUI_integrated

</pre>

Notes : \* Extended GUI is always detached by default (?)

= Issues =

Some current issues being worked on or looked into.. latest reference
svn-16791.

Bugs: \* Add a file to the playlist, drag and drop to the left panel on
Playlist or Media library icon, double click on that icon (that will
expand it and show the element just added), double click on the element
-> CRASH \* Tools, Interface, Console (problem only applies to this
option), File open file, play, close with X -> continues playing (while
the vout is destroyed, audio goes on) until the Console window is
"selected", then the clip really "quits". \* Height consistency on
Tools, Preferences, "Basic". The Video, Audio etc. option text consists
of about 4 lines height. On "All", the Advanced is only one line, while
the expanded options like CPU features, Filters etc. are 2 lines again.
\* File location of playing item in Windows shows forward instead of
backslash (also in playlist items) -- Hum ? Looks like a core issue ?
[[User:Zorglub]] -- CRASH issue when opening a 2nd file. main debug:
adding item <garbage>. Does not happen in WX. When media files are in
the default folder (Application Data?) then no problems occur since no
path needs to be selected. Also qt4 in gdb refuses to open a file
[[User:Trax]]

Unreproducible (in linux): \* Preferences, All, Audio, Filters, select
Headphone then Equalizer, the show settings (to select Basic or All) and
the whole left section suddenly becomes very wide/stretched. Same goes
for selecting Filters, parametric equalizer right away. \* Interface,
Main Interface, Skins, 2 entries of enable transparency effects

Missing stuff: \* File, Open .. think there should be a "All media
types, or all supported types" listed which is default. (Also some File
type listings have a space in front of them).

No fix possible or invalid:

Fixed:

= Mockups =

Since I (pherthyl) am (going to be) helping with the Qt interface, I
thought I'd keep a page of mockups for new UI ideas. While there are
some things we need to copy from the wxWidgets interface, there are also
lots of non-optimal bits of UI in the old interface that I think we
should improve. Since the Qt interface isn't out yet, now is the time to
make changes like this.

[[QtIntfMockups]] [[Category:Dev Discussions]] [[Category:Qt]]
