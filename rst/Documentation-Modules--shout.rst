The services discovery module was removed. '''The
[[#Access_output|Access output module]] is current.'''

== Access output == {{Moduletype=Access outputdescription=This module
forwards [[vorbis]] streams to an [[icecast]] server|sc=shout}}

{{Clear}}

Documentation is present directly in the source code (4.0.0-dev) as multiple C comment blocks, relevant comments reproduced here (copyright © 2005 VLC authors and VideoLAN, Authors: Daniel Fischer and Derk-Jan Hartman, LGPL 2.1 or later):
   /*************************************************************************\***\*
   \* Some Comments: \* \* - this only works for ogg and/or mp3, and we
   don't check this yet. \* - MP3 metadata is not passed along, since
   metadata is only available after \* this module is opened. \* \*
   Typical usage: \* \* vlc v4l:/dev/video:input=2:norm=pal:size=192x144
   \* --sout '#transcode{vcodec=theora,vb=300,acodec=vorb,ab=96} \*
   :std{access=shout,mux=ogg,dst=localhost:8005}'
   \***\ \***************************************************************************/

v4l refers to [[GNU/Linux]] Video4Linux and won't work for Windows
users.

This comment precedes the genre option:
   /\* To be listed properly as a public stream on the Yellow Pages of shoutcast/icecast
      the genres should match those used on the corresponding sites.
      Several examples are Alternative, Classical, Comedy, Country etc.
      \*/

This comment precedes the stream information options:
   /\* The shout module only "transmits" data. It does not have direct access to
      "codec level" information. Stream information such as bitrate,
      samplerate, channel numbers and quality (in case of Ogg streaming)
      need to be set manually \*/

=== Options === {{Option value=string description=Name to give to this
stream/channel on the [[shoutcast]]/[[icecast]] server }} {{Option
value=string description=Description of the stream content or
information about your channel }} {{Option value=boolean description=You
normally have to feed the shoutcast module with [[Ogg]] streams. It is
also possible to stream [[MP3]] instead, so you can forward MP3 streams
to the shoutcast/icecast server }} {{Option value=string
description=Genre of the content }} {{Option value=string
description=URL with information about the stream or your channel }}
{{Option value=string description=[[Bitrate]] information of the
[[transcode]]d stream }} {{Option value=string
description=[[Samplerate]] information of the transcoded stream }}
{{Option value=string description=Number of channels information of the
transcoded stream }} {{Option value=string description=[[Ogg]]
[[Vorbis]] Quality information of the transcoded stream }} {{Option
value=boolean description=Make the server publicly available on the
'Yellow Pages' (directory listing of streams) on the icecast/shoutcast
website. Requires the bitrate information specified for shoutcast.
Requires Ogg streaming for icecast }}

== Services discovery == {{Moduletype=Services
discoverylast_version=1.0.6sc=shoutcast|sc2=shout}}

Three sub-modules had shortcuts of <code>shoutcasttv</code>,
<code>frenchtv</code> and <code>freebox</code>.

=== Options === None (<code>--shoutcast-limit</code> was deprecated with
{{Commitdiffacb5da732a27b6c7e8d6e05c2e183d4ae49a9ea9}}). {{Clear}}

=== shout-winamp === This sub-module had the shortcut
<code>shout-winamp</code> with description "New winamp 5.2 shoutcast
import". It is scheduled
[https://git.videolan.org/?p=vlc.git;a=commitdiff;h=d3859f364921c6f4d48115da331ac3a44d7a6351
to be removed] (currently in 4.0.0-dev) with the note: <pre> Removes the
long unused Winamp/SHOUTcast directory stream filter for playlist
handling, which was mostly useful together with the service discovery
(modules/services_discovery/shout.c) which is not present anymore.
</pre> History: \*
[https://git.videolan.org/?p=vlc.git;a=commit;h=acb5da732a27b6c7e8d6e05c2e183d4ae49a9ea9
&#x5B;acb5da732a27b6c7e8d6e05c2e183d4ae49a9ea9&#x5D;] (introduction) \*
{{VLCSourceFilemodules/demux/playlist/shoutcast.c}} \*
{{VLCSourceFilemodules/demux/playlist/shoutcast.c}} \*
{{VLCSourceFilemodules/demux/playlist/shoutcast.c}} \*
{{VLCSourceFilemodules/demux/playlist/shoutcast.c}} \*
{{VLCSourceFilemodules/demux/playlist/shoutcast.c}} \*
{{VLCSourceFilemodules/demux/playlist/shoutcast.c}} \*
{{VLCSourceFilemodules/demux/playlist/shoutcast.c}} \*
{{VLCSourceFilemodules/demux/playlist/shoutcast.c}} \*
[https://git.videolan.org/?p=vlc.git;a=commit;h=d3859f364921c6f4d48115da331ac3a44d7a6351
&#x5B;d3859f364921c6f4d48115da331ac3a44d7a6351&#x5D;] (removal)
{{Clear}}

== Source code == \*
{{VLCSourceFilep=vlc/vlc-1.0.git|modules/services_discovery/shout.c}}

{{Documentation}}
