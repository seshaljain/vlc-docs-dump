Shouldn't we just go back to the version before Noki774V. I'm not sure thqt the content is the same --`Xtophe <User:Xtophe>`__ 23:55, 20 January 2006 (CET)

   It's a copy of `What can vlc do <What_can_vlc_do>`__ I think --`H2g2bob <User:H2g2bob>`__ 00:36, 21 January 2006 (CET)
   No it was not, it was more of the other being a branch of this, and this one contained MUCH more. I support reverting it. --`tonsofpcs <User:Tonsofpcs>`__ 09:39, 21 January 2006 (CET)

      You're right, sorry about that :( Restored :), set other to redirect.

libcdio *can* understand some Nero cd images. It also can understand cdrdao too. If libcdio is *not* enabled for vlc, is it really true that VCD (or CD-DA) compact disc images can be read? And if libcdio is installed, is it true that DVD images can be read? I don't think so, because I don't recall any code directly in vlc to handle BIN/CUE or even ISO.

   Yes, that appears to be the case - I've added a brief sentence to this effect, but please feel free to change it! --`H2g2bob <User:H2g2bob>`__ 19:48, 6 February 2006 (CET)

      I've made some corrections. First, the mention of proprietary formats has been dropped: BIN/CUE and NRG *are* proprietary. Second, DVD's use UDF format, something libcdio doesn't handle. Maybe vlc handles this, but if so I have a feeling it's via some magic on your OS, not something that's built in to vlc. So if such a thing works, I think you should mention on what OS's it works. On my GNU/Linux box, I opening a UDF ISO image with vlc 0.8.4 and that didn't work. Likewise I'm not sure what's with img. Some media players like mplayer work on such things because the beginning of the file looks like a MPEG (after possiblly skipping over null bytes). It's possible vlc has this behavior too. But if that's the case there is a little difference which should be noted. When libcdio reads images it gets whatever meta information is there. So for example when it reads CD-DA the track information is there but also say CD-Text information. Likewise with VCD's when libcdio reads the CD image it has the potential to get VCD navigation information and meta information, not just the MPEG tracks. A problem with trying to read a the BIN part without CUE, or TOC is that if there were say multiple MPEG tracks (or audio tracks) you wouldn't know were one stopped an the next started.

add my radio station to VLC shoutcast radio list
------------------------------------------------

i want to add my radio station to VLC shoutcast radio list. help me to add.

`Nasir Khan <User:Nasir_Khan>`__ 12:02, 28 September 2009 (UTC)

   Sorry, would not work anymore. 05:47, 28 March 2019 (CET)
