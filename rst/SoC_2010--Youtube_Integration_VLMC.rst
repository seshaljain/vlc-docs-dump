{{SoCProjectstudent=[[User:rohityadavmentor=[[User:etix|Ludovic
Fauvet]]}}

= Youtube Integration+ in VLMC =

== Abstract ==

Youtube is the most popular video sharing website, right now. VLMC is a
video editing software and having features in VLMC to search-retrieve
videos, directly upload/update/delete videos on Youtube, within the
application itself, would be awesome. The aim of this project is to
write a small C++/Qt based Youtube client library for VLMC that provides
her all the APIs to perform all those things.

== Milestones ==

{\| class="wikitable" -\| Sharing option, video export/rendering for
Youtube \| 24 May 2010 Port VLMC to Mac OS \| 27 May 2010 DEB/RPM
support in Build System \| 29 May 2010 Mac Bundle / DMG in Build System
\| 30 May 2010 Youtube API key, Authentication \| 11 June 2010 Network
Proxy support \| 15 August 2010 Direct Video Upload! \| 19 June 2010
YouTube XML Feed Parser \| 5 July 2010 }

== Short Term Goals ==

0. Proxy support.
1. XML parsing, copy url(s) to clipboard...
2. Handling Network/YT failure.
3. NSIS/Windows build problem.
4. Mac detatched video widget bug.

== Proposed Timeline ==

{\| class="wikitable" -\| Get Youtube Developer Key, study
authentication protocol and start hacking VLMC. \| May 24 - May 30

| Completed

Implement and test authentication API in VLMC.&nbsp;Export movie project
+ UI (supported formats). Start studying direct upload API. <br>

| 

May 31 - June 20<br>

| Completed

Direct upload must be implemented by now. <br>

| June 20 - June 27
| Completed.

Add option in VLMC preferences to configure Network Proxy and manage
Youtube credentials. <br>

| June 28 - July 25
| Completed.<br>

Other feature(s) in VLMC...<br>

| July 26 - August 8
| Completed.

Prepare final report and patch covering all the work done during the
SoC.<br>

| August 9 - August 15
| Completed

Submit patches to Google, SoC Over! \| &gt;16 August \| DONE! \|}

Tracker:
https://spreadsheets.google.com/ccc?key=0Avd3p221yiM5dEg0WDBIY0ZkNXUzczRpVzNrWDNuUVE&hl=en#gid=0

== Repository ==

=== VLMC ===

VideoLAN Movie Creator is a non-linear editing software for video
creation based on libVLC and running on Windows, Linux and Mac OS X. \*
http://github.com/bhaisaab/vlmc

=== Libishare ===

A small library that lets you share videos on popular video sharing
sites such as YouTube. \* http://github.com/bhaisaab/libishare

[https://www.ohloh.net/accounts/58276?ref=Detailed
https://www.ohloh.net/accounts/58276/widgets/account_detailed.gif]

== Builds ==

Coming soon!

== References ==

-  Building VLMC from source visit:
   [http://wiki.videolan.org/Building_VLMC Building VLMC from Source]
-  Building x264 and FFMPEG from src:
   http://ubuntuforums.org/showthread.php?t=786095
-  VLC Build Configuration:

   mkdir build && cd build

   ../configure --prefix=/usr --enable-snapshot --enable-dbus-control
   --enable-mozilla --enable-lirc --enable-live555 --enable-x264
   --enable-shout --enable-taglib --enable-v4l --enable-dvb
   --enable-realrtsp --enable-svg --enable-dvdread --enable-dc1394
   --enable-dv --enable-theora --enable-faad --enable-twolame
   --enable-real --enable-flac --enable-tremor --enable-dirac
   --enable-skins2 --enable-qt4 --enable-ncurses --enable-aa
   --enable-caca --enable-portaudio --enable-jack --enable-xosd
   --enable-avcodec --enable-avformat --enable-swscale --enable-mad
   --enable-a52 --enable-libmpeg2 --enable-dvdnav --enable-vorbis
   --enable-ogg --enable-theora --enable-mkv --enable-freetype
   --enable-fribidi --enable-speex --enable-flac --enable-alsa
   --with-ffmpeg-mp3lame --with-ffmpeg-faac --enable-x11 --enable-xvideo
   --disable-gtk --enable-sdl --enable-avcodec --enable-avformat
   --enable-swscale --enable-mad --enable-libdvbpsi --enable-a52
   --enable-libmpeg2 --enable-dvdnav --enable-faad --enable-vorbis
   --enable-ogg --enable-theora --enable-faac --enable-mkv
   --enable-freetype --enable-fribidi --enable-speex --enable-flac
   --enable-alsa --disable-kde --enable-qt4 --enable-ncurses
   --enable-release
