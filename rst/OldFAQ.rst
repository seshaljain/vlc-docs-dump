{{Historical}} Answers to some common problems people encounter with
VLC. More help is available in the \* [http://www.videolan.org/doc/
Documentation] \*
[http://www.videolan.org/doc/faq/en/videolan-faq-en.html FAQ] \*
[[Forum]]

== Installing VLC ==

=== Compiling VLC ===

==== How do I compile VLC? ====

-  Look at [http://developers.videolan.org/vlc/ how to compile VLC].
   There are pre-compiled (binary / executable) versions
   [http://www.videolan.org/vlc/ here].

==== Mozilla Firefox Plugin ====

-  ''Debian:'' All you need is to download the vlc plugin package -
   mozilla-plugin-vlc
   ([http://packages.debian.org/stable/graphics/mozilla-plugin-vlc
   stable release])
-  ''All Linux:'' To make the firefox plugin with the vlc player, you
   will first need the Firefox Development package (from:
   [http://packages.ubuntu.com/breezy/devel/firefox-dev ubuntu] ...).
   Then, when you compile, run ./configure with --enable-mozilla, and if
   needed with --with-mozilla-sdk-path=''/path_to_firefox_sdk''

==== "Missing header file ffmpeg/avcodec.h" and "Missing header file
postproc/postprocess.h" Errors ====

\* Make sure that you have all the libraries you need. \*\* '''on
ubuntu''': "apt-get install libavcodec-dev libpostproc-dev" will install
the needed files (worked on edgy). \* When you run ./configure for
[[ffmpeg]], make sure that at least the following flags are set
(descriptions of these avaliable from ./configure --help ) ./configure
--enable-shared --enable-shared-pp --enable-pp --enable-gpl \* The path
of ffmpeg is not set. Check if you can locate the file
'''libavcodec.pc''' on your computer, and export PKG_CONFIG_PATH to
where you found it before running ./configure. For example export
PKG_CONFIG_PATH=/home/you/ffmpeg/

With vlc-086f, FFmpeg SVN-r13060, on Slamd64 12.0.0, some other changes
must be made. These are most likely due to changes in libpostproc.

The ./configure flags for ffmpeg become
   ./configure --enable-postproc --enable-shared --enable-gpl

Then you must set a symbolic link for postproc. This took me a long time
to spot.

   root @ svr (/usr/src/vlc-0.8.6f)locate postprocess.h
   /usr/local/include/libpostproc/postprocess.h root @ svr
   (/usr/src/vlc-0.8.6f)cd /usr/local/include/ root @ svr
   (/usr/local/include)ln -s libpostproc postproc

==== "cc1: error: invalid option \`tune=opteron'" Error on 64-bit
systems ====

-  One user writes: "From what I can see, the -mtune flag is not
   available for this type of processor in man gcc. I had to change the
   configure options comment out all the lines where they set mcpu or
   mtune flags.) I don't know if this is the correct way to proceed but
   was the only way for me to get results fast."
-  This is not true on all versions of gcc. Try to compile on your
   platform before making the above changes.

..

   root @ p01 (/usr/src/vlc-0.8.6f)gcc --version gcc (GCC) 4.1.2

   root @ p01 (/usr/src/vlc-0.8.6f)uname -a Linux p01 2.6.24.3 #2 SMP
   Tue Apr 8 12:01:03 EDT 2008 x86_64 x86_64 x86_64 GNU/Linux

   root @ p01 (/usr/src/vlc-0.8.6f)grep tune= config.log
   configure:37114: checking whether gcc accepts -mtune=athlon64
   configure:37125: gcc -c -Wsign-compare -Wall -pipe -mtune=athlon64
   -DSYS_LINUX conftest.c >&5

   root @ p01 (/usr/src/vlc-0.8.6f)grep cpu= config.log
   build_cpu='x86_64' host_cpu='x86_64' target_cpu='x86_64'

==== "/usr/bin/ld: cannot find -lX11" Error on 64-bit systems ====

-  In configure, there is an x_libraries variable there that is set to
   "/usr/X11R6/lib" (around line 16371). Because it is a 64 bit system,
   this variable needs to be /usr/X11R6/lib64. After changing that, it
   should continue compiling.

==== "syntax error before "pthread_spinlock_t"" on debian-Etch or CentOS
====

\* If you have errors about ''pthread_spin*'' in the file ''vlc_threads_funcs.h'', try this fix :
   su sed -e 's/defines*\_POSIX_SPIN_LOCKSs*/define \_POSIX_SPIN_LOCKS
   -1 // wrong: /g' -i /usr/include/bits/posix_opt.h exit

source : [http://forum.videolan.org/viewtopic.php?f=13&t=43930#p139570
this post] from Rémi Denis-Courmont.

=== Installing Skins ===

-  Although all information is given on the
   [http://www.videolan.org/vlc/skins.php VLC Download skin site], you
   may miss the note to change preferences to ''skinnable interface''.
   There is an [http://forum.videolan.org/viewtopic.php?p=85603#p85603
   article on the forum] which describes the how-to. In short: there is
   a drop-down option (interface module) in the settings dialog
   (Interface &rarr; General) which defaults to ''Standard''. Change
   this and restart.

== Problems Starting VLC ==

== Error Messages ==

Error messages can be viewed by selecting Messages from the Tools menu.

=== main private error: no sout mux module matched "ts" ===

-  This can be an error if '''libdvbpsi''' was not installed when vlc
   was compiled. To fix this error, install libdvbpsi; then re-compile
   vlc. [http://developers.videolan.org/libdvbpsi/ libdvbpsi]

=== main dialogs provider error: no dialogs provider module matched
"any" ===

-  The solution is found in
   [http://forum.videolan.org/viewtopic.php?t=14733 the forum]

== Problems playing types of files ==

=== WMV files ===

-  Starting with VLC media player 0.8.6, the playback of WMV3-encoded
   videos is available on all platforms. Please note, that encrypted /
   DRM-protected video-clips still cannot be played. That is due to the
   nature of DRM and is not about to change, so please do not ask.

=== Real Media files ===

-  Realmedia files (.rm, .rpm, etc) are proprietary (ie, copyrighted)
   file formats, created by RealNetworks. Because of this, VLC can't
   support them at present.

=== QuickTime Files (.mov) ===

\* Mov file doesn't play, but plays ok in QuickTime \*\* open the url in
QuickTime player \*\* let it decide which datarate is best for your
connection \*\* let it play for a few seconds, then pause it \*\* open
the stream info, copy the url \*\* open & save that one in VLC

=== Flash Video Files (.flv) ===

-  Flash Video support has recently been added (provided through ffmpeg)
   - to view .flv files you will need version 0.8.4a. Download and
   install the latest version [http://www.videolan.org/vlc/ here].
-  VLC still has problems with a few .flv files. If you have problems
   playing a file in VLC you might be able to change it to an avi using
   [[ffmpeg]]. See [[Fixing .flv to .avi with FFmpeg]].
-  VLC 0.8.6 provided enhanced Flash Video support on all platforms, so
   it is probably worth to update if you experience problems with prior
   releases.

=== Other Files ===

{{faqlink|238663}} \* Make sure that VLC supports that file - look at
the [http://www.videolan.org/vlc/features.html list of supported
formats]

-  Make sure that the file isn't corrupted

== VLC and Other Programs ==

=== AMR ===

-  To use [http://en.wikipedia.org/wiki/Adaptive_Multi-Rate AMR], you'll
   need to compile vlc and ffmpeg with amr support yourself. This is
   because the amr license is not compatible with the vlc license.

=== ratDVD ===

-  VLC does not support [http://en.wikipedia.org/wiki/RatDVD ratDVD] and
   is not going to be, both for political and technical reasons.

== Problems Playing DVDs ==

===Unable to play any DVDs===

{{faqlink Preferences \| Input/Codecs \| General and under "Default
devices" make sure your dvd drive path is entered in the "Default DVD"
box. When you go to open a DVD, you should see something like
"dvd:///dev/dvd" as the [[media resource locator]] in the "Open:" box
near the top of the Open dialog.

=== Playing DVDs from other Region Codes ===

{{faqlink|239426}} \* The ability to play DVDs from all regions depends
mostly on your DVD drive, and testing it is usually the quickest way to
find out if your DVD drive can do it. Most newer DVD drives are RPC2
drives, which don't allow raw access to the drive untill the drive
firmware has done a regioncheck. VLC uses libdvdcss and it needs raw
access to the DVD drive to crack the encryption key. So with these
drives it is impossible to circumvent the region protection. (This goes
for all software. You will need to flash your drives firmware, but
sometimes there is no alternate firmware available for your drive). On
other RPC2 drives that DO allow raw access, it might take VLC a long
time to crack the key. So just pop the disc in your drive and try it
out, while you get a coffee. RPC1 drives should 'always' work regardless
of the regioncode.

== Poor Quality Video and Audio ==

=== The video runs but the picture is distorted ===

{{faqlink|238431}} \* ''Linux:'' There is probably a problem with the
output layer. There are several ways of troubleshooting it. \*\* First,
try with another output plugin, for instance: **: % vlc -V sdl**: % vlc
-V x11 \*\* Second, change your screen depth and/or definition. It quite
often helps. \*\* Lastly, if running Unix, have a look at your XFree86
video driver.

-  ''Windows:'' See
   [[WindowsFAQ-1.1.x#Why\_`does_VLC_only_give_black.2C_white_or_garbled <>`__.28or_other_visual_erros.29_video_output.3F]]

=== Video is choppy ===

{{faqlink|238474}} \* Your system may be too slow to decode all
pictures. Sometimes, your CPU (computer) really isn't fast enough, but
often the situation can be improved by changing your system
configuration to be a bit kinder to VLC. \*\* Quit other programs
running in the background \*\* Turn on DMA on your DVD device: **\*
''Linux:''**\ *: <nowiki>#</nowiki> hdparm -d1 /dev/dvd*\ \*\*
''Windows:'' go to the System section of the control panel, and go to
the Hardware manager (it is sometimes in a separate tab, and sometimes,
you have to go to the Advanced tab. Then, right-click on your DVD
player, and check the DMA checkbox. \*\* Upgrade to the latest driver
for your video board. \*\* ''Linux:'' you can additionally upgrade your
drivers to the latest XFree86 version. If supported, check that the
xvideo plug-in is effectively used with: \**: % vlc -vvvv

=== Audio and video are out of sync ===

{{faqlink|238571}} \* If you are [[transcoding]] a file, use the
[[audio-sync]] option. \* You can manually set the audio offset while
playing (so you can put the audio back in sync). The default keys to
increase/decrease the offset are Ctrl+K and Ctrl+L in Windows, and f and
g in Mac. \* ''Linux/Unix:'' Try using another audio output plugin and,
under Unix, kill esd or artsd if they are running. If the problem is due
to the input file, have a look at the "Audio desynchronization
compensation" option.

=== Audio is choppy ===

-  Reboot? http://ubuntuforums.org/showthread.php?t=1288433
-  Try a different codec if transcoding to ogg

== Problems with Streaming ==

==="main input error: no suitable access module for \`\ rtsp://...'"===

vlc needs livemedia from '''live555.com''' to read rtsp stream this way.

You can check you have it by :

   vlc -l \| grep live

It should read

   livedotcom live.com (RTSP/RTP/SDP) demuxer livedotcom RTSP/RTP access
   and demux

If not, you have to install '''livemedia''' and point your compilation
to this lib directory :

   ./configure '''--enable-livedotcom
   --with-livedotcom-tree=/usr/local/lib/live/'''

===Streaming playlist continuously between files (sout-keep not
working)===

add the gather module to the sout chain, for example
   vlc \*mpeg --sout-keep --sout '#gather:transcode{plapla}:rtp{plapla}'

===Streaming 1 playlist item continuously and change input without
stream break===

you can use this kind of a vlm.conf file with the --sout-keep option
   new output1 broadcast enabled loop setup output1 input
   "inputfile1.mpeg" setup output1 input "inputfile2.mpeg" setup output1
   input "/path/to/inputfile3.mpeg" setup output1 option sout-keep setup
   output1 option input-repeat=-1 setup output1 output
   #gather:transcode{etc...}:std{plapla}

   control output1 play 2

you then chan telnet into vlm and just command
   control output1 play <playlistnumber>

to change the streamed input.

===Streaming to Windows Media Player===

See [[Windows Media Player]] for details.

== Problems converting between file formats (transcoding) ==

=== Missing Audio and/or Video ===

-  Certain containers (aka muxers) can only hold certain types of video
   and audio - look at [[Transcode#Compatibility_issues]].

== Streaming/Transcoding Wizard ==

=== Transcode / Save to file ===

== VLC Crashes ==

=== General ===

{{faqlink|238592}} \* If VLC crashes, the following steps will help
determine the cause. \*\* Increase the verbosity level (either in the
preferences or with a -vvvv command line option) and look at the debug
messages (in the terminal or in the Messages window). \* If you are
convinced that it is a bug in VLC, have a look at the
[http://www.videolan.org/support/bug-reporting.html bug reporting page].

=== When using DirectShow (eg Webcam) ===

{{forum|12394}} \* There was a bug a while back when you tried to stream
using a directshow/webcam it would reboot the computer. The fix was to
specify the resolution on the command line or in the "Advanced" section
when opening the directshow.

== Other Problems ==

=== I only want one VLC player! ===

-  To use the same VLC player for all the media files, go to Settings,
   Preferences, Advanced. The following options should give behavior
   similar to WMP: minimize # of threads, allow only one running
   instance, VLC is started from file association, allow only "on"
   running instance when started from file (typo in v0.8.5).

=== Licensing, legal issues and logo use ===

-  Information on this is avaliable on the main videolan website,
   [http://videolan.org videolan.org]. Also read the
   [http://www.videolan.org/doc/faq/en/index.html#id238663 Legal
   concerns] section of the
   [http://www.videolan.org/doc/faq/en/index.html FAQ].
-  This is a wiki site: it is editable by all, so it is best to check to
   official website.

=== Fixing Strange Behaviour ===

{{faqlinkwhere is it?]]). Then restart VLC. If it does not get any
better, read the rest of this page or FAQ page, or ask for help at the
[[forum]].

=== Subtitles Problem ===

-  In the File \| Open File dialog, select "Use a subtitles file", and
   enter both the video's filename and the video's subtitle filename.
-  If you are having displaying the subtitles, the problem might be an
   encoding problem. Choose the right encoding for your language and it
   should fix your problem. You'll find the ISOs here:
   [http://alis.isoc.org/codage/iso8859/jeuxiso.en.htm]. Once you find a
   text encoding method that works well for you enter it in Preferences,
   Input / Codecs, Other codecs, Subtitles then press Save and restart
   VLC. Uncheck the "Formatted Subtitles" may help if the subtitles only
   display as little squares. If you have a specialized language like
   Hebrew, Arabic, Chinese or Japanese changing the font to a Unicode
   font will be helpful. For Polish subtitles choose CP 1250 ISO code.

=== VLC hangs when opening Matroska (mkv) files ===

\* This might occur when using VLC to view an mkv file in a directory
that has a large number of mkv files. (eg. in an Azureus download
directory) VLC will attempt to preload all the mkv files in the
directory and will hang, especially if some mkv files are not fully
downloaded yet (thus seem to be broken). \* The solution is to set the
mkv option: --mkv-preload-local-dir to false Preferences -> Input /
Codecs -> Demuxers -> Matroska -> Preload Directory (uncheck the
checkbox) (See also [[Matroska]])

=== Coarse volume control ===

Volume control, specially with Hotkeys, is too coarse. \*To have a finer
volume control, try the following option on the command line:
<code>--volume-step=1</code> :See also [[VLC command-line help]]

[[Category:FAQ]] {{Documentation}}
