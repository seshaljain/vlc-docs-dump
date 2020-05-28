When stating that an SVN/CVS version works, the revision/date should be stated. -- `Dionoea <User:Dionoea>`__ 18:33, 11 July 2006 (CEST)

mpeg2dec and ffmpeg
-------------------

What is the relation with these two? I believe ffmpeg has an mpeg2dec so why two mpeg 2 decoders? Thanks, `Daniel.Cardenas <User:Daniel.Cardenas>`__ 01:51, 22 April 2007 (CEST)

   mpeg2dec is faster `jb <User:J-b>`__ 02:36, 26 September 2007 (CEST)

      and historicaly it was the first MPEG2 decoder to be used in VLC (you could argue that it doesn't really matter ... but still :)) `Dionoea <User:Dionoea>`__ 10:41, 26 September 2007 (CEST)

FreeType
--------

VLC use FreeType 2.3.5, maybe it's possible to close `ticket 839 <http://trac.videolan.org/vlc/ticket/839>`__? --`DyLoU <User:DyLoU>`__ 01:10, 26 September 2007 (CEST)

   Done `jb <User:J-b>`__ 02:36, 26 September 2007 (CEST)

libcdio
-------

This page currently lists libcdio most recent version as 0.82 with an 'untested' note. 0.82 is dated 10/27/2009. Newer builds are available via http://git.savannah.gnu.org/gitweb/?p=libcdio.git -- `weirdpercent <User:weirdpercent>`__ 06:05, 12 April 2010 (EST)

ubuntu-single-command-installation
----------------------------------

first compilation of vlc has slightly different dependencies as listed at bottom of page:

   for 'sudo apt-get install '...

      instead of libebml2 please list libebml3
      instead of libmatroska2 please list libmatroska3

   for optional libraries

      for lua support please list liblua5.1-0-dev
      for swscale support please list libswscale-dev
      for postproc support please list libpostproc51-dev
      as alternative: ./configure --disable-swscale --disable-postproc --disable-lua
