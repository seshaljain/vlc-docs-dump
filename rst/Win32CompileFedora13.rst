Win32Compile on Fedora 13 (This document is based on `Win32Compile <Win32Compile>`__): this page give some further details for building VLC on a **Fedora 13** Linux distribution with the **Mingw32** cross-compilation tools. Get more informations on:

-  `Fedora <http://fedoraproject.org/>`__
-  `Mingw <http://www.mingw.org/>`__
-  `MingW Fedora Project <http://fedoraproject.org/wiki/SIGs/MinGW>`__

Building VLC from source
------------------------

======================================= ==================== =============================================
Method                                  Documentation        Notes
======================================= ==================== =============================================
Cross-compile with Mingw32 on Fedora 13 None: read this page **Preferred** method (uses cross compilation)
======================================= ==================== =============================================

Obtaining the build tools
-------------------------

The mingw32 cross-compile tools are available in the default repository. Install them (as root) with yum:

::

   sudo yum --verbose --noplugins install \
   mingw32-gcc-c++ \
   mingw32-gcc \
   mingw32-pthreads \
   mingw32-w32api \
   mingw32-binutils \
   mingw32-runtime \
   mingw32-filesystem \
   mingw32-cpp \
   mingw32-dlfcn-static

You may also add the ndis tools and everything needed by the ``make package-win32*`` targets:

::

   sudo yum --verbose --noplugins install \
   mingw32-nsiswrapper \
   mingw32-nsis \
   zip \
   p7zip \ 
   lua

To make 7zip work, add a symlink:

::

   sudo ln -s /usr/bin/7za /usr/win32/bin/7z

Add */usr/win32/bin* to your 'PATH' (best to add this to your ~/.bash_profile file to make it permanent):

::

   export PATH=$PATH:/usr/win32/bin

NOTE: On my Fedora 16 system, mingw binaries are in /usr/i686-pc-mingw32/bin/:

::

   sudo ln -s /usr/bin/7za /usr/i686-pc-mingw32/bin/7z
   export PATH=$PATH:/usr/i686-pc-mingw32/bin

You also need the Fedora qt-devel package, even if you are using Linux to cross-compile to a Windows exe (for moc and uic):

::

   sudo yum install qt-devel

Note: pre-built Windows Qt is 4.6.0 but the yum installed version for Linux is actually 4.6.3... *If it is problematic* try to downgrade the qt installed versions:

::

   sudo yum downgrade qt*-4.6.0

Be sure that you have *pkg-config* installed (check with ``yum info installed pkgconfig``) as the installed */usr/bin/i686-pc-mingw32-pkg-config* is not working correctly.

Saving time by using pre-built libraries
----------------------------------------

For QT4 you will need (to ease the compilation) to add some links in '/usr/win32/bin' (or /usr/i686-pc-mingw32/bin):

::

   cd /usr/win32/bin
   sudo ln -s /usr/bin/moc-qt4 .
   sudo ln -s /usr/bin/uic-qt4 .
   sudo ln -s /usr/bin/rcc .

Note: The rest of this section may be out of date; see `Win32Compile <Win32Compile>`__ section under Prepare 3rd party libraries. You will need to export the shell environment variable

::

   export PKG_CONFIG_LIBDIR=../contrib/i686-pc-mingw32/lib/pkgconfig

.

Note: for contrib-xxxxxxx-win32-bin-gcc-4.4.2-runtime-3.17-only.tar.bz2 you need to install **mingw32-runtime-3.17**

If you want to save yourself time and energy by using the pre-built versions of these libraries, you may download them from http://people.videolan.org/~jb/Contribs/, the version you download must match that of the MINGW compiler.

For the installed mingw32 packages the available versions are: http://people.videolan.org/~jb/Contribs/contrib-xxxxxxx-win32-bin-gcc-4.4.2-runtime-3.15-only.tar.bz2, where xxxxx is a date

Install this (as root) with:

``tar jxf contrib-xxxxxxx-win32-bin-gcc-4.4.2-runtime-3.15-only.tar.bz2 -C /``

Note the ``-C /``!

A pre-version is actually available here: http://rpmfarm.free.fr/13/i386/RPMS.farm/mingw32-runtime-3.17-1.EL.fc13.noarch.rpm

Note: previous contrib tarball is missing some files: /usr/win32/include/mpcdec/config_win32.h

A temporary version is available here: http://rpmfarm.free.fr/src/Patches/VLC/mpcdec_config_win32.h

Configuring the build
---------------------

First prepare the build process in the vlc tree (fetched via git - See `Git#Getting_VLC_or_x264_source_code_via_Git <Git#Getting_VLC_or_x264_source_code_via_Git>`__) by doing:

::

   cd vlc
   ./bootstrap

Once you've got all the files you need in place and the bootstap is done, you need to configure the build with the following configure script (created in *extras/package/win32* and named *configure-mingw-f13.sh*). In the following examples, assume that the third-party libraries are installed as above:

::

       +----------------------------------------------------------------------------------
       | #!/bin/sh
       | 
       | root=$(echo $0|sed 's#extras/package/win32/configure-mingw-fr13.sh##')./
       | 
       | if [ -n "$1" ]
       | then
       |         CONTRIBS="$1"
       | else
       |         CONTRIBS="/usr/win32"
       | fi
       | export CONTRIBS
       | 
       | PATH="$CONTRIBS/bin:$PATH" \
       | PKG_CONFIG=/usr/bin/pkg-config \
       | PKG_CONFIG_LIBDIR=$CONTRIBS/lib/pkgconfig \
       | CPPFLAGS="-I$CONTRIBS/include -I$CONTRIBS/include/ebml" \
       | LDFLAGS="-L$CONTRIBS/lib" \
       | CC=i686-pc-mingw32-gcc CXX=i686-pc-mingw32-g++ \
       | CONFIG="${root}configure --host=i686-pc-mingw32 --build=i386-linux
       | --enable-dirac --enable-mkv --enable-taglib --enable-nls --enable-projectm" \
       | sh ${root}extras/package/win32/configure-common.sh
       +----------------------------------------------------------------------------------

See ``./configure --help`` for more information.

Building VLC
------------

Once configured, to build VLC, just run ``make``.

Note: you may need ``make MOC=/usr/bin/moc-qt4 UIC=/usr/bin/uic-qt4`` in modules/gui/qt4) if you haven't done the links.

Once the compilation is done, you can either run VLC directly from the source tree or you can build self-contained VLC packages with the following make rules:

=========================== ====================================================================================================================================
Command                     Description
=========================== ====================================================================================================================================
``make package-win32-base`` Creates a subdirectory named ``vlc-x.x.x`` with all the binaries 'stripped' (that is, smallest size, unusable with a debugger)
``make package-win32-zip``  Same as above but will package the directory in a zip file.
``make package-win32``      Same as above but will also create an auto-installer package. You must have NSIS installed in its default location for this to work.
=========================== ====================================================================================================================================

Notes: You'll need to add */usr/win32/bin* to the path and as you used MinGW, you need to copy the mingw *libgcc_s_sjlj-1.dll* into the installation folder near *vlc.exe* (you'll find the dll on your system as you installed the mingw packages): ``cp /usr/i686-pc-mingw32/sys-root/mingw/bin/libgcc_s_sjlj-1.dll vlc-``\ \ ``/``

**Well done—you're ready to use VLC!**

`Category:Building <Category:Building>`__ `Category:GNU/Linux <Category:GNU/Linux>`__ `Category:Windows <Category:Windows>`__
