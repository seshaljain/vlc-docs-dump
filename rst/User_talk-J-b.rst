TODO
----

.tooney zone *Please give me some TODOs here*

*Give your name and don't delete anything*

-  Qt4 - jb
-  Qt4 contribs - Xtophe
-  Branch nightlies - Xtophe
-  World domination

Talk Here
---------

Hi there, jibbynou. I've been doing QA professionally since 1990. It says if I wanna join the team to ping you all here... But here looks dead. Will I get a reply?

Hi jibbynou, I've just resuscitated the `Frequently Asked Questions <Frequently_Asked_Questions>`__ (formerly `FAQ <FAQ>`__). I don't know if/where you want to link it from: up to you :-) -- `Yoann <User:Yoann>`__ 19:44, 1 March 2007 (CET)

Plop jibbynou, you can now use {{RightMenu|documentation toc}}. See `Template:RightMenu <Template:RightMenu>`__ and `Template:Documentation_toc <Template:Documentation_toc>`__. -- `Yoann <User:Yoann>`__ 18:27, 21 May 2007 (CEST)

Hello, how can i contribute in ASM programing.

Hi VLC dev team. Can I please ask for one minor change that will make VLC better? Can you please make it remember edits I make to the EQ settings each time I reopen it? Currently, there are only the presets and no "custom" preset. One cannot save custom settings and it does not remember the settings changes. In v1.01, it didn't remember anything and now in v2.0, it only remembers my Pre-Amp settings, but not my EQ changes. It is tedious for me to keep reopening the EQ every time I play a song. Aside from that, I love your program and it kills all the proprietary stuff (e.g. Windows MP). Thanks for making an awesome player. I also love that you've added a compressor so I'm not always riding the volume when watching old movies with huge dynamic range. You rock :-) --`Zubi <User:Zubi>`__ 11:40, 10 April 2012 (CEST)

Win32 V. 0.8.6i Crash On Snapshot!
----------------------------------

As of 8//8/08 I have discovered what looks like a bug inside of 0.8.6i when trying to right click and choose snapshot from the playing video. It crashed the application, and bogs down windows. This happened on windows XP Home sp2, Intel p4 2.53GHz 1GB ram. All updates on machine are current, and it also has the latest quicktime, windows media player, and winamp installed.

-Sincerely AfterBurn

   this was fixed in updated binary.

Win32 Contribs 20070220
-----------------------

There is some missing reference to gsm_ms_encoder and gsm_ms_decoder. I have tried to compile the libgsm, but there is no such method. Could you provide this library or give a hint, where to find it? Besides when using your contrib some libraries need to be put in some directory named /home/videolan/j-b..... (sorry, I don't remember the path exactly (not sitting in front of the machine where I used your contrib - I will look it up on Sunday). Why does the vlc bootstrap/configure/compile reference this path which looks like it is your build path?

Thx in advance for answering my questions and keep up the good work!

   Well, this contrib may be broken because of the support and non-support of GSM in ffmpeg. This should be changed. Use another (older contrib), and I should do a new one in a few days.

      Thanks very much. I have now just added pseudo-methods for these two missing methods and it worked for me. --`Hxp <User:Hxp>`__ 14:36, 14 March 2007 (CET)

ALERT!!! PEOPLE CHARGING FOR VLC PLAYER!!!!!
--------------------------------------------

If you download VLC player at this link http://www.vlc-mediaplayer.info/uk/ it will try to charge you £2 (via SMS) to install.

   Fixed.

Thanks for the welcome
----------------------

Thanks for the welcome message, Jean-Baptiste.

I've already made one suggestion `over here <Documentation_Talk:EditingGuidelines>`__.

As I get to know VLC, I'll try to make more contributions to the documentation wiki. I've also run a MediaWiki-based wiki for a couple of years:

http://www.screenpedia.org

But I wouldn't call myself a *professional* wiki admin!

Regards,

--`Jeremy Butler <User:Jeremy_Butler>`__ 18:12, 9 July 2007 (CEST)

MacOS wiki
----------

No probs J-b. Je vais faire ca que je pouvais, et que je comprends ! `Facius <User:Facius>`__ 14:39, 8 October 2007 (CEST)

Deux petits questions:

Est-ce que mon idee de stocker les images hors du wiki reste bien ?

Est-ce q'on sais pourquoi le Template Ed n'est pas present ? `Facius <User:Facius>`__ 14:42, 8 October 2007 (CEST)

   Il faut réactiver les images alors. Je vais le faire. `jb <User:J-b>`__ 18:34, 9 October 2007 (CEST)
   Ed ? waht's that ?

Bureaucrat
----------

Hi, could I be a bureaucrat? I'm already a sysop, and I'll feel complete if I'm a bureaucrat. (Even though I'll probably never make anyone a sysop) `The thing <User:The_thing>`__ :sup:`(`\ `Talk <User_talk:The_thing>`__\ :sup:`•`\ `Contribs <Special:Contributions/The_thing>`__\ :sup:`)` 21:13, 8 August 2008 (CEST)

   Done `jb <User:J-b>`__ 19:51, 18 August 2008 (CEST)

Error in article
----------------

| Hi, I'm using your guide to compile VLC (`User:J-b#My_VLC <User:J-b#My_VLC>`__) under Ubuntu 8.10 but is outdated:
| "*configure: WARNING: --with-ffmpeg-tree is deprecated. Use PKG_CONFIG_PATH instead.*"
| And, therefore, an error occurs when it tries to compile *libavcodec*:
| "*checking for AVCODEC... no
  configure: error: Could not find libavcodec or libavutil. Use --disable-avcodec to ignore this error.*"
| It would be better to delete that wiki page or update it.
| Thank you anyway for your effort and work.
| A greeting.

--------------

| **Add**:
| Missing an important parameter in the config of ffmpeg: --enable-postproc

| The name of postproc is different in ffmpeg svn version over the name that looks VLC (¿?):
| *VLC*:
| checking for POSTPROC... yes
| checking libpostproc/postproc.h usability... no
| checking libpostproc/postproc.h presence... no
| checking for libpostproc/postproc.h... no
| checking postproc/postprocess.h usability... no
| checking postproc/postprocess.h presence... no
| checking for postproc/postprocess.h... no
| Solution:
| The real path/name in ffmpeg svn version is libpostproc/postprocess.h.
| The temporal solution is change the name to the file *postprocess.h* > *postproc.h*

These options no longer exist:'' --with-ffmpeg-mp3lame --with-ffmpeg-faac''

| For some reason I do not understand, VLC does not recognize x264 as compiled...
| Solution:
| This solves both the problem of x264 as of ffmpeg libraries:
| export PKG_CONFIG_PATH=extras/ffmpeg/libavcodec:extras/ffmpeg/libavdevice:extras/ffmpeg/libavformat:extras/ffmpeg/libavutil:extras/ffmpeg\ */libswscale:extras/ffmpeg/libpostproc:extras/x264:/usr/lib/pkgconfig;./configure --prefix=/usr --enable-snapshot --enable-dbus-control --enable-musicbrainz --enable-shared-libvlc --enable-mozilla --enable-lirc --enable-live555 --with-live555-tree=extras/live --enable-x264 --enable-shout --enable-taglib --enable-v4l --enable-cddax --enable-dvb --enable-vcdx --enable-realrtsp --enable-xvmc --enable-svg --enable-dvdread --enable-dv --enable-theora --enable-faad --enable-twolame --enable-real --enable-flac --enable-tremor --enable-dirac --enable-skins2 --enable-qt4 --enable-aa --enable-caca --enable-esd --enable-portaudio --enable-jack --enable-xosd --enable-galaktos --enable-goom --enable-ggi --disable-cddax --disable-vcdx --enable-mkv --enable-dca --disable-qt --disable-kde --enable-a52 --enable-xvideo --disable-fribidi....*

Obviously, some parameters that I put into this config can (and should) change depending on the needs of each.

--------------

| Edits:
| There is a bug in the code of VLC that does not link the code of ffmpeg correctly.

   The solution is on my blog. `jb <User:J-b>`__ 12:15, 30 December 2008 (CET)

Websites' Status
----------------

Hello, I was just wondering if you were contemplating an upgrade of this wiki to MediaWiki 1.14 as I noticed that you are still on 1.11 which seems rather counterproductive.

I was also wondering if you had considered using `Extension:PHPBB <http://www.mediawiki.org/wiki/Extension:PHPBB/Users_Integration>`__ from mediawiki.org to allow unified login between your forum and wiki especially as you were considering OpenID.

Also do tell me if I can be of any help with the site as the code for the various VideoLAN projects is a little over my head so I'd love to help with this (I'm fairly familiar with working on community sites if not media player code).

(also something appears to be wrong with Trac: (though I'm sure this has already been noted)

::

   :Report execution failed: invalid reference to FROM-clause entry for table "t" LINE 9: LEFT OUTER JOIN ticket_custom diff ON t.id=diff.ticket AND... ^ HINT: There is an entry for table "t", but it cannot be referenced from this part of the query.)

on the page: `1 <http://trac.videolan.org/vlc/report/11>`__ )

Oh and IRCWeb isn't working as of the time of writing: http://krishna.videolan.org/cgi-bin/irc/irc.cgi (can't reach server) (once again, probably noted)

Once again, tell me if I can be of any use, otherwise, thanks for the great work on VLC and the other VideoLAN projects and I'll try and help with the wiki where I can!

--`Tek <User:Tek>`__ 14:42, 16 May 2009 (CEST)

sudo make install lines?
------------------------

Minor suggestion:

Add sudo make install lines prior to all 4 builds (vlc, live555, x264, and ffmpeg) --`Neo_The_User <User:Neo_The_User>`__ 12:26 (US Central) 05/16/2009

Audio Interface
---------------

Hello JB,

Problem regarding the audio interface:

I'm using a professional audio interface (Layla 24)on 1.7G AMD system w/2G of ram and am experiencing audio severe audio breakup. Interestingly the Windows media player works fine with the same files as does all of the pro-audio apps. I have tried all of the output options including direct X but default and WIN32 of course are the only ones that give any audio output. Those are rather distorted however. Any Suggestions or if you need more input We can meet on Skype for faster input.

I am experienced in audio and perhaps (I hold an advanced degree in Electro-Acoustics) I can help with some of the audio interface problems.

Ed Wolfrum

Spam account
------------

`User:Jheena789 <User:Jheena789>`__ seems to be a spam account. See http://wiki.videolan.org/index.php?title=Common_Problems&diff=16884&oldid=16872. `Popol0909 <User:Popol0909>`__ 15:36, 21 August 2010 (UTC)

Correction needed
-----------------

| Would you please correct this annoying typo: `VideoLAN_Wiki_talk:Rules#WikiMedia_is_not_MediaWiki <VideoLAN_Wiki_talk:Rules#WikiMedia_is_not_MediaWiki>`__ ? Or better yet, make this page read/write for everyone.
| Pourriez vous corriger cette coquille svp: `VideoLAN_Wiki_talk:Rules#WikiMedia_is_not_MediaWiki <VideoLAN_Wiki_talk:Rules#WikiMedia_is_not_MediaWiki>`__ ? Ou mieux encore, mettre la page correspondante en lecture-écriture pour tous.
| Merci d'avance.--\ `Popol0909 <User:Popol0909>`__ 12:36, 18 February 2011 (UTC)

Spammer account User:Aaittersidless‎
------------------------------------

Hi, J-b, you appear to be cleaning up spammer accounts. Thank you for doing this necessary work.

It looks like `:User:Aaittersidless‎ <:User:Aaittersidless‎>`__ is a spammer. They created an account at 05:39h 22 October 2011, and 8 minutes later added 5000 bytes of word salad, with external links, and no relationship to VLC. I suggest that you consider deleting their User: page and their account. `Jim DeLaHunt <User:Jim_DeLaHunt>`__ 05:17, 27 October 2011 (UTC)

   dealt with `jb <User:J-b>`__ 00:58, 31 October 2011 (UTC)

Help Request
------------

I'm sorry if this is the wrong place to ask, but I'm having some problems with my account. I hadn't given an email when I logged in (the site didn't request one from my Google login) and now I'm stuck with no way to update my email address. My original username is VeryLargeCone. Is there anything you can do? `VeryLargeConeALT <User:VeryLargeConeALT>`__ (`talk <User_talk:VeryLargeConeALT>`__) 01:14, 7 March 2014 (CET)

Brandondorf9999
---------------

Did you mean to [ block] `User:Brandondorf9999 <User:Brandondorf9999>`__ (`talk <User_Talk:Brandondorf9999>`__ • `contribs <Special:Contributions/Brandondorf9999>`__ • `logs <Special:Log/Brandondorf9999>`__)? All I can find are constructive edits. 10:56, 15 March 2019 (CET)

   Unblocked. 06:09, 17 May 2019 (CEST)
