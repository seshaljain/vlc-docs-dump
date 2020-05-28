== Video output == {{Moduletype=Video
outputlast_version=0.9.10|description=Outputs the video images to
files}}

In VLC 1.0.0 the image video output was rewritten into a video-filter
named [[Documentation:Modules/scene|scene]], and the old image video
output was removed.

Trivia:
[https://git.videolan.org/?p=vlc/vlc-0.9.git;a=blob;f=modules/video_output/image.c#l56
the help text] was never changed after {{Commitdiffl=this commitdiff}}
changed the default values of unsigned integers
<code>--image-out-width</code> and <code>--image-out-height</code> from
<code>-1</code> to <code>0</code>&mdash;there was little point in fixing
the help text for a deprecated module in software not yet publicly
released! The coding error is absent from the current module, scene.

Option aliases <code>--image-width</code> for
<code>--image-out-width</code> and <code>--image-height</code> for
<code>--image-out-height</code> were deprecated in 0.9.0.

=== Options === {{Option value=string default=png name=image-out-width
default=0 name=image-out-height default=0 name=image-out-ratio default=3
name=image-out-prefix default=img format time and meta variables]] }}
{{Option value=boolean description=Always write to the same file instead
of creating one file per image. In this case, the number is not appended
to the filename }}

== Demux == {{Clear}} {{Moduletype=Access demux|description=Image
demuxer}}

=== Options === {{Option value=integer description=Set the ID of the
[[elementary stream]] }} {{Option value=integer description=Set the
group of the elementary stream }} {{Option value=boolean
description=Decode at the [[demux]]er stage }} {{Option value=string
description=If non empty and <var>image-decode</var> is true, the image
will be converted to the specified [[chroma]] }} {{Option value=float
description=Duration in seconds before simulating an end of file. A
negative value means an unlimited play time }} {{Option value=string
description=[[Frame rate]] of the elementary stream produced }} {{Option
value=boolean description=Use real-time mode suitable for being used as
a master input and real-time input slaves }}

== Source code == \* {{VLCSourceFilemodules/video_output/image.c}}
(video output) \* {{VLCSourceFile|modules/demux/image.c}} (image
demuxer)

{{Documentation footer}}
