{{Moduletype=Stream outputsc=display}}

== Options == {{Option value=boolean description=Enable audio rendering.
}} {{Option value=boolean description=Enable video rendering. }}
{{Option value=integer description=Introduces a delay (ms) in the
display of the stream. }}

== Examples == [[Transcode]] and stream a file while displaying it
locally.<br /> This will display the transcoded version: % '''vlc
somevideo.avi --sout
"#transcode{vcodec=mp2v,vb=2048,acodec=mpga,ab=96}:duplicate{dst=std{access=udp,mux=ts{ttl=12},url=239.255.1.1},dst=display}"'''
This will display the original version: % '''vlc somevideo.avi --sout
"#duplicate{dst='transcode{vcodec=mp2v,vb=2048,acodec=mpga,ab=96}:std{access=udp,mux=ts{ttl=12},url=239.255.1.1}',dst=display}"'''

== Source code == \* {{VLCSourceFile|modules/stream_out/display.c}}

== See also == \* [[Documentation:Modules/duplicate]]

{{Documentation footer}}
