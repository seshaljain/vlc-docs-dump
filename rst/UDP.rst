.. raw:: mediawiki

   {{Wikipedia|User Datagram Protocol}}

.. raw:: mediawiki

   {{See also|UDP-Lite}}

**UDP** (**User Datagram Protocol**) is a so-called "send and pray" `protocol <protocol>`__. You throw data onto the network and have no guarantee of when (if ever) it reaches its destination. Nonetheless, it is used because it is extremely fast and efficient.

Next to `TCP <TCP>`__, it is one of the primary basic `Internet Protocols <IP>`__ that every major OS supports.

Raw UDP cannot normally be used for streaming. `RTP <RTP>`__ is used on top of UDP to provide proper data timestamps and ordering. RTP/UDP is extensively used for streaming live audio/video. In this case it is not important that you receive *all* data, as long as you receive *some* data continuously and fast.

Although VLC supports this protocol for streaming, not all audio and video codecs can be used.

See the `Streaming features list <http://www.videolan.org/streaming-features.html>`__ for further details.

`Category:Protocols <Category:Protocols>`__
