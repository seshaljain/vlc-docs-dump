.. raw:: mediawiki

   {{Module|name=rawvid|type=Access demux|first_version=0.9.0|description=Raw video demuxer|sc=rawvideo}}

Options
-------

.. raw:: mediawiki

   {{Option
   |name=rawvid-fps
   |value=string
   |description=This is the desired frame rate when playing raw video streams. In the form 30000/1001 or 29.97
   }}

.. raw:: mediawiki

   {{Option
   |name=rawvid-width
   |value=integer
   |description=This specifies the width in pixels of the raw video stream
   }}

.. raw:: mediawiki

   {{Option
   |name=rawvid-height
   |value=integer
   |description=This specifies the height in pixels of the raw video stream
   }}

.. raw:: mediawiki

   {{Option
   |name=rawvid-chroma
   |value=string
   |description=Force chroma. This is a four character string
   }}

.. raw:: mediawiki

   {{Option
   |name=rawvid-aspect-ratio
   |value=string
   |description=Aspect ratio (4:3, 16:9). Default assumes square pixels
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/rawvid.c}}

.. raw:: mediawiki

   {{Documentation}}
