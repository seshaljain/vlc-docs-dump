Hello. I am a 16 year old software developer but I do not do so much
development toward vlc. I do my best writing bug fixes for Mesa and
Thomas A. Anderson is not my real name.

I edit j-b's page

These are my tips to build the most minimal yet functional vlc ever with
i686 optimization (Please edit this.)

== '''X264'''==

git clone git://git.videolan.org/x264.git && cd x264 && sudo apt-get
install libasm-dev yasm nasm && ./configure --prefix=/usr && make &&
sudo make install

''' == FFMPEG == '''

sudo apt-get install subversion && svn checkout
svn://svn.ffmpeg.org/ffmpeg/trunk ffmpeg && cd ffmpeg && ./configure
--prefix=/usr --enable-gpl --disable-debug && make && sudo make install

== '''VLC''' ==

   git clone git://git.videolan.org/vlc.git && cd vlc && ./configure
   --prefix=/usr --disable-debug --disable-live555 --disable-release
   --disable-libproxy --disable-httpd --disable-speex --disable-vorbis
   --disable-tarkin --disable-fluidsynth --disable-zxbi --disable-cmml
   --disable-tiger --disable-kate --disable-sdl-image --disable-fb
   --disable-directfb --disable-ggi --disable-upnp --disable-skins2
   --disable-goom --disable-activex --disable-gnutls --disable-ncurses
   --disable-wince --disable-v4l --disable-v4l2 --disable-libv4l2
   --disable-pvr --disable-libproxy --disable-telepathy --disable-dca
   --disable-tarkin --disable-theora --disable-dirac --disable-png
   --disable-csri --disable-libass --with-tuning=i686
   --with-x264-tree=../extras/x264

make

sudo make install
