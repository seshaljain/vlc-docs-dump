{{SoCProjectstudent=[[User:Gealmentor=Jérôme Decoodt}}

=WinCE Port of VLC=

==Abstract==

The VLC media player has been port to many different platforms, but it
lacks Windows CE support since some versions. This project aims at
making VLC work on a Windows CE platform, with a few features:
*RTSP*\ H264 *Snapshots*\ Playlist \*Rebuild of interface to adapt it to
small screens

==Calendar== '''May 26 :''' Beginning of SoC

'''May 27 :''' Beginning of holidays

'''June 23 :''' Final exams

'''June 25 :''' What is done so far: the LibVLC and nearly all modules
are compiled. I run some tests on LibVLC, to make sure that it will look
good. I've begun the cross compilation of libs, like ffmpeg. The
graphical interface is running, but is uglier than anyone could imagine.
Working on VLC is fun, and I enjoy my summer :)

'''July 14 :''' Mid-term evaluations deadline

'''September 1 :''' Final evaluation deadline

'''September 15 :''' Starting the third year at the "Ecole Centrale de
Lille"

==TODO list==

{\| class="wikitable" ! What !! WHAT!? !! When !! Status Learning \|\|
Read materials about Windows CE, subtle things, little bit of hacking
\|\| May-June \|\| style="background: #ffffdd"-\| Compilation process
\|\| Design an easy compilation, deployment, debugging process, and make
a doc about it \|\| May-June \|\| style="background: #ffffdd"-\|
Contribs \|\| Build a contrib package for Windows CE \|\| All Summer
long \|\| style="background: #ffffdd"-\| Naked VLC \|\| Build a
minimalistic VLC, with an ugly interface and very few libraries \|\|
May, June \|\| style="background: #ffffdd"-\| Adding features \|\| Add
one feature, release a version; add one feature, release a version; make
a cup of coffee; add one feature, release a version \|\| All Summer long
\|\| style="background: #ffffdd"-\| Interfaces \|\| Write a nice looking
and intuitive interface for phones, and one for other types of Windows
CE devices \|\| July \|\| not started Cleaning the code \|\| Fixes,
finish the interface, hoping there are no crash, resetting my phone \|\|
August \|\| not started Let's play \|\| Add funny features: making a
Windows CE streaming server, add support of Camera, GPS \|\| August(if I
have enough time) \|\| not started Build bot \|\| Add the Windows CE
port to buildbot \|\| September \|\| not started Community \|\| Develop
for VLC, and not only on Windows CE \|\| Post GSoC \|\|
style="background: #ffffdd"}

==Contrib package== Actual state of the contrib package for VLC on
Windows CE: *libiconv*\ ffmpeg

==What will be used== This is the list of the tools that will be used to
achieve this project: *[http://www.cygwin.com/ Cygwin], a Linux-like
environment for Windows*\ [http://cegcc.sourceforge.net/ CeGCC], a
cross-compiler for Windows CE based devices
*[http://msdn2.microsoft.com/fr-fr/vstudio/default.aspx Microsoft Visual
Studio 2008] as
IDE*\ [http://msdn2.microsoft.com/fr-fr/library/aa188148.aspx Microsoft
Device Emulator], an emulator for Windows CE and Windows Mobile devices
\*a [http://www.htc.com/FR/Product.aspx?id=16394 HTC P3600 Trinity], for
the tests on real hardware
