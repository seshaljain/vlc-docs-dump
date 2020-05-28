Compile VLC on BeOS

== Required tools == You need : \* [http://www.bebits.com/app/2680 BeOS
5] with development tools \* [http://www.bebits.com/app/1610 CVS 1.11]
\* Git \* [http://www.bebits.com/app/3218 bzip2/bunzip2] \*
[http://www.bebits.com/app/2848 wget] \* [http://www.bebits.com/app/4011
gcc 2.95.3]

Compiling is usually done on a vanilla R5.0.3 install with gcc 2.95.3.

Building with older compilers won't work.

Building on a BONE-enabled install probably doesn't work at the moment.

== Build VLC == Now you can compile vlc:

=== Get the source === Download the {{VLC}} [[GetTheSource "Get the
source"]] page.

=== Build external libs ===

We now need to build the [[Contrib_Status\| 3rd party libs]]. For that,
you will need to: \* cd to the source directory with your Terminal
application. \* cd to extras/contrib/ subdir of VLC and execute
<code>./bootstrap</code> \* Now execute <code>make src</code>. This will
download and compile all the required external libraries and programs
that {{VLC}} needs (you need an internet connection, a fast one
preferably).

=== Prepare the VLC build === Now we return to VLC itself. Go back to
the top level VLC source directory. If you use Git (which you really
should), then run <code>./bootstrap</code>.

This will create configure and Makefiles for {{VLC}} (snapshots and
releases already include this).

=== Configure VLC === The next step is to configure, in the top level
VLC source directory.

<code>./configure --enable-debug --enable-sout --enable-httpd
--enable-vlm --enable-dvdread --enable-dvdnav --enable-dvbpsi
--enable-screen --enable-ogg --enable-mkv --enable-mad --enable-ffmpeg
--enable-faad --enable-a52 --enable-flac --enable-libmpeg2
--enable-vorbis --enable-speex --enable-theora --enable-freetype
--enable-fribidi --disable-skins2 --with-ffmpeg-mp3lame
--with-ffmpeg-faac --with-ffmpeg-zlib --disable-x11 --disable-hal
--disable-daap --disable-xvideo --disable-glx --disable-sdl
--disable-wxwindows</code>

=== Build VLC === After configure is finished, we can finally build
{{VLC}}. A simple <code>make</code> will do the trick.

To build a package, run <code>make package-beos</code>.

== History == Written by Eric Petit, for the VideoLAN Team. Adapted to
the Wiki by [[User:j-b|Jean-Baptiste Kempf]].

[[Category:Building]] [[Category:Coding]] {{Outdated}}
