Demux
-----

.. raw:: mediawiki

   {{Module|name=mjpeg|type=Access demux|description=[[M-JPEG]] camera demuxer}}

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=mjpeg-fps
   |value=float
   |description=This is the desired frame rate when playing MJPEG from a file. Use 0 (this is the default value) for a live stream (from a camera)
   |default=0
   }}

.. raw:: mediawiki

   {{Clear}}

Packetizer
----------

.. raw:: mediawiki

   {{Module|name=mjpeg|type=Packetizer|description=MJPEG video packetizer|sc=none}}

.. _options-1:

Options
~~~~~~~

None.

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/mjpeg.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/packetizer/mjpeg.c}}

.. raw:: mediawiki

   {{Documentation}}
