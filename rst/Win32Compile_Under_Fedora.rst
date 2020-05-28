Building Methods
----------------

From a Fedora 64-bit install, you have two basic approaches if you want to build VLC from source.

=================================================== ======================================================
Method                                              Notes
=================================================== ======================================================
| **Cross-compile with Mingw** in a virtual machine **Preferred** method that works "out of the box".
| using 32-bit Ubuntu.                             
**Cross-compile with Mingw** under Fedora.          Produces some anomalies and requires some workarounds.
=================================================== ======================================================

Using a virtual machine
-----------------------

Virtual Box is known to work for this approach. Other virtual machines might work as well, but are untested.

::

   sudo yum install VirtualBox-OSE

The basic Win32Compile is optimized for Ubuntu. It is simpler if you install the 32-bit version:

::

   wget http://www.ubuntu.com/start-download?distro=desktop&bits=32&release=latest

Create and attach the disk drives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start the VirtualBox Manager GUI.

-  Click on Machine / New... The "New Virtual Machine Wizard" will open.
-  Click Next. Enter Ubuntu32 in the Name box.
-  Change Base Memory Size to 1024MB (for better performance).
-  Leave Start-up Disk box checked. Leave Create new hard disk radio button active.
-  Choose VDI file type.
-  Choose Dynamically allocated
-  Choose Location Ubuntu32 and Size 8.00 GB
-  Click "Create". This will exit the Wizard.
-  Click "Create" again. This will create the virtual machine.
-  Click Settings / Storage. The SATA Controller should show that Ubuntu32.vdi (your 8GB disk) is attached. The IDE Controller should show an empty attachment. Click on the Empty line. The Attributes label in the last column should read "CD/DVD Drive:" with a dropdown reading "IDE Secondary". To the right of that is a CD symbol. Click on that.
-  Click on "Choose a virtual CD/DVD disk file..."
-  Navigate to the Ubuntu server you just downloaded. Click Open. Your CD should now be attached to the IDE Controller. Click OK.
-  Click on Start.

At this point, the virtual machine should boot and take you through the Ubuntu installation process. When it is complete, it will ask you to remove the CD and reboot.

Remove the virtual CD and reboot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Click on Machine / Close ...
-  Choose Power off the machine and click OK.
-  Click on Settings / Storage
-  Click on the Ubuntu CD attached to the IDE Controller
-  Click on the CD symbol at the extreme right of the Attributes section.
-  Choose Remove disk from virtual drive. Click OK
-  Click on Start.

Now Ubuntu should start. From here you can follow the instructions on the main `Win32Compile <Win32Compile>`__ page.

Using Fedora
------------

If you are using Fedora 13, you might want to visit the `Win32CompileFedora13 <Win32CompileFedora13>`__ page.

This page has been tested for compiling for `Windows <Windows>`__ under 64-bit Fedora 16. There are a few complications, as noted below.

Get the basics
~~~~~~~~~~~~~~

The mingw32 cross-compile tools are available in the default repository.

::

   sudo yum install \
   mingw32-gcc-c++ \
   mingw32-gcc \
   mingw32-pthreads \
   mingw32-w32api \
   mingw32-binutils \
   mingw32-runtime \
   mingw32-filesystem \
   mingw32-cpp \
   mingw32-dlfcn-static

You'll also need several other packages for the build process.

::

   sudo yum install \
   libtool \
   automake \
   autoconf \
   autopoint \
   make \
   gettext \
   pkg-config \
   git \
   subversion \
   dos2unix

Next, change to a directory you will use for building. You must have write access to this directory. Then use git to get the source:

::

   git clone git://git.videolan.org/vlc.git

This will give you the VLC trunk. Alternative branches (technically forks) are listed at the `VLC Git repository <http://git.videolan.org>`__. Scroll down to the ``vlc.git`` line and click on the `forks <http://git.videolan.org/?p=vlc.git;a=forks>`__ link at the extreme right. This will give you a list of alternatives, which are in the vlc directory. So, for example, to choose the 2.0 fork, the command is:

::

   git clone git://git.videolan.org/vlc/vlc-2.0.git

Next, change into the newly installed ``vlc-x.x`` directory. We will refer to this as the ``$VLCROOT`` directory:

::

   cd vlc-*
   export VLCROOT=`pwd`

Prepare `3rd party libraries <Contrib_Status>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before compiling VLC, you need lots of other libraries.

First, set an environment variable for your current "host" system for cross-compiling. This is because the contributed libraries are always maintained under the directory ``i586-mingw32msvc``, while Fedora typically is looking for them as ``i686-pc-mingw32``.

::

   export FEDORA_HOST=`rpm -ql mingw32-filesystem|grep -m1 lib|cut -d/ -f3`

You also need to set two environment variables for ``pkg-config``. This is because the current Fedora MinGW ``pkg-config`` is broken, and you need to tell the native one where to find the contribs.

::

   export PKG_CONFIG_LIBDIR=../contrib/${FEDORA_HOST}/lib/pkgconfig 
   export PKG_CONFIG=/usr/bin/pkg-config

Finally, download the "prebuilt" contributions and create a symbolic link.

::

   mkdir -p contrib/win32
   cd contrib/win32
   ../bootstrap --host=i586-mingw32msvc
   make prebuilt
   cd ..  
   ln -s i586-mingw32msvc ${FEDORA_HOST}

Install 32-bit Lua
~~~~~~~~~~~~~~~~~~

To get the 32-bit compiled Lua files needed by 32-bit VLC, you need the 32-bit Lua byte compiler. (The 64-bit version produces 64-bit files and does not currently have an option to produce 32-bit files.)

By default, you will already have 64-bit Lua installed, because the Yum/RPM packaging system depends on it. As a result, you will not be able to remove the 64-bit version. Furthermore, Yum will install the 32-bit binary libraries, but it will NOT install the 32-bit binary executables (``lua`` and ``luac``) over the 64-bit ones. Here is how to work around that.

::

   sudo yum install compat-readline5.i686 
   yumdownloader lua.i686
   sudo yum localinstall ./lua*.rpm

This installs the 32-bit libraries but not the executables. You have to manually extract and install the 32-bit versions.

::

   sudo yum install cpio
   rpm2cpio lua*.rpm | cpio -idmv

Now you will have the files from the RPM package as a tree in your local directory. They have the same names and (relative) locations as the 64-bit versions, which is why Yum refused to install them in the first place. So manually install them with the names ``lua32`` and ``luac32`` and get rid of your detritus.

::

   sudo mv usr/bin/lua /usr/bin/lua32
   sudo mv usr/bin/luac /usr/bin/luac32
   rm -rf usr
   rm -f lua*.rpm

Tell the build system where to find the 32-bit versions.

::

   export LUA=/usr/bin/lua32
   export LUAC=/usr/bin/luac32

Install Qt and correct any version mismatch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install the ``qt-devel`` package, which gives you ``moc``, ``uic`` and ``rcc`` for both Qt3 and Qt4. The executables for Qt4 are named ``moc-qt4``, ``uic-qt4`` and ``rcc``, so these need fixing.

::

   sudo yum install qt-devel
   sudo ln -s /usr/bin/moc-qt4 /usr/local/bin/moc
   sudo ln -s /usr/bin/uic-qt4 /usr/local/bin/uic

Your version of ``moc`` needs to match the version used in the contribs. Here's how to see what you've got:

::

   $ moc -v
   Qt Meta Object Compiler version 63 (Qt 4.8.0)
   $ grep "define Q_MOC" ${VLCROOT}/contrib/i586-mingw32msvc/include/qt4/src/corelib/kernel/qobjectdefs.h
   #define Q_MOC_OUTPUT_REVISION 62

In this case, the installed ``moc`` has a version of 63 (from Qt 4.8), but the contribs were built with version 62 (from Qt 4.7). To fix this:

::

   cd ${VLCROOT}/contrib/win32
   wget http://johnfreed.com/vlc/contrib/moc-`moc -v 2>&1|cut -d' ' -f6`.tar.bz2
   tar xjvf moc-`moc -v 2>&1|cut -d' ' -f6`.tar.bz2 -C ../

Finally, you need to delete the executables supplied by the contribs.

::

   rm -f ${VLCROOT}/contrib/i586-mingw32msvc/bin/moc contrib/i586-mingw32msvc/bin/uic contrib/i586-mingw32msvc/bin/rcc

Set the environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add the environment variables mentioned above to your ``~/.bash_profile`` file. This will set them every time you start up a terminal. However, you might not want to override your normal variables. In that case, the following method will work.

-  Copy your ``~/.bash_profile`` file to one called ``~/.mingw_profile``
-  Edit ``~/.mingw_profile`` to add these lines:

::

   export FEDORA_HOST=`rpm -ql mingw32-filesystem|grep -m1 lib|cut -d/ -f3`
   export PKG_CONFIG_LIBDIR=../contrib/${FEDORA_HOST}/lib/pkgconfig 
   export PKG_CONFIG=/usr/bin/pkg-config
   export LUA=/usr/bin/lua32
   export LUAC=/usr/bin/luac32

Now, to set those variables after you start a terminal:

::

   exec bash --rcfile ~/.mingw_profile

Bootstrap
~~~~~~~~~

Prepare the tree:

::

   cd $VLCROOT
   ./bootstrap

The build needs two extra DLLs that Fedora keeps in places it doesn't expect. So create symlinks to solve that:

::

   export MINGWDLLPATH=`${FEDORA_HOST}-g++ -v /dev/null 2>&1 | grep ^LIBRARY_PATH|cut -d= -f2|cut -d: -f1`
   sudo ln -s /usr/${FEDORA_HOST}/sys-root/mingw/bin/libgcc_s_sjlj-1.dll $MINGWDLLPATH
   sudo ln -s /usr/${FEDORA_HOST}/sys-root/mingw/bin/libstdc++-6.dll $MINGWDLLPATH

Configure
~~~~~~~~~

Then you can to configure the build with the ``./configure`` script. You will probably want to add the ``--enable-dvbpsi`` option in addition to the standard ones.

::

   mkdir win32 && cd win32
   ../extras/package/win32/configure.sh --enable-dvbpsi --host=${FEDORA_HOST}

Alternatively, you can run configure manually. There are a large number of options. See ``'../configure --help'`` for more information.

::

    
   ../configure --enable-dvbpsi --host=${FEDORA_HOST} \
         --enable-update-check \
         --enable-lua \
         --enable-faad \
         --enable-flac \
         --enable-theora \
         --enable-twolame \
         --enable-quicktime \
         --enable-avcodec --enable-merge-ffmpeg \
         --enable-dca \
         --enable-mpc \
         --enable-libass \
         --enable-x264 \
         --enable-schroedinger \
         --enable-realrtsp \
         --enable-live555 \
         --enable-dvdread \
         --enable-shout \
         --enable-goom \
         --enable-caca \
         --disable-portaudio \
         --disable-sdl \
         --enable-qt4 \
         --enable-skins2 \
         --enable-sse --enable-mmx \
         --enable-libcddb \
         --enable-zvbi --disable-telx \
         --enable-sqlite \
         --disable-dirac

Build VLC
~~~~~~~~~

Once configured, to build VLC, just run:

::

   make

Package VLC
~~~~~~~~~~~

Once the compilation is done, you can build self-contained VLC packages.

Depending on what type of package you want, you may also need the *zip*, *7zip*, or *nsis* tools. All three sets are needed for the ``make package-win`` target.

::

   sudo yum install \
   zip \
   p7zip \
   mingw32-nsiswrapper mingw32-nsis 

Use the following ``make`` rules:

=========================== ========================================================================================================================
Command                     Description
=========================== ========================================================================================================================
``make package-win-common`` Creates a subdirectory named ``vlc-x.x.x`` with all the binaries. You can run VLC directly from this directory.
``make package-win32-7zip`` Same as ``common`` but will also package the directory in a 7z file. (Needs ``p7zip``.)
``make package-win32-zip``  Same as ``common`` but will also package the directory in a zip file. (Needs ``zip``.)
``make package-win32-exe``  Same as ``common`` but will also create an auto-installer package. (Needs ``mingw32-nsiswrapper`` and ``mingw32-nsis``.)
``make package-win32-xpi``  Creates the web plugin.
``make package-win32``      Creates all of the above.
``make package-win-debug``  Same as ``make package-win32`` but the binaries are usable with a debugger.
=========================== ========================================================================================================================

**Well done—you're ready to use VLC!**

`Category:Building <Category:Building>`__ `Category:GNU/Linux <Category:GNU/Linux>`__ `Category:Windows <Category:Windows>`__
