\__FORCETOC_\_ The services discovery module was removed. **The**\ `Access output module <#Access_output>`__\ **is current.**

Access output
-------------

.. raw:: mediawiki

   {{Module|name=shout|type=Access output|first_version=0.8.4|description=This module forwards [[vorbis]] streams to an [[icecast]] server|sc=shout}}

.. raw:: mediawiki

   {{Clear}}

Documentation is present directly in the source code (4.0.0-dev) as multiple C comment blocks, relevant comments reproduced here (copyright © 2005 VLC authors and VideoLAN, Authors: Daniel Fischer and Derk-Jan Hartman, LGPL 2.1 or later):

| ``/*****************************************************************************``
| `` * Some Comments:``
| `` *``
| `` * - this only works for ogg and/or mp3, and we don't check this yet.``
| `` * - MP3 metadata is not passed along, since metadata is only available after``
| `` *   this module is opened.``
| `` *``
| `` * Typical usage:``
| `` *``
| `` * vlc v4l:/dev/video:input=2:norm=pal:size=192x144 \``
| `` * --sout '#transcode{vcodec=theora,vb=300,acodec=vorb,ab=96}\``
| `` * :std{access=shout,mux=ogg,dst=localhost:8005}'``
| `` *``
| `` *****************************************************************************/``

v4l refers to `GNU/Linux <GNU/Linux>`__ Video4Linux and won't work for Windows users.

This comment precedes the genre option:

| ``/* To be listed properly as a public stream on the Yellow Pages of shoutcast/icecast``
| ``   the genres should match those used on the corresponding sites. Several examples``
| ``   are Alternative, Classical, Comedy, Country etc. */``

This comment precedes the stream information options:

| ``/* The shout module only "transmits" data. It does not have direct access to``
| ``   "codec level" information. Stream information such as bitrate, samplerate,``
| ``   channel numbers and quality (in case of Ogg streaming) need to be set manually */``

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-shout-name
   |value=string
   |default="VLC media player - Live stream"
   |description=Name to give to this stream/channel on the [[shoutcast]]/[[icecast]] server
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-shout-description
   |value=string
   |default="Live stream from VLC media player"
   |description=Description of the stream content or information about your channel
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-shout-mp3
   |value=boolean
   |default=disabled
   |description=You normally have to feed the shoutcast module with [[Ogg]] streams. It is also possible to stream [[MP3]] instead, so you can forward MP3 streams to the shoutcast/icecast server
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-shout-genre
   |value=string
   |default="Alternative"
   |description=Genre of the content
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-shout-url
   |value=string
   |default=<nowiki>"http://www.videolan.org/vlc"</nowiki>
   |description=URL with information about the stream or your channel
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-shout-bitrate
   |value=string
   |default=""
   |description=[[Bitrate]] information of the [[transcode]]d stream
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-shout-samplerate
   |value=string
   |default=""
   |description=[[Samplerate]] information of the transcoded stream
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-shout-channels
   |value=string
   |default=""
   |description=Number of channels information of the transcoded stream
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-shout-quality
   |value=string
   |default=""
   |description=[[Ogg]] [[Vorbis]] Quality information of the transcoded stream
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-shout-public
   |value=boolean
   |default=disabled
   |description=Make the server publicly available on the 'Yellow Pages' (directory listing of streams) on the icecast/shoutcast website. Requires the bitrate information specified for shoutcast. Requires Ogg streaming for icecast
   }}

Services discovery
------------------

.. raw:: mediawiki

   {{Module|name=shout|type=Services discovery|first_version=0.8.2|last_version=1.0.6|description=Shoutcast services discovery module|sc=shoutcast|sc2=shout}}

Three sub-modules had shortcuts of ``shoutcasttv``, ``frenchtv`` and ``freebox``.

.. _options-1:

Options
~~~~~~~

None (``--shoutcast-limit`` was deprecated with ).

shout-winamp
~~~~~~~~~~~~

This sub-module had the shortcut ``shout-winamp`` with description "New winamp 5.2 shoutcast import". It is scheduled `to be removed <https://git.videolan.org/?p=vlc.git;a=commitdiff;h=d3859f364921c6f4d48115da331ac3a44d7a6351>`__ (currently in 4.0.0-dev) with the note:

::

   Removes the long unused Winamp/SHOUTcast directory stream filter for
   playlist handling, which was mostly useful together with the service
   discovery (modules/services_discovery/shout.c) which is not present
   anymore.

History:

-  `[acb5da732a27b6c7e8d6e05c2e183d4ae49a9ea9] <https://git.videolan.org/?p=vlc.git;a=commit;h=acb5da732a27b6c7e8d6e05c2e183d4ae49a9ea9>`__ (introduction)
-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-0.8.git|modules/demux/playlist/shoutcast.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-0.9.git|modules/demux/playlist/shoutcast.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-1.0.git|modules/demux/playlist/shoutcast.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-1.1.git|modules/demux/playlist/shoutcast.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-2.0.git|modules/demux/playlist/shoutcast.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-2.1.git|modules/demux/playlist/shoutcast.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-2.2.git|modules/demux/playlist/shoutcast.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-3.0.git|modules/demux/playlist/shoutcast.c}}

-  `[d3859f364921c6f4d48115da331ac3a44d7a6351] <https://git.videolan.org/?p=vlc.git;a=commit;h=d3859f364921c6f4d48115da331ac3a44d7a6351>`__ (removal)

.. raw:: mediawiki

   {{Clear}}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access_output/shout.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-1.0.git|modules/services_discovery/shout.c}}

.. raw:: mediawiki

   {{Documentation}}
