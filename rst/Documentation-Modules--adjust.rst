{{Moduletype=Video filterdescription=Image properties filter}}

'''Note:''' Before version 0.9.0, this used to be a vout filter.

== Options == <onlyinclude>{{Option value=float min=0.0
description=Contrast }} {{Option value=float min=0.0
description=Brightness }} {{Option value=float min=-180 description=Hue
}} {{Option value=float min=0.0 description=Saturation }} {{Option
value=float min=0.01 description=Gamma }} {{Option value=boolean
description=When this mode is enabled, pixels will be shown as black or
white. Also may invert the brightness value. The threshold value will be
the brightness defined below }}</onlyinclude>

== Examples ==
   {{%}} '''vlc --video-filter "adjust{hue=120,gamma=2.}" somevideo.avi

== Source code == \* {{VLCSourceFile|modules/video_filter/adjust.c}}

{{Documentation footer}}
