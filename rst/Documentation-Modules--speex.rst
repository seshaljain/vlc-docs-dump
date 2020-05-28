This module consists of a decoder, packetiser submodule and encoder
submodule. Only [[#Mux|the encoder]] has any options.

== Demux == {{Moduletype=Access demuxdescription=[[Speex]] audio
decoder|sc=none}}

=== Options === None. {{Clear}}

== Packetizer == {{Moduletype=Packetizerdescription=[[Speex]] audio
[[packetizer]]|sc=none}}

=== Options === None. {{Clear}}

== Mux == {{Moduletype=Muxerdescription=[[Speex]] audio
encoder|sc=none}}

=== Options === {{Option value=integer select={0,1,2}
name=sout-speex-complexity default=3 max=10 name=sout-speex-cbr
default=disabled name=sout-speex-quality default=8.0 max=10.0
name=sout-speex-max-bitrate default=0 name=sout-speex-vad
default=enabled voice activity detection]] (VAD). It is automatically
activated in VBR mode }} {{Option value=boolean description=Enable
[[wikipedia:discontinuous transmission|discontinuous transmission]]
(DTX) }}

== Source code == \* {{VLCSourceFile|modules/codec/speex.c}}

{{Documentation}}
