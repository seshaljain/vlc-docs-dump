This page is intended to explain what are the cool features of **VLC media player 0.9**, `codename <codename>`__ **Grishenko**.

Think about it as a "**Important features (AKA: the cool stuff)**" kernelnewbies-like page, so you don't have to read the complete changelog.

Very short summary
------------------

One liner
~~~~~~~~~

The 0.9 version of adds a new interface module for Linux, Unix and Windows, a media library and an improved playlist, many new inputs and codecs support and many new audio and video filters.

A bit more
~~~~~~~~~~

For video playback, new protocols, new codecs, new demuxers and many bug-fixes have been added to support more formats.

For audio playback, cover art and metadata support (and editing) have been vastly enhanced. It can play audio when the playback speed is changed.

| For the developers, libVLC has been simplified and improved, many bindings for many languages were added and there is a new Mac OS X Framework.
| Scripts written in lua can expand VLC media player's capabilities (read Youtube, Dailymotion URLs, fetch meta-data...)

If you are a *journalist*, *press* related or a *blogger*, please look `here <What_is_cool_in_0.9#Press>`__. If you distribute VLC on your website, please do the same. In both case, please state that we `need help <Help_us>`__.

If this page is not detailed enough for you, please read `Next_changes <Next_changes>`__. If you want the complete *Changelog*, see `Git <http://git.videolan.org/?p=vlc.git;a=log;h=0.9-bugfix>`__.

.. raw:: html

   <html>

.. raw:: html

   <embed src="http://vimeo.com/moogaloop.swf?clip_id=1732418&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=&amp;fullscreen=1" type="application/x-shockwave-flash" allowfullscreen="true" allowscriptaccess="always" width="400" height="302">

.. raw:: html

   </embed>

.. raw:: html

   </html>

You can also get `better quality <http://www.videolan.org/videos/>`__, `Youtube <http://www.youtube.com/watch?v=zVhk7Kq1rEU>`__ or `dailymotion <http://www.dailymotion.com/dionoea/video/11351932>`__ versions of this video.

Summary
-------

Interface
~~~~~~~~~

A new interface module based on the Qt toolkit has been added to VLC. If you are a **GNOME** or **Xfce** user, **before trolling**, please read `this <Qt_and_GTK>`__.

This new interface module has a few improvements on the old one:

-  Simplified settings and dialogs
-  Media library integration
-  Album art displaying and metadata editing
-  Live activation of Video and audio filters
-  Basic encoding profiles
-  Multiple start modes (classic, enhanced and minimalist)
-  System tray icon and minimizing
-  Fullscreen controller

And many other improvements and bug-fixes.

Moreover, some global hotkeys plugin can be found on the forum.

Playlist
~~~~~~~~

The playlist has been improved in many ways, in addition to the new Media Library *(very simple so far, but will be extended in the future)*:

-  Live Searching in the playlist,
-  Youtube, Dailymotion, Google Video and similar services URL can be scripted in VLC to play directly those URLs,
-  last.fm submission support,
-  Album art support,
-  Better metadata tagging reading and writing support for audio files.

Playback
~~~~~~~~

A lot of new decoders, demuxers, and protocols have been added.

There are new codecs support, like Flash video variants, camcorder codecs (M2TS ones), Dirac, Atrac3, H.264 PAFF, APE audio, RealVideo, VC-3, Fraps and others, but also better decoding and better performance. Many thanks to the `FFmpeg project <http://ffmpeg.org>`__ which can take most of the credit for these improvements.

There are improvements in the demuxers and new supports (subtitles format rework with many new formats, Tivo2, OMA, MIDI support...).

Tag supports of audio files have vastly been improved(fix of APE, AAC, OGG tags,...)

This version also supports DVB windows devices (BDA), iSight Webcams, v4l2 on Linux and many other ones.

Filters
~~~~~~~

Many new audio and video filters have been added:

-  New video filters like puzzle game, color extracting, sharpen, logo erasing, blue-screen and more have been added.
-  New audio filters have introduced Replay Gain support, Faster/Slower audio playback with pitch correction and a spatializer.

Most video filters can now be streamed.

Developers
~~~~~~~~~~

-  libVLC has been rewritten and split and supports externally built plugins
-  VLCKit, a Mac OS X Framework, enables external developers to develop applications around VLC.
-  New bindings can be found on the wiki and the forums

Misc
~~~~

A new update system, more secured, was developed for this release.

New localizations in Finnish, Persian, Polish, Punjabi, Bulgarian have joined the old ones.

Long summary and details
------------------------

If this page is not detailed enough for you, please read `Next_changes <Next_changes>`__. If you want the complete *Changelog*, see `Git <http://git.videolan.org/?p=vlc.git;a=log;h=0.9-bugfix>`__.

You can also have the mailing list information on http://mailman.videolan.org

Press
-----

If you are press related, can you please note a few things:

-  The software name is "VLC media player", not "VLC Media Player", not "VideoLAN", not "VideoLan Client" nor any other variation.
-  The team behind videolan.org is "VideoLAN", not "Videolan", not "VLC folks", nor "vlc".

Please be nice to state that we need help to develop the software, and link to the `Help us <Help_us>`__ page.

`Category:Changelog <Category:Changelog>`__
