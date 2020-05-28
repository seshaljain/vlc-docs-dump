{{Moduletype=Access demuxdescription=Teletext [[subtitles]]
decoder|sc=none}}

== Options == {{Option value=integer description=Override the indicated
page, try this if your subtitles don't appear (-1 = autodetect from TS,
0 = autodetect from teletext, >0 = actual page number, usually 888 or
889) }} {{Option value=boolean description=Ignore the subtitle flag, try
this if your subtitles don't appear }} {{Option value=boolean
description=Some French channels do not flag their subtitling pages
correctly due to a historical interpretation mistake. Try using this
wrong interpretation if your subtitles don't appear }}

== Source code == \* {{VLCSourceFile|modules/codec/telx.c}}

{{Documentation footer}}
