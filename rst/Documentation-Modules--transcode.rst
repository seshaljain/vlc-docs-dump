{{Stub}} {{Moduletype=Stream outputdescription=[[Transcode]] content on
the fly}}

The only shortcut to this module is <code>transcode</code>.

== Options == Note: Since [[supported]] codecs are dynamically assigned
by the running program, <code>sout-transcode-venc</code>,
<code>sout-transcode-aenc</code> and <code>sout-transcode-senc</code>
have been left blank.

Looking at the source code for 4.0.0-dev it seems no checks are directly
performed limiting <code>sout-transcode-samplerate</code> beyond <code>0
<= samplerate <= 48000</code>.

As of 2.2.0 <code>sout-transcode-fps</code> accepts fps as rationals
e.g. <code>30000/1001</code>.

Deprecated options: \* <code>hurry-up</code> (since 2.2.0),
<code>sout-transcode-high-priority</code> seems to be equivalent \*
<code>audio-sync</code> (since 2.2.0)

=== Video === {{Option value=string description=This is the video
encoder module that will be used (and its associated options) }}
{{Option value=string description=This is the video codec that will be
used }} {{Option value=integer description=Target bitrate of the
transcoded video stream }} {{Option value=float description=Scale factor
to apply to the video while transcoding (eg: 0.25) }} {{Option
value=string description=Target output frame rate for the video stream
}} {{Option value=boolean default=disabled }} {{Option value=string
select={deinterlace,ffmpeg-deinterlace} name=sout-transcode-width
default=0 name=sout-transcode-height default=0
name=sout-transcode-maxwidth default=0 name=sout-transcode-maxheight
default=0 name=sout-transcode-vfilter description=Video filters will be
applied to the video streams (after overlays are applied). You can enter
a colon-separated list of filters }}

=== Audio === {{Option value=string description=This is the audio
encoder module that will be used (and its associated options) }}
{{Option value=string description=This is the audio codec that will be
used }} {{Option value=integer description=Target bitrate of the
transcoded audio stream }} {{Option value=string description=This is the
language of the audio stream }} {{Option value=integer min=0
description=Number of audio channels in the transcoded streams }}
{{Option value=integer min=0 description=Sample rate of the transcoded
audio stream (11250, 22500, 44100 or 48000) }} {{Option value=string
\|description=Audio filters will be applied to the audio streams (after
conversion filters are applied). You can enter a colon-separated list of
filters }}

=== Overlays/Subtitles === {{Option value=string description=This is the
subtitle encoder module that will be used (and its associated options)
}} {{Option value=string description=This is the subtitle codec that
will be used }} {{Option value=boolean description=This is the subtitle
codec that will be used }} {{Option value=string \|description=This
allows you to add overlays (also known as "subpictures") on the
transcoded video stream. The subpictures produced by the filters will be
overlayed directly onto the video. You can specify a colon-separated
list of subpicture modules }}

=== Miscellaneous === {{Option value=integer min=1 description=Number of
threads used for the transcoding }} {{Option value=integer min=1
description=Defines how many pictures we allow to be in pool between
decoder/encoder threads when threads > 0 }} {{Option default=disabled
description=Runs the optional encoder thread at the OUTPUT priority
instead of VIDEO }}

== Source code == \*
{{VLCSourceFile|modules/stream_out/transcode/transcode.c}}

{{Documentation}}

[[Category:Transcoding]]
