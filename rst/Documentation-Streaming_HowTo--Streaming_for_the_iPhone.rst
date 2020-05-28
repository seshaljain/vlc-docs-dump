{{RightMenu|documentation streaming howto toc}}

== Streaming for the iPhone ==

This functionality allows you to link VLC's transcoding capability with
a segmenter which will in turn create the series of files needed for
http live streaming to the iPhone.

Unlike most of VLC's streaming, it doesn't actually stream the files,
but assumes that you have your own webserver which will do that job.

Notes from the developer: *This has only been tested using H.264 w/MP3
or AAC audio using mux=ts, and raw MP3 using mux=raw*\ I've been mostly
an FFMPEG guy till now, so forgive me if my VLC
understanding/terminology is somewhat off. \*This plug-in should support
both Live and non-live HTTP Live streaming feeds, depending on the
options passed to the module.

Notes from the community: \*The user running vlc needs to have
read/write/delete permissions on the directory where the .m3u8 playlist
and .ts file segments will be created and deleted on the webserver.

=== Instructions ===

The name of the module is livehttp, and is specified by specifying
"access=livehttp"

=== Options ===

splitanywhere= (default: false) \*Tells livehttp to split the stream
anywhere, not just on video keyframes. Currently required to be set to
true for audio-only streams and not recommended (probably won't work)
for video streams.

seglen= (default: 10) \*How many seconds of audio/video each segment
should contain. Apple recommends 10, I have been using 5.

numsegs=(default: 0) \*The number of segments to keep in the index file.
The default of 0 keeps all segments in the index (which you would want
for non-live streaming). For live streaming the specification require at
least 3.

delsegs= (default: true) \*Delete segments as they are no longer needed.
If numsegs=0 this parameter is ignored (as all segments are assumed to
be needed)

dst= \*This is actually an option to the access std module. The path of
the segment files to write. The # characters get replaced with the
segment number. So a path of "seg-###.ts" will end up with files called
"seg-001.ts, seg-002.ts, seg-003.ts" etc.

index= \*The path of the index file to write, which will contain the
"playlist" of video/audio segments to stream. Recommended to end in
.m3u8 by specifications. This is the file the <video> tag should be
pointed to.

index-url= \*This is the URL that corresponds to the dst above (how a
browser would access the dst file). The # characters get replaced same
as in the dst parameter. Note: The filename portion of this URL will
most likely need to be in the exact same format as the dst parameter. So
for example if dst=/www/seg-##.ts then the index-url should be something
like
<code><nowiki>index-url=http://mydomain.com/streams/seg-##.ts</nowiki></code>
(Note the same number of # characters)

ratecontrol=(default: false) \*If set to false the there is no rate
control (the muxer sends the data as fast/slow as it can to the
streamer). If set to true the muxer should do rate-control to control
the speed to muxed audio/video is sent to the streamer. Recommended
setting is false in most cases. The only time I've needed this set to
true is while doing a live sliding window stream of a local media file.

=== Examples === [[File:FishCam.jpg%7Cthumb%7Cright%7Calt=An HLS live
feed from a camera pointed at a fish tank with multiple stream encoding
qualities|HLS Live Stream Example: Schou FishCam http://fish.schou.me]]
All examples assume the following: *The Web Server root directory is
/var/www*\ The domain name of the web server is mydomain.com *The stream
segments &amp; index files will be written into /var/www/streaming/ and
will be accessed via
<code><nowiki>http://mydomain.com/streaming/</nowiki></code>…*\ The
destination stream name index file will be called "mystream.m3u8" \*The
following HTML will allow you to view the video based on the above on an
iPhone:

Re-stream a live video feed:
   {{%}} '''<nowiki>vlc -I dummy --mms-caching 0
   http://www.nasa.gov/55644main_NASATV_Windows.asx vlc://quit
   --sout='#transcode{width=320,height=240,fps=25,vcodec=h264,vb=256,venc=x264{aud,profile=baseline,level=30,keyint=30,ref=1},acodec=mp3,ab=96}:std{access=livehttp{seglen=10,delsegs=true,numsegs=5,index=/var/www/streaming/mystream.m3u8,index-url=http://mydomain.com/streaming/mystream-########.ts},mux=ts{use-key-frames},dst=/var/www/streaming/mystream-########.ts}'</nowiki>'''

Create a VOD stream: (Non-live. When this command finishes, all the
segments should have been created and the index file contain pointers to
all of them) % '''<nowiki>vlc -I dummy /var/myvideos/video.mpg
vlc://quit
--sout='#transcode{width=320,height=240,fps=25,vcodec=h264,vb=256,venc=x264{aud,profile=baseline,level=30,keyint=30,ref=1},acodec=mp3,ab=96}:std{access=livehttp{seglen=10,delsegs=false,numsegs=0,index=/var/www/streaming/mystream.m3u8,index-url=http://mydomain.com/streaming/mystream-########.ts},mux=ts{use-key-frames},dst=/var/www/streaming/mystream-########.ts}'</nowiki>'''

Re-stream a live audio feed:
   % '''<nowiki>vlc -I dummy --mms-caching 0
   http://www.nasa.gov/55644main_NASATV_Windows.asx vlc://quit
   --sout='#transcode{acodec=mp3,ab=96}:duplicate{dst=std{access=livehttp{seglen=10,delsegs=true,numsegs=5,index=/var/www/streaming/mystream.m3u8,index-url=http://mydomain.com/streaming/mystream-########.mp3},mux=raw,dst=/var/www/streaming/mystream-########.mp3},select=audio}'</nowiki>'''

'''Note:''' I found that these example don't work as written here; I
won't edit them in place as they might work in different circumstances.
I found two problems using the released version of VLC 2.0.0 on WinXP:

# All examples need to have the single quotes surrounding the --sout
parameter removed. Otherwise VLC complains "stream_out_standard stream
out error: no mux specified or found by extension". # The final example
is audio-only, but does not specify the splitanywhere=true flag. As a
result it writes one massive chunk waiting for a keyframe that never
comes.

Example commandline that did work for me:
   % <nowiki>vlc -I dummy x:someaudiohere.ogg vlc://quit
   --sout=#transcode{acodec=mp3,ab=96}:duplicate{dst=std{access=livehttp{seglen=10,splitanywhere=true,delsegs=true,numsegs=5,index=c:tempmystream.m3u8,index-url=http://mydomain.com/streaming/mystream-########.mp3},mux=raw,dst=c:tempmystream-########.mp3},select=audio}</nowiki>

[[User:Smowton|Smowton]] 03:23, 27 February 2012 (CET)

===Formats supported by the iOS=== See the [[iPhone]] article for a list
of supported codecs as well as
[http://developer.apple.com/iphone/library/documentation/networkinginternet/conceptual/streamingmediaguide/FrequentlyAskedQuestions/FrequentlyAskedQuestions.html
Apple's HTTP Live Streaming FAQ].

===Possible improvements/fixes===

from the developer: *Have the module auto-detect audio only streams, so
the splitanywhere option is not required.*\ I'm not sure I am doing the
right thing with the Win32 rename function. Linux allows me to rename a
file over an existing file, even if the existing file is in use. Win32
is not so friendly. This ability is useful for updating the index file
at same time it may be currently being read by the HTTP server serving
the files. \*Break the dst= and index= parameter into seperate
filename/directory entries, so you only need to specify the filename
format once. (instead of once for the dst= parameter, and once for the
index-url= parameter)

from the community: *Have the module detect the codecs used and warn the
end user if they are not compatible with the iPhone/iPod
Touch/iPad.*\ Possible multibitrate implementation that meets the iPhone
SDK specs so app developers can use VLC to host streams for their apps.

fixes: \*Audio only streams do not validate with Apple's
mediastreamvalidator. Audio streams are missing id3tags and timestamps.
Check with command, "mediastreamvalidator validate --timeout=60 [url]"

{{Documentation}}

[[Category:iOS]]
