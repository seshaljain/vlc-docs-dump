== Decoder == {{Moduletype=Access demuxdescription=[[JPEG]] image
decoder through libjpeg|sc=none}}

{{VLC}} previously decoded JPEGs through the images demuxer (introduced
in VLC 2.0.0).

=== Options === None. {{Clear}}

== Encoder == {{Moduletype=Muxerdescription=[[JPEG]] image encoder
through libjpeg|sc=jpeg}}

=== Options === {{Option value=integer max=100 \|description=Quality
level for encoding (this can enlarge or reduce output image size) }}
{{Clear}}

== Source code == \* {{VLCSourceFile|modules/codec/jpeg.c}}

{{Documentation}}
