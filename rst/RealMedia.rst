{{muxaltid=rmRealMedia}}

'''RealMedia''' is a type of file designed by RealNetworks, and can be
played with the proprietary [[RealPlayer]]. RealPlayer is available for
[[Windows]], [[macOS]] and [[Linux]]. Additionally, [[Helix Player]] may
be able to play some files, but it lacks the proprietary codecs in some
realmedia files.

RealMedia files are normally streamed over [[RTSP]] connections.

RealAlternative installs, and allows RealMedia files to be played in
[[Media Player Classic]].

==Accepted codecs== \* [[rv]]: RealVideo \* [[ra]]: [[MPEG-4]] audio \*
[[a52]], [[dnet]]: A/52 audio \* [[cook]]: Cook audio codec \* [[28_8]]:
28.8 audio codec \* [[sipr]], RealAudio 4/5 (name is from Sipro Lab
Telecom ACELP-NET)

==Compatibility== Currently, [[VLC media player]] should be able to play
most audio and video of .rm, .rmvb files.

Sipr is supported through [[libavcodec]] (Search for sipr in either of
these files:
[https://git.videolan.org/?p=ffmpeg.git;a=blob;f=Changelog;hb=HEAD][https://git.videolan.org/?p=vlc.git;a=blob;f=modules/codec/avcodec/fourcc.c].
It is not mentioned in {{VLCSourceFile|NEWS}})

== Source code == {{Filefrom [[libavcodec]]}}
