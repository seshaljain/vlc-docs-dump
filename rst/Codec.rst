{{see also|Documentation:Modules}}

{{wikipedialabel1=Video codecslabel2=Audio
codecslabel3=Containers|Category:Container_Formats}}

A part of the program which understands a type of video or audio (short
for '''Co'''der/'''Dec'''oder or '''Co'''mpression/'''Dec'''ompression).
DivX and Theora are examples of video codecs; MP3 and Vorbis are audio
codecs. The output stream produced when a codec to audio or video is
generally "muxed" into a container format, such as AVI or Ogg. As
certain codecs are often associated with certain container formats, the
name of the container is often used to imply the codec, such as "Ogg",
which usually refers to a Vorbis stream in an Ogg container.

To know what codecs are readable with {{VLC}}, ''see [[VLC Features
Formats]]''.

For [http://discerning.com/topics/audiovideo/video_encoding.html
portability to almost all decoders], we recommend using the [[MPEG-1]]
standard of <code>'''vcodec'''='''mp1v'''</code>,
<code>'''acodec'''='''mpga'''</code>, and
<code>'''mux'''='''mpeg1'''</code>. See the [[MPEG]] Wiki page for more
details on the other MPEG standards.

To save a file in a different codec, you can use the
[[Documentation:Streaming_HowTo_New#Streaming_using_the_GUI|streaming
wizard]] or [[transcode]] from the [[command prompt]] with a command
like this:

<code>vlc file --sout='#transcode{'''vcodec'''='''''mp1v''''',
'''vb'''='''''1024''''', '''acodec'''='''''mpga''''',
'''ab'''='''''128'''''}:std{access=file, '''mux'''='''''mpeg1''''',
'''dst'''='''''C:file_name.mpg'''''}'</code>

==<span id="Video"></span> Video Codecs== {{See also|Category:Video
codecs}}

Use the "name" part in your <code>vcodec=...</code> commands

{\| \| '''''name''''' \| ''description'' '''mp1v''' \| [[MPEG-1]] Video
- recommended for portability '''mp2v''' \| [[MPEG-2]] Video - used in
DVDs '''mp4v''' \| [[MPEG-4]] Video '''SVQ1''' \| [[Sorenson Video]] v1
'''SVQ3''' \| Sorenson Video v3 '''DVDv''' \| [[MPEG-2-\| '''WMV1''' \|
[[Windows Media Video]] v1 '''WMV2''' \| Windows Media Video v2 WMV3 \|
Windows Media Video v3, also called Windows Media 9 ([[VSG:Format:WMV-\|
'''DVSD''' \| [[Digital Video]] '''MJPG''' \| [[MJPEG]] '''H263''' \|
[[H263]] '''h264''' \| [[H264]] '''theo''' \| [[Theora]] '''IV20''' \|
[[Indeo Video]] IV40 \| Indeo Video version 4 or later '''RV10''' \|
[[Real Media Video]] '''cvid''' \| [[Cinepak]] '''VP31''' \| On2 [[VP3]]
'''FLV1''' \| [[Flash Video]] '''CYUV''' \| [[Creative YUV]] '''HFYU'''
\| [[Huffman YUV]] '''MSVC''' \| Microsoft Video v1 '''MRLE''' \|
Microsoft [[RLE]] Video '''AASC''' \| [[Autodesk Animator Studio Codec]]
RLE Video '''FLIC''' \| [[FLIC]] video '''QPEG''' \| [[QPEG]] Video
'''VP8''' \| [[VP8]] Video \|}

==<span id="Audio"></span> Audio Codecs== {{See also|Category:Audio
codecs}}

Use the "name" part in your <code>acodec=...</code> commands

{\| \| '''''name''''' \| ''description'' '''mpga''' \| [[MPEG audio]]
(recommended for portability) '''mp3''' \| [[MP3 audio- \| '''mp4a''' \|
[[MP4 audio]] '''a52''' \| [[Dolby Digital]] ([[A52]] or [[AC3]])
'''vorb''' \| [[Vorbis]] '''opus''' \| [[Opus]] '''spx''' \| [[Speex]]
'''flac''' \| [[FLAC]] \|} ===No-"name" Codecs===

-  [[DTS]]
-  [[AAC (Advanced Audio Coding)]]
-  [[Windows Media Audio]]
-  [[DV Audio]]
-  [[LPCM]]
-  [[ADPCM]]
-  [[AMR]]
-  [[QuickTime Audio]]
-  [[RealAudio]]
-  [[MACE]]
-  [[MusePack]]

==Subtitle Codecs==

See [[Subtitles codecs]] for more information.

{\| '''CVD''' \| [[CVD]] '''SVCD (Overlay Graphics)''' \|
[http://www.vcdimager.org/pub/vcdimager/manuals/0.7/svcd-ogt-subtitles.html
SVCD Subtitle (OGT) Information] '''SRT''' \| [[SubRip]] '''<abbr
title="SubStation Alpha/Advanced SubStation Subtitles">SSA/ASS</abbr>'''
\| [[SubStation Alpha]] '''SubViewer''' \| [[SubViewer]] '''VobSub''' \|
[[VobSub]] '''DVD subtitles''' \| [[DVD subtitles]] '''DVB subtitles'''
\| [[DVB subtitles]] '''VPlayer''' \| [[Vplayer]] '''MicroDVD''' \|
[[MicroDVD]] '''SAMI''' \| [[SAMI]]

\|}

== Muxers == Use the "name" part in your <code>mux=...</code> commands

{\| \| '''''name''''' \| ''description'' '''mpeg1''' \| [[MPEG-1]]
multiplexing - recommended for portability. Only works with mp1v video
and mpga audio, but works on all known players '''ts''' \| [[MPEG-TS-\|
'''ps''' \| [[MPEG-PS-\| '''mp4''' \| [[MPEG-4-\| '''avi''' \| [[AVI]]
'''asf''' \| [[ASF]] '''dummy''' \| [[dummy]] output, can be used in
creation of [[MP3]] files. '''ogg''' \| [[Xiph.org]]'s [[ogg]] container
format. Can contain audio, video, and metadata. \|}

== See Also == \* [[FourCC]] and http://www.fourcc.org/ \*
http://discerning.com/topics/audiovideo/video_encoding.html

{{stub}} [[Category:Codecs|*]] [[Category:Glossary]]
