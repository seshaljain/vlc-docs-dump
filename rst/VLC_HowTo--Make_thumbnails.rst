.. raw:: mediawiki

   {{howto|make a thumbnail}}

How to create a thumbnail from a video
--------------------------------------

With new VLC versions (VLC 1.1.0 and above), the thumbnails are generated with scene video filter

::

   vlc C:\video\to\process.mp4 --rate=1 --video-filter=scene --vout=dummy --start-time=10 --stop-time=11 --scene-format=png --scene-ratio=24 --scene-prefix=snap --scene-path=C:\path\for\snapshots\ vlc://quit

If you want to get rid of the sound you can add "--aout=dummy" next to "--vout=dummy".

For older VLC versions (1.0.0 and below) the same can be done with image output module

::

   vlc C:\video\to\process.mp4 -V image --start-time 0 --stop-time 1 --image-out-format jpg --image-out-ratio 24 --image-out-prefix snap vlc://quit

What it does:
~~~~~~~~~~~~~

When runs it 'plays' the video for one second without actually showing the video on screen, and then quits, leaving us with a file named 'snap000000.jpg', containing an image of the first frame of the video.

How it works:
~~~~~~~~~~~~~

First select the image output with: **-V image** or **--vout image**.

Next set the interval (in seconds) you want an image from with: **--start-time 0 --stop-time 1** In my example the first second of the video. In that case you could omit the parameter --start-time. If you want an image from the 5th second fill in: **--start-time 5 --stop-time 6**

The image format will be .jpg because i provided: **--image-out-format jpg**. You could specify **--image-out-format png** to get a .png-image instead.

**--image-out-ratio 24** specifies we want one image out of 24. In my case the video contains 24 images per second so this is the right value. If your video has more images per seconds you should increase this value to prevend you get more images as one. If the number is too high (for example 500) it still produces only one image, so the actual value is not so important as long as it is higher then the images per second.

**--image-out-prefix snap** specifies the filename must start with 'snap'. You can prefix with a path, for example c:\snap and resulting images will be created there.

You can specify **--image-out-replace**. In that case Vlc produces the file 'snap.jpg'. This will prevent VLC from creating multiple images.

**test.mpg** specifies the video to play and finally **vlc://quit** forces vlc to quit when ready.

Creating a contact sheet
~~~~~~~~~~~~~~~~~~~~~~~~

Although VLC does not provide an option for creating a contact sheet, one possible solution is to use the `ImageMagick <http://www.imagemagick.org>`__ 'montage' tool. Taking the images generated by VLC, run the following command:

``  montage --tile *.jpg montage.jpg``

For more on the tool you can check the associated `montage help page <http://www.imagemagick.org/Usage/montage/>`__.
