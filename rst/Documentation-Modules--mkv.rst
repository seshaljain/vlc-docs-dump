.. raw:: mediawiki

   {{Module|name=mkv|type=Access|first_version=0.6.0|description=[[Matroska]] stream demuxer|sc=mka|sc2=mkv}}

.. raw:: mediawiki

   {{Option
   |name=mkv-use-ordered-chapters
   |value=boolean
   |default=enabled
   |description=Play chapters in the order specified in the segment
   }}

.. raw:: mediawiki

   {{Option
   |name=mkv-use-chapter-codec
   |value=boolean
   |default=enabled
   |description=Use chapter [[codec]]s found in the segment
   }}

.. raw:: mediawiki

   {{Option
   |name=mkv-preload-local-dir
   |value=boolean
   |default=enabled
   |description=Preload matroska files in the same directory to find linked segments (not good for broken files)
   }}

.. raw:: mediawiki

   {{Option
   |name=mkv-seek-percent
   |value=boolean
   |default=disabled
   |description=Seek based on percent not time
   }}

.. raw:: mediawiki

   {{Option
   |name=mkv-use-dummy
   |value=boolean
   |default=disabled
   |description=Read and discard unknown [[wikipedia:Extensible Binary Meta Language|EBML]] elements (not good for broken files)
   }}

.. raw:: mediawiki

   {{Option
   |name=mkv-preload-clusters
   |value=boolean
   |default=disabled
   |description=Find all cluster positions by jumping cluster-to-cluster before playback
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFolder|modules/demux/mkv}}

   (folder)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/mkv/mkv.cpp}}

   (main file)

.. raw:: mediawiki

   {{Documentation}}
