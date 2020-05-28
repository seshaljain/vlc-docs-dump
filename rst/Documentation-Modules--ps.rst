{{Moduletype=Access demux|description=[[MPEG-PS]] demuxer}}

== Options == <onlyinclude> {{Option value=boolean description=Normally
we use the [[timestamp]]s of the [[MPEG]] files to calculate position
and duration. However sometimes this might not be usable. Disable this
option to calculate from the [[bitrate]] instead }}</onlyinclude>

== Source code == \* {{VLCSourceFile|modules/demux/mpeg/ps.c}}

{{Documentation footer}}
