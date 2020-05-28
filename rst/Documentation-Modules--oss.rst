oss and audio capture support were removed from and in VLC 1.0.0, but accesses were provided as sub-modules. To emulate old behaviour, use ``--input-slave oss://`` or ``--input-slave alsa://``. The access module reads from ``/dev/dsp``.

Options
-------

Audio output
~~~~~~~~~~~~

.. raw:: mediawiki

   {{Module|name=oss|type=Audio output|os=Linux|description=[[OSS|Open Sound System]] audio output|sc=none}}

.. raw:: mediawiki

   {{Option
   |name=oss-audio-device
   |value=string
   |default=""
   |description=OSS device node path
   }}

.. raw:: mediawiki

   {{Option
   |name=oss-spdif
   |value=boolean
   |default=disabled
   |description=S/PDIF can be used by default when your hardware supports it as well as the audio stream being played
   }}

.. raw:: mediawiki

   {{Clear}}

Access
~~~~~~

.. raw:: mediawiki

   {{Module|name=oss|type=Access|first_version=1.0.0|os=Linux|description=[[OSS]] input|sc=oss}}

.. raw:: mediawiki

   {{Option
   |name=oss-stereo
   |value=boolean
   |default=enabled
   |description=Capture the audio stream in stereo
   }}

.. raw:: mediawiki

   {{Option
   |name=oss-samplerate
   |value=integer
   |default=48000
   |description=[[Sample rate]] of the captured audio stream, in Hz (eg: 11025, 22050, 44100, 48000)
   }}

.. raw:: mediawiki

   {{Clear}}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/audio_output/oss.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/oss.c}}

.. raw:: mediawiki

   {{Documentation footer}}
