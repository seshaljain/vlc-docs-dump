.. raw:: mediawiki

   {{Module|name=fdkaac|type=Muxer|first_version=2.1.0|description=[[fdk-aac|FDK-AAC]] Audio encoder|sc=fdkaac}}

This module is dual-licenced under LGPL 2.1 and BSD 2-clause. (`FAAC <FAAC>`__) used to handle encoding `AAC <AAC>`__, but it is .

Options
-------

.. raw:: mediawiki

   {{Option
   |name=sout-fdkaac-profile
   |value=integer
   |default=<var>PROFILE_AAC_LC</var>
   |select={2,5,29,23,39}
   |description=Encoder Algorithm to use (2: AAC-LC, 5: HE-AAC, 29: HE-AAC-v2, 23: AAC-LD, 39: AAC-ELD)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-fdkaac-sbr
   |value=boolean
   |default=disabled
   |description=Enable [[wikipedia:spectral band replication|spectral band replication]]&mdash;This is an optional feature only for the AAC-ELD profile
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-fdkaac-vbr
   |value=integer
   |default=0
   |min=0
   |max=5
   |description=Quality of the [[VBR]] Encoding (0=cbr, 1-5 constant vbr quality, 5 is the best)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-fdkaac-afterburner
   |value=boolean
   |default=enabled
   |description=This library will produce higher quality audio at the expense of additional CPU usage (default is enabled)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-fdkaac-signaling
   |value=integer
   |default=<var>SIGNALING_COMPATIBLE</var>
   |min=0
   |max=2
   |description=1 is explicit for SBR (<var>SIGNALING_COMPATIBLE</var>) and implicit for [[PS]] (default), 2 is explicit hierarchical
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/fdkaac.c}}

.. raw:: mediawiki

   {{Documentation}}
