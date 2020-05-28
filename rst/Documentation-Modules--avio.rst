.. raw:: mediawiki

   {{See also|RTMP}}

The access output module is a sub-module.

Access
------

.. raw:: mediawiki

   {{Module|name=avio|type=Access|description=[[libavformat]] AVIO access|sc=avio|sc2=rtmp}}

Other shortcuts for this module are `RTMP <RTMP>`__-related and reflect `protocols <protocol>`__: ``rtmpe``, ``rtmps``, ``rtmpt``, ``rtmpte``, ``rtmpts``.

.. raw:: mediawiki

   {{Option
   |name=avio-options
   |value=string
   |default=NULL
   |description=Advanced options, in the form <code><nowiki>{opt=val,opt2=val2}</nowiki></code>
   }}

.. raw:: mediawiki

   {{Clear}}

Access output
~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Module|name=avio|type=Access output|description=[[libavformat]] AVIO access output|sc=avio|sc2=rtmp}}

.. raw:: mediawiki

   {{Option
   |name=sout-avio-options
   |value=string
   |default=NULL
   |description=Advanced options, in the form <code><nowiki>{opt=val,opt2=val2}</nowiki></code>
   }}

.. raw:: mediawiki

   {{Clear}}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/avio.c}}

   - (main file)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/avio.h}}

   - (contains module descriptor)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/avcodec/avcommon.h}}

   - (contains text for module options)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=ffmpeg.git|libavformat/avio.h}}

   - (called by modules/access/avio.c and modules/access/avio.h)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=ffmpeg.git|libavformat/avformat.h}}

   - (called by modules/access/avio.h)

.. raw:: mediawiki

   {{Documentation}}
