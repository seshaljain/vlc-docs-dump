{{wikipedia|Video Acceleration API}}

== Introduction to GPU decoding in VLC == {{See also|VLC GPU Decoding}}

The VLC framework can use your '''''graphic card''''' (aka GPU) to
decode H.264 streams (wrongly called HD&nbsp;videos) under certain
circumstances.

VLC, in its '''modular''' approach and its transcoding/streaming
capabilities, does decoding in GPU at the '''decoding stage only''' and
then gets the data back to go to the other stages (streaming, filtering
or plug any video output after that).

What that means is that, compared to some other implementation, GPU
decoding in VLC can be slower because it needs to get the ''data back
from the GPU''. But you can plug '''ANY''' video output (sink) to it and
use '''all '''the VLC video filters.

== Introduction to compilation of VAAPI in VLC ==

This page is about compiling VLC with support of GPU acceleration on
Linux. For Windows, look at [[VLC_DxVA2]].<br>

This howto has been written by [[User:J-b|Jean-Baptiste Kempf]] and
tested with nVidia GPU.

http://www.freedesktop.org/wiki/Software/vaapi

== Before starting ==

=== libva ===

Install libva from
http://www.splitted-desktop.com/~gbeauchesne/libva/.{{dead link}} We do
not support other libraries than the one from Mr Beauchesne.

=== Drivers ===

==== nVidia ====

http://www.splitted-desktop.com/~gbeauchesne/vdpau-video/ for
nVidia.{{dead link}} Use at least version 0.6.2.

==== ATI ====

http://www.splitted-desktop.com/~gbeauchesne/xvba-video/ for ATI.{{dead
link}} Use at least 0.6.4.

Check if LIBVA environment variables are correctly configured:

   set \| grep LIBVA

Should output something like:

   LIBVA_DRIVER_NAME=xvba LIBVA_DRIVERS_PATH=/usr/lib64/va/drivers

If not, add these, according to your library path, to your system
environment variables (/etc/environment ?)

Then run

   vainfo

which should return something like:

   VAProfileH264High : VAEntrypointVLD VAProfileVC1Advanced :
   VAEntrypointVLD

To check if everything works.

=== FFmpeg trunk ===

Get the latest FFmpeg trunk as of 2010-January. Compile it with vaapi
hwaccel support.

   ./configure --enable-gpl --enable-postproc --prefix=/path/to/
   --enable-shared --enable-vaapi make make install

Copy vaapi.h to the includes, if not done (newer FFmpeg should do that
automagically)

=== VLC ===

Get VLC from [[Git]]. Get the necessary external libraries (on
debian/*buntu: apt-get build-dep vlc)

   ./bootstrap ./configure make

<br>

== Compile VLC with vaapi ==

Configure VLC.

Edit vlc-config and add

   -lX11 -lva-x11

to the avcodec line. (Step no longer required with recent builds)

Mine looks like this:

   avcodec)
      cflags="${cflags} -I/home/jb/VideoLAN/vlc/vlc/extras/ffmpeg"
      libs="${libs} /home/jb/vlc/extras/ffmpeg/libavcodec/libavcodec.a
      /home/jb/vlc/extras/ffmpeg/libavutil/libavutil.a -lz -lm -lva -ldl
      -ljack -lasound -lm -lX11 -lva-x11"

=== Recompile VLC ===

   make clean &amp;&amp; make

=== Check ===

That everything went ok:

   ./vlc --list \| grep avcodec

should return something.

== Activate ==

Activate acceleration in the preferences.

Or directly on command line

   vlc --ffmpeg-hw

Exemple: on playback log output (with -v debug and ATI VAAPI)

   [0x7f8c4cc03ba8] avcodec decoder: Using VA API version 0.32 for
   hardware decoding.

Profit

[[Category:Building]] [[Category:GNU/Linux]] [[Category:How To]]
