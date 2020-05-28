== Options == === Access Demux === {{Moduletype=Access
demuxdescription=simulate a fake inputname=fake-caching
default=<code><var>DEFAULT_PTS_DELAY</var>/1000</code> milliseconds]] }}
{{Option value=float description=[[Framerate]] e.g. 24, 25, 29.97, 30 }}
{{Option value=integer description=Set the ID of the fake [[elementary
stream]] for use in <samp>#{{docmodname=fake-duration default=0 right}}

=== Codec === {{Moduletype=Codecdescription=handle a fake input
streamname=fake-file default="" name=fake-file-reload default=0
name=fake-width default=0 name=fake-height default=0 name=fake-keep-ar
default=disabled name=fake-aspect-ratio default="" name=fake-deinterlace
default=disabled name=fake-deinterlace-module default="deinterlace"
name=fake-chroma default="[[I420]]" \|description=Image [[chroma]] }}

== Example ==
   {{$}} '''vlc fake:// --fake-file someimage.png'''

== Source code == \* {{VLCSourceFilep=vlc/vlc-0.9.git}} \*
{{VLCSourceFilep=vlc/vlc-0.9.git}}

{{Documentation footer}}
