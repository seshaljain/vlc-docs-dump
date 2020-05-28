\__NOTOC_\_ This module has no shortcut.

Support for `DASH <wikipedia:Dynamic_Adaptive_Streaming_over_HTTP>`__ in WebM is planned for VLC 4.0.0.

Demux
-----

.. raw:: mediawiki

   {{Module|name=vpx|type=Access demux|first_version=1.1.0|description=[[WebM]] video decoder}}

`VP9 <VP9>`__ support was added in VLC 2.1.1.

Options
~~~~~~~

None.

Mux
---

.. raw:: mediawiki

   {{Module|name=vpx|type=Muxer|first_version=3.0.0|description=[[WebM]] video encoder}}

.. _options-1:

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-vpx-quality-mode
   |value=integer
   |default=0
   |min=0
   |max=2
   |description=Quality setting which will determine max encoding time: 0 is Good quality, 1 is Realtime and 2 is Best quality
   }}

.. raw:: mediawiki

   {{Clear}}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/vpx.c}}

.. raw:: mediawiki

   {{Documentation}}
