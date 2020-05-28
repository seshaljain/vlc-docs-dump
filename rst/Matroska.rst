== English help == {{muxencoder=nMatroska\|http://www.matroska.org/}}
{{open}} '''Matroska''' is a [[container]] format for storing or
streaming video and audio files. The Matroska format has many features,
such as a DVD-style menu system.

File-extensions: .mkv .mka .mks

=== Module options === :''See [[Documentation:Modules/mkv]]''

===Compatibility=== VideoLAN can only read matroska files. Also, some of
the video [[codecs]] that can be used inside this type of file are not
supported by VLC. Most notably, this includes the [[RealVideo]] 9 and 10
formats.

=== Accepted codecs === Below are the codecs supported by VLC.
Unsupported codecs include [[WavPack]].

==== Video codecs ==== \* [[mpgv]]: MPEG video \* [[mp4v]]: MPEG-4 video
\* [[div3]]: DivX \* [[avc1]] ==== Audio codecs ==== \* [[mpga]]: MPEG
audio (MP1, MP2, MP3) \* [[mp4a]]: MPEG-4 audio ([[AAC]]) \* [[a52]]:
A/52 \* [[dts]]: DTS \* [[flac]]: Free lossless audio codec
([[lossless]] audio) \* [[vorb]]: Vorbis \* [[twos]], [[araw]]:
uncompressed audio \* [[tta]]: True Audio ==== Subtitle codecs ==== \*
[[subt]] \* [[ssa]] \* [[spu]]

==Aide en Français==

Site officiel: [http://www.matroska.org/index.html.fr
http://www.matroska.org/index.html.fr]

Un article framasoft: [http://www.framasoft.net/article2113.html
http://www.framasoft.net/article2113.html]

== Source code == {{fileinput demuxer}}
