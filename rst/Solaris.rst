== Build VLC on Solaris / OpenSolaris ==

=== Status ===

{\| class="mw-datatable cellpadding-1px" summary="Support status by
platform" ! scope="col" colspan="3" \| Solaris/Oracle&nbsp;Solaris !
scope="col" colspan="4" \| OpenSolaris ! scope="col" colspan="3" \|
OpenIndiana ! scope="col" \| Solaris 11 ! scope="col" \| Solaris 10 !
scope="col" \| Solaris 10 ! scope="col" \| 2009/06 ! scope="col" \|
2009/06 ! scope="col" \| 2010/03 ! scope="col" \| 2010/03 ! scope="col"
\| snv_134 ! scope="col" \| oi151a8 ! scope="col" \| ! scope="col" \|
x86 ! scope="col" \| x86 ! scope="col" \| SPARC ! scope="col" \| x86 !
scope="col" \| SPARC ! scope="col" \| x86 ! scope="col" \| SPARC !
scope="col" \| x86 ! scope="col" \| x86 ! scope="col" \| SPARC 2.x.x
(videolan) \| style="background:#8BE09F;" \| Yes (last tested 2.1.5) \|
\| \| \| \| \| \| \| style="background:#8BE09F;" \| Yes (last tested
2.1.5) \| master (videolan) \| {{Untested}} \| {{No}} \| {{No}} \|
{{No}} \| {{No}} \| {{No}} \| {{No}} \| {{Untested}} \| {{Untested}} \|
{{Untested}} 1.x forks (videolan) \| \| {{No}} \| {{No}} \| {{No}} \|
{{No}} \| {{No}} \| {{No}} \| {{Untested}} \| {{Untested}} \|
{{Untested}} [https://repo.or.cz/w/vlc/solaris.git master
(repocz/solaris)] \| \| {{Partial}}¹ \| {{Partial}}¹ \| {{Partial}}¹ \|
{{Partial}}¹ \| {{Yes}} ''(Last tested 06/02/11)'' \| {{Partial}}¹ \|
{{Untested}} \| {{Untested}} \| {{Untested}}
[https://repo.or.cz/w/vlc/solaris.git/shortlog/refs/heads/solaris-vlc-1.1
1.1 branch (repocz/solaris)] \| \| {{Yes}} ''(Last tested 1.1.4)'' \|
{{Yes}} ''(Last tested 1.1.4)'' \| {{Yes}} ''(Last tested 1.1.4)'' \|
{{Untested}} \| {{Yes}} ''(Last tested 1.1.6-git rel 1.1.7)'' \|
{{Untested}} \| {{Yes}} ''(Last tested 1.1.10)'' \| {{Untested}} \|
{{Untested}} \|}

¹ requirements: CSWautomake ≥ 1.11.1 /
pkg://openindiana.org/developer/build/automake-111

{{Note-nb|'''Important Note''': Because of changes in VLC making xcb
mandatory, video output modules relying on X11/XCB can't work until
Solaris ships libxcb. Video output is currently done using SDL and will
open on a separate window. Blastwave latest SDL builds uses xcb and are
also unusable (referenced by sdl/aout). Configuring
<code>--disable-sdl</code> makes builds possible, but you'll lose the
sdl video output module too.}}

===== Up-to-date Binary Packages ===== (20150514) A few repositories
with binary packages exist (including QT). If you want to build exactly
those packages yourself or report packaging bugs, then please check out
the instructions on http://pkgbuild.wiki.sourceforge.net

If you want to directly install binary packages, then follow the
instructions in the links below. The IPS repository setup instructions
are listed there.

VLC 2.1.5 for OpenIndiana OI151a8 / OI151a9:
http://sfe.opencsw.org/localhostoi151a8 (hosting kindly provided by the
OpenCSW project but content is solely from SFE project)

VLC 2.1.5 Oracle Solaris 11&trade; http://sfe.opencsw.org/localhosts11
(hosting kindly provided by the OpenCSW project but content is solely
from SFE project)

=== Building on OpenIndiana ===

===== Config &amp; Build process required packages =====

Start by adding the
[https://wiki.openindiana.org/oi/Spec+Files+Extra+Repository extra
repositories]: <syntaxhighlight lang="text"> (outdated!) pkg
set-publisher -p http://pkg.openindiana.org/sfe (outdated!) pkg
set-publisher -p http://pkg.openindiana.org/sfe-encumbered
</syntaxhighlight>

Required packages for build: <syntaxhighlight lang="text">
pkg:/developer/build/automake-110 pkg:/developer/build/autoconf
pkg-config pkg:/developer/gnome/gettext pkg:/developer/build/libtool
</syntaxhighlight>

For modules: <syntaxhighlight lang="text">
pkg:/\ library/video/ffmpeg@0.8.5-0.151.1
pkg:/\ library/desktop/g++/qt@4.7.3-0.151.1 </syntaxhighlight>

===== Setting up your environment =====

===== Configure =====

=== OpenSolaris (Deprecated) ===

Mostly follows Solaris instructions.

Note that despite the configure stage could be configured to call GNU's
ld, the official gcc build always rely on collect2 and call the Sun
linker.

If you get undefined retain-symbol-file errors, your path haven't been
fixed for the configure step (must look into <code>/usr/ccs/bin/</code>
first) and the build process is applying gnu's options to sun's linker.

To use GNU's linker (optional): Either use the
<code>LD_ALTEXEC=/opt/gnu/bin/gld</code> environment variable, or use a
custom gcc build to use <code>/opt/gnu/bin/gld</code>. (vlc would fail
on some gld only options like retain-symbols-file)

( your <code>gcc -v</code> output must not contain:
<code>--with-ld=/usr/ccs/bin/ld --without-gnu-ld</code> )

An alternative to <var>LD_ALTEXEC</var> would be to symlink
<code>/usr/ccs/bin/ld</code> to <code>/opt/gnu/bin/gld</code>

===== Config &amp; Build process required packages =====

Blastwave's additional packages <syntaxhighlight lang="text"> CSWfaac
CSWfaad2 CSWffmpeglib CSWgcc4corert CSWgcc4g++rt CSWggettext CSWiconv
CSWisaexec CSWlame CSWlibogg CSWlibxcbdev CSWncurses CSWpkgutil CSWstl4
CSWsunmath CSWtheora CSWvorbis CSWx264 CSWxvid CSWzlib
</syntaxhighlight> ===== Setting up your environment =====

For Sun Studio <syntaxhighlight lang="bash"> export
PATH=/usr/ccs/bin:/opt/sunstudio12.1/bin:/opt/csw/bin:/usr/xpg4/bin:/usr/sbin:/usr/bin:/usr/sfw/bin:/usr/ccs/bin:/usr/ucb
export
LD_LIBRARY_PATH=/opt/sunstudio12.1/lib:/usr/openwin/lib/X11/:/opt/kde4/lib
export PKG_CONFIG_PATH=/opt/kde4/lib/pkgconfig:/opt/csw/lib/pkgconfig/
export CFLAGS="-D \_XPG4_2 -D \__SunOS -D \__STDC_ISO_10646_\_ -D
\__EXTENSIONS_\_ -features=extensions -fast" export CXXFLAGS=$CFLAGS
export CCC=/opt/sunstudio12.1/bin/CC CC=/opt/sunstudio12.1/bin/cc
MAKE=gmake </syntaxhighlight> For GCC

Untested. See [[#Solaris 10, SPARC|Solaris/Sparc]].

===== Configure =====

Bootstrap has no problems since Osol uses bash. <syntaxhighlight
lang="bash"> ./configure --disable-libgcrypt --disable-remoteosd
--disable-glx --disable-lua --disable-mad --disable-swscale
--disable-postproc --disable-a52 --disable-fribidi --with-gnu-ld=no
--enable-qt4 --disable-xcb </syntaxhighlight>

=== Solaris 10, x86 ===

To be done.

=== Solaris 10, SPARC ===

Sparc builds outside GCC, are currently unstable.

*Many bugs fixed (until now).*\ all shells must point to
<code>/usr/xpg4/bin/sh</code> instead of <code>/bin/sh</code> (not fully
POSIX) (tip: <code>CONFIG_SHELL=/usr/xpg4/bin/sh</code>) *bootstrapping
requires to change subprocess shell (see [[#Bootstrapping]]
below)*\ <code>filesystem.c</code> needs to be patched for
<var>NAME_MAX</var>

Blocking:

*Lots of ''<code>if (p==NULL) msgDbg("foo %s", p)</code>'' in the code
segfaults in multiple places. Developers have assumed that&nbsp;%s is
fixed as "(null)" like Glibc does. Not available on sparc.*\ crashes at
network/httpd.c at <code>poll()</code> level.

===== Boostrapping process required packages =====

Some old packages exists
[http://www.blastwave.org/jir/search.fam?qs=vlc] <syntaxhighlight
lang="text">CSWautoconf autoconf - an extensible package of M4 macros
(all) 2.65,REV=2009.11.30 CSWautomake automake - GNU Makefile generator
inspired by 4.4BSD make and include (all) 1.10.3,REV=2009.12.09
CSWggettext ggettext - GNU gettext (sparc) 0.17,REV=2009.05.27 CSWgm4
gm4 - The GNU m4 implementation of the traditional Unix macro processor
(sparc) 1.4.13,REV=2009.04.06 CSWiconv libiconv - GNU libiconv is a
Unicode conversion library (sparc) 1.13.1,REV=2009.07.01 CSWlibtool
libtool - Generic shared library support script (sparc)
1.5.26,REV=2008.12.22 CSWreadline readline - GNU readline (sparc)
5.2,REV=2009.01.23

</syntaxhighlight> ===== Config &amp; Build process required packages
===== <syntaxhighlight lang="text"> CSWlua lua - a powerful light-weight
programming language (sparc) 5.1.3,REV=2008.04.29 \*\* CSWffmpeg ffmpeg
- very fast video and audio converter (includes libavcodec) - binaries
(sparc) 0.4.9,REV=2008.06.03_rev=svn12629 \*\* CSWliba52 liba52 - free
ATSC A/52 stream decoder (sparc) 0.7.4,REV=2007.03.05 \*\* CSWlibmad
libmad - MPEG Audio Decoder (sparc) 0.15.1,REV=2005.03.26_rev=b \*\*
CSWlibpthreadstubs libpthreadstubs - pthread stubs not provided by
native libc (sparc) 0.1,REV=2008.11.16 \*\* CSWx264 x264 - H264/AVC
video encoder (sparc) 1.0.0,REV=2009.12.13 \*\* CSWlibxcb libxcb - The
XCB library (sparc) 1.1,REV=2008.11.16 CSWlibxcbdev libxcb_dev - The XCB
library (sparc) 1.1,REV=2008.11.16 CSWlibxau libxau - X11 authorisation
library (sparc) 1.0.4,REV=2008.11.17 CSWlibxaudev libxau_dev - X11
authorisation library (sparc) 1.0.4,REV=2008.11.17 CSWxproto xproto -
xproto (sparc) 7.0.14,REV=2008.11.15 CSWlibxdmcp libxdmcp - X11
authorisation library (sparc) 1.0.2,REV=2008.11.16 CSWlibxdmcpdev
libxdmcp_dev - X11 authorisation library (sparc) 1.0.2,REV=2008.11.16
CSWfribidi fribidi - a free implementation of the Unicode Bidirectional
Algorithm (sparc) 0.19.2,REV=2009.09.25 \*\* CSWqt qt - A Cross-platform
application framework for desktop and embedded development (sparc)
4.4.3,REV=2009.01.16 </syntaxhighlight> Sun Studio: We needed to build
those up to date packages (installed in /opt/vlc, as seen in
configuration) <syntaxhighlight lang="text">VLCQt VLCflac
VLClibxcb-devel VLClibxcb VLClua VLCx264 VLCxcbproto VLCxcbutil
</syntaxhighlight> ===== Setting up your environment =====

For Sun Studio Assuming compiler in <code>/opt/sunstudio12.1</code> and
some customly built packages in <code>/opt/vlc</code> <syntaxhighlight
lang="bash"> # Required for bootstrap export ACLOCAL_ARGS="-I
/opt/csw/share/aclocal/"

# Required for configure export
PATH=/opt/sunstudio12.1/bin::/opt/vlc/bin:/opt/csw/bin:/usr/xpg4/bin:/usr/sbin:/usr/bin:/usr/sfw/bin:/usr/ccs/bin:/usr/ucb

export LD_LIBRARY_PATH=/opt/vlc/lib:/opt/sunstudio12.1/lib:/opt/csw/lib
#:/opt/SUNWmlib/lib:/usr/openwin/sfw/lib

export
PKG_CONFIG_PATH=/opt/vlc/lib/pkgconfig:/opt/csw/lib/pkgconfig:/opt/vlc/qt/lib/pkgconfig:/usr/local/lib/pkgconfig

export LUA_LIBS='-L/opt/vlc/lib -llua' LUA_CFLAGS='-I/opt/vlc/include'

export MAKE=gmake export CONFIG_SHELL='/usr/xpg4/bin/sh' export
CCC=/opt/sunstudio12.1/bin/CC CC=/opt/sunstudio12.1/bin/cc MAKE=gmake

export XLIB_XCB_CFLAGS='-I/opt/vlc/include/xcb/'
XLIB_XCB_LIBS='-L/opt/vlc/lib/'

# -D_XPG4_2 required for non-sparc code compatible network structs
export CFLAGS="-I/opt/sunstudio12.1/include -I/usr/include
-features=extensions -D \_XPG4_2 -D \__SunOS -D \__STDC_ISO_10646_\_ -D
\__EXTENSIONS__" export CXXFLAGS="-I/opt/sunstudio12.1/include
-features=extensions -D \_XPG4_2 -D \__SunOS -D \__STDC_ISO_10646_\_ -D
\__EXTENSIONS__" </syntaxhighlight> Using GCC Assuming some customly
built packages in /opt/vlc <syntaxhighlight lang="bash"># Required for
bootstrap export ACLOCAL_ARGS="-I /opt/csw/share/aclocal/"

# Required for configure export
PATH=/opt/vlc/bin:/opt/csw/bin:/usr/xpg4/bin:/usr/sbin:/usr/bin:/usr/sfw/bin:/usr/ccs/bin:/usr/ucb

export
LD_LIBRARY_PATH=/opt/vlc/lib:/opt/csw/lib:/opt/SUNWmlib/lib:/usr/openwin/sfw/lib

export
PKG_CONFIG_PATH=/opt/vlc/lib/pkgconfig:/opt/csw/lib/pkgconfig:/opt/vlc/qt/lib/pkgconfig:/usr/local/lib/pkgconfig

export LUA_LIBS='-L/opt/vlc/lib -llua' LUA_CFLAGS='-I/opt/vlc/include'

export MAKE=gmake export CONFIG_SHELL='/usr/xpg4/bin/sh'

# -D_XPG4_2 required for non-sparc code compatible network structs
export CFLAGS="-D \_XPG4_2 -D \__SunOS -D \__STDC_ISO_10646_\_ -D
\__EXTENSIONS__" export CXXFLAGS=$CFLAGS

</syntaxhighlight> ===== Bootstrapping =====

Bootstrap script needs to be able to run same subshells as parent. If
bootstrap fails on <code>genmf</code>, then the subshell has fallen back
to the default /bin/sh which isn't POSIX-compliant. In that case, you
need to patch as follow: <syntaxhighlight lang="diff"> @@ -97,7 +97,7 @@
AC_DEFUN([PKG_CHECK_MODULES],[ifelse([$4], , :, [$4])]) EOF fi

-modules/genmf sed -ne 's,modules/(.*)/Makefile,1,p' configure.ac
+$SHELL modules/genmf sed -ne 's,modules/(.*)/Makefile,1,p' configure.ac
</syntaxhighlight> <syntaxhighlight lang="bash">ACLOCAL_ARGS="-I
/usr/local/share/aclocal/"

export ACLOCAL_ARGS

/usr/xpg4/bin/sh bootstrap

</syntaxhighlight> ===== Configure ===== <syntaxhighlight lang="bash">
/usr/xpg4/bin/sh configure --with-a52=/opt/csw/ --with-mad=/opt/csw/
--disable-libgcrypt --disable-remoteosd --disable-skins2 --disable-glx
</syntaxhighlight> <code>--with-gnu-ld</code> might also be required
(check configure result!)

Sun Studio: Add <code>--disable-qt4</code> if required. (Qt 4.6.0
Currently fails)

=== Qt4 Interface module ===

Trolltech only supports SunStudio builds. QT4 Interface is mainly C++,
and creates ABI dependencies with Qt libs. Kde-solaris (bionicmutton)
project packages offers the Sun ABI. If you wish to build the Qt4
Module, you need to build vlc with SunStudio, or build your own Qt
library with GCC.

You should run into a without prototype 'wcsstr' issue in
/opt/sunstudio12.1/prod/include/CC/Cstd/rw/traits<br> Only fix known:
Replace <code>wcsstr</code> with <code>wcswcs</code> in that file.

=== libxcb ===

Libxcb must currently be disabled or you'll need to use custome build as
there's no official support. It might make it into the official
repository as the package went past the fasttrack process.

=== Fully patched code repository ===

All patches are on this fork. (until they make it into the main
repository) <syntaxhighlight lang="bash"> git clone
git://repo.or.cz/vlc/solaris.git vlcsolaris </syntaxhighlight> Patches
on master branch are kept on top of this fork using rebase and forced
pushes. Don't expect to pull later updates without rebasing.

[[Category:Building]] [[Category:Operating systems]]
