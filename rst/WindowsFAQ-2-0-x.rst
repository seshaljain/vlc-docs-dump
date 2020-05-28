This page contains list of common questions and problems (FAQ aka
Frequently asked questions) that [[Windows]] users have about [[VLC
media player]] 2.0.x

{{WindowsFAQ}} {{Historical}} ==Video output related questions and
problems== ===Why does VLC only give black, white or garbled (or other
visual errors) video output?=== Usually the problem lies in display
adapter drivers. If you are too scared to update your display adapter
drivers, you can change VLC settings to make video work. If you are
using Windows XP or older the easiest fix is usually to disable
'''Accelerated video output/Overlay video output''' which can be found
first opening '''Tools -> Preferences''' and then choosing '''Video'''.
After you have unticked the Accelerated video output, press '''Save'''
to save VLC settings and restart VLC after that to make sure changes are
enabled. [http://raiska.comeze.com/tutorials/vlc092/11a.png Image about
Overlay video output setting]

If disabling Overlay video output doesn't help, then the next step is to
change video output module (aka '''VOUT'''). Open '''Tools ->
Preferences''' (set Show Settings to All) and then choosing '''Video ->
Output module'''. There are multiple output modules you can use. For
Windows XP and younger you can try '''DirectX 3D''', '''DirectX''',
'''OpenGL''' and '''Windows GDI''' video output modules. With Windows
Vista and with Windows 7, both DirectX and Windows GDI output modules
will disable Aero, so if you want to use Aero, please use DirectX 3D
(should be default). Remember to press '''Save''' to save VLC settings
and restart VLC after that to make sure changes are enabled.
[http://raiska.comeze.com/tutorials/vlc092/11b.png Image about video
output modules setting]

===Video shows green, blue or red lines=== See above.

===Video Colors are washed out (NVIDIA issue)=== Please see
[[VSG:Video:Color_washed_out]]

===How can I adjust brightness or contrast?=== You can adjust
brightness, contrast and other settings via '''Extended settings'''.
Open '''Tools -> Effects and Filters''' to adjust these settings
('''Video Effects -> Essential''' and tick '''Image adjust'''). Changes
should show up realtime.

====How can I keep the brightness and contrast adjustments in memory
forever?==== Open '''Tools -> Preferences''' (set Show Settings to All)
and then choosing '''Video -> Filters -> Image Adjust''' and set values
you want to use (trial and error).

====Can I set file specific brightness or contrast?==== Yes, but it
isn't that easy. You have to create VLC shortcut or bat file with proper
settings. More info can be found from
[http://forum.videolan.org/viewtopic.php?f=14&t=46202#p152964 this]
thread

===How do I set the default deinterlace method?=== '''Tools ->
Preferences''' (Show settings: All) '''Video -> Filters''' and tick
'''Deinterlacing''' video filter from under '''Video output filter
module''' (NOT FROM UNDER Video filter module!). Then '''Video ->
Filters -> Deinterlace''' and choose the default mode. Remember to press
'''Save''' to save VLC settings and restart VLC after that to make sure
changes are enabled.
[http://img399.imageshack.us/img399/4220/vlcdeinterlace01hc2.png] image
showing the Video output filter module part

==Audio output related questions and problems== ===Crackles, pops,
hizzes and other audio anomalies=== If you hear some unwanted audio
problems you can try another audio output module to see if that solves
the issue (Save and restart VLC after changes). Open '''Tools ->
Preferences''' (set Show Settings to All) and then choosing '''Audio ->
Output module'''. There are multiple output modules you can use for
audio. '''DirectX''' and '''Win32 waveOut''' should work in most cases.
Unfortunately there isn't an ASIO support in VLC.
[http://raiska.comeze.com/tutorials/vlc092/10b.png Image about audio
output modules setting]

===Crackles, pops, hizzes and other audio anomalies with SPDIF
passthrough=== SPDIF passthrough of Dolby Digital (AC3) and DTS
audiotracks don't work with all soundcards. '''Win32 waveOut''' output
module should work better with SPDIF. ===I don't hear dialog,
conversations etc. while playing 5.1 audio=== Make sure you have select
proper speaker setup from Windows audio settings or from soundcard
control panel. If you have done so, make sure VLC also has right
settings. '''Audio -> Audio Device''' to select proper speaker settings
during playback. ===How do I adjust audio delay?=== During playback you
can press '''k''' or '''j''' to adjust audio delay (adjust step is 50
ms). ===How can I play external audio track with video?=== '''Media ->
Open (Advanced)...''' and select the video file and after that tick
'''Show more options''' and then '''Play another media
synchronously...''' and select the audio file you want to use. Then when
playing the video go to '''Audio -> Audio Track -> Track 2''' to select
the second (or whichever it is) audio track (this so called Slave-mode
doesn't work correctly). ===How do I change my output device in case I
have multiple audio devices connected to my PC?=== Open '''Tools ->
Preferences''' (set Show Settings to All) and if you use DirectX, then
'''Audio -> Output modules -> DirectX''' and '''Output device'''. If you
use Waveout, then '''Audio -> Output modules -> WaveOut''' and '''Select
Audio Device'''. Remember to press '''Save''' to save VLC settings and
restart VLC after that to make sure changes are enabled. ===How can I
override speaker setup? (e.g. I want to always default to stereo)=== You
can force speaker setup if you use DirectX audio output from '''Tools ->
Preferences''' (set Show settings to All) '''Audio -> Output modules ->
DirectX''' and '''Speaker configuration''' dropdown menu. Remember to
press '''Save''' to save VLC settings and restart VLC after that to make
sure changes are enabled. ===Why does VLC volume change when I attach my
mobile phone to computer during playback?=== This is a feature of
Windows. You can adjust this via '''Control Panel'''. Open '''Sound'''
and go to '''Communications''' tab.<br />
[[File:Vlc_faq_usb_audio_windows_quiet.jpg]]

==(Graphical) user interface related questions and problems== ===How can
I separate playback controls from playback window?=== Go to '''Tools ->
Preferences''' (set Show Settings to All) and '''Video''' and untick
'''Embedded video''' selection. Remember to press '''Save''' to save VLC
settings and restart VLC after that to make sure changes are enabled.

===How can I make skinned interface my default interface?=== Go to
'''Tools -> Preferences''' (set Show Settings to All) and '''Interface
-> Main interfaces''' and from '''Interface module''' dropdown box
select '''Skinnable Interface'''. Remember to press '''Save''' to save
VLC settings and restart VLC after that to make sure changes are
enabled. [http://raiska.comeze.com/tutorials/vlc092/20.png Image about
Skinnable Interface setting]

===Can I jump to certain time?=== You can use '''--start-time''' from
command line when you start VLC. There is also '''Playback -> Jump to
Specific Time''' (Ctrl+T) option in GUI.

===How can I change UI language?=== You can use '''Tools ->
Preferences''' and '''Interface''' and select correct language from
'''Menus language''' drop down list. Remember to press '''Save''' to
save VLC settings and restart VLC after that to make sure changes are
enabled.

Also you can use '''--language=''' from command line if you can't
navigate with current language or you want to use batch files/scripts.
for example: '''vlc --language=en''' to get English. Other options are
auto, en, ar, pt_BR, en_GB, ca, zh_TW, cs, da, nl, fi, fr, gl, ka, de,
he, hu, it, ja, ko, ms, oc, fa, pl, pt_PT, ro, ru, zh_CN, sr, sk, sl,
es, sv, tr

===How can I disable fullscreen controller?=== You can use '''Tools ->
Preferences''' (set Show Settings to All) and '''Interface -> Main
interfaces -> Qt''' and untick '''Show a controller in fullscreen
mode''' option. [http://raiska.comeze.com/tutorials/vlc092/25.png Image
about fullscreen controller setting]

===Why doesn't the time slider show up?=== If you use WindowBlinds or
similar custom skin engine, it usually breaks QT4 interface in VLC. So
either disable that engine with VLC or change VLCs GUI to something else
(like skins2).

===How can I disable showing of the filename when video starts?=== Go to
'''Tools -> Preferences''' (set Show Settings to All) and '''Video'''
and untick '''Show media title on video'''. Remember to press '''Save'''
to save VLC settings and restart VLC after that to make sure changes are
enabled.

===How do I disable showing of the Privacy and Network Policies dialog
during first VLC startup?=== Launch VLC with '''--no-qt-privacy-ask'''
command-line option.

===How do I disable pop up track notification shown in system tray
(systray)?=== Go to '''Tools -> Preferences''' (set Show Settings to
All) and '''Interface -> Main interfaces -> Qt''' then untick '''Show
notification popup on track change'''. Remember to press '''Save''' to
save VLC settings and restart VLC after that to make sure changes are
enabled.

===How do I disable Recent Media part of QT4 interface?=== Go to
'''Tools -> Preferences''' (set Show Settings to All) and '''Interface
-> Main interfaces -> Qt''' then untick '''Save the recently played
items in the menu'''. Remember to press '''Save''' to save VLC settings
and restart VLC after that to make sure changes are enabled.

===How do I disable the blank space at the bottom of QT4 interface? (aka
Status bar)=== Untick the View -> Status Bar

===How do I change playlist icons to list view or vice versa in QT4
interface?=== Click the icon/button in playlist to toggle between
modes<br />

[[File:vlc_faq_playlist_icons.jpg]]

==Codec compatibility related questions and problems== ===How can I
identify what codecs the file uses=== With VLC, Open the file you want
and open '''Tools -> Codec Information'''. ===VLC doesn't identify used
codecs correctly or gives "undf" as codec or I want more information
about specs=== There are multiple video and audio identification tools,
but one very useful is tool called [http://mediainfo.sourceforge.net/
Mediainfo]. ===H.264/MPEG-4 AVC playback is too slow (or laggy)=== You
can speed up the H.264/MPEG-4 AVC playback by disabling loop filter for
H.264 decoding. To do this go to '''Tools -> Preferences''' and '''Input
/ Codecs ''' and in the drop-down box for '''Skip H.264 in-loop
deblocking filter''' change it to '''All'''. Remember to press
'''Save''' to save VLC settings and restart VLC after that to make sure
changes are enabled.

Also if you have multicore CPU (or one with Intel Hyper-Threading), you
can lower the FFMPEG thread count. To do this go to '''Tools ->
Preferences''' (Show settings: All), then '''Input / Codecs -> Video
codecs -> FFmpeg''', then locate Threads, and set it to 4 (or to 2, or
to 1). Remember to press '''Save''' to save VLC settings and restart VLC
after that to make sure changes are enabled.

===H.264/MPEG-4 AVC or VC-1 playback is full of image errors=== You can
also try to enable/disable GPU decoding, and see if it helps. It can be
found from '''Tools -> Preferences''' and '''Input & Codecs''' and
tick/untick '''Use GPU accelerated decoding'''. Remember to press
'''Save''' to save VLC settings and restart VLC after that to make sure
changes are enabled.

===Problem with Real audio or Real video support=== Most Real audio or
Real video should work with VLC 2.0.0, but if you have file that doesn't
work then post thread to forums. ===Why can't VLC use CoreAVC, FFDshow,
AC3filter, etc. codecs?=== VLC only uses built in codecs (see
[http://en.wikipedia.org/wiki/VLC_media_player]) so it doesn't support
VfW or DirectShow APIs for codecs. You are free to hack the source and
use it, though, for example it is possible to make VLC into a directshow
filter [http://www.sensoray.com/support/videoLan.htm]. ====But you
support [[DMO]] (Direct Media Object) module for WMV video and WMA
audio==== WMV and WMA are exceptions to this external codec support.

==File and media format compatibility related questions and problems==
===Some DVD movies don't work at all or they crash/freeze to menu or
playback=== If you open DVD with '''DVD''' selection, try with '''No DVD
menus''' option (aka '''dvdsimple''').

Some new DVD movies use copy protection mechanisms that VLC doesn't
support. It might help if you rip that movie to hard drive using tools
like '''DVDFab Decrypter''' or '''AnyDVD''' and use VLC to playback
these files from hard drive.

You may also be able to play these copy protected DVDs by opening the
movie initialization file directly. Use the '''Open File''' function in
VLC and navigate to the '''VIDEO_TS''' directory on the DVD, then open
the '''VIDEO_TS.IFO''' file. Some of the newest copy protection schemes
have been found to use tricks that confuse many of the current DVD
software programs so they cannot locate this file properly to initiate
playback on their own. This method has been found to work with some of
the newest DVDs that won't open properly in VLC 1.1.11 using the
standard approaches.

===DVD movies don't playback smooth (they stutter, lag, etc.)=== One
thing that might help is increasing the VLC DVD cache. This can be done
from '''Tools -> Preferences''' (set Show Settings to All) and '''Input
/ Codecs''' and increase '''Disc caching (ms)''' value to e.g. 5000 or
20000. Remember to press '''Save''' to save VLC settings and restart VLC
after that to make sure changes are enabled.

If DVD files from hard drive work better, then check that your DVD drive
has DMA enabled (if it is a IDE/ATAPI DVD drive).

===Can I play DVD files (VOB+IFO) from hard drive?=== Yes you can. Use
'''Media -> Open Disc...''' and instead of DVD drive, point the location
to correct folder by using either '''Browse...''' button or customize
field . For example: '''dvd://"c:moviesBLOOD DIAMONDVIDEO_TS"''' ===How
do I handle the broken AVI files?=== Some AVI files may give '''The AVI
file is broken. Seeking not work correctly.Do you want to try to
repair(this might take a long time)''' dialog. Those AVI files have some
issues and you can try to fix those file temporarily with VLC or
permanently with other tools. If you don't fix those files, seeking
won't work correctly and those files may also crash players. ====Can I
always perform same repair action?==== Yes you can. This can be done
from '''Tools -> Preferences''' (set Show Settings to All) and '''Input
/ Codecs -> Demuxers -> AVI''' and select the wanted action from
'''Force index creation''' dropdown box. '''Ask''' is default (it will
always ask what you want to do). '''Always fix''' tries to always fix
AVI files and '''Never fix''' always starts the playback without fixing.
Remember to press '''Save''' to save VLC settings and restart VLC after
that to make sure changes are enabled. ====Can I fix those broken AVI
files permanently?==== Yes. You can try for example
[http://www.divfix.org/ DivFix++] or [http://www.virtualdub.org/
Virtualdub] for fixing. Virtualdub
[http://forum.videolan.org/viewtopic.php?f=14&t=45427&p=143688&hilit=virtualdub#p143688
help].

====Can I fix those broken or partially downloaded Matroska/MKV files
too?==== Yes. You can try [http://meteorite.sourceforge.net Meteorite]
for fixing. ===Some MP4 or 3GP files don't have audio at all=== If those
files have AMR audio (usually ones from mobile phones) they might not
work with current stable VLC versions. ===How do I enable Blu-ray disc
playback (for commercially released Blu-rays)=== You have to download
some additional files, see http://vlc-bluray.whoknowsmy.name/
==Subtitles related questions and problems== ===How do I adjust subtitle
delay?=== During playback you can press '''h''' or '''g''' to adjust
subtitle delay (adjust step is 50 ms). ===How can I select right
subtitle track?=== If your video has multiple subtitle tracks, you can
select the one you would like to see from '''Video -> Subtitles
Track'''. ===Can I disable hardcoded or "burned" subtitles with VLC?===
No. ===Can I change font, font size, style or color?=== You can with
text-based subtitle formats ([[Subtitles codecs]]). Go to '''Tools ->
Preferences''' and '''Subtitles/OSD''' and adjust anything you want.
Remember to press '''Save''' to save VLC settings and restart VLC after
that to make sure changes are enabled. ===How can I change subtitles
text encoding?=== If you see wrong characters on screen or '''failed to
convert subtitle encoding''' error message you should try to change
'''Default encoding''' option which can be found from '''Tools ->
Preferences''' and '''Subtitles/OSD'''. Remember to press '''Save''' to
save VLC settings and restart VLC after that to make sure changes are
enabled.

==General problems and issues== ===VLC crashes/freezes/BSODs my
computer=== VLC doesn't do that. Normal apps shouldn't be able to cause
issues like these to operating systems. Culprit is usually bad device
driver (for example display adapter driver, soundcard driver, chipset
driver, network adapter driver etc.) or broken hardware. ===How do I
reset VLC settings?=== If you can start VLC, go to '''Tools ->
Preferences''' and then press '''Reset Preferences''' and '''Save''' to
reset and save VLC settings. Remember to restart VLC after that to make
sure changes are enabled.

If you can't start VLC, go to '''%appdata%''' folder and delete
'''vlc''' folder from there (Start -> run and type '''%appdata%vlc'''
there and press OK if you can't locate %appdata%).

Also start menu -> VideoLan -> "Reset VLC media preferences ..."

===VLC crashes on startup=== This usually happens because VLC setting
files have been corrupted. Resetting VLC settings (see above) should fix
this. ===I messed up my file associations or I want to modify them===
Please read [[Windows#How_to_associate_media_files_to_VLC|this
documentation]] or reinstall VLC.

===Can VLC burn CD, DVD, HD DVD or Blu-ray discs?=== No. ===Is VLC legal
in all countries?=== Probably not. Specially DeCSS module might violate
DMCA (and similar laws) and some codecs would require licenses for
personal/commercial use. There haven't been any court cases related to
VLC but specially companies should make sure they pay license fees to
license holders if they use VLC commercially and use patented formats or
codecs.

===Can I run multiple VLC instances?=== Yes you can. Read
[[How_to_play_multiple_instances_of_VLC|this documentation]].

===VLC 2.0.0 doesn't work with Windows Me/98/98se/95/NT/2000=== This is
by design. You need at least Windows XP with SP2 to run latest VLC. With
Windows Me/98/98se/95/NT you can use VLC 0.8.6i out of box. With Windows
2000 the latest guaranteed working version is VLC 1.1.11. You can also
check out [http://forum.videolan.org/viewtopic.php?f=14&t=64425 this
forum post ] for tips running latest VLC under Windows 98 or Windows Me.
Or [http://forum.videolan.org/viewtopic.php?f=14&t=98239#p328759 this
forum post ] for tips running latest VLC under Windows 2000.

===How can I make VLC to preview my eMule downloads?=== Check out
[http://forum.videolan.org/viewtopic.php?f=14&t=61826#p206451 this forum
post ].

===How do I specify the folder where the recorded files (via red rec
button) will be stored?=== '''Tools → Preferences''' and '''Input &
Codecs''' and '''Record directory or filename'''. Remember to press
'''Save''' to save VLC settings and restart VLC after that to make sure
changes are enabled.

{{Anchoring space}}
