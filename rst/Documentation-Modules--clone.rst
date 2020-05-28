{{Moduletype=Video output splittersc=clone}}

You can use this module to play the video in more than one window to
test different video outputs or display the same video on multiple
screens on the same computer.

== Options == <onlyinclude>{{Option value=integer description=Number of
video windows in which to clone the video. }} {{Option value=string
description=You can use specific video output modules for the clones.
Use a comma-separated list of modules. }}</onlyinclude>

== Examples ==
   {{$}} vlc --video-splitter=clone --clone-count=2 video.ogv

== Source code == \* {{VLCSourceFile|modules/video_splitter/clone.c}}

{{Documentation footer}}
