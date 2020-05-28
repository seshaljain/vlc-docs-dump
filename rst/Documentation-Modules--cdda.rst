{{See alsoname=cddafirst_version=&le; 0.8sc=cdda|sc2=cddasimple}}

The option <code>--cd-audio</code> is new as of
{{Commitdiff43bb27d91ce344eee93df3c956cd2513e3eecc3c}} (2018).

The options <code>--cdda-track</code> plays a particular track (like
<code>@track</code> does). <code>--cdda-first-sector</code> and
<code>cdda-last-sector</code> seem to be hints to VLC to skip
[[wikipedia:disk sector|disk sector]]s at the beginning or end.

{{Option value=string name=cdda-track default=0 name=cdda-first-sector
default=-1 name=cdda-last-sector default=-1 name=cddb-server
default=freedb.videolan.org name=cddb-port min=1 default=80
\|description=CDDB Server [[port]] to use }}

== Source code == \* {{VLCSourceFile|modules/access/cdda.c}}

{{Documentation}}
