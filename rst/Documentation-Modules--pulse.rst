.. raw:: mediawiki

   {{Module|name=pulse|type=Audio output|os=Linux|description=[[wikipedia:PulseAudio|PulseAudio]] audio output}}

Shortcuts to this module include ``pulseaudio`` and ``pa``. Basic PulseAudio *input* support was added in VLC 2.0.0.

Introduction
------------

PulseAudio is a sound server associated mainly with GNU/Linux users, but it can also be used on \*BSD and macOS. The pulse and modules are two modern options (there might be others) for audio output on Linux. The and modules were removed prior to the release of VLC 1.0.0.

Options
-------

None.

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/audio_output/pulse.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/audio_output/vlcpulse.c}}

   (separate module, support library for `libVLC <libVLC>`__ plugins)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/pulse.c}}

.. raw:: mediawiki

   {{Documentation footer}}
