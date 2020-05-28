== Questions ==

== General talk ==

=== Cache and GUI interface === This project may need to redesign a bit
the cache handling module access. (How is this "Interface" related ? I
agree that we might need to change the caching algorithms for
web-content, but it's definitively not interface (nor web plugin)
related. [[User:Dionoea|Dionoea]] 16:17, 8 March 2007 (CET)) : Because
VLC caches in seconds and Youtube are just caching the most they can to
have the whole file local.

=== MKV muxer === From the VLC point of view i don't agree. It would be
easier to integrate the muxer directly into VLC than put it in
libavformat and then change the libavformat <-> VLC interface to use it.
I'm not sure how the chapter / menu / subs system works in MKV but it
sure will add complexitiy to or libavformat interface (and some lagg
time between the time the mkv muxer makes it into ffmpeg and the time we
make it work in VLC). -- [[User:Dionoea|Dionoea]] 16:25, 8 March 2007
(CET) :Note that the ffmpeg project already has this listed on their
[http://wiki.multimedia.cx/index.php?title=Summer_Of_Code_2007 SOC
page.]

=== DirectX improvements ===

HD1080 streams (for instance MPEG4-AVC) push the best current machines
at their limit. Usage of http://en.wikipedia.org/wiki/DXVA could help to
leverage any GPU capabilities and accelerate the rendering (delegation
of part of the process to the GPU depending on GPU capabilities & driver
implementation). Actually, hardware manufacturers such as ATI (h264
DxVA) or NVidia (PureVideo) have already provided such implementation
and some other players have already integrated DXVA.

=== Subtitles ===

is it possible to play two subtitles at once? or at least, can this be
optionally added when the new subtitle code comes in ? :)
--[[User:Compn|Compn]] 18:02, 19 April 2007 (CEST)
