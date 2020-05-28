{{Historical|use [[Win32CompileCygwinNew]]}} Cygwin environment for
Windows from http://developers.videolan.org/vlc/cygwin-compile.txt

Originally based on "Win32 Cygwin Environment" Rev. B (20041003) by Mark
Moriarty and "Win32 Compile HOWTO" (20050513) by Gildas Bazin and
Olivier Teulière. =Introduction=

This is a guide for Windows users with a step-by-step instruction to
download, install and configure the following components on your system:

-  [http://www.cygwin.com '''Cygwin''']: Linux-like environment for
   Windows used for compilation of the VLC source code
-  [http://download.videolan.org/pub/videolan/testing/win32/ '''Win32
   contrib package''']: Precompiled library package (with DTS support).

Optionally updated libraries:

-  [http://ffmpeg.mplayerhq.hu '''FFmpeg'''] (with AMR support).
-  [http://developers.videolan.org/x264.html '''x264'''] used for
   encoding H.264/AVC video.
-  [http://www.live555.com '''live555'''] (formerly known as live.com)
   for RTP/RTCP/RTSP/SIP multimedia streaming.

The best approach to start getting comfortable with building VLC from
source is to use the precompiled library package and not yet the
optionally updated ones.

Start off by creating a download folder on your hard drive where you can
put all the installation files:

   C:Downloads (example)

For further reference, the assumption is made that the local user will
be 'Administrator'.

=Cygwin=

More info about Cygwin can be found at http://www.cygwin.com or
http://sourceware.org/cygwin

Download the latest [http://www.cygwin.com/cygwin/setup.exe Cygwin
setup] (it's at the install or update now icon on the site) and save it
in your download location:

   C:Downloadscygwin (example)

==Selecting Cygwin packages to install==

Run the setup program with the following options:

Installation type : Install from Internet (default)

Root directory : C:cygwin (default)

Local Package directory : C:Downloadscygwin (your download location)

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
      5.52-2 unzip (recommended: goes hand in hand with zip utility)
      2.23-2 zip (required: to make self contained zip packages)

   Devel
      2.1 automake (at least 1.5 is required) 20060817-1 binutils
      (autoselected) 1.11.22-1 cvs (required for autopoint) 3.4.4-3
      gcc-core (autoselected) 3.4.4-3 gcc-g++ 20040810-1 gcc-mingw
      20050522-1 gcc-mingw-core (autoselected) 20050522-1 gcc-mingw-g++
      (autoselected) 6.8-2 gdb (optional: for debugging purposes) 0.15-1
      gettext (autoselected) 0.15-1 gettext-devel 1.5.5.1-1 git
      1.5.27a-1 libtool 3.81-2 make '''3.13-1 mingw-runtime'''
      (autoselected) (forcefull downgrade, read below) 2.02-1 nasm
      (optional: for compiling x264 encoder) 0.2.31-1 patchutils
      (optional: for patching source files with .diff files) 0.23a-1
      pkgconfig (recommended: otherwise ./configure will complain about
      accuracy) 1.4.5-2 subversion

   Libs
      1.4.0-1 libgcrypt

   Net
      5.1p1-3 openssh (for source code access)

   System
      3.2.7-1 procps (for source code access)

   Web
      7.16.3-1 curl (optional: for building extras/contrib) 1.10.2-2
      wget (optional: for building extras/contrib)

The package version numbers happen to be the representation of what was
the most current version available at the time this article/section was
updated (20080430) '''with the exception of mingw-runtime which has to
be downgraded to 3.13-1 for proper usage'''. Some source code access
components were added later (20080928) to the list, just quoting state
of the art revisions. It should be relatively uncritical to the overall
build process in this area if a more recent version is used.

If you run into problems of missing packages during install
(particularly gettext: cyggettextsrc-0-14-1.dll not found) then rerun
the setup program and try selecting another Download Site from the
mirror list.

NOTE: Whenever new packages are installed or updated through the Cygwin
installer, make sure not to update the packages by keeping the old
versions (using the "Keep" option).

==Installing older GCC 3.3 version==

The gcc version used for compilation should match the version specified
in the "contrib" package, at present gcc-3.4.5-only.

So the preferred version to use is GCC 3.4 but for historical reasons
this section descibes what version to use together with an older
gcc-3.3.1-only "contrib" package. The 3.3.1 version is not available in
Cygwin but 3.3.3-3 (still) is.

The only compatibility issue with using GCC 3.4 and the precompiled
3.3.1 "contrib" package is that it doesn't support the compiling of the
matroska container .mkv so that leaves 2 options; use gcc 3.3.3-3 with a
3.3.1-only "contrib" or gcc 3.4 (or newer) but disable matroska support.

The second option requires you to add the following line to the
configure options:

   --disable-mkv

If you use the older gcc-g++ and gcc-core versions you have to change
the gcc-mingw-core and gcc-mingw-g++ back to the older versions as well.

Select the following package versions instead:

   Devel
      '''3.3.3-3''' gcc-core '''3.3.3-3''' gcc-g++ 20040810-1 gcc-mingw
      '''20040810-1''' gcc-mingw-core '''20040810-1''' gcc-mingw-g++

NOTE: The gcc-3.4.5-only "contrib" package should compile just fine with
GCC 3.3

==Cygwin environment==

Start Cygwin from the icon on your desktop. If it runs for the first
time it will automatically create a home"username" folder in the Cygwin
environment; user being the currently logged on Windows user. Assuming
this is the 'Administrator' user it will create the following folder:

   C:cygwinhomeAdministrator (example)

NOTE: On your desktop, you can rightclick the Cygwin icon and (in the
Options field of the Cygwin Properties) set the Command history Buffer
size to as large as possible: 999. This setting will make it possible to
scroll back further in the Cygwin environment.

=VLC source code=

== SVN == The very latest VLC source code can be obtained through a tool
called SVN (Subversion). The Cygwin package we're about to install comes
with an internal subversion component. Using this one is the preferred
method.

Read the [[SVN]] page.

== GIT == As of March 2008, VLC has switched to a GIT repository. If you
only need read access, you can continue to use SVN to obtain the latest
VLC trunk. If you need write (commit) access, you need the Cygwin ssh
(Secure Shell), procps, and GIT packages. To see if you have them, in a
bash shell enter: ssh --help git --help pkill --help

If you don't have them, run Cygwin's setup.exe, and download/install
them. For secure shell, generate keys and send the public key (e.g., the
file cygwin/home/your_username/.ssh/id_rsa.pub) to the proper vlc admin
(check in on IRC for more information). Then, update your Cygwin.bat
file, so it looks like: @echo off set CYGWIN=binmode C: chdir
C:cygwinbin c:cygwinbinpkill ssh-agent del
c:cygwinetcprofile.dssh-agent.sh c:cygwinbinssh-agent >
c:cygwinetcprofile.dssh-agent.sh bash --login -i (Change the "C:" as
appropriate)

And update your cygwinetcprofile file, adding the following at the bottom:
   ssh-add

The above changes will kill any pre-existing ssh-agent, start a new
instance of it, and automatically prompt you for your ssh passphrase
when the bash shell opens.

For general VLC git usage, see:
http://wiki.videolan.org/Git#Basic_Git_usage

git-gui appears to work well under Cygwin, provides a fairly simple UI.

== Snapshot == Another way of obtaining source code is by downloading a
daily code "snapshot" from the following location:

http://nightlies.videolan.org/build/source

Download the latest snapshot:

   vlc-snapshot-20080112.tar.gz (example)

and save it into a subfolder in your download location:

   C:DownloadsVLCsrc (example)

Check if the downloaded file has not been renamed by Internet Explorer
in your download folder to something with the extension .tar.tar and if
so then simple rename the files back to .tar.gz

= External libraries to the source code=

VLC depends on other libraries (code) to provide some features like AC3
audio or MPEG-4 video encoding/decoding etc.

Depending on your needs you will have to install and compile some or all
of these external libraries.

== Win32 "contrib" package ==

A package with most of these libraries already compiled so it's actually
really easy to compile a full-featured version of vlc can be found here:

http://download.videolan.org/pub/testing/win32/

Download the latest version of a "contrib" package for win32:

   contrib-20060730-win32-bin-gcc-3.4.5-only.tar.bz2 (example)

It's a good idea to check the INSTALL.Win32 file in the VLC source
directory for the appropriate contrib download file.

Save it into a subfolder in your download location:

   C:DownloadsVLCcontrib (example)

Check if the file has not been renamed by Internet Explorer in your
download folder to something with the extension .tar.tar and if so then
simply rename the file back to .tar.bz2

Also remember the "gcc-3.4.5" part in the "contrib" package filename
since it relates to the GCC version that needs to be installed in Cygwin
lateron!

== Adding additional or updated libraries to the source (optional) ==

Most of them can be found here (source code):

   http://download.videolan.org/pub/testing/contrib/

It is advised not to recompile those libraries.

Updated libraries for FFmpeg and x264 are available through SVN (which
is discussed in a later stage of this guide).

===live555 "snapshot" (optional)===

More info about live555 can be found at:

http://www.live555.com

The project source code is available here:

http://live555.com/liveMedia/public/

Download the latest snapshot:

   live.2007.01.11.tar.gz (example)

NOTE: live555-latest.tar.gz is also the latest version but keeping the
date in the filename makes it easier to reference.

and save it into a subfolder in your download location:

   C:DownloadsVLCsrc (example)

Check if the downloaded file has not been renamed by Internet Explorer
in your download folder to something with the extension .tar.tar and if
so then simple rename the files back to .tar.gz

=Getting the latest sources=

In order to have the latest source code you have to download this using
SVN.

Create a new folder at your download/install location:

   C:DownloadsVLCscripts (example)

==SVN update script for VLC==

Create a new text document with the following line:

   svn checkout svn://svn.videolan.org/vlc/trunk vlc-trunk

Save as filename in your "scripts" folder at your download/install
location with the option "All Files" and not "Text Documents"

   update-vlc.sh (example)

This command will download a complete svn trunk.

Copy the script file into your Cygwin "home directory":

   C:cygwinhomeAdministrator

Start Cygwin and enter the following command in your shell:

   dos2unix update-vlc.sh

This is for converting the 'line endings' made by Windows/DOS (in which
the text document was created) to UNIX style.

==SVN update scripts for additional libraries (optional)==

Updating source code using SVN for additional libraries such as x264 or
FFmpeg works the same way.

===SVN update scripts for x264 (optional)===

Create a new text document with the following line:

   svn checkout svn://svn.videolan.org/x264/trunk x264-trunk

Save as filename in your "scripts" folder at your download/install
location:

   update-x264.sh

Copy the script file into your Cygwin "home directory":

   C:cygwinhomeAdministrator

Start Cygwin and enter the following command in your shell:

   dos2unix update-x264.sh

===SVN update script for FFmpeg (optional)===

Create a new text document with the following line:

   svn checkout svn://svn.mplayerhq.hu/ffmpeg/trunk ffmpeg-trunk

Save as filename in your "scripts" folder at your download/install
location:

   update-ffmpeg.sh

Copy the script file into your Cygwin "home directory":

   C:cygwinhomeAdministrator

Start Cygwin and enter the following command in your shell:

   dos2unix update-ffmpeg.sh

=="Checking out" the latest source code from SVN==

Start Cygwin and enter the following command in your shell:

   ./update-vlc.sh

This will download the current "subversion trunk" (latest code) into
your home directory into the directory specified in your shell script:

   C:cygwinhomeAdministratorvlc-trunk (example)

At the end of the command it will show something like "Checked out
revision 18561".

The vlc-trunk folder will get over-written/updated the next time you run
the command. If you want to save a so called "snapshot" of the existing
vlc-trunk, rename or copy the current directory into something desired
(like vlc-trunk-20070112).

NOTE: Updating the source code for additional libraries such as x264,
FFmpeg etc. is done by running their corresponding update scripts.

==Extracting the source from a "snapshot"==

If you are not using SVN to obtain the latest source code but are using
a daily "snapshot" then copy that source package from your
download/install location to the Cygwin home directory:

   C:cygwinhomeAdministrator

Start Cygwin and enter the following command in your shell:

   tar xvf vlc-snapshot-20070112.tar.gz (example)

Replace with your version of the source package.

This will extract the contents of the file into a subfolder within your
Cygwin environment with the naming convention something like:

   vlc-0.9.0-svn (example)

=Installing the Win32 "contrib" package in Cygwin=

First the additional libraries have to be "installed" in Cygwin.

==Extracting the Win32 "contrib" package==

Copy the "contrib" package from your download/install location to the
home directory:

   C:cygwinhomeAdministrator

Start Cygwin and enter the following command in your shell:

   tar xjvf contrib-20061202-win32-bin-gcc-3.4.5-only.tar.bz2 -C /
   (example)

Replace with your version of the "contrib" file and DON'T FORGET THE /
(slash) at the end.

This will extract the contents of the file into usr/win32 folder within
your Cygwin environment.

NOTE: Make sure to DELETE your old version instead of extracting a new
version on top of it.

==Keeping the Win32 "contrib" package up-to-date==

For maintenance purposes periodically check:

http://download.videolan.org/pub/testing/win32/

to see if a newer "contrib" is available. If that is the case you should
DELETE the existing directory structure which is for the precompiled
"contrib" package:

   C:cygwinusrwin32 (example)

Download the newer file and follow the installation instructions the
same as before so you will end up with the most up-to-date version.

NOTE: Make sure to DELETE your old version instead of extracting a new
version on top of it.

=Configure scripts=

In order to make our lives just a bit easier the following section
describes what commandline options should be used for compiling and
those commands will then be put into a "script" that can be executed
(rather than having to copy and paste all the time).

==Configure script for compiling VLC==

Create a new text document with the following lines:

   CONTRIB_TREE=/usr/win32 PATH=${CONTRIB_TREE}/bin:$PATH ./bootstrap &&
   CPPFLAGS="-I${CONTRIB_TREE}/include -I${CONTRIB_TREE}/include/ebml"
   LDFLAGS=-L${CONTRIB_TREE}/lib
   PKG_CONFIG_LIBDIR=${CONTRIB_TREE}/lib/pkgconfig CC="gcc -mno-cygwin"
   CXX="g++ -mno-cygwin" ./configure --host=i686-pc-mingw32 --enable-sdl
   --with-sdl-config-path=${CONTRIB_TREE}/bin --disable-gtk --enable-nls
   --enable-ffmpeg --with-ffmpeg-mp3lame --with-ffmpeg-faac
   --with-ffmpeg-zlib --enable-faad --enable-flac --enable-theora
   --with-wx-config-path=${CONTRIB_TREE}/bin
   --with-freetype-config-path=${CONTRIB_TREE}/bin
   --with-fribidi-config-path=${CONTRIB_TREE}/bin --enable-live555
   --with-live555-tree=${CONTRIB_TREE}/live.com --enable-caca
   --with-caca-config-path=${CONTRIB_TREE}/bin
   --with-xml2-config-path=${CONTRIB_TREE}/bin
   --with-dvdnav-config-path=${CONTRIB_TREE}/bin --disable-cddax
   --disable-vcdx --enable-goom --enable-twolame --enable-dvdread
   --disable-gnomevfs --enable-dts --disable-optimizations
   --enable-debug

NOTE: The following option is added for DTS Coherent Acoustics streams
decoding support. The latest "contrib" package should already contain
libdca (formerly known as libdts) needed to compile this but at present
it's disabled by default:

   --enable-dts

NOTE: For VLC 0.9.0, replace the previous option by:

   --enable-dca

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

NOTE: The following options is needed for QT4 support:

   --enable-qt4

As of version 0.9.0 VLC will include the QT interface. More information
can be found about QT here: http://www.trolltech.com

The "Win32 contrib package" at present only includes the linux
equivalents of uic, moc and roc executables which are required for
building this interface.

The linues executables have to be '''deleted''' from the contrib folder:

   C:cygwinusrwin32binmoc (example) C:cygwinusrwin32binrcc (example)
   C:cygwinusrwin32binuic (example)

The moc, rcc and uic.exe from the
[http://www.trolltech.com/developer/downloads/qt/windows Qt/Windows Open
Source Edition] (these can be found in the bin folder after
installation) have to be placed in the contrib folder:

   C:cygwinusrwin32binmoc.exe (example) C:cygwinusrwin32binrcc.exe
   (example) C:cygwinusrwin32binuic.exe (example)

Save as filename in your "scripts" folder at your download/install
location:

   configure-vlc.sh

NOTE: Save using "All files" and not "Text files" otherwise Windows
might append the extension .txt

Copy the file into your home directory:

   C:cygwinhomeAdministrator

Start Cygwin and enter the following command in your shell:

   dos2unix configure-vlc.sh

===POSIX emulation layer===

VLC can be built with or without the so called POSIX emulation layer.
Without is the default and is usually better (and with hasn't been
tested for quite some time). If you do want to use the emulation layer,
then just leave out the line with the following options:

   CC="gcc -mno-cygwin" CXX="g++ -mno-cygwin"

===VLC optional settings===

The following option should be used when compiling using the GCC 3.4
version with older "contrib" gcc-3.3.1-only:

   --disable-mkv

==Configure scripts for compiling additional libraries (optional)==

The following section is optional. The "contrib" package contains
precompiled libraries but it is possible to update some of those
libraries to the most current versions such as x264 and FFmpeg.

===FFmpeg with AMR support (optional)===

The AMR (Adaptive Multi Rate) codec is designed to encode and decode
speech with acceptable quality for transmission over relatively low
bandwidth channels with minimal latency, typically used in mobile
networks (3GP) or voice message applications.

The AMR codec is usually referred to as:

   Narrow Band (AMR-NB, fourcc samr) for low quality Wide Band (AMR-WB,
   fourcc samw) for high quality

The sources for AMR are not compatible with the GPL (General Public
License). AMR support is disabled by default.

====Getting the AMR reference codecs (optional)====

The AMR reference codecs can be found on the 3GPP site
http://www.3gpp.org at the following download location for zipped source
code packages:

http://www.3gpp.org/ftp/Specs/2004-03/Rel-5/26_series/

Download the following 3 packages to a subfolder in your
download/install location:

   C:DownloadsVLCsrc (example)

1. AMR - latest 26073 package:

http://www.3gpp.org/ftp/Specs/2004-03/Rel-5/26_series/26073-530.zip
(example)

3GPP TS 26.073 V5.3.0 (2004-03) ANSI-C code for the Adaptive Multi Rate
(AMR) speech codec (Release 5)

2. AMR_FLOAT - latest 26104 package:

http://www.3gpp.org/ftp/Specs/2004-03/Rel-5/26_series/26104-540.zip
(example)

3GPP TS 26.104 V 5.4.0 (2004-03) ANSI-C code for the Floating-point
Adaptive Multi Rate (AMR) speech codec (Release 5)

3. AMRWB_FLOAT - latest 26204 package:

http://www.3gpp.org/ftp/Specs/2004-03/Rel-5/26_series/26204-520.zip
(example)

3GPP TS 26.204 V5.2.0 (2003-09) ANSI-C code for Floating-point Adaptive
Multi Rate Wideband (AMR-WB) speech codec (Release 5)

====Extracting the AMR reference codecs (optional)====

The following AMR reference packages should now be in your
download/install location:

   26073-530.zip (example) 26104-540.zip (example) 26204-520.zip
   (example)

Using your favourite unzipper (Windows internal extraction wizard,
WinZIP, WinRAR etc.) extract the zip files in the into the current
folder (Windows wizard would use "Extract All" and WinZIP or WinRAR
would use "Extract to 'foldername' which is the same as the .zip package
name").

This will create the following folders:

   C:DownloadsVLCsrc26073-530 C:DownloadsVLCsrc26104-540
   C:DownloadsVLCsrc26204-520

Within those folders another .zip package exists. Again unpack those zip
files into the current folder:

   26073-530_ANSI_C_source_code 26104-540_ANSI_C_source_code
   26204-520_ANSI-C_source_code

Now each unpacked source code package has an individual folder named
"c-code".

Rename the c-code subfolders within each package to amr, amr_float and
amrwb_float:

   C:DownloadsVLCsrc26073-53026073-530_ANSI_C_source_codec-code to amr
   C:DownloadsVLCsrc26104-54026104-540_ANSI_C_source_codec-code to
   amr_float
   C:DownloadsVLCsrc26204-52026204-520_ANSI-C_source_codec-code to
   amrwb_float

NOTE: the 530, 540 to 520 order looks a bit confusing but those are
actually just version numbers and the folders are shown in the correct
alphabetical order.

Copy each of the the following folders (including content, so just
select the whole folders itself):

   amr amr_float amrwb_float

to the Cygwin home directory in the libavcodec subfolder of where the
FFmpeg package resides:

   C:cygwinhomeAdministratorffmpeg-trunklibavcodec (example)

===FFmpeg configure script with "contrib" package (optional)===

NOTE: This compile script assumes you are also using the same FFmpeg
version as is used in the "contrib" package (this is why the cflags and
ldflags also point to the win32 folder where the "contrib" package was
extracted).

Create a new text document with the following lines:

   ./configure --enable-mingw32 --enable-memalign-hack
   --extra-cflags=-I/usr/win32/include --extra-ldflags=-L/usr/win32/lib
   --prefix=/usr/win32 --cc="gcc -mno-cygwin" --enable-faac
   --enable-mp3lame --enable-pp --enable-gpl --log

NOTE: For AMR encoding/decoding support also add the following options:

   --enable-amr_nb --enable-amr_wb

NOTE: VLC uses the x264 lib directly and not through ffmpeg so there is
no need to add --enable-x264

Save as filename in your "scripts" folder at your download/install
location:

   configure-ffmpeg.sh (example)

NOTE: Save using "All files" and not "Text files" otherwise Windows
might append the extension .txt

Copy the file into your home directory:

   C:cygwinhomeAdministrator

Start Cygwin and enter the following command in your shell:

   dos2unix configure-ffmpeg.sh

===FFmpeg configure script for FFmpeg "stand-alone" (optional)===

This section is only if FFmpeg compiling is required as a stand-alone
package and not in combination with the precompiled "contrib" package.

In case of failure to compile VLC with different settings (added/updated
libraries to the "contrib") it is advisable to test if FFmpeg does
compile OK just in "stand-alone" mode.

Create a new text document at the download location with following
lines:

   ./configure --target-os=mingw32 --enable-memalign-hack
   --extra-cflags=-mno-cygwin --extra-libs=-mno-cygwin --enable-postproc
   --enable-gpl

NOTE: When including libraries the following options should be
added/changed, pointing to the appropriate folder where does libraries
are located (for VLC "contrib" that would be /usr/win32 but in other
situations it might be the default /usr/local):

   --extra-cflags=-I/usr/local/include --extra-ldflags=-L/usr/local/lib
   --prefix=/usr/local

Save as filename in your "scripts" folder at your download/install
location:

   configure-ffmpeg-svn.sh (example)

Start Cygwin and enter the following command in your shell:

   dos2unix configure-ffmpeg-svn.sh

==x264 configure script (optional)==

Create a new text document with the following lines:

   ./configure --prefix=/usr/win32

NOTE: for debugging purposes you can add the following option:

   --enable-debug

Save as filename in your "scripts" folder at your download/install
location:

   configure-x264.sh

NOTE: Save using "All files" and not "Text files" otherwise Windows
might append the extension .txt.

Copy the file into your home directory:

   C:cygwinhomeAdministrator

Start Cygwin and enter the following command in your shell:

   dos2unix configure-x264.sh

=Compiling source code=

It's time to start Cygwin again...

==Additional libraries==

If any updated or additional libraries are used they need to be compiled
first. Since some of these are used indirectly through FFmpeg, FFmpeg
should be compiled last.

===Compiling x264 (optional)===

This section is only required for x264 compiling where you want to
compile x264 yourself in order to use the latest version.

Change to the appropriate x264 folder

   cd x264-trunk (example)

   ./configure

   make

If the make proceeded without errors you will have compiled a new
library file:

   C:cygwinhomeAdministratorx264-trunklibx264.a (example)

Copy this file into the Cygwin usr/win32 folder:

   C:cygwinusrwin32lib (example)

Also take the following file .h file:

   C:cygwinhomeAdministratorx264-trunkx264.h (example)

Copy this file into the usr/win32/include folder:

   C:cygwinusrwin32include (example)

NOTE: This will overwrite the x264.h and libx264.a from the precompiled
"contrib" package!

===live555 (optional)===

This section is only required if you want to compile the latest version
of live555.

Copy the live555 project package from your download/install location to
the home directory:

   C:cygwinhomeAdministrator

Start Cygwin and enter the following command in your shell:

   tar xvf live.2006.05.17.tar.gz (example)

Replace with your version of the source package.

This will extract the contents of the file into a subfolder within your
Cygwin environment with the naming convention something like:

   live (example)

===Compiling FFmpeg (optional)===

This section is only required for FFmpeg compiling.

Change to the appropriate FFmpeg folder

   cd ffmpeg-trunk (example)

   make clean

   make distclean

(This will haved remove everything except code related stuff, VLC uses a
"toolbox" script which can clean a bit more).

   ../configure-ffmpeg.sh

====Preparations for AMR support (optional)====

If you included the AMR reference codec sources in FFmpeg you should see
that AMR-NB and WB "float support" should be working:

   AMR-NB float support yes AMR-NB fixed support no AMR-WB float support
   yes AMR-WB IF2 support no network support no License: GPL

   AMR WB FLOAT NOTICE ! Make sure you have downloaded TS26.204 V5.1.0
   from
   http://www.3gpp.org/ftp/Specs/archive/26_series/26.204/26204-510.zip
   and extracted the source to libavcodec/amrwb_float

   AMR NB FLOAT NOTICE ! Make sure you have downloaded TS26.104 REL-5
   V5.1.0 from
   http://www.3gpp.org/ftp/Specs/archive/26_series/26.104/26104-510.zip
   and extracted the source to libavcodec/amr_float If you try this on
   alpha, you may need to change Word32 to int in amr/typedef.h

NOTE: These warnings/notices can be ignored since we are using more
recent versions.

====Building FFmpeg (optional)====

First clean up any leftovers from a previous compile using the following
commands:

   make clean

   make distclean

(This will haved remove everything except code related stuff, VLC uses a
"toolbox" script which can clean a bit more).

Now build FFmpeg with the following command:

   make

If the make proceeded without errors you will have compiled two new
"library" files:

   C:cygwinhomeAdministratorffmpeg-trunklibavcodeclibavcodec.a (example)
   C:cygwinhomeAdministratorffmpeg-trunklibavformatlibavformat.a
   (example)

To copy the appropriate libs and header files to the (extracted) contrib
folder use:

   make install-libs install-headers

For historical reasons the "old" method is still described here as well:

Copy the library files (with the .a extension) into the Cygwin usr/win32
folder:

   C:cygwinusrwin32lib (example)

NOTE: This will overwrite libavcodec.a and libavformat.a from the
precompiled "contrib" package!

For backup reasons you can first copy or rename the original files in
the "contrib" package (so you won't have to reinstall the complete
contrib package but can simply copy these again)

   C:cygwinusrwin32liblibavcodec.a to libavcodec.a.org
   C:cygwinusrwin32liblibavformat.a to libavformat.a.org

In older versions of ffmpeg the libraries had other names:

   C:cygwinhomeAdministratorffmpeg-20050624libavcodecavcodec.lib
   (example)
   C:cygwinhomeAdministratorffmpeg-20050624libavformatavformat.lib
   (example)

Rename those files (in Windows Explorer):

   avcodec.lib to libavcodec.a avformat.lib to libavformat.a

Then copy those library files into the Cygwin usr/win32 folder.

===Compiling live555 (optional)===

How to configure and build the code on a Linux enviroment is explained
on the following live555 page:

http://www.live555.com/liveMedia/#config-unix

Some options need to be changed/added to the config.cygwin file in the
live folder so open this file with a text-editor.

Add the -Wno-deprecated option:

   CPLUSPLUS_FLAGS = $(COMPILE_OPTS) -Wall -DBSD=1 -Wno-deprecated

Save the file under its current name config.cygwin

Enter the following commands in your Cygwin shell:

   cd live

The following command is for converting any DOS/Windows "line endings"
to UNIX style:

   dos2unix config.cygwin

   make clean

   ./genMakefiles cygwin

   make

TODO: Fix live555 compilation. It still fails with the following errors:

   GroupsockHelper.cpp:477: error: aggregate \`ip_mreq_source imr' has
   incomplete type and cannot be defined GroupsockHelper.cpp:482: error:
   invalid application of \`sizeof' to incomplete type \`ip_mreq_source'
   GroupsockHelper.cpp: In function \`Boolean
   socketLeaveGroupSSM(UsageEnvironment&, int, netAddressBits,
   netAddressBits)': GroupsockHelper.cpp:495: error: aggregate
   \`ip_mreq_source imr' has incomplete type and cannot be defined
   GroupsockHelper.cpp:500: error: invalid application of \`sizeof' to
   incomplete type \`ip_mreq_source' make[1]: \**\* [GroupsockHelper.o]
   Error 1

==Compiling VLC==

Enter the following commands in your Cygwin shell:

   cd vlc-trunk

(you can check with the pwd command to see in which folder you are and
with just the cd command without any additional parameters you can
change back to your home directory).

NOTE: The following line is optional, only use that if you have problems
compiling.

   ./toolbox --distclean

(This will have removed everything except code related stuff).

   ../configure-vlc.sh

   make

Cross your fingers...

NOTE: ./ means you run an application/script from the "current folder"
(which is vlc-trunk) and ../ points to "one directory up" (which is
where configure-vlc.sh is).

==Creating self contained packages==

Once the compilation is done, you can either run VLC directly from the
source tree or you can build self-contained VLC packages with the
following "make" commands:

   make package-win32-base

(This will create a subdirectory named vlc-x.x.x with all the binaries
"stripped" without any debugging symbols).

   make package-win32-zip

(Same as above but will package the directory in a zip file).

   make package-win32

(Same as above but will also create an auto-installer package. You will
need to have NSIS installed in its default location for this to work).

=Advanced usage=

==Updating Cygwin package versions==

If you need to update or install additional packages you can just run
the Cygwin setup.exe from your download location:

   C:Downloadscygwinsetup.exe (example)

===Using older GCC and MINGW version===

You should be aware that Cygwin automatically selects the latest
versions for gcc-g++ and gcc-mingw so if you are using older versions of
those (like 3.3.3-3 and the accompanied 20040810-1 packages for mingw)
and wish to continue to use them you need to '''change''' those versions
to '''Keep''' for '''every time you use the update process'''.

NOTE: You can click on the "View" button a few times until you see
"Partial" next to it. This will give you an overview of some "Current"
packages that will be updated to "New" versions.

select the View button until it reaches: Partial

   Devel
      3.4.4-3 gcc-core -> change version to '''Keep''' 3.4.4-3 gcc-g++
      -> change version to '''Keep''' 20050522-1 gcc-mingw-core ->
      change version to '''Keep''' 20050522-1 gcc-mingw-g++ -> change
      version to '''Keep'''

Selecting the 3.4.4-3 version automatically changes the gcc-mingw-core
and gcc-mingw-g++ to the 20050522-1 (or newer) versions as well.

===Downgrading Cygwin GCC packages===

If your Cygwin gcc versions are already the latest and you wish to
downgrade to gcc 3.3.3-3 then it's not possible to downgrade the
gcc-core/g++ and the mingw packages all at the same time, it has to be
done in two steps.

select the View button until it reaches: Up To Date

   Devel
      3.4.4-3 gcc-core -> change version to '''3.3.3-3''' 3.4.4-3
      gcc-g++ -> change version to '''3.3.3-3'''

Install, OK.

Restart the Cygwin update process.

Select the View button until it reaches: Partial

   Devel
      3.4.4-3 gcc-core -> change version to '''Keep''' 3.4.4-3 gcc-g++
      -> change version to '''Keep'''

Select the View button until it reaches: Up To Date

   Devel
      20050522-1 gcc-mingw-core -> change version to '''20040810-1'''
      20050522-1 gcc-mingw-g++ -> change version to '''20040810-1'''

Install, OK.

Again, for any new update process remember to change back those
versions!

==GDB (Gnu Debugger)==

This section requires that you installed the gdb (Gnu Debugger) in
Cygwin.

This is a typical example of creating a crashlog:

   cd vlc-trunk

   gdb --args vlc.exe --fast-mutex --reset-config --reset-plugins-cache

NOTE: vlc-0.9.0 uses libtool for building sources, if you want to debug
from the source tree, you should type the following command instead:

   libtool -mode=execute gdb --args vlc --reset-config
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

These are the log outputs that are more usefull to developers than just
mentioning "it crashes"!

NOTE: In GDB mode there are sometimes situations where GDB initially
"crashes" on certain network activity (opening network shares, network
traffic) which in normal operation does not occur. Just select c for
continue until "normal" operation continues.

==.diff files==

Frequently patches to source code are presented or discussed in forums
or in mailing lists in so called .diff format (these are "differences"
to the source code).

You can apply those patches yourself to the source code or create .diff
files. This requires the patchutils package in Cygwin.

===Patching source code===

Download a so called .diff file:

   sse2-pixel-routines-v3.diff (example)

NOTE: make sure the file doesn't get a .txt extension, so Save as type
"All Files" instead of "Text Document" (IE has a habit of renaming to
.txt. If that happens just simply rename to .diff)

Copy the .diff file into the appropriate source folder

   x264-trunk (example)

Apply the patch as follows

   patch -p0 < sse2-pixel-routines-v3.diff (example)

NOTE: replace sse2-pixel-routines-v3.diff with your "patch"

This will output something like:

   patching file common/i386/pixel.h patching file
   common/i386/pixel-a.asm patching file common/pixel.c

Your source code is now patched!

NOTE: If you want to revert to the original version you can use the -R
option with the patch command or alternatively you can just delete the
changed files and just do an SVN update to get the original/latest SVN
version back.

===Creating .diff files===

When changing the source code it's possible to create a "difference"
file against the latest source.

In this example the file /modules/codec/x264.c was changed (the part "in
kbit/s" was added to a description).

Start your Cygwin shell.

Change to the appropriate folder where a changed file is.

   cd vlc-trunk/modules/codec (example)

Output the svn diff command to a file:

   svn diff -u > x264-patch.diff

The current folder now holds a x264-patch.diff file containing the
following:

   .. rubric:: Index: x264.c
      :name: index-x264.c

   --- x264.c (revision 15921) +++ x264.c (working copy) @@ -131,7
   +131,7 @@ #define RATETOL_LONGTEXT `N <>`__\ ( "Allowed variance in
   average. " "bitrate (in kbits/s).")

   -#define VBV_MAXRATE_TEXT `N <>`__\ ("Max local bitrate") +#define
   VBV_MAXRATE_TEXT `N <>`__\ ("Max local bitrate in kbit/s") #define
   VBV_MAXRATE_LONGTEXT `N <>`__\ ( "Sets a maximum local bitrate in
   kbits/s.")

      #define VBV_BUFSIZE_TEXT `N <>`__\ ("VBV buffer")

NOTE: In Windows you should open this file with something else than
notepad (so wordpad or some more advanced editor). This has to do with
the end of line markers that are present in the file since it was made
in a Linux environment.

==Reverting to older SVN source code==

If for some reason you want to revert to (use) an older version (let's
say you are using revision 15916 of the VLC source code but would like
to test with 15915) then use the svn "update" function from within
Cygwin but use an older revision number.

Start your Cygwin shell...

   cd vlc-trunk

   svn up -r 15915

And you'll see something like this:

   U srcinputinput.c Updated to revision 15915.

The following command will show the version used:

   svn info

=FAQ/Troubleshooting=

This chapter mentions some frequently encountered problems during
compile and installation procedures and possible fixes or workarounds.

=="Making all in <folder>" takes forever with 0% CPU usage==

Make seems to "stall" at a certain point (no CPU usage) and nothing
seems to happen anymore:

   Making all in mpeg make[5]: Entering directory
   \`/home/Administrator/vlc-trunk/modules/mux/mpeg'

NOTE: This problem seems to occur on dual CPU (or HyperThreading
enabled) systems.

FIX: in the vlc-trunk do a ./toolbox --distclean before doing a
../configure-vlc.sh and try again...

==configure: error: C compiler cannot create executables==

The ../configure-vlc.sh gives the following error:

   checking for gcc... gcc -mno-cygwin checking for C compiler default
   output file name... configure: error: C compiler cannot create
   executables

FIX: it's very likely you are using the gcc 3.3 version but with the
wrong mingw packages (the ones that come with 3.4). Reinstall the
following gcc-mingw packages but make sure to use the older version!!!

20050522-1 gcc-mingw-core autoselected -> change to 20040810-1
20050522-1 gcc-mingw-g++ autoselected -> change to 20040810-1

You can check what version of gcc you are version in the Cygwin shell by
using the following command:

   gcc --version

==collect2: ld returned 1 exit status (libebml)==

A make fails with the following error:

   /usr/win32/lib/libebml.a(EbmlMaster.o):EbmlMaster.cpp:(.text$_ZNSt14__simple_all
   ocISsSt24__default_alloc_templateILb1ELi0EEE10deallocateEPSsj[std::__simple_allo
   c<std::basic_string<char, std::char_traits<char>,
   std::allocator<char> >, std::\_ \_default_alloc_template<true, 0>
   >::deallocate(std::basic_string<char, std::char \_traits<char>,
   std::allocator<char> >\ *, unsigned int)]+0x1d): undefined referenc e
   to \`std::__default_alloc_template<true, 0>::deallocate(void*,
   unsigned int)'
   /usr/win32/lib/libebml.a(EbmlMaster.o):EbmlMaster.cpp:(.text$_ZNSt14__simple_all
   ocISsSt24__default_alloc_templateILb1ELi0EEE8allocateEj[std::__simple_alloc<std:
   :basic_string<char, std::char_traits<char>, std::allocator<char> >,
   std::__defau lt_alloc_template<true, 0> >::allocate(unsigned
   int)]+0x1d): undefined reference to
   \`std::__default_alloc_template<true, 0>::allocate(unsigned int)'
   /usr/win32/lib/libebml.a(EbmlMaster.o):EbmlMaster.cpp:(.text$_ZNSt14__simple_all
   ocIPN7libebml11EbmlElementESt24__default_alloc_templateILb1ELi0EEE8allocateEj[st
   d::__simple_alloc<libebml::EbmlElement*,
   std::__default_alloc_template<true, 0> >::allocate(unsigned
   int)]+0x1d): undefined reference to \`std::__default_alloc_t
   emplate<true, 0>::allocate(unsigned int)'
   /usr/win32/lib/libebml.a(EbmlMaster.o):EbmlMaster.cpp:(.text$_ZNSt14__simple_all
   ocIPN7libebml11EbmlElementESt24__default_alloc_templateILb1ELi0EEE10deallocateEP
   S2_j[std::__simple_alloc<libebml::EbmlElement*,
   std::__default_alloc_template<tr ue, 0>
   >::deallocate(libebml::EbmlElement\*\ *, unsigned int)]+0x1d):
   undefined ref erence to \`std::__default_alloc_template<true,
   0>::deallocate(void*, unsigned in t)' collect2: ld returned 1 exit
   status make[2]: \**\* [vlc.exe] Error 1

This problem is because libEbml is a C++ lib and it doesn't seem to link
with gcc 3.4.

FIX: Use gcc 3.3 with the according 3.3 Win32 "contrib" package version
or use a Win32 "contrib" package for 3.4 (or even better try compiling
it yourself).

WORKAROUND for gcc 3.4: Use --disable-mkv in configure-vlc.

==zip: command not found==

A make package fails with the following error:

   zip -r vlc-0.8.4-svn-win32.zip vlc-0.8.4-svn /bin/bash: line 1: zip:
   command not found make: \**\* [package-win32-base-zip] Error 127

FIX: Doh! forgot to install the zip package in Cygwin :P

==vlc.exe: Permission denied==

A make finished successfully and produced vlc.exe, but running the
executable returns the following:

   bash: ./vlc.exe: Permission denied

The permissions on both vlc.exe & vlc.exe.manifest must be set to
executable.

FIX: Type the following:

   chmod 755 vlc.exe vlc.exe.manifest

==error: parse error before '(' token==

A make (compile) of FFmpeg results in the following error:

   /usr/include/sys/unistd.h:203: error: parse error before '(' token
   make[1]: \**\* [ffm.o] Error 1

It's very likely you are usix the POSIX emulater which you shouldn't...

FIX: compile with the option

   -mno-cygwin

==error: invalid conversion from \`const void*' to \`void*'==

   src/theme_loader.cpp: In function \`int gzwrite_frontend(int, const
   void*, size_t)': src/theme_loader.cpp:599: error: invalid conversion
   from \`const void*' to \`void*' src/theme_loader.cpp:599: error:
   initializing argument 2 of \`int gzwrite(void*, void*, unsigned int)'
   make[6]: \**\* [libskins2_plugin_a-theme_loader.o] Error 1

FIX: This is related to a problem with the zlib library, updating to at
least 1.2.2-1 but preferably 1.2.3 or newer is required

==error: cannot convert \`const wxChar*' to \`const char*==

   if g++ -mno-cygwin -DHAVE_CONFIG_H -I. -I. -I../../..
   -I/usr/win32/include -I/ usr/win32/include/ebml -`D_OFF_T <>`__
   -D_off_t=long -DSYS_MINGW32 -I../../../include
   top_builddir="../../.." ../../../vlc-config --cxxflags plugin
   wxwidgets -Wsign -compare -Wsign-compare -Wall -mms-bitfields -pipe
   -MT libwxwidgets_plugin_a-wx widgets.o -MD -MP -MF
   ".deps/libwxwidgets_plugin_a-wxwidgets.Tpo" -c -o libwxwid
   gets_plugin_a-wxwidgets.o \`test -f 'wxwidgets.cpp' \|\| echo
   './'`wxwidgets.cpp; then mv -f
   ".deps/libwxwidgets_plugin_a-wxwidgets.Tpo" ".deps/libwxwidgets_plugi
   n_a-wxwidgets.Po"; else rm -f
   ".deps/libwxwidgets_plugin_a-wxwidgets.Tpo"; exit 1; fi In file
   included from /usr/win32/include/wx-2.6/wx/debug.h:22, from
   /usr/win32/include/wx-2.6/wx/defs.h:452, from
   /usr/win32/include/wx-2.6/wx/wxprec.h:13, from wxwidgets.h:40, from
   wxwidgets.cpp:39: /usr/win32/include/wx-2.6/wx/wxchar.h: In function
   \`size_t wxStrlen(const wxChar *)':
   /usr/win32/include/wx-2.6/wx/wxchar.h:759: error: cannot convert
   \`const wxChar*' to \`const char*' for argument \`1' to \`size_t
   strlen(const char*)' In file included from
   /usr/win32/include/wx-2.6/wx/memory.h:20, from
   /usr/win32/include/wx-2.6/wx/object.h:25, from
   /usr/win32/include/wx-2.6/wx/wx.h:16, from wxwidgets.h:41, from
   wxwidgets.cpp:39: /usr/win32/include/wx-2.6/wx/string.h: In
   constructor \`wxString::wxString(const wxChar*)':

FIX: update wxwidgets or try a different or newer Win32 "contrib"
package.

==undefined reference to \`_av_parser_change' (FFmpeg)==

   ffmpeg.o: In function `output_packet':
   /home/Administrator/FFmpeg-20050724/ffmpeg.c:1414: undefined
   reference to <>`__\ av_parser_change'
   /home/Administrator/FFmpeg-20050724/ffmpeg.c:1415: undefined
   reference to \`_av_destruct_packet' collect2: ld returned 1 exit
   status make: \**\* [ffmpeg_g.exe] Error 1

This is a possible conflict when you use normal configure-ffmpeg (uses
/usr/win32 contrib) instead of configure-ffmpeg-svn

==undefined reference to \`_pp_get_context' (FFmpeg)==

   ./modules/codec/ffmpeg/libffmpeg.a(libffmpeg_a-postprocess.o): In
   function `Init Postproc__ffmpeg':
   /home/Administrator/vlc-trunk/modules/codec/ffmpeg/postprocess.c:164:
   undefined reference to <>`__\ pp_get_context'
   ./modules/codec/ffmpeg/libffmpeg.a(libffmpeg_a-postprocess.o): In
   function `PPQC allback':
   /home/Administrator/vlc-trunk/modules/codec/ffmpeg/postprocess.c:244:
   undefined reference to <>`__\ pp_get_mode_by_name_and_quality'
   ./modules/codec/ffmpeg/libffmpeg.a(libffmpeg_a-postprocess.o): In
   function `Post procPict__ffmpeg':
   /home/Administrator/vlc-trunk/modules/codec/ffmpeg/postprocess.c:191:
   undefined reference to <>`__\ pp_postprocess' $ ePostproc__ffmpeg':
   /home/Administrator/vlc-trunk/modules/codec/ffmpeg/postprocess.c:209:
   undefined reference to `\_pp_free_mode'
   /home/Administrator/vlc-trunk/modules/codec/ffmpeg/postprocess.c:210:
   undefined reference to <>`__\ pp_free_context' collect2: ld returned
   1 exit status make[2]: **\* [vlc.exe] Error 1 make[2]: Leaving
   directory \`/home/Administrator/vlc-trunk' make[1]:**\ \*
   [all-recursive] Error 1 make[1]: Leaving directory
   \`/home/Administrator/vlc-trunk' make: \**\* [all] Error 2

FFmpeg was not compiled with post processing support. To do so the
following options need to be added to the configure lines for FFmpeg:

   --enable-pp --enable-gpl

Postprocessing code is under GPL.

==error: expected primary-expression before '<<' token==

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

==configure: error: Could not find ffmpeg on your system==

   configure: error: Could not find ffmpeg on your system: you may get
   it from http://ffmpeg.sf.net/ (cvs version is recommended).
   Alternatively you can use --disable-ffmpeg to disable the ffmpeg
   plugins. make: \**\* [config.status] Error 1

This can happen when you do a make without doing a configure and the
configure.ac file in the source code recently updated.

FIX: do a full configure (using ../configure-vlc.sh) and then run the
make process

==Objective C source seen but \`OBJC' is undefined==

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

==Error: cannot create temporary file for diversion: Permission denied==

If the above error appears, it might mean you don't have the TMPDIR
defined in cygwin. You will need to define it and have its value point
to your temporary directory.

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

[[Category:Building]] [[Category:Windows]]
