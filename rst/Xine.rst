.. raw:: mediawiki

   {{website|Xine|http://www.xinehq.de}}

.. raw:: mediawiki

   {{open}}

**xine** is a `media player <media_player>`__ for Unix released under the GNU General Public License. It can play `CDs <CD>`__, `DVD-Video <DVD>`__, and `VCD <VCD>`__, as well as common computer multimedia formats like `AVI <AVI>`__, `WMV <WMV>`__, `MOV <MOV>`__, `MP3 <MP3>`__, `FLAC <FLAC>`__, `Theora <Theora>`__, `Speex <Speex>`__, and `Vorbis <Vorbis>`__.

xine is built as a `shared library <library>`__ (**xine-lib**) that supports different frontend player applications. To decode multimedia data xine uses libraries from the `FFmpeg <FFmpeg>`__ project or binary `codecs <codec>`__.

At present, xine has the most complete `SVCD <SVCD>`__ and `VCD <VCD>`__ support. (Anyone want to beef up support in vlc to make this not true?)

xine can handle VCD/SVCD menus, mouse hot spots, navigation (called PBC or playback control), and multiple audio channels. Many of these are missing or incomplete in vlc version 0.8.4. (Actually, pretty much all VCD/SVCD handling is broken in vlc version 0.8.4.) But one area where vlc may be a little ahead of xine is in SVCD and `CVD <CVD>`__ subtitle handling. SVCD and CVD subtitles in xine however require a `separate plugin <http://subhandler.sourceforge.net>`__ which is not part of xine whereas in vlc it is part of the main code base.

Compatibility
-------------

.. raw:: mediawiki

   {{compat}}

Web links
---------

-  `Home Page <http://xinehq.de/>`__
-  `Kaffeine <http://kaffeine.sourceforge.net/>`__ (xine-based frontend player)
-  `XinePlayer <http://xineplayer.berlios.de/>`__ (`macOS <macOS>`__ frontend)
-  `xine plugin for handling SVCD and CVD subtitles <http://subhandler.sourceforge.net/>`__

`Category:Player <Category:Player>`__
