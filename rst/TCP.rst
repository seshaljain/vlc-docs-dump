.. raw:: mediawiki

   {{Wikipedia|TCP}}

**TCP** stands for **Transmission Control Protocol**. It is a connection-oriented, reliable delivery byte-stream transport layer communication `protocol <protocol>`__, currently documented in `IETF RFC 793 <https://tools.ietf.org/html/rfc793>`__. During the data transfer phase, a number of key mechanisms determine TCP's reliability and robustness. These include using sequence numbers for ordering received TCP segments and detecting duplicate data, checksums for segment error detection, and acknowledgements and timers for detecting and adjusting to loss or delay.

TCP is not appropriate for many applications as for example, real-time applications. They often don't need, and will suffer from TCP's reliable delivery mechanisms. In those types of applications it is often better to deal with some loss, errors or congestion than to try to adjust for them. Example applications that do not typically use TCP include multimedia streaming, real-time multiplayer games and voice over IP (`VoIP <VoIP>`__). In many cases, the User Datagram Protocol (`UDP <UDP>`__) may be used in place of TCP when just application multiplexing services are required.

`Category:Protocols <Category:Protocols>`__
