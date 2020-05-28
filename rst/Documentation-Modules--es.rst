Demux
-----

.. raw:: mediawiki

   {{See also|Documentation:Modules/a52}}

.. raw:: mediawiki

   {{Module|name=es|type=Access demux|description=[[MPEG-1|MPEG-I]]/[[MPEG-2|II]]/[[MPEG-4|4]] / [[A52]] / [[DTS]] / MLP audio|sc=mpga|sc2=mp3|sc3=m4a|sc4=mp4a|sc5=aac|sc6=ac3|sc7=a52|sc8=eac3|sc9=dts|sc10=mlp|sc11=thd}}

Options
~~~~~~~

None.

MPEG-4 video
~~~~~~~~~~~~

.. raw:: mediawiki

   {{Module|name=es|type=Access demux|description=[[MPEG-4]] video|sc=m4v|sc2=mp4v}}

.. _options-1:

Options
^^^^^^^

.. raw:: mediawiki

   {{Option
   |name=es-fps
   |value=float
   |default=25
   |description=This is the [[frame rate]] used as a fallback when playing MPEG video [[elementary stream]]s.
   }}

.. raw:: mediawiki

   {{Clear}}

Stream output
-------------

.. raw:: mediawiki

   {{Module|name=es|type=Stream output|description=[[Elementary stream]] output|sc=es}}

As of VLC 2.2.0 all elementary streams are streamed by default. This can be overridden with ``--no-sout-all``.

.. _options-2:

Options
~~~~~~~

Generic
^^^^^^^

.. raw:: mediawiki

   {{Option
   |name=sout-es-access
   |value=string
   |description=This is the default output access method that will be used
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-es-mux
   |value=string
   |description=This is the default muxer method that will be used
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-es-dst
   |value=string
   |description=This is the default output URI
   }}

Audio
^^^^^

.. raw:: mediawiki

   {{Option
   |name=sout-es-access-audio
   |value=string
   |description=This is the output access method that will be used for audio
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-es-mux-audio
   |value=string
   |description=This is the muxer that will be used for audio
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-es-dst-audio
   |value=string
   |description=This is the output URI that will be used for audio
   }}

Video
^^^^^

.. raw:: mediawiki

   {{Option
   |name=sout-es-access-video
   |value=string
   |description=This is the output access method that will be used for video
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-es-mux-video
   |value=string
   |description=This is the muxer that will be used for video
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-es-dst-video
   |value=string
   |description=This is the output URI that will be used for video
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/mpeg/es.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/stream_out/es.c}}

.. raw:: mediawiki

   {{Documentation}}
