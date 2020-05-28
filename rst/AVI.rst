.. raw:: mediawiki

   {{mux|id=avi|encoder=y}}

.. raw:: mediawiki

   {{wikipedia|Audio Video Interleave}}

**AVI (Audio Video Interleave)** is a popular `container <container>`__ format used to hold video and audio data.

To play an AVI file, the audio and video files need to be encoded with `codecs <codec>`__ the player understands.

AVI files aren't designed to hold `subtitles <subtitles>`__. Also, they don't support some features which more recent container formats support.

AVIs are based on `RIFFs <RIFF>`__.

NOTE
   The VLC AVI `muxer <muxer>`__ (encoder) was severly broken in many versions. Please use the latest version, .

Module options
--------------

When playing AVI files, you can use the following options

-  --avi-interleaved (`boolean <boolean>`__)

      Force interleaved method. Default off (false).

-  --avi-index (`integer <integer>`__)

      Recreate a index for the AVI file. Use this if your AVI file is damaged or incomplete (not seekable). Values are

      -  0: Ask for action (default)
      -  1: Always fix
      -  2: Never fix
      -  3: Fix when necessary

Specification
-------------

-  http://msdn2.microsoft.com/en-us/library/ms779636.aspx

Source code
-----------

.. raw:: mediawiki

   {{file|modules/mux/avi.c|output muxer}}

.. raw:: mediawiki

   {{file|modules/demux/avi/avi.c|input demuxer}}
