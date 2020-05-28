.. raw:: html

   <div style="float: right; margin-left: 1em;">

\__TOC_\_

.. raw:: html

   </div>

This page lists most of the present in the official `VLC source code <VLC_source_code>`__. Understanding these pages might require that you know about VLC and its command line usage. It is recommended that you read the other `documentation <Documentation:Documentation>`__ first.

To list all the available modules in your VLC build, use:

``{{%}} ``\ **``vlc``\ ````\ ``--list``**

To list a module's configuration options, use:

``% ``\ **``vlc``\ ````\ ``-p``\ ````\ \ ````\ ``--advanced``\ ````\ ``--help-verbose``**

Interfaces
----------

Graphical
~~~~~~~~~

-  `macOS <Documentation:Modules/macos>`__
-  `Qt4 <Documentation:Modules/Qt4>`__
-  `Skins2 <Documentation:Modules/skins2>`__
-  `wxWidgets <Documentation:Modules/wxWidgets>`__ (up to 0.9)

Text
~~~~

-  `remote control (rc) <Documentation:Modules/rc>`__
-  `telnet <Documentation:Modules/telnet>`__ (until 2.0.0)
-  `ncurses <Documentation:Modules/ncurses>`__

-  `lua <Documentation:Modules/lua>`__

Other
~~~~~

-  `HTTP <Documentation:Modules/http_intf>`__
-  `Hotkeys <Documentation:Modules/hotkeys>`__
-  `lirc <Documentation:Modules/lirc>`__
-  `osc <Documentation:Modules/osc>`__
-  `Wiimote <Documentation:Modules/wiimote>`__

Outputs
-------

Audio Output
~~~~~~~~~~~~

-  `file <Documentation:Modules/file_aout>`__
-  `portaudio <Documentation:Modules/portaudio>`__ (up to 2.0)
-  `SDL <Documentation:Modules/sdl_aout>`__ (up to 1.1.13)

Android specific:

-  `OpenSL ES <Documentation:Modules/opensles>`__

Linux specific:

-  `Alsa <Documentation:Modules/alsa>`__
-  `aRts <Documentation:Modules/arts>`__ (up to 0.9.10)
-  `esound <Documentation:Modules/esd>`__ (up to 0.9.10)
-  `jack <Documentation:Modules/jack>`__
-  `pulse <Documentation:Modules/pulse>`__
-  `OSS <Documentation:Modules/oss>`__

macOS specific:

-  

   .. raw:: mediawiki

      {{docmod|audioqueue}}

   (up to 2.2.8)

-  

   .. raw:: mediawiki

      {{docmod|auhal}}

   (HAL AudioUnit)

Windows specific:

-  `DirectX <Documentation:Modules/directx_aout>`__
-  `WASAPI <Documentation:Modules/mmdevice>`__
-  `waveout <Documentation:Modules/waveout>`__

Video Output
~~~~~~~~~~~~

-  `ASCII Art <Documentation:Modules/aa>`__
-  `Colored ASCII Art <Documentation:Modules/caca>`__
-  `Image <Documentation:Modules/image>`__ (up to 0.9.10)
-  `OpenGL <Documentation:Modules/opengl>`__
-  `SDL <Documentation:Modules/sdl_vout>`__ (up to 2.2.8)

Linux specific:

-  `Direct framebuffer <Documentation:Modules/directfb>`__ (up to 2.2.8)
-  `Framebuffer <Documentation:Modules/fb>`__
-  `OpenGL (GLX) <Documentation:Modules/glx>`__
-  `X11 <Documentation:Modules/x11>`__
-  `XVideo <Documentation:Modules/xvideo>`__

Windows specific:

-  `Direct3D <Documentation:Modules/direct3d>`__
-  `DirectX <Documentation:Modules/directx_vout>`__
-  `OpenGL for windows <Documentation:Modules/glwin32>`__
-  `Windows GDI <Documentation:Modules/wingdi>`__

Stream Output
~~~~~~~~~~~~~

.. raw:: html

   <div class="col3">

-  `Autodel <Documentation:Modules/autodel>`__
-  `Delay <Documentation:Modules/delay>`__
-  `Description <Documentation:Modules/description>`__
-  `Display <Documentation:Modules/display>`__
-  `Dummy <Documentation:Modules/dummy_sout>`__
-  `Duplicate <Documentation:Modules/duplicate>`__
-  `Elementary Stream (es) <Documentation:Modules/es>`__
-  `Gather <Documentation:Modules/gather>`__
-  `RTP <Documentation:Modules/rtp>`__
-  `Standard (std) <Documentation:Modules/standard>`__
-  `Switcher <Documentation:Modules/switcher>`__ (up to 2.0.9)
-  `Transcode <Documentation:Modules/transcode>`__
-  `Transrate <Documentation:Modules/transrate>`__ (up to 1.0.2)

.. raw:: html

   </div>

The following are for use in the mosaic framework only:

.. raw:: html

   <div class="col3">

-  `Bridge In <Documentation:Modules/bridge-in>`__
-  `Bridge Out <Documentation:Modules/bridge-out>`__
-  `Mosaic Bridge <Documentation:Modules/mosaic-bridge>`__

.. raw:: html

   </div>

Filters
-------

Audio Filters
~~~~~~~~~~~~~

Video Filters
~~~~~~~~~~~~~

.. raw:: html

   <div class="col3">

-  `Adjust <Documentation:Modules/adjust>`__
-  `Anaglyph 3D <Documentation:Modules/anaglyph>`__
-  `AtmoLight <Documentation:Modules/atmo>`__ (up to 3.0.0)
-  `Color Threshold <Documentation:Modules/colorthres>`__
-  `Distort <Documentation:Modules/distort>`__ (up to 0.8.6 - split into various)
-  `Logo Erase <Documentation:Modules/erase>`__
-  `Extract <Documentation:Modules/extract>`__
-  `Freeze <Documentation:Modules/freeze>`__
-  `Gaussian Blur <Documentation:Modules/gaussianblur>`__
-  `Gradfun <Documentation:Modules/gradfun>`__
-  `Gradient <Documentation:Modules/gradient>`__
-  `Invert <Documentation:Modules/invert>`__
-  `Motion Blur <Documentation:Modules/motionblur>`__
-  `Noise <Documentation:Modules/noise>`__ (up to 1.1.13)
-  `Oldmovie <Documentation:Modules/oldmovie>`__
-  `Posterize <Documentation:Modules/posterize>`__
-  `Psychedelic <Documentation:Modules/psychedelic>`__
-  `Ripple <Documentation:Modules/ripple>`__
-  `Rotate <Documentation:Modules/rotate>`__
-  `Scene <Documentation:Modules/scene>`__
-  `Sepia <Documentation:Modules/sepia>`__
-  `Sharpen <Documentation:Modules/sharpen>`__
-  `VHS <Documentation:Modules/VHS>`__
-  `Wave <Documentation:Modules/wave>`__

.. raw:: html

   </div>

The following video filters are for use in transcode only:

-  `Canvas <Transcode#Canvas_and_Padding>`__
-  `Crop Padd <Transcode#Canvas_and_Padding>`__

The following video filters are for use in the mosaic framework only:

-  `Alpha mask <Documentation:Modules/alphamask>`__
-  `Blue Screen <Documentation:Modules/bluescreen>`__

Video Sub-Filters
~~~~~~~~~~~~~~~~~

-  `Logo <Documentation:Modules/logo>`__
-  `Marq <Documentation:Modules/marq>`__
-  `Mosaic <Documentation:Modules/mosaic>`__
-  `RSS <Documentation:Modules/rss>`__
-  `Subsdelay <Documentation:Modules/subsdelay>`__
-  `Time <Documentation:Modules/time>`__ (up to 0.8.6 - merged with marq)

Video Output Filters
~~~~~~~~~~~~~~~~~~~~

-  `Crop <Documentation:Modules/crop>`__
-  `Deinterlace <Documentation:Modules/deinterlace>`__
-  `Logo <Documentation:Modules/logo>`__
-  `Magnify <Documentation:Modules/magnify>`__
-  `Puzzle <Documentation:Modules/puzzle>`__
-  `Transform <Documentation:Modules/transform>`__

Video Splitters
^^^^^^^^^^^^^^^

-  `Clone <Documentation:Modules/clone>`__
-  `Panoramix <Documentation:Modules/panoramix>`__
-  `Wall <Documentation:Modules/wall>`__

Visualizations
~~~~~~~~~~~~~~

-  `Galaktos <Documentation:Modules/galaktos>`__ (up to 1.0.6)
-  `Goom <Documentation:Modules/goom>`__
-  `ProjectM <Documentation:Modules/projectm>`__
-  `Visual <Documentation:Modules/visual>`__
-  `Vovoid VSXu <Documentation:Modules/vsxu>`__

Access Filters
~~~~~~~~~~~~~~

-  `Bandwidth <Documentation:Modules/bandwidth>`__
-  `Dump <Documentation:Modules/dump>`__
-  `Record <Documentation:Modules/record>`__
-  `Timeshift <Documentation:Modules/timeshift>`__ (up to 0.9.9 - moved to core)

.. _other-1:

Other
-----

Accesses
~~~~~~~~

.. raw:: html

   <div class="col3">

-  `CD Input <Documentation:Modules/cdda>`__
-  `Directory <Documentation:Modules/directory>`__
-  `DVDnav Input <Documentation:Modules/dvdnav>`__ - DVD with menus
-  `DVDRead Input <Documentation:Modules/dvdread>`__ - DVD without menus
-  `Fake <Documentation:Modules/fake>`__ (up to 0.9.0) - presents a static image as a video stream
-  `File Input <Documentation:Modules/file>`__ - for reading local files
-  `FTP Input <Documentation:Modules/ftp>`__
-  `H.264 Video <Documentation:Modules/h26x>`__
-  `HTTP Input <Documentation:Modules/http>`__
-  

   .. raw:: mediawiki

      {{docmod|jpeg}}

-  

   .. raw:: mediawiki

      {{docmod|mjpeg}}

-  `Matroska stream <Documentation:Modules/mkv>`__
-  `MMS <Documentation:Modules/mms>`__ - for reading from the MicroSoft Media Server
-  `Raw Video <Documentation:Modules/rawvid>`__ - streams of bitmap images
-  `RTP Input <Documentation:Modules/rtp>`__
-  `RTSP <Documentation:Modules/rtsp>`__
-  

   .. raw:: mediawiki

      {{docmod|sdp}}

-  `Screen Input <Documentation:Modules/screen>`__ - screen feed
-  `UDP Input <Documentation:Modules/udp>`__
-  `VCD <Documentation:Modules/vcd>`__

.. raw:: html

   </div>

Linux specific:

-  `DC1394 <Documentation:Modules/dc1394>`__
-  `DVB Input <Documentation:Modules/dvb>`__
-  `PVR <Documentation:Modules/pvr>`__ (IVTV MPEG Encoding Card Input) (up to 2.0.9)
-  `DV <Documentation:Modules/rawdv>`__ (through libdv)
-  `Video4Linux (v4l) <Documentation:Modules/v4l>`__ (up to 1.1.13)
-  `Video4Linux2 (v4l2) <Documentation:Modules/v4l2>`__

Windows specific:

-  `BDA <Documentation:Modules/bda>`__
-  `DirectShow <Documentation:Modules/dshow>`__

macOS specific:

-  `EyeTV <Documentation:Modules/eyetv>`__ (up to 2.2.8) - reads DVB streams from the proprietary EyeTV.app; requires a plugin
-  `qtcapture <Documentation:Modules/qtcapture>`__ (up to 2.2.8) - reads uncompressed video from internal iSights
-  

   .. raw:: mediawiki

      {{docmod|qtsound}}

-  

   .. raw:: mediawiki

      {{docmod|avcapture}}

Access Outputs
~~~~~~~~~~~~~~

-  

   .. raw:: mediawiki

      {{docmod|shout}}

   (shoutcast/icecast)

Codecs
~~~~~~

Audio
^^^^^

-  

   .. raw:: mediawiki

      {{docmod|a52}}

-  

   .. raw:: mediawiki

      {{docmod|flac}}

-  

   .. raw:: mediawiki

      {{docmod|mpc}}

   - `Musepack <Musepack>`__

-  

   .. raw:: mediawiki

      {{docmod|ogg}}

-  

   .. raw:: mediawiki

      {{docmod|vorbis}}

-  

   .. raw:: mediawiki

      {{docmod|wav}}

Video
^^^^^

-  

   .. raw:: mediawiki

      {{docmod|h26x}}

-  

   .. raw:: mediawiki

      {{docmod|nsv}}

-  

   .. raw:: mediawiki

      {{docmod|schroedinger}}

-  

   .. raw:: mediawiki

      {{docmod|vpx}}

Subtitles
^^^^^^^^^

-  `kate <Documentation:Modules/kate>`__
-  `subtitle <Documentation:Modules/subtitle>`__
-  

   .. raw:: mediawiki

      {{docmod|telx}}

Demuxers
~~~~~~~~

-  `avcodec <Documentation:Modules/avcodec>`__ ("FFmpeg")

Playlist
^^^^^^^^

-  

   .. raw:: mediawiki

      {{docmod|playlist}}

   (formats are read with sub-modules)

Muxers
~~~~~~

-  

   .. raw:: mediawiki

      {{docmod|asf}}

-  

   .. raw:: mediawiki

      {{docmod|avformat}}

-  

   .. raw:: mediawiki

      {{docmod|avi}}

-  

   .. raw:: mediawiki

      {{docmod|daala}}

-  

   .. raw:: mediawiki

      {{docmod|mp4}}

-  

   .. raw:: mediawiki

      {{docmod|mpjpeg}}

-  

   .. raw:: mediawiki

      {{docmod|ogg}}

-  

   .. raw:: mediawiki

      {{docmod|schroedinger}}

-  

   .. raw:: mediawiki

      {{docmod|vpx}}

-  

   .. raw:: mediawiki

      {{docmod|wav}}

Service Discovery
~~~~~~~~~~~~~~~~~

-  `Bonjour <Documentation:Modules/bonjour>`__
-  `DAAP <Documentation:Modules/daap>`__
-  `HAL <Documentation:Modules/hal>`__ (up to 1.1.13)
-  `SAP <Documentation:Modules/sap>`__
-  `Shoutcast <Documentation:Modules/shout>`__
-  `podcast <Documentation:Modules/podcast>`__
-  `UPnP <Documentation:Modules/upnp>`__

Misc
~~~~

-  `Motion control <Documentation:Modules/motion_control>`__
-  `Netsync <Documentation:Modules/netsync>`__

`\* <Category:Modules>`__
