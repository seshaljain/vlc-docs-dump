{{Moduletype=Muxerdescription=[[fdk-aacsc=fdkaac}}

This module is dual-licenced under LGPL 2.1 and BSD 2-clause.
{{VLCSourceFile34ba8bd409b16a33353b2240330b405c970b0f7c|l=not used
anymore}}.

== Options == {{Option value=integer select={2,5,29,23,39}
name=sout-fdkaac-sbr default=disabled spectral band
replication]]&mdash;This is an optional feature only for the AAC-ELD
profile }} {{Option value=integer min=0 description=Quality of the
[[VBR]] Encoding (0=cbr, 1-5 constant vbr quality, 5 is the best) }}
{{Option value=boolean description=This library will produce higher
quality audio at the expense of additional CPU usage (default is
enabled) }} {{Option value=integer min=0 description=1 is explicit for
SBR (<var>SIGNALING_COMPATIBLE</var>) and implicit for [[PS]] (default),
2 is explicit hierarchical }}

== Source code == \* {{VLCSourceFile|modules/codec/fdkaac.c}}

{{Documentation}}
