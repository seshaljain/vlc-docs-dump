Compile VLC on BeOS

Required tools
--------------

You need :

-  `BeOS 5 <http://www.bebits.com/app/2680>`__ with development tools
-  `CVS 1.11 <http://www.bebits.com/app/1610>`__
-  Git
-  `bzip2/bunzip2 <http://www.bebits.com/app/3218>`__
-  `wget <http://www.bebits.com/app/2848>`__
-  `gcc 2.95.3 <http://www.bebits.com/app/4011>`__

Compiling is usually done on a vanilla R5.0.3 install with gcc 2.95.3.

Building with older compilers won't work.

Building on a BONE-enabled install probably doesn't work at the moment.

Build VLC
---------

Now you can compile vlc:

Get the source
~~~~~~~~~~~~~~

Download the `source code <GetTheSource>`__ (using `Git <Git>`__) as described on the `"Get the source" <GetTheSource>`__ page.

Build external libs
~~~~~~~~~~~~~~~~~~~

We now need to build the `3rd party libs <Contrib_Status>`__. For that, you will need to:

-  cd to the source directory with your Terminal application.
-  cd to extras/contrib/ subdir of VLC and execute ``./bootstrap``
-  Now execute ``make src``. This will download and compile all the required external libraries and programs that needs (you need an internet connection, a fast one preferably).

Prepare the VLC build
~~~~~~~~~~~~~~~~~~~~~

Now we return to VLC itself. Go back to the top level VLC source directory. If you use Git (which you really should), then run ``./bootstrap``.

This will create configure and Makefiles for (snapshots and releases already include this).

Configure VLC
~~~~~~~~~~~~~

The next step is to configure, in the top level VLC source directory.

``./configure --enable-debug --enable-sout --enable-httpd --enable-vlm --enable-dvdread --enable-dvdnav --enable-dvbpsi --enable-screen --enable-ogg --enable-mkv --enable-mad --enable-ffmpeg --enable-faad --enable-a52 --enable-flac --enable-libmpeg2 --enable-vorbis --enable-speex --enable-theora --enable-freetype --enable-fribidi --disable-skins2 --with-ffmpeg-mp3lame --with-ffmpeg-faac --with-ffmpeg-zlib --disable-x11 --disable-hal --disable-daap --disable-xvideo --disable-glx --disable-sdl --disable-wxwindows``

.. _build-vlc-1:

Build VLC
~~~~~~~~~

After configure is finished, we can finally build . A simple ``make`` will do the trick.

To build a package, run ``make package-beos``.

History
-------

Written by Eric Petit, for the VideoLAN Team. Adapted to the Wiki by `Jean-Baptiste Kempf <User:j-b>`__.

`Category:Building <Category:Building>`__ `Category:Coding <Category:Coding>`__
