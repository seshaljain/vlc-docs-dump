NTSC
----

Shouldn't we be using 29.97 or 29.97002997 for NTSC?

   Yes, we should! I'll change it --`H2g2bob <User:H2g2bob>`__ 03:52, 20 March 2006 (CET)

Does not create DVD compatible files
------------------------------------

This is a great tutorial, but it seems to fall one-step short of producing MPEG files that can be passed directly to dvdauthor. You still have to use ffmpeg with a -dvd option to transcode, otherwise you get the following complaint from dvdauthor:

**WARN: Skipping sector, waiting for first VOBU...** **WARN: Skipping sector, waiting for first VOBU...**

**WARN: Partial sector read (331 bytes); discarding data.** **STAT: VOBU 0 at 0MB, 1 PGCS** **Segmentation fault**

Is there some way of telling VLC to transcode use ffmpeg with the -dvd option? --`Brownstone <User:Brownstone>`__ 22:59, 28 September 2006 (CEST)

No more mp2a
------------

It appears at some point VLC got rid of the mp2a option and VLC 1.1 now defaults to mp3 instead of mp2 when using mpga, which not all players support. This also results in no audio on some DLNA clients that only support mpeg2 audio with videos when VLC is used to power the transcoding like Mediatomb. Is there a workaround to force it to use ffmpeg's mp2 audio encoder? --`Kyl416 <User:Kyl416>`__ 21:52, 9 November 2011 (UTC)
