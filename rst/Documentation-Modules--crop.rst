:''Were you looking for
{{docmodname=Croplast_version=2.0.9|description=Remove borders of the
video and replace them with black borders}}

== Options == <onlyinclude>{{Option value=string name=autocrop
default=disabled name=autocrop-ratio-max default=2405 max=15000
name=crop-ratio default=0 max=15000 name=autocrop-time default=25
name=autocrop-diff default=16 name=autocrop-non-black-pixels default=3
name=autocrop-skip-percent default=17 max=100
name=autocrop-luminance-threshold default=40 max=128
\*]]</noinclude><includeonly>(0-128)</includeonly> }}</onlyinclude>

== Note == This must be a typo. Despite the
[https://git.videolan.org/?p=vlc.git;a=blob;f=modules/video_filter/crop.c;h=2584780d98bb8527f9aacf540721a4ed5b852833;hb=c638a67c52980404d2aa6f6851b455743a898820#l97
claim of a range of <code>0-255</code>] in the help text for the
<code>--autocrop-luminance-threshold</code> option,
[https://git.videolan.org/?p=vlc.git;a=blob;f=modules/video_filter/crop.c;h=2584780d98bb8527f9aacf540721a4ed5b852833;hb=c638a67c52980404d2aa6f6851b455743a898820#l129
the call] to
<code>[https://git.videolan.org/?p=vlc.git;a=blob;f=include/vlc_configuration.h;h=bdbb11026492436f7f7297e096a8c62f8e899b68;hb=c638a67c52980404d2aa6f6851b455743a898820#l344
add_integer_with_range]</code> would have limited this to effectively
<code>0-128</code>.

== Source code == \* {{VLCSourceFilemodules/video_filter/crop.c}}

{{Documentation}}
