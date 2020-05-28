Prepare your environment
------------------------

VLC requires a C11 compiler, development headers and a toolchain.

**gcc** (version 4.9 or later) is recommended, but **clang/LLVM** are known to work as well.

If you build from the `Git <Git>`__ repositories, you will also need the GNU build system, also known as the "autotools" (autoconf, automake, libtool and gettext) to setup the Makefiles. Make sure they are up-to-date and usable for your system.

On Fedora:

``{{$}} sudo yum install git libtool pkgconfig``

On Debian or Ubuntu:

``{{$}} sudo apt-get install git build-essential pkg-config libtool automake autopoint gettext``

On Arch

``{{$}} sudo pacman -S base-devel git pkg-config autoconf automake``

Get the source
--------------

Start by `getting the source <GetTheSource>`__, using FTP for official releases, or using `Git <Git>`__ to track VLC development.

If you are using the `Git <Git>`__ development version, start by bootstrapping the source tree:

| ``{{$}} git clone ``\ ```git://git.videolan.org/vlc.git`` <git://git.videolan.org/vlc.git>`__
| ``{{$}} cd vlc``
| ``{{$}} ./bootstrap``

Bootstrapping will fail if 'autotools' is missing or out-of-date.

If you are using an official release, download source code, extract the archive and go into the resulting VLC directory, e.g.:

| ``{{$}} wget ``\ ```ftp://ftp.videolan.org/pub/videolan/vlc/`` <ftp://ftp.videolan.org/pub/videolan/vlc/>`__\ \ ``/vlc-``\ \ ``.tar.xz``
| ``{{$}} tar xvJf vlc-``\ \ ``.tar.xz``
| ``{{$}} cd vlc-``\ 

Get the third-party libraries
-----------------------------

Now you can almost `configure <configure>`__ the VLC build. But first, you need to make sure that all the required dependencies are in place.

You must install and enable all the 3rd party libraries that you need. If you fail to install a required library, you can end up with a VLC application that misbehave. See `here <Contrib_Status>`__ for the complete list.

**Nota bene**: you need to install the development packages (development header files and import libraries) to compile VLC, not just the run-time. On Debian/Ubuntu, the correct package names end with -dev. On RPM distributions, they usually end in -devel.

**Be careful!** If the libraries are not provided by your distribution, you may be better off linking VLC with them statically. See the "Contrib" method.

There are a several ways to get those libraries. You should use only one method at a time:

The preferred method
~~~~~~~~~~~~~~~~~~~~

Use your distribution packaging or portage system, in order to get all the needed libs.

Debian
^^^^^^

For example on Debian or Ubuntu:

``{{$}} sudo apt-get build-dep vlc``

OpenSuSE
^^^^^^^^

openSUSE users might have a look at the source-install (si) command in the zypper manpage:

``{{$}} sudo zypper si -d vlc``

**Note:** To get the libraries, you must first add the VLC repositories to your system repositories. For example in openSUSE:

``{{$}} sudo zypper ar ``\ ```http://download.videolan.org/pub/vlc/SuSE/`` <http://download.videolan.org/pub/vlc/SuSE/>`__\ \ `` VLC``

You should replace with the version of your system (12.1, 11.4, 11.3, 11.2 or 11.1)

The "Contrib" method
~~~~~~~~~~~~~~~~~~~~

If your distribution does not provide the needed libraries or if you really need to link VLC statically, use the VLC contribs system, included in the VLC source.

First, you need to install the GNU autotools (if you have not already done so), CMake, subversion, Git and a recent GNU/tar utility or equivalent.

\ `` apt-get install subversion yasm cvs cmake ragel``

Then you can run:

| ``{{$}} cd contrib``
| ``{{$}} mkdir native``
| ``{{$}} cd native``
| ``{{$}} ../bootstrap``
| ``{{$}} make``

That should download and build a lot of those libraries for you. Unfortunately, given the large number of libraries and the variety of the platforms people build VLC for, it is not unlikely that you will hit an error while contribs are compiling. Thus, this approach is only recommended for experienced Unix compilers.

Regardless of the method
~~~~~~~~~~~~~~~~~~~~~~~~

In any case, some basic OS support libraries are not included and must really be installed through the packaging system in any case, notably `ALSA <ALSA>`__, `PulseAudio <PulseAudio>`__ and OpenGL.

Configuration
-------------

``./configure`` is used to check whether your system is able to compile VLC. Also you can choose the features in your build. As a reminder, this command will show the various options:

``{{$}} ./configure --help``

For most users, ``./configure`` does not require any command-line options.

By default, features to be compiled are chosen automatically depending on what libraries are detected as available. If the contribs have been compiled first, the resulting VLC will be reasonably functional.

Note that libraries that are not in the default prefix, and not in vlc contribs, must be known to pkg-config in order for ``./configure`` to find them. Use *PKG_CONFIG_PATH* for this.

There are some features that are disabled (not compiled) by default. If you want them, they must be forced on by using configure flags. You can find a list of these features by searching for "disabled" in ``./configure --help``.

Prefix
~~~~~~

If you want to install VLC into another directory, run

``{{$}} ./configure --prefix=/path/to/install/folder/``

You can find example of configure in the `Configure <Configure>`__ page of this wiki.

Compilation
-----------

Compile VLC:

``{{$}} make``

You do not need to install VLC to use it. You can also simply run it from the build directory:

\ `` ./vlc``

If you really want to install VLC to the system, run this as root:

\ `` make install``

You can uninstall later with this, but you need to keep the build tree untouched until then:

\ `` make uninstall``

To remove files created during the compile (optional) type:

``{{$}} make clean``

Troubleshooting / common problems
---------------------------------

Lua
~~~

You may need to install Lua if you get "LUA byte compiler missing." message. You namely need to install "luac", the Lua byte compiler.

On Debian/Ubuntu:

``{{$}} sudo apt-get install lua5.1``

On Fedora:

``{{$}} sudo yum install lua``

XCB
~~~

VLC 1.1 and later requires XCB libraries to deal with X11 displays. Do not disable XCB or you will not get any video support!

To install these libraries run the following commands (Debian/Ubuntu):

``{{$}} sudo apt-get install libxcb-shm0-dev libxcb-xv0-dev libxcb-keysyms1-dev libxcb-randr0-dev libxcb-composite0-dev``

Under Fedora:

``{{$}} sudo yum install libxcb-devel xcb-util-devel``

For OpenGL (Debian/Ubuntu only), you will additionally need XLib with XCB:

``{{$}} sudo apt-get install libx11-xcb-dev``

If your distribution provides a version of XLib without XCB, then this later package will not be available. So you will not be able to use OpenGL. Use XVideo instead.

Compile fails after git pull
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is likely that the sources in the repository have changed significantly since they were last pulled, and a build system cache has gone out of date. Try the troubleshooting methods described in the `hacker guide for modules <Hacker_Guide/How_To_Write_a_Module#Module_load_troubleshooting>`__.

`Category:Building <Category:Building>`__ `Category:GNU/Linux <Category:GNU/Linux>`__
