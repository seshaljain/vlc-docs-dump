{{Moduletype=Access demuxos=WindowsDirectShow]] input}}

== Options == {{Option value=string description=Name of the video device
that will be used by the DirectShow plugin. If you don't specify
anything, the default device will be used }} {{Option value=string
description=Name of the audio device that will be used by the DirectShow
plugin. If you don't specify anything, the default device will be used
}} {{Option value=string description=Size of the video that will be
displayed by the DirectShow plugin. If you don't specify anything the
default size for your device will be used. You can specify a standard
size (cif, d1, ...) or <width>x<height> }} {{Option value=string
description=Define input picture [[aspect ratio]] to use. Default is 4:3
}} {{Option value=string description=Force the DirectShow video input to
use a specific chroma format (eg. [[I420]] (default), RV24, etc.) }}
{{Option value=float description=Force the DirectShow video input to use
a specific [[frame rate]] (eg. 0 means default, 25, 29.97, 50, 59.94,
etc.) }} {{Option value=boolean description=Show the properties dialog
of the selected device before starting the stream }} {{Option
value=boolean description=Show the tuner properties [channel selection]
page }} {{Option value=integer description=Set the TV channel the tuner
will set to (0 means default) }} {{Option value=integer description=Set
the tuner country code that establishes the current channel-to-frequency
mapping (0 means default) }} {{Option value=integer select={0,1,2}
name=dshow-video-input default=-1 name=dshow-video-output default=-1
name=dshow-audio-input default=-1 name=dshow-audio-output default=-1
name=dshow-amtuner-mode default=<var>AMTUNER_MODE_TV</var>
description=AM Tuner mode. Can be one of Default (0), TV (1), AM Radio
(2), FM Radio (3) or DSS (4) }} {{Option value=integer
description=Select audio input format with the given number of audio
channels (if non 0) }} {{Option value=integer description=Select audio
input format with the given [[sample rate]] (if non 0) }} {{Option
value=integer description=Select audio input format with the given
bits/sample (if non 0) }}

== Source code == \* {{VLCSourceFilemodules/access/dshow}}

{{Documentation footer}}
