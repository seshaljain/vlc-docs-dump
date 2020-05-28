This page contains some usability complaints for VLC.

Let's start. \* When cloning video for two monitors, fullscreen mode is
not available. A cloning system like that of version 1.1.0 would be a
lot more useful. The same goes for the wall feature.

-  Hard-to-guess shortcuts to operate with the movie. E.g. shift+arrows
   to rewind. -- it could be greatly improved with arrows-only
   navigation. => This should be easy to do in the new interface.
-  The fullscreen mode is always left between two videos, which is
   annoying when using playlists. It should only be disabled manually.
-  Cannot save a profile for capture device streaming. You must select
   video and audio device every time VLC is started. And you need to go
   thru all the Stream Output wizard pages to select output type and
   destination and encoding. Would be nice to be able to save a capture
   profile and just load it on the initial Open Capture Device dialog
   page (thereby skipping the wizard dialogs). This would be a nice
   productivity enhancement for people who use VLC to stream cameras,
   etc.
-  Playlist sorts using [http://en.wiktionary.org/wiki/ASCIIbetical
   ASCIIbetical] order, ie it plays part 1, part 10, part 2. Actually it
   should sort using human method like part 1, part 2 ... part 10.
-  The VLC plugin for Chrome and Firefox does not have the ability to
   play files behind a password protected source as it does not give the
   option to enter credentials.
-  Update download shuts down software and currently playing music.
   Updates could be set to install after program is closed.
-  Update on Windows creates a VideoLAN start menu folder without asking
   the user if they wish to have one created.

==Resolved complaints== \* {{done}} with [[Simple_Preferences]] -
Preferences are way too big. You can navigate thru them all the day long
and you won't find what you're really looking for.

-  {{done}} Non-responsive shortcuts in WX interface. Sometimes they
   simply don't work (after moving out of the fullscreen). => Qt4 does
   work the same way ? -- no, seems like it somewhat better in QT4,
   still to test more.
-  {{done}} Unresponsive stop/play. Video stops after some amount of
   time. -- kinda better in QT4 interface.
-  {{done}} Adding/removing a video filter during playback (i.e.
   enabling de-interlace or switching de-interlace methods), often
   causes video window to resize.
-  {{done}} Changing video aspect ratio disables video filters that have
   been added during playback (i.e. de-interlace)
-  {{done}} VideoLAN is not accessible for blind people. Don't take
   avantage of the QT accessibility API.
-  {{done}} Blu-Ray menus are not available.
-  {{done}} Parsing video orientation and showing the video upright.
-  {{done}} Offer to resume playback of a video from the point where it
   was previously stopped.
-  Audio cannot be pushed to an AirPlay device.

[[Category:Dev Discussions]]
