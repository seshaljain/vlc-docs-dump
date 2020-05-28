Changes between 0.8.6d and 0.8.6e
=================================

Various bugfixes
----------------

-  Resume playback for viewing content over `FTP <Documentation:Modules/ftp>`__
-  Fixed XShm detection with remote `X11 <Documentation:Modules/x11>`__

Security updates
----------------

-  `Subtitle <Subtitle>`__ demuxers overflow ()
-  `HTTP listener <Documentation:Modules/http_intf>`__ format string injection ()
-  Fixed buffer overflow in the `SDL_image <Documentation:Modules/sdl_vout>`__ library ()
-  Real `RTSP <RTSP>`__ overflows (, , , )
-  Arbitrary memory overwrite in the `MP4 <MP4>`__ demuxer (`CORE-2008-0130 <http://www.coresecurity.com/?action=item&id=2147>`__, )

Audio filter
------------

-  Fixed `DTS <DTS>`__ to S/PDIF converter

Audio output
------------

-  Fixed 5.1 audio on ALSA

Access
------

-  Fixed some `RTSP <RTSP>`__ hanging and user/password passing through `RTSP <RTSP>`__ URLs

Stream output
-------------

-  Fixed waiting for SPS/PPS problem in `H.264 <H.264>`__ packetizer

Encoders
--------

-  Improved compatibility for creating `H.264 <H.264>`__ video files playable on iPhones
-  Improved detection of optimal amount of threads for multi-threaded `H.264 <H.264>`__ encoding on multi-cpu systems

   -  Note that this is used when `transcode <transcode>`__ threads is set to 0 (default)
   -  Not supported on Windows (multiple threads require manual configuration)

Mac OS X Interface & Port
-------------------------

-  Restored compatibility with Mac OS X 10.3.9
-  Corrected behavior of the `Preferences <Preferences>`__ panel
-  VLC no longer crashes on quit while playing

Localization
------------

-  Updated Romanian and Polish translations

`Category:Changelog <Category:Changelog>`__
