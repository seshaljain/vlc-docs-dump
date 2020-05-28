VLC in Portage
--------------

-  To install it, just issue this on commandline:

``emerge vlc``

-  You may be also interested in enabling some USE flags. See http://www.videolan.org/vlc/download-gentoo.html for a recommended list of USE flags.

Old instructions
----------------

*This page is outdated! vlc is already in the official Portage tree*

Since version 0.6.0 and up VLC is distributed with an ebuild for the http://www.gentoo.org Portage system. This ebuild is not an official ebuild approved by Gentoo, but only a guideline for the Gentoo Maintainers. We hope that with our support, the Gentoo team will be able to respond faster to new releases and new features. But if you are confident enough, you can try to use it yourself. Instructions are always for the latest ebuild.

Some pointers
~~~~~~~~~~~~~

-  The ebuild is located at the root of the .tar.gz package and called vlc-versionnr.ebuild
-  If you want features, then be sure to set some USE variables. The following USE variables are supported: arts qt ncurses dvd gtk nls 3dfx matrox svga fbcon esd kde X alsa ggi oggvorbis gnome xv oss sdl fbcon aalib slp truetype v4l lirc wxwindows imlib matroska dvb pvr mozilla mad debug tcltk
-  VLC links statically against CVS versions of http://ffmpeg.sf.net and http://mpeg2dec.sf.net . Current installations of these software packages will not be affected.
-  the best interface is the [WxWindows Interface]. I suggest you prefix the emerge command with USE="wxwindows".
-  for Video4Linux? support prefix your emerge command with USE="v4l" .
-  for matroska support prefix your emerge command with USE="matroska" and be sure to have http://forums.gentoo.org/viewtopic.php?t=63722&highlight=matroska
-  if you want the [Skinable Interface] then prefix your emerge command with USE="wxwindows imlib".

Installation
~~~~~~~~~~~~

-  all the examples are with the 0.6.0 release.
-  in your /etc/make.conf make sure PORTDIR_OVERLAY=/usr/local/portage is added (uncommented).
-  run: wget -P/usr/portage/distfiles http://www.videolan.org/pub/vlc/0.6.0/vlc-0.6.0.tar.bz2
-  create /usr/local/portage/media-video
-  create /usr/local/portage/media-video/vlc
-  run: cd /usr/local/portage/media-video/vlc
-  run: tar jxf /usr/portage/distfiles/vlc-0.6.0.tar.bz2 vlc-0.6.0/vlc-0.6.0.ebuild
-  run: mv /usr/local/portage/media-video/vlc/vlc-0.6.0/vlc-0.6.0.ebuild /usr/local/portage/media-video/vlc/
-  run: ebuild /usr/local/portage/media-video/vlc/vlc-0.6.0.ebuild digest
-  run: emerge /usr/local/portage/media-video/vlc/vlc-0.6.0.ebuild

.. raw:: mediawiki

   {{outdated}}

`Category:Building <Category:Building>`__ `Category:GNU/Linux distros <Category:GNU/Linux_distros>`__
