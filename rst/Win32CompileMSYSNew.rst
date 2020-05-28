{{Outdated}} = '''OUTDATED''' =

See [[Win32CompileMSYS]]

= Introduction = == About ==

MSys is a helper environment for MinGW, the compiler chain for Windows
based on GCC. It can build VLC natively on Windows. Note that you should
also [[Win32Compile|cross compile]] VLC from Linux, because it is
faster, and feels easier.

VLC is a complex program with many dependencies, so minimal command-line
experience is required. Also, don't be in a hurry (4 hours is a minimum
for the whole process) and don't despair if it doesn't work first time.

== Acknowledgements ==

This howto was re-created by [[User:J-b|Jean-Baptiste Kempf]] and
updated in June 2009, September 2009, December 2009 and March 2010.

It was updated in June 2010 by Vicne with the help of J-b, gnosygnu and
MichaelMc

It was updated in July 2012 by gnosygnu. Note that there are several new
notes in [[Win32CompileMSYSTroubleShooting]]. These reflect problems
that were encountered on gnosygnu's setup (Windows XP SP3). Refer to
this
[http://forum.videolan.org/viewtopic.php?f=32&t=102843&sid=f58967215a83981dda030ff6efa3d493
forum thread] for more information.

= Windows tools needed = == Text editor ==

To edit unix-style text documents you need a suitable editor.

You can look at [http://sourceforge.net/projects/notepad2/ notepad2].
You can set File - Line endings - Default to "Unix (LF)", but it always
saves opened files in the ending style they have.

Or you can look at [http://notepad-plus-plus.org/ notepad++].

== Unzip Utility (7-zip) ==

Many files to downloaded will have to be uncompressed. As most of them
use Linux-originated formats (.tar.gz, .tar.bz2, .tar.lzma), you will
need a versatile unzipping utility. A recent version of
[http://www.7-zip.org/ 7-zip] is therefore strongly advised.

Please note that most archives contain directory structures. Unless
otherwise stated, you have to merge the contents with the existing dirs

= GNU Windows Environment = Before installing, ensure your Windows user
name does not contain spaces (VLC will not build in a folder with spaces
in it). If it does, please create another user on your system.

In the following text, we'll refer to this user name as
"&lt;username&gt;". Replace it appropriately where needed of course.

== MinGW == === TDM/MinGW Setup ===

Use the installer found at
http://sourceforge.net/projects/tdm-gcc/files/TDM-GCC%20Installer/tdm-gcc-4.7.1-2.exe/download

Go through the wizard: \* Select "Create" \* Select 32bits \* Install to
C:MinGW \* Keep default settings

=== MinGW utils ===

Install mingw-utils, for unix2dos:
http://prdownloads.sourceforge.net/mingw/mingw-utils-0.3.tar.gz

Extract contents to c:MinGW

== MSys == === MSys Setup ===

Use the installer found at
http://sourceforge.net/project/downloading.php?group_id=2435&filename=MSYS-1.0.11.exe

Go through the wizard and install to to default C:Msys1.0

In the command window that opens, answer questions as follows:

   Accept Post Install: [y] MinGW Installed? [y] path to MinGW:
   [c:/MinGW]

=== MSys Developer Toolkit ===

Use the installer found at
http://downloads.sourceforge.net/mingw/msysDTK-1.0.1.exe

Go through the wizard, keeping the default values.

This will install old versions of autotools, perl, ssh, ftp and sftp.

=== Git === Install Git from
http://code.google.com/p/msysgit/downloads/list?can=3

Go through the wizard, keeping the default value, except the one
speaking of line endings.

=== Wget === You will need Wget:
http://sourceforge.net/projects/gnuwin32/files/wget/1.11.4-1/wget-1.11.4-1-setup.exe/download

Extract it to c:MinGW

=== AutoTools and libcrypt ===

Update autoconf, automake, libtool as well as libcrypt by downloading
the following files and extracting them to C:Msys1.0:

*http://sourceforge.net/projects/mingw/files/MSYS/msysdev/autoconf/autoconf-2.68-1/autoconf-2.68-1-msys-1.0.17-bin.tar.lzma/download*\ http://sourceforge.net/projects/mingw/files/MSYS/msysdev/automake/automake-1.11.1-1/automake-1.11.1-1-msys-1.0.13-bin.tar.lzma/download
*http://sourceforge.net/projects/mingw/files/MSYS/msysdev/libtool/libtool-2.4-1/libtool-2.4-1-msys-1.0.15-bin.tar.lzma/download*\ http://prdownloads.sourceforge.net/mingw/libcrypt-1.1_1-2-msys-1.0.11-dll-0.tar.lzma
*http://sourceforge.net/projects/mingw/files/MSYS/Extension/perl/perl-5.8.8-1/perl-5.8.8-1-msys-1.0.17-bin.tar.lzma/download*\ http://sourceforge.net/projects/mingw/files/MSYS/Extension/m4/m4-1.4.14-1/m4-1.4.14-1-msys-1.0.13-bin.tar.lzma/download

=== Glib and PKG-CONFIG ===

Similarly, download the following files and extract them to C:MSys1.0:

Note\* Download the latest version inside this folders (Last tested to
be OK is glib 2.28, non-dev version)):

*http://ftp.gnome.org/pub/GNOME/binaries/win32/glib*\ ftp://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/pkg-config_0.23-3_win32.zip
*ftp://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/pkg-config-dev_0.23-3_win32.zip*\ http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/gettext-runtime_0.18.1.1-2_win32.zip

'''Note''': I found that compiling 2.1.0 requires xgettext, msgmerge,
msgfmt and so on. These in turn require libiconv. I'm not sure if that
suffices as at this point I gave up.

=== Add pkg config path variable ===

Add the following line to the *top* of C:MSys1.0msys.bat:

   set PKG_CONFIG_PATH=/win32/lib/pkgconfig

== Compile LUA tools ==

VLC uses the LUA scripting language (See [http://www.lua.org lua.org]).
Unfortunately, no binaries are provided so you need to compile them.

*Download the lua tools package from
http://www.lua.org/ftp/lua-5.1.4.tar.gz*\ Uncompress it in your home
folder (C:MSys1.0home&lt;username&gt;) *run MSys*\ type the following
commands:

   cd /home/<username>/lua-5.1.4 make mingw make install

= VLC sources = == Git == Clone the git repo git clone
git://git.videolan.org/vlc.git

= Get Precompiled contribs =
   cd vlc/contrib mkdir win32 && cd win32 ../bootstrap
   --build=i586-mingw32msvc make prebuilt

'''Note''': it will say tar complains, just ignore them and watch tar
die. I had to manually execute the rest of the prebuilt target, which
consists of

   mv i586-mingw32msvc .. cd ../i586-mingw32msvc change_prefix.sh

I also found that change_prefix.sh, which rewrites .pc files to deal
with their chosen location, used the -i option which is not supported by
MSYS-shipped sed. I rewrote the sed script to write changes $file.new
then mv $file.new $file.

= Last change&nbsp;: whoami and hostname =

Whoami is not available on Windows, and hostname doesn't support the -f
option used by the build process. These utilities are used to show the
name and computer of the person who compiled VLC in the 'About' box.

''Note for the brave&nbsp;
   the steps below are file changes so that compile works, but an
   alternative is to download and install GNU whoami and hostname
   functionality. This can be achieved by doing the following steps:

# ''download coreutils from
http://sourceforge.net/projects/mingw/files/MSYS/BaseSystem/coreutils,
selecting any version (latter is normally better) then the file named
like coreutils-5.97-2-msys-1.0.11-ext.tar.lzma (note '-ext' in file
name) and extracting who.exe, whoami.exe, hostname.exe to
C:/MSys/1.0/bin'' # ''download libintl dll from
http://sourceforge.net/projects/mingw/files/MSYS/BaseSystem/libiconv,
selecting any version (latter is normally better) then the file named
like libiconv-1.13.1-2-msys-1.0.13-dll-2.tar.lzma (note '-dll' in file
name) and extracting dll in C:/MSys/1.0/bin'' # ''download libiconv dll
from
http://sourceforge.net/projects/mingw/files/MSYS/BaseSystem/gettext,
selecting any version (latter is normally better) then the file named
like libintl-0.17-2-msys-dll-8.tar.lzma (note '-dll' in file name) and
extracting dll in C:/MSys/1.0/bin''

== Whoami ==

Create a new file containing the single line:

   echo '&lt;username&gt;'

and save it as C:MSys1.0binwhoami (without any extension)

== Hostname ==

Modify configure.ac so that it doesn't call 'hostname -f' as follows:

*open C:MSys1.0home&lt;username&gt;vlcconfigure.ac*\ goto search button:
\*change it as follows:

   old: AC_DEFINE_UNQUOTED(VLC_COMPILE_HOST, "hostname -f 2&gt;
   /dev/null \|\| hostname", [host which ran configure]) new:
   AC_DEFINE_UNQUOTED(VLC_COMPILE_HOST, "hostname", [host which ran
   configure])

= Build VLC =

The build is made exclusively from the command line, so if you closed
the prompt at the LUA step, re-execute C:MSys1.0msys.bat, then type the
commands as mentioned

== Bootstrap ==

   cd vlc cp -v /usr/share/aclocal/\* m4/ bootstrap

== Configure ==

   sh extras/package/win32/configure.sh --host=i586-pc-mingw32msvc
   --disable-nls

If you want any custom options, like "--disable-lua" or anything of that
nature, you can append them.

== Make (compile) ==

Note&nbsp;: If your &lt;username&gt; starts with the "u" or "x"
character, change C:MSys1.0home&lt;username&gt;config.h and double all
backslashes in VLC_COMPILED_BY constant.

Type the following command&nbsp;:

   PATH=/usr/win32/bin:$PATH make

If this step fails, try the following \* Go back to "Precompiled
contribs" section, and obtain the latest compiled contrib (under "Note
for the brave") \* In the configure script section (configure-msys.sh),
open that file and add --disable-upnp

== Create self-contained packages ==

Once the compilation is done, build self-contained VLC packages with one
of the following "make" commands:

   make package-win32-base

(This will create a subdirectory named vlc-x.x.x with all the binaries
"stripped" without any debugging symbols).

   make package-win32-zip

(Same as above but will package the directory in a zip file).

   make package-win32

(Same as above but will also create an auto-installer package. You will
need to have NSIS installed in its default location for this to work).

   make package-win32-base-debug

(This will create a subdirectory named vlc-x.x.x with all the binaries
containing debug info usable by gdb).

Note that with the 1.2 branch these names have changed slightly. Run '
   grep ':' Makefile \| grep package-win32

to see what they are now.

= Troubleshooting =

See [[Win32CompileMSYSTroubleShooting]].

= See also = \*[[Win32CompileMSYSOld]] - deprecated documentation

[[Category:Building]] [[Category:Windows]]
