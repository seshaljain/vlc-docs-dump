.. raw:: mediawiki

   {{Historical}}

To see the current changes under development, read `Next changes <Next_changes>`__ (also historical). \__TOC_\_

.. raw:: mediawiki

   {{Transcluded|Changelog/1.0.1}}

.. raw:: mediawiki

   {{:Changelog/1.0.1}}

--------------

.. raw:: mediawiki

   {{Transcluded|Changelog/0.9.10}}

.. raw:: mediawiki

   {{:Changelog/0.9.10}}

--------------

.. raw:: mediawiki

   {{Transcluded|Changelog/0.9.0}}

.. raw:: mediawiki

   {{:Changelog/0.9.0}}

Changes between 0.8.5 and 0.8.6
===============================

Playlist
--------

-  Shoutcast TV listings support

Input
-----

-  Support for RTSP authentication
-  Support for adding subtitles on the fly
-  Fixed MPEG-PS duration calculation
-  ATSC support for DVB input
-  Partial reading support for DVR-ms recordings
-  Partial reading support for MXF and GXF fileformat
-  Improved support for Flash Video files

Decoders
--------

-  Native WMV9/VC-1 support
-  WMA Speech support (through binary codecs)
-  VP5/VP6 - Flash Video support (not VP61)
-  The True Audio Lossless codec support
-  Matroska WavPack support
-  Improved H.264 support (interlaced, speed improvements etc but no PAFF)
-  Fixed a problem with MPEG2 field pictures
-  Fixed swapped colors on DVB subtitles

Video output
------------

-  Additional OpenGL effects (cylinder, torus, sphere, ...)
-  Experimental Direct3D 9 video output (win32). Best served on Vista :)
-  Improved libcaca support

Interfaces
----------

-  All

   -  New hotkeys for crop and zoom
   -  Support for snapshots from the HTTP interface

-  Windows

   -  Systray support in skins

-  OS X

   -  Support for Apple Remote control
   -  Fullscreen controller panel (artwork by Simon Damkjær Andersen)
   -  New playmode buttons (artwork by Simon Damkjær Andersen)
   -  right/ctrl-click menu in video outputs
   -  Main Menu uses autohide when playing videos in fullscreen mode

-  Linux

   -  Notifications using notification-daemon

Windows port
------------

-  Support for Unicode filenames (Windows NT and above)

      Windows 9x/ME users:

      -  Please note that these versions of Windows are not officially supported
      -  Unicode support for Windows 9x/ME applications is available through the

            Microsoft Layer for Unicode available from the following location: http://www.microsoft.com.nsatc.net/globaldev/handson/dev/mslu_announce.mspx
            Download the MSLU package (unicows) and extract the content into the folder C:\Windows\System

-  Fixed IPv6 support on the client side
-  Fixed disable screensaver (Direct3D and DirectX video output)

Localization
------------

-  Add Czech
-  Add Slovak
-  Add Malay
-  Add Slovenian

Developers
----------

-  Updates to the libvlc API
-  Fixes for the mozilla and activeX plugins

`Category:Changelog <Category:Changelog>`__
