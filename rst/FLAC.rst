.. raw:: mediawiki

   {{website|FLAC|https://xiph.org/flac/}}

.. raw:: mediawiki

   {{xiph|FLAC}}

.. raw:: mediawiki

   {{open}}

**FLAC** is short for **Free Lossless Audio Compression**. It is an open source `codec <codec>`__ and `file format <file_format>`__ which provides a `perfect <lossless>`__ quality audio file. FLAC files usually contain `CD quality <CD>`__ audio, but can also support almost any audio data with a wide range of sample frequencies, amount of channels and bits per sample.

FLAC provides a smaller size of file than `PCM <PCM>`__ `WAV <WAV>`__ (about half the size), but much larger than `lossy <lossy>`__ codecs like `MP3 <MP3>`__. MP3s are about 5-10% the size of WAV files, but are lower quality.

A CD's worth of data is...

-  700MB as a CD
-  700MB as WAV
-  **300MB as FLAC**
-  40MB as MP3 (128 `kbps <kbps>`__)

Container format
----------------

.. raw:: mediawiki

   {{mux|id=flac|encoder=y}}

FLAC can be used inside several `container formats <container_format>`__, such as `ogg <ogg>`__ and `matroska <matroska>`__, but can also be stored in its own container.

.. raw:: mediawiki

   {{VLC}}

can encode FLAC starting with 0.7.0.

Source code
-----------

.. raw:: mediawiki

   {{file|modules/demux/flac.c|input demuxer}}

`Category:Audio codecs <Category:Audio_codecs>`__
