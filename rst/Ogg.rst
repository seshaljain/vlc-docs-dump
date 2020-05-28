.. raw:: mediawiki

   {{mux|id=ogg|encoder=y}}

.. raw:: mediawiki

   {{wikipedia|Ogg}}

.. raw:: mediawiki

   {{open}}

| Being a `Container <Container>`__ format, ogg can embed third-party codecs (such as `DivX <DivX>`__, `XviD <XviD>`__, `MP3 <MP3>`__ and others) but usually Ogg is used with `Vorbis <Vorbis>`__, `Theora <Theora>`__, `FLAC <FLAC>`__ and `Dirac <Dirac>`__.

Accepted codecs
---------------

Below are the compatible codecs for OGG.

Accepted audio codecs
~~~~~~~~~~~~~~~~~~~~~

-  `vorb <vorb>`__: Vorbis handles general audio data at mid- to high-level bitrates (~16-256 kbit/s/channel)
-  `flac <flac>`__: Free lossless audio codec. Has same sound quality as `wave <wave>`__, but only cca half the size.
-  `spx <spx>`__: Speex handles voice data at low bitrates (~8-32 kbit/s/channel)

Accepted video codecs
~~~~~~~~~~~~~~~~~~~~~

-  `theo <theo>`__: Theora based upon On2's `VP3 <VP3>`__, it is targeted at competing with MPEG-4 video (i.e. `DivX <DivX>`__ and `XviD <XviD>`__), `RealVideo <RealVideo>`__, or `Windows Media Video <WMV>`__.
-  `drac <drac>`__
-  `tark <tark>`__ (decoding only): Tarkin, an experimental codec utilizing 3D wavelet transforms. It has been put on hold, with Theora becoming the main focus for video encoding.

-  `mpgv <mpgv>`__: MPEG
-  `mp4v <mp4v>`__: MPEG-4
-  `div3 <div3>`__: DIVX 3
-  `mjpg <mjpg>`__: MPJPEG video
-  `wmv1 <wmv1>`__, `wmv2 <wmv2>`__, `wmv3 <wmv3>`__: Windows media
-  `snow <snow>`__
-  `ms <ms>`__ (decoding only):
-  `xvid <xvid>`__ (decoding only):

Meta codecs
~~~~~~~~~~~

-  `cmml <cmml>`__ (decoding only): Text information

Source code
-----------

.. raw:: mediawiki

   {{file|modules/mux/ogg.c|output muxer}}

.. raw:: mediawiki

   {{file|modules/demux/ogg.c|input demuxer}}

References
----------

Some of this page is taken from the Wikipedia article on this subject.
