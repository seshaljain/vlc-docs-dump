{{howto|crop the video}} == What is cropping? == Cropping refers to the
removal of the outer parts of an image. So it remove something from
left, right, top and/or bottom of image. Usually with videos cropping is
used to change aspect ratio by cutting something out (known as Pan and
scan method).

== How to do it QT4 == From QT4 GUI you can enable cropping from
'''Tools -> Preferences...''' (Show settings: All) then '''Video''' and
'''Video cropping''' field.

or

'''Tools''' -> '''Effects and Filters''' (Ctrl+E) then '''Video
Effects''' -> '''Crop''', and set the values.

== How to do it from command-line/terminal/shell == For [[aspect
ratio]]s, no module is needed. Any of these adapt video to a 16:9 aspect
ratio: vlc input "--crop=16:9" vlc input "--aspect-ratio=16:9" vlc input
"--aspect-ratio=1.777"

For cropping and padding, use croppadd.

Add 100 pixels to the top of the video:
   vlc input "--video-filter=croppadd{paddtop=100}"

Remove 100 pixels from the left of the video:
   vlc input "--video-filter=croppadd{cropleft=100}"

Both:
   vlc input "--video-filter=croppadd{paddtop=100,cropleft=100}"

=== Old way === If you want to crop local video with
command-line/terminal parameters, use vlc input --vout-filter=crop
--crop-geometry=120x120+10+10 120x120 is the wanted resolution (in
pixels), and 10+10 is the top-left position where the cropping should
start (in pixels)

or if you want certain aspect ratio
   vlc input --vout-filter=crop --crop-ratio=1777

where 1777 is aspect ratio you want (divide it with 1000 to get correct
value, in this case 1,777 aka 16:9)

{{DEFAULTSORT:Crop}}
