{{Mosaic framework}} {{Moduletype=Stream outputdescription=Get
[[elementary stream]]s from the bridge framework|sc=bridge-in}}

This module gets all the [[elementary stream]]s sent to the bridge
framework. It is used when streaming a mosaic to attach the audio
streams to the mosaic output. \__TOC_\_ {{Clear}}

== Options == {{Option value=integer description=Pictures coming from
the picture video outputs will be delayed according to this value (in
milliseconds, should be &ge; 100 ms). For high values, you will need to
raise caching values. }} {{Option value=integer description=Offset to
add to the stream IDs specified in bridge-out to obtain the stream IDs
bridge-in will register. }} {{Option value=string description=Name of
this bridge-in instance. If you do not need more than one bridge-in at a
time, you can discard this option. }} {{Option value=boolean
description=If set to true, the bridge will discard all input elementary
streams except if it doesn't receive data from another bridge-in. This
can be used to configure a placeholder stream when the real source
breaks. Source and placeholder streams should have the same format. }}
{{Option value=integer description=Delay (in ms) before the placeholder
kicks in. }} {{Option value=boolean description=If enabled, switching
between the placeholder and the normal stream will only occur on
[[I-frame]]s. This will remove artifacts on stream switching at the
expense of a slightly longer delay, depending on the frequency of
I-frames in the streams. }}

== Source code == \* {{VLCSourceFile|modules/stream_out/bridge.c}}

{{Documentation footer}}
