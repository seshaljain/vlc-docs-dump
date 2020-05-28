.. raw:: mediawiki

   {{docmod|oss}}

and alsa audio capture support were removed from and in VLC 1.0.0, but accesses were provided as sub-modules. To emulate old behaviour, use ``--input-slave oss://`` or ``--input-slave alsa://``.

In the module options below AOUT_CHANS_FRONT and other variables are defined in . The values are not defined here because of their complexity.

Audio channels in VLC 2.0.1 must be configured manually (bugs) but ``--alsa-audio-channels`` defaults to stereo.

The access module option ``--alsa-format`` has been deprecated since VLC 2.1.0.

HDMI support is planned for VLC 4.0.0 through the ``--alsa-passthrough`` option.

Options
-------

Audio output
~~~~~~~~~~~~

.. raw:: mediawiki

   {{Module|name=alsa|type=Audio output|os=Linux|description=[[ALSA]] audio output|sc=none}}

.. raw:: mediawiki

   {{Option
   |name=alsa-audio-device
   |value=string
   |default=default
   |description=Audio output device (using ALSA syntax)
   }}

.. raw:: mediawiki

   {{Option
   |name=alsa-audio-channels
   |value=integer
   |default=<var>AOUT_CHANS_FRONT</var>
   |description=Channels available for audio output. If the input has more channels than the output, it will be down-mixed. This parameter is ignored when digital pass-through is active
   }}

.. raw:: mediawiki

   {{Clear}}

Access
~~~~~~

.. raw:: mediawiki

   {{Module|name=alsa|type=Access|first_version=1.0.0|os=Linux|description=[[ALSA]] audio capture|sc=alsa}}

.. raw:: mediawiki

   {{Option
   |name=alsa-stereo
   |value=boolean
   |default=enabled
   |description=Stereo
   }}

.. raw:: mediawiki

   {{Option
   |name=alsa-samplerate
   |value=integer
   |default=48000
   |description=[[Sample rate]] (Hertz)
   |select=192000, 176400, 96000, 88200, 48000, 44100, 32000, 22050, 24000, 16000, 11025, 8000, 4000
   }}

.. raw:: mediawiki

   {{Clear}}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/audio_output/alsa.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/alsa.c}}

.. raw:: mediawiki

   {{Documentation footer}}
