This page will help you to compile for `Windows <Windows>`__.

Building Methods
----------------

If you want to build VLC from source, you have several choices:

================================================ ====================================================== ================================================================================================================================================================================================
Method                                           Documentation                                          Notes
================================================ ====================================================== ================================================================================================================================================================================================
**MinGW on Linux**                               `Obtaining the toolchain <#Obtaining_the_toolchain>`__ **Preferred** method involving cross-compilation from Linux. On computers running Microsoft Windows, a virtual machine is necessary to run Linux.
`MSYS+MinGW <http://www.mingw.org>`__ on Windows `Compile with MSys <Win32CompileMSYS>`__               **Native** compilation method. MSYS is a minimal build environment to compile Unix-style projects directly on Microsoft Windows. This is **not officially supported** by VideoLAN. Best of luck.
**Cygwin** on Windows                            `Compile with Cygwin <Win32CompileCygwinNew>`__        Cygwin method. Cygwin emulates a POSIX environment to compile on Microsoft Windows. This is **error**-prone and **slow** and therefore not recommended.
================================================ ====================================================== ================================================================================================================================================================================================

Obtaining the cross-compilation toolchain
-----------------------------------------

All this howto is focused on **Debian/Ubuntu**. For other distribution, please find the related package names, but they should be very similar.

**Ubuntu 14.04** is too old to compile VLC.

Host triplet
~~~~~~~~~~~~

A number of commands below include the toolchain identifier, called the *host triplet*.

This value is **essential**: it instructs the build system to use the correct toolchain and compile the program for Windows. Without the value, the build system will perform a native compilation for Linux (or whatever your computer runs). With an incorrect value, the build will fail.

The exact value depends on your installation of the toolchain.

Notably on Debian/Ubuntu, these values must be used:

-  *i686-w64-mingw32* for Windows 32-bits, using the Mingw-w64 toolchain
-  *x86_64-w64-mingw32* for Windows 64-bits, using the Mingw-w64 toolchain

Please make sure that you replace the keywords *HOST-TRIPLET* with either *i686-w64-mingw32* or *x86_64-w64-mingw32* adapted to your target Windows version (32-bit or 64-bit, respectively)

Compiler and binary toolchain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mingw-w64
^^^^^^^^^

To compile VLC for Windows (32-bits or 64-bits), the Mingw-w64 toolchain is required:

For the 32-bit version, run this:

\ `` apt-get install gcc-mingw-w64-i686 g++-mingw-w64-i686 mingw-w64-tools``

For the 64-bit version, this becomes:

\ `` apt-get install gcc-mingw-w64-x86-64 g++-mingw-w64-x86-64 mingw-w64-tools``

**NB:** you need mingw-w64 version 5.0.1 to compile it.

Development tools
~~~~~~~~~~~~~~~~~

You will also need:

-  lua (5.2)
-  all autotools: libtool, automake, autoconf, autopoint, make, gettext, pkg-config
-  qt4-dev-tools, qt5-default (or qt4-default if qt plugin build fails)
-  git, subversion cmake, cvs if you want to rebuild contribs
-  wine-dev for creating Win32 packages
-  zip [for creating .zip package], p7zip [for .7z package], nsis [for .exe auto-installer], bzip2 [for 'make prebuild]

**Run:**

| \ `` apt-get install lua5.2 libtool automake autoconf autopoint make gettext pkg-config``
| \ `` apt-get install qt4-dev-tools qt5-default git subversion cmake cvs ``
| \ `` apt-get install wine64-development-tools libwine-dev zip p7zip nsis bzip2``
| \ `` apt-get install yasm ragel ant default-jdk protobuf-compiler dos2unix``

Get the source code
-------------------

``{{$}} git clone ``\ ```http://git.videolan.org/git/vlc.git`` <http://git.videolan.org/git/vlc.git>`__\ `` vlc``

See `Git <Git>`__ for more information.

Go into the VLC directory
-------------------------

``{{$}} cd vlc``

Prepare `3rd party libraries <Contrib_Status>`__
------------------------------------------------

VLC depends on a sizable number of third party libraries. Before compiling VLC, you need to obtain compiled versions of those. There are two ways to achieve that:

-  The *prebuilt* approach is much faster and easier, but only works with a narrow set of VLC versions.
-  The *manual build* approach takes a lot of time and disk space, and somewhat error-prone.

Please note that the prebuilt library versions are intended for the latest current *stable release* of VLC. It is not compatible with old VLC versions, nor with newer or future versions.

At the time of writing (late 2016), the prebuilt libraries work with VLC 2.2.x **only**. To compile the VLC 3.0.x development branch, **DO NOT USE** the prebuilt libraries.

Prebuilt (fast)
~~~~~~~~~~~~~~~

| `` {{$}} mkdir -p contrib/win32``
| `` {{$}} cd contrib/win32``
| `` {{$}} ../bootstrap --host=HOST-TRIPLET``
| `` {{$}} make prebuilt``

Manually built (slow)
~~~~~~~~~~~~~~~~~~~~~

Or, if you want to compile the contribs yourself and are feeling adventurous and have lots of time to burn:

`` ``\ \ `` apt-get install subversion yasm cvs cmake ragel autopoint``

| `` {{$}} mkdir -p contrib/win32``
| `` {{$}} cd contrib/win32``
| `` {{$}} ../bootstrap --host=HOST-TRIPLET``
| `` {{$}} make fetch``
| `` {{$}} make``

Linux 64-bit
~~~~~~~~~~~~

If you are on Linux **64-bit**, you **SHOULD** remove some files, or install the lib32 packages (ia32-libs, multilibs, etc...)

`` {{$}} rm -f ../i686-w64-mingw32/bin/moc ../i686-w64-mingw32/bin/uic ../i686-w64-mingw32/bin/rcc``

Fix your contrib path
~~~~~~~~~~~~~~~~~~~~~

If your host triplet is not **i686-w64-mingw32** (you are *not* compiling for Debian or Ubuntu), create a symlink to contribs:

``{{$}} ln -sf ``\ **``'HOST-TRIPLET``**\ ``' ../i686-w64-mingw32``

Notice that there is no ``../`` before the host triplet. This is intentional, and if done properly, you should see a functioning symbolic link created in the parent directory (try ``ls -l ..`` and you should see ``i686-w64-mingw32 -> x86_64-w64-mingw32/``).

Go Back
~~~~~~~

Go back to the VLC source directory:

`` {{$}} cd -``

Configuring the build
---------------------

Bootstrap
~~~~~~~~~

First, prepare the tree:

`` {{$}} ./bootstrap``

Configure
~~~~~~~~~

Then you can to configure the build with the ``./configure`` script.

Create a subfolder:

`` {{$}} mkdir win32 && cd win32``

Set your PKG_CONFIG_LIBDIR (Adapt the path to reflect your local setup)

| `` {{$}} export PKG_CONFIG_LIBDIR=$HOME/vlc/contrib/HOST-TRIPLET/lib/pkgconfig``
| `` {{$}} export PKG_CONFIG_PATH_CUSTOM=$PKG_CONFIG_LIBDIR (for Archlinux only)``

Execute the build configuration script:

``{{$}} ../extras/package/win32/configure.sh --host=HOST-TRIPLET --build=x86_64-pc-linux-gnu``

**N.B.**: Use the host and build tuples respectively corresponding to **your** cross-compilation toolchain and build system respectively. The example above assumes you are compiling for *Windows* OS and *Intel 686* architecture, and the build system is *GNU/Linux* OS and *x86 64-bits* architecture. See `above <#Host_triplet>`__ for list of common values.

Also, if you have a problem here (such as an error about Library dvdread), see the `Talk <{{TALKPAGENAME}}>`__ page.

Alternatively, you can run configure manually:

``{{$}} ../configure --host=HOST-TRIPLET --build=x86_64-pc-linux-gnu``

See ``'../configure --help'`` for more information.

Building VLC
------------

Once configured, to build VLC, just run:

`` {{$}} make``

Packaging VLC
-------------

Once the compilation is done, you can build self-contained VLC packages with the following ``make`` rules:

=========================== ====================================================================================================================================
Command                     Description
=========================== ====================================================================================================================================
``make package-win-common`` Creates a subdirectory named ``vlc-x.x.x`` with all the binaries. You can run VLC directly from this directory.
``make package-win-strip``  Same as above but will create 'stripped' binaries (that is, smallest size, unusable with a debugger).
``make package-win32-7zip`` Same as above but will package the directory in a 7z file.
``make package-win32-zip``  Same as above but will package the directory in a zip file.
``make package-win32``      Same as above but will also create an auto-installer package. You must have NSIS installed in its default location for this to work.
=========================== ====================================================================================================================================

**Well done—you're ready to use VLC!**

Extra information
-----------------

Static compilation of plugins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You might want to use the following script to enforce static compilation. Run as root, and use at your own risk.

.. code:: bash

    #!/bin/sh
    
    # This script enforces statically linking of libgcc, libstdc++-6, and libpthread,
    # without needing to rebuild gcc and mingw-w64 from scratch.
    # -static-libgcc -static-libstdc++ flags can not be used in a libtool build system,
    # as libtool removes flags that it doesn't understand.
    
    move() {
        [ -f $1 ] || return 1
        mkdir -p old/
        mv -v $* old/
        return 0
    }
    
    for x in i686 x86_64
    do
        library_path_list=`$x-w64-mingw32-gcc -v /dev/null 2>&1 | grep ^LIBRARY_PATH|cut -d= -f2|sort|uniq`
        IFS=':'
        for i in $library_path_list
        do
            cd $i
            move libstdc++-6.dll libstdc++.dll.a libgcc_s.a libgcc_s_sjlj-1.dll && ln -s libgcc_eh.a libgcc_s.a
            move libpthread.dll.a libwinpthread.dll.a
            move libwinpthread-1.dll
            [ -d ../bin ] && cd ../bin && move libwinpthread-1.dll
        done
    done
    
    exit 0

Mingw32
~~~~~~~

Up to versions 2.0.x, VLC was compiled with the older mingw32 toolchain, which only supports 32-bits Windows. If you have problems with mingw-w64, you can try mingw32 instead:

-  **Debian/Ubuntu**: run ``apt-get install gcc-mingw32 mingw32-binutils``. Note that at least version 3.17 of Mingw32 is required, which Debian does not provide. You may obtain mingw32-runtime-3.17 `here <http://people.videolan.org/~jb/debian/mingw32-runtime_3.17.0-0videolan_all.deb>`__.
-  **Gentoo** users can ``emerge crossdev && crossdev mingw32``
-  **ArchLinux** users can ``pacman -S mingw32-gcc``
-  **Fedora** users should read `Win32Compile Under Fedora <Win32Compile_Under_Fedora>`__
-  Other **Linux** systems may attempt http://www.mingw.org/wiki/LinuxCrossMinGW

`Category:Building <Category:Building>`__ `Category:Windows <Category:Windows>`__
