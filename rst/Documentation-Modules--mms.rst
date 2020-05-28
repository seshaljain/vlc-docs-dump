.. raw:: mediawiki

   {{Module|name=mms|type=Access|first_version=0.5.0|description=[[MMS]] input|sc=mms|sc2=mmsh|sc3=mmst|sc4=mmsu}}

Handles Microsoft Media Server `UDP <UDP>`__, `TCP <TCP>`__ and `HTTP <HTTP>`__ variants, including the ability to open mms:// and mmsh:// `MRLs <MRL>`__.

In the source code for mms module it says:

| `` * NOTES:``
| `` *  MMSProtocole documentation found at http://get.to/sdp``

get.to/sdp is now located at sdp.ppona.com. This document is pertinent: (`MMSprotocol.pdf <http://sdp.ppona.com/zipfiles/MMSprotocol.pdf>`__ or `archived copy <https://archive.today/QClst>`__)

Options
-------

.. raw:: mediawiki

   {{Option
   |name=mms-caching
   |value=integer
   |description=Caching in ms
   }}

.. raw:: mediawiki

   {{Option
   |name=mms-all
   |default=disabled
   |description=Force selection of all streams
   }}

.. raw:: mediawiki

   {{Option
   |name=mms-maxbitrate
   |value=integer
   |default=0
   |description=Select the stream with the maximum [[bitrate]] under this limit
   }}

.. raw:: mediawiki

   {{Option
   |name=mmsh-proxy
   |value=string
   |default=""
   |description=HTTP proxy for the HTTP MMS variant. <code><nowiki>http://[user[:password]@]proxy.example.com:</nowiki>[[port]]/</code>
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFolder|modules/access/mss}}

   (folder)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/mms/mms.c}}

   (main file)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/mms/mmsh.c}}

   (MMS over HTTP)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/mms/mmstu.c}}

   (MMS over TCP or UDP)

.. raw:: mediawiki

   {{Stub}}

.. raw:: mediawiki

   {{Documentation footer}}
