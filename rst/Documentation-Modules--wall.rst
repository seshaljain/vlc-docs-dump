{{Moduletype=Video output splitter|description=Splits the video output
in several windows}}

You can use this module to split a video output in several small
windows. This is especially useful if you want to display parts of the
same video on several computers to make a big video wall.

The option <code>--wall-element-aspect</code> is {{Commitdiffl=planned
to be removed from 4.0.0}} to fix {{Bug213}}. The option is redundant,
and there will still be a way to select a custom ratio.

For the option <code>--wall-active</code>, list the integers of the
windows. To select windows 2, 3 and 5 specify
<kbd>--wall-active=2,3,5</kbd>.

== Options == <onlyinclude>{{Option value=integer max=15
description=Number of horizontal windows in which to split the video }}
{{Option value=integer max=15 description=Number of vertical windows in
which to split the video }} {{Option value=string
description=Comma-separated list of active windows, defaults to all }}
{{Option value=string description=Aspect ratio of the individual
displays building the wall }}</onlyinclude>

== Source code == \* {{VLCSourceFile|modules/video_splitter/wall.c}}

{{Documentation footer}}
