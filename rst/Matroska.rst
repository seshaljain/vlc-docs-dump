English help
------------

.. raw:: mediawiki

   {{mux|id=mkv|encoder=n|altid=mka}}

.. raw:: mediawiki

   {{website|Matroska|http://www.matroska.org/}}

.. raw:: mediawiki

   {{open}}

**Matroska** is a `container <container>`__ format for storing or streaming video and audio files. The Matroska format has many features, such as a DVD-style menu system.

File-extensions: .mkv .mka .mks

Module options
~~~~~~~~~~~~~~

   *See*\ `Documentation:Modules/mkv <Documentation:Modules/mkv>`__

Compatibility
~~~~~~~~~~~~~

VideoLAN can only read matroska files. Also, some of the video `codecs <codecs>`__ that can be used inside this type of file are not supported by VLC. Most notably, this includes the `RealVideo <RealVideo>`__ 9 and 10 formats.

Accepted codecs
~~~~~~~~~~~~~~~

Below are the codecs supported by VLC. Unsupported codecs include `WavPack <WavPack>`__.

Video codecs
^^^^^^^^^^^^

-  `mpgv <mpgv>`__: MPEG video
-  `mp4v <mp4v>`__: MPEG-4 video
-  `div3 <div3>`__: DivX
-  `avc1 <avc1>`__

Audio codecs
^^^^^^^^^^^^

-  `mpga <mpga>`__: MPEG audio (MP1, MP2, MP3)
-  `mp4a <mp4a>`__: MPEG-4 audio (`AAC <AAC>`__)
-  `a52 <a52>`__: A/52
-  `dts <dts>`__: DTS
-  `flac <flac>`__: Free lossless audio codec (`lossless <lossless>`__ audio)
-  `vorb <vorb>`__: Vorbis
-  `twos <twos>`__, `araw <araw>`__: uncompressed audio
-  `tta <tta>`__: True Audio

Subtitle codecs
^^^^^^^^^^^^^^^

-  `subt <subt>`__
-  `ssa <ssa>`__
-  `spu <spu>`__

Aide en Français
----------------

Site officiel: http://www.matroska.org/index.html.fr

Un article framasoft: http://www.framasoft.net/article2113.html

Source code
-----------

.. raw:: mediawiki

   {{file|modules/demux/mkv/mkv.cpp|input demuxer}}
