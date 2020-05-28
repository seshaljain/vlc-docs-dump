.. raw:: mediawiki

   {{Protocol|SDP}}

SDP stands for "Session Description Protocol". It is used to describe a `streaming <stream>`__ session. SDP data is usually carried over `SAP <SAP>`__, `RTSP <RTSP>`__ or in dedicated files.

The idea behind SDP is that you can store critical stream information in the SDP and distribute this over a reliable connection (such as `HTTP <HTTP>`__ or `RTSP <RTSP>`__). Then you can stream the raw codec data over a lossy connection, such as `RTP <RTP>`__ without the need for a container.

Links
-----

-  `RFC 4566 <https://tools.ietf.org/html/rfc4566>`__

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/sdp.c}}
