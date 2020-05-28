This module has no shortcut.

Support for [[wikipedia:Dynamic Adaptive Streaming over HTTP|DASH]] in
WebM is planned for VLC 4.0.0.

== Demux == {{Moduletype=Access demuxdescription=[[WebM]] video
decoder}}

[[VP9]] support was added in VLC 2.1.1.

=== Options === None. {{Clear}}

== Mux == {{Moduletype=Muxerdescription=[[WebM]] video encoder}}

=== Options === {{Option value=integer min=0 description=Quality setting
which will determine max encoding time: 0 is Good quality, 1 is Realtime
and 2 is Best quality }} {{Clear}}

== Source code == \* {{VLCSourceFile|modules/codec/vpx.c}}

{{Documentation}}
