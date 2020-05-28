.. raw:: mediawiki

   {{mux|id=gme|encoder=n}}

.. raw:: mediawiki

   {{Website|Game Music Emu|on=Bitbucket|https://bitbucket.org/mpyne/game-music-emu/wiki/Home}}

.. raw:: mediawiki

   {{Open}}

**Game Music Emu** (GME) format is used to emulate the audio output of various video game consoles popular in the 1980s and 1990s. It gives a "retro" feel to the sound. *Game Music Emu* is a contraction of *Game Music Emulator*.

The .??z formats are just `compressed <compress>`__ with inflate.

========= ====== =================================
extension format platform
========= ====== =================================
.nsf      NSF    Nes
.nsfe     NSF    Nes
.gbs      GBS    Gameboy
.vgm      VGM    Master System, Game Gear, Genesis
.vgz      VGM    Master System, Game Gear, Genesis
.spc      SPC    Super Nes (SNES)
.gym      GYM    Genesis"
========= ====== =================================

Links
-----

-  `Blargg's Audio Libraries - Game_Music_Emu <http://blargg.8bitalley.com/libs/audio.html#Game_Music_Emu>`__: Original developer's page (old)
-  `Bitbucket - game-music-emu <https://bitbucket.org/mpyne/game-music-emu/wiki/Home>`__ (`repo link <https://bitbucket.org/mpyne/game-music-emu/src>`__): Official fork used by VLC (current)

Source code
-----------

.. raw:: mediawiki

   {{file|modules/demux/gme.c|input demuxer}}
