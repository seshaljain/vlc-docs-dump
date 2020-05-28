{{Protocol|SDP}}

SDP stands for "Session Description Protocol". It is used to describe a
[[stream]]ing session. SDP data is usually carried over [[SAP]],
[[RTSP]] or in dedicated files.

The idea behind SDP is that you can store critical stream information in
the SDP and distribute this over a reliable connection (such as [[HTTP]]
or [[RTSP]]). Then you can stream the raw codec data over a lossy
connection, such as [[RTP]] without the need for a container.

== Links == \* [https://tools.ietf.org/html/rfc4566 RFC 4566]

== Source code == \* {{VLCSourceFile|modules/access/sdp.c}}
