.. raw:: mediawiki

   {{Historical|Use [[Win32CompileMSYSNew]]}}

MSYS/MinGW environment for Windows from http://developers.videolan.org/vlc/msys-compile.txt

Introduction
============

MSYS/MinGW environment
======================

Setting up a working MSYS/MinGW environment requires the following:

-  MSYS installation
-  Updating MSYS
-  MSYS DTK (Developer Tool Kit)
-  Updating bash (shell)
-  MinGW installation
-  Configuration of fstab
-  Creation of home folder

Note that the following generic resource locations were used to download the appropriate packages (and more recent versions might be obtained from here):

`MSYS/MinGW related <http://prdownloads.sourceforge.net/mingw>`__

`nasm <http://prdownloads.sourceforge.net/nasm>`__

`SDL <http://www.libsdl.org>`__

`zip <http://www.info-zip.org>`__

`pkg-config <http://pkgconfig.freedesktop.org/releases>`__

`sed <ftp://ftp.gnu.org/pub/gnu/sed>`__

Minimal SYStem (MSYS) installation
----------------------------------

http://prdownloads.sourceforge.net/mingw/MSYS-1.0.11-2004.04.30-1.exe

Perform a basic installation into C:\msys

Do not continue with the post install (this will be done later).

Update MSYS
-----------

Update MSYS to a more recent version

http://prdownloads.sourceforge.net/mingw/MSYS-1.0.11-20060807.tar.bz2

Extract the .tar.bz2 file, it contains the following files:

| ``mount.exe``
| ``msys-1.0.dll``
| ``ps.exe``

Copy the files to:

``C:\msys\bin``

This will overwrite/update the version(s) used in MSYS.

MSYS DTK (Developer Tool Kit)
-----------------------------

http://prdownloads.sourceforge.net/mingw/msysDTK-1.0.1.exe

Perform a basic installation into C:\msys

Updating BASH
-------------

http://prdownloads.sourceforge.net/mingw/bash-3.1-MSYS-1.0.11-snapshot.tar.bz2

Extract the .tar.bz2 file, in the bin subfolder it contains the following files:

| ``bash.exe``
| ``sh.exe``

Copy the files to:

``C:\msys\bin``

This will overwrite/update the sh.exe version used in MSYS

MinGW
-----

http://prdownloads.sourceforge.net/mingw/MinGW-5.0.3.exe

Select the download option.

Do not install with "Current" MinGW packages but select "Candidate".

Select the following components to install:

| ``MinGW base tools (autoselected)``
| ``g++ compiler``

Then installation will finish downloading automatically.

Run MinGW-5.0.3.exe again and select the download and install option to restart the installation.

Selet "Candidate" still and select the same components to install.

Perform the installation into the default destination:

``C:\msys\mingw``

The following versions (or possibly newer) of the candidate packages will be downloaded and installed:

| ``mingw-runtime-3.10.tar.gz``
| ``w32api-3.7.tar.gz``
| ``binutils-2.16.91-20060119-1.tar.gz``
| ``gcc-core-3.4.5-20060117-1.tar.gz``
| ``gcc-g++-3.4.5-20060117-1.tar.gz``

(It is also possible to get these packages seperately and extract them to C:\msys\mingw)

Configuring fstab
-----------------

The folder C:\msys\etc contains the following file:

``fstab.sample``

Copy the file to:

``fstab``

Open the file with a text editor and change the path value for the mingw mount point from:

``c:/mingw to c:/msys/mingw``

Save the file.

Starting MSYS
-------------

The first time MSYS is started, a "home" folder is created, for example:

``C:\msys\home\Administrator``

Installing additional packages
==============================

The following packages are required for building VLC

-  Wget
-  Iconv
-  Gettext
-  MinGW utils
-  Libtool
-  Autoconf
-  Automake
-  Zip
-  Coreutils

WGet
----

Wget is required for building from the "extras/contrib" or mingwPORT packages.

http://prdownloads.sourceforge.net/mingw/wget-1.9.1-mingwPORT.tar.bz2

Although this is a mingwPORT package it already has a precompiled wget on board.

Extract the .tar.bz2 file. It contains the following file in the bin subfolder:

``wget.exe``

Copy the file to:

``C:\msys\mingw\bin``

Iconv (GNU libiconv)
--------------------

http://prdownloads.sourceforge.net/mingw/libiconv-1.8.0-2003.02.01-1.exe

Perform a basic installation into the default destination Folder

``C:\msys\mingw``

Updating Iconv
~~~~~~~~~~~~~~

http://prdownloads.sourceforge.net/mingw/libiconv-1.10-mingwPORT.tar.bz2

Extract the .tar.bz2 file. Copy the contents into your home folder in MSYS

``C:\msys\home\Administrator (example)``

Start the MSYS shell and do the following commands:

``cd libiconv-1.10-mingwPORT/libiconv-1.10/mingwPORT``

``mkdir -p /usr/src/libiconv-1.10``

``./mingwPORT.sh ``

Follow the default installation.

If all went well all the appropriate libraries should be installed/built and placed into c:/msys/mingw/lib.

NOTE: For some unknown reason usage of Iconv fails when 1.10 is installed directly without having installed 1.8.0.

Gettext
-------

http://downloads.sourceforge.net/mingw/gettext-0.16.1-1-bin.tar.bz2 http://downloads.sourceforge.net/mingw/gettext-0.16.1-1-dll.tar.bz2

Untar both of these packets and copy the files in the subdirectories under gettext-0.16.1-1-bin/usr/local and gettext-0.16.1-1-dll/usr/local to the corresponding subdirectories under C:\msys\mingw. For example:

| ``      copy gettext-0.16.1-1-bin/usr/local/lib/*.* to  C:\msys\mingw\lib\``
| ``      copy gettext-0.16.1-1-dll/usr/local/bin/*.* to  C:\msys\mingw\bin\``
| ``     ......................................................``

Note:

``  The latest VLC from svn requires gettext-0.16.xx to build.``

MinGW Utils
-----------

The unix2dos tool from this package is required during the "make package" process of VLC for some conversion of txt files.

http://prdownloads.sourceforge.net/mingw/mingw-utils-0.3.tar.gz

Extract the .tar.gz file. it contains the following file in the bin subfolder:

``unix2dos.exe``

Copy the file to:

``C:\msys\mingw\bin``

Libtool
-------

http://prdownloads.sourceforge.net/mingw/libtool-1.5.22-mingwPORT.tar.bz2

Extract the .tar.bz2 file. Copy the contents into your home folder in MSYS

``C:\msys\home\Administrator (example)``

Start the MSYS shell and do the following commands:

``cd libtool-1.5.22-mingwPORT/libtool-1.5.22/mingwPORT``

``mkdir -p /usr/src/libtool-1.5.22``

``./mingwPORT.sh ``

Follow the default installation.

If all went well all the appropriate libraries should be installed/built and placed into c:/msys/mingw/lib.

Autoconf
--------

http://prdownloads.sourceforge.net/mingw/autoconf-2.59-mingwPORT.tar.bz2

Extract the .tar.bz2 file. Copy the contents into your home folder in MSYS

``C:\msys\home\Administrator (example)``

Start the MSYS shell and do the following commands:

``cd autoconf-2.59-mingwPORT/autoconf-2.59/mingwPORT``

``mkdir -p /usr/src/autoconf-2.59``

``./mingwPORT.sh ``

Follow the default installation.

If all went well all the appropriate libraries should be installed/built and placed into c:/msys/mingw/lib.

Updating autoconf from contrib
------------------------------

VLC 0.8.6 and later (including 0.9.0 svn/development) require an autoconf version of 2.60 or greater.

If during the configure process the following msg appears it's time to update:

``"Hey, your autoconf is quite old. Update it".``

Open your MSYS shell:

``cd vlc-trunk/extras/contrib``

``./bootstrap``

``cd src``

``make .autoconf``

Automake
--------

http://prdownloads.sourceforge.net/mingw/automake-1.9.5-mingwPORT.tar.bz2

Extract the .tar.bz2 file. Copy the contents into your home folder in MSYS

``C:\msys\home\Administrator (example)``

Start the MSYS shell and do the following commands:

``cd automake-1.9.5-mingwPORT/automake-1.9.5/mingwPORT``

``mkdir -p /usr/src/automake-1.9.5``

``./mingwPORT.sh ``

Follow the default installation.

If all went well all the appropriate libraries should be installed/built and placed into c:/msys/mingw/lib.

Zip
---

Zip is required for making .zip packages...

http://www.info-zip.org/

ftp://ftp.info-zip.org/pub/infozip/WIN32/zip232xN.zip

Extract the .zip. It contains the following file in the bin subfolder:

``zip.exe``

Copy the file to:

``C:\msys\bin``

Coreutils
---------

The whoami tool from this package is required for "svn builds".

http://prdownloads.sourceforge.net/mingw/coreutils-5.97-MSYS-1.0.11-snapshot.tar.bz2

Extract the .tar.bz2 file. it contains the following file in the bin subfolder:

``whoami.exe``

Copy the file to:

``C:\msys\mingw\bin``

Optional packages
=================

GDB (optional)
--------------

GDB is used for debugging purposes.

http://prdownloads.sourceforge.net/mingw/gdb-6.3-2.exe

Perform an installation into the folder

``C:\msys\mingw``

ZLib (optional)
---------------

Zlib is a required package in combination with the Gpac package for .avs and .mp4 output support when building the x264 library.

http://prdownloads.sourceforge.net/mingw/zlib-1.2.3-mingwPORT-1.tar.bz2

Extract the .tar.bz2 file. Copy the contents into your home folder in MSYS

``C:\msys\home\Administrator (example)``

Start the MSYS shell and do the following commands:

``cd zlib-1.2.3-mingwPORT/zlib-1.2.3/mingwPORT``

``mkdir -p /usr/src/zlib-1.2.3``

``./mingwPORT.sh ``

``Follow the default installation.``

If all went well all the appropriate libraries should be installed/built and placed into c:/msys/mingw.

Updating SDL from mingwPORT (optional)
--------------------------------------

SDL support is required when building ffplay from the FFmpeg package.

http://prdownloads.sourceforge.net/mingw/SDL-1.2.8-mingwPORT.tar.bz2

Extract the .tar.bz2 file. Copy the contents into your home folder in MSYS

``C:\msys\home\SDL-1.2.8-mingwPORT (example)``

Start the MSYS shell and do the following commands:

``cd SDL-1.2.8-minwPORT/SDL-1.2.8/mingwPORT``

``mkdir -p /usr/src/SDL-1.2.8``

``./mingwPORT.sh ``

Follow the default installation.

If all went well all the appropriate libraries should be installed/built and placed into /usr/local/lib.

Updating SDL (optional)
~~~~~~~~~~~~~~~~~~~~~~~

http://www.libsdl.org/release/SDL-1.2.11.tar.gz

Extract the .tar.gz file. Copy the contents into your home folder in MSYS

``C:\msys\home\SDL-1.2.11 (example)``

Start the MSYS shell and do the following commands:

``cd SDL-1.2.11``

``./configure``

``make``

``make install``

If all went well all the appropriate libraries should be installed/built and placed into /usr/local/lib.

Nasm (optional)
---------------

The Netwide assembler (nasm) is required for building the x264 library.

http://sourceforge.net/project/showfiles.php?group_id=6208

Download the latest win32 binaries:

http://prdownloads.sourceforge.net/nasm/nasm-0.98.39-win32.zip?download

Extract the .zip. It contains the following file in the bin subfolder:

``nasmw.exe``

Rename the file to nasm.exe and copy it to the following location:

``C:\msys\mingw\bin``

GPAC (optional)
---------------

GPAC is required for building the x264 library with mp4 output support.

Start the MSYS shell and do the following commands:

``cvs -z3 -d:pserver:anonymous@gpac.cvs.sourceforge.net:/cvsroot/gpac co -P gpac``

This will download the latest GPAC version from CVS.

``cd gpac``

``./configure``

``make install-lib``

TODO: copy GPAC files to appropriate folder automagically.

x264 (optional)
---------------

Start the MSYS shell and do the following commands:

``svn co ``\ ```svn://svn.videolan.org/x264/trunk`` <svn://svn.videolan.org/x264/trunk>`__\ `` x264-trunk``

``cd x264-trunk``

For generic purposes:

``./configure``

``make``

For VLC:

``./configure --prefix=/usr/win32``

``make``

``make install``

This will copy the appropriate libs and .h to the prefix folder which will also be used by VLC for building the contrib

For compiling "stand-alone with mp4 output support" (this requires GPAC):

``./configure --enable-mp4-output``

``make``

If you wish to compile FFmpeg stand-alone with x264 support then also do this

``make install``

This will copy the appropriate libs and .h files to the default /usr/lib and /usr/include

FFmpeg (optional)
-----------------

Start the MSYS shell and do the following commands:

``svn co ``\ ```svn://svn.mplayerhq.hu/ffmpeg/trunk`` <svn://svn.mplayerhq.hu/ffmpeg/trunk>`__\ `` ffmpeg-trunk``

``cd ffmpeg-trunk``

For generic purposes:

| ``./configure --enable-mingw32 --enable-memalign-hack \``
| ``   --enable-gpl --enable-pp``

``make``

For compiling with x264 support:

(This assumes you did a "make install" for x264 which will have copied the appropriate lib and .h files into lib/include).

| ``./configure --enable-mingw32 --enable-memalign-hack \``
| ``   --extra-cflags=-I/usr/local/include \``
| ``   --extra-ldflags=-L/usr/local/lib \``
| ``   --enable-gpl --enable-pp --enable-x264``

``make``

For compiling into VLC:

(This does not need x264 lib in FFmpeg since VLC uses that directly, also prefix and extra flags are used to point to the "contrib" folder):

| ``./configure --enable-mingw32 --enable-memalign-hack \``
| ``   --extra-cflags=-I/usr/win32/include \``
| ``   --extra-ldflags=-L/usr/win32/lib \``
| ``   --prefix=/usr/win32 \``
| ``   --enable-faac --enable-mp3lame --enable-gpl --enable-pp``

``make``

``make install-libs install-headers``

This will copy all the appropriate libs and .h files into usr/win32/include and lib so they can be used by VLC compilation.

FAQ
===

Various troubleshooting issues..

Make .qt4 from extras/contrib
-----------------------------

Fails on:

| ``checking for libmpeg2.a in /home/Administrator/vlc-trunk/./extras/contrib/src/mpeg2dec... no``
| ``configure: error: cannot cd to /home/Administrator/vlc-trunk/./extras/contrib/src/mpeg2dec``

Workaround: configure with

``--without-contrib``

Make package-win32-zip
----------------------

Fails on:

| ``sed -i 's%share/osdmenu%osdmenu%g' ./vlc-0.9.0-svn/osdmenu/*.cfg``
| ``sed: invalid option -- i``

Workaround: compile sed 4.09 (any newer versions fail to compile on missing alloca)

ftp://ftp.gnu.org/pub/gnu/sed/sed-4.0.9.tar.gz

use the newer sed version in c:\msys\mingw\bin and rename the old one to sed3.exe or something

ONLY use the 4.09 sed to do a make package-win32-zip, it will fail to compile VLC source (so after it finishes, you have to copy the old version back again).

So in conclusion:

| ``make package-win32-zip fails with sed 3.02 on -i``
| ``make autoconf fails with sed 4.09 on -E``
| ``sed 4.10+ requires glib``
| ``glib requires pkgconfig but pkgconfig requires glib?!``

Warnings during configure
-------------------------

Using contrib from 20061015 still a lot of warnings during configure:

| ``checking dynamic linker characteristics... ./configure: line 14697: f77: command not found``
| ``./configure: line 14825: f77: command not found``

| ``configure: WARNING: libshout library not found``
| ``configure: WARNING: MusicBrainz library not found``
| ``configure: WARNING: CD Reading and information library not found``
| ``configure: WARNING: VCD information library not found``
| ``configure: WARNING: new enough libcddb not found. CDDB access disabled``

| ``checking for mpcdec/mpcdec.h... yes``
| ``configure: WARNING: only static linking is available, you must provide a gme-tree``

``./configure: line 54814: --exists: command not found``

| ``configure: WARNING: Probe disc disabled because ok libcdio library not found``
| ``configure: WARNING: VCD information on Probe disc disabled because ok``
| ``libvcdinfo not found``
| ``configure: WARNING: QT4 library not found``
| ``configure: WARNING: DAAP library not found``
| ``configure: WARNING: avahi-client library not found``

Can not write to output file with unix2dos
------------------------------------------

| ``unix2dos: converting file ./vlc-0.9.0-svn/AUTHORS.txt to DOS format ...``
| ``unix2dos: can not write to output file``
| ``unix2dos: problems converting file ./vlc-0.9.0-svn/AUTHORS.txt``
| ``unix2dos: converting file ./vlc-0.9.0-svn/MAINTAINERS.txt to DOS format ...``
| ``unix2dos: converting file ./vlc-0.9.0-svn/THANKS.txt to DOS format ...``
| ``unix2dos: can not write to output file``

Workaround: Load file in emacs and do

`` M-x set-buffer-file-coding-system RET undecided-dos``

or

`` C-x RET f undecided-dos``

and then save the file (C-x C-s)

Version
=======

-  20060926 Initial version
-  20060928 Reworked layout
-  20061011 Added troubleshooting section
-  20061119 Added FFmpeg and x264. Removed unicode warning from troubleshooting
-  20070113 WIKI version

`Category:Building <Category:Building>`__ `Category:Windows <Category:Windows>`__
