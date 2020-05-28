.. raw:: mediawiki

   {{Historical|Largely superseded by [[iOSCompile]]}}

MobileVLC is the other name of the VLC application for iOS 1.0

Warning
-------

Those **old** and **outdated** versions libraries (MobileVLC and VLCKit) are **GPL**, meaning that if you use any of their components in your application, your need to **open source your application** and comply to the GPL licence.

If you want a **LGPL** library, please refer to the new ones, that are documented `here <iOSCompile>`__.

If you use VLCKit or libvlc please **credit VLC**. And add your name to the `LibVLC Users <LibVLC_Users>`__ page.

Source Code
-----------

Source Code is available on:

-  `gitweb <http://git.videolan.org/?p=MobileVLC.git;a=summary>`__

Build process details
---------------------

For more details on the build process, see:

-  `MobileVLC's HOWTO <http://git.videolan.org/?p=MobileVLC.git;a=blob;f=HOWTO;hb=HEAD>`__

Short summary
-------------

A short summary is:

| ``$ git clone ``\ ```git://git.videolan.org/MobileVLC.git`` <git://git.videolan.org/MobileVLC.git>`__
| ``$ cd MobileVLC``
| ``$ ./buildMobileVLC.sh``

Wait a bit, and you are done!

Requirements
------------

You will require the **iPhoneOS 3.2 sdk**, though 4.2 should be supported with:

``$ ./buildMobileVLC.sh -k iphoneos4.2``

Simulator
---------

The iOS simulator is also supported, using:

``$ ./buildMobileVLC.sh -s``

For more information, see:

``$ ./buildMobileVLC.sh -h``

`Category:Building <Category:Building>`__ `Category:iOS <Category:iOS>`__
