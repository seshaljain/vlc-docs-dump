Dears: I use vlc to stream out digi-TV signal(mpeg2-TS) with udp
protocol. I want to multicast it I use command line to start VLC,like
that

"C:Program FilesVideoLANVLCvlc.exe" dvb-t:// :dvb-frequency=533000000
:dvb-bandwidth=6 --ts-es-id-pid --programs="100,101,102"
:sout=#duplicate{dst=udp{dst=224.0.0.0:8056},select="program=100",dst=udp{dst=224.0.0.0:8057},select="program=101",dst=udp{dst=224.0.0.0:8058},select="program=102"}
:ttl=16 :sout-keep

the ip where i had use multicast address,but why i still can't do it. My
thought is that the server sent the package to the multicast
address(224.0.0.0),and ClientA connect to it,so does Client B. But I
just can't!!!! AM I worng?? can somebody can tell me what can i do
resolve the question. Thanks a lot.

PS I am so sorry about my poor English. Kevin
