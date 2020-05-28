.. raw:: mediawiki

   {{RightMenu|Documentation TOC}}

Use the command line
--------------------

**TODO: completely outdated**

All standard operations of VLC should be available from the GUI. However, some complex operations can only be done from the command line and there are situations in which you don't need or want a GUI. Here is the complete description of VLC's command line and how to use it.

You need to be quite comfortable with `command line <command_line>`__ usage to use this.

``Note: Windows users have to use the ``\ *``--option-name="value"``*\ `` syntax instead of the ``\ *``--option-name``\ ````\ ``value``*\ `` syntax.``

Getting help
~~~~~~~~~~~~

VLC uses a modular structure. The core mainly manages communication between modules. All the multimedia processing is done by modules. There are input modules, `demultiplexers <demultiplex>`__, decoders, video output modules, ...

This chapter will only describe the "general" options, i.e. the core options. Each module adds new options. For example, the HTTP input module will add options for caching, proxy, authentication, ...

By using **vlc --help**, you will get the basic core options. **vlc --longhelp** will give all the basic options (core + modules). Adding **--advanced** will give the "advanced options" (for advanced users). So **vlc --longhelp --advanced** will give you all options. You can also append **--help-verbose** if you want more detailed help.

Also, you might want to get debug information. To do this, use **-v** or **-vv** (this will show lower severity messages). If your console supports it, you can add **--color to get messages in color.**

Opening streams
~~~~~~~~~~~~~~~

The following commands start VLC and start reading the given element(s):

Opening a file
^^^^^^^^^^^^^^

Start VLC with:

``{{%}} ``\ **``vlc``\ ````\ ``my_file``**

VLC should be able to recognize the file type. If it does not, you can force demultiplexer and decoder (see below).

A list of all video and audio codecs supported by VLC check the `VLC features list <https://www.videolan.org/vlc/features.html>`__.

Opening a DVD or VCD, or an audio CD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Start VLC with:

For a DVD with menus:

``{{%}} ``\ **``vlc``\ ````\ ``dvd://[device][@raw_device][@[title][:[chapter][:angle]]]``**

In most cases, **vlc dvd://** or **vlc dvd://[device]** will do. [device] is for example **/dev/dvd** on GNU/Linux or **D:** on Windows (complete path to your DVD drive).

or

(DVD without menus):

``{{%}} ``\ **``vlc``\ ````\ ``dvdsimple://[device][@raw_device][@[title][:[chapter][:angle]]]``**

or

(VCD):

``{{%}} ``\ **``vlc``\ ````\ ``vcd://[device][@{E|P|E|T|S}[number]]``**

or

(Audio CD):

``{{%}} ``\ **``vlc``\ ````\ ``cdda://[device][@[track]]``**

Receiving a network stream
^^^^^^^^^^^^^^^^^^^^^^^^^^

To receive an `unicast <unicast>`__ `RTP <RTP>`__/`UDP <UDP>`__ stream (sent by VLC's stream output), start VLC with:

``{{%}} ``\ **``vlc``\ ````\ ``rtp://@:5004``**

If 5004 is the `port <port>`__ to which packets are sent. 1234 is another commonly used port number. you use the default port (1234), **vlc rtp://** will do. For more information, look at the Streaming Howto.

To receive an multicast UDP/RTP stream (sent by VLC's stream output), start VLC with:

``{{%}} ``\ **``vlc``\ ````\ ``rtp://@multicast_address:port``**

To receive a `SSM <SSM>`__ (source specific multicast) stream, you can use:

``{{%}} ``\ **``vlc``\ ````\ ``rtp://server_address@multicast_address:port``**

This only works on `Operating systems <Operating_system>`__ that support SSM (Windows XP and Linux).

To receive a HTTP stream, start VLC with:

``{{%}} ``\ **``vlc``\ ````\ ``http://www.example.org/your_file.mpg``**

To receive a `RTSP <RTSP>`__ stream, start VLC with:</para>

``{{%}} ``\ **``vlc``\ ````\ **\ ```rtsp://www.example.org/your_stream`` <rtsp://www.example.org/your_stream>`__

Modules selection
~~~~~~~~~~~~~~~~~

VLC always tries to select the most appropriate interface, input and output modules, among the ones available on the system, according to the stream it is given to read. However, you may wish to force the use of a specific module with the following options.

-  **--intf <module>** allows you to select the interface module.
-  **--extraintf <module>** allows you to select extra interface modules that will be launched in addition to the main one. This is mainly useful for special *control* interfaces, like HTTP, RC (Remote Control), ... (see below)
-  **--aout <module>** allows you to select the audio output module.
-  **--vout <module>** allows you to select the video output module.
-  **--memcpy <module>** allows you to choose a memory copy module. You should probably never touch that.

You can get a listing of the available modules by using **vlc -l**

Stream Output
~~~~~~~~~~~~~

The Stream output system allows vlc to become a streaming server.

For more details on the stream output system, please have a look at the `Streaming HowTo <Documentation:Streaming_HowTo>`__.

| 

Other Options
~~~~~~~~~~~~~

Audio options
^^^^^^^^^^^^^

-  **--noaudio** disables audio output. Note that if you are streaming (ex: to a file) this has no effect (streaming copies the audio verbatim). Use --sout-xxx instead (ex: --no-sout-audio)
-  **--mono** forces VLC to treat the stream in mono audio.
-  **--volume <**\ `integer <integer>`__\ **>** sets the level of audio output (between 0 and 1024). Also only applies to local playback (like --noaudio).
-  **--aout-rate <**\ `integer <integer>`__\ **>** sets the audio output frequency (Hz). By default, VLC will try to autodetect this.
-  **--desync <**\ `integer <integer>`__\ **>** compensates desynchronization of audio (ms). (If audio and video streams are not synchronized, use this setting to delay the audio stream)
-  **--audio-filter <**\ `string <string>`__\ **>** adds audio filters to the processing chain. Available filters are visual (visualizer with spectrum analyzer and oscilloscope), headphone (virtual headphone patialization) and normalizer (volume normalizer)

Video options
^^^^^^^^^^^^^

-  **--no-video** disables video output.
-  **--grayscale** turns video output into grayscale mode.
-  **--fullscreen** ( or **-f**) sets fullscreen video.
-  **--nooverlay** disables `hardware acceleration <hardware_acceleration>`__ for the video output.
-  **--width, --height <**\ `integer <integer>`__\ **>** sets the video window dimensions. By default, the video window size will be adjusted to match the video dimensions.
-  **--start-time <**\ `integer <integer>`__\ **>** starts the video here; the integer is the number of seconds from the beginning (e.g. 1:30 is written as 90)
-  **--stop-time <**\ `integer <integer>`__\ **>** stops the video here; the integer is the number of seconds from the beginning (e.g. 1:30 is written as 90)
-  **--zoom <**\ `float <float>`__\ **>** adds a zoom factor.
-  **--aspect-ratio <mode>** forces source aspect ratio. Modes are 4x3, 16x9, ...
-  **--spumargin <**\ `integer <integer>`__\ **>** forces SPU subtitles position.
-  **--video-filter <**\ `string <string>`__\ **>** adds video filters to the processing chain. You can add several filters, separated by commas
-  **--sub-filter <**\ `string <string>`__\ **>** adds video subpictures filter to the processing chain.

Desktop/Screen grab options
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can see the various options for "grabbing the desktop" (VLC's built-in screen grabber capture device) by using the GUI. See https://forum.videolan.org/viewtopic.php?f=4&t=46971

Playlist options
^^^^^^^^^^^^^^^^

-  **--random** plays files randomly forever.
-  **--loop** loops playlist on end.
-  **--repeat** repeats current item until another item is forced
-  **--play-and-stop** stops the playlist after each played item.

Network options
^^^^^^^^^^^^^^^

-  **--server-port <**\ `integer <integer>`__\ **>** sets server port.
-  **--iface <**\ `string <string>`__\ **>** specifies the network interface to use.
-  **--iface-addr <**\ `string <string>`__\ **>** specifies your network interface IP address.
-  **--mtu <**\ `integer <integer>`__\ **>** specifies the MTU of the network interface.
-  **--ipv6** forces IPv6.
-  **--ipv4** forces IPv4.

CPU options
^^^^^^^^^^^

You should probably not touch these options unless you know what you are doing.

-  **--nommx** disables the use of MMX CPU extensions.
-  **--no3dn** disables the use of 3D Now! CPU extensions.
-  **--nommxext** disables the use of MMX Ext CPU extensions.
-  **--nosse** disables the use of SSE CPU extensions.
-  **--noaltivec** disables the use of Altivec CPU extensions.

Miscellaneous options
^^^^^^^^^^^^^^^^^^^^^

-  **--quiet** deactivates all console messages.
-  **--color** displays color messages.
-  **--search-path <**\ `string <string>`__\ **>** specifies interface default search path.
-  **--plugin-path <**\ `string <string>`__\ **>** specifies plugin search path.
-  **--no-plugins-cache** disables the plugin cache (plugins cache speeds up startup)
-  **--dvd <**\ `string <string>`__\ **>** specifies the default DVD device.
-  **--vcd <**\ `string <string>`__\ **>** specifies the default VCD device.
-  **--program <**\ `integer <integer>`__\ **>** specifies program (SID) (for streams with several programs, like satellite ones).
-  **--audio-type <**\ `integer <integer>`__\ **>** specifies the default audio type to use with dvds.
-  **--audio-channel <**\ `integer <integer>`__\ **>** specifies the default audio channel to use with dvds.
-  **--spu-channel <**\ `integer <integer>`__\ **>** specifies the default subtitle channel to use with dvds.
-  **--version** gives you information about the current VLC version.
-  '''--module <module> ''' displays help about specified module. (Shortcut: **-p**)

Item-specific options
~~~~~~~~~~~~~~~~~~~~~

There are many options that are related to items (like **--novideo**, **--codec**, **--fullscreen**).

For all of these, you have the possibility to make them item-specific, using ":" instead of "--" and putting the option just after the concerned item.

Examples:

``{{%}} ``\ **``vlc``\ ````\ ``file1.mpg :fullscreen``\ ````\ ``file2.mpg``**

will play file1.mpg in fullscreen mode and file2.mpg in the default mode (which is generally no fullscreen), whereas

``{{%}} ``\ **``vlc``\ ````\ ``--fullscreen``\ ````\ ``file1.mpg``\ ````\ ``file2.mpg``**

will play both files in fullscreen mode

``{{%}} ``\ **``vlc``\ ````\ ``--fullscreen``\ ````\ ``file1.mpg :sub-file=file1.srt :no-fullscreen``\ ````\ ``file2.mpg :filter=distort``**

will play file1.mpg in windowed (no-fullscreen) mode with the subtitles file file1.srt and will play file2.mpg with video filter distort enabled in fullscreen mode (item-specific options override global options).

Advanced use of filters
-----------------------

Filters
~~~~~~~

These are the old style VLC filters. They only apply to on screen display and thus cannot be streamed. However, on version 1.1.11 you are still able to apply these filters in *transcode* module using parameter *vfilter*. More information can be found on `Documentation:Streaming HowTo/Advanced Streaming Using the Command Line#vfilter <Documentation:Streaming_HowTo/Advanced_Streaming_Using_the_Command_Line#vfilter>`__.

Deinterlacing video filter
^^^^^^^^^^^^^^^^^^^^^^^^^^

Module name: **deinterlace**

-  **--deinterlace-mode {discard,blend,mean,bob,linear,x,yadif,yadif (2x),phosophor,ivtc}** choose a `deinterlacing <deinterlacing>`__ mode.

Invert video filter
^^^^^^^^^^^^^^^^^^^

Module name: **invert**

Image properties filter
^^^^^^^^^^^^^^^^^^^^^^^

Module name: **adjust**

Wall video filter
^^^^^^^^^^^^^^^^^

Module name: **wall** This filter splits the output in several windows.

Video transformation filter
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Module name: **transform**

Distort video filter
^^^^^^^^^^^^^^^^^^^^

Module name: **distort**

Clone video filter
^^^^^^^^^^^^^^^^^^

This filter clones the output window.

Module name: **clone**

Croppadd video filter
^^^^^^^^^^^^^^^^^^^^^

Module name: **croppadd**

Motion blur filter
^^^^^^^^^^^^^^^^^^

Module name: **motionblur**

Video pictures blending
^^^^^^^^^^^^^^^^^^^^^^^

Module name: **blend**

Video scaling filter
^^^^^^^^^^^^^^^^^^^^

Module name: **scale**

| 

Subpictures Filters
~~~~~~~~~~~~~~~~~~~

These are the new VLC filters. They can be streamed.

Marquee display sub filter
^^^^^^^^^^^^^^^^^^^^^^^^^^

Module name: **marq**

Logo video filter
^^^^^^^^^^^^^^^^^

Module name: **logo**

This filter can be used both as an old style filter or a subpictures filter.

Note: You can move the logo by left-clicking on it.

| 

The HTTP interface
------------------

VLC ships with a little `HTTP server integrated <HTTP_interface>`__. It is used both to stream using `HTTP <HTTP>`__, and for the HTTP remote control interface.

To start VLC with the HTTP interface, use:

``{{%}} ``\ **``vlc``\ ````\ ``-I``\ ````\ ``http``\ ````\ ``[--http-src``\ ````\ ``/directory/]``\ ````\ ``[--http-host``\ ````\ ``host:port]``**

If you want to have both the "normal" interface and the HTTP interface, use **vlc --extraintf http**.

The HTTP interface will start listening at host:port (<all interfaces>:8080 if omitted), and will reproduce the structure of /directory at ``http://host:port/`` ( vlc_source_path/share/http if omitted ).

Use a browser to go to ``http://your_host_machine:port``. You should be taken to the main page.

VLC is shipped with a set of files that should be enough for generic needs. It is also possible to customize pages. See `Documentation:Play HowTo/Building Pages for the HTTP Interface <Documentation:Play_HowTo/Building_Pages_for_the_HTTP_Interface>`__.

Available pages for 1.0.3 :

-  http://host:port - Main Interface
-  http://host:port/vlm.html - VLM Interface
-  http://host:port/mosaic.html - Mosaic Wizard
-  http://host:port/flash.html - Flash based remote playback

Other control interfaces
------------------------

VLC includes a number of so-called interfaces that are not really interfaces, but means of . Nevertheless, they are enabled by setting them as interface or extra interface, either in the Preferences, in General/Interface, or using **-I** or **--extraintf** on the command line.

Hotkeys
~~~~~~~

This module allows you to control VLC and playback via hotkeys. It is always enabled by default. You can use hotkeys in the video output window, you can't in the audio dummy interface.

Hotkeys can be hacked by:

``{{%}} ``\ **``vlc``\ ````\ ``--key-<function>``\ ````\ ``<code>``**

Code is composed by modifiers keys (Alt, Shift, Ctrl, Meta,Command) separated by a dash (-) and terminated by a key (a...z, +, =, -, ',', +, <, >, \`, /, ;, ', \\, [, ], \*, Left, Right, Up, Down, Space, Enter, F1...F12, Home, End, Menu, Esc, Page Up, Page Down, Tab, Backspace, Mouse Wheel Up and Mouse Wheel Down). Main controls are available from hotkeys, such as : fullscreen, play-pause, faster, slower, next, prev, stop, quit, vol-up, etc. (use the **--longhelp** option for full list of functions). For example, for binding fullscreen to Ctrl-f, run:

``{{%}} '''vlc --key-fullscreen 'Ctrl-f' '''``

The list of the default hotkeys is available `here <HotKeys>`__.

RC and RTCI
~~~~~~~~~~~

These two interfaces allow you to control VLC from a command shell (possibly using a remote connexion or a Unix socket).

Start VLC with **-I rc** or **--extraintf rc**. When you get the **Remote control interface initialized, \`h' for help** message, press h and Enter to get help about available commands.

To be able to remote connect to your VLC using a TCP socket (telnet-like connexion), use **--rc-host your_host:port**. Then, by connecting (using telnet or netcat) to the host on the given port, you will get the command shell.

To use a UNIX socket (local socket, this does not work for Windows), use **--rc-unix /path/to/socket**. Commands can then be passed using this UNIX socket.

The RTCI interface gives you more advanced options, such as marquee control for the marquee subpicture filter (See filter section).

| 

Ncurses
~~~~~~~

This is a text interface, using ncurses library.

Start VLC with **-I ncurses** or **--extraintf ncurses**.

The ncurses interface

Press h to get the list of all available commands, with a short description.

There is also a filebrowser available for the ncurses interface in order to add playlist items. Press 'B' to use it.

The ncurses filebrowser

You can set the filebrowser starting point by launching vlc with the **--browse-dir** option:

``{{%}} ``\ **``vlc``\ ````\ ``-I``\ ````\ ``ncurses``\ ````\ ``--browse-dir``\ ````\ ``/filebrowser/starting/point/``**

| 

Gestures
~~~~~~~~

Gestures provide a simple `mouse gestures <mouse_gestures>`__ control. TODO

| 

The Mozilla plugin
------------------

VLC can also be embedded in a web browser! The following browsers are supported: `Firefox <https://www.mozilla.org/products/firefox/>`__ and `Safari <https://www.apple.com/macosx/features/safari>`__.

Install the plugin
~~~~~~~~~~~~~~~~~~

GNU/Linux Debian, Ubuntu, etc.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install the *mozilla-plugin-vlc* package using your preferred package manager. For example, at the command line enter:

| ``# ``\ **``apt-get``\ ````\ ``update``**
| ``# ``\ **``apt-get``\ ````\ ``install``\ ````\ ``mozilla-plugin-vlc``**

Windows
^^^^^^^

Quit Firefox or Mozilla.

Select the Mozilla Plugin option when installing VLC Media Player. The installer will then automatically detect your browser and install the plugin.

Restart Firefox or Mozilla.

Manual Install
''''''''''''''

In `"Mozilla Firefox\plugins" <http://kb.mozillazine.org/Installation_directory>`__

Create the directory if it doesn't exist.

**Folders** to copy:

-  osdmenu
-  plugins

**Files** to copy:

-  vlc.exe
-  vlc.exe.manifest
-  vlc-cache-gen.exe
-  npvlc.dll.manifest
-  npvlc.dll
-  libvlccore.dll
-  libvlc.dll
-  libvlc.dll.manifest
-  axvlc.dll
-  axvlc.dll.manifest

macOS
^^^^^

*The Mozilla/Safari plugin for*\ `macOS <macOS>`__\ *is only available from vlc version 0.8.5.1 and onwards.*

Quit Safari browser.

Download the Mozilla/safari plugin package from `macOS download page <https://www.videolan.org/vlc/download-macosx.html>`__.

Run the installer from the dmg image.

| 

Compile the sources yourself
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please look at the `developers page <https://www.videolan.org/developers>`__ for information on how to do this.

| 

Use the Mozilla plugin
~~~~~~~~~~~~~~~~~~~~~~

If in the browser you open a link to an audio or video URL handled by the VLC plugin, or if a web page has HTML code that embeds audio or video handled by the VLC plugin, then the plugin should start and play the audio/video. Note the plugin (as of version 1.1.9) does not present any user interface — it has no default control panel and no keyboard shortcuts.

To get the list of the media types handled by the VLC plugin, browse to about:plugins. Conflicts will arise if you have more than one plugin installed that supports the same media type.

See the `Web plugin documentation <Documentation:WebPlugin>`__ to create HTML pages that use JavaScript to control the plugin.

Snapshot Tool
-------------

Did you know you can use special codes to automatically generate filenames in the `Snapshot Tool <Snapshot_Tool>`__?

Specifying Streaming Options
----------------------------

.. raw:: mediawiki

   {{Further|Documentation:Streaming HowTo New}}

Audio Bar Graph over Video
--------------------------

This section specifies how to enable the audiobargraph audio filter and video overlay, (mostly) via the `GUI <GUI>`__. This displays an audio meter overlaid on the video.

There are three parts - an audio filter, which sends it's output via `TCP <TCP>`__ to the Remote Control (RC) Interface. This information is then picked up and displayed by the Audio Bar Graph video subpicture filter (OSD).

To enable this, VLC needs to be started with the **--rc-host** command-line switch - e.g.

``{{%}} ``\ **``"C:\Program``\ ````\ ``Files\VideoLAN\VLC\vlc.exe"``\ ````\ ``--rc-host``\ ````\ ``localhost:12345``**

In the GUI, set the following (this example from VLC v1.1.9 on Windows 7):

-  Preferences:Show settings:All
-  Audio/Filters > Enable "Audio part of the BarGraph function"
-  Audio/Filters/audiobargraph > use defaults, change "Sends the barGraph information every n audio packets" to 1 to enable see a more accurate display
-  Interface/Main interfaces > Enable "Remote control interface"
-  Interface/Main interfaces/RC > Enable "Do not open a DOS command box interface"
-  Video/Subtitles-OSD > Enable "Audio Bar Graph Video sub filter"
-  Video/Subtitles-OSD/Audio Bar Graph > Set the following settings:

   -  "Value of the audio channels levels" = 0 (setting this to 0:1 crashes VLC v1.1.9)
   -  "X coordinate" = 0
   -  "Y coordinate" = 0 (this doesn't seem to affect anything)
   -  "Transparency of the bargraph" = 128 for 50% transparency which looks ok
   -  "Bargraph position" = Left (seems to only work Left,Center,Right - can't go top or bottom)
   -  "Alarm" = 1 (enables the silence alarm - puts a red border around the bargraph if silent for too long)
   -  "Bar width in pixel" = 10 (20 if you want it to be really visible)

.. raw:: mediawiki

   {{Documentation}}

`controlling VLC <Category:Control_VLC>`__ `Category:Proposed deletion <Category:Proposed_deletion>`__
