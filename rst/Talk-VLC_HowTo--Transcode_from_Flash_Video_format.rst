Do you also have problems when using a nightly build ? `Dionoea <User:Dionoea>`__ 09:40, 18 October 2006 (CEST)

   Yes, perhaps I should explain this page. I made it as I was sent a link `here <http://www.scaryideas.com/Videos/TruthInAdvertising/>`__ to `this .flv file <http://youtube.com/get_video?video_id=-uLxKzqpSSA&t=OEgsToPDskJFSgqk8nQUBfjkFd97fFdR>`__ (youtube). The seekbar stays at the end, and it stops playing half way through.
   I think it could be to do with seeking. Seeking at all makes it go wrong, and there are "access_file access error: seeking too far" errors when it fails. The duration is tagged as "ffmpeg demuxer debug: - duration = -1"
   Also, the following works: " cat Desktop/-uLxKzqpSSA.flv \| vlc - "
   I'm using the Debian Unstable version (svn-20061012). FLV support works almost all the time for me, but sometimes on youtube you get the odd one which doesn't quite work. --`h2g2bob <User:H2g2bob>`__ 03:26, 19 October 2006 (CEST)
