{{Moduletype=Video filter|description=motion blur video filter}}

Use this filter to blur motion in a video based on previous frames.

== Options == <onlyinclude>{{Option value=integer min=1 description=The
bluring factor (1 to 127). Higher values mean more blurring
}}</onlyinclude>

== Examples ==
   % '''vlc --video-filter "motionblur{factor=60}" somevideo.avi'''

'''Note:''' In versions prior to 0.9.0, motionblur was a video output
filter.

{{Documentation footer}}
