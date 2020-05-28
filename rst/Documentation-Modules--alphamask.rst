{{Mosaic framework}} {{Moduletype=Video filterdescription=Change the
video's alpha channelsc2=mask}}

This filter can be used in the mosaic framework to set a video's alpha
channel (or transparency) based on a [[PNG]] image's alpha channel. You
can thus blend only parts of the mosaic substream on the background.
\__TOC_\_ == Options == {{Option value=string description=[[PNG]] file
to use as a mask. The alpha channel only will be used to build the mask.
This image needs to have the same size as the video it will be used
with. }}

== Example ==
   % '''vlc -I telnet --color -vvv --vlm-conf mosaic.vlm --mosaic-keep-picture '''
      '''--fake-file ~/images/mire.jpg --fake-width 360 --fake-height
      270 ''' '''--no-audio --sub-filter mosaic'''

And the vlm config:

   new channel0 broadcast enabled setup channel0 input
   redefined-nintendo.mpg setup channel0 output
   #duplicate{dst=mosaic-bridge{height=270,width=360,chroma=YUVA,vfilter=alphamask{mask=cone_360x270.png}},select=video}

   new background broadcast enabled setup background input fake: control
   background play

   control channel0 play

The files used are available on
[https://web.archive.org/web/20121015070412/https://people.videolan.org/~dionoea/mosaic/
people.videolan.org/~dionoea/mosaic (archived)] if you want to test.
(This will blend the redefined nintendo video in a cone like region)

== Source code == \* {{VLCSourceFile|modules/video_filter/alphamask.c}}

{{Documentation footer}}
