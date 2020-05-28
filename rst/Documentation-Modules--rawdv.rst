.. raw:: mediawiki

   {{Module|name=rawdv|type=Access|first_version=0.5.0|os=Linux|description=[[DV]] (Digital Video) demuxer|sc=rawdv}}

Options
-------

.. raw:: mediawiki

   {{Option
   |name=rawdv-hurry-up
   |value=boolean
   |default=disabled
   |description=The demuxer will advance [[timestamp]]s if the input can't keep up with the rate
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/rawdv.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/rawdv.h}}

   (helper)

.. raw:: mediawiki

   {{Documentation footer}}
