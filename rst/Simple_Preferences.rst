| Discussion finished.
| Discuss on the mailing-list now about what is already implemented :=)

Read this first
---------------

The current preferences use a tree that matches the vlc internal mechanisms. The new preferences don't have to use this tree. We can use whatever we want. My first thought is a 1-level sorting, with the main topics displayed with images on the left pane and preferences pages on the right pane.

We can select preferences items one by one, we don't need the full pages that are currently used

VLC definitively needs a "simple" preferences window. Here is a list of some of the settings which would be needed:

Now, proceed
------------

(?) = to be decided

-  Audio

   -  Enable Audio
   -  Default audio volume
   -  Use S/PDIF when available
   -  Force detection of Dolby surround

      -  Filters

         -  Equalizer

            -  Equalizer preset

         -  Headphone effect
         -  Volume normalizer
         -  Parmetric equalizer

      -  Output modules (?) -- Disagree. Only needs to be modified in case of problems -- `User:Zorglub <User:Zorglub>`__ --> It's still one of the options which many people have to change, having it handy will be useful -- `User:DJ <User:DJ>`__. If we show it up, we should only include really useful modules, like DirectX/Waveout only for aout under windows. Don't show file and dummy for instance `User:Zorglub <User:Zorglub>`__ . I agree with last remark `J-b <User:J-b>`__
      -  DirectX Audio output -- It'd be best to not have any "module specific" option in these simple prefs. We could have an "Output device" option ... which could be shared by each of the audio output modules. -- `User:Dionoea <User:Dionoea>`__. Very hard to do. Much simpler is to ask for all of them to show. Only those compiled in will show up. Very easy. `User:Zorglub <User:Zorglub>`__

         -  Output device

      -  Visualizations

-  Video

   -  Enable video output
   -  Full screen video output
   -  Skip Frames (?) -- Agree `J-b <User:J-b>`__
   -  Overlay video output
   -  Always on top
   -  Video snapshot directory
   -  Video snapshot format
   -  aspect ratio (?) -- Disagree. Is a seldom used function -- `User:DJ <User:DJ>`__.
   -  Windows decorations (?) -- Agree `J-b <User:J-b>`__

      -  Video filters
      -  Output module -- Disagree. Only needs to be modified in case of problems -- `User:Zorglub <User:Zorglub>`__ --> It's still one of the options which many people have to change, having it handy will be usefull -- `User:Dionoea <User:Dionoea>`__ I agree with dionoea `J-b <User:J-b>`__

         -  Image file
         -  Open GL
         -  DirectX

            -  Name of desired display device
            -  Enable wallpaper mode (?) -- Agree `J-b <User:J-b>`__

-  Input / Codecs

   -  Audio language
   -  Subtitle language
   -  DVD device -- IMO, the devices should be detected and listed in the Open dialog box. And if really needed, the options would still be in the full preferences. They could also be remembered from one session to the other -- `User:ipkiss <User:ipkiss>`__
   -  VCD device
   -  Audio CD device
   -  UDP port -- err ... what does that mean ? -- `User:Dionoea <User:Dionoea>`__ Means nothing here `J-b <User:J-b>`__
   -  HTTP caching -- why would we only include http caching and not all other caching options ? -- `User:Dionoea <User:Dionoea>`__ Because that's almost the only one people will really want to change. We might want to add MMS. `User:Zorglub <User:Zorglub>`__ -- Has been added with a Network-caching `J-b <User:J-b>`__ 00:34, 19 February 2007 (CET)

-  Stream output (DEPRECATED)

   -  Keep stream output open -- That shouldn't be in the prefs but in the stream configuration wizards and dialogs -- `User:Dionoea <User:Dionoea>`__ Is there basic cases where we don't want to keep it open. I would be to changed the default to true in libvlc -- `Xtophe <User:Xtophe>`__. Has been changed.

-  Advanced -- We don't want to see a Advanced in Simple Prefs `J-b <User:J-b>`__ 00:34, 19 February 2007 (CET)

   -  Allow only one running instance

      This allows users to use more than one VLC player at a time.

-  

   -  Allow only one running instance when started from file (?) -- i kind of agree with ipkiss that this option shouldn't exist anyway ... i guess that i'll remove it and change the default value for "Allow only one running instance". People who want more than one instance can change the prefs -- `User:Dionoea <User:Dionoea>`__.. NOoooo please don't. Current behaviour is optimal (but we certainly don't want to show this in simple prefs) ! `User:Zorglub <User:Zorglub>`__ -- No too `J-b <User:J-b>`__
   -  Enqueue items to playlist when in one instance mode

-  Playlist -- Do these options really need to be in the prefs ? couldn't we just leave them in the playlist dialog/main controller and remember the state when quiting ? -- `User:Dionoea <User:Dionoea>`__. These options are indeed useless here. Just add change_autosave() on them `User:Zorglub <User:Zorglub>`__ Is it already done ? `J-b <User:J-b>`__ Already done on OSX (by myself) and QT4 (by zorglub) for sure, needs checking in wx. `feepk <User:Fkuehne>`__

   -  Play files randomly forever
   -  Repeat all
   -  Repeat current item
   -  Play and stop

-  Interface

   -  Language
   -  Show advanced options (DEPRECATED) -- This is "Complex preferences" specific so it shouldn't be in the "simple prefs" -- `User:Dionoea <User:Dionoea>`__

-  

   -  ffmpeg-hq ? -- Is this out of place? I can't find it in this context -- `User:DJ <User:DJ>`__. It's currently not in video, but codecs, but we are free to put whatever we want wherever. `User:Zorglub <User:Zorglub>`__. Isn't that going to get kinda confusing? `User:DJ <User:DJ>`__. Nope :) `User:Zorglub <User:Zorglub>`__

-  Subtitles

   -  default encoding
   -  size
   -  color
   -  font

-  HTTP proxy

-  HotKeys !!!

`Category:Dev Discussions <Category:Dev_Discussions>`__
