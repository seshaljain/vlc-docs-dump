{{Moduletype=Stream outputdescription=Duplicate stream outputsc2=dup}}

== Options == None. {{Clear}}

== Examples == From the changelog: <code class="nowrap">--sout
"#duplicate{dst=transcode{vcodec=mp2v},select=es=0,dst=transcode,select=es=1}:std{...}"</code>

== Source code == \* {{VLCSourceFile|modules/stream_out/duplicate.c}}

{{Documentation}}
