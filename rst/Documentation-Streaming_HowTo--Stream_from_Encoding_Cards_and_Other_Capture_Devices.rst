{{RightMenu|documentation streaming howto toc}}

==Hardware encoding cards==

Note: This is possible under GNU/Linux only.

VideoLAN supports two kinds of MPEG-2 encoding cards: \* Hauppauge
WinTV-PVR-250 and WinTV-PVR-350, \* Visiontech Kfir.

The Hauppauge WinTV-PVR-250/350 gives much better results and is cheaper
than the Visiontech Kfir.

===Stream with the Hauppauge WinTV-PVR-250/350 card=== ====Install the
drivers====

First, you will have to patch your kernel (version 2.4) to support the
v4l2 API (Video 4 Linux version 2). The patch is available on the
[http://bytesex.org/v4l/ Video4Linux HQ]. If you use a 2.6 kernel, you
only need to build I2C support and the BT848 Video For Linux module.

Once your kernel is ready, install the CK version (currently in
development) of the Linux drivers for the Hauppauge WinTV-PVR-250/350.
They are hosted on [http://67.18.1.101/~ckennedy/ivtv ivtv ck]. You will
need to patch your kernel to use it with a 2.4. You can also use the CVS
version available here: [http://ivtv.sourceforge.net/
ivtv.sourceforge.net] (this version is not developped anymore). Then,
you will have to create the device and load the modules; for this,
please refer to the documentation shipped with the drivers.

====Stream with VLC====

Note: You must add '''--enable-pvr''' to '''./configure''' to use this
feature.

   % '''vlc -vvv --color
   pvr:///dev/video0:norm=secam:size=720x576:frequency=576250:bitrate=3000000:maxbitrate=4000000
   --cr-average 1000 --sout '#rtp{mux=ts,dst=192.168.0.42,port=5004}'
   --ttl 12'''

where: *'''/dev/video0''' is the device corresponding to the encoding
card,*'''norm=secam''' is name of the standard of the analogic signal
(possible values are pal, secam, and ntsc), *'''size=720x576''' is the
size of the video you want to stream,*'''frequency=567250''' is the
frequency in kHz of the channel you want to stream,
*'''bitrate=3000000''' is the average bitrate of the
stream,*'''maxbitrate=4000000''' is the maximum bitrate of the stream,
*'''1000''' is a secret value to work around a bug of the
card.*'''192.168.0.42''' is either: **the IP address of the machine you
want to unicast to;**\ or the DNS name the machine you want to unicast
to; \*\ *or a multicast IP address.*'''12''' is the value of the TTL
(Time To Live) of your IP packets (which means that the stream will be
able to cross 11 routers).

===Stream with the Visiontech Kfir card===

====Install the drivers====

If you want to be able to stream from a Visiontech Kfir card, you need
to install its Linux drivers. Download the latest release of the drivers
from the [http://www.linuxtv.org/download/mpeg2/ drivers download page]
of the [http://www.linuxtv.org/ LinuxTV web site].

Uncompress the tarball and follow the instructions written in the
''INSTALL'' file to compile and install the drivers.

Note: If you have a VIA chipset, you need to disable USB in the BIOS.

====Stream====
   % '''vlc -vvv --color kfir:///dev/video --sout
   '#rtp{mux=ts,dst=192.168.0.42,port=5004}' --ttl 12'''

where:

*'''/dev/video''' is the device corresponding to the Kfir
card,*'''192.168.0.42''' is either : **the IP address of the machine you
want to unicast to;**\ or the DNS name the machine you want to unicast
to; \*\ *or a multicast IP address.*'''12''' is the value of the TTL
(Time To Live) of your IP packets (which means that the stream will be
able to cross 11 routers).

==Software encoding cards== ===Under GNU/Linux=== ====Install the Video
for Linux drivers====

If you want to stream from an acquisition card or a webcam, a
video4linux driver must be available for it. You can find more
information about video4linux and supported devices
[http://www.exploits.org/v4l here].

Compile the right module for your device, and insert it into your
kernel. Some video4linux modules are shipped with the 2.4.x and 2.6.x
Linux kernels, the patch is available on the [http://bytesex.org/v4l
Video4Linux HQ].

You can test your device by using any of the listed programs in the
''Video: TV and PVR/DVR'' section of [http://www.exploits.org/v4l/ this
page].

Note that v4l2 modules will also work with VLC.

====Stream with VLC====

Note: You must add '''--enable-v4l''' to '''./configure''' to use this
feature.

   % '''vlc -vvv --color
   v4l:///dev/video:norm=secam:frequency=543250:size=640x480:channel=0:adev=/dev/dsp:audio=0
   --sout
   '#transcode{vcodec=mp4v,acodec=mpga,vb=3000,ab=256,venc=ffmpeg{keyint=80,hurry-up,vt=800000},deinterlace}:rtp{mux=ts,dst=239.255.12.13,port=5004}'
   --ttl 12'''

Note: You can find all transcode options on this page :
[[Documentation:Streaming_HowTo/Advanced_Streaming_Using_the_Command_Line|Advanced
Streaming Using the Command Line]].

where: *'''/dev/video''' is the device corresponding to your acquisition
card or your webcam,*'''norm=secam''' is name of the standard of the
analogic signal (possible values are pal, secam, and ntsc),
*'''frequency=543250''' is the frequency of the channel in kHz
(''Warning:'' for VLC < 0.6.1, Frequency is channel frequency in MHz
multiplied by 16),*'''size=640x480''' is the size of the video you want
(you can also put the standard size like ''subqcif'' (128x96), ''qsif''
(160x120), ''qcif'' (176x144), ''sif'' (320x240), ''cif'' (352x288) or
''vga'' (640x480)), *'''channel=0''' is the number of the channel
(usually 0 is for tuner, 1 for composite and 2 for
svideo),*'''adev=/dev/dsp''' is the audio device, *'''audio=1''' is the
number of the audio channel (usually 0 is for mono and 1 for
stereo),*'''vcodec=mp4v''' is the video format you want to encode in
(''mp4v'' is MPEG-4, ''mpgv'' is MPEG-1, and there is also ''h263'',
''DIV1'', ''DIV2'', ''DIV3'', ''I420'', ''I422'', ''I444'', ''RV24'',
''YUY2''), *'''acodec=mpga''' is the audio format you want to encode in
(''mpga'' is MPEG audio layer 2, ''a52'' is A52 i.e. AC3
sound),*'''vb=3000''' is the video bitrate in Kbit/s *'''ab=256''' is
the audio bitrate in Kbit/s*'''venc=ffmpeg''' allows to set the encoder
to use, where: **'''keyint=80''' is the maximal amount of frames between
two key frames**'''hurry-up''' allows the encoder to decrease the
quality of the stream if the CPU can't keep up with the encoding rate
**'''vt=800000''' is the tolerance in kbit/s for the bitrate of the
outputted video \*'''deinterlace''' tells VLC to deinterlace the video
on the fly, \*'''192.168.0.42''' is either:**'''the IP address of the
machine you want to unicast to; **'''or the DNS name the machine you
want to unicast to;**'''or a multicast IP address. \*'''12''' is the
value of the TTL (Time To Live) of your IP packets (which means that the
stream will be able to cross 11 routers).

==Stream with DirectShow (Windows)==

===Install your peripheral drivers=== You need to install your
peripherals under Windows with the appropriate drivers. Nothing else is
necessary. ===Stream unicast/multicast with VLC in command line=== %
'''C:Program FilesVideoLANVLCvlc.exe -I rc --ttl 12 dshow:// vdev="VGA
USB Camera" adev="USB Camera" size="640x480"
--sout=#rtp{mux=ts,dst=239.255.42.12,port=5004}'''

Note: You either need to provide the full path to the vlc.exe executable
or add its location to the Windows Path variable.

*'''-I rc''' is to activate the remote control interface (MS/DOS
console)*'''12''' is the value of the TTL (Time To Live) of your IP
packets (which means that the stream will be able to cross 11 routers),
*'''vdev="VGA USB Camera"''' is the name of the video peripheral that
DirectShow will use (this is only an exemple),*'''adev="USB Camera"'''
is the name of the audio peripheral, *'''size="640x480"''' is the
resolution (you can also put the standard size like ''subqcif''
(128x96), ''qsif'' (160x120), ''qcif'' (176x144), ''sif'' (320x240),
''cif'' (352x288) or ''vga'' (640x480)).*'''239.255.42.12''' is either:
**the IP address of the machine you want to unicast to;**\ or the DNS
name the machine you want to unicast to; \**or a multicast IP address.

===Stream to file(s) with VLC in command line===
   % '''C:PathTovlc.exe -I rc dshow:// :dshow-vdev="Osprey-210 Video
   Device 1" :dshow-adev="Unbalanced 1 (Osprey-2X0)" :dshow-caching=200
   --sout="#duplicate{dst='transcode{vcodec=h264,vb=1260,fps=24,scale=1,width=640,height=480,acodec=mp4a,ab=96,channels=2,samplerate=44100}:std{access=file,mux=mp4,dst=C:\Path\To\File-1.mp4}',dst='transcode{vcodec=h264,vb=560,fps=24,scale=1,width=427,height=320,acodec=mp4a,ab=96,channels=2,samplerate=44100}:std{access=file,mux=mp4,dst=C:\Path\To\File-2.mp4}'}"'''

*'''-I rc''' is to activate the remote control interface (MS/DOS
console)*'''dshow://...''' configures your input capture card / settings
*'''#duplicate{}''' multiple output configurations*'''transcode{}'''
video/audio codec settings \*'''std{}''' output/muxer settings

== Mac OSX ==

Note that VLC does not support streaming from live video or audio
sources on Mac OSX.

{{Documentation}}
