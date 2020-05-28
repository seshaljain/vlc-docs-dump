{{Howto|stream VLC to a website with .asf and Flash}}
   <!-- this is not needed, this is the title: '''Stream VLC to Website
   with .asf and Flash''' -->

This HowTo is intended to be a follow on from
[[Simple_Stream_VLC_to_Website]] wiki page.

== Introduction & Scope ==

The "Simple Stream VLC to Website" wiki employed an Out of the Box
solution with no modifications to the VLC command string. You may wish
to read through the previous Wiki first, as it covers fundamentals which
are assumed, if you have not done so already. This HowTo is aimed at VLC
users who are intending to “Live Stream” from a capture device, eg
Webcam, TV camera, live audio source etc and are looking to get a little
more out of the features available in VLC and wish to start to
understand the command line string and explore techniques to transcode,
compress and output a stream to a web site more efficiently and
effectively. The following examples are aimed at reducing bandwidth,
with a view to streaming on the internet with available upstream
bandwidth being the major consideration. The methods described below are
targeting a bandwidth of around 235k.

== Checks and prerequisites == To start with, Video transcoding,
compression and streaming is CPU intensive. So you are going to need
something like Intel P4 at 2.4Gb or equivalent as a minimum dedicated
box to use the example method 2 in this HowTo. Method 1 is achievable
with a pair of 1Gb cpu or more machines. You will have an appreciation
of the bandwidth requirements of what you are trying to achieve.

== Limitations == This HowTo was written and tested using VLC version
series 1.0.1 to 1.1.4 for Win XP.and VLC 0.9.9a to 1.0.6 for Ubuntu
Linux. (8.04 & 10.04) Earlier versions may work but have not been
tested. This HowTo, the methods and examples have been tested on
Operating Systems:

Method 1:-WinXP and Ubuntu Linux (8.04 & 10.04)

Method 2:-WinXP and Ubuntu Linux (8.04 & 10.04)

There are subtle and significant differences in capability and
performance of VLC versions and their respective OS platforms. See Notes
and Troubleshooting for more information. Hardware capability also plays
an important role in this respect.

Web server Apache 2.2 was used in all cases.

== Introduction to the VLC Command line == First a couple of reference
links for further reading

-  [[Documentation:Streaming_HowTo/Advanced_Streaming_Using_the_Command_Line#Structure_of_stream_output]]
-  [[Documentation:Streaming_HowTo/Command_Line_Examples]]
-  [[VLC_command-line_help]]

The above links will give an overview of the commands available to use
to manipulate and optimise the Command output string. The following
methods and examples modify the generated stream output string. I have
included an example of a complete true command line with the same
parameters as the Win XP example in Method 2. See Appendix. This should
help to give an insight into how to construct a complete command line
and enter the appropriate parameters. The following methods and examples
deal directly with the output string found in the GUI.

== Description of command parameters used in the methods following ==

vb=xx Video Bandwidth. This parameter in effect sets the target
bandwidth of the output video stream and hence the compression required.
The more compression the lower the video quality.

ab=xx Audio Bandwidth. As above, but relates to audio.

fps=xx Frames Per Second. The more fps, then the smoother the moving
image, however, this uses more bandwidth and compression. So lower fps
will give better quality for given bandwidth.

width=xx & height=xx Determines the aspect ratio and the size of the
image in pixels. The larger the image, the better the definition, but
will require more cpu power and bandwidth. The smaller the image the
less compression and bandwidth needed to stream.

deinterlace=<option or none=default> This command useful if you are
using an interlaced source. Eg. An NTSC or PAL source

scale=xx determines the output size relative to source size applied to
width/height ratio. So scale=0.5 will half original width/height in
pixels. Or in this case 25% of the original pixel area.

== Transcode Strategies ==

Single vs Two stage transcode? A single stage transcode may work well
for many situations. A two stage transcode may offer advantages in
quality at the cost of time and hardware to effect it. A two stage
transcode on two different boxes will be less susceptible to quality
problems related to mutual or random cpu activity spikes caused by other
applications. Method 1 works well with two stage giving an improved
picture quality with modest cpu usage given that the wmv codec is less
than best compared with what is available. Method 2 can work well in
single stage and usually better in two stage, but requires more cpu
power.I leave it to you, the user, to experiment with what works best
for you.

== Tweaking ==

There are any number of “tweaks” and “mods” that can be applied to the
output string or command line. I recommend that you try the example
methods as they are before changing everything to suit your anticipated
needs. Example tweaks. Look these up in the command line help link.

--sout-keep Keeps your stream open and listening.

--audio-desync=<integer> To preset and synchronise your audio to video,
you can +/- the integer.

audio-sync To maintain audio/video synchronisation on the fly. This
command will sit inside your sout=#transcode string, Eg after
samplerate=xxxxx.

The links referred to above should give a more expansive description of
what can be done. Again, do experiment when you have got a working
solution.

=== Method 1 wmv/div3 - asf ===

For this first method we will keep things very simple. The method is
similar to and follows on from “Simple Stream VLC to Website” .There
will be a couple of small changes and additions to the default command
strings. This method works well with a minimum of effort and hardware.
This method is described using wmv and will also work with div3. This
method will employ a two stage transcode using two computers. A common
configuration. The first stage will be the Primary
source/capture/compression (Box1) . The secondary output from (Box2) for
final compression and will be your web server.

Box 1 Set up: Select “Streaming” set up your capture devices and set the
video size to 256x192 Simply using the default values in the GUI, select
“Stream”, then “Next” at source, at “Destinations” check the box
“display locally” <optional> , select HTTP from the dropdown box, and
click the “Add” button, leave the address field as 0.0.0.0 and change
the port number to 8080. Activate transcoding box is checked, select the
Windows WMV/asf Transcoding profile and click “next” again. You should
now see the “Generated stream output string”. This is where we will make
the changes and additions. So. Look at what is in this field and compare
with the example below. Then modify the output string with the changes
listed below. Or clear the output field and copy and paste.

First output string (box 1)

   :sout=#transcode{vcodec=WMV2,vb=400,fps=15,width=256,height=192,deinterlace,acodec=wma2,ab=64,channels=2,samplerate=44100}:duplicate{dst=std{access=http,mux=asf,dst=/},dst=display}

The changes/additions we have made here: # vb changed to vb=400 # Added
fps=15 # Removed scale=1 # Added width=256 # Added height=192 # I have
added “deinterlace” Optional if using an analogue interlaced TV camera #
ab changed to ab=64

Box 2 Set up: Pickup the stream from Box 1 with “Open Network Stream”
and check that it is streaming OK. Repeat the setup procedure as for Box
1, but use the following output string. Second output string (box 2)

   :sout=#transcode{vcodec=WMV2,vb=200,fps=15,scale=1,acodec=wma2,ab=32,channels=2}:duplicate{dst=display,dst=std{access=http,mux=asf,dst=/}}

The changes/additions we have made to second output string

1. vb reduced again to 200
2. Added fps=15
3. ab reduced again to 32

Sample metafile for HTML below

   <ASX version ="3.0">
      <TITLE>extstream8080</TITLE>
         <ENTRY>
            <REF HREF="http://youripaddress:8080" />

         </ENTRY>

   </ASX>

(saved as <extstream8080.asx>)

Sample HTML for embedded web page

   <nowiki><!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">

<html><head> <meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type"><title>External Stream 8082 embedded</title>

</head> <body> <big style="font-weight: bold;"><big>Box 2 streaming on
port 8082<br> <br> <br> </big></big> <embed src="extstream8080.asx"
height="450" width="512"> </body></html></nowiki>

Alternatively, you could embed with MS MP.

=== Method 2 H264 and Flash .flv ===

Method 2 is somewhat more sophisticated, but should give a good result
with minimal bandwidth. It can be successfully effected in a single
stage transcode, but a two stage transcode may improve the quality
depending on the quality of the hardware available. This method employs
an optional first stage pre compression in asf followed by an H264 and a
final output in .flv (Flash) and includes a subsection on Flash players
“JWPlayer” and “Flowplayer” There is some additional information in
Notes further down this HowTo.

Box 1 Set up: (optional) Primary source/capture/compression in asf
Select the dropdown box output stream to DIV3/mp3 asf. Follow the
similar modifications to the output string as per Method 1, Box 1

The changes/additions we will make here: # vb=600 # fps=25 # Remove
scale=1 # Added width=256 # Added height=192 # I have added
“deinterlace” Optional, if using analogue interlaced TV camera # ab
changed to ab=64

Box 2 Set up: Secondary output in .flv Select your input, Eg the network
stream from Box 1, or your source/capture device. Select Streaming and
tab <next> through to the “Options” screen without choosing anything in
the previous “Destinations” tab. The “Generated stream output string”
field should be blank. The following output strings can be copied and
pasted into the empty field. Do make sure that there are no spaces in
the string when you copy/paste.

First example string for Win XP (and ffmpeg-x264 enabled Linux) users

   :sout=#transcode{vcodec=h264,vb=200,deinterlace,ab=32,fps=25,width=256,height=192,acodec=mp3,samplerate=44100}:duplicate{dst=std{access=http{mime=video/x-flv},mux=ffmpeg{mux=flv},dst=/mediaplayer/stream.flv},dst=display}

Second example string for (stripped ffmpeg) Linux users

   :sout=#transcode{vcodec=FLV1,acodec=mp3,vb=200,deinterlace,fps=25,samplerate=44100,ab=32}:duplicate{dst=std{access=http,mux=ffmpeg{mux=flv},dst=/stream.flv},dst=display}

The above examples should work OK when adapted to your destination IP
and port. That said, they are examples of two different approaches. The
Windows approach utilises the H264 codec. The Ubuntu Linux approach
example provides for a working solution in FLV1 which should work OK
with the “Stripped” standard version of ffmpeg in a standard
installation. This method would benefit from a two stage transcode to
improve quality.

As of Ubuntu 10.04 – VLC 1.0.6 there is a more complete and up to date
version of ffmpeg and x264 support in the standard repos'. Eg
libavdevice-extra52 & x264. Note VideoLan currently recommends VLC
versions 1.1.x . See VideoLan Ubuntu Downloads page for further
information

You will probably want to check that everything is working at this
stage. So point a VLC client at the stream to check it out. Check out
the “Troubleshooting” section.

Next we will need a player to embed the stream into a web page. JWPlayer
and Flowplayer are suitable for this purpose. Both of these players need
a path to their java files.Eg. The Win XP example had /mediaplayer/ in
the path This was the default folder for JWPlayer in that example. The
Linux example assumed that the necessary java files placed in the root
dir of the webserver and needed no path. These players are described in
detail in the documentation on their websites. If you have not used
these players before, take time to become familiar with them before
using them in this context.

http://flowplayer.org/

http://www.longtailvideo.com/support/tutorials/Embedding-Flash

Example html for a “Flowplayer” embedded page relating to the example
VLC Linux output string above. Do note that the Windows example had
/mediaplayer/ in the path! This example does not.

   <nowiki><!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
   "http://www.w3.org/TR/html4/strict.dtd">

<html><head><title></title> <title>This Flash Streaming from VLC
video</title> <script src="flowplayer-3.1.4.min.js"></script><meta
content="text/html; charset=ISO-8859-1" http-equiv="content-type">
</head> <body> <big style="font-weight: bold;">Flowplayer test file
local</big><br> <br> <br> <br> < See Flowplayer documentation and note
below for this line> </a> <script language="JavaScript">
flowplayer("player", "flowplayer-3.1.4.swf"); </script> <p><br>
</body></html></nowiki>

Note The href= value in this line would contain
"http://yourIP:8080/stream.flv"

== Troubleshooting ==

OK so it all went wrong? And did not work. At the risk of stating the
obvious? Backtrack. Check each stage step by step and prove that each
bit is working before moving to the next. Common faults and checks are
listed as follows: #1. Many Linux distros may not include by default the
full version of ffmpeg and h/x264 and associated libs for encoding. You
may need to go research and install all necessary components to get it
all working.

#2. The quality of both video and sound can vary due to many factors,
which may include the version of VLC, the OS platform, the version of
players, plugins Etc. Problems such as stuttering, pixelation, excessive
buffering delays are not uncommon. In general terms, keeping up to date
with the latest versions of everything is good practice, however in some
cases, a newer version may not work as well (if at all) as it’s
predecessor.

#3. Realtime streaming is cpu intensive and also sensitive to being
interrupted in realtime. Other applications can and will interrupt. Shut
down all unnecessary applications ( and the ones in background) Spikes
of intensive cpu activity which will not always show up in Task
Manager/System Monitor can and will cause problems with the quality of
your stream output. You may wish to raise the priority of VLC to reduce
the effect of interrupts.

#4. Clients need to be equipped with the necessary means to display your
stream! Sounds an obvious statement? Probably not a problem if you have
an up to date box, with MS Windows and a recent Flash plugin. I have
encountered any number of problems with old hardware, other Operating
Systems, browsers and Flash plugins. Don’t be surprised or disappointed
at the apparent failure or erratic performance of your stream if you are
testing it with a client that is not suitably equipped and able. Using
Localhost to check out your stream may also give unexpected and
misleading results.

#5. The quality of the video input is also very important. Low quality
webcams, camera and capture devices, noisy TV input devices will give
even more disappointing results when transcoded.

== Notes ==

There are many ways to compress/transcode your stream. The example
methods were intended to be a fairly universal and tested starting
point. Some combinations work some don’t. Some combinations work in one
scenario but will not work in another. If the example methods do not
work for you, the Videolan forums are the best place to start looking
for a solution.

== Appendix ==

The following is an example of a full command line with the same
settings as Method 2 Win XP. The first part, up to ”sout” is the input
string. The vdev= and adev= are the (your) input devices and can be
viewed and extracted from the first “streaming” window or tab in the
GUI, with the “show more options” box checked. You will need to apply
the correct syntax for your OS. In Windows ( note the double quotation
marks,Eg ”<xxx>” syntax in Windows , for Linux use the single quotation
marks '<xxx>') you would enter this at the command prompt path at
C:/program files/videolan/vlc . You will also have to add quotation
marks around any devices in MS Windows (see example below). Also note,
in this example, video size has been defined twice, both in the input
and output sections. If you did not include a setting for Video Size in
the GUI screen it would not be present in the (generated) input string.
Try adding and changing options to see how the VLC GUI builds the input
string for you. It is not necessary for video size to be defined here,
but should work OK with or without this parameter in the input section.
I have included it to show how the string is generated in the GUI. The
complete input and output sections can be simply copied and pasted from
the GUI into a text editor and built into a complete string to create
full working command line. Note, avoid using "word wrap" in the text
editor, it can sometimes introduce unwanted characters in the string.

   vlc dshow:// :dshow-vdev="Conexant's BtPCI Capture"
   :dshow-adev="Aureon 5.1 Fun Wave" :dshow-size="256x192"
   --sout="#transcode{vcodec=h264,vb=200,deinterlace,fps=25,width=256,height=192,ab=32,acodec=mp3,samplerate=44100}:duplicate{dst=std{access=http{mime=video/x-flv},mux=ffmpeg{mux=flv},dst=/mediaplayer/stream.flv},dst=display}"
