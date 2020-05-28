\__NOTOC_\_ VLC 2.0 **Twoflower** is a major new version of our popular media player. With faster decoding on multi-core, GPU, and mobile hardware and the ability to open more formats, notably professional, HD and 10bits codecs, 2.0 is a major upgrade for VLC. Twoflower has a new rendering pipeline for video, with higher quality subtitles, and new video filters to enhance your videos. It supports many new devices and BluRay Discs (experimental). Completely reworked Mac and Web interfaces and improvements in the other interfaces make VLC easier than ever to use. Twoflower fixes several hundreds of bugs, in more than 7000 commits from 160 volunteers.

Features
--------

Video
~~~~~

-  Rewritten video output core and modules, allowing subpicture blending in GPU.
-  Shader support in the OpenGL output, for colorspace conversion, including 10bits.
-  New video outputs for Windows 7, Android, iOS and OS/2.
-  New debanding, grain, denoising and anti-flickering filters.
-  New deinterlacing filter, including an Inverse Telecine algorithm.

Audio
~~~~~

-  New resamplers for higher quality audio.
-  New dynamic range compressor and karaoke filters.
-  Simplification of the audio core for faster processing.
-  New audio outputs for iOS, Android and OS/2.

Formats
~~~~~~~

-  Multi-threaded decoding for H.264, MPEG-4/Xvid and WebM.
-  Support for 10bits codecs, WMV image and some other codecs.
-  Rewritten support for images, including jpeg, png, xcf, bmp...
-  Important changes in RealVideo and Real Format support.
-  CrystalHD cards and Android OpenMAX support for hardware decoding.

Input and Devices
~~~~~~~~~~~~~~~~~

-  Experimental support for BluRay discs:

   -  Menus are deactivated in this release (will come soon).
   -  MACS and BD+ DRM libraries and keys are not shipped, for legal reasons.

-  Support for SDI capture cards and QTKit devices.
-  Support for new adaptive streaming protocols, like HLS and DASH.

For Mac Users
~~~~~~~~~~~~~

-  Completely new, single window interface:

   -  Available in 2 colors: Lion grey and QTX black.
   -  Extensions support and better Lion integration.

-  Support for all QTKit devices through qtcapture and qtsound modules.
-  Continued support for X 10.5 and PPC users (1080p and ProRes on Dual-G5!).

For Anime Fans
~~~~~~~~~~~~~~

-  Vastly improved MKV demuxer.
-  Rewritten linked segments and ordered chapter files support.
-  Correct support for FLAC, RV and Hi10p in MKV.
-  Rewritten seeking support in cue files.
-  Various ASS subtitles improvements.

For Professional Users
~~~~~~~~~~~~~~~~~~~~~~

-  Support for ProRes 422 and 4444, AVC/Intra.
-  Support for Jpeg-2000 and DNxHD/VC-3 in 10bits.
-  Support for EBU subtitles (stl) and EIA-608.
-  SDI and HD-SDI card support for input on Linux.
-  New Dirac/VC-2 encoder, faster than the previous one.

For Developers
~~~~~~~~~~~~~~

-  libVLC, libVLCcore and libcompat have switched from GPL to `LGPLv2.1+ <http://www.videolan.org/press/lgpl-libvlc.html>`__.
-  New libVLC examples are available: media player, photobooth and mediainfo clones.
-  New JSON requests on the web interface to control running VLC instances.
-  Implementation of the `MPRIS2 <http://www.mpris.org/2.1/spec/>`__ interface to control media players.
-  VLC's web plugins have been rewritten for better integration and stability in all browsers.

External links
--------------

-  `Download on main site <http://www.videolan.org/vlc/releases/2.0.1.html>`__

`Category:About VideoLAN <Category:About_VideoLAN>`__ `Category:Changelog <Category:Changelog>`__
