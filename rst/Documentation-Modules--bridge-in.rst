.. raw:: mediawiki

   {{Mosaic framework}}

.. raw:: mediawiki

   {{Module|name=bridge-in|type=Stream output|first_version=0.8.2|description=Get [[elementary stream]]s from the bridge framework|sc=bridge-in}}

This module gets all the `elementary streams <elementary_stream>`__ sent to the bridge framework. It is used when streaming a mosaic to attach the audio streams to the mosaic output. \__TOC_\_

Options
-------

.. raw:: mediawiki

   {{Option
   |name=sout-bridge-in-delay
   |value=integer
   |default=0
   |description=Pictures coming from the picture video outputs will be delayed according to this value (in milliseconds, should be &ge; 100 ms). For high values, you will need to raise caching values.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-bridge-in-id-offset
   |value=integer
   |default=8192
   |description=Offset to add to the stream IDs specified in bridge-out to obtain the stream IDs bridge-in will register.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-bridge-in-name
   |value=string
   |default="default"
   |description=Name of this bridge-in instance. If you do not need more than one bridge-in at a time, you can discard this option.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-bridge-in-placeholder
   |value=boolean
   |default=disabled
   |description=If set to true, the bridge will discard all input elementary streams except if it doesn't receive data from another bridge-in. This can be used to configure a placeholder stream when the real source breaks. Source and placeholder streams should have the same format.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-bridge-in-placeholder-delay
   |value=integer
   |default=200
   |description=Delay (in ms) before the placeholder kicks in.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-bridge-in-placeholder-switch-on-iframe
   |value=boolean
   |default=enabled
   |description=If enabled, switching between the placeholder and the normal stream will only occur on [[I-frame]]s. This will remove artifacts on stream switching at the expense of a slightly longer delay, depending on the frequency of I-frames in the streams.
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/stream_out/bridge.c}}

.. raw:: mediawiki

   {{Documentation footer}}
