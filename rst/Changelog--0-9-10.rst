Changes between 0.9.9a and 0.9.10
=================================

HTTP Interface
--------------

-  Fixed default ACL

Mac OS X
--------

-  Fixed crashes on multi-screen setups
-  Corrected volume and subtitle encoding options in the Preferences
-  Improved Information panel behavior, when playlist is not displayed
-  Fixed `QTCapture <Documentation:Modules/qtcapture>`__ input support for the latest iSight models
-  Added a menu-item to unlock the video window's aspect ratio
-  Fixed redraw issues when autosizing the video window
-  Updated libpng, libgpg-error, libgcrypt, fribidi

Various fixes to the following modules
--------------------------------------

-  access:

   -  `HTTP <Documentation:Modules/http>`__, SMB
   -  updated and additional access scripts (BBC radio, dailymotion, ...)
   -  Prevent integer underflow in Real pseudo-RTSP module, discovered by tixxDZ, DZCORE Labs, Algeria

-  stream out:

   -  RTP, RTSP VoD, `Mosaic Bridge <Documentation:Modules/mosaic-bridge>`__

-  decoder:

   -  TSCC

`Category:Changelog <Category:Changelog>`__
