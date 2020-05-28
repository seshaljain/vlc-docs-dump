.. raw:: mediawiki

   {{See also|Documentation:Modules/live555}}

.. raw:: mediawiki

   {{Module|name=rtp|type=Access|first_version=0.7.0|description=Real-Time Protocol ([[RTP]]) input|sc=dccp|sc2=rtptcp|sc3=udplite}}

The only supported format for ``rtp-dynamic-pt`` is ```theora`` <theora>`__.

SRTP
----

The module supports RTP with encryption (`SRTP <SRTP>`__) through using `libgcrypt <https://directory.fsf.org/wiki/Libgcrypt>`__ (`gcrypt manual <https://www.gnupg.org/documentation/manuals/gcrypt/>`__). There are no sub-modules or other shortcuts (in particular, srtp will not work).

Hexadecimal strings are base-16 numbers. Each character is one of 0123456789abcdef (case-insensitive).

Crypto
~~~~~~

Functions of interest (defined in and ) lie in between:

.. code:: c

   #ifdef HAVE_SRTP

and

.. code:: c

   #endif

In summary:

-  SRTP sessions are one-way and re-keyed periodically
-  To set or reset the master key and master salt for an SRTP session ``int srtp_setkey (srtp_session_t *s, const void *key, size_t keylen, const void *salt, size_t saltlen)`` is called
-  The ``setkey`` values are currently hard-coded as `AES <wikipedia:Advanced_Encryption_Standard>`__ in `counter mode <wikipedia:Block_cipher_mode_of_operation#CTR>`__ authenticated with `HMAC <wikipedia:HMAC>`__-`SHA1 <wikipedia:SHA1>`__; the salt with `PRF <wikipedia:Pseudorandom_function_family>`__-AES-CM. There are code comments suggesting this be improved

   -  `SHA1 is deprecated <https://shattered.io/>`__ but using it here should be passably secure for now

-  There are explanations (for hackers) in the form of code comments in the files

Options
-------

.. raw:: mediawiki

   {{Option
   |name=rtcp-port
   |value=integer
   |min=0
   |max=65535
   |description=[[RTCP]] packets will be received on this transport protocol [[port]]. If zero, [[multiplex]]ed RTP/RTCP is used
   |default=0
   }}

.. raw:: mediawiki

   {{Option
   |name=srtp-key
   |value=string
   |description=[[RTP]] packets will be authenticated and deciphered with this Secure RTP master shared secret key. This must be a 32-character-long hexadecimal string
   }}

.. raw:: mediawiki

   {{Option
   |name=srtp-salt
   |value=string
   |description=[[SRTP|Secure RTP]] requires a (non-secret) master [[wikipedia:salt (cryptography)|salt]] value. This must be a 28-character-long hexadecimal string
   }}

.. raw:: mediawiki

   {{Option
   |name=rtp-max-src
   |value=integer
   |min=1
   |max=255
   |description=How many distinct active RTP sources are allowed at a time
   |default=1
   }}

.. raw:: mediawiki

   {{Option
   |name=rtp-timeout
   |value=integer
   |description=How long to wait (in seconds) for any packet before a source is expired
   |default=5
   }}

.. raw:: mediawiki

   {{Option
   |name=rtp-max-dropout
   |value=integer
   |min=0
   |max=32767
   |description=RTP packets will be discarded if they are too much ahead (i.e. in the future) by this many packets from the last received packet
   |default=3000
   }}

.. raw:: mediawiki

   {{Option
   |name=rtp-max-misorder
   |value=integer
   |min=0
   |max=32767
   |description=RTP packets will be discarded if they are too far behind (i.e. in the past) by this many packets from the last received packet
   |default=100
   }}

.. raw:: mediawiki

   {{Option
   |name=rtp-dynamic-pt
   |value=string
   |description=This payload format will be assumed for dynamic payload types (between 96 and 127) if it can't be determined otherwise with out-of-band mappings ([[SDP]])
   |default=NULL
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/rtp/rtp.c}}

.. raw:: mediawiki

   {{Documentation}}
