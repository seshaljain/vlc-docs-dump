.. raw:: mediawiki

   {{howto|use video from a TV or Video card}}

.. raw:: mediawiki

   {{stub}}

--------------

The following describes how to watch TV with your DVB-Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(tested with DVB-T and the Windows-Version of VLC)

-  find out the frequencies of your location
-  go to File/Open CaptureCard
-  choose DVB DirectShow
-  check your kind of card (DVB-S -C -T)
-  choose first frequency and bandwidth
-  click on play

If your stream has "multiple" (for instance multiple sub channels, or you want to programmatically select a particular audio stream):

-  when the channel plays, select playlist
-  rightclick on the item, which is playing and select information
-  go to stream
-  here you can find all broadcast-channels with their service-ID
-  write them down
-  go to File/Open CaptureCard
-  in the option-line at the bottom append a space (if not there) a : and the keyword "program=", followed by one of the service-IDs
-  it should look like: ...300ms :program=16214
-  click on play
-  that's your channel
-  now you can rename this playing item of the playlist to your station-name
-  and the same with the next service-ID
-  and so on with the next frequency

**Don't forget to save your playlist!**

Have fun!

Spielmops

--------------

The minimal command to transcode from a capture card to a portable MPEG file (this example includes trancoding which may be lessly, be careful) is thus:

``vlc v4l:// :v4l-norm=1: '--sout=#transcode{vcodec=mp1v,vb=2030,audio-sync,acodec=mpga,ab=192,channels=2}:std{access=file,mux=mpeg1,url="out_file.mpg"}'``

These MPEG files have been verified to work with:

-  Windows Media Player 10
-  Apple QuickTime Player 7
-  XINE 1.0
-  ffplay
-  xanim 2.80 (no audio)
