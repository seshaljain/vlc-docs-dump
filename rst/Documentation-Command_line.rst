.. raw:: mediawiki

   {{See also|Command-line interface}}

.. raw:: mediawiki

   {{Outdated}}

.. raw:: mediawiki

   {{RightMenu|Documentation TOC}}

Use the command line
--------------------

**TODO: completely outdated**

All standard operations of VLC should be available from the . However, some complex operations can only be done from the command line and there are situations in which you don't need or want a GUI. Here is the complete description of VLC's command line and how to use it.

You need to be quite comfortable with command line usage to use this.

``Note: Windows users have to use the ``\ *``--option-name="value"``*\ `` syntax instead of the ``\ *``--option-name``\ ````\ ``value``*\ `` syntax.``

Getting help
------------

VLC uses a modular structure. The core mainly manages communication between `modules <Documentation:modules>`__. All the multimedia processing is done by modules. There are input modules, `demultiplexers <demultiplex>`__, decoders, video output modules, ...

This chapter will only describe the "general" options, i.e., the core options. Each module adds new options. For example, the HTTP input module will add options for caching, proxy, authentication, ...

By using **vlc --help**, you will get the basic core options. **vlc --longhelp** will give all the basic options (core + modules). Adding **--advanced** will give the "advanced options" (for advanced users). So **vlc --longhelp --advanced** will give you all options. You can also append **--help-verbose** if you want more detailed help.

Also, you might want to get debug informations. To do this, use **-v** or **-vv** (this will show lower severity messages). If your console supports it, you can add **--color to get messages in color.**

Opening streams
---------------

The following commands start VLC and start reading the given element(s):

Opening a file
~~~~~~~~~~~~~~

Start VLC with:

``% ``\ **``vlc``\ ````\ ``my_file``**

VLC should be able to recognize the file type. If it does not, you can force demultiplexer and decoder (see below).

A list of all video and audio codecs supported by VLC is available on the `VLC features list <http://www.videolan.org/vlc/features.html>`__.

Opening a DVD or VCD, or an audio CD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start VLC with:

For a `DVD with menus <Documentation:Modules/dvdnav>`__:

``% ``\ **``vlc``\ ````\ ``dvd://[device][@raw_device][@[title][:[chapter][:angle]]]``**

In most cases, **vlc dvd://** or **vlc dvd://[device]** will do.

-  On GNU/Linux [device] is the path to the block device: e.g., **vlc dvd:///dev/dvd**.
-  On Windows, [device] is the drive letter with **/** and **:/**: e.g., **vlc dvd:///D:/**.

or

(`DVD without menus <Documentation:Modules/dvdread>`__):

``% ``\ **``vlc``\ ````\ ``dvdsimple://[device][@raw_device][@[title][:[chapter][:angle]]]``**

or

(VCD):

``% ``\ **``vlc``\ ````\ ``vcd://[device][@{E|P|E|T|S}[number]]``**

or

(`Audio CD <Documentation:Modules/cdda>`__):

``% ``\ **``vlc``\ ````\ ``cdda://[device][@[track]]``**

Receiving a network stream
~~~~~~~~~~~~~~~~~~~~~~~~~~

To receive an unicast RTP/UDP stream (sent by VLC's stream output), start VLC with:

``% ``\ **``vlc``\ ````\ ``rtp://@:5004``**

If 5004 is the `port <port>`__ to which packets are sent. 1234 is another commonly used port number. you use the default port (1234), **vlc rtp://** will do. For more information, look at the Streaming Howto.

To receive an multicast UDP/RTP stream (sent by VLC's stream output), start VLC with:

``% ``\ **``vlc``\ ````\ ``rtp://@multicast_address:port``**

To receive a `SSM <SSM>`__ (source specific multicast) stream, you can use:

``% ``\ **``vlc``\ ````\ ``rtp://server_address@multicast_address:port``**

This only works on OSs that support SSM (Windows XP and Linux).

To receive a HTTP stream, start VLC with:

``% ``\ **``vlc``\ ````\ ``http://www.example.org/your_file.mpg``**

To receive a RTSP stream, start VLC with:

``% ``\ **``vlc``\ ````\ ``rtsp://www.example.org/your_stream``**

Modules selection
-----------------

.. raw:: mediawiki

   {{See also|Documentation:Modules}}

VLC always tries to select the most appropriate interface, input and output modules, among the ones available on the system, according to the stream it is given to read. However, you may wish to force the use of a specific module with the following options.

-  **--intf <module>** allows you to select the interface module.
-  **--extraintf <module>** allows you to select extra interface modules that will be launched in addition to the main one. This is mainly useful for special *control* interfaces, like HTTP, RC (Remote Control), ... (see below)
-  **--aout <module>** allows you to select the audio output module.
-  **--vout <module>** allows you to select the video output module.
-  **--memcpy <module>** allows you to choose a memory copy module. You should probably never touch that.

You can get a listing of the available modules by using **vlc -l**

Stream Output
-------------

The Stream output system allows vlc to become a streaming server.

For more details on the stream output system, please have a look at the `Streaming HowTo <Documentation:Streaming_HowTo>`__.

| 

Other Options
-------------

Audio options
~~~~~~~~~~~~~

Note that in recent versions (3.x.x branch, possibly earlier):

-  ``--mono`` no longer exists: use ``--stereo-mode=0`` instead
-  ``--volume`` no longer exists but ``--volume-step`` and ``--gain`` may be used
-  ``--aout-rate`` no longer exists: ``--audio-resampler`` might be equivalent?
-  ``--desync`` no longer exists: use ``--audio-desync`` instead

--------------

-  **--audio**, **--no-audio** disables audio output. Note that if you are streaming (ex: to a file) this has no effect (streaming copies the audio verbatim). Use --sout-xxx instead (ex: --no-sout-audio)
-  **--gain <float>** audio gain (between 0 and 8)
-  **--volume-step <float>** audio output volume step (between 1 and 256)
-  **--volume-save**, **--no-volume-save** remember the volume (default enabled)
-  **--spdif**, **--no-spdif** Force S/PDIF support (default disabled)
-  **--force-dolby-surround** {0 (Auto), 1 (On), 2 (Off)} Force detection of Dolby Surround
-  **--stereo-mode** {0 (Unset), 1 (Stereo), 2 (Reverse stereo), 3 (Left), 4 (Right), 5 (Dolby Surround), 6 (Headphones)} Stereo audio output mode
-  **--audio-desync <integer>** Audio desynchronization compensation
-  **--audio-replay-gain-mode** {none,track,album} Replay gain mode
-  **--audio-replay-gain-preamp <float>** Replay preamp
-  **--audio-replay-gain-default <float>** Default replay gain
-  **--audio-replay-gain-peak-protection**, **--no-audio-replay-gain-peak-protection** Peak protection (default enabled)
-  **--audio-time-stretch**, **--no-audio-time-stretch** Enable time stretching audio (default enabled)
-  **-A**, **--aout** {any,pulse,alsa,sndio,adummy,afile,amem,none} Audio output module
-  **--role** {video,music,communication,game,notification,animation,production,accessibility,test} Media role
-  **--audio-filter <string>** adds audio filters to the processing chain. Available filters are visual (visualizer with spectrum analyzer and oscilloscope), headphone (virtual headphone spatialization) and normalizer (volume normalizer)
-  **--audio-visual** {any,visual,glspectrum,none} Audio visualizations
-  **--audio-resampler** {any,samplerate,ugly,soxr,speex_resampler,none} Audio resampler

Video options
~~~~~~~~~~~~~

-  **--no-video** disables video output.
-  **--grayscale** turns video output into grayscale mode.
-  **--fullscreen** ( or **-f**) sets fullscreen video.
-  **--nooverlay** disables `hardware acceleration <hardware_acceleration>`__ for the video output.
-  **--width, --height <integer>** sets the video window dimensions. By default, the video window size will be adjusted to match the video dimensions.
-  **--start-time <integer>** starts the video here; the integer is the number of seconds from the beginning (e.g. 1:30 is written as 90)
-  **--stop-time <integer>** stops the video here; the integer is the number of seconds from the beginning (e.g. 1:30 is written as 90)
-  **--zoom <float>** adds a zoom factor.
-  **--aspect-ratio <mode>** forces source aspect ratio. Modes are 4x3, 16x9, ...
-  **--spumargin <integer>** forces SPU subtitles postion.
-  **--video-filter <string>** adds video filters to the processing chain. You can add several filters, separated by commas
-  **--video-splitter <string>** adds video splitters to the processing chain. (wall, panoramix, clone)
-  **--sub-filter <string>** adds video subpictures filter to the processing chain.

Desktop/Screen grab options
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can see the various options for "grabbing the desktop" (VLC's built-in screen grabber capture device) by using the GUI. See http://forum.videolan.org/viewtopic.php?f=4&t=46971

Playlist options
~~~~~~~~~~~~~~~~

-  **--random** plays files randomly forever.
-  **--loop** loops playlist on end.
-  **--repeat** repeats current item until another item is forced
-  **--play-and-stop** stops the playlist after each played item.
-  **--no-repeat --no-loop** prevents the video from being executed again. (Useful when want to encode a file)

Network options
~~~~~~~~~~~~~~~

-  **--server-port <integer>** sets server port.
-  **--iface <string>** specifies the network interface to use.
-  **--iface-addr <string>** specifies your network interface IP address.
-  **--mtu <integer>** specifies the MTU of the network interface.
-  **--ipv6** forces IPv6.
-  **--ipv4** forces IPv4.

CPU options
~~~~~~~~~~~

You should probably not touch these options unless you know what you are doing.

-  **--nommx** disables the use of MMX CPU extensions.
-  **--no3dn** disables the use of 3D Now! CPU extensions.
-  **--nommxext** disables the use of MMX Ext CPU extensions.
-  **--nosse** disables the use of SSE CPU extensions.
-  **--noaltivec** disables the use of Altivec CPU extensions.

Miscellaneous options
~~~~~~~~~~~~~~~~~~~~~

-  **--quiet** deactivates all console messages.
-  **--color** displays color messages.
-  **--search-path <string>** specifies interface default search path.
-  **--plugin-path <string>** specifies plugin search path.
-  **--no-plugins-cache** disables the plugin cache (plugins cache speeds up startup)
-  **--dvd <string>** specifies the default DVD device.
-  **--vcd <string>** specifies the default VCD device.
-  **--program <integer>** specifies program (SID) (for streams with several programs, like satellite ones).
-  **--audio-type <integer>** specifies the default audio type to use with dvds.
-  **--audio-channel <integer>** specifies the default audio channel to use with dvds.
-  **--spu-channel <integer>** specifies the default subtitle channel to use with dvds.
-  **--version** gives you information about the current VLC version.
-  '''--module <module> ''' displays help about specified module. (Shortcut: **-p**)

Item-specific options
---------------------

There are many options that are related to items (like **--novideo**, **--codec**, **--fullscreen**).

For all of these, you have the possibility to make them item-specific, using ":" instead of "--" and putting the option just after the concerned item.

Examples:

``% ``\ **``vlc``\ ````\ ``file1.mpg :fullscreen``\ ````\ ``file2.mpg``**

will play file1.mpg in fullscreen mode and file2.mpg in the default mode (which is generally no fullscreen), whereas

``% ``\ **``vlc``\ ````\ ``--fullscreen``\ ````\ ``file1.mpg``\ ````\ ``file2.mpg``**

will play both files in fullscreen mode

``% ``\ **``vlc``\ ````\ ``--fullscreen``\ ````\ ``file1.mpg :sub-file=file1.srt :no-fullscreen``\ ````\ ``file2.mpg :filter=distort``**

will play file1.mpg in windowed (no-fullscreen) mode with the subtitles file file1.srt and will play file2.mpg with video filter distort enabled in fullscreen mode (item-specific options override global options).

Filters
-------

These are the old style VLC filters. They only apply to on screen display and thus cannot be streamed. However, on version 1.1.11 you are still able to apply these filters in *transcode* module using parameter *vfilter*. More information can be found on `Advanced Streaming Using the Command Line <Documentation:Streaming_HowTo/Advanced_Streaming_Using_the_Command_Line#vfilter>`__.

Deinterlacing video filter
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Further|Documentation:Modules/deinterlace}}

Module name: **deinterlace**

Invert video filter
~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Further|Documentation:Modules/invert}}

Module name: **invert**

Image properties filter
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Further|Documentation:Modules/adjust}}

Module name: **adjust**

Wall video filter
~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Further|Documentation:Modules/wall}}

Module name: **wall**

This filter splits the output in several windows. Note: for ``--wall-active``, to select windows 2 and 4 you would write **--wall-active 2,4**. When this option isn't specified, all windows are displayed.

Video transformation filter
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Further|Documentation:Modules/transform}}

Module name: **transform**

Distort video filter
~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Further|Documentation:Modules/distort}}

Module name: **distort**

Clone video filter
~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Further|Documentation:Modules/clone}}

This filter clones the output window.

Module name: **clone**

Crop video filter
~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Further|Documentation:Modules/crop}}

Module name: **crop**

Motion blur filter
~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Further|Documentation:Modules/motionblur}}

Module name: **motionblur**

Video pictures blending
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Further|Documentation:Modules/blend}}

Module name: **blend**

Video scaling filter
~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Further|Documentation:Modules/scale}}

Module name: **scale**

| 

Subpictures Filters
-------------------

These are the new VLC filters. They can be streamed.

Marquee display sub filter
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Further|Documentation:Modules/marq}}

Module name: **marq**

The sub filter was merged into this module.

Logo video filter
~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Further|Documentation:Modules/logo}}

Module name: **logo**

This filter can be used both as an old style filter or a subpictures filter.

Note: You can move the logo by left-clicking on it.

| 

.. raw:: mediawiki

   {{Documentation}}
