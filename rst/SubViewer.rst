\__NOTOC_\_ **SubViewer** is a file format for storing `subtitles <subtitles>`__. A friend of the SubViewer creator developed `SubRip <SubRip>`__ to extract subtitles from DVDs, so the formats are similar. Like SubRip, blank lines separate frames. It may have the `file extension <file_extension>`__ ``.sub``.

Specification
-------------

SubViewer 1
~~~~~~~~~~~

A sample SubViewer document may look like;

::

   [INFORMATION] <-- beginning of optional info section, closing tag required
   [TITLE] Title of film.
   [AUTHOR] Author of film.
   [SOURCE] Arbitrary text
   [FILEPATH] Arbitrary text
   [DELAY]    (time in frames to delay all subtitles
   [COMMENT]  Arbitrary text
   [END INFORMATION]
   [SUBTITLE]   <-- beginning of subtitle section, no closing tag required.
   [COLF]&HFFFFFF,[SIZE]12,[FONT]Times New Roman
   00:01:00.10,00:02:00.20
   Oh, no.
   The eggs are hatching!

   00:02:00.30,00:03:00.40
   No, never mind, I was hallucinating.

SubViewer 2
~~~~~~~~~~~

In SubViewer 2.0 format, the whole subtitle is written on one line, with line breaks indicated by ``[br]``, as follows:

::

   00:01:00.10,00:02:00.20
   Oh, no.[br]The eggs are hatching!

References
----------

`Divxstation <http://divxstation.com/article.asp?aId=27>`__ article by Stachken

`Category:Subtitles <Category:Subtitles>`__
