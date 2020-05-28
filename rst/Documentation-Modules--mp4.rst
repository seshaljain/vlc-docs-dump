Support for fragmented `MP4 <MP4>`__ muxing/demuxing was added in VLC 3.0.0.

The demux module is planned to support `HEIF <wikipedia:High_Efficiency_Image_File_Format>`__ in future versions (currently in 4.0.0-dev) through a ``heif`` submodule.

Demux
-----

.. raw:: mediawiki

   {{Module|name=mp4|type=Access demux|first_version=0.5.0|description=[[MP4]] stream demuxer|sc=none}}

.. raw:: mediawiki

   {{Option
   |name=mp4-m4a-audioonly
   |value=boolean
   |default=disabled
   |description=Ignore non audio tracks from [[.m4a|iTunes audio files]]
   }}

.. raw:: mediawiki

   {{Clear}}

Mux
---

.. raw:: mediawiki

   {{Module|name=mp4|type=Muxer|description=[[MP4]]/[[MOV]] muxer|sc=mp4|sc2=mov|sc3=3gp}}

.. raw:: mediawiki

   {{Option
   |name=sout-mp4-faststart
   |value=boolean
   |default=enabled
   |description=Create "Fast Start" files. "Fast Start" files are optimized for downloads and allow the user to start previewing the file while it is downloading
   }}

.. raw:: mediawiki

   {{Clear}}

mp4frag
~~~~~~~

.. raw:: mediawiki

   {{Module|name=mp4frag|type=Muxer|first_version=3.0.0|description=Fragmented and streamable MP4 muxer|sc=mp4frag|sc2=mp4stream}}

.. raw:: mediawiki

   {{Clear}}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/mp4/mp4.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/mux/mp4/mp4.c}}

.. raw:: mediawiki

   {{Documentation}}
