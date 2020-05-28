{{ProtocolReal-time Transport ProtocolRTP audio video
profile|label2=RTP/AVP }} '''RTP''' or '''Real-time Transport
Protocol''' is a [[protocol]] for streaming media (including [[VoIP]]
and video teleconferencing) over the Internet. [[RTCP]] is used
alongside this protocol to give feedback on the quality of the
connection and [[RTSP]] changes streaming aspects of the connection.<br
/> For example, RTP might stream a video, RTCP might show dropped
frames, and RTSP might pause the video playback.<br /> RTP is often
layered on top of [[UDP]] because UDP is quicker than [[TCP]].

VLC has built-in support for RTP as a server (streaming output). As a
client, VLC uses the [[LiveMedia]] library.

== RTP/AVP == <!-- [[AVP]] and [[RTP/AVP]] redirect to this section. -->
RTP is generic and is extensible through profiles. '''RTP/AVP''' or
'''RTP Audio Video Profile''' is a ''profile'' for RTP specific for live
multimedia streams. RTP/AVP requires a specified ''payload format'' to
establish which [[codec]]s will be used. Each has a dedicated RFC, e.g.
[https://tools.ietf.org/html/rfc6184 RFC 6184] for [[H.264]] payload
format.

== See also == \* [[SRTP]]

== Links == \* [https://tools.ietf.org/html/rfc3550 RFC 3550]: RTP \*
[https://tools.ietf.org/html/rfc3551 RFC 3551]: RTP/AVP

[[Category:Protocols]]
