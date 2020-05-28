{{WikipediaUDP-Lite}}

'''UDP''' ('''User Datagram Protocol''') is a so-called "send and pray"
[[protocol]]. You throw data onto the network and have no guarantee of
when (if ever) it reaches its destination. Nonetheless, it is used
because it is extremely fast and efficient.

Next to [[TCP]], it is one of the primary basic [[IP|Internet
Protocols]] that every major OS supports.

Raw UDP cannot normally be used for streaming. [[RTP]] is used on top of
UDP to provide proper data timestamps and ordering. RTP/UDP is
extensively used for streaming live audio/video. In this case it is not
important that you receive ''all'' data, as long as you receive ''some''
data continuously and fast.

Although VLC supports this protocol for streaming, not all audio and
video codecs can be used.

See the [http://www.videolan.org/streaming-features.html Streaming
features list] for further details.

[[Category:Protocols]]
