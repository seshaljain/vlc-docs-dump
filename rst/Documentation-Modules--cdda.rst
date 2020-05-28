.. raw:: mediawiki

   {{See also|CD}}

.. raw:: mediawiki

   {{Module|name=cdda|type=Access|first_version=&le; 0.8|description=Read a [[CD]]|sc=cdda|sc2=cddasimple}}

The option ``--cd-audio`` is new as of (2016). The option ``--cdda-caching`` (seems) to be deprecated as of (2018).

The options ``--cdda-track`` plays a particular track (like ``@track`` does). ``--cdda-first-sector`` and ``cdda-last-sector`` seem to be hints to VLC to skip `disk sectors <wikipedia:disk_sector>`__ at the beginning or end.

.. raw:: mediawiki

   {{Option
   |name=cd-audio
   |value=string
   |description=Audio CD device
   }}

.. raw:: mediawiki

   {{Option
   |name=cdda-track
   |value=integer
   |default=0
   |description=NULL
   }}

.. raw:: mediawiki

   {{Option
   |name=cdda-first-sector
   |value=integer
   |default=-1
   |description=NULL
   }}

.. raw:: mediawiki

   {{Option
   |name=cdda-last-sector
   |value=integer
   |default=-1
   |description=NULL
   }}

.. raw:: mediawiki

   {{Option
   |name=cddb-server
   |value=string
   |default=freedb.videolan.org
   |description=Address of the CDDB server to use
   }}

.. raw:: mediawiki

   {{Option
   |name=cddb-port
   |value=integer
   |min=1
   |max=65535
   |default=80
   |description=CDDB Server [[port]] to use
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/cdda.c}}

.. raw:: mediawiki

   {{Documentation}}
