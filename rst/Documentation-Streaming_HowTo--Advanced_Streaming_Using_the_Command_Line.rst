{{See alsodocumentation streaming howto toc}}

<!-- TODO :

   Update all this Improve texts Video Filters update of syntax other
   modules ? gather

-->

== Structure of stream output == Stream output is the name of the
feature of {{VLC}} that allows to output any stream read by VLC to a
file or as a network stream instead of displaying it. Different kind of
processing can be applied to the stream during this process
(transcoding, re-scaling, filters, re-muxing…). Stream output includes
different modules, each of them having different capabilities. You can
''chain'' modules to enhance the possibilities.

Here is the list of the modules currently available : \*
'''{{docmodtranscode}}''' is used to [[transcode]] (decode and re-encode
the stream using a different [[codec]] and/or [[bitrate]]) the audio and
the video of the input stream. If the input or output access method
doesn't allow pace control (network, capture devices), this will be done
"[[wiktionary:on the flyduplicate}}''' allows you to create a second
chain, where the stream will be handled in an independent way. \*
'''{{docmodes}}''' allows you to make separate [[Elementary Stream]]s
(ES) out of an input stream. This can be used to save audio and video
streams to separate files, for instance. \* '''{{docmodbridge-in}}'''
TODO \* '''{{docmod|mosaic-bridge}}''' TODO

Each of these modules may take options. Here is the syntax that you must use :
   {{%}} '''vlc input_stream --sout
   "#module1{option1=parameter1{parameter-option1},option2=parameter2}:module2{option1=…,option2=…}:…"'''

{{Note|Some of the module options (option1 in the example) have to be
set, others are optional. Option parameters (parameter-option1 in the
example) are always optional. These option parameters are also often
very advanced settings. If you don't understand their description, this
certainly means that you don't need them.}}

You may also use the following syntax :
   {{%}} '''vlc input_stream --sout-module1-option1=…
   --sout-module1-option2=… --sout-module2-option1=…
   --sout-module2-option2=… …'''

For example, to transcode a stream and send it, use :
   {{%}} '''vlc input_stream --sout
   '#transcode{options}:standard{options}' '''

In the following documentation, single bullet points represent options
and double bullet points represent item options (sub-options) : \*
<code>--module=option</code> \*\*
<code>--module=option{item-option="value"}</code>

== Description of the modules == === standard (alias std) === This
module saves the stream to a file or sends it over a network, after
having [[mux]]ed it.

The available options are :

==== access ==== This option allows to set the medium used to save or
send the stream. This is a compulsory option. Available options are : \*
'''file''': saves the stream to a file. Use the ''append'' option to
append the stream to an existing file instead of replacing it :
standard{ … ,'''access=file{append}''', … } \* '''udp''': streams to a
[[UDP]] unicast or [[multicast]] address. \*\* '''caching=<time in
ms>''' to set the time VLC should buffer data before sending it; \*\*
'''ttl=<ttl>''' to set the [[TTL]] of the sent UDP packets; \*\*
'''group=<amount of packets>''' to sent packets by burst instead of one
by one; \*\* '''late=<time in ms>''' to drop packets that arrive too
late at this stage of the chain; \*\* '''raw''' if you don't want to
wait until the [[MTU]] is filled before sending the packet. \*
'''http''': streams over [[HTTP]]. \*\* '''user=<user name>''' to enable
HTTP basic authentication and set the user; \*\* '''pwd=<password>''' to
set the basic authentication password; \*\* '''mime=<mime type>''' to
set the mime type returned by the server. \* '''https''': streams over
HTTP, using a secured [[SSL/TLS]] connection. \*\* (same as for http
option) \*\* '''cert=<path to certificate>'''to set the certificate to
use; \*\* '''key=<path to key>''' to set the private key file the server
should use for the TLS connection; \*\* '''ca=<path to certificate>'''
to set the path to the root CA certificates to use for TLS; \*\*
'''crl=<path to certificate>''' to set the revocation certificate to use
for the TLS connection. \* '''mmsh''': streams using the Microsoft
[[MMS]] protocol. This protocol is used as transport method by many
Microsoft applications. Note that only a small part of the MMS protocol
is supported ([[MMSH|MMS encapsulated in HTTP]]). \*\* (same as for http
module) \* '''rtp''': streams over [[RTP]]. This can only be used to
stream [[MPEG-TS]] over plain RTP. Support for this option has been
removed in VLC 0.9.0 and later. You should use the '''rtp''' stream
output module instead. \*\* (same as for the '''udp''' setting)

==== mux ==== This option allows you to set the encapsulation method
used for the resulting stream. This option has to be set.

Available options are : \* '''ts''': the [[MPEG-TS]] muxer. This the
standard muxer used to stream [[MPEG-2]]. This muxer can be used with
any '''access''' method. Supported codecs are MPEG 1/2/4, [[MJPEG]],
[[H263]], [[H264]], I263, [[WMV]] 1/2 and [[Theora]] for video, MPEG
audio, [[AAC]] and [[a52]] for the audio stream. \*\*
'''pid-video=<pid>''' to set the PID of the video track; \*\*
'''pid-audio=<pid>''' to set the PID of the audio track; \*\*
'''pid-spu=<pid>''' to set the PID of the subtitle track; \*\*
'''pid-pmt=<pid>''' to set the PID of the PMT (Program Map Table); \*\*
'''tsid=<id>''' to set the ID of the resulting [[TS]] stream; \*\*
'''shaping=<shaping delay in ms>''' to set the minimum interval during
which the bitrate of the stream will remain constant, for variable
bitrate streams; \*\* '''use-key-frames''' uses [[I-frame]]s as limits
for the shaping intervals; \*\* '''pcr=<PCR interval in ms>''' allows to
set at which interval Program Clock References will be sent; \*\*
'''dts-delay=<delay in ms>''' allows to delay PTS (Presentation Time
Stamps) from the DTS (Decoding Time Stamp) from the given time; \*\*
'''crypt-audio''' allows to enable encryption of the audio track using
the CSA algorithm; \*\* '''csa-ck=<key as a 16 character word>''' allows
to set the key used for CSA encryption. \* '''ps''': the [[MPEG-PS]]
muxer. This the standard muxer for MPEG 2 files (.mpg). It can be used
with the file and http output methods. Supported codecs are MPEG 1/2 and
MJPEG for video, MPEG audio and a52 for audio streams. \*\*
'''dst-delay=<delay in ms>''': It allows to delay PTS (Presentation Time
Stamps) from the DTS (Decoding Time Stamp) from the given time. \*
'''mpeg1''': the standard MPEG 1 muxer. This muxer should be used
instead of ps with MPEG 1 video streams, when saved to a file or
streamed over HTTP. Supported codecs are MPEG 1 and MPEG audio. \*\*
(same as for the PS muxer) \* '''ogg''': the [[ogg]] muxer. This is the
muxer from the Xiph project. It can be used with the HTTP and file
output methods. Supported codecs are MPEG 1/2/4, MJPEG WMV 1/2 and
[[Theora]], audio streams can be vorbis, [[flac]], [[speex]], [[a52]] or
MPEG audio. \*\* (none) \* '''asf''': the Microsoft [[ASF]] muxer. This
is the standard muxer used for streaming by Microsoft applications. Is
also used as container for [[WMA]] audio files. This muxer can be used
with the file and HTTP output methods. Supported codecs are [[MPEG-4]],
MJPEG, [[WMV]] 1/2 for video, MPEG audio, and a52 for audio streams.
\*\* '''title=<title>'''; \*\* '''autor=<author>'''; \*\*
'''copyright=<copyright message>'''; \*\* '''comment=<comments>'''; \*\*
'''rating=<rating>''' allow you to set what will be displayed in the
according field of the stream comments. \* '''asfh''': this is a special
version of the ASF muxer, that should be used for MMSH streaming. MMSH
is the only supported output method. Supported codecs are the same as
for ASF. \*\* (same as for ASF) \* '''avi''': the Microsoft [[AVI]]
muxer. This is very common encapsulation format for [[MPEG-4]] files.
The only supported output method is file. Supported codecs are MPEG
1/2/4, H263, H264 and I263 for video, MPEG audio and a52 for audio
streams. \*\* (none) {{Notemultipart jpeg muxer]]. This encapsulation
format is mostly used on surveillance video cameras with an integrated
web server. Such streams are usually embedded in web pages and seen with
standard Internet browsers, as they are seen as a succession of jpeg
images. The only supported output method is HTTP. The only usable codec
is [[MJPEG]]. No sound track can be muxed in such streams. \*\* (none)

==== dst ==== This option allows to give various information about the
location where the stream should actually be saved or sent.

Here is the meaning of the '''dst''' option depending on the parameter
used for the '''access''' option: \* If the '''file''' output method is
used, '''dst''' is the path where the file should be saved. \* If the
'''udp''' or '''rtp''' output method is used, '''dst''' is the unicast
or multicast destination address&nbsp;&ndash; and,
optionally&nbsp;&ndash; UDP port, in the form '''address:port'''. \* If
the '''http''', '''https''' or '''mmsh''' output method is chosen,
'''dst''' is the address, port and path of the local network interface
on which the server should listen for requests. If no address is given,
VLC will listen on all the network interfaces. These bits of information
have to be supplied using the '''address:port/path''' syntax.

==== sap ==== Use this option if you want VLC to send [[SAP]] (Session
Announcement Protocol) announces. SAP is a service discovery protocol,
that uses a special [[multicast]] address to send a list of available
streams on a server.

This option can only be enabled with the '''udp''' output method.

==== group ==== This option allows to specify the name of an optional
'''group''' of streams. A VLC used as a client will use this field to
classify the stream.

This option uses a private extension of the SAP protocol. VLC will be
the only client able to read this field.

This option can only be used if the '''sap''' option has been enabled.

==== sap-ipv6 ==== Use this option if you want the SAP announces to be
sent using the '''IPv6''' protocol instead of '''IPv4'''.

This option can only be used if the '''sap''' option has been enabled.

==== slp ==== SLP stands for ''Service Location Protocol''. It is an
alternative to SAP for session announcement. Use this option if you want
to send such announcements.

==== name ==== Use this option to specify the name of the stream that
will be sent in SAP and SLP announcements.

This option can only be used if the '''sap''' or '''slp''' option has
been enabled.

=== display === This module can be used to display the stream. This is
particularly useful in a '''{{docmod|duplicate}}''' chain, in order to
monitor a stream while it is being saved or streamed.

Available options are :

==== novideo ==== You can use this option to disable video in the
displayed stream.

==== noaudio ==== You can use this option to disable audio in the
displayed stream.

==== delay ==== You can use this option to introduce a delay in the
display of the stream. Delay has to be given in ms (milliseconds).

=== rtp === This module can be used to send a stream using the ''[[RTP]]
(Real Time Protocol)'' protocol (see RFC 3550).

Although use of ''[[RTSP]]'' is possible using this module, it won't
allow you to make ''Video On Demand''. Please have a look at the
description of the VLM module for that.

The different available options are :

==== dst ==== This option allows the destination UDP address to be
given. This can be the address of a host or a multicast group. This
option has to be given, unless the ''sdp=rtsp://''option is given
([[#sdp|see below]]). In the latter case, the stream will be sent to the
host doing the ''RTSP'' request.

==== port ==== This option allows to set the UDP [[port]] used to send
the first ''elementary stream''. This port has to be even. Other streams
will be streamed using even ports directly above this one.

==== port-video ==== This option allows to set the UDP port used to send
the first video ''elementary stream''. This port has to be even.

==== port-audio ==== This option allows to set the UDP port used to send
the first audio ''elementary stream''. This port has to be even.

==== sdp ==== This option allows to set the way the [[SDP]] (Session
Description Protocol) file corresponding the the stream should be made
available. Options are : \* '''file://\ <path to the file>''', to export
the SDP as a local file. \* '''<nowiki>http://\ <local interface
IP:port/path></nowiki>''', to make the file available using the
integrated HTTP server of VLC. {{NoteThe ''local interface IP'' argument
is optional. If not given, VLC will listen on all available
interfaces.}} \* '''sap''', to export the SDP using the [[SAP]] (Session
Announcement Protocol, see RFC 2974).

==== ttl ==== This option can be used to set the ''[[TTL]]'' (Time to
Live) of the sent UDP packets.

==== mux ==== This option allows to set the encapsulation method used to
send the stream. See '''mux''' options of the
'''[[#standard|standard]]''' module for a description of the available
method.

Only '''ts''' is possible for [[RTP]] streams. By default, each
elementary stream is sent as a separate RTP medium, i.e. no
encapsulation is done.

==== rtcp-mux ==== This option enables RTP/RTCP [[multiplex]]ing (see
draft-ietf-avt-rtp-and-rtcp-mux), i.e. sends and receives [[RTCP]]
packets on the same port numbers as RTP packets.

By default, RTCP packets are sent and received on the next port.

==== proto ==== This selects the transport protocol to carry [[RTP]]
packets.

Possible values include : \* '''dccp''', accept incoming [[DCCP]]
connections at the specified IP address (dst=), \* '''sctp''', accept
[[SCTP]] connections at the specified IP address (dst=), ''not
implemented yet'', \* '''tcp''', accept [[TCP]] connections at the
specified IP address (dst=) and use RFC 4571 RTP framing, ''not
implemented yet,'' \* '''udp''', send [[UDP]] packets to the specified
destination (either [[unicast]] or [[multicast]]); this is the default
value, \* '''udplite''', send [[UDP-Lite]] packets to the specified
destination (either unicast or multicast).

This options uses UDP-Lite instead of UDP as the transport protocol for
RTP and RTCP packets.

==== name ==== This option can be used to set the name that will be
displayed on the client receiving the stream.

==== description ==== This option can be used to give an additional
description of the stream.

==== url ==== This option allows to give the address of a website with
additional information about the stream.

==== email ==== This option allows to give a contact e-mail address.

=== es === The '''{{docmod|es}}''' module can be used to separate the
different ''elementary streams'' from a stream, and save each of them in
a different file or send it to a separate destination.

The available parameters are :

==== access-video ==== Use this option to set the medium used to save or
send the video ''elementary streams''. Possible values and item options
are the same as for the '''access''' option of the '''standard''' module
([[#standard|see above]]).

==== access-audio ==== Use this option to set the medium used to save or
send the audio ''elementary streams''. Possible values and item options
are the same than for the '''access''' option of the '''standard'''
module ([[#standard|see above]]).

==== access ==== This option can be used instead of both
'''access-video''' and '''access-audio''' options, when they share the
same setting.

==== mux-video ==== Use this option to set the encapsulation method used
for the video ''elementary streams''. Possible values and item options
are the same as for the '''mux''' option of the '''standard''' module
([[#standard|see above]]).

==== mux-audio ==== Use this option to set the encapsulation method used
for the audio ''elementary streams''. Possible values and item options
are the same than for the '''mux''' option of the '''standard''' module
([[#standard|see above]]).

==== mux ==== This option can be used instead of both '''mux-video'''
and '''mux-audio''' options, when they share the same setting.

==== dst-video ==== Use this option to set the location where the video
''elementary streams'' should be saved, sent, or made available. The
exact meaning of this option depends on the value of the
'''access-video''' option and is the same as for the '''url''' option of
the '''standard''' module ([[#standard|see above]]).

{{Note|If you use the ''%n'' string in the url field, VLC will replace
it by the number of the audio or video track considered. The ''%c''
string will be replaced by the name ([[FourCC]]) of the codec of the
track. ''%a'' prints the access output used and ''%m'' the muxer used.}}

==== dst-audio ==== Use this option to set the location where the audio
''elementary streams'' should be saved, sent, or made available. The
exact meaning of this option depends on the value of the
'''access-audio''' option and is the same as for the '''url''' option of
the '''standard''' module ([[#standard|see above]]).

{{Note|If you use the ''%n'' string in the url field, VLC will replace
it by the number of the audio or video track considered. The ''%c''
string will be replaced by the name ([[FourCC]]) of the codec of the
track. ''%a'' prints the access output used and ''%m'' the muxer used.}}

==== dst ==== This option can be used instead of both '''dst-video'''
and '''dst-audio''' options, when they share the same setting.

=== transcode === You can use this module to transcode a stream, e.g.,
to change its codecs or the encoding bitrates. Some additional
processing can be done during this process, such as re-scaling,
deinterlacing, resampling, etc.

{{Note|Depending on the bitrate of the original stream and of the
options chosen, transcoding can be a very CPU-intensive task. As a
consequence, streaming of a real-time transcoded stream can lead to
dropped frames or a jerky image and sound in some cases, when running
out of resources.}}

Available options are :

==== vcodec ==== This option allows to specify the codec the video
tracks of the input stream should be transcoded to.

List of available codecs can be found on the
[https://www.videolan.org/streaming/features.html streaming features
page].

==== vb ==== This option allows to set the [[bitrate]] of the transcoded
video stream, in kbit/s.

==== venc ==== This allows to set the encoder to use to encode the
videos stream. Available options are: \* '''ffmpeg''': this is the
[[libavcodec]] encoding module. It handles a large variety of different
codecs (the list can be found on the
[https://www.videolan.org/streaming/features.html streaming features
page]. \*\* '''keyint=<number of frames>''' allows to set the maximal
amount of frames between 2 key frames; \*\* '''hurry-up''' allows the
encoder to decrease the quality of the stream if the CPU can't keep up
with the encoding rate; \*\* '''interlace''' allows to improve the
quality of the encoding of interlaced streams; \*\*
'''noise-reduction=<noise reduction factor>''' enables a noise reduction
algorithm (will decrease required bitrate at the cost of details in the
image); \*\* '''vt=<bitrate tolerance in kbit/s>''' allows to set a
tolerance for the bitrate of the output video stream; \*\*
'''bframes=<amount of frames>''' allows to set the amount of
[[B-frame]]s between 2 key frames; \*\* '''qmin=<quantizer>''' allows to
set the minimum quantizer scale; \*\* '''qmax=<quantizer>''' allows to
set the maximum quantizer scale; \*\* '''qscale=<quantizer scale>'''
allows to specify a fixed quantizer scale for VBR encodings; \*\*
'''i-quant-factor=<quantization factor>''' allows to set the
quantization factor of [[I-frame]]s, compared to [[P-frame]]s; \*\*
'''hq=<quality>''' allows to choose the quality level for the encoding
of the motion vectors (arguments are simple, rd or bits, default is
simple *FIXME*); \*\* '''strict=<level of compliance>''' allows to force
a stricter standard compliance (possible values are -1, 0 and 1, default
is 0); \*\* '''strict-rc''' enables a strict rate control algorithm;
\*\* '''rc-buffer-size=<size of the buffer in bits>''' allows to choose
the size of the buffer used for rate control (bigger means more
efficient rate control); \*\* '''rc-buffer-aggressivity=<float
representing the aggressiveness>''' allows to set the rate control
buffer aggressiveness *FIXME*; \*\* '''pre-me''' allows to enable pre
motion estimation; \*\* '''mpeg4-matrix''' enable use of the MPEG4
quantization matrix with MPEG2 streams, improving quality while keeping
compatibility with MPEG2 decoders; \*\* '''trellis''' enables trellis
quantization (better quality, but slower processing). \* '''theora''':
The Xiph.org [[Theora]] encoder. The module is used to produce theora
streams. Theora is a free patent and royalties-free video codec. \*\*
'''quality=<quality level>'''. This option allows to create a VBR
stream, overriding '''vb''' setting. the quality level must be an
integer between 1 and 10. Higher is better. \* '''x264'''. [[x264]] is a
free open-source [[h264]] encoder. h264 (or MPEG4-AVC) is a recent
high-quality video codec. \*\* '''keyint=<number of frames>''' allows to
set the maximal amount of frames between 2 key frames; \*\*
'''idrint=<number of frames>''' allows to set the maximal amount of
frames between 2 IDR frames; \*\* '''bframes=<amount of frames>'''
allows to set the amount of B-frames between an I and a P frame; \*\*
'''qp=<quantizer parameter>''' allows to specify a fixed quantizer
(between 1 and 51); \*\* '''qp-max=<quantizer parameter>''' allows to
set the maximum value for the quantizer; \*\* '''qp-min=<quantizer
parameter>''' allows to set the minimum value for the quantizer; \*\*
'''cabac''' enables the <abbr title="Context-Adaptive Binary Arithmetic
Coding">CABAC</abbr> algorithm (slower, but enhances quality); \*\*
'''loopfilter''' enables [[deblocking]] loop filter; \*\* '''analyse'''
enables the analyze mode; \*\* '''frameref=<amount of frames>''' allows
to set the number of previous frames used as predictors; \*\*
'''scenecut=<sensibility>''' allows to control how aggressively the
encoder should insert extra I-frame, on scene change.

==== fps ==== This option allows to set the [[framerate]] of the
transcoded video, in frames per second; reducing the framerate of a
video can help decrease its bitrate.

==== deinterlace ==== This option allows to enable [[deinterlacing]] of
interlaced video streams before encoding.

==== croptop ==== This option allows to crop the upper part of the
source video while transcoding. The argument is the number of lines the
video should be cropped.

==== cropbottom ==== This option allows to crop the lower part of the
source video. The argument is the Y coordinate of the first line to be
cropped.

==== cropleft ==== This option allows to crop the left part of the
source video while transcoding. The argument is the number of columns
the video should be cropped.

==== cropright ==== This option allows to crop the right part of the
source video. The argument is the X coordinate of the first column to be
cropped.

==== scale ==== This option allows the give the ratio from which the
video should be rescaled while being transcoded. This option can be
particularly useful to help reduce the bitrate of a stream.

==== width ==== This option allows you to give the width of the
transcoded video, in pixels.

==== height ==== This option allows you to give the height of the
transcoded video, in pixels.

==== acodec ==== This option allows you to specify the codec the audio
tracks of the input stream should be transcoded to.

List of available codecs can be found on the
[https://www.videolan.org/streaming/features.html streaming features
page].

==== ab ==== This option allows to set the bitrate of the transcoded
audio stream, in kbit/s.

==== aenc ==== This allows to set the encoder to use to encode the audio
stream. Available options are : \* '''ffmpeg''': this is the
[[libavcodec]] encoding module. It handles a large variety of different
codecs (the list can be found on the
[https://www.videolan.org/streaming/features.html streaming features
page]). \* '''vorbis'''. This module uses the [[vorbis]] encoder from
the [[Xiph.org]] project. Vorbis is a free, open, license-free lossy
audio codec. \*\* '''quality=<quality level>''' allows to use [[VBR]]
(variable bitrate) encoding instead of the default [[CBR]] (constant
bitrate), and to set the quality level (between 1 and 10, higher is
better); \*\* '''max-bitrate=<bitrate in kbit/s>''' allows to set the
maximum bitrate, for vbr encoding; \*\* '''min-bitrate=<bitrate in
kbit/s>''' allows to set the minimum bitrate, for vbr encoding; \*\*
'''cbr''' allows to force cbr encoding. \* '''speex'''. This module uses
the [[speex]] encoder from the Xiph.org project. Speex is a lossy audio
codec, best fit for very low bitrates (around 10 kbit/s) and
particularly video conferences.

==== samplerate ==== This option allows to set the [[sample rate]] of
the transcoded audio stream, in Hz. Reducing the sample rate is a way to
lower the bitrate of the resulting audio stream.

==== channels ==== This option allows to set the number of channels of
the resulting audio stream. This is useful for codecs that don't have
support for more than 2 channels, or to lower the bitrate of an audio
stream.

==== scodec ==== This option allows to specify subtitle format the
subtitles tracks of the input stream should be converted to.

List of available codecs can be found on the
[https://www.videolan.org/streaming/features.html streaming features
page].

==== senc ==== This allows to set the converter to use to encode the
subtitle stream.

The only subtitle encoder we have at this time is '''dvbsub'''.

==== soverlay ==== This option allows rendering subtitles directly on
the video, while transcoding it.

Do not confuse this option with senc/scodec that transcode the subtitles
and stream them.

==== sfilter ==== This option allows to render some images generated by
a so-called ''subpicture filter'' (e.g. a logo, a text string, etc.) on
top of the video.

The list of available ''subpicture filters'' can be found on the [https://www.videolan.org/streaming/features.html streaming features page]. The Item options of this modules can be found using the following command line :
   {{%}} '''vlc -p --advanced <module name>'''

==== threads ==== This option allows to set the number of computer
processing threads that should be used to encode the streams. Increasing
this number to the amount of processors on the computer (or twice this
number on Intel P4 HT processors) should improve transcoding
performance.

==== vfilter ==== Uses video filter during transcode process. Parameters
of vfilter can be found on the [[Documentation:Advanced Use of
VLC#Filters|Advanced Use of VLC Filters]].

The example
   '''vlc input_file
   --sout="#transcode{vfilter=adjust{gamma=1.5},vcodec=theo,vb=2000,scale=0.67,acodec=vorb,ab=128,channels=2}:standard{access=file,mux=ogg,dst="output_file.ogg"}"
   '''

will adjust ''input_file'' gamma to 1.5, resize the video size
(resolution) by 0.67 (e.g. 1080x720 to 720x480), convert video using the
Theora codec with bitrate @ 2000 kb/s and audio using the Vorbis codec
with bitrate @ 128 kb/s, encapsulate the video and audio to an Ogg
container and save it to ''output_file.ogg''.

=== duplicate === This module can be used to duplicate the stream, and
so process it through several different chains.

Available options are :

==== dst ==== This option allows to give the chain through which the
duplicated stream should be processed.

{{Note|'''dst''' options have to be used in the same duplicate block to
actually duplicate the stream. Any of the stream output module described
earlier can be used as parameter of this option.}}

==== select ==== This options can be used to duplicate only a part
''elementary streams'' of a complete stream.

Several criteria can be given, by separating each of them with a
comma.<br /> For criteria that need a parameter, such as '''es''' and
'''program''', you can also specify a range, using the syntax
'''criteria=num_start-num_end'''.

Available parameters are : \* '''program=''': duplicate only
''elementary streams'' belonging to the selected program (or SID). This
option only works with [[MPEG-TS]] streams. \* '''noprogram=''': do not
duplicate ''elementary streams'' belonging to the selected program (or
PID). This option only works with MPEG-TS streams. \* '''es=''':
duplicate only the ''elementary stream'' with the selected id. \*
'''noes=''': do not duplicate the ''elementary stream'' with the
selected id. \* '''video''': duplicate only video ''elementary
streams''. \* '''novideo''': do not duplicate video ''elementary
streams''. \* '''audio''': duplicate only audio ''elementary streams''.
\* '''noaudio''': do not duplicate audio ''elementary streams''. \*
'''spu''': duplicate only subtitle ''elementary streams''. \*
'''nospu''': do not duplicate subtitle ''elementary streams''.

Example :
   #duplicate{dst=std{…},select="program=100-200,novideo"}

This ''duplicate'' chain will only output the non video ''elementary
streams'' belonging to the programs which PID are between 100 and 200.

=== Miscellaneous === Here are a few additional global options : \*
'''--sout-all''', '''--no-sout-all''': Enable streaming of all ES
(default enabled). If disabled VLC will only stream one audio ES and one
video ES (the first ones). If sout-all remains enabled, all ES (audio,
video and SPU) will be streamed. \* '''--sout-keep''',
'''--no-sout-keep''': Keep sout open (default disabled) : use the same
sout instance across the various playlist items, if possible. \*
'''--no-sout-audio''': This option disables audio in the output stream.
\* '''--no-sout-video''': This option disables video in the output
stream.

=== Simplified Syntax === The stream output also offers a simplified
syntax, with which you can only you use the '''[[#standard|standard]]'''
module's main options : {{%}} '''vlc input_stream --sout
access/mux://url''' where '''access''', '''mux''' and '''url''' are as
defined in the options of the '''standard''' module.

== Examples == To fully understand the complex syntax of VLC's stream
output, please look at the examples in the next section.

{{Documentation}}
