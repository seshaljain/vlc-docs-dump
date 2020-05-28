.. raw:: mediawiki

   {{stub}}

This area of the wiki contains a list with some of the possibilities gives you. It was made to help people better realize the potential VLC has. Some entries will simply mention the possibility, while others try to explain how to do it as well.

Mediaplayer
-----------

 Compact Disc (CD) Images
~~~~~~~~~~~~~~~~~~~~~~~~

If you have a `CD-DA <CD-DA>`__ (audio CD), `SVCD <SVCD>`__, or `VCD <VCD>`__ packaged inside a CD-image, in some cases `VLC media player <VLC_media_player>`__ can play this without you having to mount it or extract it. You can simply choose *Open file* and pick the CD-image. For CD-image support VLC has to be `compiled <compile>`__ using libcdio (``--enable-libcdio``) and the various plugins which use libcdio need to be selected (``--enable-cddax``, ``--enable-vcdx``). Some of these options may not be the default for your `operating system <operating_system>`__.

The kinds of Compact Disc formats supported are CDRWIN's *BIN/CUE format*, cdrdao's *TOC format*, and a limited set of Nero (NRG) formats.

   *(*\ `libcdio <libcdio>`__\ *also supports ISO-9660 image reading, but at present there is no VLC access plugin which uses it.*\ `DVD <DVD>`__\ *images follow the UDF format and there is some UDF support through libcdio. It is possible that will get added in the future; volunteers are most welcome.)*

How to enable/use subtitles
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Before you try to enable `subtitles <subtitle>`__ make sure the subtitles you have are in a format that VLC can read! You can find the list of compatible subtitle formats `here <https://www.videolan.org/vlc/features.html>`__.
| If VLC has detected any sort of subtitles available, you will be able to turn them on under the menu: *Video → Subtitles track → Track 1*

Auto-detection of subtitle files uses a 'fuzzy' logic which you can specify. If this is wrongly specified you may end up with more subtitle file options than really exist or miss some that are provided. By default it loads any file in the expected directory if part of the video name is matched exactly. If you don't see the number of subtitle options you expect, you might want to allow more 'fuzziness' by changing the preference in *Video → Subtitles → Subtitle auto-detection* where help is available if you 'hover' over the field.

If you mainly use .srt or .sub subtitles you can automatically enable them when detected; set the *Input/Codecs → Advanced → Choose subtitle track* option to 0, which will automatically enable the subtitle track. You can also experiment with the *Choose subtitle language* option on the same page. It may require some experimenting but it is possible to have subtitles enabled automatically.

**Note:** On macOS, the *Video → Subtitles track* menu item is permanently disabled for some reason. You must manually specify the location of the subtitles file in the *Subpictures* pane of the `preferences <preferences>`__.

Unfortunately the default font for .srt subtitles does not display Unicode characters—characters that are not shown include hexadecimal U+2011 (non-breaking-hyphen ``‑``), U+2012 (figure dash ``‒``) and U+2A2F (cross-product ``⨯``).

Playing Windows Media files
~~~~~~~~~~~~~~~~~~~~~~~~~~~

VLC should be able to successfully play both audio and video in .wma and .wmv 1 and 2. For the newest version (wmv3) only the Windows version of VLC will be able to play it, since no `open-source <open-source>`__ implementation of wmv3 has yet been made, VLC plays it by using the Windows API. `DRM <DRM>`__-crippled files, however, cannot be played with VLC on any operating system.

How to control the aspect ratio of the video
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Transcluded|Change the aspect ratio}}

.. raw:: mediawiki

   {{:VLC HowTo/Change the aspect ratio}}

Be remotely controlled
~~~~~~~~~~~~~~~~~~~~~~

VLC provides a series of interfaces which allow it to be controlled in various ways such as via telnet, a web browser, several iPhone apps, desktop widgets and more. See `VLC HowTo#Remote Control for VLC <VLC_HowTo#Remote_Control_for_VLC>`__.

Announce What's Playing to IRC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Announce the currently playing track to mirc (an IRC client). This is often referred to as a "now playing" script.
| One approach to get this functionality with VLC is with the `HTTP interface <HTTP_interface>`__.
| Using it you can create a simple file which will display "*Artist* with the song *Title* from the album *Album* and the genre *Genre*" inside a page in your browser. You can then pull that page from mirc with standard sockets and thereby use the text in a script in mirc. Below I will provide some VERY simple and very ugly examples on how you could use this. The examples are tested with VLC 0.8.5 and mirc 6.12. I can't guarantee the code will work with any other versions (although it most likely will).
| Okay, so here we go.
| You start by creating a test.html file in the http interface directory ("\\http").
| Paste the following on ONE line of the file or it will not work:

::

   ANNOUNCE <vlc id="value" param1="'ARTIST' vlc_get_meta"/>
    with the song <vlc id="value" param1="'TITLE' vlc_get_meta"/>
    from the album <vlc id="value" param1="'ALBUM' vlc_get_meta"/>
   , The genre is <vlc id="value" param1="'Genre' vlc_get_meta"/>

— or for streaming server info —

::

   ANNOUNCE <vlc id="value" param1="'TITLE' vlc_get_meta"/>
    with the song <vlc id="value" param1="'NOW_PLAYING' vlc_get_meta"/> 

| Remember to leave an empty line behind the actual line of code, vlc/mirc seems to want this.
| Then you must create a script in mirc under remote (Alt+R) and paste in the following:

::

   alias now {
     sockopen vlc_meta_info 127.0.0.1 8082
   }

   on *:SOCKOPEN:vlc_meta_info: {
     sockwrite -n $sockname GET /test.html HTTP/1.1
     sockwrite -n $sockname Host: localhost
     ;sockwrite -n $sockname Connection: Keep-Alive
     sockwrite -n $sockname $crlf
     sockwrite -n $sockname $null
   }

   on *:sockread:vlc_meta_info: {
     if ($sockerr > 0) return
     :nextread
     sockread %temp
     if ($sockbr == 0) return
     if (%temp == $null) %temp = ---
     if (ANNOUNCE isin %temp) {
       %temp = $remove(%temp,ANNOUNCE )
       describe $active is listening to %temp
     }
     goto nextread

     sockclose vlc_meta_info
   }

A couple things you may want to change are the `port <port>`__ number the HTTP interface listens on (that's the first line and `port <port>`__ 8082 in my case) and the text *is listening to* to whatever you like.

That's pretty much it. You should enable the HTTP interface in VLC by default if you want to use this on a regular basis. This is done under `preferences <preferences>`__ in *Interface → Main interfaces*.

Then with all this done (and VLC restarted) you can type ``/now`` in mirc and it will display your currently playing track.

| This was made for mp3 tracks, so if it doesn't work with other types of media let me know.
| You can reach me at: jonas (at) vrt.dk
| (I'm also regularly in the freenode videolan channel, nickname E-bola)

Now Playing Script for mIRC by Jckf
-----------------------------------

Script and help for Inf3rn0's Now Playing script here: `NowPlaying <http://home.no/inf3rn0/NowPlaying/>`__

Based on E-Bola's Now Playing script.

Note: If anybody still uses this and wants to contact me, don't look for anyone named Inf3rn0. Look for Jckf ;)

Streaming - client
------------------

 Listen to online radio
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Transcluded|VLC HowTo/Listen to online radio}}

.. raw:: mediawiki

   {{:VLC HowTo/Listen to online radio}}

Streaming - server
------------------

VLM
~~~

`VLM <VLM>`__ is the *Video On Demand* part of the VLC streaming server features. It lets you set up a bunch of entries, and then lets users ask for and receive those streams. It has A LOT of possibilities and I will try to cover them all here.

You can divide VLM entries into 2 general categories: VOD, and broadcast entries.

See also
--------

-  `Timeshifting <Timeshift>`__
-  `3D <3D>`__
