{{Howto|jump to a certain time in a video}}

== Graphical == [[File:Go to time - VLC 3.0.6 Linux.pngrightalt=]]

In the menu bar select '''Playback''' → '''Jump to Specific Time'''.
Alternatively, press <kbd>Ctrl+T</kbd>. Enter the hours, minutes, and
seconds.

== Command-line == To seek from the command-line, use <code>--start-time
<seconds></code> to skip the beginning or <code>--stop-time
<seconds></code> to skip the end. As of VLC version 1.0.0 sub-second
values are accepted. Example: {{%}} vlc --start-time=83.4
--stop-time=300 BigBuckBunny.ogv Plays an open-source movie starting at
1 minute 23.4 seconds and ending at 5 minutes.

Advanced users: playback control is documented in <code>vlc
--module=core --advanced</code>

{{VSG}}

[[Category:GNU GPL Licensed pages]]
