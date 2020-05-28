.. raw:: mediawiki

   {{wikipedia|Musical_Instrument_Digital_Interface#Standard MIDI files|label1=Midi files}}

.. raw:: mediawiki

   {{Module|name=smf|type=Demux|description=Standard MIDI Files|first_version=0.9.0}}

Standard MIDI Files (SMF) contain sounds events that indicate the notes and instruments in a musical performance, but do not include the digital waveform of the audio. They usually have the extension ``.mid`` or ``.midi``. To play a MIDI file, software has to synthesize the music, which usually requires reading digital samples of musical instruments from a large file.

Play .mid (MIDI) files in VLC
-----------------------------

.. raw:: mediawiki

   {{Module|name=fluidsynth|type=Codec|description=MIDI synthesis with the FluidSynth library|first_version=0.9.0 (Linux)|first_version=0.9.0 (Linux)<br />1.1.0 (Windows)|last_version=3.0.x (Windows)|os=Linux}}

.. raw:: mediawiki

   {{VLC}}

can play Standard MIDI File (.MID) and RIFF MIDI (.RMI) files since version 0.9.0.

Windows binary builds included MIDI support only in versions from 1.1.0 through 2.0.8. Starting from version 2.1.0, support was dropped due to `security issues <https://trac.videolan.org/vlc/ticket/9486>`__. It was re-activated in VLC 3.0.0.

SoundFonts file
~~~~~~~~~~~~~~~

To playback MIDI files, you need a `SoundFont <wikipedia:SoundFont>`__ file (with extension ``.sf2``). You can download them from either of these two places:

-  http://www.schristiancollins.com/generaluser.php
-  http://sourceforge.net/apps/trac/fluidsynth/wiki/SoundFont

Configure SoundFont in VLC
~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to open VLC's preferences. The preferences window has two display modes called **Simple** and **All**. Choose the display mode called **All**, then go to **Input/Codecs** > **Audio codecs** > **FluidSynth**. Then select the .sf2 file with **Browse** button and save the preferences with **Save** button.

Linux
~~~~~

If the **FluidSynth** codec is not shown in VLC's preferences, you have to install it as well as sound fonts. E.g. on `Ubuntu <Ubuntu>`__ 18.04 and derivatives it is in the **vlc-plugin-fluidsynth** package, while the **fluid-soundfont-gs** and **fluid-soundfont-gm** packages install some sound fonts in ``/usr/share/sounds/sf2``.

`Category:Container <Category:Container>`__
