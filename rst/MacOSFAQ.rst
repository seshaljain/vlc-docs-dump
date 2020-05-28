.. raw:: mediawiki

   {{Outdated|important=y}}

.. raw:: mediawiki

   {{Lowercase}}

On Mac OS 9
^^^^^^^^^^^

Sorry, VLC will not work on OS 9, and probably never will. However, Mac OS X is supported.

Why VLC 0.8.1 doesn't work with Mac OS X 10.1.5?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because we do use functions which aren't available in this version. The 0.7.0 release is the last one which supports this OS. Additionally, you shouldn't use it anymore, since 10.2 is much faster than 10.1.5 even on older Macs.

Which is the last release for 10.2.8?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

That's VLC 0.8.4a. Note that it requires QuickTime 6.5.2, which is the latest QuickTime version for this Mac OS X release series. With prior versions, you'll get unexpected video output results.

Why doesn't VLC 0.8.6a work on 10.3, although you state it does?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First of all, make sure that you got 10.3.9 installed. Any earlier release, particularly 10.3.5 and below, doesn't support current versions of VLC. Additionally, while QuickTime 6.5.2 is strictly required, QuickTime 7.x is strongly recommended for performance and usability reasons.

Do current releases of VLC work on Mac OS 10.5 / Leopard?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, VLC 0.8.6b runs without any problems out of the box. VLC's next major release 0.9.0 will add further support (most importantly the ability to compile VLC on Leopard) and may include some exclusive features.

VLC just bounces in the Dock and quits or just shows a "VLC" menu and nothing else. What to do?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Please check whether you're using a VLC release which is able to run on your version of Mac OS X. If it fits, run the "Remove Preferences" script provided on VLC's disk-image or delete both a folder called "VLC" and a file called org.videolan.vlc.plist in ~/Library/Preferences (your personal preferences folder).

I am on Mac OS 9. Which version of VLC can I run?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the download page notes: "There is not, and there will never be, a version for Mac OS 9." http://www.videolan.org/vlc/download-macosx.html

How do you tell Apple's &$@&$*&! DVDPlayer not to start automatically when you insert a DVD?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get to Mac OS X global system preferences, open up the "CDs & DVDs" section in the "Hardware" category, add VLC to the list of apps next to "When you insert a video DVD" and select it afterwards. That's it. Note that setting up VLC for Audio CD playback is possible this way as well.

Why won't VLC play DVDs from a region other than what my drive is set to?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Many people try to use VLC to play DVDs from regions their drive is not set to. However, the DVD drives on most new Macs have region lockout on the hardware level, so VLC will not necessarily be able to play discs from multiple regions. You *may* be able to play the disc by opening it as a Video_TS folder instead of a DVD, or by changing the method used by libdvdccss to decrypt DVDs (go to Preferences->All->Input/Codecs->Access Modules->DVD without menus->Method used by libdvdcss for decryption). If you play a lot of DVDs from different regions your best option is to buy a USB or Firewire external drive that you can set to the region you require.

See also
^^^^^^^^

-  `WindowsFAQ <WindowsFAQ>`__ - FAQ for Windows users.

**Notice: although we post FAQ-lists here, you shouldn't add comments or new questions to the wiki directly. Write them in the**\ `web-forum <http://forum.videolan.org>`__\ **please.**

`Category:FAQ <Category:FAQ>`__ `Category:macOS <Category:macOS>`__
