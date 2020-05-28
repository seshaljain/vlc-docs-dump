A **media resource locator** (**MRL**) is a string of characters used to identify a multimedia resource or part of a multimedia resource. A MRL may be used to identify inputs or outputs to .

The MRL syntax is:

``[[access][/demux]://]URL[#[title][:chapter][-[title][:chapter]]] [:option=value ...]``

(in earlier versions of VLC, the delimiter before the optional title and chapter was '@', not '#'.)

=========== ==================================================================================== =========================================================================
MRL section Description                                                                          Possible values
=========== ==================================================================================== =========================================================================
access      How to obtain the media data                                                         | cdda: CD Digital Audio
                                                                                                 | dir: Filesystem-based directory
                                                                                                 | dv: Digital Video/FireWire
                                                                                                 | dvd: DVD
                                                                                                 | file: Filesystem-based file
                                                                                                 | ftp: FTP
                                                                                                 | gnomevfs: GnomeVFS
                                                                                                 | http: HTTP
                                                                                                 | mms: Microsoft Media Server
                                                                                                 | pvr: PVR
                                                                                                 | rtp: RTP
                                                                                                 | rtsp: RTSP
                                                                                                 | simpledvd: simple interface to DVD-Video, bypassing menus (?)
                                                                                                 | smb: Server Message Block
                                                                                                 | tcp: TCP
                                                                                                 | udp: UDP
                                                                                                 | vcdx: Video CD
                                                                                                 | vlc: commands to VLC itself, e.g. vlc://pause\ *seconds* and vlc://quit
demux       The format of the source data                                                        | a52sys/Raw A/52 demuxer
                                                                                                 | aiff/AIFF demuxer
                                                                                                 | asf/ASF v1.0 demuxer
                                                                                                 | au/AU demuxer
                                                                                                 | avi/AVI demuxer
                                                                                                 | demuxdump/File dumpper
                                                                                                 | dtssys/Raw DTS demuxer
                                                                                                 | flac/FLAC demuxer
                                                                                                 | h264/H264 video demuxer
                                                                                                 | m3u/Playlist metademux
                                                                                                 | m4a/MPEG-4 audio demuxer
                                                                                                 | m4v/MPEG-4 video demuxer
                                                                                                 | mjpeg/M-JPEG camera demuxer
                                                                                                 | mp4/MP4 stream demuxer
                                                                                                 | mpga/MPEG audio / MP3 demuxer
                                                                                                 | mpgv/MPEG-I/II video demuxer
                                                                                                 | nsc/Windows Media NSC metademux
                                                                                                 | nsv/NullSoft demuxer
                                                                                                 | nuv/Nuv demuxer
                                                                                                 | ogg/OGG demuxer
                                                                                                 | playlist/B4S playlist import
                                                                                                 | playlist/DVB playlist import
                                                                                                 | playlist/M3U playlist import
                                                                                                 | playlist/New winamp 5.2 shoutcast import
                                                                                                 | playlist/PLS playlist import
                                                                                                 | playlist/Playlist
                                                                                                 | playlist/Podcast parser
                                                                                                 | playlist/XSPF playlist import
                                                                                                 | ps/MPEG-PS demuxer
                                                                                                 | ps/MPEG-PS demuxer
                                                                                                 | pva/PVA demuxer
                                                                                                 | rawdv/DV (Digital Video) demuxer
                                                                                                 | real/Real demuxer
                                                                                                 | sgimb/Kasenna MediaBase parser
                                                                                                 | subtitle/Text subtitles parser
                                                                                                 | tta/TTA demuxer
                                                                                                 | ty/TY Stream audio/video demux
                                                                                                 | vobsub/Vobsub subtitles parser
                                                                                                 | voc/VOC demuxer
                                                                                                 | wav/WAV demuxer
                                                                                                 | xa/XA demuxer
URL         The `URI <http://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ of the source See http://www.w3.org/TR/uri-clarification/
title       Which title to select for input                                                      Positive integer
chapter     Which chapter to select for input                                                    Positive integer
option      Options to apply only to the specified MRL                                           See `VLC command-line help <VLC_command-line_help>`__ for a full list
=========== ==================================================================================== =========================================================================

Exception
---------

An exception to these rules appears to be with `UDP <UDP>`__/`RTP <RTP>`__ streams, where it may look like:

| ```udp://@:portnumber`` <udp://@:portnumber>`__
| ``# Example: ``
| ``#   ``\ ```udp://@:1234`` <udp://@:1234>`__
| ``#``
| ``# Apparently the @ has a meaning like localhost, though``
| ``#   ``\ ```udp://localhost:1234`` <udp://localhost:1234>`__
| ``# doesn't seem to work in this circumstance, for some reason.``

`Category:Glossary <Category:Glossary>`__
