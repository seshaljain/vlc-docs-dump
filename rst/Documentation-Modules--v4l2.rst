{{Moduletype=Access demuxos=Linux|description=Video for Linux 2 input}}

== Options ==

{{Option value=integer \|description=Caching in ms }}

=== Video input === {{Option value=string description=Primary device
name }} {{Option value=integer description=Video standard }} {{Option
value=string description=Force use of a specific video chroma (Use MJPG
here to use a webcam's MJPEG stream) }} {{Option value=integer
description=Card input to use for video }} {{Option value=integer
description=Card input to use for audio }} {{Option value=integer
description=IO method }} {{Option value=integer description=Prefered
video width (if non zero) }} {{Option value=integer description=Prefered
video height (if non zero) }} {{Option value=float description=Frames
per second (if non zero) }}

=== Audio input === These options do not apply to audio streams in
compressed data. {{Option value=string description=Audio input device }}
{{Option value=integer description=Allowed audio input methods (bitmask:
1 for OSS, 2 for ALSA) }} {{Option default=enabled name=v4l2-samplerate
default=48000 \|description=Audio input sample rate in Hz }}

=== Tuner === {{Option value=integer description=Tuner to use }}
{{Option value=integer description=Tuner frequency in Hz or MHz
depending on the underlying v4l2 driver }} {{Option value=integer
description=Tuner audio mode }}

=== Controls === These controls will be used only if they are supported
by the v4l2 driver. {{Option default=disabled name=v4l2-brightness
default=-1 name=v4l2-contrast default=-1 name=v4l2-saturation default=-1
name=v4l2-hue default=-1 name=v4l2-black-level default=-1
name=v4l2-auto-white-balance default=-1 name=v4l2-do-white-balance
default=-1 name=v4l2-red-balance default=-1 name=v4l2-blue-balance
default=-1 name=v4l2-gamma default=-1 name=v4l2-exposure default=-1
name=v4l2-autogain default=-1 name=v4l2-gain default=-1 name=v4l2-hflip
default=-1 name=v4l2-vflip default=-1 name=v4l2-hcenter default=-1
name=v4l2-vcenter default=-1 name=v4l2-audio-volume default=-1
name=v4l2-audio-balance default=-1 name=v4l2-audio-mute
description=Audio mute }} {{Option value=integer description=Audio bass
}} {{Option value=integer description=Audio treble }} {{Option
value=integer description=Audio loudness }} {{Option value=string
description=Set any other control listed in the debug output using a
comma seperated list in curly braces such as
{video_bitrate=6000000,audio_crc=0,stream_type=3} }}

== Example ==

Open a video device with default settings:
   % '''vlc v4l2:///dev/video0:width=640:height=480'''

Get information about a video device's capabilities:
   % '''vlc -vvv --color v4l2:///dev/video0 --run-time 1 vlc://quit -I
   dummy -V dummy -A dummy

Command line for Hauppauge PVR 250 to get France 2 (at ECP) and encode as MPEG2 and stream using UDP multicast:
   % '''vlc -I dummy -vvv
   'v4l2c://:audio-method=0:controls-reset:set-ctrls={video_bitrate_mode=1,video_bitrate=4000000,video_peak_bitrate=4000000}:width=720:height=576:tuner=0:tuner-frequency=478550'
   --sout "#std{access=udp{ttl=12},mux=ts,url=239.255.1.1}"'''

Note: v4l2c is an alias used to force VLC to use the v4l2 module in it's
Access variant without probing the Access Demux version first (the c
stands for compressed).

== Source code == \* {{VLCSourceFile|modules/access/v4l2/v4l2.c}}

== See also == \* [[Documentation:Modules/v4l]] \*
[[Documentation:Modules/dshow]]

{{Documentation footer}}

[[Category:GNU/Linux]]
