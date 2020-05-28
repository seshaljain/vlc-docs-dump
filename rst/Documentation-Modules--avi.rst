== Demux == {{Moduletype=Access demuxsc=none}} {{Option value=boolean
description=Force interleaved method }} {{Option value=integer
select={0,1,2,3} \|description=Recreate a index for the AVI file. Use
this if your AVI file is damaged or incomplete (not seekable). 0 ("Ask
for action"), 1 ("Always fix"), 2 ("Never fix"), 3 ("Fix when
necessary") }} {{Clear}}

== Mux == {{Moduletype=Muxersc=avi}} {{Option value=string
description=Artist }} {{Option value=string description=Date }} {{Option
value=string description=Genre }} {{Option value=string
description=Copyright }} {{Option value=string description=Comment }}
{{Option value=string description=Name }} {{Option value=string
description=Subject }} {{Option value=string description=Encoder }}
{{Option value=string description=Keywords }} {{Clear}}

== Source code == \* {{VLCSourceFilemodules/mux/avi.c}} \*
{{VLCSourceFolder|modules/demux/avi}}

{{Documentation}}
