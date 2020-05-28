The ogg demux module refers to `Ogg <Ogg>`__ as *OGG*. The `Xiph Wiki <Xiph_Wiki>`__ `clarifies <https://wiki.xiph.org/Ogg#Name>`__ that the name is not an acronym and should be written *Ogg* or *ogg*.

The earliest mention of Ogg `muxing <muxing>`__ support in the changelog was for the macOS port in 0.5.3.

Demux
-----

.. raw:: mediawiki

   {{Module|name=ogg|type=Access demux|first_version=0.5.0|description=[[Ogg|OGG]] demuxer|sc=ogg}}

Options
~~~~~~~

None.

Mux
---

.. raw:: mediawiki

   {{Module|name=ogg|type=Muxer|description=[[Ogg]]/[[OGM]] muxer|sc=ogg|sc2=ogm}}

.. _options-1:

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-ogg-indexintvl
   |value=integer
   |default=1000
   |min=0
   |max=<var>INT_MAX</var>
   |description=Minimal index interval, in [[wiktionary:ms|millisecond]]s. Set to 0 to disable index creation.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-ogg-indexratio
   |value=float
   |default=1.0
   |min=1.0
   |max=1000
   |description=Set index size ratio. Alters default (60min content) or estimated size.
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/ogg.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/ogg_granule.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/oggseek.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/mux/ogg.c}}

.. raw:: mediawiki

   {{Documentation footer}}
