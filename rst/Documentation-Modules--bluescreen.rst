{{Mosaic framework}} {{Moduletype=Video filterdescription=Change the
video's alpha channel|sc=bluescreen}}

This filter can be used in the mosaic framework to set a video's alpha
channel (or transparency) based on a pixel's color. This is also known
as [[wikipedia:green screen|green screen]] or chroma key blending and
can be used to create effects like on most weather channels.

== Options == {{Option value=integer max=255 description=U chroma
component. }} {{Option value=integer max=255 description=V chroma
component. }} {{Option value=integer max=255 description=Tolerance of
the bluescreen blender on color variations for the U plane. A value
between 10 and 20 seems sensible. }} {{Option value=integer max=255
description=Tolerance of the bluescreen blender on color variations for
the V plane. A value between 10 and 20 seems sensible. }}

== Example ==
   % '''vlc -vvv --vlm-conf mosaic.vlm --mosaic-keep-picture
   --sub-filter mosaic'''

And the vlm config:

   new channel0 broadcast enabled setup channel0 input rushfondvert.avi
   setup channel0 output
   #duplicate{dst=mosaic-bridge{chroma=YUVA,vfilter=bluescreen},select=video}

   new background broadcast enabled setup background input
   redefined-nintendo.mpg control background play

   control channel0 play

Have a look at
[https://web.archive.org/web/20060819104251/http://people.videolan.org/~dionoea/bluescreen2.mpg
people.videolan.org/~dionoea/bluescreen2.mpg (archived)] for an example
of the VLC bluescreen filter. The overlay video is
[https://web.archive.org/web/20061205222657/http://people.videolan.org/~dionoea/rushfondvert.avi
rushfondvert.avi (archived)] and features someone with a mask in front
of a green background. The bluescreen module's default values are
adjusted to remove the background from this video. For other videos you
should use your favorite color editing tool to find out the appropriate
U and V values.

== Another example == Tested with VLC 2.0.0

   new channel0 broadcast enabled setup channel0 input rushfondvert.avi
   setup channel0 output
   #duplicate{dst=mosaic-bridge{height=270,width=360,chroma=YUVA,vfilter=bluescreen},select=video}:display

   new background broadcast enabled setup background input
   file:///mire.jpg

   control background play control channel0 play

== Source code == \* {{VLCSourceFile|modules/video_filter/bluescreen.c}}

== See also == \* [[YUV]]

{{Documentation footer}}
