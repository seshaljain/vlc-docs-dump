.. raw:: mediawiki

   {{mux|id=real|altid=rm|encoder=n}}

.. raw:: mediawiki

   {{mmwiki|RealMedia}}

**RealMedia** is a type of file designed by RealNetworks, and can be played with the proprietary `RealPlayer <RealPlayer>`__. RealPlayer is available for `Windows <Windows>`__, `macOS <macOS>`__ and `Linux <Linux>`__. Additionally, `Helix Player <Helix_Player>`__ may be able to play some files, but it lacks the proprietary codecs in some realmedia files.

RealMedia files are normally streamed over `RTSP <RTSP>`__ connections.

RealAlternative installs, and allows RealMedia files to be played in `Media Player Classic <Media_Player_Classic>`__.

Accepted codecs
---------------

-  `rv <rv>`__: RealVideo
-  `ra <ra>`__: `MPEG-4 <MPEG-4>`__ audio
-  `a52 <a52>`__, `dnet <dnet>`__: A/52 audio
-  `cook <cook>`__: Cook audio codec
-  `28_8 <28_8>`__: 28.8 audio codec
-  `sipr <sipr>`__, RealAudio 4/5 (name is from Sipro Lab Telecom ACELP-NET)

Compatibility
-------------

Currently, `VLC media player <VLC_media_player>`__ should be able to play most audio and video of .rm, .rmvb files.

Sipr is supported through `libavcodec <libavcodec>`__ (Search for sipr in either of these files: `1 <https://git.videolan.org/?p=ffmpeg.git;a=blob;f=Changelog;hb=HEAD>`__\ `2 <https://git.videolan.org/?p=vlc.git;a=blob;f=modules/codec/avcodec/fourcc.c>`__. It is not mentioned in )

Source code
-----------

.. raw:: mediawiki

   {{File|modules/codec/avcodec/fourcc.c|from [[libavcodec]]}}
