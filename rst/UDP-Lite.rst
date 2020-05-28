{{See alsoUDP-Lite}}

UDP-Lite is a protocol similar to [[UDP]] that delivers streams of data
even if deemed "damaged". This may be useful in some noisy network
environments where data may get lost.
[https://tools.ietf.org/html/rfc3828 RFC 3828] suggests UDP-Lite to be
applicable for salvaging voice and video codecs, mentioning [[H.264]]
and [[MPEG-4]] by name: this is because these and similar codecs already
do integrity checks in the form of checksums. VLC has had UDP-Lite
support (input RTP/AVP, output RTP) since 0.9.0.

For more information, see [https://erg.abdn.ac.uk/users/gerrit/udp-lite/
UDP Lite Wiki]

[[Category:Glossary]] [[Category:Protocols]]
