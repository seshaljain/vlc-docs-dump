.. raw:: mediawiki

   {{mux|id=wav|encoder=y}}

**WAVE** is a way of storing audio, which is normally `uncompressed <raw>`__. It is based on `RIFF <RIFF>`__. Note that wav isn't a streamable audio format, so you can only stream it using `RTP <RTP>`__ (to stream it otherwise, transcode it to something that's streamable).

Accepted audio codecs
---------------------

-  `dummy <dummy>`__: Uncompressed audio of various types, based on storing integer values of the amplitude of the sound (see `PCM <wikipedia:PCM>`__).
-  `fl32 <fl32>`__: Floating point 32-bit uncompressed audio, also based on PCM but allowing the values to be stored as floating point data types. This can give better quality audio when the sound becomes quiet.

Converting to WAVE
------------------

The command-line for `converting <convert>`__ any readable input file to a WAVE audio file is the following:

``{{%}} ``\ \ `` -I dummy -vv ``\ \ `` --sout=#transcode{acodec=``\ \ ``,channels=2,ab=``\ \ ``,samplerate=44100}:standard{access=file,mux=wav,dst=``\ \ ``} vlc://quit``

Where on Windows you need to add installation directory in front of (by default ).

As you can specify one of the above mentioned ones. The `bitrate <bitrate>`__ of the output file is specified by the parameter.

Source code
-----------

.. raw:: mediawiki

   {{file|modules/mux/wav.c|output muxer}}

.. raw:: mediawiki

   {{file|modules/demux/wav.c|input demuxer}}
