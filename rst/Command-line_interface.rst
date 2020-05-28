<!-- note to editors: a single space before a line will cause that line
to appear as if it were wrapped in <pre> HTML tags --> {{See
alsoConsoleDocumentation:Command line}}

This page describes how to access the terminal and start VLC in it.

A terminal is a text-based way to run programs. It is normally
pre-installed on your computer. The command prompt may also be called
the "Command Prompt", "Console", "Terminal", "MS-DOS Prompt", or
something similar.

Running VLC from the terminal gives you access to many commands and
features in VideoLAN which you would not otherwise have: see the [[VLC
command-line help]] page to find out more about options from the command
line.

Note that '''<samp>%</samp>''' is used on many of the examples on the
VLC Wiki to represent the prompt, so you don't need to type that in.<br>
Depending on your [[operating system]], the prompt could appear as a
<samp>&gt;</samp>, <samp>%</samp>, <samp>$</samp> or <samp>#</samp>
symbol. Read on for a detailed explanation.

Tip: For extended command-line work (or play) it may be worth changing
to the directory of VLC. Most command-line interpreters will understand
<code><nowiki>vlc</nowiki></code> or
<code><nowiki>vlc.exe</nowiki></code> to be the program in that
directory.

== Windows == In Windows, this is called the '''command prompt'''. To
open the command prompt: \* Click on the Start Menu and select Run. \*
In the Run box, type '''<kbd>cmd</kbd>''' (or '''<kbd>command</kbd>'''
for older versions of Windows) and press enter. The command prompt will
look something like this: C:> To run VLC, you will need to know where
you installed VLC; the default is '''<code>{{Path to
VLCdir=y}}</code>'''. So to start VLC, type the full path to VLC and the
options: {{Path to VLC|windows}} ''options'' replacing ''options'' with
the name of the file to play and its options.

== macOS == You can run VLC on [[macOS]] using a terminal application,
such as '''Terminal.app''' in '''/Applications/Utilities'''. In the
terminal window type {{Path to VLC|mac}} ''options'' replacing
''options'' with VLC options, commands, the name of the file to play,
and so on.

To suppress the launch of any Mac-like interface, <u>you have to add</u>
the Option <code>-I</code> or <code>--intf</code> followed by the
interface you want to use instead.<br> Available interfaces are: \*
''rc'' (remote control) \* ''ncurses'' (command-line-gui) \* ''http''
(web interface, usually on [[port]] 8080)—this interface will prevent
VLC from appearing even in the Dock.

In older versions you could replace the "VLC" at the end of the path
with "[[clivlc]]" to suppress the launch of any Mac-like interface.

== Linux/Unix == How to get a Linux terminal varies by distribution (for
any desktop setup it will be somewhere in the applications; these are
merely shortcuts). If you use Ubuntu or Linux Mint, gnome-terminal can
be opened with the key combination <kbd>Ctrl+Alt+T</kbd>. If you use
RHEL/Fedora/CentOS, gnome-terminal can be opened by right-clicking on
the desktop and selecting <samp>Open terminal</samp>.

By convention: \* The '''standard user''' prompt may appear as
<samp>$</samp> or <samp>%</samp> or something else.<br> \* The '''root
user''' prompt is represented with a <samp>#</samp>. This is an
indication that you must either log in as root (potential security risk)
or prefix the command with <code>sudo</code> and enter your
password.<br> To run VLC, you can normally type {{Path to VLC|linux}}
''options'' replacing ''options'' with the name of the file to play and
its options.

[[Category:Documentation]] [[Category:Coding]]
