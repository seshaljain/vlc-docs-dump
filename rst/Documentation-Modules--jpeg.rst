\__NOTOC_\_

Decoder
-------

.. raw:: mediawiki

   {{Module|name=jpeg|type=Access demux|first_version=2.2.0|description=[[JPEG]] image decoder through libjpeg|sc=none}}

.. raw:: mediawiki

   {{VLC}}

previously decoded JPEGs through the images demuxer (introduced in VLC 2.0.0).

Options
~~~~~~~

None.

Encoder
-------

.. raw:: mediawiki

   {{Module|name=jpeg|type=Muxer|first_version=2.2.0|description=[[JPEG]] image encoder through libjpeg|sc=jpeg}}

.. _options-1:

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-jpeg-quality
   |value=integer
   |min=0
   |max=100
   |description=Quality level for encoding (this can enlarge or reduce output image size)
   }}

.. raw:: mediawiki

   {{Clear}}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/jpeg.c}}

.. raw:: mediawiki

   {{Documentation}}
