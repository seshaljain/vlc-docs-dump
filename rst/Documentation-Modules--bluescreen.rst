.. raw:: mediawiki

   {{Mosaic framework}}

.. raw:: mediawiki

   {{Module|name=bluescreen|type=Video filter|first_version=0.9.0|description=Change the video's alpha channel|sc=bluescreen}}

This filter can be used in the mosaic framework to set a video's alpha channel (or transparency) based on a pixel's color. This is also known as `green screen <wikipedia:green_screen>`__ or chroma key blending and can be used to create effects like on most weather channels.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=bluescreen-u
   |value=integer
   |min=0
   |max=255
   |default=120
   |description=U chroma component.
   }}

.. raw:: mediawiki

   {{Option
   |name=bluescreen-v
   |value=integer
   |min=0
   |max=255
   |default=90
   |description=V chroma component.
   }}

.. raw:: mediawiki

   {{Option
   |name=bluescreen-ut
   |value=integer
   |min=0
   |max=255
   |default=17
   |description=Tolerance of the bluescreen blender on color variations for the U plane. A value between 10 and 20 seems sensible.
   }}

.. raw:: mediawiki

   {{Option
   |name=bluescreen-vt
   |value=integer
   |min=0
   |max=255
   |default=17
   |description=Tolerance of the bluescreen blender on color variations for the V plane. A value between 10 and 20 seems sensible.
   }}

Example
-------

``% ``\ **``vlc``\ ````\ ``-vvv``\ ````\ ``--vlm-conf``\ ````\ ``mosaic.vlm``\ ````\ ``--mosaic-keep-picture``\ ````\ ``--sub-filter``\ ````\ ``mosaic``**

And the vlm config:

| ``new channel0 broadcast enabled``
| ``setup channel0 input rushfondvert.avi``
| ``setup channel0 output #duplicate{dst=mosaic-bridge{chroma=YUVA,vfilter=bluescreen},select=video}``
| `` ``
| ``new background broadcast enabled``
| ``setup background input redefined-nintendo.mpg``
| ``control background play``
| `` ``
| ``control channel0 play``

Have a look at `people.videolan.org/~dionoea/bluescreen2.mpg (archived) <https://web.archive.org/web/20060819104251/http://people.videolan.org/~dionoea/bluescreen2.mpg>`__ for an example of the VLC bluescreen filter. The overlay video is `rushfondvert.avi (archived) <https://web.archive.org/web/20061205222657/http://people.videolan.org/~dionoea/rushfondvert.avi>`__ and features someone with a mask in front of a green background. The bluescreen module's default values are adjusted to remove the background from this video. For other videos you should use your favorite color editing tool to find out the appropriate U and V values.

Another example
---------------

Tested with VLC 2.0.0

| ``new channel0 broadcast enabled``
| ``setup channel0 input rushfondvert.avi``
| ``setup channel0 output #duplicate{dst=mosaic-bridge{height=270,width=360,chroma=YUVA,vfilter=bluescreen},select=video}:display``
| ``new background broadcast enabled``
| ``setup background input ``\ ```file:///mire.jpg`` <file:///mire.jpg>`__
| ``control background play``
| ``control channel0 play``

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/video_filter/bluescreen.c}}

See also
--------

-  `YUV <YUV>`__

.. raw:: mediawiki

   {{Documentation footer}}
