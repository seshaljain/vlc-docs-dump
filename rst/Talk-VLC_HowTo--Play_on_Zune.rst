==Quality==

this produces a file with tawdry quality, can anyone give some hints as
to how to make it better?

:you can increase the bitrate of the video (vb=2048 is a really nice
one). - Jebrew

==Transcoding== The only problem with the sample script is that it still
requires a re-encoding by the Zune software. Does anyone have a script
that does not require re-encoding? If it requires installation of more
codecs or anything, I'm okay with that. It's just cumbersome to have to
rip a dvd, then transcode with VLC, then transcode again using the Zune
software. I'd like to eliminate as many of those steps as possible while
still allowing me to take a few movies with me on those long flights. -
Jebrew

==My Transcoding Script== I wrote a script for the Zune v2 (4/8/80G)
that can play mp4's. Works like a charm and no second transcoding by the
Zune software.
[http://blog.chase.net.au/index.php/2007/12/converting-avis-for-my-zune
Check out my blog post]. If someone thinks it's worthwhile I can put it
up on the main article page. :Note that you can simplify the command
line in your script a bit (well, it's still using the same options but
it's shorter) --intf=dummy
--sout=#transcode{width=320,vcodec=h264,vb=768,venc=x264{level=13,bframes=0,cabac,qp=0,8x8dct},acodec=mp4a,ab=128,channels=2,threads=%NUMBER_OF_PROCESSORS%}:standard{mux=mp4,dst="%OUTDIR%!targ!.mp4",access=file}
vlc:quit :[[User:Dionoea|Dionoea]] 14:30, 17 January 2008 (CET)
