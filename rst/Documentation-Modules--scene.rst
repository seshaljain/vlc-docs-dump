{{Moduletype=Video filterdescription=Send your video to picture files}}

'''Note:''' Before version 1.0.0, this used to be
[[Documentation:Modules/image|image]].

== Options == {{Option value=string description=Image format. Format of
the output images ([[png]], [[jpeg]], ...) }} {{Option value=integer
default=-1 }} {{Option value=integer default=-1 }} {{Option value=string
description=Filename prefix. Prefix of the output images filenames.
Output filenames will have the "prefixNUMBER.format" form if
<var>scene-replace</var> is not true }} {{Option value=string
description=Directory path prefix. Directory path where images files
should be saved. If not set, then images will be automatically saved in
users homedir }} {{Option value=boolean default=disabled }} {{Option
value=integer min=1 description=Recording ratio. Ratio of images to
record. 3 means that one image out of three is recorded }}

== Source code == \* {{VLCSourceFile|modules/video_filter/scene.c}}

{{Documentation}}
