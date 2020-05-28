{{Mosaic framework}} {{Moduletype=Stream outputdescription=Send an
[[elementary stream]] to the bridge framework|sc=bridge-out}}

This module sends an [[elementary stream]] to the bridge framework. It
is used when streaming a mosaic to send the audio stream to the mosaic
output.

== Options == {{Option value=integer description=Integer identifier for
this elementary stream. This will be used to "find" this stream later.
}} {{Option value=string description=Name of the destination bridge-in.
If you do not need more than one bridge-in at a time, you can discard
this option. }}

== Source code == \* {{VLCSourceFile|modules/stream_out/bridge.c}}

{{Documentation footer}}
