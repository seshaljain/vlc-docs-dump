{{Howto|extract audio}} VLC can '''extract audio''' from any of the many
input sources it supports, and write this audio to an audio-file in a
variety of formats. In other words, it discards any video content from
the input source, and it converts the audio content to the desired
format.

You can invoke audio extraction from the VLC graphical user interface,
or from the VLC command line. When using the VLC command line, you can
select options that let you monitor the audio (and/or video, actually)
as the extraction happens. Or, you can select options to hide VLC's
visual interfaces, leaving it to extract and convert the audio data as
fast as the computer allows -- which might take a fraction of the time.
You can also script the VLC command line invocations, letting you do
many extraction tasks without manual effort.

==Planning==

Identify the source from which you want to extract the audio signal. You
will open this source from VLC using the same GUI operations or
command-line options as you would for any other VLC usage.

Is the source an audio-only file? If so, then this operation is a simple
[[transcode|transcoding]] of audio content from one format to another.
Be aware that, while VLC has certain facility for this task, other tools
may be even more powerful, faster, or more reliable for the task. For
instance, the [http://flac.sourceforge.net/documentation_tools_flac.html
FLAC tools] include a command-line utility which can convert [[WAV]]
files into [[FLAC]] files with excellent speed and reliability. Where
VLC really shines is for sources which combine video and audio content.

Is the source a [[DVD]], or other container with internal structure,
such as multiple "Titles", and multiple "Chapters" in each Title? If so,
then you need to identify which Title and Chapters include the audio
content you want, and which are irrelevant. For instance, a DVD may have
a menu in Title 1, an advertisement in Title 2, the main content in
Title 3, and a trailer in Title 3. The main content in Title 3 may be
divided into dozens of chapters, like the tracks in a CD. In a case like
this, you probably want only the audio content from Title 3, not from
the other Titles. You may want to extract a single audio file with the
content of all of Title 3, or you may want a separate audio output file
for each Chapter.

The VLC GUI provides a somewhat clumsy but workable way to explore the
structure of a DVD or corresponding video file. Here is how (as of
Windows version 1.1.11): # Run the VLC app. # Put the DVD into the
computer's DVD reader. # From '''Media''' menu, select '''Open
Disc...''' (Ctl-D). The '''Open Media''' dialog appears. # Select the
'''Disc''' tab. In the '''Disc''' tab's "Disk Selection" section, select
the "DVD" radio button . From the "Disc device" menu, select the menu
entry corresponding to the computer's DVD reader. For example, it might
be "F:- Wedding Movie". Click the '''Play''' button at the bottom of the
dialog. The '''Open Media''' dialog disappears. The DVD now appears as
an entry in the playlist, e.g. "DVD://F". # Double-click on the DVD
entry in the playlist. The DVD starts playing. If necessary, select
entries in the DVD's menu to start the DVD playing the content from
which you want to extract audio. # From the '''Playback''' menu, hover
over '''Title >'''. A second menu appears, with entries like "DVD Menu",
"Title 1", "Title 2", "Title 3". These are the Title choices you have to
pull from. A check mark will be next to one of the entries. This is the
Title with your content. # On the '''Playback''' menu, move down to
hover over '''Chapter >'''. A second menu appears, with entries like
"Chapter 1", "Chapter 2", etc. A check mark will be next to one of the
entries. This is the Chapter with your content. # Note the last entry in
the '''Chapter >''' submenu. This tells how many chapters there are in
total in that title. # Note the Title and Chapter number of the start of
the content from which you want to extract audio. Also note the final
Title and Chapter number of the content.

==Using the VLC graphical user interface (GUI)==

See [http://www.wikihow.com/Rip-DVD-Audio-to-MP3-Using-VLC-Media-Player
How to Rip DVD Audio to MP3 Using VLC Media Player], Edited by AudioDude
and 2 others, WikiHow.com

Note that VLC's GUI lets you specify the Title and Chapter from which it
will start, but VLC will continue extracting until the end of the Title.
It doesn't let you extract a single Chapter at a time. To do that, you
will need to use the VLC command line.

==Using the VLC command line==

This section gives examples of how to extract audio using VLC's command
line invocation.

===The VLC command invocation=== The start of the command line is the
VLC invocation. On Windows this looks like: "c:Program
FilesVideoLANVLCvlc.exe"

On macOS it looks like:
   /Applications/VLC.app/Contents/MacOS/VLC

On Linux, if the vlc executable is on your path, it looks like:
   vlc

===General options=== The command line will have a sequence of general
options. These are the same for all platforms. -I dummy --no-sout-video
--sout-audio --no-sout-rtp-sap --no-sout-standard-sap --ttl=1
--sout-keep

Here's what those options mean: ;-I dummy:VLC should run with no GUI,
typing error messages and asking for input in the command line window.
This is better for scripting and for faster completion. Leave this
option off if you want the GUI to appear. ;--no-sout-video:VLC will not
pass on a video component to the streaming output ;--sout-audio:VLC
will, however, pass on an audio component to the streaming output
;--no-sout-rtp-sap --no-sout-standard-sap:VLC will not deliver streaming
output in [[RTP]]-[[SAP]] or [[SAP|Standard SAP]] forms. ;--ttl=1:A
parameter for RTP and SAP; innocuous here. ;--sout-keep:Keep a copy of
the streaming output; innocuous here.

===The sout string=== An option string, marked by '''--sout''', tells
VLC how to transcode the content and in what format to write it. See
below for fully detailed examples. However, here is one sout string,
specifying to transcode to a WAV audio format. --sout
"#transcode{acodec=s16l,channels=2}:std{access=file,mux=wav,dst=C:UserAdminDesktopyourAudio.wav}"

===The source MRL=== The '''[[Media Resource Locator]]''' ([[MRL]]) is a
string which tells VLC where to find the source content, e.g. the DVD or
source file. For more on the MRL syntax, see [[VLC command-line help]].

The MRL for a DVD, selecting only Title 3, Chapter 38, in Windows looks like:
   dvdsimple:///F:#3:38-3:38

A similar MRL for macOS looks like:
   dvdsimple:///\ dev/rdisk2/@3:38-3:38

An MRL could also be a filename, directory name, or a path to a file or directory name.
   Video.TS///C:UsersAdminDesktopyourVideo.mp4#1:33-16:38

At the every end of the command line, put this special second MRL. It tells VLC to end its run without looking for another MRL to transcode.
   vlc://quit

===Specifying output format===

====Extracting audio in original format====

If you want the extracted audio in the same format as it is stored in
the input, then VLC can provide it to you with no loss of quality,
because there is no re-encoding of the content.

The way to do this for AC3 format audio from a DVD video is (on Linux):

   vlc --no-sout-video dvdsimple:///\ dev/scd0@1:1
   :sout='#std{access=file,mux=raw,dst=./file.ac3}'

Note: <tt>:sout</tt> means that the option ''sout'' applies only to the
preceding stream, not to the whole command line. See ''[[VLC
command-line help]]''.

====Extracting audio in FLAC format====

This is an example of a Windows command line which extracts the audio
content of an arbitrary file, to a FLAC audio file.
"C:UserAdminDesktopyourAudio.wav" is the destination of your file, and
"C:UserAdminDesktopyourVideo.mp4#0:01-3:38" is the location of your
original video, followed by arbitrary starting and ending times.

The example has line breaks for clarity, but your command should all be
on one line:

   "c:Program FilesVideoLANVLCvlc.exe" -I dummy --no-sout-video
   --sout-audio --no-sout-rtp-sap --no-sout-standard-sap --ttl=1
   --sout-keep --sout
   "#transcode{acodec=flac}:std{mux=raw,dst=C:UserAdminDesktopyourAudio.flac}"
   Video.TS:///C:UserAdminDesktopyourVideo.mp4#0:01-3:38 vlc://quit

Notice the changes: ;acodec=flac:tells VLC to convert audio content
using the [[FLAC]] [[codec]] ;mux=raw:uses a raw file structure instead
of the WAV file structure ;File extension .flac:The file extension is
FLAC for FLAC-format content.

====Extracting audio in MP3 format====

'''TODO!'''

====Extracting audio in WAV format====

This is an example of a Windows command line which extracts the audio
content of an arbitrary file, to a WAV audio file.
"C:UserAdminDesktopyourAudio.wav" is the destination of your file, and
"C:UserAdminDesktopyourVideo.mp4#0:01-3:38" is the location of your
original video, followed by arbitrary starting and ending times.

The example has line breaks for clarity, but your command should all be
on one line:

   "c:Program FilesVideoLANVLCvlc.exe" -I dummy --no-sout-video
   --sout-audio --no-sout-rtp-sap --no-sout-standard-sap --ttl=1
   --sout-keep --sout
   "#transcode{acodec=s16l,channels=2}:std{access=file,mux=wav,dst=C:UserAdminDesktopyourAudio.wav}"
   Video.TS:///C:UserAdminDesktopyourVideo.mp4#0:01-3:38 vlc://quit

The parameter '''acodec=s16l''' tells VLC to use convert the audio
content using the [[s16l]] [[codec]], which is the codec for [[WAV]]
format audio. Parameter '''mux=wav''' tells VLC to write the s16l audio
data into a file with the WAV structure. The file path starts with "\\",
because each pair "\" is converted to a single "" by the command line
environment, giving a server path of <tt>\ServerQmultimedia</tt>. The
file extension is ".wav" for WAV format files.

===Scripting extraction of multiple chapters using a batch file=== The
above example command lines caused VLC to extract audio for a single
Chapter of a single Title into a single audio file. It is possible on
Windows, macOS, and Linux command lines to write a script that loops
through the Chapters of a Title and calls VLC for each one. Such a
script can run unnattended for the tens of minutes it might take to
extract a couple of hours of audio content, in dozens of tracks.

Here is a windows batch file which scripts VLC to extract all Chapters
from a Title to a set of files in a directory on a Windows server. The
first five lines, each beginning '''set''', define parameters. The final
line, beginning '''for /L''', performs the loop and invokes VLC. The
Windows batch file processor replaces parameter names surrounded by
percent characters, e.g. %DestPrefix%, by their values. <pre> set
DVDDrive=F: set DestPrefix=\\ServerQmultimediaMusicwav_filesaudio set
Title=3 set FirstChapter=1 set LastChapter=38

rem the following has line breaks for legibility. Remove them so it's
all on one line. for /L %%i in (%FirstChapter%,1,%LastChapter%) do
"c:Program FilesVideoLANVLCvlc.exe" -I dummy --no-sout-video
--sout-audio --no-sout-rtp-sap --no-sout-standard-sap --ttl=1
--sout-keep --sout
"#transcode{acodec=s16l,channels=2}:std{access=file,mux=wav,dst=%DestPrefix%_c%%i.wav}"
dvdsimple:///%DVDDrive%#%Title%:%%i-%Title%:%%i vlc://quit </pre>

To use this script, copy its contents into a file, say with a name
'''riploop.bat'''. Be sure the final line, beginning with '''for /L''
and ending with '''vlc://quit''', is all on a single line; remove the
line breaks which were inserted for legibility on this page. Then type
in a Windows command line window, connect to the directory with the
script file, and type '''riploop.bat''' to run it. VLC will pop up a new
command line window for each invocation of VLC.

== See Also == \*
[http://www.wikihow.com/Rip-DVD-Audio-to-MP3-Using-VLC-Media-Player How
to Rip DVD Audio to MP3 Using VLC Media Player], Edited by AudioDude and
2 others, WikiHow.com \* article ''[[Extract audio from a file]]''
