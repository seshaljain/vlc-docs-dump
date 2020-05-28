{{howto|create a video file from a DVD using VLC}} \__TOC_\_ You can use
VLC to rip a "raw" video file from a DVD, or you can use VLC to create a
condensed "transcoded" video file from a DVD. This page mostly deals
with using it to rip a raw video file from the [[command line]]. ==
Instructions ==

Here is an example. You'll need to type this at the command prompt
(windows) or terminal (linux), all on one line.

This is how to rip the "raw" video from a DVD, assuming you want to rip
your DVD's title <code>1</code> to filename <code>dvdout.mpg</code>,
from drive <code>dvd:</code>

   {{promptwindows}} dvdsimple:///d:#1 --sout
   "#standard{access=file,mux=ts,dst=dvdout.mpg}" vlc://quit

the <code>vlc://quit</code> at the end just tells it to exit after
ripping. You can also add a <code>--qt-start-minimized</code>, if
desired.

Note that the above doesn't do any transcoding on the video stream, it
just basically dumps a verbatim copy to your hard drive. In comparison
with other ripping programs, this is sometimes lacking a few frames from
the original (up to 10), but is typically pretty accurate. If you want
one that is even more accurate, use MPlayer's dumpstream or makemkv.

You may have some luck ripping the DVD from
[https://www.howtogeek.com/howto/2696/how-to-rip-dvds-with-vlc the GUI],
as well, though this is a bit tricky [1]. See also note at bottom. Using
the GUI may help if you want to both rip and [[transcode]]
simultaneously, as the above commands only do a raw copy. Recommend
using [[HandBrake]] if you want to do transcoding too. {{Note-nb|If you
use the GUI you will need to name your output filename with the correct
extension for your mux type or VLC will silently ignore your request to
convert the stream on the DVD, and just display the video instead.
Silently, mind you. (If it is working right it won't show you a video by
default).}} You will also need to check the 'no DVD menus' option, which
instructs it to use <code>dvdsimple://</code> instead of
<code>dvd://</code> which
[https://forum.videolan.org/viewtopic.php?f=2&t=52748 loops back] to the
main menu after playing the title.

If it stops halfway through, cleaning your disc might help. If it still
fails half-way through, it may work better to use <code>dvd://</code>
(in the GUI, that's not check 'no DVD menus') instead of
<code>dvdsimple://</code> but this is probably not a good option as it
never stops but loops back to the main menu forever so you will have to
stop it manually by monitoring it. Recommend MPlayer's dumpstream in
this case.

   {{promptwindows}} dvd:///d:#1 --sout
   "#standard{access=file,mux=ts,dst=dvdout.mpg}" vlc://quit

It might also help to set the caching value either higher or to
<code>0</code> (in the GUI: under advanced options).

OS X example (you may be able to use
<code>dvdsimple:///Volumes/volumeName</code> as well).

   {{$}} {{Path to VLC|mac}} dvdsimple:///dev/disk1#1 --sout
   "#standard{access=file,mux=ts,dst=dvdout.dvdsimple.vlc.mpg}"

== Related ==

[[WindowsFAQ-1.1.x#Some DVD movies don't work at all or they
crash/freeze to menu or playback]]

[[HandBrake]] is a free user friendly open source tool for ripping DVD's
and simultaneously transcoding (condensing) the output file. It uses VLC
by default for ripping if installed on OS X. For windows users handbrake
can also use VLC's [[libdvdcss]] if you first
[https://forum.handbrake.fr/viewtopic.php?f=11&t=16670#p78021 install
it].

=== MPlayer === [[MPlayer]] is another excellent option for ripping a
raw mpeg stream from a DVD. See [[wikibooks:Mplayer#Rip DVD to raw
video|wikibook instructions]] for it.

=== makemkv ===

MakeMKV is also good for ripping DVD or blu-ray to a raw mpeg file. To
select specific titles, count down from the top of the checked title
options. The first one at the top is "title 1." After ripping, you could
then convert it (to condense/transcode it) by using handbrake or VLC.

If you want to convert makemkv's output to an mpeg file (mpeg-ts) then
you could use tsmuxer. OS X users will need a
[https://instantitunes.wordpress.com/2010/02/26/use-tsmuxer-on-snow-leopard/
special version] of tsmuxer, however.

=== ddrescue and vobcopy ===

Some DVDs have bad sectors as a [[copy protection]] mechanism, which
makes some tools choke. However, ddrescue can rip copy-protected DVDs to
iso files like this:

   {{$}} sudo umount /dev/disk2 {{$}} ddrescue /dev/disk2 movie.iso

(Substitute <code>/dev/disk2</code> for your DVD drive).

Once that's done, eject the DVD and run

   {{$}} open -a finder movie.iso {{$}} vobcopy -l

to decrypt the main feature movie.iso into a [[VOB]] file. HandBrake can
then be used to transcode the vob file if desired.
