{{Moduletype=Access demux|description=[[MPEG-TS]] demuxer}}

The options <code><nowiki>ts-dump-file</nowiki></code>,
<code><nowiki>ts-dump-append</nowiki></code> and
<code><nowiki>ts-dump-size</nowiki></code> were removed in
{{Commitdiff|31dee2cbaa16d16de94b5a1b36fe7f3909b8b28d}} with the summary
"There is a dump demux for that."

The options <code><nowiki>ts-out</nowiki></code> and
<code><nowiki>ts-out-mtu</nowiki></code> have been deprecated since VLC
2.2.0. <code><nowiki>ts-silent</nowiki></code> is also deprecated.

== Options == <onlyinclude> {{Option value=string default=auto
name=ts-extra-pmt default=NULL name=ts-trust-pcr default=enabled
name=ts-es-id-pid default=enabled name=ts-csa-ck default=NULL
name=ts-csa2-ck default=NULL name=ts-csa-pkt default=188
name=ts-split-es default=enabled dvbs]] pages into independent {{ES}}.
It can be useful to turn off this option when using stream output }}
{{Option value=boolean description=Seek and position based on a percent
byte position, not a PCR generated time position. If seeking doesn't
work property, turn on this option }} {{Option value=boolean
description=Detect discontinuities and drop packet duplicates. (bluRay
sources are known broken and have false positives) }} {{Option
value=boolean description=Only create ES on program sending data }}
{{Option value=boolean description=Try to generate PAT/PMT if missing }}
{{Option value=boolean description=Try to fix too early PCR (or late
DTS) }}</onlyinclude>

== Source code == \* {{VLCSourceFile|modules/demux/mpeg/ts.c}}

{{Documentation footer}}
