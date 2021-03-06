This page contains list of common questions and problems (FAQ aka Frequently asked questions) that `Windows <Windows>`__ users have about `VLC media player <VLC_media_player>`__ 0.9.x.

Video output related questions and problems
-------------------------------------------

Why does VLC only give black, white or garbled video output?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usually the problem lies in display adapter drivers. If you are too scared to update your display adapter drivers, you can change VLC settings to make video work. If you are using Windows XP or older the easiest fix is usually to disable **Accelerated video output/Overlay video output** which can be found first opening **Tools -> Preferences...** and then choosing **Video**. After you have unticked the Accelerated video output, press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled. `Image about Overlay video output setting <http://raiska.comeze.com/tutorials/vlc092/11a.png>`__

If disabling Overlay video output doesn't help, then the next step is to change video output module. Open **Tools -> Preferences...** (set Show Settings to All) and then choosing **Video -> Output module**. There are multiple output modules you can use. For Windows XP and younger you can try **DirectX 3D**, **DirectX**, **OpenGL** and **Windows GDI** video output modules. With Windows Vista DirectX and Windows GDI output modules will disable Aero so if you want to use Aero, please use DirectX 3D (should be default). Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled. `Image about video output modules setting <http://raiska.comeze.com/tutorials/vlc092/11b.png>`__

Video shows green, blue or red lines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See above.

How can I adjust brightness or contrast?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can adjust brightness, contrast and other settings via **Extended settings**. Open **Tools -> Extend Settings...** to adjust these settings (**Video Effects -> Basic** and tick **Image adjust**). Changes should show up realtime.

How can I keep the brightness and contrast adjustments in memory forever?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open **Tools -> Preferences...** (set Show Settings to All) and then choosing **Video -> Filters -> Image Adjust** and set values you want to use (trial and error).

Can I set file specific brightness or contrast?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, but it isn't that easy. You have to create VLC shortcut or bat file with proper settings. More info can be found from `this <http://forum.videolan.org/viewtopic.php?f=14&t=46202#p152964>`__ thread

How do I set the default deinterlace method?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Tools -> Preferences...** (Show settings: All) **Video -> Filters** and tick **Deinterlacing** video filter from under **Video output filter module** (NOT FROM UNDER Video filter module!). Then **Video -> Filters -> Deinterlace** and choose the default mode. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled. `1 <http://img399.imageshack.us/img399/4220/vlcdeinterlace01hc2.png>`__ image showing the Video output filter module part

Audio output related questions and problems
-------------------------------------------

Crackles, pops, hizzes and other audio anomalies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you hear some unwanted audio problems you can try another audio output module to see if that solves the issue. Open **Tools -> Preferences...** (set Show Settings to All) and then choosing **Audio -> Output module**. There are multiple output modules you can use for audio. **DirectX** and **Win32 waveOut** should work in most cases. Unfortunately there isn't an ASIO support in VLC. `Image about audio output modules setting <http://raiska.comeze.com/tutorials/vlc092/10b.png>`__

Crackles, pops, hizzes and other audio anomalies with SPDIF passthrough
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SPDIF passthrough of Dolby Digital (AC3) and DTS audiotracks don't work with all soundcards. **Win32 waveOut** output module should work better with SPDIF.

I don't hear dialog, conversations etc. while playing 5.1 audio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure you have select proper speaker setup from Windows audio settings or from soundcard control panel. If you have done so, make sure VLC also has right settings. **Audio -> Audio Device** to select proper speaker settings during playback.

How do I adjust audio delay?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

During playback you can press **k** or **j** to adjust audio delay (adjust step is 50 ms).

How can I play external audio track with video?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Media -> Advanced Open File...** and select the video file and after that tick **Show more options** and then **Play another media synchronously...** and select the audio file you want to use. Then when playing the video go to **Audio -> Audio Track -> Track 2** to select the second (or whichever it is) audio track.

(Graphical) user interface related questions and problems
---------------------------------------------------------

How can I separate playback controls from playback window?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to **Tools -> Preferences...** (set Show Settings to All) and **Video** and untick **Embedded video** selection. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

How can I make skinned interface my default interface?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to **Tools -> Preferences...** (set Show Settings to All) and **Interface -> Main interfaces** and from **Interface module** dropdown box select **Skinnable Interface**. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled. `Image about Skinnable Interface setting <http://raiska.comeze.com/tutorials/vlc092/20.png>`__

Can I jump to certain time?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use **--start-time** from command line when you start VLC. There is also **Playback -> Go to specific time...** option in GUI.

How can I change UI language?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use **Tools -> Preferences...** (set Show Settings to All) and **Interface** and select correct language from **Language** drop down list. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

Also you can use **--language=** from command line if you can't navigate with current language or you want to use batch files/scripts. for example: **vlc --language=en** to get English. Other options are auto, en, ar, pt_BR, en_GB, ca, zh_TW, cs, da, nl, fi, fr, gl, ka, de, he, hu, it, ja, ko, ms, oc, fa, pl, pt_PT, ro, ru, zh_CN, sr, sk, sl, es, sv, tr

How can I disable fullscreen controller?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use **Tools -> Preferences...** (set Show Settings to All) and **Interface -> Main interfaces -> Qt** and untick **Show a controller in fullscreen mode** option. `Image about fullscreen controller setting <http://raiska.comeze.com/tutorials/vlc092/25.png>`__

Why doesn't the time slider show up?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you use WindowBlinds or similar custom skin engine, it usually breaks QT4 interface in VLC. So either disable that engine with VLC or change VLCs GUI to something else (like skins2).

How can I disable showing of the filename when video starts?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to **Tools -> Preferences...** (set Show Settings to All) and **Video** and untick **Show media title on video**. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

How do I disable showing of the Privacy and Network Policies dialog during first VLC startup?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Launch VLC with **--no-qt-privacy-ask** command-line option.

Codec compatibility related questions and problems
--------------------------------------------------

How can I identify what codecs the file uses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With VLC, Open the file you want and open **Tools -> Codec Information...**.

VLC doesn't identify used codecs correctly or gives "undf" as codec or I want more information about specs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are multiple video and audio identification tools, but one very useful is tool called `Mediainfo <http://mediainfo.sourceforge.net/>`__.

H.264/MPEG-4 AVC playback is too slow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can speed up the H.264/MPEG-4 AVC playback by disabling loop filter for H.264 decoding. To do this go to **Tools -> Preferences...** (set Show Settings to All) and **Input / Codecs -> Other codecs -> FFmpeg** and in the drop-down box for **Skip the loop filter for H.264 decoding** change it to **All**. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

No Real audio or Real video support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Current stable VLC doesn't play all Real video or audio codecs.

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

If you open DVD with **DVD** selection, try with **No DVD menus** option (aka **dvdsimple**).

Some new DVD movies use copy protection mechanisms that VLC doesn't support. It might help if you rip that movie to hard drive using tools like **DVDFab Decrypter** or **AnyDVD** and use VLC to playback these files from hard drive.

DVD movies don't playback smooth (they stutter, lag, etc.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One thing that might help is increasing the VLC DVD cache. This can be done from **Tools -> Preferences...** (set Show Settings to All) and **Input / Codecs -> Access Modules -> DVD with menus** (or **DVD without menus** if you use dvdsimple method for playback) and increase **Caching value in MS** value to for example to 5000 or to 20000. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

If DVD files from hard drive work better, then check that your DVD drive has DMA enabled (if it is a IDE/ATAPI DVD drive).

Can I play DVD files (VOB+IFO) from hard drive?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes you can. Use **Media -> Open Disc...** and instead of DVD drive, point the location to correct folder by using either **Browse...** button or customize field . For example: **dvd://"c:\movies\BLOOD DIAMOND\VIDEO_TS"**

How do I handle the broken AVI files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some AVI files may give **The AVI file is broken. Seeking not work correctly.Do you want to try to repair(this might take a long time)** dialog. Those AVI files have some issues and you can try to fix those file temporarily with VLC or permanently with other tools. If you don't fix those files, seeking won't work correctly and those files may also crash players.

Can I always perform same repair action?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes you can. This can be done from **Tools -> Preferences...** (set Show Settings to All) and **Input / Codecs -> Demuxers -> AVI** and select the wanted action from **Force index creation** dropdown box. **Ask** is default (it will always ask what you want to do). **Always fix** tries to always fix AVI files and **Never fix** always starts the playback without fixing. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

Can I fix those broken AVI files permanently?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. You can try for example `DivFix++ <http://divfixpp.sourceforge.net/home.htm>`__ or `Virtualdub <http://www.virtualdub.org/>`__ for fixing. Virtualdub `help <http://forum.videolan.org/viewtopic.php?f=14&t=45427&p=143688&hilit=virtualdub#p143688>`__.

Some MP4 or 3GP files don't have audio at all
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If those files have AMR audio (usually ones from mobile phones) they won't work with current stable VLC versions.

Transport stream (TS and M2TS) files or Blu-ray files don't work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is known issue. Some files work and others don't.

No RA, RAM, RMVB support
~~~~~~~~~~~~~~~~~~~~~~~~

Please see `#No Real audio or Real video support <#No_Real_audio_or_Real_video_support>`__.

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

During playback you can press **h** or **g** to adjust subtitle delay (adjust step is 50 ms).

How can I select right subtitle track?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your video has multiple subtitle tracks, you can select the one you would like to see from **Video -> Subtitles Track**.

Can I disable hardcoded or "burned" subtitles with VLC?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No.

Can I change font, font size, style or color?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can with text-based subtitle formats (`Subtitles codecs <Subtitles_codecs>`__). Go to **Tools -> Preferences...** (set Show Settings to All) and **Video -> Subtitles/OSD -> Text renderer** and adjust anything you want. **Font size in pixels** overrides **Relative font size** selection. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

How can I change subtitles text encoding?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you see wrong characters on screen or **failed to convert subtitle encoding** error message you should try to change **Subtitles text encoding** option which can be found from **Tools -> Preferences...** (set Show Settings to All) and **Input / Codecs -> Other codecs -> Subtitles**. Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

How can I select a Unicode font, so I can watch e.g. Chinese subtitles?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to **Tools -> Preferences...** (set Show Settings to All) and **Video -> Subtitles/OSD**, then change the **Text Rendering Module** from **Default** to **Freetype2 font renderer**. After that go to **Video -> Subtitles/OSD -> Text renderer** and choose Unicode font (like **ARIALUNI.TTF**) to Font (you cannot select fonts directly from %windir%\fonts by using Browse... because the default Windows explorer behavior doesn't allow it, but you can copy the font to another folder before selecting it or type location directly to Font field, like C:\WINDOWS\Fonts\ARIALUNI.TTF). Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

General problems and issues
---------------------------

VLC crashes/freezes/BSODs my computer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VLC doesn't do that. Normal apps shouldn't be able to cause issues like these to operating systems. Culprit is usually bad device driver (for example display adapter driver, soundcard driver, chipset driver, network adapter driver etc.) or broken hardware.

How do I reset VLC settings?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you can start VLC, go to **Tools -> Preferences...** and then press **Reset Preferences** and **Save** to reset and save VLC settings. Remember to restart VLC after that to make sure changes are enabled.

If you can't start VLC, go to **%appdata%** folder and delete **vlc** folder from there.

VLC crashes on startup
~~~~~~~~~~~~~~~~~~~~~~

This usually happens because VLC setting files have been corrupted. Resetting VLC settings should fix this.

I messed up my file associations or I want to modify them
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Go to **Tools -> Preferences...** and **Interface** and press **Association Setup**. Or check `this <Windows#How_to_associate_media_files_with_VLC>`__.

Can VLC burn CD, DVD, HD DVD or Blu-ray discs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. You can uses VLC to create a media file, then must use some other utility to burn that media file to DVD, hwoever.

Is VLC legal in all countries?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Probably not. Specially DeCSS module might violate DMCA (and similar laws) and some codecs would require licenses for personal/commercial use. There haven't been any court cases related to VLC but specially companies should make sure they pay license fees to license holders if they use VLC commercially and use patented formats or codecs.

Can I run multiple VLC instances?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes you can. `VLC HowTo/Play multiple instances <VLC_HowTo/Play_multiple_instances>`__

Can I start VLC instances synchronously?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes you can. Check this `thread (command line) <http://forum.videolan.org/viewtopic.php?f=2&t=46110#p146010>`__ or this `thread (GUI) <http://forum.videolan.org/viewtopic.php?f=2&t=39832&start=0&st=0&sk=t&sd=a#p124197>`__.

Latest VLC (0.9.2) doesn't work with Windows Me/98/98se/95/NT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is by design. You need at least Windows 2000 to run latest VLC. For earlier Windows releases, use VLC 0.8.6i.
