.. raw:: mediawiki

   {{Module|name=delay|type=Stream output|first_version=2.0.0|description=Delay a [[stream]]|sc=delay}}

Options
-------

.. raw:: mediawiki

   {{Option
   |name=sout-delay-id
   |value=integer
   |default=0
   |description=Specify an identifier integer for this [[elementary stream]].
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-delay-delay
   |value=integer
   |default=0
   |description=Specify a delay (in [[wiktionary:ms|ms]]) for this elementary stream. Positive means delay and negative means advance.
   }}

Examples
--------

From the changelog: ``#delay{id=12,delay=500}:standard...``

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/stream_out/delay.c}}

.. raw:: mediawiki

   {{Documentation footer}}
