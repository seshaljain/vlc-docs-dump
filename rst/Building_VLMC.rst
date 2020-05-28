.. figure:: VLMC_icon.png
   :alt: VLMC_icon.png

   VLMC_icon.png

Building VLMC from source
-------------------------

This wiki page has information on building `VideoLAN Movie Creator <VideoLAN_Movie_Creator>`__ (VLMC) from source.

VLMC is a free video editing software, offering features to realize semi-professional quality movies, but with the aim to stay simple and user-friendly.

Resources
~~~~~~~~~

VLMC requires a c++ compiler (g++), cmake, Qt(4.6+), libVLC and frei0r plugins.

-  To install `Qt <Qt>`__, refer to: https://www.qt.io
-  To install `libVLC <libVLC>`__, you are required to `compile VLC <compile_VLC>`__
-  To get the current source of , refer to: `GetTheSource <GetTheSource>`__
-  For information on using Git, refer to: `Git <Git>`__
-  If you are interested in mailing lists, go to https://mailman.videolan.org/listinfo/. We have two VLMC mailing lists:

   -  `vlmc-announce <https://mailman.videolan.org/pipermail/vlmc-announce/>`__: Official announcements (release, events, ...)
   -  `vlmc-devel <https://mailman.videolan.org/pipermail/vlmc-devel/>`__: Developers discussions

Getting the code
~~~~~~~~~~~~~~~~

You can fetch the current VLMC working tree using Git:

``{{$}} git clone ``\ ```https://code.videolan.org/videolan/vlmc.git`` <https://code.videolan.org/videolan/vlmc.git>`__

Do the same for VLC (as described in `GetTheSource <GetTheSource>`__):

``{{$}} git clone ``\ ```git://git.videolan.org/vlc.git`` <git://git.videolan.org/vlc.git>`__

Building VLMC on Linux
~~~~~~~~~~~~~~~~~~~~~~

Following is the cleanest way of compiling VLMC (commands for \*nix OS)

1. Compile and install `libVLC <libVLC>`__, libVLC is required by VLMC (you can also install VLC using your Linux distribution), for example:

| ``{{$}} cd path_to_vlc_src``
| ``{{$}} ./bootstrap``
| ``{{$}} ./configure ``\ *``--your-options-here``\ ````\ ``(see``\ ````\ ``--help)``*
| ``{{$}} make``
| \ `` make install``

2. For Compiling VLMC:

| ``{{$}} cd path_to_vlmc_src``
| ``{{$}} mkdir build && cd build``
| ``{{$}} cmake ..``
| ``{{$}} make``

3. Run VLMC:

``{{$}} ./vlmc``

Building VLMC in developer mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, VLMC enables a crash handler, which is responsible for saving a backup of the project in the event of a crash.

While this might be handy for the users, it makes life harder on developers, since a debugger would attach to the daemon process instead of VLMC.

In order to disable this, you'll need a tool such as ccmake, or cmake-gui, to disable the ``WITH_CRASHHANDLER`` option.

Alternatively, you can invoke cmake with ``-DWITH_CRASHHANDLER=OFF`` flag

Cross Compiling VLMC for Windows on Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VLMC can be cross-compiled for Windows, on Linux using mingw:

| ``{{$}} cd contribs``
| ``{{$}} sh contribs.sh``
| ``{{$}} cd ..``
| ``{{$}} mkdir win32 && cd win32``
| ``{{$}} cmake -DCMAKE_TOOLCHAIN_FILE=../cmake/toolchain-win32.cmake ..``
| ``{{$}} make``

Compiling on Mac OS
~~~~~~~~~~~~~~~~~~~

Dependencies
^^^^^^^^^^^^

-  Build tools: Xcode command-line tools
-  homebrew

Get the sources:
^^^^^^^^^^^^^^^^

``{{$}} git clone ``\ ```https://code.videolan.org/videolan/vlmc.git`` <https://code.videolan.org/videolan/vlmc.git>`__

Get the actual dependencies:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| ``{{$}} brew tap tomahawk-player/tomahawkqt5``
| ``{{$}} brew install make``
| ``{{$}} brew install vlc``
| ``{{$}} brew install qt5``
| ``{{$}} brew install frei0r``

Compile vlmc:
^^^^^^^^^^^^^

Now cd to root source directory and build:

| ``{{$}} mkdir build && cd build``
| ``{{$}} cmake ..``
| ``{{$}} make``

This will by default create a Mac Bundle, ``vlmc.app`` in ``/build/bin``

To create a dmg image:
^^^^^^^^^^^^^^^^^^^^^^

To create a dmg image, uncomment ``#dmg`` in ``/src/CMakeLists.txt``, at the end of the file.

This creates the ``app/dmg`` in ``<build-directory>/bin``

Packaging VLMC
~~~~~~~~~~~~~~

-  On Linux, you can create deb/rpm package by using:

``{{$}} make package``

-  You can create NSIS installer for Windows using cross-compiling on Linux:

``{{$}} make installer``

Start hacking ;-)

`Category:Building <Category:Building>`__ `Category:VideoLAN projects <Category:VideoLAN_projects>`__
