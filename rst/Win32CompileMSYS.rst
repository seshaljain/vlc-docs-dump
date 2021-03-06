Introduction
============

`MSys2 <http://sourceforge.net/projects/msys2/>`__ is a helper environment for MinGW, the compiler chain for Windows based on GCC.

It can build VLC natively on Microsoft Windows. However, VideoLAN developers **strongly recommend** `cross-compiling VLC from Linux <Win32Compile>`__, which is faster and easier. If you decide to stick to the MSYS method, you are on your own. Should you encounter any problem and ask for help, expect to be told to cross-compile.

Either way, VLC is a complex program with many dependencies, most of which are obtained/built through the command line interface. Therefore, experience with the POSIX command line (i.e. the *Unix shell*) is **required**. Time, patience and persistence are indispensable. The entire process outlined below should take at the very least 4 hours. Experience show that mistakes are common, especially with beginners, so you might need to make multiple attempts.

Install Windows tools
=====================

Text editor
-----------

To edit unix-style text documents you need a suitable editor: Notepad is not enough.

-  Use `notepad2 <http://sourceforge.net/projects/notepad2/>`__. You can set File - Line endings - Default to "Unix (LF)", but it always saves opened files in the ending style they have.

-  Or use `notepad++ <http://notepad-plus-plus.org/>`__.

Unzip Utility (7-zip)
---------------------

Files to downloaded will have to be uncompressed. Some of them use Unix originated formats (.tar.gz, .tar.bz2, .tar.lzma), you will then need a versatile unzipping utility.

A recent version of `7-zip <http://www.7-zip.org/>`__ is therefore strongly advised.

Install MSys2 and GCC
=====================

Install MSys2 from http://msys2.github.io/

We recommend to use the 32bits version.

Let the default, and run the command line.

Tools
-----

Install the autotools suite:

`` pacman -S git subversion cvs automake autoconf libtool m4 make gettext pkg-config mingw-w64-i686-lua findutils  mingw-w64-i686-headers yasm patch``

gcc
~~~

Download gcc from: `mingw-w64 <http://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/4.9.2/threads-win32/sjlj/i686-4.9.2-release-win32-sjlj-rt_v3-rev0.7z/download>`__.

Unzip it to C:\MSys2\\

Restart
~~~~~~~

**Exit MSys2, run autorebase.bat and re-run MSys2 from mingw32_shell.bat**

Check GCC
---------

Run

``gcc -v``

And check that it says

| ``Thread model: win32``
| ``gcc version 4.9.2 (i686-win32-sjlj-rev0, Built by MinGW-W64 project)``

Get VLC sources
===============

Git
---

\ **YOU MUST** keep the native line-endings of the repo.

``git config core.autocrlf=false``

Clone the git repo

``git clone ``\ ```git://git.videolan.org/vlc.git`` <git://git.videolan.org/vlc.git>`__

**Nota Bene:** ensure your Windows user name does not contain spaces so that the cloning folder of VLC will not not have spaces in it.

Get precompiled 3rd party libraries
===================================

| ``cd vlc/contrib``
| ``mkdir win32 && cd win32``
| ``../bootstrap --build=i686-w64-mingw32``
| ``make prebuilt``

**Note:** check that all is well with moc -v

Build VLC
=========

Bootstrap
---------

In VLC root folder, do:

``./bootstrap``

Configure
---------

| ``mkdir win32``
| ``cd win32``
| ``sh ../extras/package/win32/configure.sh --host=i686-w64-mingw32 --disable-nls``

**Note:** If you want any custom options, like "--disable-lua" or anything of that nature, you can append them.

Make (compile)
--------------

``make -j4``

**Note:** If your <username> starts with the "u" or "x" character, change C:\MSys\1.0\home\<username>\config.h and double all backslashes in VLC_COMPILED_BY constant.

Create packages
===============

Run VLC
-------

Once the compilation is done, build self-contained VLC packages with one of the following "make" commands:

``make package-win-common``

This will create a subdirectory named vlc-x.x.x with all the binaries with debugging symbols. You can run ./vlc.exe from there.

Create proper packages
----------------------

``make package-win32-zip``

(Same as above but will package the directory in a zip file).

``make package-win32-exe``

(Same as above but will also create an auto-installer package. You will need to have NSIS installed in its default location for this to work).

Troubleshooting
===============

See `Win32CompileMSYSTroubleShooting <Win32CompileMSYSTroubleShooting>`__.

Acknowledgements
----------------

This howto was re-created by `Jean-Baptiste Kempf <User:J-b>`__ and updated in June 2009, September 2009, December 2009 and March 2010.

It was updated in June 2010 by Vicne with the help of J-b, gnosygnu and MichaelMc

It was updated in July 2012 by gnosygnu. Note that there are several new notes in `Win32CompileMSYSTroubleShooting <Win32CompileMSYSTroubleShooting>`__. These reflect problems that were encountered on gnosygnu's setup (Windows XP SP3). Refer to this `forum thread <http://forum.videolan.org/viewtopic.php?f=32&t=102843&sid=f58967215a83981dda030ff6efa3d493>`__ for more information.

This howto was re-re-created by `Jean-Baptiste Kempf <User:J-b>`__ in September 2012 and updated until 2015, with MSys2

See also
========

-  `Win32CompileMSYSOld <Win32CompileMSYSOld>`__ - deprecated documentation

`Category:Building <Category:Building>`__ `Category:Windows <Category:Windows>`__
