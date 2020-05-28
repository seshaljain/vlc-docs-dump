A '''media resource locator''' ('''MRL''') is a string of characters
used to identify a multimedia resource or part of a multimedia resource.
A MRL may be used to identify inputs or outputs to {{VLC}}.

The MRL syntax is:

   [[access][/demux]://]URL[#[title][:chapter][-[title][:chapter]]]
   [:option=value ...]

(in earlier versions of VLC, the delimiter before the optional title and
chapter was '@', not '#'.)

{\| class="wikitable"
   ! MRL section ! Description ! Possible values

access \| How to obtain the media data \| cdda: CD Digital Audio<BR>
dir: Filesystem-based directory<BR> dv: Digital Video/FireWire<BR> dvd:
DVD<BR> file: Filesystem-based file<BR> ftp: FTP<BR> gnomevfs:
GnomeVFS<BR> http: HTTP<BR> mms: Microsoft Media Server<BR> pvr: PVR<BR>
rtp: RTP<BR> rtsp: RTSP<BR> simpledvd: simple interface to DVD-Video,
bypassing menus (?)<BR> smb: Server Message Block<BR> tcp: TCP<BR> udp:
UDP<BR> vcdx: Video CD<BR> vlc: commands to VLC itself, e.g.
vlc://pause''seconds'' and vlc://quit demux \| The format of the source
data \| a52sys/Raw A/52 demuxer<BR> aiff/AIFF demuxer<BR> asf/ASF v1.0
demuxer<BR> au/AU demuxer<BR> avi/AVI demuxer<BR> demuxdump/File
dumpper<BR> dtssys/Raw DTS demuxer<BR> flac/FLAC demuxer<BR> h264/H264
video demuxer<BR> m3u/Playlist metademux<BR> m4a/MPEG-4 audio
demuxer<BR> m4v/MPEG-4 video demuxer<BR> mjpeg/M-JPEG camera demuxer<BR>
mp4/MP4 stream demuxer<BR> mpga/MPEG audio / MP3 demuxer<BR>
mpgv/MPEG-I/II video demuxer<BR> nsc/Windows Media NSC metademux<BR>
nsv/NullSoft demuxer<BR> nuv/Nuv demuxer<BR> ogg/OGG demuxer<BR>
playlist/B4S playlist import<BR> playlist/DVB playlist import<BR>
playlist/M3U playlist import<BR> playlist/New winamp 5.2 shoutcast
import<BR> playlist/PLS playlist import<BR> playlist/Playlist<BR>
playlist/Podcast parser<BR> playlist/XSPF playlist import<BR> ps/MPEG-PS
demuxer<BR> ps/MPEG-PS demuxer<BR> pva/PVA demuxer<BR> rawdv/DV (Digital
Video) demuxer<BR> real/Real demuxer<BR> sgimb/Kasenna MediaBase
parser<BR> subtitle/Text subtitles parser<BR> tta/TTA demuxer<BR> ty/TY
Stream audio/video demux<BR> vobsub/Vobsub subtitles parser<BR> voc/VOC
demuxer<BR> wav/WAV demuxer<BR> xa/XA demuxer URL \| The
[http://en.wikipedia.org/wiki/Uniform_Resource_Identifier URI] of the
source \| See http://www.w3.org/TR/uri-clarification/ title \| Which
title to select for input \| Positive integer chapter \| Which chapter
to select for input \| Positive integer option \| Options to apply only
to the specified MRL \| See [[VLC command-line help]] for a full list
\|}

== Exception == An exception to these rules appears to be with
[[UDP]]/[[RTP]] streams, where it may look like:

   `udp://@:portnumber <udp://@:portnumber>`__ # Example: # udp://@:1234
   # # Apparently the @ has a meaning like localhost, though #
   udp://localhost:1234 # doesn't seem to work in this circumstance, for
   some reason.

[[Category:Glossary]]
