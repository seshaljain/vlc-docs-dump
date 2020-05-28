.. raw:: mediawiki

   {{Historical}}

Cross compile VLC for ARM-based platforms
-----------------------------------------

Last updated: v0.0.2, 19 march 2004 This document describes all the steps to cross compile vlc for ARM based platforms. It describes how to build a cross compilation toolchain, how to build the libraries needed by vlc and the compilation of the vlc itself.

Introduction
------------

This document is only a first draft. It does not intend to cover all subjects and is written for vlc version 0.7.2. You may still have some problems at some steps or find better way to do them. If you have any comment do not hesitate to contact us. Which platforms are targeted ?

I will describe here how to compile vlc for an ARM based PDA running linux. It includes for example :

-  Compaq - iPaq (H36xx, H38xx,...), using Familiar Linux

   -  GNU Portable Environment (GPE)
   -  Opie

-  YOPY/Linupy
-  Zaurus

Requirements for cross-compilation
----------------------------------

Why cross-compiling ?
~~~~~~~~~~~~~~~~~~~~~

It is of course possible to compile directly on the targeted platform. But there are a lot of great advantages to cross-compile :

-  The most important one is probably the speed, because a desktop computer is most of the time faster than a PDA for compilation.
-  Another big problem is that a complete compilation toolchain does take a great amount of disk space. And this space is usually very limited on embedded systems.
-  And there also may not be enough memory to compile big files.

Building the toolchain
----------------------

Prerequisite
~~~~~~~~~~~~

Importants paths
^^^^^^^^^^^^^^^^

During this section, we will use the following paths :

I would personally advise to compile everything as a normal user and then install everything as root.

${SRCDIR}
^^^^^^^^^

This is where the sources will be located and where the compilation will be done. (eg: /usr/src or /home/foobar/arm-src).

${PREFIX}
^^^^^^^^^

This is where you want to install your cross compilation toolchain. It can be either installed system-wide (in /usr/local/arm/2.95.3 for example). Installation steps (i.e. make install) will have to be done as root. Or it can be installed in user-land, for the user's own use (/home/foobar/arm/2.95.3 for example). In this paper, the chosen prefix is /usr/local/arm/2.95.3, you will have to adapt the commands to what you choose..

Files needed
^^^^^^^^^^^^

Download the following files and put them in the ${SRCDIR}. Most of them are available on the "VideoLAN website".

-  binutils-2.11.2.tar.gz
-  linux-2.4.19.tar.bz2
-  patch-2.4.19-rmk4.bz2
-  gcc-2.95.3.tar.gz
-  gcc-2.95.3.diff.bz2
-  gcc-2.95.3.diffbis.bz2 - [File hard to find, Please post link to file]
-  gcc-2.95.3.diff2
-  glibc-2.2.5.tar.gz
-  glibc-linuxthreads-2.2.5.tar.gz
-  SDL-1.2.5.tar.gz
-  glib-1.2.10.tar.gz
-  ffmpeg.tar.gz
-  mad-0.14.2b.tar.gz
-  flac-1.1.0.tar.gz
-  libdvbpsi-0.1.2.tar.gz
-  a52dec-0.7.4.tar.gz

Binutils
--------

Compiling binutils is pretty simple :

| ``tar -xzf binutils-2.11.2.tar.gz``
| ``cd binutils-2.11.2``
| ``./configure --target=arm-linux --prefix=/usr/local/arm/2.95.3``
| ``make``
| ``make install``

Preparing linux kernel
----------------------

Before building the glibc library the right kernel header files should be available. Therefor the kernel that is going to be used needs to be prepared so all necessary header files are present. Follow these steps.

| ``tar -xzf linux-2.4.19.tar.bz2``
| ``bunzip2 patch-2.4.19-rmk4.bz2``
| ``cd linux-2.4.19``
| ``make mrproper``
| ``patch -p1 < ../patch-2.4.19-rmk4.bz2``
| ``make clean ARCH=arm CROSS_COMPILE=arm-linux-``
| ``make ARCH=arm h3600_config``

**Do not forget** to save the configuration even if no changes are made !

| ``make ARCH=arm menuconfig``
| ``make symlinks ARCH=arm CROSS_COMPILE=arm-linux-``
| ``mkdir -p /usr/local/arm/2.95.3/arm-linux/include``
| ``cp -Rf include/asm include/asm-arm include/linux \``
| ``/usr/local/arm/2.95.3/arm-linux/include``
| ``cd /usr/local/arm/2.95.3/arm-linux``
| ``ln -s include sys-linux``

Basic cross compiler (gcc)
--------------------------

| ``tar -xvzf gcc-2.95.3.tar.gz``
| ``bunzip2 gcc-2.95.3.diff.bz2``
| ``bunzip2 gcc-2.95.3.diffbis.bz2``
| ``patch -p1 -d gcc-2.95.3 < gcc-2.95.3.diff``
| ``patch -p1 -d gcc-2.95.3 < gcc-2.95.3.diffbis``
| ``cd gcc-2.95.3``
| ``./configure --target=arm-linux --disable-threads --enable-languages=c \``
| ``--prefix=/usr/local/arm/2.95.3 --with-headers=linux-2.4.19/include``
| ``make``
| ``make install``

Compiling glibc
---------------

Depending on your target, you may choose another glibc version (eg: 2.1.3 for linupy 1.4)

| ``tar -xvzf glibc-2.2.5.tar.gz``
| ``cd glibc-2.2.5``
| ``tar -xvzf ../glibc-linuxthreads-2.2.5.tar.gz``
| ``CC=arm-linux-gcc ./configure arm-linux --target=arm-linux \``
| ``--prefix=/usr/local/arm/2.95.3/arm-linux --enable-add-ons``

The following step takes quite a long time!

``CC=arm-linux-gcc make``

If you have problems compiling glibc due to pread/pwrite, edit sysdeps/unix/sysv/linux/kernel-features.h and turn \__ASSUME_PREAD_SYSCALL and \__ASSUME_PWRITE_SYSCALL from 1 to 0.

``CC=arm-linux-gcc make install``

Full cross compiler (gcc)
-------------------------

Now it is time to build a cross-compiler that can built user space libraries too. Follow these steps:

| ``rm -Rf gcc-2.95.3``
| ``tar -xvzf gcc-2.95.3.tar.gz``
| ``patch -p1 -d gcc-2.95.3 < gcc-2.95.3.diff``
| ``patch -p1 -d gcc-2.95.3 < gcc-2.95.3.diff2``
| ``cd gcc-2.95.3``
| ``./configure --target=arm-linux --prefix=/usr/local/arm/2.95.3``
| ``make``
| ``make install``

Misc
----

Add /usr/local/arm/2.95.3/bin to your PATH. Add the following line (depends on your shell) to your shell's configuration file :

``export PATH=/usr/local/arm/2.95.3/bin:$PATH``

I would advise you to completely log out and then log in again, so that the change would be taken into account. You can now check that when you type arm-linux-gcc, it launches the cross-compiler.

Next are some packages that you may compile by yourself, but I found it was easier to use the precompiled packages. You can take them at "ipkgfind">. You may find packages with other version numbers which should not be a problem.

-  libgcc1_3.1.1-1_arm.ipk This provides libgcc.so.1 which is needed to compile some libraries.
-  xlibs_4.1-5_arm.ipk, xlibs-dev_4.1.0-16_arm.ipk Those are the libraries ans the development files for X windows.
-  zlib1g_1.1.4-3_arm.ipk, zlib1g-dev_1.1.3-fam1_arm.ipk These libraries are needed by some libraries to compile.

Install these packages on your compiler box in /usr/local/arm/2.95.3/arm-linux : You can use the script install.sh :

| ``#!/bin/sh``
| ``# script to install .ipk into the arm-toolchain``
| ``# usage : ./install.sh foobar.ipk``

| ``if ! tar -xvzf $1 2> /dev/null``
| ``then``
| ``ar xv $1 2> /dev/null``
| ``fi``
| ``cp data.tar.gz /usr/local/arm/2.95.3/arm-linux``
| ``cd /usr/local/arm/2.95.3/arm-linux``
| ``tar -xvzf data.tar.gz``

Setting up Opie cross-compile environment
-----------------------------------------

Download the Opie SDK from the website `OPIE website <http://opie.handhelds.org/>`__ using the menuitem "Download Opie SDK" or try the direct link here: "Download Opie SDK". Download all files to your ${SOURCES}/opie directory. Opie SDK

The Opie SDK does not come with a README file or installation instructions. I give them here instead. There are two tar files in the download a OpieSDK.tar.gz2 and a kdevelop_src.tar.bz2. The last file is a modified kdevelop for use with the OpieSDK. In this tutorial we will not use that. Unpack OpieSDK.tar.bz2 in your sources cd ${SOURCES}/opie directory.

| ``cd ${SOURCES}/opie``
| ``tar -xjvf OpieSdk.tar.bz2``

It creates a directories structure ${SOURCES}/opie/opt/OpieSDK. Inside that directory a script is present to start_kdevelop. Modify this script so that it uses the correct paths for you setup.

| ``#!/bin/sh``
| ``source ${SOURCES}/opie/opt/OpieSdk/dev_env``

| ``export KDEDIR=${SOURCES}/opie/opt/OpieSdk/kde``
| ``export PATH=${SOURCES}/opie/opt/OpieSdk/kde/bin:$PATH``
| ``kbuildsycoca``
| ``kdevelop``

Save the script. Do the same with the script arm_source

| ``source ${SOURCES}/opie/opt/OpieSdk/dev_env``
| ``export QTDIR=$QTDIR_ARM``
| ``export OPIEDIR=$OPIEDIR_ARM``

Save the script and modify the script host_source in the same manner as above.

| ``source ${SOURCES}/opie/opt/OpieSdk/dev_env``
| ``export QTDIR=$QTDIR_NAT``
| ``export OPIEDIR=$OPIEDIR_NAT``

Save the script and modify the script dev_env in the same manner as above.

| ``export PYTHONPATH=${SOURCES}/opie/opt/OpieSdk/python/opie:${SOURCES}/opie/opt/OpieSdk/python/sip``
| ``export PATH=/usr/local/arm/2.95.3/bin:/opt/OpieSdk/host_tools:${SOURCES}/opie/opt/OpieSdk/opie/x86/qt-2.3.7/bin:$PATH``
| ``export PATH=${SOURCES}/opie/opt/OpieSdk/opie/x86/qmake:$PATH``
| ``export QTDIR_NAT=${SOURCES}/opie/opt/OpieSdk/opie/x86/qt-2.3.7``
| ``export OPIEDIR_NAT=${SOURCES}/opie/opt/OpieSdk/opie/x86/sdk``
| ``export QTDIR_ARM=${SOURCES}/opie/opt/OpieSdk/opie/arm/qt-2.3.7``
| ``export OPIEDIR_ARM=${SOURCES}/opie/opt/OpieSdk/opie/arm/sdk``
| ``export OPIE_SDK_BASE=${SOURCES}/opie/opt/OpieSdk/``
| ``export OPIE_SDK_QMAKE_BASE=${SOURCES}/opie/opt/OpieSdk/opie/x86/sdk/mkspecs/qws/``
| ``export OPIE_DOC=${SOURCES}/opie/opt/OpieSdk/apidocs``

| ``export LD_LIBRARY_PATH=${SOURCES}/opie/opt/OpieSdk/sip/lib:$OPIEDIR_NAT/lib:$QTDIR_NAT/lib:$LD_LIBRARY_PATH``
| ``export OPIE_LANGUAGES=de:en:cz:da:dk:es:fr:hu:it:ja:ko:lv:mk:nl:no:pl:pt:pt_BR:ru:sl:zh_CN:zh_TW``

The symbolic linke to the tool qmake points now to the wrong place. We need to fix this symbolic link. Here is the way to do that.

| ``cd host_tools``
| ``ln -sf ${SOURCES}/opie/opt/OpieSdk/opie/x86/sdk/qmake/qmake qmake``
| ``cd ../``

Now it is time to fire up our development environment and start hacking in Opie.

Cross compiling libraries needed by vlc
---------------------------------------

Download ipaq-config.site to ${SOURCES}. When downloading source tarballs copy them to your ${SOURCES} directory. Each section is supposed to begin with cd ${SOURCES}.

SDL
~~~

It is not clean at all but did not found a better working method. Using config.site it compiles well, but when linking with vlc there are problems !

| ``/usr/local/arm/2.95.3/arm-linux/bin should contain the cross compiler without the prefix arm-linux-.``
| ``tar -xvzf SDL-1.2.5.tar.gz``
| ``cd SDL-1.2.5``
| ``./configure --enable-release --target=arm-linux --host=arm-linux \``
| ``--disable-esd \``
| ``--prefix=/usr/local/arm/2.95.3/arm-linux/usr \``
| ``--x-includes=/usr/local/arm/2.95.3/arm-linux/usr/X11R6/include \``
| ``--x-libraries=/usr/local/arm/2.95.3/arm-linux/usr/X11R6/lib \``
| ``--disable-video-opengl``

``export PATH=/usr/local/arm/2.95.3/arm-linux/bin:$PATH``

``make && make install``

Glib/GTK+
~~~~~~~~~

| ``tar -xvzf glib-1.2.10.tar.gz``
| ``cd glib-1.2.10``
| ``CONFIG_SITE=../ipaq-config.site ./configure \``
| ``--prefix=/usr/local/arm/2.95.3/arm-linux/usr``
| ``make``
| ``make install``
| ``cd ..``
| ``tar -xvzf gtk+-1.2.10.tar.gz``
| ``cd gtk+-1.2.10``
| ``CONFIG_SITE=../ipaq-config.site ./configure \``
| ``--prefix=/usr/local/arm/2.95.3/arm-linux/usr --with-glib=../glib-1.2.10``
| ``make``
| ``make install``

ffmpeg
~~~~~~

| ``tar -xvzf ffmpeg.tar.gz``
| ``cd ffmpeg``
| ``./configure --arch=armv4l --cc=arm-linux-gcc --disable-mmx \``
| ``--prefix=/usr/local/arm/2.95.3/arm-linux/usr --enable-shared``
| ``cd libavcodec``
| ``make``

Vlc does not require that you install ffmpeg.

mad
~~~

| ``tar -xvzf mad-0.14.2b.tar.gz``
| ``cd mad-0.14.2b``
| ``./configure --enable-release --target=arm-linux --host=arm-linux \``
| ``--disable-esd \``
| ``--prefix=/usr/local/arm/2.95.3/arm-linux/usr \``
| ``--x-includes=/usr/local/arm/2.95.3/arm-linux/usr/X11R6/include \``
| ``--x-libraries=/usr/local/arm/2.95.3/arm-linux/usr/X11R6/lib \``
| ``--disable-video-opengl``
| ``export PATH=/usr/local/arm/2.95.3/arm-linux/bin:$PATH``
| ``make``

gpe
~~~

Not described.

tremor
~~~~~~

Tremor is an integer decoder for the vorbis audio codec. Download the source through subversion at the "xiph.org" website.

| ``svn co ``\ ```http://svn.xiph.org/trunk/Tremor`` <http://svn.xiph.org/trunk/Tremor>`__
| ``cd Tremor``
| ``CONFIG_SITE=../ipaq-config.site ./configure \``
| ``--prefix=/usr/local/arm/2.95.3/arm-linux/usr``
| ``make``

ogg
~~~

For ogg, it is the same as Tremor.

| ``svn co ``\ ```http://svn.xiph.org/trunk/ogg`` <http://svn.xiph.org/trunk/ogg>`__
| ``cd ogg``
| ``CONFIG_SITE=../ipaq-config.site ./configure \``
| ``--prefix=/usr/local/arm/2.95.3/arm-linux/usr``
| ``make``

flac
~~~~

| ``tar -xvzf flac-1.1.0.tar.gz``
| ``cd flac-1.1.0``
| ``./configure --enable-release --host=arm-linux --target=arm-linux \``
| ``--prefix=/usr/local/arm/2.95.3/arm-linux/usr``

It will probably fail (due to the xmms plugin), but it is not a problem, we will continue installation by hand.

| ``cp -Rf include/FLAC /usr/local/arm/2.95.3/arm-linux/include``
| ``cd src/libFLAC``
| ``make install``

libdvbpsi
~~~~~~~~~

| ``tar -xvzf libdvbpsi-0.1.2.tar.gz``
| ``cd libdvbpsi-0.1.2``
| ``./bootstrap``
| ``./configure --target=arm-linux --host=arm-linux``
| ``make``

a52
~~~

| ``tar -xvzf a52dec-0.7.4.tar.gz``
| ``cd a52dec-0.7.4``
| ``./configure --enable-release --host=arm-linux --target=arm-linux \``
| ``--prefix=/usr/local/arm/2.95.3/arm-linux/usr``
| ``make && make install``

Cross compiling vlc itself
--------------------------

First of all, run the ./bootstrap script. Then run one of the ipkg/rules.*, according to what you want to compile. Finally you just have to type make and you'll get a stand alone vlc.

Run arm-linux-strip to remove symbols and so the size of the file, and now you can test it easily on your PDA.

Enjoy !

Version
-------

Made by Marc Ariberti and Jean-Paul Saman. Adapted to the wiki by `Jean-Baptiste Kempf <User:J-b>`__.

`Category:Building <Category:Building>`__
