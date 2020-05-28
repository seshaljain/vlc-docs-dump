.. raw:: mediawiki

   {{mux|id=flv|mod=avcodec|encoder=n}}

**Flash Video** is a file format mainly used for playing data in a Flash player on a webpage. It has the extension **.flv**.

There are two types of flv files, the one based on `H.263 <H.263>`__ (which exists since Flash 6) and another based on `VP6 <VP6>`__ (which was introduced in Flash 8). In Flash 9 Update 3 Adobe added support for MPEG-4, thus since this version flv files may also contain `H.264 <H.264>`__ and HE-\ `AAC <AAC>`__.

Compatibility
-------------

H.263 flash video is supported by the latest VLC, with some bugs. There is a `workaround <Fixing_.flv_to_.avi_with_FFmpeg>`__ using `ffmpeg <ffmpeg>`__ for this. VP6 is also supported by VLC from version 0.8.6b and above.

However, seeking, (that is, jumping to a position in the video) is not supported until 0.9.0 in either codecs.

Streaming Flash Video With VLC
------------------------------

Starting from VLC revision 18876 (which means 0.9.0-svn after 17/02/2007), you can stream flash with VLC. You also need to build VLC with a fairly recent ffmpeg version (r7593 21/01/2007 or newer).

You can then use the following command line to do HTTP Flash Video streaming:

``% ./vlc ``\ \ `` --sout "#transcode{vcodec=FLV1,acodec=mp3}:std{access=http,dst=/stream.flv}"``

You can then point any flash based player to that stream using http://192.2.0.1:8080/stream.flv where 192.2.0.1 is the server IP address.

Note that flash only accepts 3 audio sample rates (44.1 kHz, 22.05 kHz and 11.025 kHz). If your source audio uses something else, muxing will fail. You can change the sampling rate by adding samplerate=44100 in transcode.

Making VLC the default player for FLV files for MAC and Windows 7, 8
--------------------------------------------------------------------

The instructions for making VLC the default player for FLV files can be found at the following links:

Mac https://www.youtube.com/watch?v=QTVu6bAK3rM

Windows 7 https://www.youtube.com/watch?v=eec6M1D3d9s

Windows 8 https://www.youtube.com/watch?v=mZ2pKsg2kpQ

Note: this and many other video codecs appear to be disabled and silently not working on Windows binaries, the system won't complain, but all you find is a container with no video stream in it.
