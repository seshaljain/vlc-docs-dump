{{Historical|see [[WinCECompile]]}}

== Introduction ==

This guide is to compile and build VLC for Windows CE devices. These are
the versions used for this guide:

   -  Ubuntu 9.04 jaunty
   -  vlc 1.0.2 ( version from git )

== Installing Cross-compile Tools ==

1) Download the latest arm-wince-mingw32ce from
   [http://cegcc.sourceforge.net/ Sourceforge]
2) untar it on / ( tar command with -C / )

      &nbsp;% sudo apt-get install bzip2 &nbsp;% bzip2 -d
      &lt;your-version&gt;.tar.bz2 &nbsp;% sudo tar xvf
      &lt;your-version&gt;.tar -C /

<br> 3) get wince tools from
[http://eleves.ec-lille.fr/~couprieg/divers/wince.tar.gz WinCE-Tools]

3.1)Untar it:

   &nbsp;% sudo tar xvzf wince.tar.gz -C /

== Getting VLC Source ==

1) Get git.

   &nbsp;% sudo apt-get install git-buildpackage

2) Retrieve the last vlc version from git repository

   &nbsp;% git clone git://git.videolan.org/vlc.git

== Getting additional tools ==

   &nbsp;% sudo apt-get install libtool &nbsp;% sudo apt-get install
   autotools-dev &nbsp;% sudo apt-get install libgcrypt11-dev &nbsp;%
   sudo apt-get install autoconf

Finally build the symbolics links ( sometimes is not necessary ).

Create symbolic links from /opt/mingw32ce/bin/\* to /usr/bin/ --&gt;
Preserve the original names.

== Building VLC ==

Now is time to build VLC.

   &nbsp;% cd vlc &nbsp;% ./bootstrap

Configure:

<br>

   &nbsp;%
   PATH=/opt/mingw32ce/bin:/opt/mingw32ce/arm-mingw32ce/bin:$PATH
   CC="arm-mingw32ce-gcc" CXX="arm-mingw32ce-g++"
   CFLAGS="-I/usr/wince/include -I/opt/mingw32ce/arm-mingw32ce/include
   -mwin32 -D \__COREDLL_\_ -D \_WIN32_WCE=0x0500"
   CPPFLAGS="-I/usr/wince/include -I/opt/mingw32ce/arm-mingw32ce/include
   -mwin32 -D \__COREDLL_\_ -D \_WIN32_WCE=0x0500"
   LDFLAGS="-L/opt/mingw32ce/arm-mingw32ce/lib -L/usr/wince/lib"
   ./configure --host=arm-mingw32ce --disable-sdl --disable-gtk
   --disable-dvdnav --disable-dvdread --disable-avformat
   --disable-postproc --disable-hal --disable-nls --enable-sout
   --enable-vlm --disable-wxwindows --disable-a52 --enable-libmpeg2
   --disable-freetype --disable-libgcrypt --disable-fribidi
   --disable-mad --disable-optimize-memory --disable-audioscrobbler
   --disable-tremor --disable-faad --enable-ffmpeg --disable-avcodec
   --enable-vlc --disable-activex --disable-testsuite --disable-skins2
   --disable-qt4 --disable-notify --disable-httpd --disable-dbus-control
   --disable-growl --disable-telepathy --disable-lua --disable-vlm
   --disable-gnutls --disable-bonjour --disable-x11 --disable-glx
   --disable-xvideo --disable-remoteosd --disable-schroedinger
   --disable-dshow --enable-wingdi --disable-real --disable-realrtsp
   --disable-optimizations --enable-debug --enable-wince
   --enable-waveout --disable-directx --disable-x264 --disable-live555
   --disable-pulse --disable-swscale --disable-telnet --disable-libmpeg2

      &nbsp;% make

      &nbsp;% make package-wince

Now your VLC is ready!!! You will have a zip file ready to be unzipped
on your device.

== Final tasks ==

Copy this dll in the install directory

   -  libiconv-2.dll ( Need to be cross-compiled )
   -  libcharset-1.dll ( Need to be cross-compiled )
   -  libgcc_s_sjlj-1.dll ( mingw32ce provides it )
   -  libstdc++-6.dll ( mingw32ce provides it )

== Finished ==

This guide provides a way to build an executable vlc for WINCE, but it
is not working ok, since the GUI is not responding properly.

I am still working on it, so if anyone achieve some progress please
contact me. And of course, if you have any doubt, question or find
something wrong in this post don't hesitate to contact me.
--[[User:Hectorhg|HectorHg]] 13:47, 1 October 2009 (UTC)

[[Category:Coding]] [[Category:Building]] [[Category:Windows]]
