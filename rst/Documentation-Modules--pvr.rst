{{Moduletype=Accessos=Linuxsc=pvr}}

This module was removed with commitdiff {{CommitdiffV4L]] instead
{{Clear}}

== Options == The module did not accept <code>--pvr-frequency</code>
beyond the endpoints given by <code>static const int
pi_radio_range[2]</code>: <span class="nowrap"><code>65000 &le;
<var>x</var> &le; 108000</code></span>. This was not mentioned in the
help text.

The variables in <code>--pvr-norm</code> are defined in
{{VLCSourceFile|modules/access/v4l2/linux/videodev2.h}}.

{{Option value=string description=[[wikipedia:Personal video
recordername=pvr-radio-device default="/dev/radio0" name=pvr-norm
select={<var>V4L2_STD_UNKNOWN</var>,<var>V4L2_STD_SECAM</var>,<var>V4L2_STD_PAL</var>,<var>V4L2_STD_NTSC</var>}
description=Norm of the stream (Automatic, SECAM, [[PAL]], or [[NTSC]])
}} {{Option value=integer description=Width of the stream to capture (-1
for autodetection) }} {{Option value=integer description=Height of the
stream to capture (-1 for autodetection) }} {{Option value=integer
description=Frequency to capture (in kHz), if applicable }} {{Option
value=integer description=[[Framerate]] to capture, if applicable (-1
for autodetect) }} {{Option value=integer description=Interval between
[[keyframe]]s (-1 for autodetect) }} {{Option value=integer
description=If this option is set, [[B-Frame]]s will be used. Use this
option to set the number of B-Frames }} {{Option value=integer
description=[[Bitrate]] to use (-1 for default) }} {{Option
value=integer description=Peak bitrate in [[VBR]] mode }} {{Option
value=integer default=-1 name=pvr-audio-bitmask default=-1 Bitmask]]
that will get used by the audio part of the card }} {{Option
value=integer description=Audio volume (0-65535) }} {{Option
value=integer description=Channel of the card to use (Usually: 0 -
tuner, 1 - composite, 2 - svideo) }}

== Source code == \* {{VLCSourceFile|modules/access/pvr.c}}

{{Documentation}}
