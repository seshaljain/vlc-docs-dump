Has anyone written a code for using Infrared Devices with VLC? I'd just love to be able to control VLC from accross the room.

   Use lirc `jb <User:J-b>`__ 03:14, 3 June 2007 (CEST)

== Why is the intf=none interface not mentioned? == Why is the intf=none interface not mentioned, it seems that if you want to use NO interface then 'none' is the best ('dummy' pops up a command line window for me on windows) is this just a windows thing? I've found it to be quite handy

   On my Linux, "-I dummy" do not show a command line interface and "-I none" give me an error, it can't find this interface module. Using vlc --list-verbose, I can only list those "interfaces" modules:

| ``% command line ~= vlc --list-verbose |grep -B 2 interface ``
| ``VLC media player 1.0.0-git Goldeneye                                                                                                           ``
| `` telnet                VLM remote control interface ``
| `` http                  HTTP remote control interface ``
| `` globalhotkeys         Global Hotkeys interface ``
| `` showintf              Show interface with mouse ``
| `` rc                    Remote control interface ``
| `` gestures              Mouse gestures control interface  ``
| `` hotkeys               Hotkeys management interface     ``
| `` motion                motion control interface     ``
| `` signals               POSIX signals handling interface ``
| `` dbus                  D-Bus control interface     ``
| `` telepathy             Telepathy "Now Playing" (MissionControl)``
| `` audioscrobbler        Submission of played songs to last.fm``
| `` inhibit               Power Management Inhibitor    ``
| `` logger                File logging   ``
| `` lua                   Lua Playlist Parser Interface``
| `` screensaver           X Screensaver disabler  ``
| `` dummy                 Dummy interface function``
| `` qt4                   Qt interface``
| `` skins2                Skinnable Interface``
| `` cmml                  CMML annotations decoder``

What's with the rick-roll in "FULL LIST"?
-----------------------------------------

the sub section "full list" first entry has qt4 linked to a troll site... whoever created that link should be banned from ALL wiki's PERMANENTLY! no excuse for such vandalism... the site could inject a virus if it wanted to but looks like they're just making money at expense of people who click --`the Great and Almighty qazwiz <User:Qazwiz>`__ (`talk <User_talk:Qazwiz>`__) 04:03, 16 June 2017 (CEST) --`the Great and Almighty qazwiz <User:Qazwiz>`__ (`talk <User_talk:Qazwiz>`__) 04:08, 16 June 2017 (CEST)

   We do have a problem with vandalism but that was not vandalism :)
   See https://en.wikipedia.org/wiki/Qt_(software)#History_of_Qt or https://en.wikipedia.org/wiki/Trolltech
   It's just their historical company name (now they are "The Qt Company" with their site at https://www.qt.io)
   When you see something strange or wrong on a wiki, you're encouraged to make it better! Don't just leave it! :)

   .. raw:: mediawiki

      {{User:DoesItReallyMatter/real_sig}}

   12:50, 20 January 2019 (CET)
