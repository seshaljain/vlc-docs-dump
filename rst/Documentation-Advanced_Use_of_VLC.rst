{{RightMenu|Documentation TOC}}

== Use the command line == '''TODO: completely outdated''' {{Outdated}}

All standard operations of VLC should be available from the GUI.
However, some complex operations can only be done from the command line
and there are situations in which you don't need or want a GUI. Here is
the complete description of VLC's command line and how to use it.

You need to be quite comfortable with [[command line]] usage to use
this.

   Note: Windows users have to use the ''--option-name="value"'' syntax
   instead of the ''--option-name value'' syntax.

=== Getting help ===

VLC uses a modular structure. The core mainly manages communication
between modules. All the multimedia processing is done by modules. There
are input modules, [[demultiplex]]ers, decoders, video output modules,
...

This chapter will only describe the "general" options, i.e. the core
options. Each module adds new options. For example, the HTTP input
module will add options for caching, proxy, authentication, ...

By using '''vlc --help''', you will get the basic core options. '''vlc
--longhelp''' will give all the basic options (core + modules). Adding
'''--advanced''' will give the "advanced options" (for advanced users).
So '''vlc --longhelp --advanced''' will give you all options. You can
also append '''--help-verbose''' if you want more detailed help.

Also, you might want to get debug information. To do this, use '''-v'''
or '''-vv''' (this will show lower severity messages). If your console
supports it, you can add '''--color to get messages in color.'''

=== Opening streams ===

The following commands start VLC and start reading the given element(s):

==== Opening a file ====

Start VLC with:

   {{%}} '''vlc my_file'''

VLC should be able to recognize the file type. If it does not, you can
force demultiplexer and decoder (see below).

A list of all video and audio codecs supported by VLC check the
[https://www.videolan.org/vlc/features.html VLC features list].

==== Opening a DVD or VCD, or an audio CD ====

Start VLC with:

For a DVD with menus:

   {{%}} '''vlc
   dvd://[device][@raw_device][@[title][:[chapter][:angle]]]'''

In most cases, '''vlc dvd://''' or '''vlc dvd://[device]''' will do.
[device] is for example '''/dev/dvd''' on GNU/Linux or '''D:''' on
Windows (complete path to your DVD drive).

or

(DVD without menus):

   {{%}} '''vlc
   dvdsimple://[device][@raw_device][@[title][:[chapter][:angle]]]'''

or

(VCD):

   {{%}} '''vlc vcd://[device][@{EES}[number]]'''

or

(Audio CD):

   {{%}} '''vlc cdda://[device][@[track]]'''

==== Receiving a network stream ====

To receive an [[unicast]] [[RTP]]/[[UDP]] stream (sent by VLC's stream
output), start VLC with:

   {{%}} '''vlc rtp://@:5004'''

If 5004 is the [[port]] to which packets are sent. 1234 is another
commonly used port number. you use the default port (1234), '''vlc
rtp://''' will do. For more information, look at the Streaming Howto.

To receive an multicast UDP/RTP stream (sent by VLC's stream output),
start VLC with:

   {{%}} '''vlc rtp://@multicast_address:port'''

To receive a [[SSM]] (source specific multicast) stream, you can use:

   {{%}} '''vlc rtp://\ server_address@multicast_address:port'''

This only works on [[Operating system]]s that support SSM (Windows XP
and Linux).

To receive a HTTP stream, start VLC with:

   {{%}} '''vlc
   <nowiki>http://www.example.org/your_file.mpg\ </nowiki>'''

To receive a [[RTSP]] stream, start VLC with:&lt;/para&gt;

   {{%}} '''vlc rtsp://www.example.org/your_stream'''

=== Modules selection ===

VLC always tries to select the most appropriate interface, input and
output modules, among the ones available on the system, according to the
stream it is given to read. However, you may wish to force the use of a
specific module with the following options.

*'''--intf &lt;module&gt;''' allows you to select the interface
module.*'''--extraintf &lt;module&gt;''' allows you to select extra
interface modules that will be launched in addition to the main one.
This is mainly useful for special ''control'' interfaces, like HTTP, RC
(Remote Control), ... (see below) *'''--aout &lt;module&gt;''' allows
you to select the audio output module.*'''--vout &lt;module&gt;'''
allows you to select the video output module. \*'''--memcpy
&lt;module&gt;''' allows you to choose a memory copy module. You should
probably never touch that.

You can get a listing of the available modules by using '''vlc -l'''

=== Stream Output ===

The Stream output system allows vlc to become a streaming server.

For more details on the stream output system, please have a look at the
[[Documentation:Streaming HowTo|Streaming HowTo]].

<br>

=== Other Options ===

==== Audio options ====

*'''--noaudio''' disables audio output. Note that if you are streaming
(ex: to a file) this has no effect (streaming copies the audio
verbatim). Use --sout-xxx instead (ex: --no-sout-audio)*'''--mono'''
forces VLC to treat the stream in mono audio. *'''--volume
&lt;[[integer]]&gt;''' sets the level of audio output (between 0 and
1024). Also only applies to local playback (like
--noaudio).*'''--aout-rate &lt;[[integer]]&gt;''' sets the audio output
frequency (Hz). By default, VLC will try to autodetect this.
*'''--desync &lt;[[integer]]&gt;''' compensates desynchronization of
audio (ms). (If audio and video streams are not synchronized, use this
setting to delay the audio stream)*'''--audio-filter
&lt;[[string]]&gt;''' adds audio filters to the processing chain.
Available filters are visual (visualizer with spectrum analyzer and
oscilloscope), headphone (virtual headphone patialization) and
normalizer (volume normalizer)

==== Video options ====

*'''--no-video''' disables video output.*'''--grayscale''' turns video
output into grayscale mode. *'''--fullscreen''' ( or '''-f''') sets
fullscreen video.*'''--nooverlay''' disables [[hardware acceleration]]
for the video output. *'''--width, --height &lt;[[integer]]&gt;''' sets
the video window dimensions. By default, the video window size will be
adjusted to match the video dimensions.*'''--start-time
&lt;[[integer]]&gt;''' starts the video here; the integer is the number
of seconds from the beginning (e.g. 1:30 is written as 90)
*'''--stop-time &lt;[[integer]]&gt;''' stops the video here; the integer
is the number of seconds from the beginning (e.g. 1:30 is written as
90)*'''--zoom &lt;[[float]]&gt;''' adds a zoom factor.
*'''--aspect-ratio &lt;mode&gt;''' forces source aspect ratio. Modes are
4x3, 16x9, ...*'''--spumargin &lt;[[integer]]&gt;''' forces SPU
subtitles position. *'''--video-filter &lt;[[string]]&gt;''' adds video
filters to the processing chain. You can add several filters, separated
by commas*'''--sub-filter &lt;[[string]]&gt;''' adds video subpictures
filter to the processing chain.

==== Desktop/Screen grab options ====

You can see the various options for "grabbing the desktop" (VLC's
built-in screen grabber capture device) by using the GUI. See
https://forum.videolan.org/viewtopic.php?f=4&t=46971

==== Playlist options ====

*'''--random''' plays files randomly forever.*'''--loop''' loops
playlist on end. *'''--repeat''' repeats current item until another item
is forced*'''--play-and-stop''' stops the playlist after each played
item.

==== Network options ====

*'''--server-port &lt;[[integer]]&gt;''' sets server port.*'''--iface
&lt;[[string]]&gt;''' specifies the network interface to use.
*'''--iface-addr &lt;[[string]]&gt;''' specifies your network interface
IP address.*'''--mtu &lt;[[integer]]&gt;''' specifies the MTU of the
network interface. *'''--ipv6''' forces IPv6.*'''--ipv4''' forces IPv4.

==== CPU options ====

You should probably not touch these options unless you know what you are
doing.

*'''--nommx''' disables the use of MMX CPU extensions.*'''--no3dn'''
disables the use of 3D Now! CPU extensions. *'''--nommxext''' disables
the use of MMX Ext CPU extensions.*'''--nosse''' disables the use of SSE
CPU extensions. \*'''--noaltivec''' disables the use of Altivec CPU
extensions.

==== Miscellaneous options ====

*'''--quiet''' deactivates all console messages.*'''--color''' displays
color messages. *'''--search-path &lt;[[string]]&gt;''' specifies
interface default search path.*'''--plugin-path &lt;[[string]]&gt;'''
specifies plugin search path. *'''--no-plugins-cache''' disables the
plugin cache (plugins cache speeds up startup)*'''--dvd
&lt;[[string]]&gt;''' specifies the default DVD device. *'''--vcd
&lt;[[string]]&gt;''' specifies the default VCD device.*'''--program
&lt;[[integer]]&gt;''' specifies program (SID) (for streams with several
programs, like satellite ones). *'''--audio-type &lt;[[integer]]&gt;'''
specifies the default audio type to use with dvds.*'''--audio-channel
&lt;[[integer]]&gt;''' specifies the default audio channel to use with
dvds. *'''--spu-channel &lt;[[integer]]&gt;''' specifies the default
subtitle channel to use with dvds.*'''--version''' gives you information
about the current VLC version. \*'''--module &lt;module&gt; ''' displays
help about specified module. (Shortcut: '''-p''')

=== Item-specific options ===

There are many options that are related to items (like '''--novideo''',
'''--codec''', '''--fullscreen''').

For all of these, you have the possibility to make them item-specific,
using ":" instead of "--" and putting the option just after the
concerned item.

Examples:

   {{%}} '''vlc file1.mpg&nbsp;:fullscreen file2.mpg'''

will play file1.mpg in fullscreen mode and file2.mpg in the default mode
(which is generally no fullscreen), whereas

   {{%}} '''vlc --fullscreen file1.mpg file2.mpg'''

will play both files in fullscreen mode

   {{%}} '''vlc --fullscreen
   file1.mpg&nbsp;:sub-file=file1.srt&nbsp;:no-fullscreen
   file2.mpg&nbsp;:filter=distort'''

will play file1.mpg in windowed (no-fullscreen) mode with the subtitles
file file1.srt and will play file2.mpg with video filter distort enabled
in fullscreen mode (item-specific options override global options).

== Advanced use of filters ==

=== Filters ===

These are the old style VLC filters. They only apply to on screen
display and thus cannot be streamed. However, on version 1.1.11 you are
still able to apply these filters in ''transcode'' module using
parameter ''vfilter''. More information can be found on
[[Documentation:Streaming HowTo/Advanced Streaming Using the Command
Line#vfilter]].

==== Deinterlacing video filter ====

Module name: '''deinterlace'''

\*'''--deinterlace-mode {discard,blend,mean,bob,linear,x,yadif,yadif
(2x),phosophor,ivtc}''' choose a [[deinterlacing]] mode.

==== Invert video filter ====

Module name: '''invert'''

==== Image properties filter ====

Module name: '''adjust''' {{Transcluded|Documentation:Modules/adjust}}
{{:Documentation:Modules/adjust}}

==== Wall video filter ====

Module name: '''wall''' This filter splits the output in several
windows. {{Transcluded|Documentation:Modules/wall}}
{{:Documentation:Modules/wall}}

==== Video transformation filter ====

Module name: '''transform'''
{{Transcluded|Documentation:Modules/transform}}
{{:Documentation:Modules/transform}}

==== Distort video filter ====

Module name: '''distort''' {{See|Documentation:Modules/distort}}

==== Clone video filter ====

This filter clones the output window.

Module name: '''clone''' {{Transcluded|Documentation:Modules/clone}}
{{:Documentation:Modules/clone}}

==== Croppadd video filter ====

Module name: '''croppadd'''
{{Transcluded|Documentation:Modules/croppadd}}
{{:Documentation:Modules/croppadd}}

==== Motion blur filter ====

Module name: '''motionblur'''
{{Transcluded|Documentation:Modules/motionblur}}
{{:Documentation:Modules/motionblur}}

==== Video pictures blending ====

Module name: '''blend'''

==== Video scaling filter ====

Module name: '''scale'''

<br>

=== Subpictures Filters ===

These are the new VLC filters. They can be streamed.

==== Marquee display sub filter ====

Module name: '''marq''' {{Transcluded|Documentation:Modules/marq}}
{{:Documentation:Modules/marq}}

==== Logo video filter ====

Module name: '''logo''' {{Transcluded|Documentation:Modules/logo}}
{{:Documentation:Modules/logo}}

This filter can be used both as an old style filter or a subpictures
filter.

Note: You can move the logo by left-clicking on it.

<br>

== The HTTP interface ==

VLC ships with a little [[HTTP interface|HTTP server integrated]]. It is
used both to stream using [[HTTP]], and for the HTTP remote control
interface.

To start VLC with the HTTP interface, use:

   {{%}} '''vlc -I http [--http-src /directory/] [--http-host
   host:port]'''

If you want to have both the "normal" interface and the HTTP interface,
use '''vlc --extraintf http'''.

The HTTP interface will start listening at host:port (&lt;all
interfaces&gt;:8080 if omitted), and will reproduce the structure of
/directory at
<code><nowiki>`http://host:port/ <http://host:port/>`__\ </nowiki></code>
( vlc_source_path/share/http if omitted ).

Use a browser to go to
<code><nowiki>`http://your_host_machine:port <http://your_host_machine:port>`__\ </nowiki></code>.
You should be taken to the main page.

VLC is shipped with a set of files that should be enough for generic
needs. It is also possible to customize pages. See [[Documentation:Play
HowTo/Building Pages for the HTTP Interface]].

Available pages for 1.0.3&nbsp;:

*<nowiki>http://host:port</nowiki> - Main
Interface*\ <nowiki>`http://host:port/vlm.html <http://host:port/vlm.html>`__\ </nowiki>
- VLM Interface *<nowiki>http://host:port/mosaic.html</nowiki> - Mosaic
Wizard*\ <nowiki>`http://host:port/flash.html <http://host:port/flash.html>`__\ </nowiki>
- Flash based remote playback

== Other control interfaces ==

VLC includes a number of so-called interfaces that are not really
interfaces, but means of [[Category:Control VLC|controlling VLC]].
Nevertheless, they are enabled by setting them as interface or extra
interface, either in the Preferences, in General/Interface, or using
'''-I''' or '''--extraintf''' on the command line.

=== Hotkeys ===

This module allows you to control VLC and playback via hotkeys. It is
always enabled by default. You can use hotkeys in the video output
window, you can't in the audio dummy interface.

Hotkeys can be hacked by:

   {{%}} '''vlc --key-&lt;function&gt; &lt;code&gt;'''

Code is composed by modifiers keys (Alt, Shift, Ctrl, Meta,Command)
separated by a dash (-) and terminated by a key (a...z, +, =, -, ',', +,
&lt;, &gt;, \`, /,&nbsp;;, ', , [, ], \*, Left, Right, Up, Down, Space,
Enter, F1...F12, Home, End, Menu, Esc, Page Up, Page Down, Tab,
Backspace, Mouse Wheel Up and Mouse Wheel Down). Main controls are
available from hotkeys, such as&nbsp;: fullscreen, play-pause, faster,
slower, next, prev, stop, quit, vol-up, etc. (use the '''--longhelp'''
option for full list of functions). For example, for binding fullscreen
to Ctrl-f, run:

   {{%}} '''vlc --key-fullscreen 'Ctrl-f' '''

The list of the default hotkeys is available [[HotKeys|here]].

=== RC and RTCI ===

These two interfaces allow you to control VLC from a command shell
(possibly using a remote connexion or a Unix socket).

Start VLC with '''-I rc''' or '''--extraintf rc'''. When you get the
'''Remote control interface initialized, \`h' for help''' message, press
h and Enter to get help about available commands.

To be able to remote connect to your VLC using a TCP socket (telnet-like
connexion), use '''--rc-host your_host:port'''. Then, by connecting
(using telnet or netcat) to the host on the given port, you will get the
command shell.

To use a UNIX socket (local socket, this does not work for Windows), use
'''--rc-unix /path/to/socket'''. Commands can then be passed using this
UNIX socket.

The RTCI interface gives you more advanced options, such as marquee
control for the marquee subpicture filter (See filter section).

<br>

=== Ncurses ===

This is a text interface, using ncurses library.

Start VLC with '''-I ncurses''' or '''--extraintf ncurses'''.

The ncurses interface

Press h to get the list of all available commands, with a short
description.

There is also a filebrowser available for the ncurses interface in order
to add playlist items. Press 'B' to use it.

The ncurses filebrowser

You can set the filebrowser starting point by launching vlc with the
'''--browse-dir''' option:

   {{%}} '''vlc -I ncurses --browse-dir /filebrowser/starting/point/'''

<br>

=== Gestures ===

Gestures provide a simple [[mouse gestures]] control. TODO

<br>

== The Mozilla plugin ==

VLC can also be embedded in a web browser! The following browsers are
supported: [https://www.mozilla.org/products/firefox/ Firefox] and
[https://www.apple.com/macosx/features/safari Safari].

=== Install the plugin ===

==== GNU/Linux Debian, Ubuntu, etc. ====

Install the ''mozilla-plugin-vlc'' package using your preferred package
manager. For example, at the command line enter:

   # '''apt-get update''' # '''apt-get install mozilla-plugin-vlc'''

==== Windows ====

Quit Firefox or Mozilla.

Select the Mozilla Plugin option when installing VLC Media Player. The
installer will then automatically detect your browser and install the
plugin.

Restart Firefox or Mozilla.

===== Manual Install ===== In
[http://kb.mozillazine.org/Installation_directory "Mozilla
Firefoxplugins"]

Create the directory if it doesn't exist.

'''Folders''' to copy: \* osdmenu \* plugins

'''Files''' to copy: \* vlc.exe \* vlc.exe.manifest \* vlc-cache-gen.exe
\* npvlc.dll.manifest \* npvlc.dll \* libvlccore.dll \* libvlc.dll \*
libvlc.dll.manifest \* axvlc.dll \* axvlc.dll.manifest

==== macOS ====

''The Mozilla/Safari plugin for [[macOS]] is only available from vlc
version 0.8.5.1 and onwards.''

Quit Safari browser.

Download the Mozilla/safari plugin package from
[https://www.videolan.org/vlc/download-macosx.html macOS download page].

Run the installer from the dmg image.

<br>

==== Compile the sources yourself ====

Please look at the [https://www.videolan.org/developers developers page]
for information on how to do this.

<br>

=== Use the Mozilla plugin ===

If in the browser you open a link to an audio or video URL handled by
the VLC plugin, or if a web page has HTML code that embeds audio or
video handled by the VLC plugin, then the plugin should start and play
the audio/video. Note the plugin (as of version 1.1.9) does not present
any user interface — it has no default control panel and no keyboard
shortcuts.

To get the list of the media types handled by the VLC plugin, browse to
'''about:plugins'''. Conflicts will arise if you have more than one
plugin installed that supports the same media type.

See the [[Documentation:WebPlugin|Web plugin documentation]] to create
HTML pages that use JavaScript to control the plugin.

== Snapshot Tool ==

Did you know you can use special codes to automatically generate
filenames in the [[Snapshot Tool]]?

== Specifying Streaming Options == {{Further|Documentation:Streaming
HowTo New}}

== Audio Bar Graph over Video ==

This section specifies how to enable the audiobargraph audio filter and
video overlay, (mostly) via the [[GUI]]. This displays an audio meter
overlaid on the video.

There are three parts - an audio filter, which sends it's output via
[[TCP]] to the Remote Control (RC) Interface. This information is then
picked up and displayed by the Audio Bar Graph video subpicture filter
(OSD).

To enable this, VLC needs to be started with the '''--rc-host''' command-line switch - e.g.
   {{%}} '''"C:Program FilesVideoLANVLCvlc.exe" --rc-host
   localhost:12345'''

In the GUI, set the following (this example from VLC v1.1.9 on Windows
7): \* Preferences:Show settings:All \* Audio/Filters > Enable "Audio
part of the BarGraph function" \* Audio/Filters/audiobargraph > use
defaults, change "Sends the barGraph information every n audio packets"
to 1 to enable see a more accurate display \* Interface/Main interfaces
> Enable "Remote control interface" \* Interface/Main interfaces/RC >
Enable "Do not open a DOS command box interface" \* Video/Subtitles-OSD
> Enable "Audio Bar Graph Video sub filter" \* Video/Subtitles-OSD/Audio
Bar Graph > Set the following settings: \*\* "Value of the audio
channels levels" = 0 (setting this to 0:1 crashes VLC v1.1.9) \*\* "X
coordinate" = 0 \*\* "Y coordinate" = 0 (this doesn't seem to affect
anything) \*\* "Transparency of the bargraph" = 128 for 50% transparency
which looks ok \*\* "Bargraph position" = Left (seems to only work
Left,Center,Right - can't go top or bottom) \*\* "Alarm" = 1 (enables
the silence alarm - puts a red border around the bargraph if silent for
too long) \*\* "Bar width in pixel" = 10 (20 if you want it to be really
visible)

{{Documentation}} [[Category:Proposed deletion]]
