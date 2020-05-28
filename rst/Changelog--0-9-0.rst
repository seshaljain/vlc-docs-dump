Changes between 0.8.6 and 0.9.0
===============================

Important notes
---------------

-  This version of VLC contains a `new interface <Qt_Interface>`__ for Windows and Linux. This interface lacks a few features that used to be present in vlc 0.8.6:

   -  "Streaming wizard" and "VLM control". These features will be replaced by a better alternative in the next version. If you absolutely need these features, we advise you to keep vlc 0.8.6
   -  Similarly, "Bookmarks" will be reintroduced in an improved version at a later point

-  The default Interface is now `Qt Interface <Qt_Interface>`__ on linux and windows.
-  The default for --sout-keep has changed. It's now activated by default.
-  The marq, mosaic and logo commands in the `rc interface <Console#rc_interface>`__ changed. They now require a target name as their first argument. Example:

   ::

      vlc --sub-filter "marq@test{marquee=Hello}" -I rc <somevideo> 

   You can then use commands like:
   ::

      @test marq-marquee Goodbye

   These new commands are also available in the `telnet interface <Console#telnet_interface>`__.

-  The `HTTP Interface <HTTP_Interface>`__ is now only available on the local machine by default.

   If you want to make it available from other machines, you will have to edit the ".hosts" file.

   -  On UNIX/Linux, the file is in /usr/share/vlc/http/.hosts

      If you're using the old http interface, it's located in /usr/share/vlc/http/old/.hosts

   -  On Windows they are in C:\Program Files\VideoLAN\VLC\http\.hosts and C:\Program Files\VideoLAN\VLC\http\old\.hosts
   -  On Mac OS X, you can find it in VLC.app/Contents/MacOS/share/http/.hosts and respectively in VLC.app/Contents/MacOS/share/http/old/.hosts

-  The "`rtp <RTP>`__" access output module has been removed:

   Please use the RTP stream output instead, e.g.:
   Old: '#std{access=rtp,dst=239.255.1.2,sap}'
   New: '#rtp{dst=239.255.1.2,sap}'

Important Changes
-----------------

Playlist
~~~~~~~~

-  Vastly improved playlist support:

   -  `Media library <Media_library>`__ support
   -  "Live search"
   -  `Shoutcast <Shoutcast>`__ TV listings
   -  `Audioscrobbler <http://www.audioscrobbler.net/>`__/`last.fm <http://www.last.fm/>`__ support

-  Album art support
-  User definable Lua playlist scripts. See `share/luaplaylist/README.txt <http://trac.videolan.org/vlc/browser/trunk/share/luaplaylist/README.txt>`__

   (Default scripts open YouTube, DailyMotion, metacafe and Google Video URLs)

-  User definable Lua metadata and album art fetcher scripts. See `share/luameta/README.txt <http://trac.videolan.org/vlc/browser/trunk/share/luameta/README.txt>`__

Input/Demuxers
~~~~~~~~~~~~~~

-  `UDP-Lite <UDP-Lite>`__ transport for `RTP <RTP>`__/`AVP <AVP>`__
-  `DCCP <DCCP>`__ transport for `RTP <RTP>`__/`AVP <AVP>`__
-  Proxy support for `MMSH <MMSH>`__ stream
-  `JACK <JACK>`__ audio input support
-  MP4 gpac and Apple chapter support
-  Input run time option (improved live stream recording)
-  Fixed aiff stereo file
-  Fixed audio glitch on seek
-  Improved FLAC demuxer (duration / current time / meta data)
-  AAC tags support
-  APEv1/2 tags support
-  Improved ID3v2 tags support
-  Improved Ogg/Vorbis tags support
-  Raw video support
-  Standard MIDI File (types 0 & 1) support
-  Tivo Series 2 support
-  v4l2 access module support
-  CD+G karaoke Files support
-  MXF files support

Decoders
~~~~~~~~

-  `VP60/VP61/VP6F/VP62 <VP6>`__ support
-  `MKV <MKV>`__ `USF <USF>`__ subtitles support
-  HTML based subtitles support
-  Flash Screen Video support
-  CamStudio Screen Video support
-  DOSBox Capture support
-  Karl Morton's Video support
-  limited atrac3 support
-  Fluidsynth MIDI software synthesis (with external sound fonts)
-  New codec FOURCCs to support more specific files: Avid, FCP, Sony, Samsung, ...
-  Closed Caption Decoder (DVD, ReplayTV, Tivo, DVB/ATSC)
-  H.264 PAFF support
-  DNxHD / VC-3 support
-  NellyMoser ASAO support
-  APE (Monkey audio) support
-  VBI & EBU (Teletext) support

Encoders
~~~~~~~~

-  Flash Screen Video support

Video output and filters
~~~~~~~~~~~~~~~~~~~~~~~~

-  `Adjust <Documentation:Modules/adjust>`__, `Invert <Documentation:Modules/invert>`__ and `Distort <Documentation:Modules/distort>`__ (now split into `Wave <Documentation:Modules/wave>`__, `Ripple <Documentation:Modules/ripple>`__, `Gradient <Documentation:Modules/gradient>`__ and `Psychedelic <Documentation:Modules/psychedelic>`__) video filters can now be streamed
-  New `puzzle <Documentation:Modules/puzzle>`__ video output filter
-  Rewrite `motion detection <Documentation:Modules/motion_control>`__ video filter
-  New `extract <Documentation:Modules/extract>`__ video filter (extract Red, Green and Blue components from a video)
-  New `sharpen <Documentation:Modules/sharpen>`__ video filter (increase the contrast of adjacent pixels)
-  New `erase <Documentation:Modules/erase>`__ video filter (remove a logo from a video)
-  Enhancements to subtitles' renderer to support bold, italics and some HTML tags
-  Support for RGBA and I420 blending. This improves `Mosaic <Mosaic>`__ CPU usage \*a lot*.
-  New transparency mask video filter (for use with the mosaic_bridge module).
-  New bluescreen video filter (for use with the mosaic_bridge module). This was previously part of the mosaic module.
-  Fix random characters problem in RSS filter.
-  Add rotate-deciangle for more precision on rotate filter
-  Support for Intel SSE2 intruction set in chroma converters
-  Improved use of Intel MMX intruction set in chroma converters

Audio output and filters
~~~~~~~~~~~~~~~~~~~~~~~~

-  Replay gain support.
-  Play audio when going slower/faster ( no pitch filter yet ).
-  New spatializer audio filter.

Stream output
~~~~~~~~~~~~~

-  RTSP for TS-multiplexed broadcast streams
-  New RTP payload formats:

   -  Speex voice audio codec
   -  ITU T.140 (for text, subtitles) output
   -  G.711 (both A-law and µ-law) output

-  UDP-Lite transport for RTP
-  DCCP transport for RTP
-  Lots of fixes for RTSP broadcasting

Interfaces
~~~~~~~~~~

-  Windows/Linux

   -  Brand `new interface <Qt4_Interface>`__ for Linux and Windows, based on the Qt toolkit

-  All

   -  Improved user interaction
   -  Improved `mouse gestures <Mouse_Gestures>`__
   -  Experimental Lua interface modules. See vlc -I lua for more info

-  Unix

   -  Option to allow only one running instance, using `D-Bus <D-Bus>`__ interface.
   -  `D-Bus <D-Bus>`__ Interface implementing the MPRIS (Media Player Remote Interfacing specification - see `DBus-spec <DBus-spec>`__), a common dbus control interface for media players that intends to become an xdg standard when finished: `1 <http://wiki.xmms2.xmms.se/index.php/Media_Player_Interfaces>`__.

-  Motion module use disk accelerometers to keep video horizontal
-  Ncurses interface now uses ncursesw to correctly display wide characters when using an UTF-8 locale.
-  Plugin to set Telepathy presence message using MissionControl

Linux Port
~~~~~~~~~~

-  VLC now complies with the `XDG Base Directory Specification version 0.6 <http://standards.freedesktop.org/basedir-spec/basedir-spec-0.6.html>`__ (which means that VLC doesn't use the $HOME/.vlc directory anymore)

Mac OS X Port
~~~~~~~~~~~~~

-  Mac OS X Framework that can be used to embed VLC in third party applications. (Google Summer Of Code Student project).

LibVLC
~~~~~~

-  Event management and various improvement in libvlc. (Part of a Google Summer Of Code Student project).

Capture
~~~~~~~

-  new `BDA <BDA>`__ device driver plugin for `DVB <DVB>`__-C/S/T capture cards on Microsoft Windows

Localisations
~~~~~~~~~~~~~

-  Finnish
-  Persian
-  Polish

Changes in between
------------------

Links to changelogs between:

   `0.8.6h and 0.8.6i <Changelog/0.8.6i>`__
   `0.8.6g and 0.8.6h <Changelog/0.8.6h>`__
   `0.8.6f and 0.8.6g <Changelog/0.8.6g>`__
   `0.8.6e and 0.8.6f <Changelog/0.8.6f>`__
   `0.8.6d and 0.8.6e <Changelog/0.8.6e>`__
   `0.8.6c and 0.8.6d <Changelog/0.8.6d>`__
   `0.8.6b and 0.8.6c <Changelog/0.8.6c>`__
   `0.8.6a and 0.8.6b <Changelog/0.8.6b>`__
   `0.8.6 and 0.8.6a <Changelog/0.8.6a>`__

`Category:Changelog <Category:Changelog>`__
