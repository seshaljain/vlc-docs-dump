.. raw:: mediawiki

   {{howto|create a video file from a DVD using VLC}}

\__TOC_\_ You can use VLC to rip a "raw" video file from a DVD, or you can use VLC to create a condensed "transcoded" video file from a DVD. This page mostly deals with using it to rip a raw video file from the `command line <command_line>`__.

Instructions
------------

Here is an example. You'll need to type this at the command prompt (windows) or terminal (linux), all on one line.

This is how to rip the "raw" video from a DVD, assuming you want to rip your DVD's title ``1`` to filename ``dvdout.mpg``, from drive ``dvd:\``

\ `` ``\ \ `` dvdsimple:///d:#1 --sout "#standard{access=file,mux=ts,dst=dvdout.mpg}" vlc://quit``

the ``vlc://quit`` at the end just tells it to exit after ripping. You can also add a ``--qt-start-minimized``, if desired.

Note that the above doesn't do any transcoding on the video stream, it just basically dumps a verbatim copy to your hard drive. In comparison with other ripping programs, this is sometimes lacking a few frames from the original (up to 10), but is typically pretty accurate. If you want one that is even more accurate, use MPlayer's dumpstream or makemkv.

You may have some luck ripping the DVD from `the GUI <https://www.howtogeek.com/howto/2696/how-to-rip-dvds-with-vlc>`__, as well, though this is a bit tricky [1]. See also note at bottom. Using the GUI may help if you want to both rip and `transcode <transcode>`__ simultaneously, as the above commands only do a raw copy. Recommend using `HandBrake <HandBrake>`__ if you want to do transcoding too. You will also need to check the 'no DVD menus' option, which instructs it to use ``dvdsimple://`` instead of ``dvd://`` which `loops back <https://forum.videolan.org/viewtopic.php?f=2&t=52748>`__ to the main menu after playing the title.

If it stops halfway through, cleaning your disc might help. If it still fails half-way through, it may work better to use ``dvd://`` (in the GUI, that's not check 'no DVD menus') instead of ``dvdsimple://`` but this is probably not a good option as it never stops but loops back to the main menu forever so you will have to stop it manually by monitoring it. Recommend MPlayer's dumpstream in this case.

\ `` ``\ \ `` dvd:///d:#1 --sout "#standard{access=file,mux=ts,dst=dvdout.mpg}" vlc://quit``

It might also help to set the caching value either higher or to ``0`` (in the GUI: under advanced options).

OS X example (you may be able to use ``dvdsimple:///Volumes/volumeName`` as well).

``{{$}} ``\ \ `` dvdsimple:///dev/disk1#1 --sout "#standard{access=file,mux=ts,dst=dvdout.dvdsimple.vlc.mpg}"``

Related
-------

`WindowsFAQ-1.1.x#Some DVD movies don't work at all or they crash/freeze to menu or playback <WindowsFAQ-1.1.x#Some_DVD_movies_don't_work_at_all_or_they_crash/freeze_to_menu_or_playback>`__

`HandBrake <HandBrake>`__ is a free user friendly open source tool for ripping DVD's and simultaneously transcoding (condensing) the output file. It uses VLC by default for ripping if installed on OS X. For windows users handbrake can also use VLC's `libdvdcss <libdvdcss>`__ if you first `install it <https://forum.handbrake.fr/viewtopic.php?f=11&t=16670#p78021>`__.

MPlayer
~~~~~~~

`MPlayer <MPlayer>`__ is another excellent option for ripping a raw mpeg stream from a DVD. See `wikibook instructions <wikibooks:Mplayer#Rip_DVD_to_raw_video>`__ for it.

makemkv
~~~~~~~

MakeMKV is also good for ripping DVD or blu-ray to a raw mpeg file. To select specific titles, count down from the top of the checked title options. The first one at the top is "title 1." After ripping, you could then convert it (to condense/transcode it) by using handbrake or VLC.

If you want to convert makemkv's output to an mpeg file (mpeg-ts) then you could use tsmuxer. OS X users will need a `special version <https://instantitunes.wordpress.com/2010/02/26/use-tsmuxer-on-snow-leopard/>`__ of tsmuxer, however.

ddrescue and vobcopy
~~~~~~~~~~~~~~~~~~~~

Some DVDs have bad sectors as a `copy protection <copy_protection>`__ mechanism, which makes some tools choke. However, ddrescue can rip copy-protected DVDs to iso files like this:

| ``{{$}} sudo umount /dev/disk2``
| ``{{$}} ddrescue /dev/disk2 movie.iso``

(Substitute ``/dev/disk2`` for your DVD drive).

Once that's done, eject the DVD and run

| ``{{$}} open -a finder movie.iso``
| ``{{$}} vobcopy -l``

to decrypt the main feature movie.iso into a `VOB <VOB>`__ file. HandBrake can then be used to transcode the vob file if desired.
