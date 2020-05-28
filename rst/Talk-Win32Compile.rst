Nice how to :) I'm not sure that we really need two different howto for
compiling VLC for win32 though. Trax's cygwin compile howto on
http://developers.videolan.org/vlc/ already covers lots of stuff. So you
might want to merge both (ask trax fist, you can find him on #videolan
on Freenode) -- [[User:Dionoea|Dionoea]] 15:13, 24 June 2006 (CEST)

The binary contribs that exist on the page as of now are out of date.
Asking around, updated packages can be found at
http://people.videolan.org/~jb/Contribs/ . Updated binary Qt libraries
can be had at
http://download.videolan.org/pub/testing/contrib/qt4-4.4.1-win32-bin.tar.bz2
tar -C / -jxvf /path/to/contribs.tar.bz2 && tar -C /usr/win32 --strip 1
/path/to/qt-bin.tar.bz2 [[User:Keithel|Keithel]] 23:18, 7 October 2008
(CEST)

From comments from j-b, it's best to use the 20080811 contribs at the
moment, as the ffmpeg build is bad in it. To get beyond the qjpeg
linkage problem, after configure has been run, hack the vlc-config
script to add it to the qt4 libs section. Then there will be a failure
in the gnutls plugin linking, -- gpg-error lib missing.
[[User:Keithel|Keithel]] 19:19, 8 October 2008 (CEST)

Final fixes to make cross-compile all working using 0811 contribs +
qt4-4.4.1 package: Apply contribs as in my above comments. Modify
Makefile.am in root, changing ACLOCAL_AMFLAGS to -I m4 -I
/usr/win32/share/aclocal . run the bootstrap - ./bootstrap. Then pass
--with-libgcrypt-prefix=$CONTRIBS to configure in addition to params
supplied in this article. Once configure is done, modify vlc-config ,
search for qt4 section and -lQtCore. Put -lqjpeg after it. Now run
'make' and everything should build properly. [[User:Keithel|Keithel]]
01:43, 9 October 2008 (CEST)
