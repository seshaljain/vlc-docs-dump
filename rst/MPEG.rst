{{wikipedia|MPEG}} MPEG refers to a set of standards created by the
[http://www.chiariglione.org/about Moving Picture Experts Group]. MPEG
refers to several video, audio and [[container]] formats; see the full
list at the [[Codec]] page.

An MPEG file is a file using an MPEG container (these are called
''mpeg1'', ''ts'', ''ps'', and ''mp4'' for MPEG-4).

== Creating an MPEG File with VLC == To make an MPEG file, you need to:
\* Pick a container (see [[#Container_formats|below]]) \* Transcode the
audio and video to formats able to be held in the container: in general
this is the MPEG video and audio formats only. Check the
[https://www.videolan.org/streaming/features.html compatibility
information] in the official documentation, but be warned that while VLC
allows any codec and mux, most other players support only a few
combinations!

== <span id="MPEG-1"></span><span id="MPEG-2"></span> MPEG-1 and 2 ==
{{see alsoMPEG-1|MPEG-2}}

-  Muxer: '''ts''', '''ps''', '''mpeg1'''

MPEG-1 is a video and audio compression format, used in [[Video CD]]s.
It is compatible with a large number of software and hardware devices.

Here is an example of how to transcode an [[AVI]] into a portable MPEG-1 video from the [[command prompt]]
   {{%}} vlc ''file.avi'' --sout='#transcode{vcodec=mp1v,
   acodec=mpga}:std{access=file, mux=mpeg1,url=''file.mpg''}'

MPEG-2 is used in digital television and [[DVB]]. It is also used as the
format for [[DVD]]s. The biggest advantage of this format over MPEG-1 is
in its support for interlaced pictures; MPEG-2 can cleanly [[compress]]
[[interlaced]] video, while MPEG-1 internally only works on
progressive-scan video, so interlacing must be faked.

Here is an example of how to transcode an AVI into an MPEG-2 video from the [[command prompt]]
   {{%}} vlc ''file.avi'' --sout='#transcode{vcodec=mp2v,
   acodec=mpga}:std{access=file, mux=ps,url=''file.mpg''}'

=== Transcoding and Streaming ===

{{Bug|1965}} formerly required supplying a framerate of 25 in order to
[[transcode]] and stream an MPEG-1 or MPEG-2 payload.<br /> '''This has
been fixed since 2.0.0.'''

''HINT:'' Use an MPEG-TS (transport) stream container if you are
streaming MPEG through the network (see [[#Container formats|Container
Formats]]).

=== Video === {{codec videoid=mp2vid=mp4v}} {{codec video|id=h264}}
Codecs for MPEG-1 Video, MPEG-2 Video, MPEG-4 Video and H.264 Video
(MPEG-4 AVC).

=== Audio === {{codec audioinfo=MP2 audio.}} {{codec audioinfo=[[MP3]]
audio.}} {{codec audioinfo=[[AAC]] audio.}} Codecs for MPEG Layer 1/2
audio, MPEG Layer 3 audio and MPEG-4 AAC audio

=== Container formats === MPEG-2 specified 2 [[container]] formats, ts
and ps. Containers hold video and audio information in them, and package
them up so it can be sent over a network or stored on disk. \* '''ts'''
(Transport Stream) should be used to store or send data where data loss
will probably occur, such as over a network. \* '''ps''' (Program
Stream) should be used to store or send data where data loss is not
likely, such as on a DVD.

Both ps and ts can transport MPEG-4 Video, but only ts can send MPEG-4
Audio. In addition, MPEG-4 specifies its own container format, '''mp4'''
(see [[MPEG-4]])

==== <span id="TS"></span> TS, MPEG2 Transport Stream ====
{{muxencoder=y}}

===== Module options ===== {{Transcluded|Documentation:Modules/ts}}
{{:Documentation:Modules/ts}}

===== Accepted video codecs ===== \* [[mp1v]]: MPEG-1 video \* [[mpgv]]:
MPEG-1 or MPEG-2 video \* [[mp4v]]: MPEG-4 video (ASP) \* [[h264]]:
H.264, MPEG-4 AVC \* [[Dirac|drac]]: Dirac \* [[jpeg]] \* [[ms]]: MS
codecs (nonstandard?)

===== Accepted audio codecs ===== \* [[MP1]], [[MP2]], [[MP3]] \*
[[mp4a]]: MPEG-4 Audio (MP4) \* [[a52]] \* [[lpcm]] \* [[dts]]

===== Accepted subtitle codecs ===== \* [[spu]] \* [[subt]] \* [[telx]]

==== <span id="PS"></span> PS, aka MPEG Program Stream ====
{{muxencoder=y}}

===== Module options ===== {{Transcluded|Documentation:Modules/ps}}
{{:Documentation:Modules/ps}}

===== Accepted video codecs ===== \* [[mpgv]]: MPEG-1 or MPEG2 \*
[[mp4v]]: MPEG-4

===== Accepted audio codecs ===== \* [[mpga]]: MP1, MP2 or MP3 \*
[[mp4a]]: MPEG-4 (MP4) \* [[dts]] \* [[a52]] \* [[lpcm]]

===== Accepted subtitle codecs ===== \* [[spu]] \* [[ogt]] \* [[cvd]]

{{clear}}

== <span id="MPEG-3"></span> MPEG-3 == {{wikipedia|MPEG-3}} A largely
unused audio and video compression format. \* Note that the amazingly
common [[MP3]] audio files are actually '''MPEG-1 Layer 3''' audio, not
MPEG-3. {{clear}}

== MPEG-4 == {{See|MPEG-4}}

== Source code == {{fileoutput muxer}} {{fileinput demuxer}} {{fileinput
demuxer}} {{fileinput demuxer}}

== Further reading == \*
[https://sound.media.mit.edu/resources/mpeg4/audio/ sound.media.mit.edu
- The MPEG Audio Web Page]
