:''See also [[Windows Media Player]]'' {{wikipedia|Windows Media Video}}
'''Windows Media''' is a generic name for the set of proprietary
streaming audio and video technologies developed by Microsoft. It
includes the '''Windows Media Video''' (WMV) and '''Windows Media
Audio''' (WMA) codecs.

Windows Media Video is not built solely on Microsoft in-house
technology. From version 7 (WMV1), Microsoft has used its own
non-standard version of [[MPEG-4]] Part 2.

Windows Media is often generated using Microsoft's proprietary Windows
Media Video 9 VCM software for Windows.

Microsoft has submitted Version 9 codec to the [[wikipedia:Society of
Motion Picture and Television Engineers|Society of Motion Picture and
Television Engineers]] (SMPTE), for approval as an international
standard. The Trial version of standards were published by SMPTE in
September 2005. A reference decoder implementation and test sequences
are also available. This codec is used to distribute high definition
video on standard DVDs in a format Microsoft has branded as '''WMV
HD''', which can be played back on computers or compatible DVD players.

== Encoding == You can encode audio to WMA format with following command
{{%}} vlc input.wav
:sout="#transcode{acodec=wma2,ab=128,channels=2,samplerate=44100}:std{access=file,mux=asf,dst=output.wma}"

You can encode video and audio to WMV format with following command
   {{%}} vlc input.avi
   :sout="#transcode{vcodec=WMV2,width=720,vb=1200,height=576,acodec=wma2,ab=128,channels=2}:std{access=file,mux=asf,dst=output.wmv}"

== Container == Windows Media files use the [[ASF]] container. They
generally have the file extension '''.wmv''', '''.wma''', '''.wm''' or
'''.asf'''.

Windows Media codecs can also be used inside [[AVI]] files.

=== Codecs used in WMV files === See next paragraph for more information
on codecs in WMV files.

== Codecs == {{codec videoaltid=WMVid=WMV2for=Windows Media}} {{codec
audioaltid=WMA|for=Windows Media}} Windows Media often uses special
native codecs for '''Windows Media Video''' and '''Windows Media
Audio'''. WMV3 is often called "Windows Media 9".

{\| class="wikitable" ! scope="col" \| [[Fourcc]] !! scope="col" \|
[[Codec]] !! scope="col" \| Supported by VLC? !! scope="col" \| Comments
MP43 \|\| [[MPEG-4]] \|\| {{Up-to-date}} \|\| WMV1 \|\| {{Up-to-date}}
\|\| WMV2 \|\| Windows Media Video v8 \|\| {{Up-to-date}} \|\| Not
totally implemented for rare files. Please send the files. WMV3 \|\|
Windows Media Video 9 (v3) \|\| {{Up-to-date}} \|\| Not totally
implemented for rare files (VBR). Please send the files. WVC1, WMVA \|\|
Windows Media Video 9 Advanced Profile \|\| {{Up-to-date}} \|\| Not
totally implemented for rare files (VBR, interlacing). Please send the
files. WMVP \|\| Windows Media Video 9 Image \|\| {{Up-to-date}} \|\|
VLC 2.0 or through [[dmo]] for older versions WVP2 \|\| Windows Media
Video 9.1 Image (v2) \|\| {{Up-to-date}} \|\| VLC 2.0 or through [[dmo]]
for older versions MSS1 \|\| Windows Media Screen v7 \|\| {{Up-to-date}}
\|\| with [[dmo]] ONLY MSS2 \|\| Windows Media Video 9 screen codec \|\|
{{Up-to-date}} \|\| with [[dmo]] ONLY }

More info on [http://msdn2.microsoft.com/en-us/library/bb331872.aspx
MSDN]

== Compatibility ==

=== Protected content === Windows Media files may contain [[Digital
Restrictions Management]] (DRM) facilities intended to protect
copyrights. VLC does not play any DRM'd files.

=== Windows Media Video 3 === WMV3, the Video part of Windows Media 9,
is supported in VLC since version 0.8.6. Upgrade to the latest version
({{VLC:latest version}}) to play WMV files.

If you are unable to upgrade, there are still some fixes. If you're
using Windows and have Windows Media Player 9/10 installed, VLC should
be able to play these files, by using Microsoft's own files. Or, if
you're using Linux, see the [[Common Problems]] page for a workaround.

=== On Windows Media Player (Mac) === Microsoft's Windows Media Player
for the Mac does not support all WMV encoded files since it supports
only the ASF file container.{{check}}

[[Category:Windows]]
