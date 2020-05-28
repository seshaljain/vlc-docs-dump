{{ProtocolSession Announcement Protocol}} '''SAP''' stands for
'''Session Announcement Protocol'''. It is defined in
[https://tools.ietf.org/html/rfc2974 RFC 2974].<br /> It uses
[[multicast]] to announce streams efficiently on a Local Area Network or
on the [[MBONE]]: any computer on the network can receive announces from
all others without any manual configuration.

SAP conveys [[SDP]]'s to describe streams parameters. This can include
an [[RTSP]] control URL to use for setting up the stream, or a multicast
group address to subscribe to. The SDP also includes port numbers and
audio/video codecs parameters, and a stream name, etc.

This technique allows a lot of server to emit streams (often
multicasted) and announce them on the network. Clients on the network
can then listen for these announces.<br /> VLC can do this with the
"SAP" service discovery plugin.<br /> You then get a listing of all
these streams and can simply ''tune'' into the stream of your choice.

Because SAP uses [[multicast]] (as do [[wikipedia:UPnPBonjour]]), it can
normally only operate on a Local area network.<br /> Unless your
computer is connected to the [[MBONE]], you cannot use SAP to advertise
your streams onto the Internet, nor can you receive streams from other
places.

== See also == \* [[MiniSAPServer]] \*
[http://www.uninett.no/multimedia/streamingguide/alle.html Example of
what is announced via SAP on the MBONE]{{dead link}}

[[Category:Protocols]]
