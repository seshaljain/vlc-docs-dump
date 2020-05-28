.. raw:: mediawiki

   {{Protocol|RTP}}

.. raw:: mediawiki

   {{Wikipedia
   |Real-time Transport Protocol|label1=RTP
   |RTP audio video profile|label2=RTP/AVP
   }}

| **RTP** or **Real-time Transport Protocol** is a `protocol <protocol>`__ for streaming media (including `VoIP <VoIP>`__ and video teleconferencing) over the Internet. `RTCP <RTCP>`__ is used alongside this protocol to give feedback on the quality of the connection and `RTSP <RTSP>`__ changes streaming aspects of the connection.
| For example, RTP might stream a video, RTCP might show dropped frames, and RTSP might pause the video playback.
| RTP is often layered on top of `UDP <UDP>`__ because UDP is quicker than `TCP <TCP>`__.

VLC has built-in support for RTP as a server (streaming output). As a client, VLC uses the `LiveMedia <LiveMedia>`__ library.

RTP/AVP
-------

RTP is generic and is extensible through profiles. **RTP/AVP** or **RTP Audio Video Profile** is a *profile* for RTP specific for live multimedia streams. RTP/AVP requires a specified *payload format* to establish which `codecs <codec>`__ will be used. Each has a dedicated RFC, e.g. `RFC 6184 <https://tools.ietf.org/html/rfc6184>`__ for `H.264 <H.264>`__ payload format.

See also
--------

-  `SRTP <SRTP>`__

Links
-----

-  `RFC 3550 <https://tools.ietf.org/html/rfc3550>`__: RTP
-  `RFC 3551 <https://tools.ietf.org/html/rfc3551>`__: RTP/AVP

`Category:Protocols <Category:Protocols>`__
