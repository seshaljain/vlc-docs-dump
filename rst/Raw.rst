.. raw:: mediawiki

   {{codec audio|id=raw|mod=araw}}

.. raw:: mediawiki

   {{wikipedia|PCM}}

.. raw:: mediawiki

   {{mmwiki|PCM}}

VLC's **raw** codec decodes raw audio data in the PCM format.

**Pulse-code modulation** or **PCM** is the simplest way of storing audio data. At regular time intervals the audio is sampled, and the amplitude is stored.

PCM is the basis for `WAVE <WAVE>`__ audio files.

Fourcc
------

The following `fourccs <fourcc>`__ are used for this codec:

.. raw:: html

   <div class="col3">

-  araw
-  "pcm "
-  aflt
-  twos
-  sowt
-  alaw
-  ulaw
-  fl64
-  fl32
-  s32l
-  s32b
-  s24l
-  s24b
-  s16l
-  s16b
-  "s8 "
-  "u8 "
-  in24
-  in32

.. raw:: html

   </div>

See also
--------

-  `dummy <dummy>`__
-  `US Library of Congress Linear Pulse Code Modulated Audio (LPCM) <http://www.digitalpreservation.gov/formats/fdd/fdd000011.shtml>`__ - Potentially useful documentation on LPCM and PCM by digital preservationists
-  `ADPCM <ADPCM>`__

Source code
-----------

.. raw:: mediawiki

   {{file|modules/codec/araw.c|audio codec}}
