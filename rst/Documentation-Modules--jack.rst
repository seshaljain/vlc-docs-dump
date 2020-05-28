This module allows to connect to `JACK Audio Connection Kit <JACK_Audio_Connection_Kit>`__.

Access
------

.. raw:: mediawiki

   {{Module|name=jack|type=Access|first_version=0.9.0|os=Unix, Linux, BSD|description=JACK input|sc=jack}}

The option ``--jack-input-caching`` no longer exists, removed with a commitdiff entitled DEMUX)_GET_PTS_DELAY}}.

Audio output
------------

.. raw:: mediawiki

   {{Module|name=jack|type=Audio output|first_version=0.8.5|os=Unix, Linux, BSD|description=JACK audio output|sc=none}}

.. raw:: mediawiki

   {{Option
   |name=jack-auto-connect
   |value=boolean
   |default=enabled
   |description=If enabled, this option will automatically connect sound output to the first writable JACK clients found
   }}

.. raw:: mediawiki

   {{Option
   |name=jack-connect-regex
   |value=string
   |default="system"
   |description=If automatic connection is enabled, only JACK clients whose names match this [[wikipedia:regular expression|regular expression]] will be considered for connection
   }}

.. raw:: mediawiki

   {{Option
   |name=jack-name
   |value=string
   |default=""
   |description=JACK client name
   }}

.. raw:: mediawiki

   {{Clear}}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/jack.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/audio_output/jack.c}}

.. raw:: mediawiki

   {{Documentation}}
