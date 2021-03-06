**configure** (also known as **./configure**) is a gigantic `shell script <wikipedia:bash>`__ used to gather information about your computer and select options on what to link to and how. Before running make (which compiles vlc), you should run configure.

If you are compiling source from `Git <Git>`__, then you should run ./bootstrap before running configure.

You can run configure like this:

``./configure --options``

*Beginner's guide*
------------------

   enter the command

``{{%}} ./configure --help | less``

and hit enter. Type a slash '/', type "disabled" (without quotes), hit enter. Pressing **n** goes to the next match, **N** goes to previous match, **q** returns to the command line. Use the up/down arrow keys to scroll. All matches except the *--cache-file* option (which belongs to ``configure`` itself) are VLC features that must be forced on if desired.)

**VLC 1.1 and earlier**: You probably need to tweak the "configure" line.

Options
-------

Below are some common options for configure:

====================================== ================================================
option                                 meaning
====================================== ================================================
--prefix=*/home/user/vlc/*             Sets the location of where to install vlc
--enable-flac                          Turns on support for `FLAC <FLAC>`__ audio files
--enable-ffmpeg                        Links with `ffmpeg <ffmpeg>`__
--with-ffmpeg-tree=*/home/user/ffmpeg* Location of ffmpeg source code
====================================== ================================================

See `./configure --help <VLC_configure_help>`__ for more information.

Examples
--------

This is an example of a typical VLC configure line:

| ``./configure --enable-x11 --enable-xvideo --enable-sdl --enable-avcodec --enable-avformat \``
| ``     --enable-swscale --enable-mad --enable-libdvbpsi --enable-a52 --enable-libmpeg2 \``
| ``     --enable-dvdnav --enable-faad --enable-vorbis --enable-ogg --enable-theora \``
| ``     --enable-faac --enable-mkv --enable-freetype --enable-fribidi --enable-speex \``
| ``     --enable-flac --enable-live555 --with-live555-tree=/usr/lib/live --enable-caca \``
| ``     --enable-skins --enable-skins2 --enable-alsa --enable-qt4 --enable-ncurses``

Linux
~~~~~

| ``{{%}} ./configure --enable-x11 --enable-xvideo --disable-gtk \``
| ``     --enable-sdl --enable-ffmpeg --with-ffmpeg-mp3lame \``
| ``     --enable-mad --enable-libdvbpsi --enable-a52 --enable-dts \``
| ``     --enable-libmpeg2 --enable-dvdnav --enable-faad \``
| ``     --enable-vorbis --enable-ogg --enable-theora --enable-faac\``
| ``     --enable-mkv --enable-freetype --enable-fribidi \``
| ``     --enable-speex --enable-flac --enable-livedotcom \``
| ``     --with-livedotcom-tree=/usr/lib/live --enable-caca \``
| ``     --enable-skins --enable-skins2 --enable-alsa --disable-kde\``
| ``     --disable-qt --enable-wxwindows --enable-ncurses \``
| ``     --enable-release ``

Linux GIT
~~~~~~~~~

| ``./configure --enable-x11 --enable-xvideo --disable-gtk \``
| ``     --enable-sdl --enable-ffmpeg --with-ffmpeg-mp3lame \``
| ``     --enable-mad --enable-libdvbpsi --enable-a52 --enable-dca \``
| ``     --enable-libmpeg2 --enable-dvdnav --enable-faad \``
| ``     --enable-vorbis --enable-ogg --enable-theora --enable-faac\``
| ``     --enable-mkv --enable-freetype --enable-fribidi \``
| ``     --enable-speex --enable-flac --enable-livedotcom \``
| ``     --with-livedotcom-tree=/usr/lib/live --enable-caca \``
| ``     --enable-skins --enable-skins2 --enable-alsa --disable-kde\``
| ``     --disable-qt --enable-wxwindows --enable-ncurses \``
| ``     --enable-asa --enable-release ``

Windows
~~~~~~~

*From*\ http://developers.videolan.org/vlc/vlc/INSTALL.win32

If you are cross-compiling from Debian, you can use something along those lines:

| `` ./bootstrap && \``
| `` PKG_CONFIG_LIBDIR=/usr/win32/lib/pkgconfig \``
| `` CPPFLAGS="-I/usr/win32/include -I/usr/win32/include/ebml" \``
| `` LDFLAGS=-L/usr/win32/lib \``
| `` CC=i586-mingw32msvc-gcc CXX=i586-mingw32msvc-g++ \``
| `` ./configure --host=i586-mingw32msvc --build=i386-linux \``
| ``     --disable-gtk \``
| ``     --enable-nls --enable-sdl --with-sdl-config-path=/usr/win32/bin \``
| ``     --enable-ffmpeg --with-ffmpeg-mp3lame --with-ffmpeg-faac \``
| ``     --with-ffmpeg-zlib --enable-faad --enable-flac --enable-theora \``
| ``     --with-wx-config-path=/usr/win32/bin \``
| ``     --with-freetype-config-path=/usr/win32/bin \``
| ``     --with-fribidi-config-path=/usr/win32/bin \``
| ``     --enable-live555 --with-live555-tree=/usr/win32/live.com \``
| ``     --enable-caca --with-caca-config-path=/usr/win32/bin \``
| ``     --with-xml2-config-path=/usr/win32/bin \``
| ``     --with-dvdnav-config-path=/usr/win32/bin \``
| ``     --disable-cddax --disable-vcdx --enable-goom \``
| ``     --enable-twolame --enable-dvdread \``
| ``     --enable-debug``

If you are using cygwin, you can build VLC with or without the POSIX emulation layer. Without is usually better and with POSIX emulation hasn't been tested in about a year or so. So to build without the emulation layer, use something like this:

| `` ./bootstrap && \``
| `` PKG_CONFIG_PATH=/usr/win32/lib/pkgconfig \``
| `` CPPFLAGS="-I/usr/win32/include -I/usr/win32/include/ebml" \``
| `` LDFLAGS=-L/usr/win32/lib \``
| `` CC="gcc -mno-cygwin" CXX="g++ -mno-cygwin" \``
| `` ./configure \``
| ``     --disable-gtk \``
| ``     --enable-nls --enable-sdl --with-sdl-config-path=/usr/win32/bin \``
| ``     --enable-ffmpeg --with-ffmpeg-mp3lame --with-ffmpeg-faac \``
| ``     --with-ffmpeg-zlib --enable-faad --enable-flac --enable-theora \``
| ``     --with-wx-config-path=/usr/win32/bin \``
| ``     --with-freetype-config-path=/usr/win32/bin \``
| ``     --with-fribidi-config-path=/usr/win32/bin \``
| ``     --enable-live555 --with-live555-tree=/usr/win32/live.com \``
| ``     --enable-caca --with-caca-config-path=/usr/win32/bin \``
| ``     --with-xml2-config-path=/usr/win32/bin \``
| ``     --with-dvdnav-config-path=/usr/win32/bin \``
| ``     --disable-cddax --disable-vcdx --enable-goom \``
| ``     --enable-twolame --enable-dvdread \``
| ``     --enable-debug``

If you want to use the emulation layer, then just omit the CC="gcc -mno-cygwin" CXX="g++ -mno-cygwin" line. You're on your own though.

If you are compiling with MSYS/MINGW, then you can use something along those lines:

| `` ./bootstrap && \``
| `` PKG_CONFIG_PATH=/usr/win32/lib/pkgconfig \``
| `` CPPFLAGS="-I/usr/win32/include -I/usr/win32/include/ebml" \``
| `` LDFLAGS=-L/usr/win32/lib \``
| `` ./configure \``
| ``     --disable-gtk \``
| ``     --enable-nls --enable-sdl --with-sdl-config-path=/usr/win32/bin \``
| ``     --enable-ffmpeg --with-ffmpeg-mp3lame --with-ffmpeg-faac \``
| ``     --with-ffmpeg-zlib --enable-faad --enable-flac --enable-theora \``
| ``     --with-wx-config-path=/usr/win32/bin \``
| ``     --with-freetype-config-path=/usr/win32/bin \``
| ``     --with-fribidi-config-path=/usr/win32/bin \``
| ``     --enable-caca --with-caca-config-path=/usr/win32/bin \``
| ``     --with-xml2-config-path=/usr/win32/bin \``
| ``     --with-dvdnav-config-path=/usr/win32/bin \``
| ``     --disable-cddax --disable-vcdx --enable-goom \``
| ``     --enable-twolame --enable-dvdread \``
| ``     --disable-mkv \``
| ``     --enable-debug``

If you have used the "extras/contrib" way, you don't need to precise the CFLAGS, LDFLAGS and --with-foo-config-path=.

| ``./bootstrap && \``
| `` ./configure \``
| ``     --disable-gtk \``
| ``     --enable-nls --enable-sdl \``
| ``     --enable-ffmpeg --enable-faad --enable-flac --enable-theora \``
| ``     --disable-cddax --disable-vcdx --enable-goom \``
| ``     --enable-twolame --enable-dvdread \``
| ``     --enable-mkv --enable-caca --enable-live555\``
| ``     --enable-debug``

See also `VLC configure help <VLC_configure_help>`__

`Category:Building <Category:Building>`__ `Category:GNU/Linux <Category:GNU/Linux>`__
