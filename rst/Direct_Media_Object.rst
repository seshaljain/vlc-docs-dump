{{ mmwiki \| label1=Direct Media Object \| Microsoft_Direct_Media_Object_API }}

Aka. MS DMO API, it is an API for various codecs and other Direct Media Objects.

Integration in VLC
------------------

Using DMO, can use external codecs to read video it would not be able to without, for example many `Windows Media <Windows_Media>`__ codecs that vlc has no native plugin for, like Microsoft Screen codecs or Microsoft Image codecs.

Windows
~~~~~~~

Use it with the **--codec dmo** switch from command-line or activate it in the preferences (**Tools -> Preferences...** and **Show settings: All** and **Input/Codecs -> Other codecs** and tick **Prefer system plugins over VLC**, press Save and restart VLC after the change).

Linux
~~~~~

Under linux, you can use them with the --enable-loader switch that uses Wine's emulation. You have to put the Windows Media dlls in the /usr/win32 folder.

`Category:Codecs <Category:Codecs>`__
