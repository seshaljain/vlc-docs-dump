.. raw:: mediawiki

   {{SoCProject|year=2010|student=[[User:juhovh|Juho Vähä-Herttua]]|mentor=[[User:Ilkka Ollakka|Ilkka Ollakka]]}}

ASF and other demuxer support
=============================

Abstract
--------

I was selected to do a project related to ASF and Matroska demuxers, but since there's some overlap related to Matroska, my main goal now is to improve both the ASF demuxer and muxer as much as I can and then find another similar project to work on the rest of the time. It's worth to note that the timeline on this website is just a suggestion, and it's no problem to work on small independent patches during the time as well. I like to do things well on the first try, that's why the schedule is not made too tight.

Information
-----------

I'm a student at Aalto University School of Science and Technology and I hope this is my final year here. I've been a student since 2003 and plan to graduate during summer 2010. Partly because of all this I might have some other things to take care of until the end of June. The plan is to work full time on this project from July to August however. I have a `personal website <http://juho.vähä-herttua.fi/>`__ that I made some years ago, it has most of the useful information about myself.

Timeline
--------

**Updated timeline can be seen in Week 7**

==================== ================= ===================================================================================
Date                 Period            Description
==================== ================= ===================================================================================
April 26 - May 24    Community bonding Getting more familiar with the VLC code base, some small fixes.
May 24 - May 30      Week 1            Review all the existing code, map out needed features.
May 31 - June 6      Week 2            Start cleaning up the demuxer code, go through existing related bugs.
June 7 - June 13     Week 3            Write a working VLC demuxer plugin with a clear API.
June 14 - June 20    Week 4            Work on an API to combine the demuxing and muxing code together.
June 21 - June 27    Week 5            Finish and review the muxing code, write some test cases.
June 28 - July 4     Week 6            Write a working VLC muxer plugin using the rewritten muxer.
July 5 - July 11     Week 7            Extra cleaning up period, because there's always something that slips the deadline.
July 12 - July 18    Week 8            (small extra project, to be discussed with mentors)
July 19 - July 25    Week 9            (small extra project, to be discussed with mentors)
July 26 - August 1   Week 10           Start finishing up (write test suites, run code with valgrind).
August 2 - August 8  Week 11           Continue finishing up.
August 9 - August 15 Week 12           Finish up and do any final testing.
==================== ================= ===================================================================================

Produced code
-------------

For convenience everything is hosted in my personal `github repository <http://github.com/juhovh/vlc>`__. There are at least three branches available, plus possibly some extra branches depending on the need. The meaning of the branches is as follows:

| `master <http://github.com/juhovh/vlc>`__ - Follows the VLC master in git://git.videolan.org/vlc.git plus patches
| `vlc-1.1 <http://github.com/juhovh/vlc/tree/vlc-1.1>`__ - Follows the VLC 1.1 in git://git.videolan.org/vlc/vlc-1.1.git plus patches
| `libasf <http://github.com/juhovh/vlc/tree/libasf>`__ - Branched from VLC 1.1 for now because it's more stable, will contain experimental ASF code

The new code will first enter the *libasf* branch and when it's stable enough I will port it for the 1.2 version and push to *master*. The main idea is to have only that kind of code that can be merged to upstream is in *master* and *vlc-1.1* branches. The *vlc-1.1* branch is mainly for patching possible small issues that come up in VLC 1.1 or backporting changes from *master* when appropriate.

Weekly progress
---------------

**Week 1**

The ASF demuxer codebase is pretty clean and straightforward, except for the patches that add DVR-MS, they are not so clearly described but can be seen easily in commit `308d7c4354df86074583e4635cde5cfbb705e00c <http://git.videolan.org/?p=vlc/vlc-1.1.git;a=commitdiff;h=308d7c4354df86074583e4635cde5cfbb705e00c;hp=9cd8ee7b4ee1f29fc1c0d584be813b4130492246>`__. There's things like "64 bytes we don't know much about" that should be cleared out. The DEMUX_SET_TIME falls back to the SeekPercent which should be improved so that it would seek to video keyframes. Right now seeking in files without index often result in garbage on the screen for a while. There's comments like "/\* FIXME I have to do that for some file, I don't known why \*/" where I have some kind of idea why it has to be done for some file, these should be commented and cleared up.

The ASF muxer has very limited capabilities of editing the metadata of generated ASF file. Only the basic metadata set "title, author, copyright, comment, rating" can be modified, plus two additional options "packet-size" and "bitrate-override". The header serialization is done by writing the headers statically byte by byte. It would make sense to use the ASF header structs already used in the ASF demuxer and serialize those to the output for more flexibility. The muxer also seems to create an index object in the end of the stream, but the index object doesn't seem to contain any index entries. If the index is really to be used, it should create a proper seeking index at least.

**Week 2**

No work done because busy with master's thesis and graduation. Some questions discussed with mentors through email though.

**Week 3**

Committed an initial asf plugin with libasf, noticed that the libasf interfaces are still not quite flexible enough when it comes to the header values required to maintain compatibility with earlier asf demuxer. Since the header handling needs to be redone anyway to support muxing, it's now the plan to first skip to implementing a header structure that's easy to parse/serialize and base the new asf plugin on that. Basically this means switching weeks 3 and 4 in the plan.

**Week 4**

Note to self about compiling qt4 on Mac OSX. Make a 32-bit build and:

| export CC=/Developer/usr/bin/llvm-gcc-4.2
| export CXX=/Developer/usr/bin/llvm-g++-4.2
| export OBJC=/Developer/usr/bin/llvm-gcc-4.2
| export QT4_CFLAGS="-DQT_GUI_LIB -DQT_CORE_LIB -DQT_SHARED -I/usr/local/Qt4.6/mkspecs/macx-g++ -I. -I/Library/Frameworks/QtCore.framework/Versions/4/Headers -I/usr/include/QtCore -I/Library/Frameworks/QtGui.framework/Versions/4/Headers -I/usr/include/QtGui -I/usr/include -F/Library/Frameworks"
| export QT4_LIBS="-F/Library/Frameworks -L/Library/Frameworks -framework QtGui -framework QtCore"
| ../configure --enable-debug --enable-qt4 --disable-macosx --disable-nls

There's many problems with the build, but audio plays ok.

**Week 5**

Made a list of all known ASF objects in a header file http://www.vaha-herttua.fi/public/object.h.txt, most of the week went spending Finnish midsummer though....

**Week 6**

Started with an attempt to merge the VLC's ASF code into libasf http://code.google.com/p/libasf/ that I've used elsewhere. This was largely a wasted effort though, since the libasf.c in VLC is a \_huge\_ piece of code and rewriting that by hand is not sensible. It should be either run through some regexps or not done at all, I think it makes more sense to port the changes from libasf to VLC instead, which would make more sense.

What wasn't so much wasted effort was the reviewing of the VLC's ASF code though, and I merged two small changes to my VLC 1.1 tree, they can be applied to 1.2 tree instead since they're not \_really\_ broken. (doesn't effect much anything)

http://github.com/juhovh/vlc/commit/b6d1d41acea310b84f3661166aacac5c27579eb6 http://github.com/juhovh/vlc/commit/40926045f54f72d4c1c73a70106066339efab832

And I might need some consulting in the Mac OS X video_output module later, since the Qt4 port is mainly stuck on that. When playing everything seems to work correctly, but there's no video shown. If that could be fixed then porting the old Mac OS X interface to 1.2 wouldn't be a problem either. But my only computer's (Mac laptop) keyboard just broke and I have to take it to the service. I hope they fix it fast, in the meantime I'll try to use school computers...

**Week 7**

From Tuesday to Sunday I was practically without a computer. During Monday I went through the old Mac OS X interface code a little bit, commits in `repository <http://github.com/juhovh/vlc/commits/macosx>`__. But j-b probably cleaned up the code a bit better in his patches that also included the voutgl.m that I simply removed. If I can get my laptop back I should merge j-b's patches as well to see if it could be used.

==================== ======= =====================================================================================================================================================================================================================================
Date                 Period  Description
==================== ======= =====================================================================================================================================================================================================================================
July 12 - July 18    Week 8  Merge new ASF object definitions to VLC, test QMacCocoaViewContainer
July 19 - July 25    Week 9  Add handling of mutual exclusions to ASF code to fix `bug 3796 <http://trac.videolan.org/vlc/ticket/3796>`__.
July 26 - August 1   Week 10 Find out how the language support could be added to mms as reported in `bug 3797 <http://trac.videolan.org/vlc/ticket/3797>`__, see if the libasf.\* files from asf lugin could be used in the mms plugin to remove code duplication.
August 2 - August 8  Week 11 Start finishing up, make sure that the patches are ok.
August 9 - August 15 Week 12 Finish up and do any final testing.
==================== ======= =====================================================================================================================================================================================================================================

**Week 8**

Still haven't got my computer out of the service, but my school was nice enough to provide me with my own computer for now, because it's quiet there during the summer. I went through the bugs #3796 and #3797 and sent the ASF patches I had to the mailing list. The suggested fix for #3796 was not accepted, but after looking through the code I have an idea how it could be fixed now without breaking anything else.

The bug #3797 is a bit more difficult, because to be able to select a language on the mms plugin I would need to get information to either ASF plugin or MMS plugin about the elementary stream that is selected or unselected. All I found was INPUT_EVENT_ES event, but that's apparently used for interfaces and not so much for the plugins... Is there a way I could get information about the selected streams to the ASF plugin for example?

**Week 9**

Probably my most productive week so far, got most of the Mac OS X related Qt4 interface patches upstream with only one major patch remaining. I'll be doing cosmetic changes and interface bug fixes in the qt4-macosx branch for now, and will probably collect several patches together and send them to review and discussion next week. I think after getting the fullscreen to work properly I can at least personally take the Qt4 interface as my main VLC interface on Mac. Other than being ugly it doesn't have any major issues.

**Week 10**

A lot of time this week went into debugging Qt4 dialogs, but later I found most of the problems were related into me having a buggy Qt 4.7 binary installed on my computer. The time didn't go to waste though, since I got to study the code quite thoroughly. I also got all the patches prepared last week to upstream, which means that the master of VLC is now pretty usable on Mac with the Qt4 interface. I also have some patches in queue that are not merged yet, mainly support for double-clicking video files on Mac and fixes in the menu issues. There are still some things with the Mac OS X Qt4 interface that have quite high priority:

| 1) Fixing the crash if libvlc_Quit is called during video playback
| 2) Full screen video support in video_output macosx module
| 3) Resize support in video_out macosx module
| 4) Always on top support in video_out macosx module
| 5) Testing a distributable VLC.app that includes the Qt4 binaries
| After these changes I believe I can start using Qt4 interface as my main VLC interface on Mac. Hopefully this will make it possible to get rid of the old Mac OS X interface and give Mac OS X developers more time to work on Lunettes, since Lunettes surely has its own target group that won't be satisfied with Qt4 interface.

**Week 11**

Commands I used to add QtCore and QtGui frameworks into the VLC-release.app:

| export CC=/Developer/usr/bin/llvm-gcc-4.2
| export CXX=/Developer/usr/bin/llvm-g++-4.2
| export OBJC=/Developer/usr/bin/llvm-gcc-4.2
| export QT4_CFLAGS="-I/Library/Frameworks/QtCore.framework/Versions/4/Headers -I/Library/Frameworks/QtGui.framework/Versions/4/Headers"
| export QT4_LIBS="-framework QtGui -framework QtCore"
| ../configure --enable-debug --enable-qt4 --disable-macosx --disable-nls
| make
| make VLC-release.app
| cp -R /Library/Frameworks/QtCore.framework VLC-release.app/Contents/Frameworks
| cp -R /Library/Frameworks/QtGui.framework VLC-release.app/Contents/Frameworks
| install_name_tool -id @executable_path/../Frameworks/QtCore.framework/Versions/4/QtCore VLC-release.app/Contents/Frameworks/QtCore.framework/Versions/4/QtCore
| install_name_tool -id @executable_path/../Frameworks/QtGui.framework/Versions/4/QtGui VLC-release.app/Contents/Frameworks/QtGui.framework/Versions/4/QtGui
| install_name_tool -change QtCore.framework/Versions/4/QtCore @executable_path/../Frameworks/QtCore.framework/Versions/4/QtCore VLC-release.app/Contents/MacOS/plugins/libqt4_plugin.dylib
| install_name_tool -change QtGui.framework/Versions/4/QtGui @executable_path/../Frameworks/QtGui.framework/Versions/4/QtGui VLC-release.app/Contents/MacOS/plugins/libqt4_plugin.dylib
| install_name_tool -change QtCore.framework/Versions/4/QtCore @executable_path/../Frameworks/QtCore.framework/Versions/4/QtCore VLC-release.app/Contents/Frameworks/QtGui.framework/Versions/4/QtGui
| echo "[Paths]" > VLC-release.app/Contents/Resources/qt.conf
