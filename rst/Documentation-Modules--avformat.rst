{{See also|Documentation:Modules/avcodec}}

[[Muxing]] options are provided as a sub-module and internally depend on
the variable <var>ENABLE_SOUT</var>.

== Demux == {{Moduletype=Access demuxname=avformat-format default=NULL
name=avformat-options default=NULL \|description=Advanced options, in
the form <kbd>{opt=val,opt2=val2}</kbd> }}

== Mux == {{Moduletype=Muxername=sout-avformat-mux default=NULL
name=sout-avformat-options default=NULL name=sout-avformat-reset-ts
default=disabled \|description=The muxed content will start near a 0
[[timestamp]] }}

== Source code == \*
{{VLCSourceFoldermodules/demux/avformat/avformat.c}} (file) \*
{{VLCSourceFilemodules/demux/avformat/avformat.h}} (header, defines
<var>MUX_LONGTEXT</var> and <var>FORMAT_LONGTEXT</var> shown here)

{{Documentation}}
