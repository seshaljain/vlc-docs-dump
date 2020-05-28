.. raw:: mediawiki

   {{wikipedia|MPEG}}

MPEG refers to a set of standards created by the `Moving Picture Experts Group <http://www.chiariglione.org/about>`__. MPEG refers to several video, audio and `container <container>`__ formats; see the full list at the `Codec <Codec>`__ page.

An MPEG file is a file using an MPEG container (these are called *mpeg1*, *ts*, *ps*, and *mp4* for MPEG-4).

Creating an MPEG File with VLC
------------------------------

To make an MPEG file, you need to:

-  Pick a container (see `below <#Container_formats>`__)
-  Transcode the audio and video to formats able to be held in the container: in general this is the MPEG video and audio formats only. Check the `compatibility information <https://www.videolan.org/streaming/features.html>`__ in the official documentation, but be warned that while VLC allows any codec and mux, most other players support only a few combinations!

 MPEG-1 and 2
------------

.. raw:: mediawiki

   {{see also|H.262/MPEG-2 Part 2}}

.. raw:: mediawiki

   {{wikipedia|MPEG-1|MPEG-2}}

-  Muxer: **ts**, **ps**, **mpeg1**

MPEG-1 is a video and audio compression format, used in `Video CDs <Video_CD>`__. It is compatible with a large number of software and hardware devices.

Here is an example of how to transcode an `AVI <AVI>`__ into a portable MPEG-1 video from the `command prompt <command_prompt>`__

``{{%}} vlc ``\ *``file.avi``*\ `` --sout='#transcode{vcodec=mp1v, acodec=mpga}:std{access=file, mux=mpeg1,url=``\ *``file.mpg``*\ ``}'``

MPEG-2 is used in digital television and `DVB <DVB>`__. It is also used as the format for `DVDs <DVD>`__. The biggest advantage of this format over MPEG-1 is in its support for interlaced pictures; MPEG-2 can cleanly `compress <compress>`__ `interlaced <interlaced>`__ video, while MPEG-1 internally only works on progressive-scan video, so interlacing must be faked.

Here is an example of how to transcode an AVI into an MPEG-2 video from the `command prompt <command_prompt>`__

``{{%}} vlc ``\ *``file.avi``*\ `` --sout='#transcode{vcodec=mp2v, acodec=mpga}:std{access=file, mux=ps,url=``\ *``file.mpg``*\ ``}'``

Transcoding and Streaming
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Bug|1965}}

| formerly required supplying a framerate of 25 in order to `transcode <transcode>`__ and stream an MPEG-1 or MPEG-2 payload.
| **This has been fixed since 2.0.0.**

*HINT:* Use an MPEG-TS (transport) stream container if you are streaming MPEG through the network (see `Container Formats <#Container_formats>`__).

Video
~~~~~

.. raw:: mediawiki

   {{codec video|id=mp1v}}

.. raw:: mediawiki

   {{codec video|id=mp2v|altid=mpgv}}

.. raw:: mediawiki

   {{codec video|id=mp4v}}

.. raw:: mediawiki

   {{codec video|id=h264}}

Codecs for MPEG-1 Video, MPEG-2 Video, MPEG-4 Video and H.264 Video (MPEG-4 AVC).

Audio
~~~~~

.. raw:: mediawiki

   {{codec audio|id=mpga|info=MP2 audio.}}

.. raw:: mediawiki

   {{codec audio|id=mp3|info=[[MP3]] audio.}}

.. raw:: mediawiki

   {{codec audio|id=mp4a|info=[[AAC]] audio.}}

Codecs for MPEG Layer 1/2 audio, MPEG Layer 3 audio and MPEG-4 AAC audio

Container formats
~~~~~~~~~~~~~~~~~

MPEG-2 specified 2 `container <container>`__ formats, ts and ps. Containers hold video and audio information in them, and package them up so it can be sent over a network or stored on disk.

-  **ts** (Transport Stream) should be used to store or send data where data loss will probably occur, such as over a network.
-  **ps** (Program Stream) should be used to store or send data where data loss is not likely, such as on a DVD.

Both ps and ts can transport MPEG-4 Video, but only ts can send MPEG-4 Audio. In addition, MPEG-4 specifies its own container format, **mp4** (see `MPEG-4 <MPEG-4>`__)

 TS, MPEG2 Transport Stream
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: mediawiki

   {{mux|id=ts|encoder=y}}

Module options
''''''''''''''

.. raw:: mediawiki

   {{Transcluded|Documentation:Modules/ts}}

.. raw:: mediawiki

   {{:Documentation:Modules/ts}}

Accepted video codecs
'''''''''''''''''''''

-  `mp1v <mp1v>`__: MPEG-1 video
-  `mpgv <mpgv>`__: MPEG-1 or MPEG-2 video
-  `mp4v <mp4v>`__: MPEG-4 video (ASP)
-  `h264 <h264>`__: H.264, MPEG-4 AVC
-  `drac <Dirac>`__: Dirac
-  `jpeg <jpeg>`__
-  `ms <ms>`__: MS codecs (nonstandard?)

Accepted audio codecs
'''''''''''''''''''''

-  `MP1 <MP1>`__, `MP2 <MP2>`__, `MP3 <MP3>`__
-  `mp4a <mp4a>`__: MPEG-4 Audio (MP4)
-  `a52 <a52>`__
-  `lpcm <lpcm>`__
-  `dts <dts>`__

Accepted subtitle codecs
''''''''''''''''''''''''

-  `spu <spu>`__
-  `subt <subt>`__
-  `telx <telx>`__

 PS, aka MPEG Program Stream
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: mediawiki

   {{mux|id=ps|encoder=y}}

.. _module-options-1:

Module options
''''''''''''''

.. raw:: mediawiki

   {{Transcluded|Documentation:Modules/ps}}

.. raw:: mediawiki

   {{:Documentation:Modules/ps}}

.. _accepted-video-codecs-1:

Accepted video codecs
'''''''''''''''''''''

-  `mpgv <mpgv>`__: MPEG-1 or MPEG2
-  `mp4v <mp4v>`__: MPEG-4

.. _accepted-audio-codecs-1:

Accepted audio codecs
'''''''''''''''''''''

-  `mpga <mpga>`__: MP1, MP2 or MP3
-  `mp4a <mp4a>`__: MPEG-4 (MP4)
-  `dts <dts>`__
-  `a52 <a52>`__
-  `lpcm <lpcm>`__

.. _accepted-subtitle-codecs-1:

Accepted subtitle codecs
''''''''''''''''''''''''

-  `spu <spu>`__
-  `ogt <ogt>`__
-  `cvd <cvd>`__

.. raw:: mediawiki

   {{clear}}

 MPEG-3
------

.. raw:: mediawiki

   {{wikipedia|MPEG-3}}

A largely unused audio and video compression format.

-  Note that the amazingly common `MP3 <MP3>`__ audio files are actually **MPEG-1 Layer 3** audio, not MPEG-3.

.. raw:: mediawiki

   {{clear}}

MPEG-4
------

.. raw:: mediawiki

   {{See|MPEG-4}}

Source code
-----------

.. raw:: mediawiki

   {{file|modules/mux/mp4/mp4.c|output muxer}}

.. raw:: mediawiki

   {{file|modules/demux/mpeg/ps.c|input demuxer}}

.. raw:: mediawiki

   {{file|modules/demux/mpeg/ts.c|input demuxer}}

.. raw:: mediawiki

   {{file|modules/demux/mpeg/ps.h|input demuxer}}

Further reading
---------------

-  `sound.media.mit.edu - The MPEG Audio Web Page <https://sound.media.mit.edu/resources/mpeg4/audio/>`__
