This is a list of small independent improvements to VLC for which we are
looking for interested developers, because we simply don't have enough
time.

These do not require advanced knowledge of VLC internals but they can
still vastly improve many parts of VLC

For each project, we list a contact person, who knows the subject best
and who will be able to assist you if you are interested in working on
these. We generally are very often present on irc.videolan.org, chan
#videolan, so please don't hesitate to drop by or to send a mail if you
are interested in a given problem (our mail adresses are generally
<nick>@videolan.org).

We also have a number of "easy" bugs. You can check them out
[http://trac.videolan.org/vlc/query?status=new&status=assigned&status=reopened&difficulty=easy&order=priority\ \`
here]

= Easy projects =

== Video Filters == You can do video filters for {{VLC}}.

You can inspire yourself on this
[http://movavi.com/enhancemovie/filters.html list of filters] from a
commercial product.

You can start the code
[http://git.videolan.org/?p=vlc.git;a=tree;f=modules/video_filter here].

== Subtitles improvements == {{VLC}} does not support all the styles for
a lot of subtitles type. Take a look at
{{VLCSourceFile|modules/codec/subsdec.c}} to start coding.

= Network =

== RTCP support ==

Our RTSP implementation (for broadcasting and video on demand) does not
support the RTCP protocol. This is a must to have a real support for
RTSP. Some work has already been started, but there is still much to do.

Contact: [[User:JPSaman|JPSaman]]

== Performant VLC streaming server ==

There are many bottlenecks currently limiting the performance and
scalability of VLC as a streaming server: \* The I/O blocks are linear,
which implies lots of avoidable memory copying and dynamic memory
allocations (particularly in the streaming output). \* <s>mdate() (the
timestamping function) is invoked in too many places to count them; but
it is not a cheap operation on modern systems and should be avoided on
the fast path. Ideally, a single thread would only need to call mdate()
at most once per wake-up. In some case, mdate() is only used for
debugging purpose which is really inefficient.</s> \* The HTTP/RTSP core
is single-threaded. This prevents scaling to SMP systems (which are the
norm on server-side nowadays) properly. This also implies not very
scalable I/O event polling. This also becomes problematic when one
HTTP/RTSP client triggers a computationally intensive operation (such as
establishing a TLS context if HTTP/SSL is used). \* There are many
dynamic memory allocations that could be avoided. Video filters and
codecs are very careful about this, but the stream output plugins are
not. In many case, a stack-based buffer can be used (stack buffer, has
constant time fast lock-less allocation, and needs not be freed
explicitly) instead. \* <s>The messaging subsystems might be adding more
locking (needs checking); this should be avoided particularly if the
message is anyway ignord (e.g. debug message in non-debug mode).</s> \*
Interleaved RTP in RTSP is not supported.

Other improvements that would be particularly benefitial on the server
side:

-  Memory allocation failure are not always duly handled. In some cases,
   that could potentially be leveraged by a client to crash a VLC server
   by causing a very large allocation attempt.
-  <s>Rewrite and revive the root wrapper to allow VLC to bind to the
   RTSP (554) port while not retaining root privileges.</s>

Contact: [[User:Courmisch|Courmisch]]

= Inputs =

== DVB support for Windows ==

DVB is the norm for : \* Digital Terrestrial TV (aka DVB-T) \* Digital
Cable TV (aka DVB-C) \* Digital Satellite TV (aka DVB-S)

Several DVB input cards exist. We support these on Linux, but not on
Windows. For Windows, we need to support so-called BDA drivers.

The problem is that we don't have both the time and the required
hardware on Windows comps.

This project is probably not terribly complex, but you need the
hardware. Someone has already began it on the forum, so start from
there.

== V4L2 support ==

VLC currently has a pvr module and a v4l (video for linux) module.
However \* some cards are only supported in the new v4l2 API \* The
linux kernel will soon drop v4l support

So if someone could update VLC's current modules to work with V4L2 and
the new ivtv api, this would be a welcome addition. This is not a very
difficult project, but you will need to have the hardware to test
against. The code has been began, so it should not be too difficult.

= Video =

== DirectX 9 video output ==

DirectX 9 features some improvements that we could use in our video
output

== Improvements to the X11 video output ==

Fullscreen support to improve .

= Interfaces =

== Streaming profiles ==

This is a big subject, that has barely started. Interested persons will
need to work closely with existing developers to implement this. Not
much information is available yet. The idea is to make streaming very
easy, and yet powerful by using parametrable profiles. These could be
used either by the graphical interfaces or through HTTP/command line
interfaces

= Playlist =

== Improved Podcast support ==

Our current podcast support is very weak. We can read them, but that's
all. We need a real infrastructure to handle them correctly. This will
require some changes to the playlist code, so you will need to work
closely with existing developers.

== Improved ASX support ==

ASX is a playlist format used by Microsoft stuff. We can read it but we
could do much better. More information is available at
https://trac.videolan.org/vlc/ticket/20

== Disc probing ==

We currently have some miscellaneous code to detect discs (DVDs, Audio
CDs, ...) but it's a bit scattered and it could be used much better in
the playlist.

== Live folders ==

Some programs support so-called live folders. You add a folder to the
playlist, and if the files in the folder are changed, the changes are
copied to the playlist.

Having this would of course be great :)

It might require some work to be able to do this in Linux, Windows and
OS X, but the current developers will of course be able to help on
these.

= Misc =

== DBus Integration ==

[[DBus]] is a communication mechanism for Linux (mainly).

We would like VLC to be able to use it so that other programs can
interact with vlc (start/stop, know what is being played, ...)

Work is well advanced, see [[DBus]]

[[Category:Coding]] [[Category:Development]]
