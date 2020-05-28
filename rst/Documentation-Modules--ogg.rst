The ogg demux module refers to [[Ogg]] as ''OGG''. The [[Xiph Wiki]]
[https://wiki.xiph.org/Ogg#Name clarifies] that the name is not an
acronym and should be written ''Ogg'' or ''ogg''.

The earliest mention of Ogg [[muxing]] support in the changelog was for
the macOS port in 0.5.3.

== Demux == {{Moduletype=Access demuxdescription=[[Oggsc=ogg}}

=== Options === None. {{Clear}}

== Mux == {{Moduletype=Muxersc=ogg|sc2=ogm}}

=== Options === {{Option value=integer min=0 description=Minimal index
interval, in [[wiktionary:msname=sout-ogg-indexratio default=1.0
max=1000 \|description=Set index size ratio. Alters default (60min
content) or estimated size. }}

== Source code == \* {{VLCSourceFilemodules/demux/ogg_granule.c}} \*
{{VLCSourceFilemodules/mux/ogg.c}}

{{Documentation footer}}
