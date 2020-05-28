.. raw:: mediawiki

   {{Mux|id=vplayer|mod=subtitle}}

**VPlayer** is a format for containing `subtitle <subtitle>`__ information. It may have a .txt `file extension <file_extension>`__.

Specification
-------------

The VPlayer format is one of the following:

::

   Frame Type Structure:

   {1000}{2000}This is a subtitle.|This is a second subtitle.
   {3000}{4000}This is a third subtitle.|This is a fourth subtitle.
   {5000}{6000}This is a fifth subtitle.|This is a sixth subtitle.

   Time Duration Structure 1:

   01:00:10:This is a subtitle.
   02:00:20:This is a second subtitle.
   03:00:30:This is a third subtitle.
   04:00:40:This is a fourth subtitle.

   Time Duration Structure 2:
   :Leading zeros may be omitted.

`Category:Subtitles <Category:Subtitles>`__
