{{Moduletype=Stream outputdescription=[[MPEG-2 video]] switcher stream
output|sc=switcher}}

This module used the {{docmod|avcodec}} library.

== Options == {{Option value=string description=Full paths of the files
separated by colons }} {{Option value=string description=List of sizes
separated by colons (720x576:480x576) }} {{Option value=string
description=[[Aspect ratio]] (4:3, 16:9) }} {{Option value=integer
description=[[UDP]] port to listen to for commands }} {{Option
value=integer description=Initial command to execute }} {{Option
value=integer description=Number of [[P-frame]]s between two
[[I-frame]]s }} {{Option value=integer description=Fixed quantizer scale
to use }} {{Option value=boolean description=Mute audio when command is
not 0 }}

== Source code == \* {{VLCSourceFilemodules/stream_out/switcher.c}}

{{Documentation}}
