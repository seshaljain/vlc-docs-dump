.. raw:: mediawiki

   {{wikipedia|MPEG-4}}

.. raw:: mediawiki

   {{mmwiki|ISO MPEG-4}}

**MPEG-4** is a form of `MPEG <MPEG>`__ encoding. It is a flexible audio and video compression format. The format describes audio and video `compression <compression>`__, with a container format for streaming across networks and saving to disk. It also contains optional extra features, including `DRM <DRM>`__ and `subtitles <subtitles>`__. These extra features are only included in software if needed. MPEG-4 can provide better quality than MPEG-2 at low `bitrates <bitrate>`__.

Here is an example of how to transcode an AVI into an MPEG-4 video from the `command prompt <command_prompt>`__

``{{%}} vlc ``\ *``file.avi``*\ `` --``\ ```sout`` <sout>`__\ ``='#``\ ```transcode`` <transcode>`__\ ``{vcodec=mp4v,acodec=mp4a}:std{access=file,mux=mp4,dst=``\ *``file.m4v``*\ ``}'``

MPEG-4 audio is an advanced, complicated audio format. It includes `AAC <AAC>`__ for high bitrates, multilingual tracks, text-to-speech modes for very low bitrates, the ability to synthesize instrumental sounds (similar to `MIDI <MIDI>`__), and more.

Codecs
------

.. raw:: mediawiki

   {{codec audio|id=mp4a|altid=m4a|mod=avcodec|for=MPEG-4}}

.. raw:: mediawiki

   {{codec video|id=mp4v|altid=m4v|mod=avcodec|for=MPEG-4}}

MPEG-4 specifies a range of codecs

The `fourccs <fourcc>`__ of MPEG-4 codecs are:

-  DivX Codecs

   -  DIV1, div1, DIVX, divx, DX50, dx50, XVID, XviD, xvid

-  `FFMPEG <FFMPEG>`__ MPEG-4

   -  FMP4, fmp4

-  3IV2, 3iv2
-  BLZ0
-  DXGM
-  HDX4, hdx4
-  M4S2, m4s2
-  MP4S, mp4s
-  MP4V, mp4v
-  RMP4
-  SEDG
-  SMP4
-  UMP4
-  WV1F
-  XVIX

Container
---------

MP4 (**.mp4**) is the global file extension for the official container format defined in the MPEG-4 standard (ISO 14496-14).

-  **.mp4**: the only official extension; used for both audio and video files (and advanced content)
-  **.3gp**: this extension is used for the 3gp format, derived from the ISO standard
-  **.m4a**: introduced by Apple for aac/alac *audio-only* files.

NOTE: .m4a files can safely be renamed to .mp4—but the distinction between audio (m4a) and video (mp4) may be useful if you are going to share files, or if you tend to forget what files you have.

For complete details on MP4, see the following link:

-  http://forum.doom9.org/showthread.php?s=&threadid=62723

 .mp4 audio
~~~~~~~~~~

**.m4a** is the `file extension <file_extension>`__ attached to names of files containing `MPEG-4 <MPEG-4>`__ Audio. Generally, MPEG-4 files are have the **.mp4** file extension.

The .m4a file extension has been popularized by Apple, which started using the .m4a file extension in their `iTunes <iTunes>`__ software and `iPod <iPod>`__ music players to distinguish between MPEG-4 Video and Audio files. Currently, most software that supports MPEG-4 Audio also supports the .m4a extension. The most common type of .m4a files available are those using the AAC (`Advanced Audio Coding <Advanced_Audio_Coding>`__) audio format, but other formats such as `Apple Lossless <Apple_Lossless>`__ and even `mp3 <mp3>`__ files may be put inside a .m4a container file. You can normally safely rename the file extension of an .mp4 file containing only audio to .m4a or vice versa to get the file to properly play in your favorite audio player.

Protected MPEG-4 Audio
^^^^^^^^^^^^^^^^^^^^^^

When these files have `digital restrictions management <digital_restrictions_management>`__ (DRM) applied to them, their extension are often changed to **.m4p**, the *p* standing for *protected*. Music files purchased from the iTunes Music Store, for example, have this extension.

Audiobooks
^^^^^^^^^^

When they contain audiobook data, MPEG-4 files have a **.m4b** extension.

.. _container-1:

Container
---------

.. raw:: mediawiki

   {{mux|id=mp4|encoder=y|altid=mov|altid2=3gp}}

Accepted video codecs
~~~~~~~~~~~~~~~~~~~~~

-  **mp4v**, including all the codecs described above
-  `mpgv <mpgv>`__
-  `MJPG <MJPG>`__
-  `mjpb <mjpb>`__
-  `SVQ1 <SVQ1>`__
-  `SVQ3 <SVQ3>`__
-  `H263 <H263>`__
-  `h264 <h264>`__

Accepted audio codecs
~~~~~~~~~~~~~~~~~~~~~

-  `mp4a <mp4a>`__ (is `aac <AAC>`__)
-  `mpga <mpga>`__
-  `samr <samr>`__
-  `sawb <sawb>`__

Accepted subtitle codec
~~~~~~~~~~~~~~~~~~~~~~~

-  `subt <subt>`__

Decoding libraries
------------------

In addition to `FFmpeg <FFmpeg>`__, there is `MPEG4IP <MPEG4IP>`__ that can decode MPEG-4 streams.

Source code
-----------

.. raw:: mediawiki

   {{file|modules/mux/mp4/mp4.c|output muxer}}

.. raw:: mediawiki

   {{file|modules/demux/mp4/mp4.c|input demuxer}}

Further reading
---------------

-  `MPEG-4 Audio FAQ (2000 publication) <https://sound.media.mit.edu/resources/mpeg4/audio/faq/mpeg4.html>`__
-  `MPEG-4 ISO/IEC standard (1999 publication) <https://sound.media.mit.edu/resources/mpeg4/audio/general/w3156.pdf>`__
