{{See alsoname=erasefirst_version=0.9.0|description=logo erasing video
filter}}

Use this filter to erase a logo (or any given area) from the video.

== Options == {{Option value=string description=[[PNG]] file to use as a
mask. The alpha channel only will be used to build the mask }} {{Option
value=integer description=X offset from upper left corner }} {{Option
value=integer description=Y offset from upper left corner. }}

== Example ==
   {{$}} '''vlc --video-filter "erase{mask=logo.png,x=100,y=50}"
   somevideo.avi'''

== Source code == \* {{VLCSourceFile|modules/video_filter/erase.c}}

{{Documentation footer}}
