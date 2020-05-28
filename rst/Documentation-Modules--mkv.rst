{{Moduletype=Accessdescription=[[Matroska]] stream demuxersc2=mkv}}

{{Option value=boolean description=Play chapters in the order specified
in the segment }} {{Option value=boolean description=Use chapter
[[codec]]s found in the segment }} {{Option value=boolean
description=Preload matroska files in the same directory to find linked
segments (not good for broken files) }} {{Option value=boolean
description=Seek based on percent not time }} {{Option value=boolean
description=Read and discard unknown [[wikipedia:Extensible Binary Meta
Languagename=mkv-preload-clusters default=disabled \|description=Find
all cluster positions by jumping cluster-to-cluster before playback }}

== Source code == \* {{VLCSourceFoldermodules/demux/mkv/mkv.cpp}} (main
file)

{{Documentation}}
