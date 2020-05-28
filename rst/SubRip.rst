.. raw:: mediawiki

   {{Mux|id=subrip|mod=subtitle}}

.. raw:: mediawiki

   {{Wikipedia|SubRip}}

**SubRip** is the native subtitle format of the `SubRip program <http://zuggy.wz.cz/>`__, developed by a friend of the creator of `SubViewer <SubViewer>`__. It is one of the most used formats for `subtitles <subtitles>`__.

It may have the `file extension <file_extension>`__ ``.srt``. It can be embedded in `mkv <Matroska>`__ files.

Specification
-------------

Format
~~~~~~

Each frame of a subtitle is formatted as follows:

| \ ``n``\ 
| ``h1:m1:s1,d1 --> h2:m2:s2,d2``
| ``Line 1``
| ``Line 2``
| ``…``

Note the last line is a blank line between subtitle frames, and the decimal separator is a comma (per French-style).

n
   sequential number. This may also appear on the same line as start/stop times
h1:m1:s1,d1
   start time of this frame, in hours minutes and seconds to three decimal places
h2:m2:s2,d2
   stop time

Example
^^^^^^^

A 2-frame subtitle:

| ``1``
| ``00:00:20,000 --> 00:00:24,400``
| ``a bla bla ble a bla bla ble``
| ``a bla bla ble``
| ``2``
| ``00:00:24,600 --> 00:00:27,800``
| ``a bla bla ble…``

Extensions
~~~~~~~~~~

Some subtitles feature html tags inside the SubRip text:

-  

   .. raw:: mediawiki

      {{Tag pair|b}}

   : bold

-  

   .. raw:: mediawiki

      {{Tag pair|s}}

   : strikethrough

-  

   .. raw:: mediawiki

      {{Tag pair|u}}

   : underline

-  

   .. raw:: mediawiki

      {{Tag pair|i}}

   : italic

-  ``<font color=… face=…>``: font attributes

See also
--------

-  `SongSubtitles.org <SongSubtitles.org>`__ (now defunct)

`Category:Subtitles <Category:Subtitles>`__
