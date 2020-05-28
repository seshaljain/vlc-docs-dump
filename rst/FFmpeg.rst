.. raw:: mediawiki

   {{website|FFmpeg|https://ffmpeg.org/}}

.. raw:: mediawiki

   {{open}}

**FFmpeg** is an `open source <open_source>`__ library for encoding and decoding different types of media files, generally `MPEG <MPEG>`__ and MPEG-based files.

FFmpeg supports lots of `codecs <codec>`__: the main ones are included on the codecs page. If you want the full list, (including different spellings for the same codec), the `source code <source_code>`__ lists them all (there's way too many to list them all here ;-). In look under *Codec fourcc -> ffmpeg_id mapping* (that bit changes the codecs you type in to vlc to ffmpeg's internal codec names).

Avcodec
-------

.. raw:: mediawiki

   {{See|Documentation:Modules/avcodec}}

Avformat
--------

.. raw:: mediawiki

   {{See also|Documentation:Modules/avformat}}

The libavformat `module <module>`__ is a `mux <mux>`__ and a `demux <demux>`__ module for , based on the libavformat library.

It can decode and encode most of the containers supported in VLC, but is not usually the default one, except for a few ones, listed under.

.. raw:: mediawiki

   {{mux|id=gxf|mod=avformat|encoder=y}}

.. raw:: mediawiki

   {{mux|id=mxf|mod=avformat|encoder=n}}

.. raw:: mediawiki

   {{mux|id=flv|mod=avformat|encoder=y}}

.. raw:: mediawiki

   {{mux|id=nut|mod=avformat|encoder=y}}

.. raw:: mediawiki

   {{mux|id=webm|mod=avformat|encoder=y}}

.. raw:: mediawiki

   {{mux|id=rm|mod=avformat|encoder=n}}

Source code
-----------

.. raw:: mediawiki

   {{file|modules/codec/avcodec/fourcc.c|codec}}

.. raw:: mediawiki

   {{stub}}

`Category:Libraries <Category:Libraries>`__ `Category:Third parties <Category:Third_parties>`__
