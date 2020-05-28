oss and {{docmodv4l}} and {{docmod|v4l2}} in VLC 1.0.0, but accesses
were provided as sub-modules. To emulate old behaviour, use
<code>--input-slave oss://</code> or <code>--input-slave alsa://</code>.
The access module reads from <code>/dev/dsp</code>.

== Options == === Audio output === {{Moduletype=Audio
outputdescription=[[OSSsc=none}} {{Option value=string description=OSS
device node path }} {{Option value=boolean description=S/PDIF can be
used by default when your hardware supports it as well as the audio
stream being played }} {{Clear}}

=== Access === {{Moduletype=Accessos=Linuxsc=oss}} {{Option
value=boolean description=Capture the audio stream in stereo }} {{Option
value=integer description=[[Sample rate]] of the captured audio stream,
in Hz (eg: 11025, 22050, 44100, 48000) }} {{Clear}}

== Source code == \* {{VLCSourceFilemodules/access/oss.c}}

{{Documentation footer}}
