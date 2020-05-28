{{wikipedia|XMMS}} '''XMMS''' is an open source media player similar to
[[Winamp]]. It supports most common audio formats, and also plays some
videos.

==Compatibility==

XMMS has good audio compatibility, and can play a range of video
formats. XMMS does have some problems when receiving [[stream]]ed
content.

When streaming [[Ogg]]/[[vorbis]] to XMMS via [[HTTP]] the [[MRL]] needs to end in ".ogg". This could be done by providing a filename with the [[sout]] line, something like this:
   {{%}} vlc --sout http/ogg:127.0.0.1:8080/my_audio.ogg

As a temporary hack you could append "?.ogg" to the MRL you give XMMS.

XMMS supports [[ES]], [[PS]] and [[MPEG-1]] muxers with [[mpga]] audio
out of the box. The [[TS]] muxer gives strange audio in XMMS.

[[Category:Player]]
