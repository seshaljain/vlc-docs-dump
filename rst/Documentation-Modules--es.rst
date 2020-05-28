== Demux == {{See
alsoname=esdescription=[[MPEG-1II]]/[[MPEG-4sc=mpgasc3=m4asc5=aacsc7=a52sc9=dtssc11=thd}}

=== Options === None. {{Clear}}

=== MPEG-4 video === {{Moduletype=Access demuxsc=m4v|sc2=mp4v}}

==== Options ==== {{Option value=float description=This is the [[frame
rate]] used as a fallback when playing MPEG video [[elementary
stream]]s. }} {{Clear}}

== Stream output == {{Moduletype=Stream outputsc=es}}

As of VLC 2.2.0 all elementary streams are streamed by default. This can
be overridden with <code>--no-sout-all</code>.

=== Options === ==== Generic ==== {{Option value=string name=sout-es-mux
description=This is the default muxer method that will be used }}
{{Option value=string \|description=This is the default output URI }}

==== Audio ==== {{Option value=string name=sout-es-mux-audio
description=This is the muxer that will be used for audio }} {{Option
value=string \|description=This is the output URI that will be used for
audio }}

==== Video ==== {{Option value=string name=sout-es-mux-video
description=This is the muxer that will be used for video }} {{Option
value=string \|description=This is the output URI that will be used for
video }}

== Source code == \* {{VLCSourceFilemodules/stream_out/es.c}}

{{Documentation}}
