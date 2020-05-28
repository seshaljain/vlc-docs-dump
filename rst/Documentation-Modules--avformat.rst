.. raw:: mediawiki

   {{See also|Documentation:Modules/avcodec}}

`Muxing <Muxing>`__ options are provided as a sub-module and internally depend on the variable ENABLE_SOUT.

Demux
-----

.. raw:: mediawiki

   {{Module|name=avformat|type=Access demux|description=Avformat [[demuxer]]}}

.. raw:: mediawiki

   {{Option
   |name=avformat-format
   |value=string
   |default=NULL
   |description=Internal [[libavcodec]] format name
   }}

.. raw:: mediawiki

   {{Option
   |name=avformat-options
   |value=string
   |default=NULL
   |description=Advanced options, in the form <kbd>{opt=val,opt2=val2}</kbd>
   }}

Mux
---

.. raw:: mediawiki

   {{Module|name=avformat|type=Muxer|description=Avformat [[muxer]]}}

.. raw:: mediawiki

   {{Option
   |name=sout-avformat-mux
   |value=string
   |default=NULL
   |description=Force use of a specific avformat muxer
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-avformat-options
   |value=string
   |default=NULL
   |description=Advanced options, in the form <kbd>{opt=val,opt2=val2}</kbd>
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-avformat-reset-ts
   |value=boolean
   |default=disabled
   |description=The muxed content will start near a 0 [[timestamp]]
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFolder|modules/demux/avformat}}

   (folder)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/avformat/avformat.c}}

   (file)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/avcodec/avcommon.h}}

   (header, defines AV_OPTIONS_LONGTEXT and AV_RESET_TS_LONGTEXT shown here)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/avformat/avformat.h}}

   (header, defines MUX_LONGTEXT and FORMAT_LONGTEXT shown here)

.. raw:: mediawiki

   {{Documentation}}
