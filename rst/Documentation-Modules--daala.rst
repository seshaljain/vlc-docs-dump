.. raw:: mediawiki

   {{Module|name=daala|type=Muxer|first_version=3.0.0|description=[[Daala]] video encoder}}

Support for this module comes from the libdaala `library <library>`__.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=sout-daala-quality
   |value=integer
   |default=10
   |min=0
   |max=511
   |description=Enforce a quality between 0 (lossless) and 511 (worst)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-daala-keyint
   |value=integer
   |default=256
   |min=1
   |max=1000
   |description=Enforce a [[keyframe]] interval between 1 and 1000
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-daala-chroma-fmt
   |value=string
   |default=420
   |select={420,444}
   |description=Picking [[chroma]] format will force a conversion of the video into that format. <code>420</code> means <code>[[4:2:0]] Y'CbCr</code> and <code>444</code> means <code>[[4:4:4]] Y'CbCr</code>
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/daala.c}}

.. raw:: mediawiki

   {{Documentation}}
