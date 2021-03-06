This page contains list of common questions and problems (FAQ aka Frequently asked questions) that `Windows <Windows>`__ users have about `VLC media player <VLC_media_player>`__ 0.8.6.

Video output related questions and problems
-------------------------------------------

Why does VLC only give black, white or garbled video output?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usually the problem lies in display adapter drivers. If you are too scared to update your display adapter drivers you can change VLC settings to make video work. If you are using Windows XP or older the easiest fix is usually to disable **Overlay video output** which can be found first opening **Settings -> Preferences...** and then choosing **Video**. After you have unticked the Overlay video output, press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled. `Image about Overlay video output setting <http://koti.mbnet.fi/raiska/tutorials/vlc/11a.png>`__

If disabling Overlay video output doesn't help the next step is to change video output module. Open **Settings -> Preferences...** and then choosing **Video -> Output module** (remember to tick **Advanced options** box). There are multiple output modules you can use. For Windows XP and younger you can try **DirectX 3D**, **DirectX**, **OpenGL** and **Windows GDI** video output modules. With Windows Vista DirectX and Windows GDI output modules will disable Aero so if you want to use Aero, please use DirectX 3D (should be default). Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled. `Image about video output modules setting <http://koti.mbnet.fi/raiska/tutorials/vlc/11b.png>`__

Direct3D video output is a bit blurry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is known issue that has been fixed in latest `Nightly builds <http://nightlies.videolan.org/>`__.

Video shows green, blue or red lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See `VSG:Video:VisualErrors <VSG:Video:VisualErrors>`__

How can I adjust brightness or contrast?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can adjust brightness, contrast and other settings via **Extend GUI**. Open **Settings -> Extend GUI** to adjust these settings. Changes should show up realtime.

Can I set file specific brightness or contrast?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, but it isn't that easy. You have to create VLC shortcut or bat file with proper settings. More info can be found from `this <http://forum.videolan.org/viewtopic.php?f=14&t=46202#p152964>`__ thread

Audio output related questions and problems
-------------------------------------------

Crackles, pops, hizzes and other audio anomalies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you hear some unwanted audio problems you can try another audio output module to see if that solves the issue. Open **Settings -> Preferences...** and then choosing **Audio -> Output module** (remember to tick **Advanced options** box). There are multiple output modules you can use for audio. **DirectX** and **Win32 waveOut** should work in most cases. Unfortunately there isn't an ASIO support in VLC.

Crackles, pops, hizzes and other audio anomalies with SPDIF passthrough
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SPDIF passthrough of Dolby Digital (AC3) and DTS audiotracks don't work with all soundcards. **Win32 waveOut** output module should work better with SPDIF and you can also try latest `Nightly builds <http://nightlies.videolan.org/>`__ with Win32 waveOut.

I don't hear dialog, conversations etc. while playing 5.1 audio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure you have select proper speaker setup from Windows audio settings or from soundcard control panel. If you have done so, make sure VLC also has right settings. **Audio -> Audio Device** to select proper speaker settings.

How do I adjust audio delay?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

During playback you can press **Ctrl + k** or **Ctrl + l** to adjust audio delay (adjust step is 50 ms).

(Graphical) user interface related questions and problems
---------------------------------------------------------

How can I separate playback controls from playback window?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to **Settings -> Preferences** and **Interface -> Main interfaces -> wxWidgets** and untick **Embed video in interface** selection. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

How can I make skinned interface my default interface?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to **Settings -> Preferences** and **Interface -> Main interfaces** and from **Interface module** dropdown box select **Skinnable Interface**. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

My remote control, media keys or special input device can't control VLC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Current VLC Hotkeys feature doesn't support special mediakeys so you have to bind keys to regular keyboard keys. Latest `Nightly builds <http://nightlies.videolan.org/>`__ support mediakeys.

My remote control, media keys or special input device can't control VLC (nightlies)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Make sure you disable other software that might capture those keys while you set those keys in VLC (for example Winamp may cause issues).

My VLC Equalizer settings aren't saved when I close VLC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is known issue. There isn't any workaround for this in current stable releases.

Can I jump to certain time?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

With stable builds only option is to use **--start-time** from command line when you start VLC. `Nightly builds <http://nightlies.videolan.org/>`__ have new **Playback -> Go to specific time...** option in GUI.

How can I change UI language?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use **Settings -> Preferences** and **Interface** and select correct language from **Language** drop down list. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

Also you can use **--language=** from command line if you can't navigate with current language or you want to use batch files/scripts. for example: **vlc --language=en** to get English. Other options are auto, en, ar, pt_BR, en_GB, ca, zh_TW, cs, da, nl, fi, fr, gl, ka, de, he, hu, it, ja, ko, ms, oc, fa, pl, pt_PT, ro, ru, zh_CN, sr, sk, sl, es, sv, tr

Codec compatibility related questions and problems
--------------------------------------------------

How can I identify what codecs the file uses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With VLC, Open the file you want and open **View -> Stream and Media Info** and go to **Advanced information** tab.

VLC doesn't identify used codecs correctly or gives "undf" as codec or I want more information about specs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are multiple video and audio identification tools, but one very useful is tool called `Mediainfo <http://mediainfo.sourceforge.net/>`__.

H.264/MPEG-4 AVC playback is too slow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can speed up the H.264/MPEG-4 AVC playback by disabling loop filter for H.264 decoding. To do this go to **Settings -> Preferences** and **Input / Codecs -> Other codecs -> FFmpeg** (remember to tick **Advanced options** box) and in the drop-down box for **Skip the loop filter for H.264 decoding** change it to **All**. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

H.264/MPEG-4 AVC interlaced content crashes VLC (MBAFF and PAFF)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is known issue. Current stable VLC versions don't support interlaced H.264/MPEG-4 AVC content. Latest `Nightly builds <http://nightlies.videolan.org/>`__ should support most interlaced H.264/MPEG-4 AVC videos.

No Real audio or Real video support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Current stable VLC doesn't play all Real video or audio codecs but support has gotten little better on latest `Nightly builds <http://nightlies.videolan.org/>`__.

Why can't VLC use CoreAVC, FFDshow, AC3filter, etc. codecs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VLC only uses build in codecs so it doesn't support VfW or DirectShow APIs for codecs.

But you support `DMO <DMO>`__ (Direct Media Object) module for WMV video and WMA audio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

WMV and WMA are exceptions to this external codec support.

File and media format compatibility related questions and problems
------------------------------------------------------------------

Some DVD movies don't work at all or they crash/freeze to menu or playback
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you open DVD with **DVD (menus)** selection, try just plain **DVD** option (aka **dvdsimple**).

Some new DVD movies use copy protection mechanisms that VLC doesn't support. It might help if you rip that movie to hard drive using tools like DVDFab Decrypter or AnyDVD and use VLC to playback these files from hard drive.

DVD movies don't playback smooth (they stutter, lag, etc.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One thing that might help is increasing the VLC DVD cache. This can be done from **Settings -> Preferences** and **Input / Codecs -> Access Modules -> DVD with menus** (or **DVD without menus** if you use dvdsimple method for playback) (remember to tick **Advanced options** box) and increase **Caching value in MS** value to for example to 5000 or to 20000. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

Can I play DVD files (VOB+IFO) from hard drive?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes you can. Use **File -> Open Disc...** and instead of DVD drive, point the location to correct folder by using customize field (Nightly build also has **Browse...** button). For example: **dvd://"c:\movies\BLOOD DIAMOND\VIDEO_TS"**

FLV (Flash Video) rewind doesn't work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is known issue. It should be fixed in latest `Nightly builds <http://nightlies.videolan.org/>`__.

How do I handle the broken AVI files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some AVI files may give **The AVI file is broken. Seeking not work correctly.Do you want to try to repair(this might take a long time)** dialog. Those AVI files have some issues and you can try to fix those file temporarily with VLC or permanently with other tools. If you don't fix those files, seeking won't work correctly and those files may also crash players.

Can I always perform same repair action?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes you can. This can be done from **Settings -> Preferences** and **Input / Codecs -> Demuxers -> AVI** and select the wanted action from **Force index creation** dropdown box. **Ask** is default (it will always ask what you want to do). **Always fix** tries to always fix AVI files and **Never fix** always starts the playback without fixing. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

Can I fix those broken AVI files permanently?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. You can try for example `DivFix++ <http://divfixpp.sourceforge.net/home.htm>`__ or `Virtualdub <http://www.virtualdub.org/>`__ for fixing. Virtualdub `help <http://forum.videolan.org/viewtopic.php?f=14&t=45427&p=143688&hilit=virtualdub#p143688>`__.

Some MP4 or 3GP files don't have audio at all
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If those files have AMR audio (usually ones from mobile phones) they won't work with current stable VLC versios. You can try latest `Nightly builds <http://nightlies.videolan.org/>`__ to see if they work better with AMR audio.

MP4 and MKV rewind time is equal to system uptime
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is known issue. It should be fixed in latest `Nightly builds <http://nightlies.videolan.org/>`__.

Transport stream (TS and M2TS) files or Blu-ray files don't work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is known issue. Some MPEG-2 only files work but H.264/MPEG-4 AVC or VC-1 inside guarantees failure.

No RA, RAM, RMVB support
~~~~~~~~~~~~~~~~~~~~~~~~

Please see `No Real audio or Real video support <WindowsFAQ#No_Real_audio_or_Real_video_support>`__.

I have many MKV files in same folder and that seems to cause issues to VLC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is known issue. It should be fixed in latest `Nightly builds <http://nightlies.videolan.org/>`__.

MOD files from my video camera don't work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is known issue. There are currently two workarounds. Either change file extension from .mod to .mpg or remove **libmod_plugin.dll** file from **vlc\plugins** folder.

Is it safe to remove libmod_plugin.dll?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes it is. After removing libmod_plugin.dll you can't listen module music formats like MOD, S3M, XM etc. but nowadays most people don't listen those files at all. If you need to get MOD, S3M, XM etc. support back, then just extract libmod_plugin.dll back to **vlc\plugins** folder from VLC zip file.

Subtitles related questions and problems
----------------------------------------

How do I adjust subtitle delay?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

During playback you can press **Ctrl + h** or **Ctrl + j** to adjust subtitle delay (adjust step is 50 ms).

How can I select right subtitle track?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your video has multiple subtitle tracks, you can select the one you would like to see from **Video -> Subtitles Track**.

Can I disable hardcoded or "burned" subtitles with VLC?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No.

Dragging and dropping the subtitles to VLC disables pause
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is known issue. It will be hopefully fixed in upcoming releases. Only solution is to either open subtitles from **Use a subtitles file** when you open file you want to watch or trust to **Autodetect subtitle files** and name the subtitles in same as the movie (for example, **my_movie.avi** and **my_movie.srt**).

SSA and ASS subtitles look horrible and don't support all styles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is known issue. Support should be better in latest `Nightly builds <http://nightlies.videolan.org/>`__.

Can I change font, font size, style or color?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can with text-based subtitle formats (`Subtitles codecs <Subtitles_codecs>`__). Go to **Settings -> Preferences** and **Video -> Subtitles/OSD -> Text renderer** (remember to tick **Advanced options** box) and adjust anything you want. **Font size in pixels** overrides **Relative font size** selection. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

How can I change subtitles text encoding?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you see wrong characters on screen or **failed to convert subtitle encoding** error message you should try to change **Subtitles text encoding** option which can be found from **Settings -> Preferences** and **Input / Codecs -> Other codecs -> Subtitles**. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

General problems and issues
---------------------------

VLC crashes/freezes/BSODs my computer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VLC doesn't do that. Normal apps shouldn't be able to cause issues like these to operating systems. Culprit is usually bad device driver (for example display adapter driver, soundcard driver, chipset driver, network adapter driver etc.) or broken hardware.

How do I reset VLC settings?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you can start VLC, go to **Settings -> Preferences...** and then press **Reset All** and **Save** to reset and save VLC settings. Remember to restart VLC after that to make sure changes are enabled.

If you can't start VLC, go to **%appdata%** folder and delete **vlc** folder from there.

VLC crashes on startup
~~~~~~~~~~~~~~~~~~~~~~

This usually happens because VLC setting files have been corrupted. Resetting VLC settings should fix this.

I messed up my file associations or I want to modify them
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Check out `Windows#How to associate media files with VLC <Windows#How_to_associate_media_files_with_VLC>`__.

Can VLC burn CD, DVD, HD DVD or Blu-ray discs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No.

Is VLC legal in all countries?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Probably not. Specially DeCSS module might violate DMCA (and similar laws) and some codecs would require licenses for personal/commercial use. There haven't been any court cases related to VLC but specially companies should make sure they pay license fees to license holders if they use VLC commercially and use patented formats or codecs.

Can I run multiple VLC instances?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes you can. `VLC HowTo/Play multiple instances <VLC_HowTo/Play_multiple_instances>`__

Can I start VLC instances synchronously?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes you can. Check this `thread (command line) <http://forum.videolan.org/viewtopic.php?f=2&t=46110#p146010>`__ or this `thread (GUI) <http://forum.videolan.org/viewtopic.php?f=2&t=39832&start=0&st=0&sk=t&sd=a#p124197>`__.

Latest VLC (0.8.6h) doesn't work with Windows Me/98/98se/95
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is known issue. You can either use 0.8.6f or take libwxwidgets.dll from 0.8.6f and copy it to 0.8.6h.
