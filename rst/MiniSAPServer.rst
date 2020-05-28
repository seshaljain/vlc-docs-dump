.. raw:: mediawiki

   {{Historical}}

| MiniSAPServer was a lightweight and easy-to-use `VideoLAN <VideoLAN>`__ application that could produce `SAP <SAP>`__ announcements.
| It is no longer necessary:

   | … Remember [that] miniSAPserver should be used to announce the streams sent by `VLS <VLS>`__;\ :sup:`\*` the streams sent by `VLC <VLC>`__'s stream output can be announced by VLC itself ! …
   | ―\ `VideoLAN News - Release: miniSAPserver 0.2.2 <https://www.videolan.org/news.html#news-2003-07-25>`__\ 

\ *\* VLS*\ `is deprecated <https://forum.videolan.org/viewtopic.php?f=3&t=11405>`__\ *, and the same functionality*\ `is built into VLC <https://www.videolan.org/vlc/streaming.html>`__\ 

| VLC can listen for SAP announcements with the module and announce them with the stream_out_rtp module. Since no wiki page exists yet, options can be found by typing into a `command prompt <command_prompt>`__.
| Windows:

\ `` -p stream_out_rtp --advanced --help-verbose | more``

macOS:

\ `` -p stream_out_rtp --advanced --help-verbose | less``

Linux:

\ `` -p stream_out_rtp --advanced --help-verbose | less``

Links
-----

| Links are still provided for reference/development purposes.
| If you aren't developing code, they will probably be of no benefit to you.

-  `code.videolan.org - minisapserver <https://code.videolan.org/videolan/minisapserver>`__ (source)
-  `Browse FTP download archives <https://download.videolan.org/pub/videolan/miniSAPserver/>`__ (binaries)

`† <Category:VideoLAN_projects>`__
