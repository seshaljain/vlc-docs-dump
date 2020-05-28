.. raw:: mediawiki

   {{lowercase}}

Development environment
-----------------------

To develop VLC for iOS, you need:

-  OS X 10.10 Yosemite (or later)
-  Latest Xcode version (version 6 works so far)
-  A correct shell (we recommend iTerm2 and zsh)
-  `CocoaPods <http://cocoapods.org>`__ (for dependency management)

Get the source
--------------

We provide source code packages for every release. You can find the latest on our `Download VLC for iOS website <http://www.videolan.org/vlc/download-ios.html>`__. Older releases `are also available <http://download.videolan.org/videolan/vlc-iOS/>`__.

Build it
--------

Install the dependencies

``pod update``

Wait, and grab a coffee.

Open the VLC.xcworkspace and run!

Deploy
------

Open the .xcworkspace (not .xcodeproj) in Xcode and click on Run.

Buliding release version needs code signing

Before running simulator in Xcode, run .sh with -s first; Before running iphoneos in Xcode, run .sh without -s first.

Send patches
------------

You can create patches and send them to our `mailing list <http://mailman.videolan.org/listinfo/ios>`__ ios@v.o, or on our `IRC <IRC>`__.

Please see `Git#Submitting_patches <Git#Submitting_patches>`__ on how to send patches...

Notes
-----

If everything goes well, congratulations to Lucky You! If not, please report any problem to our `mailing list <http://mailman.videolan.org/listinfo/ios>`__ ios@v.o, on our `IRC <IRC>`__ or join us on the `forum <http://forum.videolan.org>`__.

History
~~~~~~~

The first version of this howto was written by `jb <User:J-b>`__ on 18 July 2013.

Previous Version
~~~~~~~~~~~~~~~~

The old version of the app can be compiled using this `howto <MobileVLC>`__.

`Category:Building <Category:Building>`__ `Category:iOS <Category:iOS>`__
