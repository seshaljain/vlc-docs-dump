== General presentation ==

'''Hello!'''

My name is '''[http://www.jbkempf.com/ Jean-Baptiste Kempf'''] and my
nickname is ''jb'' or ''j-b'', in the VideoLAN community.

I am one of the main {{VLC}} developer and the president of the VideoLAN
non-profit organization.

[http://www.jbkempf.com/ My personal website] explains a bit more who I
am and what I do.

=== Education === I graduated in one of the best 'Grandes Ecoles', best
scientific schools and universities in France: the ''[http://www.ecp.fr
"Ecole Centrale Paris"]''.

My degree ''"Ingénieur de l'école Centrale Paris"'', which is also a
Master's Degree.

I also earned a ''Master's Degree'' in Computer Science from the
[http://www.u-psud.fr/ University of Paris].

=== VideoLAN === I have been working on the VideoLAN project in many
aspects since 2006 and I am very involved, doing a large variety of
things, not only development.

As a developer, I mostly program Qt4 interface. I also work a lot on
contribs and external libraries and [[FourCC]] supports. I have built
VLC media player on most possible platform (no BeOS, though).

As a non-developer, I moderate e-mails, worked a lot on this wiki
(almost rewritten it with [[User:H2g2bob]]), answer forums and mails,
work on the websites and help on IRC. As you can imagine, I do a lot of
support.

jb (at) videolan (d0t) org is my mail, related to VideoLAN.
[http://www.jbkempf.com My Website] (far from being finished) is my
website.

Use my talk page to talk to me or give me some TODOs.

== Wiki ==

I have rewritten a lot of pages on this wiki, and I have more than 1000
edits on this wiki.

=== Names ===

I am known under 'j-b', 'jb' on all the [[VideoLAN Sites]].

== My VLC == These are my tips to help you build the best VLC ever. I
use debian/sid, for many reasons.

=== External libraries === apt-get build-dep vlc libdvdcss2

apt-get install nasm yasm libasm-dev

=== Get VLC === <pre> git clone git://git.videolan.org/vlc.git\ </pre>
<pre> cd vlc; ./bootstrap </pre>

<pre> cd extras;</pre>

=== x264 (optional) ===

<pre> git clone git://git.videolan.org/x264.git x264-trunk</pre>

<pre> cd x264-trunk; ./configure --prefix=/usr; make</pre>

=== live555 (optional) === <pre> wget
http://www.live555.com/liveMedia/public/live555-latest.tar.gz </pre>

<pre> tar xvzf live555-latest.tar.gz cd live

sh genMakefiles linux; make </pre>

=== ffmpeg (mandatory) ===

<pre> cd vlc-trunk/extras git clone git://git.videolan.org/ffmpeg.git
ffmpeg cd ffmpeg </pre>

==== ffmpeg configure line ==== <pre> ./configure --prefix=/usr
--enable-gpl --enable-pthreads --enable-libmp3lame --enable-libfaac
--enable-nonfree</pre> <pre> make </pre>

=== VLC configure line === <pre> mkdir build && cd build && ../configure
--prefix=/usr --enable-snapshot --enable-debug --enable-dbus-control
--enable-musicbrainz --enable-shared-libvlc --enable-mozilla
--enable-lirc --enable-live555 --with-live555-tree=../extras/live
--enable-x264 --with-x264-tree=../extras/x264-trunk --enable-shout
--enable-taglib --enable-v4l --enable-cddax --enable-dvb --enable-vcdx
--enable-realrtsp --enable-xvmc --enable-svg --enable-dvdread
--enable-dc1394 --enable-dv --enable-theora --enable-faad
--enable-twolame --enable-real --enable-flac --enable-tremor
--with-ffmpeg-mp3lame --with-ffmpeg-faac --enable-quicktime
--enable-dirac --enable-skins2 --enable-qt4 --enable-ncurses --enable-aa
--enable-caca --enable-esd --enable-portaudio --enable-jack
--enable-xosd --enable-galaktos --enable-goom --enable-ggi
--disable-cddax --disable-vcdx

</pre>

<pre>make</pre>

<pre>sudo make install</pre>

== Ubuntu == apt-get build-dep vlc

apt-get install libtool automake autoconf ffmpeg
