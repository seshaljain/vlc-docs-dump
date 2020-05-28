{{docmodv4l}} and {{docmod|v4l2}} in VLC 1.0.0, but accesses were
provided as sub-modules. To emulate old behaviour, use
<code>--input-slave oss://</code> or <code>--input-slave alsa://</code>.

In the module options below <var>AOUT_CHANS_FRONT</var> and other
variables are defined in {{VLCSourceFile|include/vlc_es.h}}. The values
are not defined here because of their complexity.

Audio channels in VLC 2.0.1 must be configured manually (bugs) but
<code>--alsa-audio-channels</code> defaults to stereo.

The access module option <code>--alsa-format</code> has been deprecated
since VLC 2.1.0.

HDMI support is planned for VLC 4.0.0 through the
<code>--alsa-passthrough</code> option.

== Options == === Audio output === {{Moduletype=Audio
outputdescription=[[ALSA]] audio outputname=alsa-audio-device
default=default name=alsa-audio-channels
default=<var>AOUT_CHANS_FRONT</var> \|description=Channels available for
audio output. If the input has more channels than the output, it will be
down-mixed. This parameter is ignored when digital pass-through is
active }} {{Clear}}

=== Access === {{Moduletype=Accessos=Linuxsc=alsa}} {{Option
value=boolean description=Stereo }} {{Option value=integer
description=[[Sample rate]] (Hertz) \|select=192000, 176400, 96000,
88200, 48000, 44100, 32000, 22050, 24000, 16000, 11025, 8000, 4000 }}
{{Clear}}

== Source code == \* {{VLCSourceFilemodules/access/alsa.c}}

{{Documentation footer}}
