.. raw:: mediawiki

   {{Mosaic framework}}

.. raw:: mediawiki

   {{Module|name=bridge-out|type=Stream output|first_version=0.8.2|description=Send an [[elementary stream]] to the bridge framework|sc=bridge-out}}

This module sends an `elementary stream <elementary_stream>`__ to the bridge framework. It is used when streaming a mosaic to send the audio stream to the mosaic output.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=sout-bridge-out-id
   |value=integer
   |default=0
   |description=Integer identifier for this elementary stream. This will be used to "find" this stream later.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-bridge-out-in-name
   |value=string
   |default="default"
   |description=Name of the destination bridge-in. If you do not need more than one bridge-in at a time, you can discard this option.
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/stream_out/bridge.c}}

.. raw:: mediawiki

   {{Documentation footer}}
