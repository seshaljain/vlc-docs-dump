.. raw:: mediawiki

   {{Module|name=waveout|type=Audio output|description=Wave audio output|os=Windows|first_version=0.4}}

Introduction
------------

This is an optionnal audio output for Windows. It can be used when the `DirectSound <Documentation:Modules/directx_aout>`__ module doesn't work.

It uses the normal Multimedia Windows API that is present since Windows 95.

Options
-------

Float32 output
~~~~~~~~~~~~~~

This option allows you to enable or disable the high-quality float32 audio output mode (which is not well supported by some soundcards).

Audio Device Selection
~~~~~~~~~~~~~~~~~~~~~~

This option allows you to select the audio output device listed.

It uses the string name of the audio device.
