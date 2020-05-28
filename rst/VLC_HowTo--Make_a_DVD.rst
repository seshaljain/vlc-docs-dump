{{howto|create a DVD to play in your DVD player from video files stored
on your computer}} {{Example code}}

== DVD Formats == To make a DVD, you first have to change your movie
file into the DVD format, which is MPEG 2. This format is:

=== PAL Format === Europe and elsewhere \* Encapsulation (mux): '''mpeg
ps''' up to 10.08 Mbps total for everything. \* Video: \*\* Format
'''mp2v''' (MPEG-2 Video), up to 9.8 Mbps \*\* Resolution of
'''720x576''' (Full D1), '''704x576''', '''352x576''' (Half D1),
'''352x288''' (same as VCD) \*\* '''25''' frames/sec \* Audio: \*\* Up
to 8 audio tracks in the following formats. At least one track must be
in a52, mp2a or raw. **\* '''mp2a''' Standard MPEG Audio.**\ \*
'''a52''' AC3 Dolby Digital **\* DTS Audio**\ \* PCM Uncompressed
('''raw''') \*\* Format: '''48000 Hz''', 32 - 1536 kbps

=== NTSC Format === Used mainly in USA \* Encapsulation (mux): '''mpeg
ps''' up to 10.08 Mbps total for everything. \* Video: \*\* Format
'''mp2v''' (MPEG-2 Video), up to 9.8 Mbps \*\* Resolution of
'''720x480''' (Full D1), '''704x480''', '''352x480''' (Half D1),
'''352x240''' (same as VCD) \*\* '''29.97''' frames/sec \* Audio: \*\*
Up to 8 audio tracks in the following formats. At least one track must
be in a52 or raw. **\* '''mp2a''' Standard MPEG Audio.**\ \* '''a52'''
AC3 Dolby Digital **\* DTS Audio**\ \* PCM Uncompressed ('''raw''') \*\*
Format: '''48000 Hz''', 32 - 1536 kbps

== Encoding the Video with VLC ==

-  Format a file into a .mpg, mpeg ps encapsulation, mp2v video (a good
   bitrate is 4 Mbps).
-  For audio, mp2a 2-channel 192K works well. If you need more channels,
   use a52 and increase the bitrate; budget 64 or 96K/channel (2
   channels 192K, 6 channel 384K,...
-  A DVD format file should be 720x480 resolution for NTSC, or 720x576
   resolution for PAL.
-  Set the --sout-transcode-fps to match your target, using 29.97 for
   NTSC, 25 for PAL.
-  Set the --sout-ffmpeg-keyint to 16 (possibly not needed, but I use
   this and it works)
-  Set the --sout-ffmpeg-strict-rc (see notes below)
-  Use the --aspect-ratio switch to control things. For instance, a
   Webcam or framegrabber with 640x480 or 320x240 resolution has an
   --aspect-ratio of 4:3. You need to specify this so that the
   transcoding doesn't make the output video "fat", stretch things to
   fit the wider DVD width. Standard DVD "letterbox" has an aspect ratio
   of 16:9.

Here is an example. The .asf source movie is a 640x480 frame grabber.
You'll need to type this at the command prompt (windows) or terminal
(linux), all on one line. You may also need to give the full path to vlc
(ie, replace ''vlc'' with ''"C:Program FilesVideoLANvlcvlc"'', or
wherever you installed vlc)

-  In the command I included '''--stop-time=20''', which tells VLC to
   only encode the first 20 seconds. This is so you can then view the
   output and make sure it looks OK. To encode the full thing, just use
   the same command without the --stop-time=20.

\* This command goes all on one line. Important bits (which you should edit) are shown in bold.
   vlc "C:MoviesYour File.asf"
   :sout=#transcode{vcodec=mp2v,vb='''4096''',acodec=mp2a,ab='''192''',scale=1,'''channels=2'''}:std{access=file,mux=ps,dst="C:MoviesYour
   File Output.ps.mpg"} '''--aspect-ratio="4:3"'''
   --sout-transcode-width='''720''' --sout-transcode-height='''480'''
   --sout-transcode-fps='''29.97''' --sout-ffmpeg-keyint=16
   --sout-ffmpeg-strict-rc '''--stop-time=20'''

Explained: *'''channels=2''' - needed because mp2a can only cope with 2
channels, it's not needed (or wanted) if you used a52*
'''aspect-rato="..."''' - to avoid stretching to image, set this to the
ratio of your source file. \* If you use PAL, don't forget to change
720, 480 and 29.97! \* '''sout-ffmpeg-keyint''' - number of keyframes
(this is to do with the encoding. Inclusion will help the quality of the
output file) \* '''sout-ffmpeg-strict-rc''' ffmpeg by default uses a
variable bit rate. This flag keeps the max rate of the VBR closer to the
average rate. Without this flag, ffmpeg may produce a file with a max
rate that will be incompatible for DVD. \* '''stop-time''' delete this
to encode the whole thing

'''Alternative''' - This is a slightly different way to do the encoding:

   vlc C:MoviesDiveModules1to3_2Mbps.asf
   :sout=#transcode{vcodec=mp2v,vb=4096,scale=1,acodec=mp2a,ab=192,channels=2}:std{access=file,mux=ps,dst="C:TEMPDive1_3_out.mpg"}
   --aspect-ratio "4:3" --sout-transcode-width 720
   --sout-transcode-height 480 --sout-transcode-fps 29.97
   --sout-ffmpeg-keyint 16 --sout-ffmpeg-strict-rc

Note that the ''sout-ffmpeg-strict-rc'', or ''strict rate control'',
flag can be permanently set in the Preferences as an Advanced Option
under Input/Codecs->Other Codecs->FFmpeg. Note that this may be
necessary to create a mpeg2 file that is DVD compatible

== DVD ISO Creation and Burning ==

=== Windows ===

This example shows how to create a DVD using
[http://sourceforge.net/projects/dvd-hive/ DVDHive] and
[http://www.cdburnerxp.se/ CDBurnerXP]. These are good, ''free'' tools,
and you will need to install both of these.

-  DVD Hive SourceForge.net project is inactive.
-  Launch DVD Hive
-  Select Options, type in a name you want for the video
-  Select Add, then browse to the .mpg file and select it.
-  Select Hive -- it will create a .iso image.
-  If the resulting ISO is < 4.4GB you should be OK. Otherwise reencode
   with VLC, knocking the bitrate down a bit (the 4 mbps mp2v/192k mp2a
   works fine, with a full-length video). Also note that some versions
   of windows (mainly 98) and filesystems (FAT16, FAT32) can't cope with
   files over 4GB (XP on NTFS is fine).
-  Launch CDBurnerXP
-  A "New Compilation" window opens -- pick the first choice, which says
   "...and/or burn an ISO image..."
-  In the upper left corner of the main window, select File -- Write
   Disc From ISO File
-  "Write ISO Image" screen opens.
-  "No ISO Image" -- click the "..." button next to it, and browse to
   where you put the .ISO (DVD-Hive defaults to putting it in c:program
   filesDVD HiveISO).
-  "Writing Speed" -- select the minimum value specified for your media
   and DVD drive. For example, my DVD supports 8X write, but I often use
   4X write media, so I change it to say 4X.
-  "Write Disc" -- click it, and the image will be burned.

=== Linux ===

You can burn DVDs in linux using [http://dvdauthor.sourceforge.net
dvdauthor]. It's quite tricky to use that on its own, so you should
download a front-end - try [http://qdvdauthor.sourceforge.net/ Q DVD
Author] or [http://dvdstyler.sourceforge.net/ DVD Styler].
