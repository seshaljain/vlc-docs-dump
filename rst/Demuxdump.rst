.. raw:: mediawiki

   {{mux|id=dump|encoder=n}}

A special codec used mainly for debugging. This saves the input as a file (specified by *demuxdump-file*), without decoding it.

This is a way to "decode" input to VLC. To output data without a `container <container>`__, use `dummy <dummy>`__.

For example, saving the raw input of an `mp3 <mp3>`__ `shoutcast <shoutcast>`__ stream can be done with:

``{{%}} vlc http://example.org/shoutcast.mp3 :demux=dump :demuxdump-file=output.mp3``

Module options
--------------

-  demuxdump-file (file name)

      File to output data, default: "stream-demux.dump"

-  demuxdump-append (`boolean <boolean>`__)

      Append data to file. Set as true to append data, or false (default) to overwrite the file with the new data.

Source code
-----------

.. raw:: mediawiki

   {{file|modules/demux/demuxdump.c|input demuxer}}
