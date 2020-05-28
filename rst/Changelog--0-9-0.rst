= Changes between 0.8.6 and 0.9.0 =

== Important notes == \* This version of VLC contains a [[Qt Interfacerc
interface]] changed. They now require a target name as their first
argument. Example: :<pre>vlc --sub-filter "marq@test%7Bmarquee=Hello}"
-I rc <somevideo> </pre> :You can then use commands like: <pre>@test
marq-marquee Goodbye</pre> :These new commands are also available in the
[[Console#telnet interface|telnet interface]].

\* The [[HTTP Interface]] is now only available on the local machine by
default. : If you want to make it available from other machines, you
will have to edit the ".hosts" file. :\* On UNIX/Linux, the file is in
/usr/share/vlc/http/.hosts :: If you're using the old http interface,
it's located in /usr/share/vlc/http/old/.hosts :\* On Windows they are
in C:Program FilesVideoLANVLChttp.hosts and C:Program
FilesVideoLANVLChttpold.hosts :\* On Mac OS X, you can find it in
VLC.app/Contents/MacOS/share/http/.hosts and respectively in
VLC.app/Contents/MacOS/share/http/old/.hosts

\* The "[[RTP|rtp]]" access output module has been removed: : Please use
the RTP stream output instead, e.g.: : Old:
'#std{access=rtp,dst=239.255.1.2,sap}' : New:
'#rtp{dst=239.255.1.2,sap}'

== Important Changes ==

=== Playlist === \* Vastly improved playlist support: \*\* [[Media
library]] support \*\* "Live search" \*\* [[Shoutcast]] TV listings \*\*
[http://www.audioscrobbler.net/ Audioscrobbler]/[\ http://www.last.fm/
last.fm] support \* Album art support \* User definable Lua playlist
scripts. See
[http://trac.videolan.org/vlc/browser/trunk/share/luaplaylist/README.txt
share/luaplaylist/README.txt] :(Default scripts open YouTube,
DailyMotion, metacafe and Google Video URLs) \* User definable Lua
metadata and album art fetcher scripts. See
[http://trac.videolan.org/vlc/browser/trunk/share/luameta/README.txt
share/luameta/README.txt]

=== Input/Demuxers === \* [[UDP-Lite]] transport for [[RTP]]/[[AVP]] \*
[[DCCP]] transport for [[RTP]]/[[AVP]] \* Proxy support for [[MMSH]]
stream \* [[JACK]] audio input support \* MP4 gpac and Apple chapter
support \* Input run time option (improved live stream recording) \*
Fixed aiff stereo file \* Fixed audio glitch on seek \* Improved FLAC
demuxer (duration / current time / meta data) \* AAC tags support \*
APEv1/2 tags support \* Improved ID3v2 tags support \* Improved
Ogg/Vorbis tags support \* Raw video support \* Standard MIDI File
(types 0 & 1) support \* Tivo Series 2 support \* v4l2 access module
support \* CD+G karaoke Files support \* MXF files support

=== Decoders === \* [[VP6|VP60/VP61/VP6F/VP62]] support \* [[MKV]]
[[USF]] subtitles support \* HTML based subtitles support \* Flash
Screen Video support \* CamStudio Screen Video support \* DOSBox Capture
support \* Karl Morton's Video support \* limited atrac3 support \*
Fluidsynth MIDI software synthesis (with external sound fonts) \* New
codec FOURCCs to support more specific files: Avid, FCP, Sony, Samsung,
... \* Closed Caption Decoder (DVD, ReplayTV, Tivo, DVB/ATSC) \* H.264
PAFF support \* DNxHD / VC-3 support \* NellyMoser ASAO support \* APE
(Monkey audio) support \* VBI & EBU (Teletext) support

=== Encoders === \* Flash Screen Video support

=== Video output and filters === \*
[[Documentation:Modules/adjustInvert]] and
[[Documentation:Modules/distortWave]],
[[Documentation:Modules/rippleGradient]] and
[[Documentation:Modules/psychedelicpuzzle]] video output filter \*
Rewrite [[Documentation:Modules/motion controlextract]] video filter
(extract Red, Green and Blue components from a video) \* New
[[Documentation:Modules/sharpenerase]] video filter (remove a logo from
a video) \* Enhancements to subtitles' renderer to support bold, italics
and some HTML tags \* Support for RGBA and I420 blending. This improves
[[Mosaic]] CPU usage *a lot*. \* New transparency mask video filter (for
use with the mosaic_bridge module). \* New bluescreen video filter (for
use with the mosaic_bridge module). This was previously part of the
mosaic module. \* Fix random characters problem in RSS filter. \* Add
rotate-deciangle for more precision on rotate filter \* Support for
Intel SSE2 intruction set in chroma converters \* Improved use of Intel
MMX intruction set in chroma converters

=== Audio output and filters === \* Replay gain support. \* Play audio
when going slower/faster ( no pitch filter yet ). \* New spatializer
audio filter.

=== Stream output === \* RTSP for TS-multiplexed broadcast streams \*
New RTP payload formats: \*\* Speex voice audio codec \*\* ITU T.140
(for text, subtitles) output \*\* G.711 (both A-law and µ-law) output \*
UDP-Lite transport for RTP \* DCCP transport for RTP \* Lots of fixes
for RTSP broadcasting

=== Interfaces === \* Windows/Linux \*\* Brand [[Qt4 Interfacemouse
gestures]] \*\* Experimental Lua interface modules. See vlc -I lua for
more info \* Unix \*\* Option to allow only one running instance, using
[[D-Bus]] interface. \*\* [[D-Bus]] Interface implementing the MPRIS
(Media Player Remote Interfacing specification - see [[DBus-spec]]), a
common dbus control interface for media players that intends to become
an xdg standard when finished:
[http://wiki.xmms2.xmms.se/index.php/Media_Player_Interfaces]. \* Motion
module use disk accelerometers to keep video horizontal \* Ncurses
interface now uses ncursesw to correctly display wide characters when
using an UTF-8 locale. \* Plugin to set Telepathy presence message using
MissionControl

=== Linux Port === \* VLC now complies with the
[http://standards.freedesktop.org/basedir-spec/basedir-spec-0.6.html XDG
Base Directory Specification version 0.6] (which means that VLC doesn't
use the $HOME/.vlc directory anymore)

=== Mac OS X Port === \* Mac OS X Framework that can be used to embed
VLC in third party applications. (Google Summer Of Code Student
project).

=== LibVLC === \* Event management and various improvement in libvlc.
(Part of a Google Summer Of Code Student project).

=== Capture === \* new [[BDA]] device driver plugin for [[DVB]]-C/S/T
capture cards on Microsoft Windows

=== Localisations === \* Finnish \* Persian \* Polish

== Changes in between == Links to changelogs between:
:[[Changelog/0.8.6i0.8.6g and 0.8.6h]]<br/> :[[Changelog/0.8.6g0.8.6e
and 0.8.6f]]<br/> :[[Changelog/0.8.6e0.8.6c and 0.8.6d]]<br/>
:[[Changelog/0.8.6c0.8.6a and 0.8.6b]]<br/> :[[Changelog/0.8.6a|0.8.6
and 0.8.6a]]<br/>

[[Category:Changelog]]
