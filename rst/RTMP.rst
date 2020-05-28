{{protocolmod=avio}} {{wikipediaMacromedia Flash]].

{{clear}} ==Compatibility== VLC supports RTMP and rtmp:// URLs as of
version 1.1, through the [[Documentation:Modules/avio|avio]] module via
the libavformat library. In past versions, use of rtmpdump was required
in conjunction with VLC, but that is no longer needed after VLC 1.1.x.

==URL format== The basic URL format is: rtmp://tcurl/app/playpath

==Options== Some options can be used in command line :

{\| class="wikitable" ! Option !! Description rtmp_pageurl \|\|
rtmp_swfurl \|\| rtmp_swfvfy \|\| rtmp_live \|\| rtmp_playpath \|\|
Playpath rtmp_app \|\| Application rtmp_tcurl \|\| ip[:port] }

==Example== Find the swfurl of the RTMP stream (if required), and place
it in the appropriate location below:

   vlc rtmp://10.12.34.56/ --avio-options
   "{rtmp_swfurl=http://path/to/the.swf}"

==See also== \* [[SoC_2009/RTMP_Flash_Streaming]] \*
http://www.osflash.org/rtmp_os

[[Category:Protocols]]
