.. raw:: mediawiki

   {{wikipedia|Compact disc}}

A **CD** or **Compact Disc** is a circular disk with a silver look to it. |A CD|

Audio CDs
---------

.. raw:: mediawiki

   {{protocol|CDDA|info=Usage: cdda://device@track}}

**Audio CDs** contain audio data, and can be read by a CD player. Any CD marked with the CDDA mark can be played in any player also marked with a CDDA mark.

Audio CDs can be played with `VLC media player <VLC_media_player>`__ if you have a CD drive on your PC. After inserting the CD, run VLC and select *Open Disc* from the *File* menu. Then click on the *Audio CD* option and press OK. If you prefer, you can use the `command prompt <command_prompt>`__ to run an audio CD:

| ``vlc cdda://D:``
| ``vlc cdda:///dev/cdrom``

Where ``D:`` (windows) or ``/dev/cdrom`` (Linux) is the location of your CD drive. To play a single track, append @ followed by the track number. For example, to play track 3, type

``vlc cdda://D:@3``

Audio CDs contain `uncompressed <uncompress>`__ `lossless <lossless>`__ audio, which takes up a lot of space on the disk but is *very* good quality. The format for this is stereo audio (has both left and right audio channels) in 44100Hz 16-bit `PCM <PCM>`__ `WAV <WAV>`__ format.

Module options
~~~~~~~~~~~~~~

   *See*\ `Documentation:Modules/cdda <Documentation:Modules/cdda>`__

Data CDs
--------

**Data CDs** contain programs or files which can be read by your PC – you can only use these with your PC.

CDs can also contain other data and program code. When you insert a CD in some versions of `Windows <Windows>`__, programs on the CD may run without asking you first – you may wish to `turn off autorun <https://www.howtogeek.com/236241/how-to-enable-disable-and-customize-autoplay-in-windows-10/>`__ or hold the Shift key when inserting a CD to prevent this from happening.

Playing media files on a data CD
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can play files from a data CD, in exactly the same way as playing them from your hard drive (note: Linux users will need to `mount <wikipedia:Mount_(computing)>`__ the CD drive first).

See the `file <file>`__ access module for details of playing files from your computer.

CDs with both audio and data (Mixed CDs)
----------------------------------------

**Mixed CDs** contain both audio and data, for example a CD may come with a music video as a "bonus feature". The data part (such as the music video) can only be used on your PC, but the audio is able to be played on your PC or CD player.

Some mixed CDs come with programs which will try to install `copy protection <copy_protection>`__ on your computer – see `2005 Sony BMG CD copy protection scandal <wikipedia:2005_Sony_BMG_CD_copy_protection_scandal>`__.

To play the audio CD part, follow the `instructions for an audio CD <#Audio_CDs>`__. To play files on the data CD part, follow the `instructions for a data CD <#Data_CDs>`__.

See also
--------

-  `CD <CD>`__
-  `DVD <DVD>`__
-  `VCD <VCD>`__/SVCD

.. raw:: html

   <hr style="width:8em;" />

-  `FLAC <FLAC>`__
-  `wikipedia:ISO image <wikipedia:ISO_image>`__: an obscure format that can store e.g. an operating system on a disc

Source code
-----------

.. raw:: mediawiki

   {{file|modules/access/cdda.c|access module}}

`Category:Physical media <Category:Physical_media>`__

.. |A CD| image:: CD.png
   :width: 100px
