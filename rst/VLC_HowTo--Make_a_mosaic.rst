.. raw:: mediawiki

   {{See also|Documentation:Modules/mosaic}}

.. raw:: mediawiki

   {{howto|set up a mosaic of a few videos or stream like a TV portal}}

VLC mosaic howto
----------------

This is a small example about how to use to create a mosaic. What we basically want is a video mosaic mixing 3 video channels (channels 1, 2 and 3) on a background image (background.png) and streaming the resulting video on the network. Note that we will also be streaming the 3 sound tracks from channels 1, 2 and 3 in the same `MPEG-TS <MPEG-TS>`__ stream.

Starting with VLC 0.8.5-test2, the `HTTP interface <HTTP_interface>`__ features a "Mosaic wizard". You might want to use it if you have no knowledge of VLC `command line <command_line>`__ usage.

https://web.archive.org/web/20070303011022/https://people.via.ecp.fr/~dionoea/videolan/mosaic1.png

Other neat examples :

-  `12 video mosaic <https://web.archive.org/web/20081011005351/https://people.via.ecp.fr/~dionoea/videolan/mosaic2.jpg>`__
-  `20 video mosaic <https://web.archive.org/web/20070404201658/https://people.via.ecp.fr/~dionoea/videolan/mos1.png>`__
-  `20 video mosaic <https://web.archive.org/web/20081011005318/https://people.via.ecp.fr/~dionoea/videolan/mos2.png>`__

Step 0
~~~~~~

Read the `VLC streaming howto <https://web.archive.org/web/20091228140745/https://www.videolan.org/doc/streaming-howto/en/streaming-howto-en.html>`__\ `[fr] <https://web.archive.org/web/20100106011007/https://www.videolan.org/doc/streaming-howto/fr/streaming-howto-fr.html>`__ (`chapters 3 <https://web.archive.org/web/20091227093342/https://www.videolan.org/doc/streaming-howto/en/ch03.html>`__\ `[fr] <https://web.archive.org/web/20100117041601/https://www.videolan.org/doc/streaming-howto/fr/ch03.html>`__ and `5 <https://web.archive.org/web/20091230100742/https://www.videolan.org/doc/streaming-howto/en/ch05.html>`__\ `[fr] <https://web.archive.org/web/20100112081440/https://www.videolan.org/doc/streaming-howto/fr/ch05.html>`__ concerning command line and VLM usage in VLC) : `www.videolan.org/doc <https://web.archive.org/web/20091227093342/https://www.videolan.org/doc/>`__

Step 1
~~~~~~

`Get VLC <https://www.videolan.org/vlc/#download>`__ 2 or newer and `install it <Documentation:Installing_VLC>`__ on your computer.

Step 2
~~~~~~

You now have to get a background for the mosaic.

An image is the easiest way to have a background that can be played as long as necessary. The image should be the same size as the video you want to create. Many image formats are supported (`JPEG <JPEG>`__, `PNG <PNG>`__ …).

It is also possible to use a video as a background for the mosaic, and `superimpose <wiktionary:superimpose>`__ other videos.

The `frame rate <frame_rate>`__ of the background video or image will be the frame rate of the mosaic video. This is important since the default frame rate for image files is 10fps.

For videolan 1.x and earlier, use the : access method. The frames per second cannot be changed.

You should test it with VLC to see if it displays locally :

``./vlc ``\ ```file:///full/path/to/background.png`` <file:///full/path/to/background.png>`__\ `` --image-duration=-1 --image-fps=10``

Step 3
~~~~~~

You now need to configure VLC to get the 3 source streams and blend them on the background image.

The `VLM configuration file <VLM#vlm.conf>`__ looks like :

::

   new channel1 broadcast enabled                                                       
   setup channel1 input udp://@239.255.2.60:1234                                        
   setup channel1 output #duplicate{dst=mosaic-bridge{id=1,height=144,width=180},select=video,dst=bridge-out{id=1},select=audio}                                                         
                                                                                   
   new channel2 broadcast enabled
   setup channel2 input udp://@239.255.10.200:1234
   setup channel2 output #duplicate{dst=mosaic-bridge{id=2,height=144,width=180},select=video,dst=bridge-out{id=2},select=audio}                                                         

   new channel3 broadcast enabled
   setup channel3 input udp://@239.255.6.9:1234
   setup channel3 output #duplicate{dst=mosaic-bridge{id=3,height=144,width=180},select=video,dst=bridge-out{id=3},select=audio}                                                         

   new background broadcast enabled
   setup background input /full/path/to/background.png
   setup background output #transcode{sfilter=mosaic,vcodec=mp2v,vb=10000,scale=1}:bridge-in{delay=400,id-offset=100}:standard{access=udp,mux=ts,url=239.255.12.42,sap,name="mosaic"}

   control background play
   control channel1 play
   control channel2 play
   control channel3 play

Since VLC 2.0, the mosaic options must be passed in the command line, and not in the VLM file.

Alternatively, one can setup a mosaic directly from files using a VLM configuration file as the following :

::

   new channel1 broadcast enabled                                                       
   setup channel1 input file:///path/to/movie.mp4
   setup channel1 output #duplicate{dst=mosaic-bridge{id=1,height=366}} 
                                               
   new channel2 broadcast enabled                                                       
   setup channel2 input file:///path/to/movie.mp4
   setup channel2 output #duplicate{dst=mosaic-bridge{id=2,height=366}}

   new channel3 broadcast enabled                                                       
   setup channel3 input file:///path/to/movie.mp4
   setup channel3 output #duplicate{dst=mosaic-bridge{id=3,height=366}}

   new channel4 broadcast enabled                                                       
   setup channel4 input file:///path/to/movie.mp4
   setup channel4 output #duplicate{dst=mosaic-bridge{id=4,height=366}}
                                    
   new mosaic broadcast enabled
   setup mosaic input file:///path/to/background1600.png
   setup mosaic output #transcode{sfilter=mosaic,vcodec=mp4v,VB=20000,acodec=none,fps=15,scale=1}:display

   control mosaic play
   control channel1 play
   control channel2 play
   control channel3 play
   control channel4 play

To `write the resulting stream to a file <Documentation:Modules/standard>`__, the mosaic output line may also be replaced by :

::

   setup mosaic output #transcode{sfilter=mosaic,vcodec=mp4v,VB=20000,acodec=none,fps=15,scale=1}:standard{access=file,mux=ogg,dst="output_file.ogg"}

Note that the source streams are network streams, which is likely to be the case if you're considering doing a mosaic.

Step 4
~~~~~~

And now, the right command to launch VLC :

``./vlc --color -I telnet --vlm-conf --mosaic-width=360 --mosaic-height=288 --mosaic-keep-picture --mosaic-rows=2 --mosaic-cols=2 --mosaic-position=1 --mosaic-order=1,2,3,4 ../mosaic.vlm.conf --ttl 12 --udp-caching 800``

Other examples
--------------

Dual webcam with alphamask
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{See also|Documentation:Modules/alphamask}}

https://web.archive.org/web/20110421103501/https://people.videolan.org/~dionoea/mosaic/dual-webcam.png

::

   new isight broadcast
   setup isight input v4l2:///dev/video0:width=320:height=240:audio-method=0
   setup isight option v4l2-brightness=90
   setup isight output #mosaic-bridge{chroma=YUVA,vfilter=alphamask{mask=../mask.png},width=320,height=240}
   setup isight enabled

   new logitech broadcast
   setup logitech input v4l2:///dev/video1:width=640:height=480:audio-method=0
   setup logitech output #transcode{vcodec=mp4v,vb=1024,sfilter="mosaic:marq{marquee='VLC dual webcam setup',position=8}"}:bridge-in:display
   setup logitech enabled

   new audio broadcast enabled
   setup audio input v4l:///dev/dsp1
   setup audio output #transcode{acodec=mp4a,ab=128}:bridge-out

   control isight play
   #control audio play
   control logitech play

You can then launch it with :

``vlc --vlm-conf ../dual-webcam.conf --no-media-library --plugin-path modules -v --no-video-title --mosaic-keep-picture``

The mask.png file is used to set transparency values on the isight camera (uses the png alpha plane). An example file to use `is available <https://web.archive.org/web/20110824043406/https://people.videolan.org/~dionoea/mosaic/mosaic_transparency_mask.txt>`__ at people.videolan.org/~dionoea/mosaic.

See also
--------

-  `Diagram that might help <https://web.archive.org/web/20070303010905if_/http://people.via.ecp.fr:80/~dionoea/videolan/mosaic-diagram.png>`__
-  `VLC mosaic-related resources <https://web.archive.org/web/20121015070412/https://people.videolan.org/~dionoea/mosaic/>`__
-  `Example set-up of conference web-streaming with two grabber cards <MosaicExampleSetup>`__

.. raw:: mediawiki

   {{Mosaic framework}}
