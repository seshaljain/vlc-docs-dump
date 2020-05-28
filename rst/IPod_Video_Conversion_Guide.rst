{{lowercase}} {{howto|Make your Video Files playable on an iPod using
vlc 0.8.6}}

The following is a guide for converting (transcoding to file) any video
that VLC Media Player (VLC) can play into a format that the Apple iPod
can play. This should be "fool proof." This guide does not cover the
process of putting those files onto an iPod.

To play on this device, the file you copy to it needs to be of the
correct format. This format is summarized below:

{\| Video Codec \| '''mp4v''' ([[MPEG4]]) Audio Codec \| '''mp4a'''
([[MP4 audio]]), '''aac''' ([[AAC]]) [[Container]] \| '''mp4'''
([[MPEG-4-\| Size \| 320x240 or 640 x 480 for iPod Classic, iPhone, and
iPod Touch \| Widescreen iPod Classic, iPhone, and iPod Touch support
640 x 360 Other iPods support 320 x 180 \|}

== Why Use VLC to Convert Video for the iPod? ==

If you're looking for the absolute highest quality in video conversion,
then do NOT use VLC to convert Video for the iPod. There are many,
probably too many, programs already available.

I prefer to use VLC to convert to iPod video, because I know that if VLC
can play the file, then VLC can convert it for my iPod. I can also use
VLC in a script, which means I can tie it into my intranet, run
conversions automatically, and/or keep "profiles" (by using scripts) for
each video format that I'd like to convert. In addition, converting to
iPod video with VLC is very quick, because the encoder is only doing one
pass. This means that VLC is not just good for converting to iPod video,
but it is also good for converting to any type of video, where I need
versatility and speed.

If considering the disk space on an iPod and the battery life, I think
it is unnecessary to worry about file size/quality. Whereas a person can
store their entire music library on an iPod, a person will not be able
to store their entire video library on an iPod. At some point, that
person will need to come home, dock the iPod, and transfer files. It is
more likely that a movie, a music video, or at most a complete
television series will be stored on the iPod.

== Converting a Video with the Graphical User Interface ==

Open VLC. Please be sure you are using the default settings for VLC.
Please be especially sure that you do not have "repeat" set, as you will
infinitely overwrite your transcoded file.

http://www.kludgeroo.com/linked/videolan/vlc_ipod_converstion_8.6a.html_files/b8f63409-cb02-11db-8d2f-e8beb4eeadb9.png

Click "File" then "Open File", which will bring up the Open dialog.

<br>
http://www.kludgeroo.com/linked/videolan/vlc_ipod_converstion_8.6a.html_files/2afeac56-cb03-11db-8d30-e8beb4eeadb9.png"

<br> Be sure that you are on the File tab. Click Browse and select the
file that you would like to convert. Now check the Stream/Save box and
click the Settings ... button. This will open the Stream Output dialog.
This is where the magic happens.

<br>
http://www.kludgeroo.com/linked/videolan/vlc_ipod_converstion_8.6a.html_files/8f7744fe-cb03-11db-8d31-e8beb4eeadb9.png

*Notice that when you first open the dialog (if you haven't already
tried to stream/save a file in this session) the Stream output MRL box
at the top is empty. As you make your selections in the rest of this
window, that box will fill up with your options in a form that the VLC
executable understands.*\ First, check the File box, then click the
Browse... button to the right. Now choose the name of the file that will
be created during the conversion. Be sure to change the extension to
"mp4". \*Now choose the Encapsulation method. This is also known as the
"container". Select MP4.

*Go to Transcoding options next and check Video codec. Change the box to
its immediate right to mp4v or h264. The next box to the right changes
the bitrate of the video. I recommend 768 kb/s. Note - for higher
quality and only a slight increase in file size, use 1024. This will
make watching the video tolerable if you use the ipod AV cable and a
TV*\ Still in the Transcoding options area, check the Audio codec box,
and change the box to its immediate right to mp4a. The next box to the
right changes the audio bitrate. I recommend 64 kb/s or 96 kb/s. Note -
For higher quality (and not terrible file size) use 128. If you output
the file over decent speakers or if the movie has a complex soundtrack,
this will make a noticeable difference.

http://www.kludgeroo.com/linked/videolan/vlc_ipod_converstion_8.6a.html_files/cea16d6e-cb06-11db-8d4f-e8beb4eeadb9.png

So far, everything is fairly standard, but here comes the tricky part.
Go back up to the "Stream output MRL Target:" box. Notice that the box
is full of text. Look for the part that has #transcode{ }, and type
'''width=320,canvas-height=240''' somewhere inside the { }. Do not add
extra spaces. This setting changes the width to 320 pixels and adds
black bars above and below the movie, allowing all movies to maintain
the appearance of their original aspect ratio. '''Be careful''' here. If
you change any of the settings below this box, you will have to re-enter
the width and height settings.

Click OK to close the Stream ouput dialog, then click OK to close the
File open dialog. The movie should now start playing without showing the
picture on the screen. When it is complete you should have an iPod
compatible file.

== Converting a Video through the Command-line ==

Conversion via the command-line is a little beyond the scope of this
document, but using VLC in a script is my favorite way to convert
videos. This generally allows me the leisure of dragging the file onto
the script and magically getting my new iPod file in a certain
directory.

Generally speaking, the format of the command can be:

   vlc -vvv "my
   video.avi"&nbsp;:sout="#transcode{width=320,canvas-height=240,vcodec=mp4v,
   vb=768, acodec=mp4a, ab=96, channels=2}:std{access=file, mux=mp4,
   url=myvideo.mp4}" vlc:quit

On a Windows machine, I use the following batch script for drag and drop
functionality. Once a file is dropped onto it, vlc converts the video to
a folder that is set in the script.

The ipod video is saved in "<code>My Documents/ipod video</code>". You
must create this folder '''before''' using this script.

<code></code>

   @REM Remove the quotes from&nbsp;%1 variable for vlc paramters @SET
   infile=%1 @SET infile=%infile:"=% @REM Strip directory paths
   from&nbsp;%1 ... @FOR /F "delims="&nbsp;%%i in ("%infile%") do SET
   filename=%%~ni @SET outdir=%userprofile%My Documentsipod video@SET
   outfile=%outdir%%filename%.mp4 @REM The following command should be
   on ONE line only. @REM Be sure to remove the carriage returns in your
   batch file. "C:Program FilesVideoLANVLCvlc.exe" -vvv
   "%infile%"&nbsp;:sout="#transcode{width=320, canvas-height=240,
   vcodec=mp4v, vb=768, acodec=mp4a, ab=96,
   channels=2}:standard{access=file,mux=mp4,url=%outfile%}" vlc:quit

<br>

== Converting with Subtitles ==

The basic rule for subtitles is: if you can see them in VLC, then you
can put them in your converted video; however, getting this to work can
be tricky. Essentially, you use the '''soverlay''' option in the
#transcode{...} section to tell VLC that it needs to combine the video
and the subtitle streams into one video stream. Of course, that means
nothing if you don't know how to get subtitles to display in the first
place.

Subtitles for video can be stored in the orginal file as images or text.
Subtitles can also come from a separate text file. It all depends on the
original video file. Despite where the subtitles come from, you need to
first get the subtitles to appear in VLC during normal playback.

If the subtitles are a part of the original file (as with DVD, SVCD,
OGM, or MKV video), you will need to use the '''sub-track''' option to
select the desired subtitle track. You will specify this option
''after'' the #transcode {...} section.

http://www.kludgeroo.com/linked/videolan/vlc_ipod_converstion_8.6a.html_files/8965ad57a-cb06-11db-8d4f-e8beb4eeadb9.png"

To find the track numbers for the original file, play the file in VLC,
click on the Video menu, and view the available tracks under Subtitles
Track. The value that you will use for sub-track is the value in this
list minus 1. From the picture above, you would specify sub-track=2 to
get the second English track listed. (Use sub-track=5 for Deutsch.) To
tie it all together, your #transcode{...} section would look like this:

   #transcode{...,'''soverlay'''}:stuff{...options...}'''&nbsp;:sub-track=2'''

Depending on the original file, you may also be able to get away with
using the '''sub-language''' option instead of specifying the exact
subtitle track. Note that this would play the first English track if we
specified sub-language=English. Your #transcode{...} section would look
like this:

   #transcode{...,'''soverlay'''}:stuff{...options...}'''&nbsp;:sub-language=English'''

Now that you have the video playing with subtitles, you can create a
video with the subtitles overlayed on the video, using the same methods
at the top of the document.

For best results, first transcode to file ''without'' setting a new
width or height (the width=320,canvas-height=240 setting in the
#transcode{...} section). After you have made the larger file with the
subtitles overlayed, then convert to the smaller iPod width and height.
This will make it so that your subtitles appear in the correct
proportions on the smaller screen size.

== Testing Your New File ==

Now as I stated earlier, I've run many tests on different input file
formats and containers. Currently it is very rare for me to find a file
that I cannot convert. As far as testing the file goes, I strongly
recommend using Apple's Quicktime player. It is much faster than
repeatedly transferring the video to your iPod, disconnecting the iPod,
and playing the video. Unfortunately, Quicktime is only available on Mac
and Windows.

== Best video output for your ipod ==

Why would you want the best output? Because (many people don't know
that) you can play movie on TV from your ipod with a single (usually
cheap) cable. I have i Ipod video of the 5th generation and after
several hours of testing here are my conclusions:

H264 from vlc does not seem to be supported on this generation so the
choice is Mp4v all the way.(althoug h264 would be a better codec)

The maximum output resolution is 800 X 400. Any values below that is
supported. Your better off keeping the same aspect ratio as the source.
for example: most dvds are 720 x 480 so you should put 600 x 400 to keep
that same ratio.

If you dont keep the same ratio VLC will crop or add black canvas
depending on what you are doing that means your video will never be odd
looking.

The maximum Bitrate supported is 2400 kbps.

Adding <code>,deinterlace</code> to the #transcode{} section to
deinterlace the video is a good idea but not necessary as it will
correct the interlaced material and does not have an impact on
uninterlaced material.

== Solving Problems with Your New File ==

Here are some of my most notable problems and their solutions.

=== VLC closes without outputting anything or the file is 0kb. ===

*Make sure you are only converting the movie, not a playlist.*\ If
you're using a script, make sure your script is correct. (I admit, the
one I provided will probably have faults.)

=== My file is very small or only audio is recorded or only some of the
video is present. ===

*More than likely, the input file is slightly corrupted in a spot or you
are using the mp4v generic codec instead of the h264 codec. h264 really
does work more consistently.*\ Try adding '''fps=25,samplerate=44100'''
to the #transcode{...} section. \*Your CPU may be getting too hot.
Seriously. This was happening to me on one of my machines, and when I
tried it on another, conversion worked fine. Using a thermometer on the
original CPU/heatsink, I discovered that the CPU jumped to 70 degrees
during conversion! Solution: get another fan.

=== iTunes will not accept the new mp4 file ===

\*If converting WMV, ASF or DVR-MS, you can probably use the
'''vcodec=mp4v''' instead. There seems to be a problem with the output
container when using these as file inputs.

== Notes ==

\*The 5G and 5.5G of iPod video (with latest firmware) support video
resolutions up to 640x480; however, the screen resolution is still
320x240. This may only be useful with subtitled videos, as it removes
the second step of resizing the overlayed video.

== Older version of this howto ==

To make the video the correct size, you can edit the [[Preferences]], or
run vlc from a [[Command prompt]].

<code></code>

   vlc "input_filename"&nbsp;:sout="#transcode{vcodec=mp4v, vb=512,
   acodec=mp4a, ab=128, channels=2, audio-sync, width=320,
   height=240}:std{access=file, mux=mp4,url="output_filename"}"
   --aspect-ratio=width:height

<br>

This all goes on one line, and you'll need to fill in some of the
values: the input and output filenames, plus the aspect ratio of the
input file. By default vlc will stretch the video to the size specified
by sout-transcode-height and width, but if you tell vlc the file's
aspect ratio, it will scale and put a black border around it. The aspect
ratio can be written as a ratio of width and height, with a colon
between the two, or as a decimal.

Further I found that the iPod was particular about the parameter
"channels" being set to 2. I found that without this parameter iTunes
would import the file into the library but would not be able to upload
the same to the iPod.

Further during my experiments I figured out that it was better to stick
with MPEG4 encoding for the video stream. While H.264 codec is the
latest video compression standard I found the resultant file size
usually larger than when the MPEG4 compression mode was used, keeping
all the other parameters like the resolution and the bitrate same. This
definitely seems contradictory to what I would have expected but these
were the findings of my experiments while using videoLan VLC media
player.

(In fact, if the bit rates are chosen equally, the file sizes can be
expected to be roughly the same. The advantage of h.264 over mpeg4 is
its better video quality with the same bit rate or the allowance for
lower bit rates and thus smaller files with comparable video quality.)

If you would like to try using H.264 set the parameter vcodec to h264 in
the above command line as follows

<code></code>

   vlc "input_filename"&nbsp;:sout="#transcode{vcodec=h264, vb=512,
   acodec=mp4a, ab=128, channels=2, audio-sync, width=320,
   height=240}:std{access=file,
   mux=mp4,url="output_filename"}"--aspect-ratio=width:height

<br>

A useful tip - If you intend to create a batch file that would transcode
several titles in a DVD one after the other use the keyword vlc:quit as
follows

<code></code>

   vlc "input_filename"&nbsp;:sout="#transcode{vcodec=h264, vb=512,
   acodec=mp4a, ab=128, channels=2, audio-sync, width=320,
   height=240}:std{access=file, mux=mp4,url="output_filename"}" vlc:quit
   --aspect-ratio=width:height

<br>

== Converting Oddly Sized Input Videos to View on the iPod Video ==

The command-line examples above did not work for me when converting
video that did not already have a 4:3 aspect ratio. After converting the
video, iTunes would not load the video into my library, and I would get
"invalid data" errors when trying to view the file in the Quicktime
Player. It seams as of at least version 8.6a (not tested on previous
versions), vlc will use just the height value to determine the resultant
width, while maintaining the original aspect ratio, not the specified
ratio.

To remedy this, I used the '''sout-transcode-canvas-height''' option
with the '''sout-transcode-width''' and removed the specific aspect
ratio option and the specific height declaration. My example
command-line is below:

<code></code>

   vlc.exe -vvv "my video.avi"&nbsp;:sout="#transcode{vcodec=mp4v,
   vb=768, acodec=mp4a, ab=96, channels=2, samplerate=22050, width=320,
   canvas-height=240}:std{access=file, mux=mp4, url=myvideo.mp4}"
   vlc:quit

<br>

'''NOTE''' I've noticed that some files encoded with XVID come out
without video. If this happens, try using vcodec=h264.

This command will start vlc, transcode the video to file, and quit when
complete. The resultant video will be 320x240 with a black canvas
filling in the height to the video borders. If the input is already has
a 4:3 (320x240) aspect ratio, then no border will appear.

Here is an
[http://www.kludgeroo.com/linked/videolan/vlc_test_conversion_ipod.mp4
iPod format sample video] converted with vlc.

== Using Batch Files ==

Here is the info for a batch file to convert videos one after another,
although you have to enter your input and output values yourself (use
find and replace, or, if you are better than me, make an actual
script/program). Make sure the output names are different or else it
will get stuck and/or overwrite the old one

<code></code>

   vlc "'''input_filename'''"&nbsp;:sout="#transcode{vcodec=mp4v,
   vb=512, acodec=mp4a, ab=128, channels=2, audio-sync, width=320,
   height=240}:std{access=file, mux=mp4,url="'''output_filename'''"}"
   vlc:quit --aspect-ratio=width:height

<br>

<code></code>

   vlc "'''input_filename(1)'''"&nbsp;:sout="#transcode{vcodec=mp4v,
   vb=512, acodec=mp4a, ab=128, channels=2, audio-sync, width=320,
   height=240}:std{access=file, mux=mp4,url="'''output_filename(1)'''"}"
   vlc:quit --aspect-ratio=width:height

<br>

......etc for each video to convert (useful for converting short .flv or
.gvi, or pretty much any file) I relise this is inefficient,

but hopefully someone will make a script (vlc seems best for making ipod
videos from any source).

'''NOTE2:''' I find that if i have spaces in the output it doesn't work,
but this seems to be a problem with the .bat file. just don't use spaces
and use an autorenamer to rename
([http://batchrenamer.sourceforge.net/])

'''NOTE:''' If you can somehow to get 264 to work (megui makes it
work...) just change ''vcodec=mp4v'' to ''vcodec=h264''.

The script to drag and drop files (for Windows) is as follows:

<code></code>

   C:PROGRA~1VIDEOLANVLCVLC
   -vvv&nbsp;%1&nbsp;:sout=#transcode{vcodec=mp4v,vb=512,acodec=mp4a,ab=128,channels=2,width=320,height=240}:duplicate{dst=std{access=file,mux=mp4,dst=%1.m4p}}
   pause

There is no problem with spaces in filenames.

''This is also described (with snapshots) on
http://tom.zickel.org/vlcmp4/''

{{forum|15971}}

If the audio ends up being too quiet, the easiest way to make it louder
is in the "Get Info" box in iTunes.

[[File:Ipod.jpg]]

== Version 0.9.2 and later<br> ==

Some of these tips won't work with VLC 0.9.2, but the following command
line should work with 0.9.2

   vlc -vvv
   "my_video.avi"&nbsp;:sout=#transcode{width=320,canvas-height=240,vcodec=mp4v,vb=768,acodec=mp4a,ab=96,channels=2}:duplicate{dst=std{access=file,mux=mp4,dst=video.mp4}}
   vlc://quit

VLC&nbsp;1.0.2 uses the same command line parameters as VLC&nbsp;0.9.2.
However neither VLC 0.9.2 nor VLC 1.0.2 is able to create any video
files that Quicktime (and therefore iTunes) can play. Quicktime
complains about errors in files generated by transcode options (other
than the two below) that worked fine when using VLC 0.8.6a.

If you want to try for yourself, the changes to the command line
parameters from 0.8.6 to 0.9.2 and later are<br> <pre>url=video.mp4
</pre> changing to<br> <pre>dst=video.mp4 </pre> And<br> <pre>vlc:quit
</pre> changing to<br> <pre>vlc://quit </pre> to allow VLC&nbsp;to quit
and let Windows close the command prompt window.<br>

== Credits ==

Written by loqu (AKA Rob),
http://www.kludgeroo.com/linked/videolan/vlc_ipod_converstion_8.6a.html
(dead:
[https://web.archive.org/web/20100228144535/http://www.kludgeroo.com/linked/videolan/vlc_ipod_converstion_8.6a.html
archived version])

I've tested this guide on many containers, with and without subtitles.
This is an evolving guide, so please refer to
http://www.kludgeroo.com/linked/videolan/vlc_ipod_converstion_8.6a.html
for the original.

Before I begin I'd like to thank the good people over at
http://www.videolan.org for making a great multi-platform media program.
I decided to make this guide, because I had to invest much of my time to
get this to work. This is my way of giving back to the community.

{{Outdated}}

[[Category:iOS]]
