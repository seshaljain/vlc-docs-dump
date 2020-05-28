.. raw:: mediawiki

   {{Module|name=stream_out_standard|type=Stream output|description=Standard stream output module|sc=standard|sc2=std}}

The option ``sout-standard-group`` was deprecated in 2.1.0. The option ``sout-standard-phone`` was deprecated in 3.0.0.

.. raw:: mediawiki

   {{Option
   |name=sout-standard-access
   |value=string
   |default=""
   |description=Output method to use for the stream.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-standard-mux
   |value=string
   |default=""
   |description=[[Muxer]] to use for the stream.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-standard-dst
   |value=string
   |default=""
   |description=Destination (URL) to use for the stream. Overrides path and bind parameters.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-standard-bind
   |value=string
   |default=""
   |description=Address to bind to (helper setting for dst) address:[[port]] to bind vlc to listening incoming streams. Helper setting for dst, <code>dst{{=}}

bind+'/'+path. dst-parameter overrides this. }} bind+'/'+path. dst-parameter overrides this. }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/stream_out/standard.c}}

.. raw:: mediawiki

   {{Documentation footer}}
