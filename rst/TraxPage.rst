NOTE: I mostly focussed on QT4 so if there's an issue it doesn't
necessarily mean it isn't a problem in WX either..

== Remaining issues == 10, 12, 13, 14, 23?, 25?, 28, 30, 31, 32, 34, 35,
36, 37, 38, 40, 41, 45

== nightly win32-20070831 ==

1 WX/QT4 (in trac): play file, open playlist, '''CRASH''' \**\*
http://trac.videolan.org/vlc/ticket/1344 \* rumoured to be fixed in svn
already [[User:TraxTrax]]

   Starting program: /home/User/daily/vlc-0.9.0-svn-21875-debug/vlc.exe
   -I wx

   Program received signal SIGSEGV, Segmentation fault. [Switching to
   thread 2776.0x8a8] 0x77c478c0 in strlen () from
   /cygdrive/c/WINDOWS/system32/msvcrt.dll (gdb) bt #0 0x77c478c0 in
   strlen () from /cygdrive/c/WINDOWS/system32/msvcrt.dll #1 0x691c2103
   in TextPrint (p_msg=0x3e8320, p_file=0x77c5fce0) at logger.c:393 #2
   0x691c1f28 in FlushQueue (p_sub=0xbcaa40, p_file=0x77c5fce0,
   i_mode=0) at logger.c:377 #3 0x691c1e49 in Run (p_intf=0xa51348) at
   logger.c:337 #4 0x70317339 in RunInterface () from
   /home/User/daily/vlc-0.9.0-svn-21875-debug/libvlc.dll #5 0x77c3a3b0
   in msvcrt!_endthreadex () from
   /cygdrive/c/WINDOWS/system32/msvcrt.dll #6 0x00a51348 in ?? () #7
   0x00000000 in ?? () from

As for QT4, normal discovery is fine but if you first open file, then
shoutcast TV discovery and click on item

   Starting program: /home/User/daily/vlc-0.9.0-svn-21875-debug/vlc.exe

   Program received signal SIGSEGV, Segmentation fault. [Switching to
   thread 2084.0x1e8] ---Type <return> to continue, or q <return> to
   quit---0x70321655 in \__vlc_mutex_lock () from
   /home/User/daily/vlc-0.9.0-svn-21875-debug/libvlc.dll (gdb) bt #0
   0x70321655 in \__vlc_mutex_lock () from
   /home/User/daily/vlc-0.9.0-svn-21875-debug/libvlc.dll #1 0x7032139f
   in input_item_subitem_added () from
   /home/User/daily/vlc-0.9.0-svn-21875-debug/libvlc.dll #2 0x7038b075
   in vlc_event_send () from
   /home/User/daily/vlc-0.9.0-svn-21875-debug/libvlc.dll #3 0x70244a01
   in input_ItemAddSubItem (p_parent=0x4c23640, p_child=0x7d077e0) at
   ../../../include/vlc_input.h:160 #4 0x702446a7 in Demux
   (p_demux=0x4c1cc68) at pls.c:164 #5 0x70334c48 in MainLoop () from
   /home/User/daily/vlc-0.9.0-svn-21875-debug/libvlc.dll #6 0x7033474a
   in Run () from /home/User/daily/vlc-0.9.0-svn-21875-debug/libvlc.dll
   #7 0x77c3a3b0 in msvcrt!_endthreadex () from
   /cygdrive/c/WINDOWS/system32/msvcrt.dll #8 0x04bd89e8 in ?? () #9
   0x04b7b0e0 in ?? () #10 0x003e0000 in ?? () #11 0x04cbe700 in ?? ()
   #12 0x00000000 in ?? () from

2 QT4 (fixed): mkv crash (regression, works in WX) \* Sample ?
[[User:J-bjb]] 16:57, 8 September 2007 (CEST)

3 QT4 (fixed): play file, deinterlace, enable, resizes video to 10x10
pixels! deinterlace disable same effect workaround: disable/enable video
track \* should be fixed on win32 [[User:Funmanfunman]]

4 QT4/WX (fixed): play button, doesn't give open dialog anymore \* Works
fine, but we need a way to know which one of "media
library"/"playlist"/"services discovery" is active, and also a way to
get the number of items in one of these "playlists" [[User:FunmanTrax]]

5 QT4: open file, doesn't go where you click. when there is 2 rows and
you click on a 2nd row it will shift the whole view to the left. so if
you doubleclick (which used to select and open) you end up selecting the
wrong file \* Qt4.2 bug under windows. \* WONTFIX

6 QT4/WX (fixed): no longer avi corrupt warning popup \* Ok in 21875
[[User:Trax|Trax]]

7 QT4 (fixed): slider doesn't go where you click anymore, regression
(does work in WX) \* fixed by ssbssa [[User:Funman|funman]]

8 QT4 (duplicate of issue 1): shoutcast TV, changing channels often
segfaults \* might be related to issue 1 [[User:Traxfunman]]

9 QT4 (wontfix): extended prefs, various modules not found (erase, marq,
logo etc.) \* ok on linux [[User:FunmanTrax]] \* no, there are not in
the same category, that is it. [[User:J-b|jb]]

10 QT4: wrong win32 slash, / instead of in filename \* TO BE TRAC-ed
with details [[User:J-b|jb]] 08:23, 26 October 2007 (CEST)

11 QT4: shows popup filename in taskbar while wx doesn't \* just means
wx sucks [[User:Funman|funman]]

12 QT4: shows full filename in titlebar instead of just the filename,
video only \* ok on linux [[User:Funmanjb]] 08:23, 26 October 2007
(CEST)

13 QT4: shows full filename on vout osd instead of just the filename \*
ok on linux [[User:Funmanjb]] 08:23, 26 October 2007 (CEST)

14 QT4 (merged to trac): assertion '''CRASH''' in playlist_model.cpp:
add sap or podcast, select, remove also will not remove audio or TV

15 QT4 (fixed): open network: \*\* https will not appear in customize
\*\* rtsp cannot enter address \*\* udp/rtp (unicast) can enter address
but doesn't appear in customize \* Done and fixed [[User:J-b|jb]] 12:27,
8 September 2007 (CEST)

16 QT4 (fixed): assertion '''CRASH''' on open directory: playlist/tree.c
line 191 \* fixed, not using PLAYLIST_GO anymore, so the added directory
won't start playing [[User:Funman|funman]]

17 QT4 (implemented): Filter "video files" doesnt include .gxf and .mxf

18 QT4: dock playlist, doesn't seem to work properly when showing
videos, too small undock and replay a clip and '''CRASH''' (because the
size is small?) \* Won't fix until QDockWidget

19 QT4 (fixed): would be nice to have the speaker icon have a mute
version with a cross in it \* fixed [[User:Funman|funman]]

20 QT4 (fixed): the numerical value for slower/faster isn't updated \*
Done [[User:J-b|jb]] 15:48, 8 September 2007 (CEST)

21 QT4 (not reproducable): play file, open playlist, doubleclick the
file you are playing, '''CRASH''' as sertion failed: playlist_model.cpp
line 495, expression index.isValid() or does this only happen when
adding telnet interface in the mean time!? \* no longer an issue since
svn 22584 or nightly 20070813 [[User:Trax|Trax]]

22 QT4 (fixed): play button is now also pause button but has no pause
icon yet \* done [[User:J-b|jb]] 12:43, 8 September 2007 (CEST)

23 QT4: cannot play files with underscores (this is in cygwin)

24 QT4 (fixed): S button for taking snapshots doesn't work, nor does F
for fullscreen \* F does work [[User:J-bjb]] 16:12, 8 September 2007
(CEST) \* S is ok but F does not work in 21875 win32 [[User:Traxfunman]]
\* confirmed to work in 22822 win32 [[User:Trax|Trax]]

25 QT4 (unknown): rightclick in video doesn't open menu immediately,
needs a "first" click this works counterintuitive, especially if you
after that doubleclick for fullscreen (which needs another click then)
\* Not reproducable in 21952, might be related to other problem
[[User:Trax|Trax]]

26 QT4: option to unhide menus works quite well, how do I unhide easily?
suggestion, rightclick on video, tools, make a hide menu toggle (but
this won't work if there is no vout active) \* Partly done. Not optimal
but this would be enough though [[User:J-b|jb]] 19:25, 8 September 2007
(CEST)

27 QT4 (fixed): in win32 it seems the main window isn't resized properly
initially the bottom line icons (forward, stop etc.) are half their
usual height, dragging the resize slider bottom right a bit makes it
"normal" again after clip is played it "resets" to the wrong height
again in initial mode \* fixed by ssbssa [[User:Funman|funman]] 03:38, 8
September 2007 (CEST)

28 QT4 (fixed): file, open, this will give a default folder

   C:documents and settingsuserapplication data note that there are no
   capitals while there should be (what is manipulating this?) in WX the
   last used folder is remembered, in QT4 not

-  This has been changed after my XDG Base Directory Specification
   commit. (It should at least default to a "normal" user directory, not
   app data). Not sure if that was the issue you were mentioning though.
   [[User:Dionoea|Dionoea]]
-  Yes that was my problem [[User:Trax|Trax]]

29 QT4: file open, when browsing there is always debug msgs:

   intersectingStaticSet: row 10 was invalid

-  QT4.2 bug under windows

30 QT4: when files are opened with weird characters in filename or path
like

   I:&#2892;file_1.avi it will be misidentified as having subtitles and
   spam: freetype warning: unbreakable string does not happen in WX

-  linux ok [[User:Funman|funman]]

31 QT4/WX: in cygwin gdb it's impossible to open files, gives weird
filename could not open spam; drag and drop does work

32 QT4/WX: start audio stream, open visualisation goom, disable goom,
will not destroy the goom vout

33 QT4/WX (fixed): goto time function doesn't reset timing counter.
example clip is at 0:52/4:10 goto 0:10 with function and counter stays
at 0:52/4:10 until the played clip exceeds 52 sec. then it continues to
count \* Done. [[User:J-b|jb]] 12:58, 8 September 2007 (CEST)

34 QT4/WX: generic performance issue. a simple thing like opening
internet explorer with blank page will interfere with VLC cause
audio/video hickups when something is playing. regression but
--high-prio "fixes" it \* make high-prio default ? [[User:FunmanTrax]]

35 QT4/WX: play clip, turn on wallpaper, turn on deinterlace, wallpaper
disappears from menu

== svn 21737 ==

36 QT4 (not reproducable 20070813): shoutcast TV discovery, click on the
1st discovered item, '''CRASH''' on playlist_nodedump \* duplicate
issue? [[User:TraxTrax]]

37 QT4: show more options in open dialogue. it's perhaps usable to always have this enabled?
   makes it easier to copy/paste links in VLC and you can see what some
   options do if you toggle them (timeshift etc.)

-  i don't agree, but we could have a setting to have it always enabled
   (i.e. not by default) [[User:Funman|funman]]

38 QT4/WX: opening a shoutcast playlist will not autostart the 1st item

39 QT4: (partially fixed) extended settings, add text, enable, disable
(VLC marq still remains!), enable, '''CRASH''' \* fixed (marq still
remains anyway :/) [[User:Funman|funman]]

40 QT4: extended settings, add logo, '''CRASH''' \* qt4 threads related
[[User:Funman|funman]]

41 QT4: file, open file. blank icons for files (no icons for registered
filetypes)

42 QT4 (fixed): [00000642] main interface error: option errors-dialog
does not exist \* done in rev 21869. [[User:J-b|jb]] 16:54, 8 September
2007 (CEST)

43 QT4 (fixed): menu inconsistencies. main menu has interfaces as part
of tools while right click menu in vout has interfaces as seperate
option \* done in rev 21879 [[User:J-b|jb]] 19:25, 8 September 2007
(CEST)

44 QT4 (fixed): extended prefs doesn't have Close, OK or Cancel button.
feels unnatural to close the prefs with the X top right. Use same Save,
Cancel, Reset ext. prefs like the normal prefs menu has? \* done in rev
21890 [[User:J-b|jb]] 03:30, 9 September 2007 (CEST)

45 QT4: equalizer status isn't updated everywhere (already in trac?)
when changing from main menu the status in extended prefs isn't updated
accordingly and vice versa.the function is ok it's only the selection
that isn't updated. why bother with 2 locations? doesn't extended prefs
suffice or is main menu intended as "quick" setting?

== svn 21817 ==

46 QT4: cosmetics. extended prefs.. using wall or clone filter it's not
possible to set the amount of clone or wall rows before hand because
it's greyed out so you always have to use the defaults first, enable the
option then set the appropriate amount. \* Yes. This is a normal
behaviour, way easier to code. [[User:J-bDionoea]]

47 QT4: start vlc, open playlist, dock playlist:
   33201 1 QPaintDevice: Cannot destroy paint device that is being
   painted. Be sure to QPainter::end() painters!

48 QT4 (fixed): cosmetics. media information stats. imho the order looks
nicer to have Video, Audio, Input, Streaming and also have the main
window be just as big as all the expanded settings (same for Codec
information) \* Done [[User:J-b|jb]] 13:08, 8 September 2007 (CEST)

49 QT4: open disc, disk device is not selectable (nothing to select,
stays empty) and browse button is not functional yet. does work when I
just manually type in my DVD drive as D: \* Partially fixed, disk is
selectable but browse doesn't work 20071018 nightly [[User:Trax|Trax]]

50 QT4: cosmetics. language selection in interfaces is not sorted
alphabetically \* No idea how to do that [[User:J-bDionoea]]

51 QT4: cosmetics. Tools, Codec information and Media information, to
have both seems a bit redundant (they both open the Codec information
tab). Why not drop Codec information from the menu but keep the CTRL+I
as Media information as I stands for information :) \* Because this is
the most asked question in support: "What is the codec" [[User:J-b|jb]]
13:02, 8 September 2007 (CEST)

52 QT4: cosmetics: Tools, Codec information, Codec Details, why bother
showing empty fields (i.e. Language is often not used) \* Because noones
wants the same things. Won't fix [[User:J-b|jb]] 13:01, 8 September 2007
(CEST)

53 QT4: cosmetics. overall view of QT4 is quite huge compared to WX and even other players (this sample doesn't even have the extra buttons)
   http://www.firstmiletv.nl/vlc/problems/qt4/windowsize.jpg the
   play/stop etc. buttons in tray icon menu are already a lot smaller,
   are they usable?

54 QT4: cosmetics. the title section of the clip on the bottom does not
have a 3d "feel" as if it's embedded, the same way the speed and
time/duration section is.

55 QT4: cosmetics. personally I'd like the title section on the right
and the time/speed on the left as it is with WX. this because those
sections are rather fixed and "look" better at the left starting side.

56 QT4: cosmetics. as the slider bar is already quite large, why not
have the time/duration section on the left or right side on the same
height. this leaves more room for (often) long title info.

57 QT4: cosmetics and nice to have. magnetic menus for debug, ext. prefs
etc. they open all over the place :)

58 QT4: always shows time slider, even for livestreams (i.e. shoutcast)

[[Category:Dev Discussions]]
