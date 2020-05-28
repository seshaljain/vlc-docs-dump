I have avi from old computer games, that i can't look. I need the Indeo
Codecs, but as I see I have them already (Windows XP SP2). On your VLC
features list (http://www.videolan.org/vlc/features.html) VideoLan does
not use the Indeo Codecs.

Why aren't they not supported?<br> I can't look them with VideoLan or is
there something I can do?

(BTW, I can't play the games either) --[[User:Lemmi|Lemmi]] (unsigned)

: In general, VLC ignores the codecs on your machine (the only
exception, I believe, is the WMV3 codec). However, VLC does have support
for Indeo Video 2.0 and 3.0, but not 4.0 or 5.0. : Indeo is owned by
[http://ligos.com/ Ligos], who owns the rights to the Indeo codecs. :
From the [[forum]], markfm (Developer), says: :: "IV50 is proprietary,
that's why VLC doesn't support it, VLC is an open-source, GPL project,
so unless someone were to reverse-engineer Indeo Video 5, come out with
an open-source implementation, it won't be in VLC. ::
"Reverse-engineering a CODEC is painful, time consuming. CODECs
generally work by doing some pretty advanced mathematical operations on
the video data -- various Fourier and wavelet transformation techniques,
working with the video in the frequency domain, a bunch of matrix math
things, various mechanisms to predict movement and only sent small
blocks of data at a time (inter frames), all in pursuit of high video
quality at minimal bandwidth (a lot of compression)." : Sorry not to be
of more help, --[[User:H2g2bob|H2g2bob]] 16:37, 19 March 2006 (CET)
