{{See alsoCategory:Control VLC}}

Interfaces are the way you interact with {{VLC}}. Like anything else in
VLC, they are modules, which allows for their interchangeability
([[#Using|see below]]).

== Main interfaces == VLC has four main graphical interfaces: \* The
[[Qt Interface]] (qt) is the default interface on [[Linux]] and
[[Windows]] starting with version 0.9.0. : Used to be [[wxWidgets
Interface]] (wx) before. \* The [[Skins|skins2 Interface]] is an
interface where you can customize VLC's look (works on Linux and
Windows). \* The [[macOS Interface]] is the default (and only) graphical
interface on [[macOS]]. \* The [[BeOS Interface]] is the default (and
only) graphical interface on [[BeOS]].

== Full list == Besides the above main interfaces, VLC contains many
more: {\| Current (>=0.9.0) default [https://www.qt.io/ Qt4] interface
on [[Linux]] and [[Windows]]. '''wx''' \| Previous (<0.9.0) default
[http://www.wxwidgets.org/ wxWidgets] interface on [[Linux]] and
[[Windows]]. '''skins2''' \| Load VLC with a [[skin]]. (Linux and
Windows only) '''macosx''' \| Default [[Mac OS X]] interface.
'''minimal_macosx''' \| Minimal [[Mac OS X]] interface. '''beos''' \|
Default [[BeOS]] interface. '''http''' \| [[Web Interface]], used for
controlling VLC from over a network. '''gestures''' \| [[Mouse
Gestures]], where you can control VLC by moving the mouse '''rc''',
'''ncurses''', '''telnet''' \| [[Console-\| '''showintf''' \| Show
interfaces module. '''hotkeys''' and '''joystick''' \| Control VLC with
the keyboard/joystick (see [[HotKeys]]). '''dummy''' \| Don't use an
interface ([[HotKeys]] still available). \|}

== Listing the available interfaces ==

To get a list of available interfaces, running VLC with the <code>-l</code> option:
   {{%}} vlc -l

This also displays the [[muxers]] and [[encoders]]/[[decoders]] and puts it in a file called <code>vlc-help.txt</code>. On Linux, run
   {{%}} vlc -l \| grep -iF interface

to display the interfaces.

== <span id="Using"></span> Using an interface ==

To run VLC with a different primary interface, use the following command:
   {{%}} vlc --intf ''name''

You can also use
   {{%}} vlc -I ''name''

You can also change the default in the [[Preferences]].

However, you can also launch more than one interface:
   {{%}} vlc --intf qt --extraintf sap,telnet,http

This will launch VLC with the default Qt interface, but will also launch
the [[SAP]], [[telnet]] and [[web interface]] in addition to the Qt one.
The default for this can also be changed in the preferences.

Note that if you only use the [[dummy]] interface, you won't be able to
tell vlc to quit (except watching a video). You may have to break it
manually with <kbd>Ctrl+C</kbd>; or use <code>vlc://quit</code> as the
last item on the playlist.

[[Category:Control VLC\|\ *]] [[Category:Interfaces\|*]]
