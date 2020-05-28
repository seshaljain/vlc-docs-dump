\__FORCETOC_\_

Access
------

.. raw:: mediawiki

   {{Module|name=udp|type=Access|description=[[UDP]] input|sc=udp|sc2=udpstream|sc3=udp4|sc4=udp6}}

The options ``--server-port`` and ``--udp-buffer`` were deprecated in 2.0.0 and 3.0.0. ``--udp-timeout`` was added in 3.0.0.

.. raw:: mediawiki

   {{Option
   |name=udp-timeout
   |value=integer
   |default=-1
   |description=[[UDP]] Source timeout (sec)
   }}

.. raw:: mediawiki

   {{Clear}}

Access output
-------------

.. raw:: mediawiki

   {{Module|name=udp|type=Access output|description=[[UDP]] stream output|sc=udp}}

.. raw:: mediawiki

   {{Option
   |name=sout-udp-caching
   |value=integer
   |default=<code><var>DEFAULT_PTS_DELAY</var> / 1000</code>
   |description=Default caching value for outbound [[UDP]] streams. This value should be set in milliseconds
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-udp-group
   |value=integer
   |default=1
   |description=Packets can be sent one by one at the right time or by groups. You can choose the number of packets that will be sent at a time. It helps reducing the scheduling load on heavily-loaded systems
   }}

.. raw:: mediawiki

   {{Clear}}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/udp.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access_output/udp.c}}

.. raw:: mediawiki

   {{Documentation}}
