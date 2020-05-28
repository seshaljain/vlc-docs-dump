.. raw:: mediawiki

   {{Module|name=auhal|type=Audio output|os=macOS|description=HAL AudioUnit output}}

The option ``macosx-audio-device`` is obsolete since VLC 2.2.0

Options
-------

.. raw:: mediawiki

   {{Option
   |name=auhal-volume
   |value=integer
   |min=0
   |max=512
   |default=256
   |description=Audio volume
   }}

.. raw:: mediawiki

   {{Option
   |name=auhal-audio-device
   |value=string
   |default=""
   |description=Last audio device
   }}

.. raw:: mediawiki

   {{Option
   |name=auhal-warned-devices
   |value=string
   |default=""
   |description=NULL
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/audio_output/auhal.c}}

.. raw:: mediawiki

   {{Documentation}}
