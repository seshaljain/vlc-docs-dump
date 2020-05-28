{{wikipedia|Windows Media Player}} Windows Media Player is the standard
multimedia [[player]] for Microsoft® [[Windows]]® systems.

== Supported formats ==

According to Microsoft® [http://support.microsoft.com/kb/316992
Knowledge Base Article 316992], Windows Media Player supports the
following formats "out of the box":

{\| class="wikitable"
   ! scope="col" \| Type ! scope="col" \| Supported formats

Microsoft® media formats \| *Advanced Systems Format (.[[asf]])*\ Audio
Visual Interleave (.[[avi]]) *Audio for Windows (.[[wav]])*\ Microsoft®
Digital Video Recording (.dvr-ms) *Windows Media Audio
(.[[wma]])*\ Windows Media Video (.wmv, .wm) Microsoft® media metafiles
\| *Advanced Stream Redirector (.asx)*\ Windows Media Audio Redirector
(.wax) *Windows Media Download Package (.wmd)*\ Windows Media Player
Playlist (.wpl) *Windows Media Redirector (.wmx)*\ Windows Media Video
Redirector (.wvx) ISO/IEC (MPEG) \| *MPEG-1 (.mpeg, .mpg, .m1v)*\ MPEG
Audio Layer III (.[[mp3]]) *MPEG Audio Layer II (.mp2, .mpa)*\ Metafile
Playlist (.[[m3u]]) Industry standard \| *Audio Interchange File Format
( .aif, .aifc, .[[aiff]])*\ CD Audio Track (.cda) *Musical Instrument
Digital Interface (.mid, .[[midi]], .rmi)*\ Sun Microsystems and NeXT
(.[[au]], .snd) \|}

== Common Issues == === MPEG-2 and MPEG-4 playback ===

Microsoft® does not bundle [[codec]]s for [[MPEG-2]] or [[MPEG-4]] with
Windows and recommends purchasing them as part of a "DVD decoder pack"
from a third-party vendor.

The symptom associated with a missing codec is Windows Media Player
displaying the cryptic "C00D11CD" error code immediately after opening
an MPEG-2 or MPEG-4 coded file or stream. At that point, you must
purchase the appropriate codec, perhaps from Microsoft's®
[http://www.microsoft.com/windows/windowsmedia/player/plugins.aspx list
of approved vendors].

=== Streaming from VLC === To date, the only option for streaming from
VLC to Windows Media Player is to: \* [[Transcode]] the file or feed
into [[WMV]] format \* Encapsulate the transcoded stream in the [[ASF]]
container format \* Use [[MMS]] or [[MMSH]] for the stream transport

{{forum|255}}.

Otherwise, Windows Media Player does not appear to support streaming for
anything other than its proprietary formats.

<blockquote>'' "Windows Media Player 9 Series can play files in a wide
variety of digital media file formats, but Windows Media Services 9
Series '''cannot stream all of those files'''. In certain cases, you may
need to convert digital media files into a compatible format before you
can stream them."
[http://www.microsoft.com/windows/windowsmedia/forpros/server/faq.aspx#2_3]
''</blockquote>

Streaming to Windows Media Player over [[HTTP]] is supported, but the
multimedia stream must be converted to a Microsoft-proprietary format
with [[Windows Media Encoder]] beforehand.

Streaming is known to work with Windows Media Player 9 or higher. In
particular, Windows Media Player 8 does not interoperate with VLC.
{{forum|5199}}

=== Compatibility === If you discover problems with your Windows Media
Player please download the latest version: \*
[https://www.microsoft.com/EN-US/download/windows-media-player-details.aspx
English] \*
[https://www.microsoft.com/DE-DE/download/windows-media-player-details.aspx
Deutsch] \*
[https://www.microsoft.com/FR-FR/download/windows-media-player-details.aspx
Français]

{{Outdated}}

[[Category:Player]] [[Category:Windows]]
