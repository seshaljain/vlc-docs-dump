{{Codec audioid=sawb}} {{MmwikiAMR-NBAMR-WBAdaptive Multi-Rate audio
codec|l1=AMR format}}

== Tutorial == To stream amr-nb with vlc to mobile-phone eg. next
setting works (tested on few nokia & sony ericsson phones)

<pre>
transcode{vcodec=H263,width=128,height=96,vb=28,fps="12.5",acodec=samr,ab="5.25",samplerate=8000,
channels=1,venc=ffmpeg{keyint=6,strict=1,strict-rc=1}}:rtp{mp4a-latm,port-video=2244,port-audio=2242,dst=1
27.0.0.1,ttl=12,sdp="`file:///usr/local/movies/mobile.sdp\\ <file:///usr/local/movies/mobile.sdp\>`__"}</pre>

It seems that mp4a-latm somehow affects on audio-output on amr also.
AMR-NB requires 8000 [[samplerate]] and only 1 channel, also if you
choose incorrect audio-[[bitrate]], vlc gives you <samp>unknown
codec</samp> or similar error.
