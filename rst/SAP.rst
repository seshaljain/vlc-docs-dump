.. raw:: mediawiki

   {{Protocol|SAP}}

.. raw:: mediawiki

   {{wikipedia|Session Announcement Protocol}}

| **SAP** stands for **Session Announcement Protocol**. It is defined in `RFC 2974 <https://tools.ietf.org/html/rfc2974>`__.
| It uses `multicast <multicast>`__ to announce streams efficiently on a Local Area Network or on the `MBONE <MBONE>`__: any computer on the network can receive announces from all others without any manual configuration.

SAP conveys `SDP <SDP>`__'s to describe streams parameters. This can include an `RTSP <RTSP>`__ control URL to use for setting up the stream, or a multicast group address to subscribe to. The SDP also includes port numbers and audio/video codecs parameters, and a stream name, etc.

| This technique allows a lot of server to emit streams (often multicasted) and announce them on the network. Clients on the network can then listen for these announces.
| VLC can do this with the "SAP" service discovery plugin.
| You then get a listing of all these streams and can simply *tune* into the stream of your choice.

| Because SAP uses `multicast <multicast>`__ (as do `UPnP <wikipedia:UPnP>`__ and Apple `Bonjour <wikipedia:Bonjour_(software)>`__), it can normally only operate on a Local area network.
| Unless your computer is connected to the `MBONE <MBONE>`__, you cannot use SAP to advertise your streams onto the Internet, nor can you receive streams from other places.

See also
--------

-  `MiniSAPServer <MiniSAPServer>`__
-  `Example of what is announced via SAP on the MBONE <http://www.uninett.no/multimedia/streamingguide/alle.html>`__\ 

`Category:Protocols <Category:Protocols>`__
