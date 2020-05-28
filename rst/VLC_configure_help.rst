.. raw:: mediawiki

   {{See also|configure}}

This details the current output of your configure.

To launch and get the current information about this file:

``./configure --help``

| ````
| :literal:`\`configure' configures vlc 2.1.0-git to adapt to many kinds of systems.`
| ````
| ``Usage: ../configure [OPTION]... [VAR=VALUE]...``
| ````
| ``To assign environment variables (e.g., CC, CFLAGS...), specify them as``
| ``VAR=VALUE.  See below for descriptions of some of the useful variables.``
| ````
| ``Defaults for the options are specified in brackets.``
| ````
| ``Configuration:``
| ``  -h, --help              display this help and exit``
| ``      --help=short        display options specific to this package``
| ``      --help=recursive    display the short help of all the included packages``
| ``  -V, --version           display version information and exit``
| :literal:`  -q, --quiet, --silent   do not print `checking ...' messages`
| ``      --cache-file=FILE   cache test results in FILE [disabled]``
| :literal:`  -C, --config-cache      alias for `--cache-file=config.cache'`
| ``  -n, --no-create         do not create output files``
| :literal:`      --srcdir=DIR        find the sources in DIR [configure dir or `..']`
| ````
| ``Installation directories:``
| ``  --prefix=PREFIX         install architecture-independent files in PREFIX``
| ``                          [/usr/local]``
| ``  --exec-prefix=EPREFIX   install architecture-dependent files in EPREFIX``
| ``                          [PREFIX]``
| ````
| :literal:`By default, `make install' will install all the files in`
| :literal:`\`/usr/local/bin', `/usr/local/lib' etc.  You can specify`
| :literal:`an installation prefix other than `/usr/local' using `--prefix',`
| :literal:`for instance `--prefix=$HOME'.`
| ````
| ``For better control, use the options below.``
| ````
| ``Fine tuning of the installation directories:``
| ``  --bindir=DIR            user executables [EPREFIX/bin]``
| ``  --sbindir=DIR           system admin executables [EPREFIX/sbin]``
| ``  --libexecdir=DIR        program executables [EPREFIX/libexec]``
| ``  --sysconfdir=DIR        read-only single-machine data [PREFIX/etc]``
| ``  --sharedstatedir=DIR    modifiable architecture-independent data [PREFIX/com]``
| ``  --localstatedir=DIR     modifiable single-machine data [PREFIX/var]``
| ``  --libdir=DIR            object code libraries [EPREFIX/lib]``
| ``  --includedir=DIR        C header files [PREFIX/include]``
| ``  --oldincludedir=DIR     C header files for non-gcc [/usr/include]``
| ``  --datarootdir=DIR       read-only arch.-independent data root [PREFIX/share]``
| ``  --datadir=DIR           read-only architecture-independent data [DATAROOTDIR]``
| ``  --infodir=DIR           info documentation [DATAROOTDIR/info]``
| ``  --localedir=DIR         locale-dependent data [DATAROOTDIR/locale]``
| ``  --mandir=DIR            man documentation [DATAROOTDIR/man]``
| ``  --docdir=DIR            documentation root [DATAROOTDIR/doc/vlc]``
| ``  --htmldir=DIR           html documentation [DOCDIR]``
| ``  --dvidir=DIR            dvi documentation [DOCDIR]``
| ``  --pdfdir=DIR            pdf documentation [DOCDIR]``
| ``  --psdir=DIR             ps documentation [DOCDIR]``
| ````
| ``Program names:``
| ``  --program-prefix=PREFIX            prepend PREFIX to installed program names``
| ``  --program-suffix=SUFFIX            append SUFFIX to installed program names``
| ``  --program-transform-name=PROGRAM   run sed PROGRAM on installed program names``
| ````
| ``X features:``
| ``  --x-includes=DIR    X include files are in DIR``
| ``  --x-libraries=DIR   X library files are in DIR``
| ````
| ``System types:``
| ``  --build=BUILD     configure for building on BUILD [guessed]``
| ``  --host=HOST       cross-compile to build programs to run on HOST [BUILD]``
| ````
| ``Optional Features and Packages:``
| ``  --disable-option-checking  ignore unrecognized --enable/--with options``
| ``  --disable-FEATURE       do not include FEATURE (same as --enable-FEATURE=no)``
| ``  --enable-FEATURE[=ARG]  include FEATURE [ARG=yes]``
| ``  --with-PACKAGE[=ARG]    use PACKAGE [ARG=yes]``
| ``  --without-PACKAGE       do not use PACKAGE (same as --with-PACKAGE=no)``
| :literal:`  --enable-silent-rules          less verbose build output (undo: `make V=1')`
| :literal:`  --disable-silent-rules         verbose build output (undo: `make V=0')`
| ``  --enable-maintainer-mode  enable make rules and dependencies not useful``
| ``              (and sometimes confusing) to the casual installer``
| ``  --disable-dependency-tracking  speeds up one-time build``
| ``  --enable-dependency-tracking   do not reject slow dependency extractors``
| ``  --with-binary-version=STRING``
| ``                          To avoid plugins cache problem between binary``
| ``                          version``
| ``  --with-macosx-sdk=DIR   compile using the SDK in DIR``
| ``  --with-macosx-version-min=VERSION``
| ``                          compile for MacOS X VERSION and above``
| ``  --with-contrib=DIR      search for 3rd party libraries in DIR/include and``
| ``                          DIR/lib``
| ````
| ``  --enable-shared[=PKGS]  build shared libraries [default=yes]``
| ``  --enable-static[=PKGS]  build static libraries [default=no]``
| ``  --with-pic              try to use only PIC/non-PIC objects [default=use``
| ``                          both]``
| ``  --enable-fast-install[=PKGS]``
| ``                          optimize for fast installation [default=yes]``
| ``  --with-gnu-ld           assume the C compiler uses GNU ld [default=no]``
| ``  --with-sysroot=DIR Search for dependent libraries within DIR``
| ``                        (or the compiler's sysroot if not specified).``
| ``  --disable-libtool-lock  avoid locking (might break parallel builds)``
| ``  --disable-nls           do not use Native Language Support``
| ``  --with-gnu-ld           assume the C compiler uses GNU ld default=no``
| ``  --disable-rpath         do not hardcode runtime library paths``
| ``  --with-libiconv-prefix[=DIR]  search for libiconv in DIR/include and DIR/lib``
| ``  --without-libiconv-prefix     don't search for libiconv in includedir and libdir``
| ``  --with-libintl-prefix[=DIR]  search for libintl in DIR/include and DIR/lib``
| ``  --without-libintl-prefix     don't search for libintl in includedir and libdir``
| ``  --enable-dbus           compile D-Bus message bus support (default enabled)``
| ``  --disable-dbus-control  D-Bus control interface (default enabled)``
| ``  --enable-telepathy      Telepathy Presence plugin through DBus(default``
| ``                          enabled)``
| ``Optimization options:``
| ``  --enable-debug          build with run-time assertions (default disabled)``
| ``  --enable-gprof          profile with gprof (default disabled)``
| ``  --enable-cprof          profile with cprof (default disabled)``
| ``  --enable-coverage       build for test coverage (default disabled)``
| ``  --disable-optimizations disable compiler optimizations (default enabled)``
| ``  --disable-mmx           disable MMX optimizations (default auto)``
| ``  --disable-sse           disable SSE (1-4) optimizations (default auto)``
| ``  --disable-neon          disable NEON optimizations (default auto)``
| ``  --disable-altivec       disable AltiVec optimizations (default auto)``
| ``  --enable-optimize-memory``
| ``                          optimize memory usage over performance``
| ``  --enable-run-as-root    allow running VLC as root (default disabled)``
| ``  --disable-sout          disable streaming output (default enabled)``
| ``  --disable-lua           disable LUA scripting support (default enabled)``
| ``  --disable-httpd         disable the built-in HTTP server (default enabled)``
| ``  --disable-vlm           disable the stream manager (default enabled)``
| ``Input plugins:``
| ``  --enable-libproxy       support libproxy (default auto)``
| ``  --enable-live555        enable RTSP input through live555 (default enabled)``
| ``  --enable-dc1394         IIDC FireWire input module [default=auto]``
| ``  --enable-dv1394         DV FireWire input module [default=auto]``
| ``  --enable-linsys         Linux Linear Systems Ltd. SDI and HD-SDI input cards``
| ``                          (default enabled)``
| ``  --enable-dvdread        dvdread input module [default=auto]``
| ``  --disable-dvdnav        disable DVD navigation with libdvdnav (default auto)``
| ``  --disable-dshow         support DirectShow (default auto)``
| ``  --enable-bluray         (libbluray for Blu-ray disc support ) [default=auto]``
| ``  --enable-opencv         (OpenCV (computer vision) filter) [default=off]``
| ``  --disable-smb           disable SMB/CIFS support (default auto)``
| ``  --enable-sftp           support SFTP file transfer via libssh2 (default``
| ``                          disabled)``
| ``  --disable-v4l2          disable Video4Linux version 2 (default auto)``
| ``  --enable-pvr            support PVR V4L2 cards (default disabled)``
| ``  --disable-decklink      disable Blackmagic DeckLink SDI input (default auto)``
| ``                          --with-decklink-sdk=DIR,``
| ``                            location of Blackmagic DeckLink SDI SDK)``
| ``  --enable-gnomevfs       GnomeVFS access module [default=auto]``
| ``  --enable-vcdx           navigate VCD with libvcdinfo (default disabled)``
| ``  --disable-vcd           disable built-in VCD and CD-DA support (default``
| ``                          enabled)``
| ``  --disable-libcddb       disable CDDB for Audio CD (default enabled)``
| ``  --enable-screen         disable screen capture (default enabled)``
| ``  --enable-realrtsp       Real RTSP module (default disabled)``
| ``  --enable-macosx-eyetv   Mac OS X EyeTV (TNT Tuner) module (default enabled on Mac OS X)``
| ``  --enable-macosx-qtkit Mac OS X qtcapture (video) and qtsound (audio) module (default enabled on Mac OS X)``
| ``Mux/Demux plugins:``
| ``  --enable-dvbpsi         build with dvbpsi support enabled [default=auto]``
| ``  --enable-gme            use Game Music Emu (default auto)``
| ``  --enable-sid            C64 sid demux support (default auto)``
| ``  --enable-ogg            Ogg demux support [default=auto]``
| ``  --enable-mux_ogg        Ogg mux support [default=auto]``
| ``  --enable-shout          libshout output plugin [default=auto]``
| ``  --disable-mkv           do not use libmatroska (default auto)``
| ``  --disable-mod           do not use libmodplug (default auto)``
| ``  --disable-mpc           do not use libmpcdec (default auto)``
| ``Codec plugins:``
| ``  --enable-wma-fixed      libwma-fixed module (default disabled)``
| ``  --enable-shine          shine mp3 encoding module (default disabled)``
| ``  --enable-omxil          openmax il codec module (default disabled)``
| ``  --enable-iomx           iomx codec module (default disabled)``
| ``  --enable-crystalhd      crystalhd codec plugin (default auto)``
| ``  --enable-mad            libmad module (default enabled)``
| ``  --with-mad=PATH         path to libmad``
| ``  --with-mad-tree=PATH    mad tree for static linking``
| ``  --enable-merge-ffmpeg   merge FFmpeg-based plugins (default disabled)``
| ``  --enable-avcodec        libavcodec codec (default enabled)``
| ``  --enable-libva          VAAPI GPU decoding support (libVA) (default auto)``
| ``  --enable-dxva2          DxVA2 GPU decoding support (default auto)``
| ``  --enable-switcher       Stream-out switcher plugin (default disabled)``
| ``  --enable-avformat       libavformat containers (default enabled)``
| ``  --enable-swscale        libswscale image scaling and conversion (default``
| ``                          enabled)``
| ``  --enable-postproc       libpostproc image post-processing (default enabled)``
| ``  --enable-faad           faad codec (default auto)``
| ``  --with-faad-tree=PATH   faad tree for static linking``
| ``  --enable-twolame        MPEG Audio Layer 2 encoder [default=auto]``
| ``  --enable-quicktime      QuickTime module (deprecated)``
| ``  --enable-a52            A/52 support with liba52 (default enabled)``
| ``  --with-a52=PATH         a52 headers and libraries``
| ``  --with-a52-tree=PATH    a52dec tree for static linking``
| ``  --with-a52-fixed        specify if liba52 has been compiled with fixed point support``
| ``  --enable-dca            DTS Coherent Acoustics support with libdca``
| ``                          [default=auto]``
| ``  --enable-flac           libflac decoder/encoder support [default=auto]``
| ``  --enable-libmpeg2       libmpeg2 decoder support [default=auto]``
| ``  --enable-vorbis         Vorbis decoder and encoder [default=auto]``
| ``  --enable-tremor         Tremor decoder support (default disabled)``
| ``  --enable-speex          Speex support [default=auto]``
| ``  --enable-theora         experimental theora codec [default=auto]``
| ``  --enable-dirac          dirac encoder [default=auto]``
| ``  --enable-schroedinger   dirac decoder and encoder using schroedinger``
| ``                          [default=auto]``
| ``  --enable-png            PNG support (default enabled)``
| ``  --enable-x26410b           H264 10-bit encoding support with static libx264 (default disabled)``
| `` --with-x26410b-tree=PATH      H264 10-bit encoding module with libx264 (static linking)``
| ``  --enable-x264           H264 encoding support with libx264 (default enabled)``
| ``  --with-x264-tree=PATH   x264 tree for static linking``
| ``  --enable-fluidsynth     MIDI synthetiser with libfluidsynth [default=auto]``
| ``  --enable-zvbi           VBI (inc. Teletext) decoding support with libzvbi``
| ``                          (default enabled)``
| ``  --enable-telx           Teletext decoding module (conflicting with zvbi)``
| ``                          (default enabled if zvbi is absent)``
| ``  --enable-libass         Subtitle support using libass (default enabled)``
| ``  --enable-kate           kate codec [default=auto]``
| ``  --enable-tiger          Tiger rendering library for Kate streams (default auto)``
| ``Video plugins:``
| ``  --enable-egl            OpenGL support through EGL (default disabled)``
| ``  --with-x                use the X Window System``
| ``  --enable-xcb            X11 support with XCB (default enabled)``
| ``  --enable-xvideo         XVideo support (default enabled)``
| ``  --enable-glx            OpenGL support through GLX (default enabled)``
| ``  --enable-sdl            SDL support (default enabled)``
| ``  --enable-sdl-image      SDL image support (default enabled)``
| ``  --enable-macosx-vout    Mac OS X video output module (default enabled on Mac OS X)``
| ``  --enable-freetype       freetype support   (default auto)``
| ``  --enable-fribidi        fribidi support    (default auto)``
| ``  --enable-fontconfig     fontconfig support (default auto)``
| ``  --enable-macosx-quartztext   Mac OS X quartz text module (default enabled on Mac OS X)``
| ``  --enable-svg            SVG rendering library [default=auto]``
| ``  --enable-android-surface   Android Surface video output module (default disabled)``
| ``  --enable-ios-vout    iOS video output module (default disabled)``
| ``  --enable-directx        Win32 DirectX support (default enabled on Win32)``
| ``  --enable-direct2d       Win7/VistaPU Direct2D support (default auto on Win32)``
| ``  --enable-wingdi         Win32 GDI module (default enabled on Win32)``
| ``  --enable-directfb       DirectFB support (default disabled)``
| ``  --with-directfb=PATH    path to DirectFB headers and libraries``
| ``  --enable-aa             aalib output (default disabled)``
| ``  --enable-caca           libcaca output [default=auto]``
| ``  --enable-kva            support the K Video Accelerator KVA (default enabled``
| ``                          on OS/2)``
| ``Audio plugins:``
| ``  --enable-pulse          use the PulseAudio client library (default auto)``
| ``  --enable-alsa           support the Advanced Linux Sound Architecture``
| ``                          (default auto)``
| ``  --enable-oss            support the Open Sound System OSS (default enabled``
| ``                          on FreeBSD/NetBSD/DragonFlyBSD)``
| ``  --disable-sndio         support the OpenBSD sndio (default auto)``
| ``  --enable-wasapi         use the Windows Audio Session API (default auto)``
| ````
| ``  --enable-waveout        Win32 waveOut module (default enabled on Win32)``
| ``  --enable-macosx-audio   Mac OS X audio module (default enabled on MacOS X)``
| ``  --enable-audioqueue     AudioQueue audio module (default disabled)``
| ``  --enable-jack           JACK audio I/O modules [default=auto]``
| ``  --enable-opensles       Android OpenSL ES audio module (default disabled)``
| ``  --enable-samplerate     Resampler with libsamplerate [default=auto]``
| ``  --enable-kai            support the K Audio Interface KAI (default enabled``
| ``                          on OS/2)``
| ``Interface plugins:``
| ``  --enable-hildon         Hildon touchscreen UI (default disabled)``
| ``  --enable-qt4            Qt 4 support (default enabled)``
| ``  --enable-skins2         skins interface module (default auto)``
| ``  --enable-libtar         libtar support for skins2 (default auto)``
| ``  --enable-macosx         Mac OS X gui support (default enabled on Mac OS X)``
| ``  --enable-macosx-dialog-provider Mac OS X dialog module (default enabled on Mac OS X)``
| ``  --disable-ncurses       ncurses text-based interface (default auto)``
| ``  --enable-lirc           lirc support (default disabled)``
| ``Visualisations and Video filter plugins:``
| ``  --enable-visual         visualisation plugin (default enabled)``
| ``  --enable-goom           goom visualization plugin [default=auto]``
| ``  --enable-projectm       projectM visualization plugin (default enabled)``
| ``  --enable-vsxu           Vovoid VSXu visualization plugin (default auto)``
| ``  --disable-atmo          AtmoLight (homemade Philips Ambilight clone)``
| ``                          (default enabled)``
| ``Service Discovery plugins:``
| ``  --enable-bonjour        Bonjour services discovery [default=auto]``
| ``  --enable-udev           Linux udev services discovery [default=auto]``
| ``  --enable-mtp            MTP devices support [default=auto]``
| ``  --enable-upnp           Intel UPNP SDK [default=auto]``
| ``Misc options:``
| ``  --enable-libxml2        libxml2 support [default=auto]``
| ``  --disable-libgcrypt     gcrypt support (default enabled)``
| ``  --enable-gnutls         GNU TLS TLS/SSL support (default enabled)``
| ``  --disable-taglib        do not use TagLib (default enabled)``
| ``  --enable-update-check   update checking system (default disabled)``
| ``  --enable-growl          growl notification plugin (default disabled)``
| ``  --enable-notify         libnotify notification [default=auto]``
| ``  --enable-media-library  media library (default disabled)``
| ``  --enable-sqlite         sqlite3 [default=auto]``
| ``  --with-kde-solid=PATH   KDE Solid actions directory (auto)``
| ``  --enable-loader         build DLL loader for ELF i386 platforms (default``
| ``                          disabled)``
| ``Components:``
| ``  --enable-vlc            build the VLC media player (default enabled)``
| ``  --enable-macosx-vlc-app build the VLC media player (default enabled on Mac OS X)``
| ````
| ``Some influential environment variables:``
| ``  CC          C compiler command``
| ``  CFLAGS      C compiler flags``
| ``  LDFLAGS     linker flags, e.g. -L<lib dir> if you have libraries in a``
| ``              nonstandard directory <lib dir>``
| ``  LIBS        libraries to pass to the linker, e.g. -l<library>``
| ``  CPPFLAGS    (Objective) C/C++ preprocessor flags, e.g. -I<include dir> if``
| ``              you have headers in a nonstandard directory <include dir>``
| ``  CPP         C preprocessor``
| ``  CXX         C++ compiler command``
| ``  CXXFLAGS    C++ compiler flags``
| ``  OBJC        Objective C compiler command``
| ``  OBJCFLAGS   Objective C compiler flags``
| ``  CCAS        assembler compiler command (defaults to CC)``
| ``  CCASFLAGS   assembler compiler flags (defaults to CFLAGS)``
| ``  DESKTOP_FILE_VALIDATE``
| ``              Validator for desktop entry files``
| ``  CXXCPP      C++ preprocessor``
| ``  PKG_CONFIG_PATH``
| ``              Paths where to find .pc not at the default location``
| ``  PKG_CONFIG  path to pkg-config utility``
| ``  PKG_CONFIG_LIBDIR``
| ``              path overriding pkg-config's built-in search path``
| ``  MINIZIP_CFLAGS``
| ``              C compiler flags for MINIZIP, overriding pkg-config``
| ``  MINIZIP_LIBS``
| ``              linker flags for MINIZIP, overriding pkg-config``
| ``  DBUS_CFLAGS C compiler flags for DBUS, overriding pkg-config``
| ``  DBUS_LIBS   linker flags for DBUS, overriding pkg-config``
| ``  LUA_CFLAGS  C compiler flags for LUA, overriding pkg-config``
| ``  LUA_LIBS    linker flags for LUA, overriding pkg-config``
| ``  LUAC        LUA byte compiler``
| ``  LIBPROXY_CFLAGS``
| ``              C compiler flags for LIBPROXY, overriding pkg-config``
| ``  LIBPROXY_LIBS``
| ``              linker flags for LIBPROXY, overriding pkg-config``
| ``  DC1394_CFLAGS``
| ``              C compiler flags for DC1394, overriding pkg-config``
| ``  DC1394_LIBS linker flags for DC1394, overriding pkg-config``
| ``  DV1394_CFLAGS``
| ``              C compiler flags for DV1394, overriding pkg-config``
| ``  DV1394_LIBS linker flags for DV1394, overriding pkg-config``
| ``  LINSYS_SDI_CFLAGS``
| ``              C compiler flags for LINSYS_SDI, overriding pkg-config``
| ``  LINSYS_SDI_LIBS``
| ``              linker flags for LINSYS_SDI, overriding pkg-config``
| ``  DVDREAD_CFLAGS``
| ``              C compiler flags for DVDREAD, overriding pkg-config``
| ``  DVDREAD_LIBS``
| ``              linker flags for DVDREAD, overriding pkg-config``
| ``  DVDNAV_CFLAGS``
| ``              C compiler flags for DVDNAV, overriding pkg-config``
| ``  DVDNAV_LIBS linker flags for DVDNAV, overriding pkg-config``
| ``  BLURAY_CFLAGS``
| ``              C compiler flags for BLURAY, overriding pkg-config``
| ``  BLURAY_LIBS linker flags for BLURAY, overriding pkg-config``
| ``  OPENCV_CFLAGS``
| ``              C compiler flags for OPENCV, overriding pkg-config``
| ``  OPENCV_LIBS linker flags for OPENCV, overriding pkg-config``
| ``  GNOMEVFS_CFLAGS``
| ``              C compiler flags for GNOMEVFS, overriding pkg-config``
| ``  GNOMEVFS_LIBS``
| ``              linker flags for GNOMEVFS, overriding pkg-config``
| ``  LIBCDIO_CFLAGS``
| ``              C compiler flags for LIBCDIO, overriding pkg-config``
| ``  LIBCDIO_LIBS``
| ``              linker flags for LIBCDIO, overriding pkg-config``
| ``  LIBVCDINFO_CFLAGS``
| ``              C compiler flags for LIBVCDINFO, overriding pkg-config``
| ``  LIBVCDINFO_LIBS``
| ``              linker flags for LIBVCDINFO, overriding pkg-config``
| ``  LIBCDDB_CFLAGS``
| ``              C compiler flags for LIBCDDB, overriding pkg-config``
| ``  LIBCDDB_LIBS``
| ``              linker flags for LIBCDDB, overriding pkg-config``
| ``  DVBPSI_CFLAGS``
| ``              C compiler flags for DVBPSI, overriding pkg-config``
| ``  DVBPSI_LIBS linker flags for DVBPSI, overriding pkg-config``
| ``  SID_CFLAGS  C compiler flags for SID, overriding pkg-config``
| ``  SID_LIBS    linker flags for SID, overriding pkg-config``
| ``  OGG_CFLAGS  C compiler flags for OGG, overriding pkg-config``
| ``  OGG_LIBS    linker flags for OGG, overriding pkg-config``
| ``  MUX_OGG_CFLAGS``
| ``              C compiler flags for MUX_OGG, overriding pkg-config``
| ``  MUX_OGG_LIBS``
| ``              linker flags for MUX_OGG, overriding pkg-config``
| ``  SHOUT_CFLAGS``
| ``              C compiler flags for SHOUT, overriding pkg-config``
| ``  SHOUT_LIBS  linker flags for SHOUT, overriding pkg-config``
| ``  LIBMODPLUG_CFLAGS``
| ``              C compiler flags for LIBMODPLUG, overriding pkg-config``
| ``  LIBMODPLUG_LIBS``
| ``              linker flags for LIBMODPLUG, overriding pkg-config``
| ``  AVCODEC_CFLAGS``
| ``              C compiler flags for AVCODEC, overriding pkg-config``
| ``  AVCODEC_LIBS``
| ``              linker flags for AVCODEC, overriding pkg-config``
| ``  LIBVA_CFLAGS``
| ``              C compiler flags for LIBVA, overriding pkg-config``
| ``  LIBVA_LIBS  linker flags for LIBVA, overriding pkg-config``
| ``  AVFORMAT_CFLAGS``
| ``              C compiler flags for AVFORMAT, overriding pkg-config``
| ``  AVFORMAT_LIBS``
| ``              linker flags for AVFORMAT, overriding pkg-config``
| ``  SWSCALE_CFLAGS``
| ``              C compiler flags for SWSCALE, overriding pkg-config``
| ``  SWSCALE_LIBS``
| ``              linker flags for SWSCALE, overriding pkg-config``
| ``  POSTPROC_CFLAGS``
| ``              C compiler flags for POSTPROC, overriding pkg-config``
| ``  POSTPROC_LIBS``
| ``              linker flags for POSTPROC, overriding pkg-config``
| ``  TWOLAME_CFLAGS``
| ``              C compiler flags for TWOLAME, overriding pkg-config``
| ``  TWOLAME_LIBS``
| ``              linker flags for TWOLAME, overriding pkg-config``
| ``  DCA_CFLAGS  C compiler flags for DCA, overriding pkg-config``
| ``  DCA_LIBS    linker flags for DCA, overriding pkg-config``
| ``  FLAC_CFLAGS C compiler flags for FLAC, overriding pkg-config``
| ``  FLAC_LIBS   linker flags for FLAC, overriding pkg-config``
| ``  LIBMPEG2_CFLAGS``
| ``              C compiler flags for LIBMPEG2, overriding pkg-config``
| ``  LIBMPEG2_LIBS``
| ``              linker flags for LIBMPEG2, overriding pkg-config``
| ``  VORBIS_CFLAGS``
| ``              C compiler flags for VORBIS, overriding pkg-config``
| ``  VORBIS_LIBS linker flags for VORBIS, overriding pkg-config``
| ``  SPEEX_CFLAGS``
| ``              C compiler flags for SPEEX, overriding pkg-config``
| ``  SPEEX_LIBS  linker flags for SPEEX, overriding pkg-config``
| ``  SPEEXDSP_CFLAGS``
| ``              C compiler flags for SPEEXDSP, overriding pkg-config``
| ``  SPEEXDSP_LIBS``
| ``              linker flags for SPEEXDSP, overriding pkg-config``
| ``  THEORA_CFLAGS``
| ``              C compiler flags for THEORA, overriding pkg-config``
| ``  THEORA_LIBS linker flags for THEORA, overriding pkg-config``
| ``  DIRAC_CFLAGS``
| ``              C compiler flags for DIRAC, overriding pkg-config``
| ``  DIRAC_LIBS  linker flags for DIRAC, overriding pkg-config``
| ``  SCHROEDINGER_CFLAGS``
| ``              C compiler flags for SCHROEDINGER, overriding pkg-config``
| ``  SCHROEDINGER_LIBS``
| ``              linker flags for SCHROEDINGER, overriding pkg-config``
| ``  X26410B_CFLAGS``
| ``              C compiler flags for X26410B, overriding pkg-config``
| ``  X26410B_LIBS``
| ``              linker flags for X26410B, overriding pkg-config``
| ``  X264_CFLAGS C compiler flags for X264, overriding pkg-config``
| ``  X264_LIBS   linker flags for X264, overriding pkg-config``
| ``  FLUIDSYNTH_CFLAGS``
| ``              C compiler flags for FLUIDSYNTH, overriding pkg-config``
| ``  FLUIDSYNTH_LIBS``
| ``              linker flags for FLUIDSYNTH, overriding pkg-config``
| ``  ZVBI_CFLAGS C compiler flags for ZVBI, overriding pkg-config``
| ``  ZVBI_LIBS   linker flags for ZVBI, overriding pkg-config``
| ``  LIBASS_CFLAGS``
| ``              C compiler flags for LIBASS, overriding pkg-config``
| ``  LIBASS_LIBS linker flags for LIBASS, overriding pkg-config``
| ``  KATE_CFLAGS C compiler flags for KATE, overriding pkg-config``
| ``  KATE_LIBS   linker flags for KATE, overriding pkg-config``
| ``  TIGER_CFLAGS``
| ``              C compiler flags for TIGER, overriding pkg-config``
| ``  TIGER_LIBS  linker flags for TIGER, overriding pkg-config``
| ``  GL_CFLAGS   C compiler flags for GL, overriding pkg-config``
| ``  GL_LIBS     linker flags for GL, overriding pkg-config``
| ``  EGL_CFLAGS  C compiler flags for EGL, overriding pkg-config``
| ``  EGL_LIBS    linker flags for EGL, overriding pkg-config``
| ``  XMKMF       Path to xmkmf, Makefile generator for X Window System``
| ``  XCB_CFLAGS  C compiler flags for XCB, overriding pkg-config``
| ``  XCB_LIBS    linker flags for XCB, overriding pkg-config``
| ``  XCB_SHM_CFLAGS``
| ``              C compiler flags for XCB_SHM, overriding pkg-config``
| ``  XCB_SHM_LIBS``
| ``              linker flags for XCB_SHM, overriding pkg-config``
| ``  XCB_COMPOSITE_CFLAGS``
| ``              C compiler flags for XCB_COMPOSITE, overriding pkg-config``
| ``  XCB_COMPOSITE_LIBS``
| ``              linker flags for XCB_COMPOSITE, overriding pkg-config``
| ``  XCB_XV_CFLAGS``
| ``              C compiler flags for XCB_XV, overriding pkg-config``
| ``  XCB_XV_LIBS linker flags for XCB_XV, overriding pkg-config``
| ``  XCB_RANDR_CFLAGS``
| ``              C compiler flags for XCB_RANDR, overriding pkg-config``
| ``  XCB_RANDR_LIBS``
| ``              linker flags for XCB_RANDR, overriding pkg-config``
| ``  XCB_KEYSYMS_CFLAGS``
| ``              C compiler flags for XCB_KEYSYMS, overriding pkg-config``
| ``  XCB_KEYSYMS_LIBS``
| ``              linker flags for XCB_KEYSYMS, overriding pkg-config``
| ``  XPROTO_CFLAGS``
| ``              C compiler flags for XPROTO, overriding pkg-config``
| ``  XPROTO_LIBS linker flags for XPROTO, overriding pkg-config``
| ``  SDL_CFLAGS  C compiler flags for SDL, overriding pkg-config``
| ``  SDL_LIBS    linker flags for SDL, overriding pkg-config``
| ``  SDL_IMAGE_CFLAGS``
| ``              C compiler flags for SDL_IMAGE, overriding pkg-config``
| ``  SDL_IMAGE_LIBS``
| ``              linker flags for SDL_IMAGE, overriding pkg-config``
| ``  FREETYPE_CFLAGS``
| ``              C compiler flags for FREETYPE, overriding pkg-config``
| ``  FREETYPE_LIBS``
| ``              linker flags for FREETYPE, overriding pkg-config``
| ``  FRIBIDI_CFLAGS``
| ``              C compiler flags for FRIBIDI, overriding pkg-config``
| ``  FRIBIDI_LIBS``
| ``              linker flags for FRIBIDI, overriding pkg-config``
| ``  SVG_CFLAGS  C compiler flags for SVG, overriding pkg-config``
| ``  SVG_LIBS    linker flags for SVG, overriding pkg-config``
| ``  DIRECTFB_CFLAGS``
| ``              C compiler flags for DIRECTFB, overriding pkg-config``
| ``  DIRECTFB_LIBS``
| ``              linker flags for DIRECTFB, overriding pkg-config``
| ``  CACA_CFLAGS C compiler flags for CACA, overriding pkg-config``
| ``  CACA_LIBS   linker flags for CACA, overriding pkg-config``
| ``  PULSE_CFLAGS``
| ``              C compiler flags for PULSE, overriding pkg-config``
| ``  PULSE_LIBS  linker flags for PULSE, overriding pkg-config``
| ``  ALSA_CFLAGS C compiler flags for ALSA, overriding pkg-config``
| ``  ALSA_LIBS   linker flags for ALSA, overriding pkg-config``
| ``  JACK_CFLAGS C compiler flags for JACK, overriding pkg-config``
| ``  JACK_LIBS   linker flags for JACK, overriding pkg-config``
| ``  SAMPLERATE_CFLAGS``
| ``              C compiler flags for SAMPLERATE, overriding pkg-config``
| ``  SAMPLERATE_LIBS``
| ``              linker flags for SAMPLERATE, overriding pkg-config``
| ``  HILDON_CFLAGS``
| ``              C compiler flags for HILDON, overriding pkg-config``
| ``  HILDON_LIBS linker flags for HILDON, overriding pkg-config``
| ``  HILDON_FM_CFLAGS``
| ``              C compiler flags for HILDON_FM, overriding pkg-config``
| ``  HILDON_FM_LIBS``
| ``              linker flags for HILDON_FM, overriding pkg-config``
| ``  QT4_CFLAGS  C compiler flags for QT4, overriding pkg-config``
| ``  QT4_LIBS    linker flags for QT4, overriding pkg-config``
| ``  XPM_CFLAGS  C compiler flags for XPM, overriding pkg-config``
| ``  XPM_LIBS    linker flags for XPM, overriding pkg-config``
| ``  XINERAMA_CFLAGS``
| ``              C compiler flags for XINERAMA, overriding pkg-config``
| ``  XINERAMA_LIBS``
| ``              linker flags for XINERAMA, overriding pkg-config``
| ``  XEXT_CFLAGS C compiler flags for XEXT, overriding pkg-config``
| ``  XEXT_LIBS   linker flags for XEXT, overriding pkg-config``
| ``  GOOM_CFLAGS C compiler flags for GOOM, overriding pkg-config``
| ``  GOOM_LIBS   linker flags for GOOM, overriding pkg-config``
| ``  PROJECTM_CFLAGS``
| ``              C compiler flags for PROJECTM, overriding pkg-config``
| ``  PROJECTM_LIBS``
| ``              linker flags for PROJECTM, overriding pkg-config``
| ``  PROJECTM2_CFLAGS``
| ``              C compiler flags for PROJECTM2, overriding pkg-config``
| ``  PROJECTM2_LIBS``
| ``              linker flags for PROJECTM2, overriding pkg-config``
| ``  VSXU_CFLAGS C compiler flags for VSXU, overriding pkg-config``
| ``  VSXU_LIBS   linker flags for VSXU, overriding pkg-config``
| ``  BONJOUR_CFLAGS``
| ``              C compiler flags for BONJOUR, overriding pkg-config``
| ``  BONJOUR_LIBS``
| ``              linker flags for BONJOUR, overriding pkg-config``
| ``  UDEV_CFLAGS C compiler flags for UDEV, overriding pkg-config``
| ``  UDEV_LIBS   linker flags for UDEV, overriding pkg-config``
| ``  MTP_CFLAGS  C compiler flags for MTP, overriding pkg-config``
| ``  MTP_LIBS    linker flags for MTP, overriding pkg-config``
| ``  UPNP_CFLAGS C compiler flags for UPNP, overriding pkg-config``
| ``  UPNP_LIBS   linker flags for UPNP, overriding pkg-config``
| ``  LIBXML2_CFLAGS``
| ``              C compiler flags for LIBXML2, overriding pkg-config``
| ``  LIBXML2_LIBS``
| ``              linker flags for LIBXML2, overriding pkg-config``
| ``  GNUTLS_CFLAGS``
| ``              C compiler flags for GNUTLS, overriding pkg-config``
| ``  GNUTLS_LIBS linker flags for GNUTLS, overriding pkg-config``
| ``  MCE_CFLAGS  C compiler flags for MCE, overriding pkg-config``
| ``  MCE_LIBS    linker flags for MCE, overriding pkg-config``
| ``  TAGLIB_CFLAGS``
| ``              C compiler flags for TAGLIB, overriding pkg-config``
| ``  TAGLIB_LIBS linker flags for TAGLIB, overriding pkg-config``
| ``  NOTIFY_CFLAGS``
| ``              C compiler flags for NOTIFY, overriding pkg-config``
| ``  NOTIFY_LIBS linker flags for NOTIFY, overriding pkg-config``
| ``  SQLITE_CFLAGS``
| ``              C compiler flags for SQLITE, overriding pkg-config``
| ``  SQLITE_LIBS linker flags for SQLITE, overriding pkg-config``
| ``  KDE4_CONFIG kde4-config utility``
| ````
| :literal:`Use these variables to override the choices made by `configure' or to help`
| ``it to find libraries and programs with nonstandard names/locations.``

`Category:Building <Category:Building>`__ `Category:GNU/Linux <Category:GNU/Linux>`__
