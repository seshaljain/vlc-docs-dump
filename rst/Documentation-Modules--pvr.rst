.. raw:: mediawiki

   {{Module|name=pvr|type=Access|last_version=2.0.9|os=Linux|description=IVTV MPEG Encoding cards input|sc=pvr}}

| This module was removed with commitdiff .
| The changelog for 2.1.0 notes under the section *Removed modules*:

`` * PVR: IVTV analog TV encoder - use ``\ ```V4L`` <Documentation:Modules/v4l2>`__\ `` instead``

.. raw:: mediawiki

   {{Clear}}

Options
-------

The module did not accept ``--pvr-frequency`` beyond the endpoints given by ``static const int pi_radio_range[2]``: \ ``65000 ≤``\ \ ``x``\ \ ``≤ 108000``\ . This was not mentioned in the help text.

The variables in ``--pvr-norm`` are defined in .

.. raw:: mediawiki

   {{Option
   |name=pvr-device
   |value=string
   |default="/dev/video0"
   |description=[[wikipedia:Personal video recorder|PVR]] video device
   }}

.. raw:: mediawiki

   {{Option
   |name=pvr-radio-device
   |value=string
   |default="/dev/radio0"
   |description=PVR radio device
   }}

.. raw:: mediawiki

   {{Option
   |name=pvr-norm
   |value=integer
   |select={<var>V4L2_STD_UNKNOWN</var>,<var>V4L2_STD_SECAM</var>,<var>V4L2_STD_PAL</var>,<var>V4L2_STD_NTSC</var>}
   |default=<var>V4L2_STD_UNKNOWN</var>
   |description=Norm of the stream (Automatic, SECAM, [[PAL]], or [[NTSC]])
   }}

.. raw:: mediawiki

   {{Option
   |name=pvr-width
   |value=integer
   |default=-1
   |description=Width of the stream to capture (-1 for autodetection)
   }}

.. raw:: mediawiki

   {{Option
   |name=pvr-height
   |value=integer
   |default=-1
   |description=Height of the stream to capture (-1 for autodetection)
   }}

.. raw:: mediawiki

   {{Option
   |name=pvr-frequency
   |value=integer
   |default=-1
   |description=Frequency to capture (in kHz), if applicable
   }}

.. raw:: mediawiki

   {{Option
   |name=pvr-framerate
   |value=integer
   |default=-1
   |description=[[Framerate]] to capture, if applicable (-1 for autodetect)
   }}

.. raw:: mediawiki

   {{Option
   |name=pvr-keyint
   |value=integer
   |default=-1
   |description=Interval between [[keyframe]]s (-1 for autodetect)
   }}

.. raw:: mediawiki

   {{Option
   |name=pvr-bframes
   |value=integer
   |default=-1
   |description=If this option is set, [[B-Frame]]s will be used. Use this option to set the number of B-Frames
   }}

.. raw:: mediawiki

   {{Option
   |name=pvr-bitrate
   |value=integer
   |default=-1
   |description=[[Bitrate]] to use (-1 for default)
   }}

.. raw:: mediawiki

   {{Option
   |name=pvr-bitrate-peak
   |value=integer
   |default=-1
   |description=Peak bitrate in [[VBR]] mode
   }}

.. raw:: mediawiki

   {{Option
   |name=pvr-bitrate-mode
   |value=integer
   |select={0,1}
   |default=-1
   |description=Bitrate mode to use ([[VBR]] or [[CBR]])
   }}

.. raw:: mediawiki

   {{Option
   |name=pvr-audio-bitmask
   |value=integer
   |default=-1
   |description=[[wiktionary:bitmask|Bitmask]] that will get used by the audio part of the card
   }}

.. raw:: mediawiki

   {{Option
   |name=pvr-audio-volume
   |value=integer
   |default=-1
   |description=Audio volume (0-65535)
   }}

.. raw:: mediawiki

   {{Option
   |name=pvr-channel
   |value=integer
   |default=-1
   |description=Channel of the card to use (Usually: 0 - tuner, 1 - composite, 2 - svideo)
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/pvr.c}}

.. raw:: mediawiki

   {{Documentation}}
