.. raw:: mediawiki

   {{See also|Stream to memory (smem) tutorial}}

.. raw:: mediawiki

   {{Module|name=smem|type=Stream output|first_version=1.1.0|description=Stream output to memory buffer|sc=smem}}

.. raw:: mediawiki

   {{Clear}}

There is a note in the source code:

.. code:: c

   /*****************************************************************************
    * How to use it
    *****************************************************************************
    *
    * You should use this module in combination with the transcode module, to get
    * raw datas from it. This module does not make any conversion at all, so you
    * need to use the transcode module for this purpose.
    *
    * For example, you can use smem as it :
    * --sout="#transcode{vcodec=RV24,acodec=s16l}:smem{smem-options}"
    *
    * Into each lock function (audio and video), you will have all the information
    * you need to allocate a buffer, so that this module will copy data in it.
    *
    * the video-data and audio-data pointers will be passed to lock/unlock function
    *
    ******************************************************************************/

Options
-------

.. raw:: mediawiki

   {{Option
   |name=sout-smem-video-prerender-callback
   |value=string
   |default="0"
   |description=Address of the video prerender callback function. This function will set the buffer where render will be done.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-smem-audio-prerender-callback
   |value=string
   |default="0"
   |description=Address of the audio prerender callback function. This function will set the buffer where render will be done.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-smem-video-postrender-callback
   |value=string
   |default="0"
   |description=Address of the video postrender callback function. This function will be called when the render is into the buffer.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-smem-audio-postrender-callback
   |value=string
   |default="0"
   |description=Address of the audio postrender callback function. This function will be called when the render is into the buffer.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-smem-video-data
   |value=string
   |default="0"
   |description=Data for the video callback function.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-smem-audio-data
   |value=string
   |default="0"
   |description=Data for the audio callback function.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-smem-time-sync
   |value=boolean
   |default=enabled
   |description=Time Synchronisation option for output. If true, stream will render as usual, else it will be rendered as fast as possible.
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/stream_out/smem.c}}

.. raw:: mediawiki

   {{Documentation}}
