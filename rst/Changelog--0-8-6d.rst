Changes between 0.8.6c and 0.8.6d
=================================

Various bugfixes
----------------

-  Mozilla plugin: supports a reasonable amount of MIME types on Windows
-  Linux: Fixed S/PDIF passthrough with `ALSA <ALSA>`__
-  Automatic recovery on unexpected stream discontinuity (clock gap) occurrences in input
-  Use field order (top/bottom) for correct bob/linear deinterlacing
-  Fix invalid free in bookmarks loading code.

Windows and Mac OS Binaries
---------------------------

-  `FLAC <FLAC>`__ Security Update () to prevent multiple integer overflows

Active X plugin
---------------

-  Security update (`VideoLAN-SA-0703 <http://www.videolan.org/sa0703.html>`__, )

Mac OS X Interface & Port
-------------------------

-  Apple Remote support on Mac OS X 10.5 Leopard with enhanced functionality
-  Improved Video Output compatibility for Mac OS X 10.5 Leopard
-  Improved behavior of the Fullscreen Controller and mode changes between Fullscreen and Windowed Video Output
-  Softened the white flash artifacts that may appear during the transition of two different movies
-  Support for current `Ogg <Ogg>`__ file formats

NOTE: This release requires Mac OS X 10.4 or higher. Mac OS X 10.3.9 is not supported anymore.

Encoders
--------

-  Improved `H.264 <H.264>`__ encoding speed on Mac OS X

Other changes
-------------

-  The automatic updating facility was removed
-  You now need to append ``--m3u-extvlcopt`` to your command line to enable EXTVLCOPT options parsing in `m3u <M3U>`__ playlists ()
-  RTSP server remote denial of service fixed ()

`Category:Changelog <Category:Changelog>`__
