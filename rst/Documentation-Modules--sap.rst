.. raw:: mediawiki

   {{Module|name=sap|type=Services discovery|first_version=0.8.2|description=Network streams ([[SAP]])}}

This module will listen on `port <port>`__ 9875 for SAP announcements. The option ``--sap-timeshift`` has been deprecated since 1.0.0 (redundant). Options ``--sap-ipv4`` and ``--sap-ipv6`` have been deprecated since 2.0.0.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=sap-addr
   |value=string
   |default=NULL
   |description=The SAP module normally chooses itself the right addresses to listen to. However, you can specify a specific address
   }}

.. raw:: mediawiki

   {{Option
   |name=sap-timeout
   |value=integer
   |default=1800
   |description=Delay after which SAP items get deleted if no new announcement is received
   }}

.. raw:: mediawiki

   {{Option
   |name=sap-parse
   |value=boolean
   |description=This enables actual parsing of the announces by the SAP module. Otherwise, all announcements are parsed by the "{{docmod|live555}}" (RTP/RTSP) module
   |default=enabled
   }}

.. raw:: mediawiki

   {{Option
   |name=sap-strict
   |value=boolean
   |description=When this is set, the SAP parser will discard some non-compliant announcements
   |default=disabled
   }}

Sub-module
----------

.. raw:: mediawiki

   {{Module|name=sap|type=Services discovery|description=[[SDP]] Descriptions parser|sc=sdp}}

.. _options-1:

Options
~~~~~~~

None.

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/services_discovery/sap.c}}

.. raw:: mediawiki

   {{Documentation}}
