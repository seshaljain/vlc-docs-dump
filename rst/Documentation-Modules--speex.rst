This module consists of a decoder, packetiser submodule and encoder submodule. Only `the encoder <#Mux>`__ has any options.

Demux
-----

.. raw:: mediawiki

   {{Module|name=speex|type=Access demux|first_version=0.7.0|description=[[Speex]] audio decoder|sc=none}}

Options
~~~~~~~

None.

Packetizer
----------

.. raw:: mediawiki

   {{Module|name=speex|type=Packetizer|first_version=0.7.0|description=[[Speex]] audio [[packetizer]]|sc=none}}

.. _options-1:

Options
~~~~~~~

None.

Mux
---

.. raw:: mediawiki

   {{Module|name=speex|type=Muxer|first_version=0.7.0|description=[[Speex]] audio encoder|sc=none}}

.. _options-2:

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-speex-mode
   |value=integer
   |default=0
   |select={0,1,2}
   |description=Enforce the mode of the encoder: 0 - Narrow-band (8kHz), 1 - Wide-band (16kHz), 2 - Ultra-wideband (32kHz)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-speex-complexity
   |value=integer
   |default=3
   |min=1
   |max=10
   |description=Enforce the complexity of the encoder
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-speex-cbr
   |value=boolean
   |default=disabled
   |description=Enforce a [[constant bitrate]] encoding (CBR) instead of default variable bitrate encoding (VBR)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-speex-quality
   |value=float
   |default=8.0
   |min=0.0
   |max=10.0
   |description=Enforce a quality between 0 (low) and 10 (high)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-speex-max-bitrate
   |value=integer
   |default=0
   |description=Enforce the maximal VBR bitrate
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-speex-vad
   |value=boolean
   |default=enabled
   |description=Enable [[wikipedia:voice activity detection|voice activity detection]] (VAD). It is automatically activated in VBR mode
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-speex-dtx
   |value=boolean
   |default=disabled
   |description=Enable [[wikipedia:discontinuous transmission|discontinuous transmission]] (DTX)
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/speex.c}}

.. raw:: mediawiki

   {{Documentation}}
