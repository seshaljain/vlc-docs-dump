{{Image requested}} {{Moduletype=Video filterdescription=apply gradients
and edge detection filters}}

Use this filter to apply gradients or do simple edge detection
algorithms to the video image.

== Options == {{Option value=string description=One of "gradient",
"edge" or "hough". }}

{{Option value=integer description=0 to discard colors, 1 to keep
colors. }}

{{Option default=enabled \|description=Apply a cartoon effect. }}

== Example ==
   % '''vlc --video-filter "gradient{type=1}" somevideo.avi'''

== Screenshots ==
http://photos.cellerier.net/d/406-1/vlcsnap-8120371.png
http://photos.cellerier.net/d/397-1/vlcsnap-10589245.png

'''Note:''' In versions prior to 0.9.0, this was part of the
[[Documentation:Modules/distort|distort]] video filter.

{{Documentation footer}}
