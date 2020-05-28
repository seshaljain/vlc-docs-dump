{{See alsoname=rtpfirst_version=0.7.0sc=dccpsc3=udplite}}

The only supported format for <code>rtp-dynamic-pt</code> is
<code>[[theora]]</code>.

== SRTP == The module supports RTP with encryption ([[SRTP]]) through
{{VLCSourceFilel=srtp.c}} using
[https://directory.fsf.org/wiki/Libgcrypt libgcrypt]
([https://www.gnupg.org/documentation/manuals/gcrypt/ gcrypt manual]).
There are no sub-modules or other shortcuts (in particular,
<kbd>srtp</kbd> will not work).

Hexadecimal strings are base-16 numbers. Each character is one of
<kbd>0123456789abcdef</kbd> (case-insensitive).

=== Crypto === Functions of interest (defined in
{{VLCSourceFilel=srtp.c}} and {{VLCSourceFilel=srtp.h}}) lie in
{{VLCSourceFilel=rtp.c}} between: <syntaxhighlight lang="c"> #ifdef
HAVE_SRTP </syntaxhighlight> and <syntaxhighlight lang="c"> #endif
</syntaxhighlight>

In summary: \* SRTP sessions are one-way and re-keyed periodically \* To
set or reset the master key and master salt for an SRTP session
<code>int srtp_setkey (srtp_session_t *s, const void*\ key, size_t
keylen, const void *salt, size_t saltlen)</code> is called* The
<code>setkey</code> values are currently hard-coded as
[[wikipedia:Advanced Encryption Standardcounter mode]] authenticated
with [[wikipedia:HMACSHA1]]; the salt with [[wikipedia:Pseudorandom
function family|PRF]]-AES-CM. There are code comments suggesting this be
improved \*\* [https://shattered.io/ SHA1 is deprecated] but using it
here should be passably secure for now \* There are explanations (for
hackers) in the form of code comments in the files

== Options == {{Option value=integer max=65535 default=0 }} {{Option
value=string name=srtp-salt description=[[SRTPsalt]] value. This must be
a 28-character-long hexadecimal string }} {{Option value=integer max=255
default=1 }} {{Option value=integer default=5 }} {{Option value=integer
max=32767 default=3000 }} {{Option value=integer max=32767 default=100
}} {{Option value=string default=NULL }}

== Source code == \* {{VLCSourceFile|modules/access/rtp/rtp.c}}

{{Documentation}}
