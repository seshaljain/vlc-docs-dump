.. raw:: mediawiki

   {{Module|name=portaudio|type=Audio output|description=Audio output based on the portaudio library (v19)|first_version=0.8|last_version=2.0}}

.. raw:: mediawiki

   {{Historical}}

Introduction
------------

This was an audio output plugin that used the cross-platform portaudio library to render audio on all platforms.

It was removed in VLC 2.0 `Twoflower <Twoflower>`__ due to serious problems such as a dependency on the old aout packet API.\ `1 <https://mailman.videolan.org/pipermail/vlc-devel/2012-January/085344.html>`__ It also had a clock resolution of 1 second, making it impossible for VLC to keep reasonable synchronization with such low precision. Instead of resampling it mostly will discard samples or insert silences.

The Win32 backend of PortAudio was also extremely buggy.

Users should use the plugin for <= Windows XP, (WASAPI) for Windows Vista+, for `macOS <macOS>`__ and (PulseAudio) for Linux.

Options
-------

None.

.. raw:: mediawiki

   {{Documentation footer}}
