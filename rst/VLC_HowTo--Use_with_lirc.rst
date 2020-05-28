.. raw:: mediawiki

   {{howto|To use {{VLC}} with an infra red remote control on Linux}}

.. raw:: html

   <div class="widebox">

**Note:** This article is about advanced lirc usage with VLC. For basic stuff please see `Documentation:Modules/lirc <Documentation:Modules/lirc>`__.

.. raw:: html

   </div>

The aim is to have your remote behave the same way as for a television remote: program +/-, volume +/-, jump to position 3 when button 3 is pressed,...

Build-in lirc commands are only for basic control in the movie-playing mode, but I need to use other commands from `RC Interface <RC_Interface>`__ - mainly "goto x" function. So the goal was to be able to use goto function with lirc.

VLC
---

Use a VLC version with lirc enabled.

Start-Up Script
~~~~~~~~~~~~~~~

.. code:: bash

   #start/stop script for lircd+vlc for Kubuntu 6.10
   start() {
      echo "Starting lirc support..."
      sudo setserial /dev/ttyS0 uart none       #serial port down
      sudo /sbin/modprobe lirc_serial           #load module
      sudo /sbin/modprobe lirc_dev           #load module
      sudo /usr/local/sbin/lircd --driver=default --device=/dev/lirc0 --output=/dev/lircd --pidfile=/var/run/lircd.pid --listen  #run lirc daemon
      sudo chmod 666 /dev/lircd                 #access
      sudo irexec -d   #daemon to pass ir commands
   }

   stop() {
      echo "Stoping lirc support..."
      sudo /usr/bin/killall -w lircd                #kill lirc daemon
      sudo /sbin/rmmod lirc_serial              #unload module
      sudo /sbin/rmmod lirc_dev                 #unload module
      sudo setserial /dev/ttyS0 uart 16550A     #serial port up
   }

   restart() {
      stop
      sleep 2
      start
   }

   case "$1" in
   'start')
     start
     ;;
   'stop')
      stop
      ;;
   'restart')
     restart
      ;;
   *)
   echo "usage $0 start|stop|restart"
   esac
   exit 0

Scripts
~~~~~~~

It is necessary to run vlc with rc interface to use all the supported commands (see vlc help). I use this script to run VLC with rc intf. Lircd is loaded and later unloaded. I have a desktop shortcut icon and I had to change properties of the shortcut to run in terminal. The other option is ``vlc --fake-tty`` option, but this uses 100 % CPU :-(

.. code:: bash

   #/bin/bash
   /home/ondra/.vlc/ovladac.sh start
   vlc -I rc --rc-host localhost:12345 /home/ondra/playlist.m3u   
   /home/ondra/.vlc/ovladac.sh stop

I use irexec to pass commands to VLC rc intf. Commands can be passed with netcat: ``echo "vlc_rc_command" | netcat localhost 12345 -q 1`` (q means quit after 1 s). Commands are written in scripts, which are executed with irexec:

Here is a script, which is executed when remote button 1 is pressed. The others are similar.

``{{$}} cat play1.sh``

.. code:: bash

   #!/bin/bash
   echo "goto 0" | netcat localhost 12345 -q 1

.lircrc
-------

   *See also: included with VLC viewable online; it is not part of this guide but it may be more up-to-date*

The last part of the .lircrc file.

There are defined actions for all requested buttons. **irexec** executes concerned shell script.

.. code:: bash

   # remote numbers
   begin
           prog = irexec
           button = 1
           config = /home/ondra/.vlc/play1.sh  &\n
   end

   begin
           prog = irexec
           button = 2
           config = /home/ondra/.vlc/play2.sh  &\n
   end

   begin
           prog = irexec
           button = 3
           config = /home/ondra/.vlc/play3.sh  &\n
   end

   begin
           prog = irexec
           button = 4
           config = /home/ondra/.vlc/play4.sh  &\n
   end

   begin
           prog = irexec
           button = 5
           config = /home/ondra/.vlc/play5.sh  &\n
   end

   begin
           prog = irexec
           button = 6
           config = /home/ondra/.vlc/play6.sh  &\n
   end

   begin
           prog = irexec
           button = 7
           config = /home/ondra/.vlc/play7.sh  &\n
   end

   begin
           prog = irexec
           button = 8
           config = /home/ondra/.vlc/play8.sh  &\n
   end

   begin
           prog = irexec
           button = 9
           config = /home/ondra/.vlc/play9.sh  &\n
   end

   begin
           prog = irexec
           button = 0
           config = /home/ondra/.vlc/play0.sh  &\n
   end
   begin
           prog = irexec
           button = Menu
           config = /home/ondra/.vlc/pause.sh  &\n
   end

This is the complete list of supported keys in VLC 0.8.6:

::

   Fullscreen -> key-toggle-fullscreen
   Play/Pause -> key-play-pause
   Pause only -> key-pause
   Play only -> key-play
   Faster -> key-faster
   Slower -> key-slower
   Next -> key-next
   Previous -> key-prev
   Stop -> key-stop
   Position -> key-position
   Very short backwards jump -> key-jump-extrashort
   Very short forward jump -> key-jump+extrashort
   Short backwards jump -> key-jump-short
   Short forward jump -> key-jump+short
   Medium backwards jump -> key-jump-medium
   Medium forward jump -> key-jump+medium
   Long backwards jump -> key-jump-long
   Long forward jump -> key-jump+long
   Activate -> key-nav-activate
   Navigate up -> key-nav-up
   Navigate down -> key-nav-down
   Navigate left -> key-nav-left
   Navigate right -> key-nav-right
   Go to the DVD menu -> key-disc-menu
   Select previous DVD title -> key-title-prev
   Select next DVD title -> key-title-next
   Select prev DVD chapter -> key-chapter-prev
   Select next DVD chapter -> key-chapter-next
   Quit -> key-quit
   Volume up -> key-vol-up
   Volume down -> key-vol-down
   Mute -> key-vol-mute
   Subtitle delay up -> key-subdelay-up
   Subtitle delay down -> key-subdelay-down
   Audio delay up -> key-audiodelay-up
   Audio delay down -> key-audiodelay-down
   Cycle audio track -> key-audio-track
   Cycle subtitle track -> key-subtitle-track
   Cycle source aspect ratio -> key-aspect-ratio
   Cycle video crop -> key-crop
   Cycle deinterlace modes -> key-deinterlace
   Show interface -> key-intf-show
   Hide interface -> key-intf-hide
   Take video snapshot -> key-snapshot
   Go back in browsing history -> key-history-back
   Go forward in browsing history -> key-history-forward
   Record -> key-record
   Dump -> key-dump
   Crop one pixel from the top of the video -> key-crop-top
   Uncrop one pixel from the top of the video -> key-uncrop-top
   Crop one pixel from the left of the video -> key-crop-left
   Uncrop one pixel from the left of the video -> key-uncrop-left
   Crop one pixel from the bottom of the video -> key-crop-bottom
   Uncrop one pixel from the bottom of the video -> key-uncrop-bottom
   Crop one pixel from the right of the video -> key-crop-right
   Uncrop one pixel from the right of the video -> key-uncrop-right
   Set playlist bookmark 1 -> key-set-bookmark1
   Set playlist bookmark 2 -> key-set-bookmark2
   Set playlist bookmark 3 -> key-set-bookmark3
   Set playlist bookmark 4 -> key-set-bookmark4
   Set playlist bookmark 5 -> key-set-bookmark5
   Set playlist bookmark 6 -> key-set-bookmark6
   Set playlist bookmark 7 -> key-set-bookmark7
   Set playlist bookmark 8 -> key-set-bookmark8
   Set playlist bookmark 9 -> key-set-bookmark9
   Set playlist bookmark 10 -> key-set-bookmark10
   Play playlist bookmark 1 -> key-play-bookmark1
   Play playlist bookmark 2 -> key-play-bookmark2
   Play playlist bookmark 3 -> key-play-bookmark3
   Play playlist bookmark 4 -> key-play-bookmark4
   Play playlist bookmark 5 -> key-play-bookmark5
   Play playlist bookmark 6 -> key-play-bookmark6
   Play playlist bookmark 7 -> key-play-bookmark7
   Play playlist bookmark 8 -> key-play-bookmark8
   Play playlist bookmark 9 -> key-play-bookmark9
   Play playlist bookmark 10 -> key-play-bookmark10 

Can be extracted using this command:

``{{$}} vlc -H --advanced 2>&1 |sed -n '/--key/ {s/^\ *--//; s/^``\ :math:`.*`\ `` <[^>]*>\ *``\ :math:`.*`\ ``$/\2 -> \1/; h}; /^.*[^ ].*-> key/ p; /^ -> key/ { n; s/^[ \t\n]*//M; G; s/\n//; p}'``

Version
-------

This has been written by [User:J-b] using Ondřej Kuda's HowTo.

See also
--------

-  `Original post on VideoLAN forum <http://forum.videolan.org/viewtopic.php?t=30671>`__
-  `Gentoo Wiki's HowTo <http://gentoo-wiki.com/HOWTO_LIRC#Using_LIRC_with_VLC_media_player>`__
-  `Enhanced VLC lirc remote control <http://www.natur.cuni.cz/~kuda/howtos/vlc_lirc.html>`__

`Category:Control VLC <Category:Control_VLC>`__ `Category:GNU/Linux <Category:GNU/Linux>`__
