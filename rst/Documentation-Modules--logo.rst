{{See alsoVLC HowTo/Add a logo}}

The logo filter can be used to add a logo on the video. This logo can be
a static image or series of images which will be displayed
alternatively. When used as a video output filter, you can move the logo
with the mouse.

== Video sub-filter == {{Moduletype=Video sub-filtersc=logo}}
<onlyinclude>{{Option value=string name=logo-x default=0 name=logo-y
default=0 name=logo-position<span id="logo-position"></span>
select=[[#appendix_logo-positiondefault=5 name=logo-opacity default=255
max=255 name=logo-delay default=1000 ms]]. Sets the duration each image
will be displayed for in a loop iteration unless specified otherwise in
the <code>--logo-file</code> option. }} {{Option value=integer
description=Number of loops for the logo animation. -1 for continuous, 0
to disable. }}</onlyinclude> {{Clear}}

== Video output filter == {{Moduletype=Video output filtersc=logo}}
{{Clear}}

== Examples ==
   {{%}} '''vlc --video-filter "logo{file=cone.png,opacity=128}"
   somevideo.avi'''

: This command will display image cone.png in the video's upper right
corner with 50% transparency.

   {{%}} '''vlc --video-filter
   "logo{file='cone1.png,2000,128;cone2.png,3000'}" somevideo.avi'''

: This command will display image cone1.png for 2 seconds with 50%
transparency followed by image cone2.png for 3 seconds at default
transparency and loop.

== Source code == \* {{VLCSourceFile|modules/spu/logo.c}}

== Appendix == <div class="plainlist"> \*^
[[#logo-position|--logo-position]]<span
id="appendix_logo-position"></span> </div> {{Alignment mapping}}

{{Documentation footer}}
