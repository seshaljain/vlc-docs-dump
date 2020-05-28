{{Moduletype=Video outputdescription=GNU/Linux framebuffer video
output|sc=none}}

Option <code>--fb-aspect-ratio</code> is deprecated.<br /> Option
<code>--fb-hw-accel</code> is planned to be deprecated in 4.0.0
(currently 4.0.0-dev).

== Options == {{Option value=string description=Framebuffer device to
use for rendering (usually <code>/dev/fb0</code>) }} {{Option
value=boolean description=Run framebuffer on current
[[wiktionary:TTYname=fb-chroma default=RGB name=fb-mode
select={0,1,2,3,4} description=Select the resolution for the
framebuffer. Currently it supports the values: 0 - QCIF, 1 - CIF, 2 -
NTSC, 3 - PAL, 4 - auto }}

== Source code == \* {{VLCSourceFile|modules/video_output/fb.c}}

{{Documentation}}
