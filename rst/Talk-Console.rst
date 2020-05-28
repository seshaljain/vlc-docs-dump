What am I doing wrong here?

::

   C:\telnet 127.0.0.1 4212
   Password:
   Welcome, Master
   > stop : Unknown command
   > pause : Unknown command
   >

I am trying to follow [these commands http://www.videolan.org/doc/streaming-howto/en/ch05.html].

--`Axiom <User:Axiom>`__ 23:00, 10 January 2007 (CET)

   According to someone of the forums, while I was doing the commands were wildly wrong, this `only works in Linux <http://forum.videolan.org/viewtopic.php?p=95378#95378>`__ --`Axiom <User:Axiom>`__ 20:53, 12 January 2007 (CET)

      It seems like to rc interface is really what I need (all I want to do a pause and unpause a video), but how does one go about connecting to that, and does it work on Windows?

All docs I could find:

::

   +----[ Remote control commands ]
   |
   | add XYZ  . . . . . . . . . . add XYZ to playlist
   | playlist . . .  show items currently in playlist
   | play . . . . . . . . . . . . . . . . play stream
   | stop . . . . . . . . . . . . . . . . stop stream
   | next . . . . . . . . . . . .  next playlist item
   | prev . . . . . . . . . .  previous playlist item
   | goto . . . . . . . . . . . .  goto item at index
   | clear . . . . . . . . . . .   clear the playlist
   | status . . . . . . . . . current playlist status
   | title [X]  . . . . set/get title in current item
   | title_n  . . . . . .  next title in current item
   | title_p  . . . .  previous title in current item
   | chapter [X]  . . set/get chapter in current item
   | chapter_n  . . . .  next chapter in current item
   | chapter_p  . .  previous chapter in current item
   |
   | seek X . seek in seconds, for instance `seek 12'
   | pause  . . . . . . . . . . . . . .  toggle pause
   | fastforward  . . . . . .  .  set to maximum rate
   | rewind  . . . . . . . . . .  set to minimum rate
   | faster . . . . . . . .  faster playing of stream
   | slower . . . . . . . .  slower playing of stream
   | normal . . . . . . . .  normal playing of stream
   | f [on|off] . . . . . . . . . . toggle fullscreen
   | info . . .  information about the current stream
   | get_time . . seconds elapsed since stream's beginning
   | is_playing . .  1 if a stream plays, 0 otherwise
   | get_title . . .  the title of the current stream
   | get_length . .  the length of the current stream
   |
   | volume [X] . . . . . . . .  set/get audio volume
   | volup [X]  . . . . .  raise audio volume X steps
   | voldown [X]  . . . .  lower audio volume X steps
   | adev [X] . . . . . . . . .  set/get audio device
   | achan [X]. . . . . . . .  set/get audio channels
   | menu [on|off|up|down|left|right|select] use menu
   |
   | marq-marquee STRING  . . overlay STRING in video
   | marq-x X . . . . . . . . . . . .offset from left
   | marq-y Y . . . . . . . . . . . . offset from top
   | marq-position #. . .  .relative position control
   | marq-color # . . . . . . . . . . font color, RGB
   | marq-opacity # . . . . . . . . . . . . . opacity
   | marq-timeout T. . . . . . . . . . timeout, in ms
   | marq-size # . . . . . . . . font size, in pixels
   |
   | time-format STRING . . . overlay STRING in video
   | time-x X . . . . . . . . . . . .offset from left
   | time-y Y . . . . . . . . . . . . offset from top
   | time-position #. . . . . . . . relative position
   | time-color # . . . . . . . . . . font color, RGB
   | time-opacity # . . . . . . . . . . . . . opacity
   | time-size # . . . . . . . . font size, in pixels
   |
   | logo-file STRING . . .the overlay file path/name
   | logo-x X . . . . . . . . . . . .offset from left
   | logo-y Y . . . . . . . . . . . . offset from top
   | logo-position #. . . . . . . . relative position
   | logo-transparency #. . . . . . . . .transparency
   |
   | mosaic-alpha # . . . . . . . . . . . . . . alpha
   | mosaic-height #. . . . . . . . . . . . . .height
   | mosaic-width # . . . . . . . . . . . . . . width
   | mosaic-xoffset # . . . .top left corner position
   | mosaic-yoffset # . . . .top left corner position
   | mosaic-align 0..2,4..6,8..10. . .mosaic alignment
   | mosaic-vborder # . . . . . . . . vertical border
   | mosaic-hborder # . . . . . . . horizontal border
   | mosaic-position {0=auto,1=fixed} . . . .position
   | mosaic-rows #. . . . . . . . . . .number of rows
   | mosaic-cols #. . . . . . . . . . .number of cols
   | mosaic-keep-aspect-ratio {0,1} . . .aspect ratio
   |
   | check-updates [newer] [equal] [older]
   |               [undef] [info] [source] [binary] [plugin]
   |
   | help . . . . . . . . . . . . . this help message
   | longhelp . . . . . . . . . a longer help message
   | logout . . . . .  exit (if in socket connection)
   | quit . . . . . . . . . . . . . . . . .  quit vlc
   |
   +----[ end of help ]

--`Axiom <User:Axiom>`__ 21:18, 12 January 2007 (CET)
