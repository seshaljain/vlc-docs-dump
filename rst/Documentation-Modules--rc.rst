{{Moduletype=Interface|description=Text based command interface}}

== Introduction == The remote control interface (rc for short) is one of
the three console interfaces provided by VLC. The other two being
[[Documentation:Modules/ncursestelnet]].

To force VLC into using this interface, do the following:

   {{%}} vlc -I rc

This interface is operated through textual commands typed into the
invoking terminal window.

This is the default interface if no [[GUI]] environment is available.

== Command reference == Type <tt>help</tt> followed by enter for a terse
list of commands or <tt>longhelp</tt> for the complete list.

<!-- Paste help and/or longhelp output here -->

== Command line options == There are several options you can use in
conjunction with the rc interface:

{\| \| '''Option''' \| '''Description''' \| '''Enabled by default'''
<tt>--rc-show-pos</tt> \| Show stream position \| No
<tt>--no-rc-show-pos</tt> \| Show the current position in seconds within
the stream from time to time. \| No <tt>--rc-fake-tty</tt> \| Fake TTY
\| No <tt>--no-rc-fake-tty</tt> \| Force the rc module to use stdin as
if it was a TTY. \| No <tt>--rc-unix=<string></tt> \| UNIX socket
command input. Accept commands over a Unix socket rather than stdin. \|
<nowiki>-</nowiki> <tt>--rc-host=<string></tt> \| TCP command input.
Accept commands over a socket rather than stdin. You can set the address
and port the interface will bind to. \| <nowiki>-</nowiki>
<tt>--rc-quiet</tt> \| Do not open a DOS command box interface
<tt>--no-rc-quiet</tt> \| By default the rc interface plugin will start
a DOS command box. Enabling the quiet mode will not bring this command
box but can also be pretty annoying when you want to stop VLC and no
video window is open. \| No \|}

To get this list run
   vlc -p rc --advanced --help-verbose

== Miscellaneous == Starting with VLC 0.8.0 you can access this
interface through a network with a telnet-client by using the
<tt>--rc-host localhost:port</tt> option.
