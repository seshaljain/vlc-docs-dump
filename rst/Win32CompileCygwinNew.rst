This is a new version of the Win32CompileCygwin written by
[[User:J-b|Jean-Baptiste Kempf]]

'''This version ONLY works for 0.9.x, for 1.0.x and for 1.1.x.'''

'''WARNING''': building VLC on Cygwin has ever been a failure-prone
task. It is also very slow (specially if you enable debug and
optimizations). If you want to build on windows, [[Win32CompileMSYSNew]]
is a much better option. Otherwise, you should strongly consider
cross-compiling from Linux (on a virtual machine, via dual-boot or from
another computer, see [[Win32Compile]]). You were warned.

=Introduction=

This is a guide for Windows users with a step-by-step instruction to
download, install, configure and build your VLC.

This guide uses [http://www.cygwin.com '''Cygwin'''] a Linux-like
environment for Windows used for compilation of the VLC source code.

Start off by creating a VLC and a download folder on your hard drive
where you can put all the installation files:

   C:VLCC:VLCDownloads

For further reference, the assumption is made that the local user will
be 'Administrator'.

=Cygwin=

Download the latest [http://www.cygwin.com/cygwin/setup.exe Cygwin
setup] and save it in your download location:

   C:VLCDownloads

More info about Cygwin can be found at http://www.cygwin.com or
http://sourceware.org/cygwin

==Selecting Cygwin packages to install==

Run the setup program with the following options:

Installation type : Install from Internet (default)

Root directory : C:cygwin (default)

Local Package directory : C:VLCDownloadscygwin (your download location)

Internet Connection : Direct Connection (preferred, if it fails try
another)

Download Site : Choose a download site closest to you (FTP preferred)

At the "Select Packages" section of the installation process you can
select packages by clicking the button with the rotating 2 arrows. (This
is under the "New" section). It shows "Skip" next to the button if the
package isn't selected yet.

Clicking the button a few times will rotate through the possible package
versions including "Skip" (meaning do not install or remove if
installed) and "Keep" (meaning keep using the current installed
version). If a package was already installed it will also show the
"Current" version just to the left of it.

Select the following packages (some others will automatically be
selected as well):

   Archive
      unzip zip

   Devel
      autoconf automake binutils cvs (optional: for building
      extras/contrib) gcc gcc-core gcc-g++ gcc-mingw gcc-mingw-core
      gcc-mingw-g++ gdb gettext gettext-devel git libgcrypt-devel
      libiconv libtool make mingw-runtime nasm patchutils pkg-config
      subversion (optional: for building extras/contrib)

   Editor
      vim

   Libs
      expat libgcrypt

   Utils
      ncurses

   Web
      curl (optional: for building extras/contrib) wget (optional: for
      building extras/contrib)

==Cygwin environment==

Start Cygwin from the icon on your desktop (With Windows Vista run it
with admin rights, so right click and select "Run as administrator"). If
it runs for the first time it will automatically create a home"username"
folder in the Cygwin environment; user being the currently logged on
Windows user. Assuming this is the 'Administrator' user it will create
the following folder:

   C:cygwinhomeAdministrator (example)

NOTE: On your desktop, you can rightclick the Cygwin icon and (in the
Options field of the Cygwin Properties) set the Command history Buffer
size to as large as possible: 999. This setting will make it possible to
scroll back further in the Cygwin environment.

=VLC source code=

== Git == The very latest VLC source code can be obtained through a tool
called [[Git]]. The Cygwin package we're about to install comes with an
internal git component.

   cd /cygdrive/c/VLC/

   git clone git://git.videolan.org/vlc.git

or if you just want to download latest VLC revision (saves bandwidth)

   git clone git://git.videolan.org/vlc.git --depth 1

or if your proxy denies git protocol connections use:

   git clone http://git.videolan.org/git/vlc.git

In this case you need to set the proxy address first:

   export http_proxy = <proxy>:<port>

If git fails for some reason, then please try to use git from basic
Windows command prompt (Start -> Run -> cmd), not from Cygwin shell.

Please note that the very latest VLC sources ("master" branch) does not
necessary build fine all the time. So if you need something stable,
better is to use a git tag or a version snapshot archive.

== Snapshots ==

You can do the same by using the snapshots in the
[http://nightlies.videolan.org/ nightly builds] site.

== Specific Version ==

You can get a specific version of VLC source code from the
[http://download.videolan.org/pub/videolan/vlc/ source ftp] directory.

Another option is to sync specific version represented by a tag in git:

   git checkout <version>

where <version> is one like: 1.0.1, 1.0.2, ..

=Bootstrap= First move to vlc folder, if you aren't already there

   cd vlc

and then run bootstrap.

dos2unix botstrap
   ./bootstrap

You should go through dos2unix for every script which produces errors
related to 'r'

It might fail with some '''unable to remap error
<some_dll_file_name>'''. It seems you need to rebase all Cygwin DLLs:
close all your cygwin applications and launch 'ash' from basic windows
command prompt (Start -> Run -> cmd), from there run rebaseall (so start
e.g. C:cygwinbinash.exe and type there text below).

   /bin/rebaseall -v

= External libraries to the source code=

VLC depends on other libraries (code) to provide some features like AC3
audio or MPEG-4 video encoding/decoding etc.

Depending on your needs you will have to install and compile some or all
of these external libraries.

== Get the Win32 "contrib" package ==

A package with most of these libraries already compiled so it's actually
really easy to compile a full-featured version of vlc can be found here:

http://download.videolan.org/pub/testing/win32/ or
http://people.videolan.org/~jb/Contribs/ or take
ftp://ftp.videolan.org/pub/vlc/1.0.0/win32/contrib-1.0.0.tar.bz2

Download the latest version of a "contrib" package for win32:

   contrib-20080702-win32-bin-gcc-4.2.1-sjlj-runtime-3.13-only.tar.bz2
   (this is an '''example''' so '''DON'T''' download packages this old,
   unless you really have to!)

It's a good idea to check the INSTALL.Win32 file in the VLC source
directory for the appropriate contrib download file if you build older
VLC versions.

Save it into your download location:

   C:VLCDownloads

==Installing the Win32 "contrib" package in Cygwin==

Start Cygwin and enter the following command in your shell:

   rm -rf /usr/win32 cd /cygdrive/c/VLC/Downloads tar xf
   contrib-20080702-win32-bin-gcc-4.2.1-sjlj-runtime-3.13-only.tar.bz2
   -C /

Replace with your version of the "contrib" file and DON'T FORGET THE /
(slash) at the end.

This will extract the contents of the file into usr/win32 folder within
your Cygwin environment.

NOTE: Make sure to DELETE your old version (/usr/win32 folder) instead
of extracting a new version on top of it.

Version 1.0.2 of VLC source code has been tested and found working with
contrib-20091020-win32-bin-gcc-4.2.1-sjlj-runtime-3.15.2-only.tar.bz2

==Keeping the Win32 "contrib" package up-to-date==

For maintenance purposes periodically check:

http://download.videolan.org/pub/testing/win32/

==Qt4 issues== There are some Qt4 and winapi issues (like
'''InterlockedCompareExchange''' error) which you can work out with
information you get from
http://forum.videolan.org/viewtopic.php?f=14&t=50360&p=164758&hilit=win32api#p164219
and http://forum.videolan.org/viewtopic.php?f=14&p=175301#p175301
threads. If you don't plan to compile Qt4 or skins2 interface, you can
skip this.

=Configure=

In order to make our lives just a bit easier the following section
describes what commandline options should be used for compiling and
those commands will then be put into a "script" that can be executed
(rather than having to copy and paste all the time).

==Configure script for compiling VLC==

Create a new text document with the following lines:

   PATH=/usr/win32/bin:$PATH PKG_CONFIG_LIBDIR=/usr/win32/lib/pkgconfig
   CPPFLAGS="-I/usr/win32/include -I/usr/win32/include/ebml"
   LDFLAGS=-L/usr/win32/lib CC="gcc -mno-cygwin" CXX="g++ -mno-cygwin"
   ./configure --host=i686-pc-mingw32 --enable-nls --enable-sdl
   --with-sdl-config-path=/usr/win32/bin --enable-faad --enable-flac
   --enable-theora --enable-live555
   --with-live555-tree=/usr/win32/live.com --enable-caca
   --with-caca-config-path=/usr/win32/bin
   --with-dvdnav-config-path=/usr/win32/bin --enable-goom
   --enable-dvdread --enable-debug --disable-optimizations --disable-mkv
   --disable-taglib --disable-zvbi --disable-dirac --disable-x264
   --disable-fluidsynth

This command is tested and configures VLC 1.0.2 properly so that it
builds fine.

NOTE: The following options are added for debug purposes and makes the
final package a bit larger but the advantage is it's easier to debug in
case of crash reports:

   --disable-optimizations --enable-debug

If you want to report a crash bug to the VLC team, it is necessary that
you provide a stack backtrace. Unfortunately, Windows automatic crash
reporter cannot generate such a backtrace as debug symbols used by GCC
compiler aren't understood by Windows, therefore we suggest that you
install Dr. MinGW
(http://jrfonseca.dyndns.org/projects/gnu-win32/software/drmingw/) which
will extend Windows Just-In-Time Debugger and provide the necessary
debug information.

NOTE: The following options is needed for Qt4 support:

   --enable-qt4

As of version 0.9.0 VLC will include the Qt interface. More information
can be found about QT here: http://www.trolltech.com

The "Win32 contrib package" at present includes the linux and Windows
equivalents of uic, moc and roc executables which are required for
building this interface.

The linuxs executables have to be '''deleted''' from the contrib folder:

   C:cygwinusrwin32binmoc (example) C:cygwinusrwin32binrcc (example)
   C:cygwinusrwin32binuic (example)

Save as filename in your "scripts" folder at your download/install
location:

   configure-vlc.sh

NOTE: Save using "All files" and not "Text files" otherwise Windows
might append the extension .txt

Copy the file into your home directory:

   C:cygwinhomeAdministrator

Start Cygwin and enter the following command in your shell:

   dos2unix configure-vlc.sh

After your configure-vlc.sh is completed, copy it to your vlc directory
and run it:

   ./configure-vlc.sh

If it complains about permissions, use chmod and try again:

   chmod 777 configure-vlc.sh

NOTE. (If you plan to use JVLC) To make vlc-control.dll accessible by
Java on ''Windows'' configure-vlc.sh should be modified to include
"-Wl,--add-stdcal-alias". Example:

   ... CC="gcc -mno-cygwin -Wl,--add-stdcall-alias" CXX="g++ -mno-cygwin
   -Wl,--add-stdcall-alias" ./configure ...

===Mozilla plugin===

If you want to build Mozilla plugin, add this to your configure-vlc.sh

   --enable-mozilla --with-mozilla-sdk-path=/usr/win32/gecko-sdk

If configure-vlc.sh goes correctly, you should see '''plugins/bindings :
activex mozilla'''

===POSIX emulation layer===

VLC can be built with or without the so called POSIX emulation layer.
Without is the default and is usually better (and with hasn't been
tested for quite some time). If you do want to use the emulation layer,
then just leave out the line with the following options:

   CC="gcc -mno-cygwin" CXX="g++ -mno-cygwin"

=Compiling source code=

It's time to start Cygwin again...

==Compiling VLC==

Enter the following commands in your Cygwin shell:

   cd vlc

NOTE: Open /cygdrive/c/VLC/libtool in text editor and if
"global_symbol_pipe =" line is blank, replace it with :

   global_symbol_pipe="sed -n -e 's/^.*[
   ]\([ABCDGIRSTW][ABCDGIRSTW]*\\)[ ][
   ]\ *\\(\)\([_A-Za-z][_A-Za-z0-9]*\\)$/\1\2\3 \\3/p'"

Build it! (remember to run configure-vlc.sh before first build)

   make

Cross your fingers and wait... because it might take few hours before
compilation is done. If you have multicore CPU or multi CPU box, you can
use -j2 switch (or maybe -j3 or -j4 etc.) to speed up make process

   make -j2

==Creating self contained packages==

Once the compilation is done, you can build self-contained VLC packages
with the following "make" commands:

   make package-win32-base

(This will create a subdirectory named vlc-x.x.x with all the binaries
"stripped" without any debugging symbols).

   make package-win32-zip

(Same as above but will package the directory in a zip file).

   make package-win32

(Same as above but will also create an auto-installer package. You will
need to have NSIS installed in its default location for this to work).

-  If you have permissions problems running make package-*, chmod 777 -R
   the vlc folder.
-  If you have permissions problems running vlc.exe after packaging,
   rename or delete vlc.exe.manifest

=Advanced usage=

==Updating Cygwin package versions==

If you need to update or install additional packages you can just run
the Cygwin setup.exe from your download location:

   C:Downloadscygwinsetup.exe (example)

==GDB (Gnu Debugger)==

This section requires that you installed the gdb (Gnu Debugger) in
Cygwin.

This is a typical example of creating a crashlog:

   cd vlc-trunk

   gdb --args vlc.exe --fast-mutex --reset-config --reset-plugins-cache

NOTE: vlc-0.9.0 uses libtool for building sources, if you want to debug
from the source tree, you should type the following command instead:

   libtool --mode=execute gdb --args vlc --reset-config
   --reset-plugins-cache

In the debugger mode run the program and make sure you reset the
preferences!

   (gdb) run

NOTE: the (gdb) is just a prompt which means you are in the debugger
mode, please note that ''--fast-mutex'' option is no longer supported in
vlc-0.9.0

It will now take a lot longer than usual for VLC to start :)

Now operate VLC as you would normally do. As soon as a crash issue
occurs you'll notice a line like this:

   Program received signal SIGSEGV, Segmentation fault. 0x0041394c in
   playlist_ItemGetById (p_playlist=0x19ec4f8, i_id=29) at
   src/playlist/item-ext.c:459 ---Type <return> to continue, or q
   <return> to quit---459 i = i_bottom + ( i_top - i_bottom ) / 2;

Now you can do a "backtrace" by using the bt command:

   (gdb) bt

And output similar to this will be created:

   #0 0x0041394c in playlist_ItemGetById (p_playlist=0x19ec4f8, i_id=29)
      at src/playlist/item-ext.c:459

   #1 0x0b26bbf7 in wxvlc::Playlist::CountItems (this=0x1822e288, root=
      {m_pItem = 0x29fef8}) at playlist.cpp:695

   #2 0x0b26bc83 in wxvlc::Playlist::CountItems (this=0x1822e288, root=
      {m_pItem = 0x29e8b0}) at playlist.cpp:689

   #3 0x0b26bc83 in wxvlc::Playlist::CountItems (this=0x1822e288, root=
      {m_pItem = 0x29a818}) at playlist.cpp:689

   #4 0x0b26bc83 in wxvlc::Playlist::CountItems (this=0x1822e288, root=
      {m_pItem = 0x299718}) at playlist.cpp:689

   #5 0x0b26bc83 in wxvlc::Playlist::CountItems (this=0x1822e288, root=
      {m_pItem = 0xffff0000}) at playlist.cpp:689

   #6 0x0b26bf49 in wxvlc::Playlist::AppendItem (this=0x1822e288,
      event=@0x1827afd0) at playlist.cpp:564

   #7 0x0b2757fc in wxvlc::Playlist::OnPlaylistEvent (this=0x1822e288,
      event=@0x1827afd0) at playlist.cpp:1438

   #8 0x0b3771b8 in wxEvtHandler::ProcessEventIfMatches ()
      at /usr/win32/include/wx-2.6/wx/event.h:2183

   #9 0x0b376a1c in wxEventHashTable::HandleEvent ()
      at /usr/win32/include/wx-2.6/wx/event.h:2183

   #10 0x0b37730d in wxEvtHandler::ProcessEvent ()
      at /usr/win32/include/wx-2.6/wx/event.h:2183

   #11 0x0b37711b in wxEvtHandler::ProcessPendingEvents ()
      at /usr/win32/include/wx-2.6/wx/event.h:2183

   ---Type <return> to continue, or q <return> to quit---#12 0x0b376017 in wxAppConsole::ProcessPendingEvents ()
      at /usr/win32/include/wx-2.6/wx/event.h:2183

   #13 0x0b3ec75a in wxIdleWakeUpModule::MsgHookProc ()
      at /usr/win32/include/wx-2.6/wx/bmpbuttn.h:81

   #14 0x773aca2d in USER32!GetScrollRange ()
      from /cygdrive/c/WINDOWS/system32/user32.dll

   #15 0x00000000 in ?? () from (gdb)

To backtrace all the running threads use:

   (gdb) thread apply all bt

These are the log outputs that are more usefull to developers than just
mentioning "it crashes"!

NOTE: In GDB mode there are sometimes situations where GDB initially
"crashes" on certain network activity (opening network shares, network
traffic) which in normal operation does not occur. Just select c for
continue until "normal" operation continues.

== Common errors == ===vlc.exe: Permission denied===

A make finished successfully and produced vlc.exe, but running the
executable returns the following:

   bash: ./vlc.exe: Permission denied

The permissions on both vlc.exe & vlc.exe.manifest must be set to
executable.

FIX: Type the following:

   chmod 755 vlc.exe vlc.exe.manifest

===error: parse error before '(' token===

A make (compile) of FFmpeg results in the following error:

   /usr/include/sys/unistd.h:203: error: parse error before '(' token
   make[1]: \**\* [ffm.o] Error 1

It's very likely you are usix the POSIX emulater which you shouldn't...

FIX: compile with the option

   -mno-cygwin

===error: expected primary-expression before '<<' token===

   In file included from
   /usr/lib/gcc/i686-pc-mingw32/3.4.4/../../../../include/w32
   api/windows.h:52, from ../../../include/vlc_common.h:459, from
   ../../../include/vlc/vlc.h:153, from dshow.cpp:31:
   /usr/lib/gcc/i686-pc-mingw32/3.4.4/../../../../include/w32api/wingdi.h:3:1:
   warn ing: this is the location of the previous definition In file
   included from /usr/win32/include/dshow.h:35, from common.h:45, from
   dshow.cpp:35: /usr/win32/include/ddraw.h:14: warning: ignoring
   #pragma warning In file included from /usr/win32/include/dshow.h:35,
   from common.h:45, from dshow.cpp:35: /usr/win32/include/ddraw.h:5552:
   warning: ignoring #pragma warning In file included from
   /usr/win32/include/dshow.h:45, from common.h:45, from dshow.cpp:35:
   /usr/win32/include/strmif.h:2: warning: ignoring #pragma warning In
   file included from /usr/win32/include/dsound.h:13, from
   /usr/win32/include/amaudio.h:18, from /usr/win32/include/dshow.h:47,
   from common.h:45, from dshow.cpp:35:
   /usr/win32/include/d3dtypes.h:22: warning: ignoring #pragma warning
   /usr/win32/include/d3dtypes.h:1813: warning: ignoring #pragma warning
   In file included from /usr/win32/include/dshow.h:48, from
   common.h:45, from dshow.cpp:35: /usr/win32/include/control.h:2:
   warning: ignoring #pragma warning dshow.cpp: In function int
   CommonOpen(vlc_object_t*, access_sys_t*, vlc_bool_t) ':
   dshow.cpp:456: error: expected primary-expression before '<<' token
   dshow.cpp:456: error: expected primary-expression before '<<' token
   dshow.cpp:456: error: expected primary-expression before '<<' token
   dshow.cpp:456: error: expected primary-expression before '<' token
   dshow.cpp:456: error: expected primary-expression before '.' token
   dshow.cpp:470: error: expected primary-expression before '==' token
   dshow.cpp:470: error: expected primary-expression before '==' token
   dshow.cpp:470: error: expected primary-expression before '==' token
   dshow.cpp:470: error: expected primary-expression before '=' token
   dshow.cpp:484: error: expected primary-expression before '>>' token
   dshow.cpp:484: error: expected primary-expression before '>>' token
   dshow.cpp:484: error: expected primary-expression before '>>' token
   dshow.cpp:484: error: expected primary-expression before '>' token
   dshow.cpp:484: error: expected primary-expression before '.' token
   dshow.cpp:485: error: expected;' before "IAMCrossbar" dshow.cpp:491:
   error: pXbar' undeclared (first use this function) dshow.cpp:491:
   error: (Each undeclared identifier is reported only once for each
   function it appears in.) make[6]: \**\* [libdshow_plugin_a-dshow.o]
   Error 1 make[6]: Leaving
   directory/home/Administrator/vlc-trunk/modules/access/dshow' make[5]:
   **\* [all-modules] Error 1 make[5]: Leaving directory
   \`/home/Administrator/vlc-trunk/modules/access/dshow' make[4]:**\ \*
   [all-recursive] Error 1 make[4]: Leaving directory
   \`/home/Administrator/vlc-trunk/modules/access' make[3]: \**\* [all]
   Error 2

Basically in case of conflict svn adds "<<< mine" and "=======" and
">>>> r1242" which makes gcc complain.

FIX: revert the offending file

===Objective C source seen but \`OBJC' is undefined===

The configure process stops halfway.

   -  aclocal-1.9 -I m4
   -  autoconf
   -  autoheader

   + automake-1.9 --add-missing --copy -Wall configure.ac: installing
   \`autotools/install-sh' configure.ac: installing \`autotools/missing'
   activex/Makefile.am:143: shell $(VLC_CONFIG: non-POSIX variable name
   activex/Makefile.am:143: (probably a GNU make extension)
   activex/Makefile.am: installing \`autotools/compile'
   activex/Makefile.am: installing \`autotools/depcomp'
   modules/gui/macosx/Makefile.am: Objective C source seen but \`OBJC'
   is undefined modules/misc/testsuite/Makefile.am: Objective C source
   seen but \`OBJC' is undefi ned src/Makefile.am: Objective C source
   seen but \`OBJC' is undefined Makefile.am:282: user target
   \`vlc$(EXEEXT)' defined here...
   /usr/share/automake-1.9/am/program.am: ... overrides Automake target
   \`vlc$(EXEEX T)' defined here Makefile.am:230: while processing
   program \`vlc' make: \**\* No targets specified and no makefile
   found. Stop.

This problem is related to a warning earlier on and only occured in a
few revisions where a built-in workaround wasn't working properly:

   + echo 'Enabling provisional autoconf 2.59 work-around. Update
   autoconf ASAP.' Enabling provisional autoconf 2.59 work-around.
   Update autoconf ASAP.

FIX: update autoconf to 2.60 or newer. If Cygwin doesn't provide this
version yet then build it yourself from extras/contrib.

Enter the following commands in your Cygwin shell:

   cd vlc-trunk/extras/contrib

   ./bootstrap

   cd src

   make .autoconf

There should now be compiled autoconf version (probably 2.60 or newer)
in extras/contrib that the bootstrap process will use.

Now start the whole "Compile VLC" process from the start again.

===Error: cannot create temporary file for diversion: Permission
denied===

If the above error appears, it might mean you don't have the TMPDIR
defined in cygwin. You will need to define it and have its value point
to your temporary directory. You can use '''export
TMPDIR="/cygdrive/c/temp"''' or any directory for it (/cygdrive/c/temp
is same as C:temp). If this doesn't help, make sure you run cygwin with
admin rights (With Windows Vista, right click cygwin shortcut and select
"Run as administrator"). Avira AntiVir might also cause issues to m4, so
disabling it while ./bootstrap might help.

==Compiling faster== Building VLC on Cygwin is really slow, but you can
spend less time recompiling by using [http://ccache.samba.org/ ccache].
This software saves the files compiled with their compilation command,
and output them if they were not changed and if the compilation command
is the same as last build. It is really useful for frequent make clean
&& make. To use it, change the CC line in your configure script to:

   CC="ccache gcc -mno-cygwin" CXX="ccache g++ -mno-cygwin"

The first build after reconfiguring will be as slow as ever, but the
following builds will be faster.

=Version=

20050627 Initial version

20050628 Updated some more exceptions

20050628 Some info added about FFmpeg compiling with AMR

20050629 Finalized FFmpeg compiling

20050630 Cross-compiling

20050724 Some extra compile explanations

20050726 Removed cross-compiling (was for linux -> win32) Patching
source code with .diff files

20050823 Added zlib error

20050923 --enable-sdl --with-sdl-config-path=/usr/win32/bin added to
configure. Added debug section

20051102 Changed FFmpeg lib names

20051128 Detailed Cygwin upgrade/downgrade for gcc 3.3. Renamed some
update scripts. Added FFmpeg CVS update. --disable-gnomevfs added to
configure (only used on linux)

20060121 PKG_CONFIG_PATH=/usr/win32/lib/pkgconfig added to configure

20060128 Added curl and libtool to Cygwin for those that want to be able
to build extras/contrib themselves

20060217 Added make install-libs install-headers to FFmpeg compile

20060222 Remark about missing "gettext" libs for Cygwin during install

20060225 ./bootstrap: you need libtool

20060618 Updated GCC to 3.4 version and added FFmpeg SVN and DTS support

20060805 Added note about using older binutils and gdb for Cygwin!

20060915 Added note about updating autoconf from extras/contrib for an
OBJC problem during configure

20061108 Added note this document is no longer usable since Cygwin has
been unusable probably related to some bash/dos2unix change

20070612 Added note about --enable-dca

20080228 New version by [[User:J-b|jb]]

20080307 Added --host=i686-pc-mingw32 option to the configure script

20080311 Simplification

20080323 Added some tips for Vista

20081001 git should now work from Cygwin again

20081010 expat has moved to under Libs

20081020 QT4 problems part added and new contrib suggestion

20081110 Mozilla plugin addition

20090104 sed command for gettext version change

20090210 JB contrib location added.

20090303 ranlib removed, it is a OPTIONAL STEP!

20090623 Mention 1.1.x support

20090926 Remove sed line (not needed anymore), add tips to 'ash', tell
that version tools are optional, change lib order to alphabets

20091023 Add some more details how to checkout with git

20091028 Update the configure command to work fine for recent version
1.0.2

= See also = \*[[Win32CompileCygwinOld]] - deprecated documentation

[[Category:Building]] [[Category:Coding]] [[Category:Windows]]
