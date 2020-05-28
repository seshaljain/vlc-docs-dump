.. raw:: mediawiki

   {{wikipedia|XMMS}}

**XMMS** is an open source media player similar to `Winamp <Winamp>`__. It supports most common audio formats, and also plays some videos.

Compatibility
-------------

XMMS has good audio compatibility, and can play a range of video formats. XMMS does have some problems when receiving `streamed <stream>`__ content.

When streaming `Ogg <Ogg>`__/`vorbis <vorbis>`__ to XMMS via `HTTP <HTTP>`__ the `MRL <MRL>`__ needs to end in ".ogg". This could be done by providing a filename with the `sout <sout>`__ line, something like this:

``{{%}} vlc --sout http/ogg:127.0.0.1:8080/my_audio.ogg``

As a temporary hack you could append "?.ogg" to the MRL you give XMMS.

XMMS supports `ES <ES>`__, `PS <PS>`__ and `MPEG-1 <MPEG-1>`__ muxers with `mpga <mpga>`__ audio out of the box. The `TS <TS>`__ muxer gives strange audio in XMMS.

`Category:Player <Category:Player>`__
