{{Back to|VLC Features}} This is a new page that lists the audio/video
codecs that VLC can or cannot read. It is still under development, don't
hesitate to add a some [[FourCC]] and infos.

It should now be a bit more complete than the official features page on
[https://www.videolan.org/vlc/features.html VideoLAN website].

If you have any question about those codecs, just consult our
[[Knowledge Base]] or our friends on the [http://wiki.multimedia.cx
Multimedia Wiki]. If you don't find information, search with Wikipedia
or Google.

== Video Codecs ==

=== Widely Used Video Codecs ===

{\| class="wikitable codec-table centered sortable" -! Name !! FOURCC !!
Playable !! Encoder !! library !! Comment \| mpeg, mp1v, mpg1, PIM1 \|\|
{{Yes}} \|\| {{Yes}} \|\| libmpeg2 , ffmpeg \|\| \| mp2v, mpg2, vcr2,
hdv1, hdv2, hdv3, mx*n, mx*p|\| {{Yes}} \|\| {{Yes}} \|\| libmpeg2 ,
ffmpeg \|\| \| \|\| {{Yes}} \|\| ffmpeg \|\| \| DIV1, DIV2, DIV3, mp41,
mp42, MPG4, MPG3 \|\| {{Yes}} \|\| {{Yes}} \|\| ffmpeg \|\| \| DIV4,
DIV5, DIV6, col1, col0, 3ivd \|\| {{Yes}} \|\| {{Yes}} \|\| ffmpeg \|\|
\| DIVX, Xvid, mp4s, m4s2, xvid, mp4v, fmp4, 3iv2, smp4, ... \|\|
{{Yes}} \|\| {{Yes}} \|\| ffmpeg \|\| \| h261 \|\| {{Yes}} \|\| {{Yes}}
\|\| ffmpeg \|\| \| h262 \|\| {{Yes}} \|\| {{Yes}} \|\| ffmpeg \|\| Same
as MPEG-2 Video \| h263 \|\| {{Yes}} \|\| {{Yes}} \|\| ffmpeg \|\| \|
h264, s264, AVC1, DAVC, H264, X264, VSSH \|\| {{Yes}} \|\| ffmpeg
(decode), x264 (encode) \|\| \| SVQ 1 \|\| {{Yes}} \|\| {{Yes}} \|\|
ffmpeg \|\| \| SVQ 3 \|\| {{Yes}} \|\| {{No}} \|\| ffmpeg \|\| \| \|\|
{{Yes}} \|\| ffmpeg \|\| \| cvid \|\| {{No}} \|\| internal, ffmpeg \|\|
\| thra \|\| {{Yes}} \|\| {{Yes}}, violated \|\| libtheora \|\| \| wmv1,
wmv2 \|\| {{Yes}} \|\| {{Yes}} \|\| ffmepg \|\| \| wmv3, wvc1, wmva \|\|
{{Yes}} \|\| {{No}} \|\| ffmpeg \|\| Not all profiles are supported. See
[[DMO]]. \| VP31, VP30, VP3 \|\| {{Yes}} \|\| {{No}} \|\| ffmpeg \|\| \|
VP50, VP5, VP51 \|\| {{Yes}} \|\| {{No}} \|\| ffmpeg \|\| \| VP60, VP61,
VP62, VP6F, VP6A \|\| {{Yes}} \|\| {{Yes}} \|\| ffmpeg \|\| \| VP7 \|\|
{{No}} \|\| {{No}} \|\| \|\| \| FSV1 \|\| {{Yes}} \|\| {{Yes}} \|\|
ffmpeg \|\| \| IV31, IV32 \|\| {{Yes}} \|\| {{no}} \|\| ffmpeg \|\| \|
{{Yes}} \|\| {{no}} \|\| libavcodec \|\| \| RV10, RV13, RV20 \|\|
{{Yes}} \|\| {{Yes}} \|\| ffmpeg \|\| \| RV30, RV40 \|\| {{No}} \|\|
{{No}} \|\| \|\| \| BBCD \|\| {{Yes}} \|\| {{Yes}} \|\| dirac \|\| \|
\|\| {{Yes}} \|\| {{Yes}} \|\| ffmpeg \|\| }

=== Rarer Video Codecs ===

{\| class="wikitable codec-table centered sortable" -! Rare codecs !!
FOURCC !! Decoder !! Encoder !! library !! Comment \| 'rle','smc
','rpza', 'qdrw' \|\| {{Yes}} \|\| {{No}} \|\| ffmpeg \|\| \| \|\|
{{No}} \|\| {{No}} \|\| \|\| Professional use, no open source decoders
\| \|\| ?? \|\| ?? \|\| \|\| \| \|\| ?? \|\| ?? \|\| \|\| \| \|\|
{{Yes}} \|\| {{Yes}} \|\| \|\| \| \|\| ?? \|\| ?? \|\| \|\| \| ASV1,
ASV2 \|\| {{Yes}} \|\| {{Yes}} \|\| ffmpeg \|\| \| \|\| {{Yes}} \|\|
{{no}} \|\| ffmpeg \|\| \| \|\| {{No}} \|\| {{No}} \|\| \|\| \| QPEG
\|\| {{Yes}} \|\| {{Untested}} \|\| ffmpeg \|\| \|}

== Audio Codecs ==

{\| class="wikitable codec-table centered sortable" -! Name !! FOURCC !!
Decoder !! Encoder !! library !! Comment \| mpga \|\| {{Yes}} \|\|
{{Yes}} \|\| libmad (decoding), twolame (encoding) \|\| ISO/IEC MPEG \|
mp3, .mp3, LAME \|\| {{Yes}} \|\| {{Yes}} \|\| libmad (decoding),
ffmpeg-mp3lame \|\| ISO/IEC MPEG - '''(recompile needed for encoding)'''
\| mp4a|\| {{Yes}} \|\| {{Yes}} \|\| faad (decode), faac (encoding) \|\|
ISO/IEC MPEG \| \|\| {{Yes}} \|\| {{Untested}} \|\| faad (decode),
libaacplus + ffmpeg (encoding) \|\| ISO/IEC MPEG, AAC+ encoding through
libaacplus + ffmpeg (patched) - untested '''RECOMPILE VLC & ffmpeg for
this''' Audio codec \| a52, a52b \|\| {{Yes}} \|\| {{Yes}} \|\| liba52
(decode), ffmpeg (encode) \|\| \| atrc \|\| {{No}} \|\| \|\| \| ILBC,
ilbc \|\| {{Untested}} \|\| {{Untested}} \|\| QuickTime (decode) \|\|
(check for encoder and free decoder) \| \|\| {{No}} \|\| ffmpeg \|\|
(check for encoder) \| \|\| {{No}} \|\| ffmpeg \|\| \| Qclp \|\| {{No}}?
\|\| ffmpeg \|\| Usually in QCP container.
[https://trac.videolan.org/vlc/ticket/5347 buggy?] \| lpcJ, 28_8, dnet,
sipr, cook, atrc, raac, racp, ralf \|\| {{Yes}} \|\| {{No}} \|\| \|\|
Some work. Half don't \| shrn \|\| {{No}} \|\| {{No}} \|\| \|\| ffmpeg
and ffplay do it. VLC doesn't. (It is in the FOURCC list in VLC's
{{VLCSourceFileDionoea]]) \| spex \|\| {{Yes}} \|\| {{Yes}} \|\|
libspeex \|\| \| vorb \|\| {{Yes}} \|\| {{Yes}} \|\| libvorbis \|\| \|
dts \|\| {{Yes}} \|\| {{No}} \|\| libdca \|\| DTS-HD unsupported \| \|\|
{{Yes}} \|\| {{No}} \|\| libmpcdec \|\| \| wma1, wma2 \|\| {{Yes}} \|\|
{{Yes}}, violated \|\| ffmpeg \|\| WMA9 is not supported \| flac \|\|
{{Yes}} \|\| {{Yes}} \|\| libflac \|\| lossless \| alac \|\| {{Yes}}
\|\| {{No}} \|\| ffmpeg \|\| lossless \| \|\| {{No}} \|\| \|\| lossless
\| \|\| {{Yes}} \|\| {{No}} \|\| libmpcdec \|\| \| \|\| {{Yes}} \|\|
{{Yes}} \|\| ffmpeg and internal \|\| \| samr \|\| {{Yes}} \|\| {{Yes}}
\|\| ffmpeg + libamrnb + libamrwb \|\| '''RECOMPILE VLC for this'''
Speech codec \| SONC \|\| {{Yes}} \|\| {{Yes}} \|\| ffmpeg \|\| }

== Subtitles Codecs == {{Transcluded|Subtitles codecs}} <!-- Editors:
This page includes content from Subtitles codecs. Make edits to this
section there. --> {{:Subtitles codecs}}

== Format/Container/Muxers ==

{\| class="wikitable codec-table centered sortable" -! Name !!
extensions !! Playable !! Savable !! Comment \| .3gp \|\| {{Yes}} \|\|
{{Untested}} \|\| \| .asf, .wmv \|\| {{Yes}} \|\| {{No}} \|\| \| .asf,
.wmv \|\| {{Yes}} \|\| {{Yes}} \|\| \| .au \|\| {{Yes}} \|\| \|\| \|
.avi \|\| {{Yes}} \|\| {{Yes}}, violated \|\| \| \|\| {{Untested}} \|\|
{{Untested}} \|\| \| .flv \|\| {{Yes}} \|\| {{Yes}} \|\| through ffmpeg
\| .mov \|\| {{Yes}} \|\| {{Yes}} \|\| \| .mp4 \|\| {{Yes}} \|\| {{Yes}}
\|\| \| .ogm, .ogg \|\| {{Yes}} \|\| {{Yes}} \|\| \| .mkv, .mka \|\|
{{Yes}} \|\| {{No}}, WIP \|\| Summer of Code 2007 Project \| .ts, .mpg
\|\| {{Yes}} \|\| {{Yes}} \|\| \| .mpg, .mp3, .mp2 \|\| {{Yes}} \|\|
{{Yes}} \|\| \| .nsc \|\| {{Yes}} \|\| {{No}} \|\| \| .nsv \|\| {{Yes}}
\|\| {{No}} \|\| \| .nut \|\| {{Yes}} \|\| {{Yes}} \|\| Muxable through
libavformat \| .ra, .ram, .rm, .rv , .rmbv \|\| {{Partial}} \|\| {{No }}
\|\| version 4 and 5, no support for version 3 \| .a52, .dts, .aac,
.flac, .dv, .vid \|\| {{Yes}} \|\| ?? \|\| \| .tta, .tac \|\| {{Yes}}
\|\| {{No}} \|\| \| .ty \|\| {{Yes}} \|\| {{No}} \|\| \| .wav, .dts \|\|
{{Yes}} \|\| {{Yes}} \|\| \| .xa \|\| {{Yes}} \|\| {{No}} \|\| }

== HD-Discs codecs == {{Transcluded|HD-Discs codecs}} <!-- Editors: This
page includes content from HD-Discs codecs. Make edits to this section
there. --> {{:HD-Discs codecs}}

[[Category:Codecs]] [[Category:Knowledge Base]]

{{DEFAULTSORT:*}}
