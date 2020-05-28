.. raw:: mediawiki

   {{lowercase}}

Supported codecs
----------------

=========== ================== =============== ===================
Video Codec **mp4v**, **H264** up to 2500 kbps and up to 640x480px
Audio Codec **mp4a**, **aac**  up to 160 kbps 
Container   **mp4**                           
Screen size 480x320px          (1.5:1 or 3:2) 
=========== ================== =============== ===================

iPhone Movie Conversion Hints
-----------------------------

For a more complete description with pictures read the `iPod <iPod>`__ video conversion guide! The following has been tested for 0.8.6i.

Video files
~~~~~~~~~~~

Codec: *H264* leads to better videos than *mp4v* but is **lots** slower. I strongly recommend to use the *mp4v* codec.

Size: Usually the smaller video dimension is the height. Therefore setting the video height to the phone screen height (320px) is reasonable. Instead of always calculating the corresponding width use the canvas-aspect parameter, VLC will then do it for you. Only go larger if you plan to watch iPhone movies also on larger screens. In this case, the limiting size will most probably be the width (max 640px).

`Bitrate <Bitrate>`__: 768 kbps shows good results and reasonable file size. If you have action movies with many fast movements 1024 kbps or even more are recommended.

Audio files
~~~~~~~~~~~

Codec: *mp4a* works nicely. *aac* was not tested.

Bitrate: For listening with earplugs 160 kbps are sufficient.

Converting via command line
---------------------------

Here an example conversion of a DVD is shown and commented.

::

   vlc "dvdsimple://D:@1 :sub-track=0 :audio-track=2" 
   :sout="#transcode{canvas-aspect=1.5:1,height=320,vcodec=mp4v,vb=768,
   acodec=mp4a,ab=128,channels=2,soverlay}
   :std{access=file,mux=mp4,dst=movie.mp4}" vlc:quit

**height=320,canvas-aspect=1.5:1,vcodec=mp4v,vb=768,**

Sets the height to the screen height, the correct width with canvas aspect, the video codec is MPEG-4 video and the bitrate is 768 kbps

**acodec=mp4a,ab=160,channels=2**

Codec for audio is MPEG-4 audio, bitrate 160 and channels = 2 means normal stereo output.

**soverlay**

Burns the subtitles in the movie. The default size is large enough to be readable.

`Category:How To <Category:How_To>`__ `Category:iOS <Category:iOS>`__
