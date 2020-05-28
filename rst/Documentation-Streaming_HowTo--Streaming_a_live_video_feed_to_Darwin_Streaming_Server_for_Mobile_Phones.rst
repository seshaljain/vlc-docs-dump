==Streaming a live video to DSS for Mobile Phones with VLC==

   {{%}} '''vlc -vvv
   v4l2:///dev/video0:input=1:width=128:height=96:adev=hw.1,0:samplerate=32000
   --sout
   '#transcode{venc=ffmpeg{keyint=1},vcodec=mp4v,vb=100k,acodec=mp4a,fps=10,ab=8k,channels=1,samplerate=16000}:rtp{mp4a-latm,dst=127.0.0.1,port-audio=20000,port-video=20002,ttl=127,name=CHANNEL,sdp=file:///usr/local/movies/channel.sdp}''''

where: \* '''v4l2:///dev/video0''' is the video device you want you want
to stream, \* '''input=1''' is the input channel of the video device (0
- tv tuner, 1 - composite), \* '''width=128:height=96''' is the width
and height of the input video signal to fetch by VLC, \*
'''adev=hw.1,0''' is the alsa audio device to capture audio from, \*
'''samplerate=32000''' is the input sample rate of the audio live feed,
\* '''venc=ffmpeg''' is the encoder used (in this case it's ffmpeg, but
you can use x264), \* '''{keyint=1}''' is the advanced ffmpeg encoder
switches, \* '''vcodec=mp4v''' is video codec used to encode this live
video feed (in this case it's MPEG4), \* '''vb=100k''' is the video
[[bitrate]] (100 kbits/s is this case), \* '''acodec=mp4a''' is the
audio codec used (is this case it's AAC), \* '''fps=10''' is the frame
rate of the video feed, \* '''ab=8k''' is the audio bitrate (is this
case 8 kbits/s), \* '''mp4a-latm''' is only used for aac audio, it
activates a different payload format for aac, \* '''dst=127.0.0.1''' is
the destination IP, where Darwin Streaming Server is hosted, \*
'''ttl=127''' is the value of the TTL (Time To Live) of your IP packets
(which means that the stream will be able to cross 126 routers), \*
'''sdp=file:///usr/local/movies/channel.sdp''' is where to create the
[[SDP]] file for live streaming with Darwin Streaming Server (it should
be inside of the DSS movies folder), \* '''name=CHANNEL''' is the name
of the live video feed.

Tested on Nokia N73 and SE K800.

There is a small problem with some Nokia phones and Darwin Streaming
Servers, that need a line to be edited in the created SDP file (for
example):

-  '''from b=RR:0 to b=RR:800'''

After running this command from console, you can access it from your
mobile phone or VLC or any player that supports [[RTSP]] protocol

\* '''rtsp://192.168.2.3/channel.sdp''' where \* '''192.168.2.3''' is
the IP address of the machine where DSS is running.

{{Documentation}}

[[Category:Mobile documentation]]
