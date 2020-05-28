= Google Code In =

This page is about gathering '''ideas''' for the VideoLAN project for
acceptance in the
[http://code.google.com/opensource/gci/2011-12/index.html Google Code In
2011-2012] program.

VideoLAN has been part of [http://code.google.com/soc/ Google Summer of
Code] in [[SoC_20072008]], [[SoC_20092010]].

[[x264 GCodeIn Ideas|x264]] is also participating in Videolan's Code-In.

= Ideas for VideoLAN =

== Warning == This is a temporary page for listing ideas for Google
Code-in tasks.

The final tasks will be moved to melange, when needed.

The list is being migrated to a google doc for ease of
importing/processing.

[https://docs.google.com/spreadsheet/viewform?hl=en_GB&formkey=dHZHenE4WFhXZlBrck5GZmtrQ0wyR2c6MQ#gid=0
Simplified
Form]|[\ https://docs.google.com/spreadsheet/ccc?key=0ArFsnoouksujdHZHenE4WFhXZlBrck5GZmtrQ0wyR2c&hl=en_GB#gid=0
List so far]

Please help filling it the data using the form.

== libav ==

=== Code Cleanup === '''Category''': Code <br> '''Description''': libav
has a coding style and all the new contributions must abide to it, sadly
ancient files do not abide to it<br> '''Outcome''': provide a patchset
with properly formatted code, points will be awarded per file.
Additional points if a larger file is split in the process.
'''Difficulty''': <br> '''Tools''': <br> '''Time''': <br> '''Mentor''':
<br>

=== Video Tutorial: avconv === '''Category''': Documentation <br>
'''Description''': avconv had been recently introduced and new and old
users of ffmpeg might enjoy having some walkthrough to a number of
common tasks. <br> '''Outcome''': Prepare a video with a short tutorial
for one of the following tasks: <br> *Transcode to h264/aac/mov
<br>*\ Transcode to vp8/vorbis/webm <br> *Transcode to h264/speex/flv
<br>*\ Live streaming from a video source (webcam/screen capture) to a
remote server (rtmp, rtsp) <br> '''Difficulty''': <br> '''Tools''': <br>
'''Time''': <br> '''Mentor''': <br>

=== Help document filter usage === '''Category''': Documentation <br>
'''Description''': A list of filters is nice, but actual examples would
help a lot <br> '''Outcome''': You'll provide 5 different examples
involving filters <br> '''Difficulty''': <br> '''Tools''': <br>
'''Time''': <br> '''Mentor''': <br>

=== Live-streaming from libav === '''Category''': Documentation <br>
'''Description''': Lots of sites let you broadcast yourself, but
sometimes getting there can be a challenge- help improve this <br>
'''Outcome''': Produce a guide showing how to do live-streaming to a
video site of your choice <br> '''Difficulty''': <br> '''Tools''': <br>
'''Time''': <br> '''Mentor''': <br>

=== Create a new preset === '''Category''': Documentation <br>
'''Description''': libav has a fine set of presets, but they're limited
in scope- other codecs could certainly benefit from some nice presets
<br> '''Outcome''': Create a new preset that gets accepted into libav
<br> '''Difficulty''': <br> '''Tools''': <br> '''Time''': <br>
'''Mentor''': <br>

=== Practical examples on capturing from devices === '''Category''':
Documentation <br> '''Description''': There's many devices that avconv
can capture from, but not all are well documented- some only have a
mention or two and no examples <br> '''Outcome''': At least five new
examples on capturing from devices will be created <br>
'''Difficulty''': <br> '''Tools''': <br> '''Time''': <br> '''Mentor''':
<br>

=== Document metadata tags and their usage === '''Category''':
Documentation <br> '''Description''': There are huge number of metadata
tags spread across many standards, and libav supports many of them.
Documentation on them is sparse, and is mostly contained in the source
code <br> '''Outcome''': At least one metadata format will be documented
fully with examples <br> '''Difficulty''': <br> '''Tools''': <br>
'''Time''': <br> '''Mentor''': <br>

=== Fuzzing MPEG2 files === '''Category''': Quality Assurance <br>
'''Description''': <br> '''Outcome''': Fuzz at least 10 MPEG2 files and
file bug reports for crashes w/samples <br> '''Difficulty''': <br>
'''Tools''': <br> '''Time''': <br> '''Mentor''': <br>

=== Fuzzing H264 files === '''Category''': Quality Assurance <br>
'''Description''': <br> '''Outcome''': Fuzz at least 10 H264 files and
file bugreports for crashes w/samples <br> '''Difficulty''': <br>
'''Tools''': <br> '''Time''': <br> '''Mentor''': <br>

=== Fuzzing MPEG4 (Divx/Xvid) files === '''Category''': Quality
Assurance <br> '''Description''': <br> '''Outcome''': Fuzz at least 10
MPEG4 files and file bug reports on crashes w/samples <br>
'''Difficulty''': <br> '''Tools''': <br> '''Time''': <br> '''Mentor''':
<br>

=== Fuzzing MJPEG files === '''Category''': Quality Assurance <br>
'''Description''': <br> '''Outcome''': Fuzz at least 10 MJPEG files and
file bugreports on crashers w/samples <br> '''Difficulty''': <br>
'''Tools''': <br> '''Time''': <br> '''Mentor''': <br>

=== Fuzzing other codecs === '''Category''': Quality Assurance <br>
'''Description''': Other codecs that aren't as mainstream definitely
could use some fuzztesting to shake out problems and possible security
threats <br> '''Outcome''': Fuzz at least 10 files for your chosen codec
and file bugreports on crashers w/samples <br> '''Difficulty''': <br>
'''Tools''': <br> '''Time''': <br> '''Mentor''': <br>

=== Fuzzing existing crashers === '''Category''': Quality Assurance <br>
'''Description''': A wide range of projects use libav, and some of them
maintain bugtrackers or forums which contain records of crashing files
<br> It would be nice to know if those files still crash libav, and if
fuzzing them creates a new crash <br> '''Outcome''': Test 10 open
reports of crashing files from a libav-using project to see if it still
crashes on the latest libav, and then fuzz test those files, filing
bugreports on any crashes found <br> '''Difficulty''': <br> '''Tools''':
<br> '''Time''': <br> '''Mentor''': <br>

=== Common problems with no documented solution === '''Category''':
Research <br> '''Description''': Anyone who has spent some time on
mailing lists or IRC channels starts to see the same questions pop up
time and again <br> The most frequent of these usually get put in an
FAQ, or some other easily-accessible place '''Outcome''': Document an
issue that seems to pop up regularly without getting answered and find
an answer for it <br> '''Difficulty''': <br> '''Tools''': <br>
'''Time''': <br> '''Mentor''': <br>

=== Find a new video codec === '''Category''': Research <br>
'''Description''': There are hundreds of video codecs in existence, and
many of them are known and documented <br> For as many as are known,
there's undoubtedly still more out there waiting to be found and written
about <br> '''Outcome''': Find a video file that does not play in
current libav, and provide information on it, containing at the least:
<br> *Video codec name <br>*\ How to identify this type (usually a
fourcc, a certain file header or a unusual/unique file extension) <br>
*Samples with descriptions of what they depict and codec features used
in them if known <br>*\ Links to the original decoder and encoder <br>
'''Difficulty''': <br> '''Tools''': <br> '''Time''': <br> '''Mentor''':
<br>

=== Find a new audio codec === '''Category''': Research <br>
'''Description''': There are a large number of audio codecs out there,
and just like video codecs, many of them are known and documented <br>
Undoubtedly though, there are still more out there that are not yet
known or documented <br> '''Outcome''': Find a currently unknown audio
codec and provide information about it so it can be eventually supported
<br> This information should include the following: <br> *Audio codec
name <br>*\ How to identify this type (twoCC, a file header or a
distinctive file extension usually) <br> \*Samples, ideally made from
lossless source and details on any features used if known <br>
'''Difficulty''': <br> '''Tools''': <br> '''Time''': <br> '''Mentor''':
<br>

== VideoLAN Communication ==

=== Wiki Orphans and Double tracking === '''Category''': Documentation
<br> '''Description''': The wiki has way too many [[Special:LonelyPages
double redirected pages]], they should be linked by other pages or
marked for deletion, and redirects should be fixed<br> '''Outcome''': A
better wiki with less orphaned pages or redirects <br> '''Difficulty''':
easy <br> '''Tools''': a wiki account<br> '''Time''': 4hours <br>
'''Mentor''': [[User:Xtophe|xtophe]] <br>

=== Wiki short pages tracking === '''Category''': Documentation <br>
'''Description''': The wiki has too many [[Special:ShortPagesxtophe]]
<br>

=== Update wiki guides === '''Category''': Documentation <br>
'''Description''': Not all of the guides on the wiki have been updated
for newer versions of VLC<br> Update one for the latest released version
of VLC<br> '''Outcome''': A working guide for the latest release of VLC
<br> '''Difficulty''': <br> '''Tools''': <br> '''Time''': <br>
'''Mentor''': <br>

=== Create a guide on capturing video from capture cards ===
'''Category''': Documentation <br> '''Description''': A guide to
capturing video from video capture cards <br> One for hardware-encoder
cards, and one for non-hardware encoder cards would be great <br>
'''Outcome''': A guide with screenshots for one type of video capture
card <br> '''Difficulty''': <br> '''Tools''': <br> '''Time''': <br>
'''Mentor''': <br>

=== VideoLAN flyer/poster === '''Category''': Outreach <br>
'''Description''': The VideoLAN project needs a flyer for promotional
matters <br> '''Outcome''': A cool A5-sized flyer presenting VideoLAN
<br> '''Difficulty''': medium <br> '''Tools''': Image-Editing
software<br> '''Time''': 3days <br> '''Mentor''':
[[User:Jpsaman|Jean-Paul Saman]] <br>

=== VideoLAN Forum improvements === '''Category''': Research and
Outreach <br> '''Description''': The VideoLAN [http://forum.videolan.org
forums] have many shortcomings, especially regarding spam and "Solved
topics"<br> We need research on solutions and advise us how we can
improve the forums <br> '''Outcome''': small report on ideas, advice and
solution<br> '''Difficulty''': medium <br> '''Tools''': Browser and Text
editor<br> '''Time''': 3days <br> '''Mentor''': VLC_help <br>

=== VideoLAN PHP webpage for file uploading for bugreports ===
'''Category''': Code <br> '''Description''': The VideoLAN project needs
a small WebPage in PHP to be able to upload the files for the
bugreports<br> As some of those files are big, some progression bar
should be done in Javascript too <br> '''Outcome''': a working deployed
PHP script<br> '''Difficulty''': hard <br> '''Tools''': PHP development
environment<br> '''Time''': 5days <br> '''Mentor''': etix <br>

== VLC == === Create VLC videos for training === '''Category''':
Training <br> '''Description''': Creation of youtube Videos of
screencasts of VLC usage<br> This task can be divided in chunks of 5
videos <br> '''Outcome''': VLC Youtube channels <br> '''Difficulty''':
easy <br> '''Tools''': VLC, screencast recorders<br> '''Time''': 2 days
<br> '''Mentor''': [[User:linkfanel|linkfanel]] <br>

=== VLC documentation illustration === '''Category''': Documentation
<br> '''Description''': Creation of VLC screenshots and small diagrams
to improve the VLC documentation on the wiki<br> '''Outcome''': VLC
illustrations on the documentation <br> '''Difficulty''': easy <br>
'''Tools''': VLC, Image Editing software<br> '''Time''': 5 days <br>
'''Mentor''': [[User:ivoire|Rémi Duraffort]] <br>

=== VLC users survey creation === '''Category''': Outreach <br>
'''Description''': Creation of a survey for VLC users, about their usage
of VLC, that we will put on the website <br> '''Outcome''': Survey ready
to be sent to the VLC users <br> '''Difficulty''': medium <br>
'''Tools''': text editor and web browser<br> '''Time''': 5 days <br>
'''Mentor''': [[User:J-b|jb]] <br>

=== VLC fullscreen controller redesign === '''Category''': User
Interface <br> '''Description''': Find ideas to improve and redesign the
fullscreen controller of the VLC version on Windows/Linux <br>
'''Outcome''': Sketchs and ideas for the fullscreen controller <br>
'''Difficulty''': medium <br> '''Tools''': web browser and image
editor<br> '''Time''': 5 days <br> '''Mentor''': [[User:J-b|jb]] <br>

=== Help out your language's translation === '''Category''': Translation
<br> '''Description''': Help translate more of VLC into your language
<br> '''Outcome''': Add at least 5% more translations <br>
'''Difficulty''': <br> '''Tools''': <br> '''Time''': <br> '''Mentor''':
<br>

=== VLC volume controller redesign === '''Category''': User Interface
<br> '''Description''': Find ideas to improve and redesign the volume
controller of the VLC version on Windows/Linux <br> '''Outcome''':
Sketchs and ideas for the volume controller<br> '''Difficulty''': hard
<br> '''Tools''': web browser and image editor<br> '''Time''': 3 weeks
<br> '''Mentor''': [[User:J-b|jb]] <br>

=== VLC Lyrics extension === '''Category''': Code <br>
'''Description''': Creation of one extension in lua that can be able to
fetch and display Lyrics from one website API<br> '''Outcome''': Working
Lua Lyrics extension script <br> '''Difficulty''': hard <br>
'''Tools''': text editor and VLC <br> '''Time''': 10 days <br>
'''Mentor''': [[User:Jpeg|jpeg]] <br>

=== VLC Songkick extension === '''Category''': Code <br>
'''Description''': Creating one extension in lua that can be able to
fetch and display Lyrics from Songkick API<br> '''Outcome''': Working
Lua Songkick extension script <br> '''Difficulty''': hard <br>
'''Tools''': text editor and VLC <br> '''Time''': 10 days <br>
'''Mentor''': [[User:Jpeg|jpeg]] <br>

=== VLC webplugin testpages === '''Category''': Code <br>
'''Description''': This task is about updating the Html/CSS/JS scripting
test pages for the [[Documentation:WebPluginJean-Paul Saman]] <br>

=== VLC warnings cleanup === '''Category''': Code <br>
'''Description''': This has for objective to delete a lot of warnings in
C and C++ code when doing VLC compilation for Linux and Windows.<br>
'''Outcome''': Less warnings in C and C++ code <br> '''Difficulty''':
hard <br> '''Tools''': text editor and compilation toolchain<br>
'''Time''': 10 days <br> '''Mentor''': [[User:ivoire|Rémi Duraffort]]
<br>

=== libVLC Qt example media player === '''Category''': Code <br>
'''Description''': Creating a small example of how to create a media
player based on libVLC and Qt on Windows/Linux.<br> '''Outcome''': a
cool media player to demonstrate the libVLC API in Qt <br>
'''Difficulty''': hard <br> '''Tools''': complete compilation
toolchain<br> '''Time''': 15 days <br> '''Mentor''': pdherbemont <br>

=== libVLC Gtk example media player === '''Category''': Code <br>
'''Description''': Creating a small example of how to create a media
player based on libVLC and Gtk on Windows/Linux.<br> '''Outcome''': a
cool media player to demonstrate the libVLC API in Gtk <br>
'''Difficulty''': hard <br> '''Tools''': complete compilation
toolchain<br> '''Time''': 15 days <br> '''Mentor''': pdherbemont <br>

=== libVLC Elementary example media player === '''Category''': Code <br>
'''Description''': Creating a small example of how to create a media
player based on libVLC and Elementary on Linux.<br> '''Outcome''': a
cool media player to demonstrate the libVLC API in Elementary <br>
'''Difficulty''': hard <br> '''Tools''': complete compilation
toolchain<br> '''Time''': 15 days <br> '''Mentor''': pdherbemont lu_zero
<br>

=== libVLC wxWidgets example media player === '''Category''': Code <br>
'''Description''': Creating a small example of how to create a media
player based on libVLC and wxWidgets on Windows/Linux.<br>
'''Outcome''': a cool media player to demonstrate the libVLC API in
wxWidgets <br> '''Difficulty''': hard <br> '''Tools''': complete
compilation toolchain<br> '''Time''': 15 days <br> '''Mentor''':
pdherbemont <br>

== VLMC ==

=== Create VLMC videos for training === '''Category''': Training <br>
'''Description''': Creation of youtube Videos of screencasts of VLMC
usage<br> This task can be divided in chunks of 3 videos <br>
'''Outcome''': VLMC Youtube channels <br> '''Difficulty''': easy <br>
'''Tools''': VLMC, screencasting tools<br> '''Time''': 3 days <br>
'''Mentor''': [[User:etix|etix]] <br>

=== VLMC UI testing === '''Category''': Quality Assurance <br>
'''Description''': Testing VLMC Interface and testing all dialogs and
options to find bugs<br> '''Outcome''': Bugreports <br>
'''Difficulty''': easy<br> '''Tools''': VLMC <br> '''Time''': 3 days<br>
'''Mentor''': Hugo <br>

=== VLMC files testing === '''Category''': Quality Assurance<br>
'''Description''': Testing VLMC for Windows or Linux with many file
formats <br> '''Outcome''': Bug reports on the forum that don't work
<br> '''Difficulty''': medium <br> '''Tools''': VLMC, mediainfo,
Windows/Linux <br> '''Time''': 7 days <br> '''Mentor''': Hugo <br>

== Contact == For ANY question, contact [[User:J-bxtophe]]

IRC channel: #videolan or irc://irc.freenode.net

{{GSoC}}

[[Category:SoC 2011 Project|*]]
