{{Moduletype=Access demuxdescription=[[Kate]] overlay decoder|sc=kate}}

The help text for this module: <pre> Kate is a codec for text and image
based overlays. The Tiger rendering library is needed to render complex
Kate streams, but VLC can still render static text and image based
subtitles if it is not available. Note that changing settings below will
not take effect until a new stream is played. This will hopefully be
fixed soon. </pre>

== Options == === Basic === {{Option value=boolean description=Kate
streams allow for text formatting. VLC partly implements this, but you
can choose to disable all formatting. Note that this has no effect if
rendering via Tiger is enabled }}

=== Tiger === {{Option value=boolean description=Kate streams can be
rendered using the Tiger library. Disabling this will only render static
text and bitmap based streams }} {{Option value=float max=1.0f
description=Select rendering quality, at the expense of speed. 0 is
fastest, 1 is highest quality }}

==== Tiger rendering defaults ==== {{Option value=string
name=kate-tiger-default-font-effect default=0
name=kate-tiger-default-font-effect-strength min=0.0f default=0.5
name=kate-tiger-default-font-color default=0x00ffffff (white)
name=kate-tiger-default-font-alpha min=0x00 default=0xff
name=kate-tiger-default-background-color default=0x00ffffff (white)
name=kate-tiger-default-background-alpha min=0x00 default=0x00
\|description=Transparency of the default background color if the Kate
stream does not specify a particular background color to use (0x00 is
fully transparent, 0xff is fully opaque) }}

== Source code == \* {{VLCSourceFile|modules/codec/kate.c}}
