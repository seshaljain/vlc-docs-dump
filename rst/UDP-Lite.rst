.. raw:: mediawiki

   {{See also|UDP}}

.. raw:: mediawiki

   {{Wikipedia|UDP-Lite}}

UDP-Lite is a protocol similar to `UDP <UDP>`__ that delivers streams of data even if deemed "damaged". This may be useful in some noisy network environments where data may get lost. `RFC 3828 <https://tools.ietf.org/html/rfc3828>`__ suggests UDP-Lite to be applicable for salvaging voice and video codecs, mentioning `H.264 <H.264>`__ and `MPEG-4 <MPEG-4>`__ by name: this is because these and similar codecs already do integrity checks in the form of checksums. VLC has had UDP-Lite support (input RTP/AVP, output RTP) since 0.9.0.

For more information, see `UDP Lite Wiki <https://erg.abdn.ac.uk/users/gerrit/udp-lite/>`__

`Category:Glossary <Category:Glossary>`__ `Category:Protocols <Category:Protocols>`__
