{{SoCProjectstudent=[[User:tuttlementor=Benjamin Larsson}}

==Abstract==

I'm working on the OMA demuxer in libavformat to implement a decryptor
for OpenMG protected audio files. If I can complete this task in time, I
will work on finishing an ATRAC3plus decoder for libavcodec.

==OMA Decryptor== ===Overview=== <blockquote>''The idea of the Sony DRM
is that there are up to 232 different "root keys" used for different
purposes. Each of these root keys is distributed in the form of EKBs
(enabling key blocks) which contain the root key in encrypted form. The
EKBs are considered to be public. All devices and software products
taking part in the Sony rights-management system are identified by their
64-bit product ID (called leaf ID in Sony speak). Each n-bit-prefix of
the product ID is associated with a specific key (called node key in
Sony speak) that all devices having a device ID in that specific range
share. In the easiest case, the EKB contains the root key encrypted with
some of these node keys, in more convoluted cases, the EKB contains key
chains.''<sup>[[#ref_anon|note]]</sup></blockquote>

===Header Format=== Standard ID3 headers are used in .oma files (usually
v2.3) with the magic "ea3" instead of "ID3"
[http://wiki.multimedia.cx/index.php?title=Oma]. Encryption headers are
stored as binary data within a GEOB frame
[http://www.id3.org/d3v2.3.0#line-1400] with content description
"OMG_LSI" or "OMG_BKLSI". The ID3 header is followed by an "EA3" header
of size 0x60 bytes.

===GEOB Binary Data Format=== All values big-endian, i.e. network byte
order.

'''Header:''' <pre> [2 bytes] version (must be 1) [2 bytes] n1: size of
the keyring subobject (should be 0x40) [2 bytes] n2: size of the EKB
subobject [2 bytes] n3: size of the ID subobject [2 bytes] n4: size of
the signature subobject (must be 8) [6 bytes] padding to get the main
object header to 16 bytes [n1 bytes] keyring subobject [n2 bytes] EKB
subobject [n3 bytes] ID subobject [n4 bytes] signature subobject </pre>

'''Keyring subobject:''' <pre> subobject header: [12 bytes] subobject
ID, must be "KEYRING " (5 spaces at the end) [2 bytes] subobject slice
size (should be 16) [2 bytes] subobject slice count (should be 3, does
not include the header which always occupies one slice, so slice size
can not be lower than 16 bytes)

subobject body:
   [2 bytes] amount of used data bytes in the body (this field included,
   should be 0x28) [10 bytes] unknown [4 bytes] ID of the root key used
   to encrypt the keys in the keyring [8 bytes] file master key 3-DES
   encrypted by the root key. [8 bytes] content encryption key DES
   "decrypted" by the file master key [8 bytes] unknown

subobject padding:
   [8 bytes] padding to fill the last slice

</pre>

'''EKB subobject:''' <pre> (optional) header: "EKB " followed by 28
bytes of zero.

(mandatory) The EKB:
   [4 bytes] EKB ID (should always match the required root key ID from
   the keyring) [4 bytes] reserved (usually 0x0) [24 bytes] key check
   value, this value 3-DES decrypted with the EKB root key should yield
   to: EKB root key + EKB ID + 4 bytes random padding (the value can be
   used to test if a root key is valid for an EKB if the ID is unknown)
   [4 bytes] tlen: tag length [4 bytes] dlen: data length [4 bytes] sig
   length [tlen bytes] tags (this can be used to see if a node key has
   an entry point in the EKB) [dlen bytes] blocks of 24 bytes, each
   being the root key for this EKB 3-DES encrypted with a node key [4
   bytes] significant tag length [rest of the subobject] some ECDSA
   sigs, irrelevant for key recovery

</pre>

Example output of an EKB (from
[http://samples.mplayerhq.hu/oma/03-Exodus.oma]): <pre> EKB ID: 0x1001d
Reserved: 0x0 Unknown 3:
3947f40a33652f987173c39868c5235b8420c8cffb0e7f4e Tag Length: 0xc Data
Length: 0x50 Sig Length: 0x34 Tags: 851451450402fffe00000000 Data:
36d200387491519da7759470a01769da Enc(K00000000,KR)
6955aea69f6a3e6918c7c6bbd7ccfb1b Enc(K00000001,KR)
818da9979067295cb7555aec211b9ebd Enc(K00000010,KR)
d47ed90979e039a1e076680db8bfedb0 Enc(K00000011,KR)
d32426b8f77922bd46c9449fdf0174c0 Enc(K11111111,KR) Significant Tag
Length: 0x8 Sig ID: 0x1 Sig Len: 0x28 ECDSA r:
db546ac5e04d4fcbf2463b01de2cd0fbaf7aa71e ECDSA s:
ef442905979dbee7284ea4533a2f71c7cb865839 </pre>

K00000000 is Sony's nomenclature meaning the key for the device group
whose device ID starts with 0 bits of zero. See the EKB dumping script
[https://wiki.physik.fu-berlin.de/linux-minidisc/doku.php?id=dump_ekb]
for details on the EKB format and how to identify keys in the tag/data
section. The ID of the key used by Sonic Stage in their .oma files is
0x0001001d, and this also seems to used in almost any .oma file out
there.

A more complex example of an EKB with key chains: <pre> EKB ID: 0x1000a
Reserved: 0x0 Key chec val:
68869089b724181ee860041d2eb3fddbe74c7ccdb1e306c0 Tag Length: 0x1c Data
Length: 0x130 Sig Length: 0x34 Tags:
a49248039e4d208040007fffff8240e002492493fffff00000000000 Data:
2798095a2e864002d58f1f68fa25fb91 Enc(K000000000,KR)
2545064deaca14f996bdc8a406c22b81 Enc(K000000010,KR)
66eb2dff4e3752253f5915e451d94aad Enc(K0000000110,KR)
a8ecfb6c65c949f7c47de8f96df6bd2b Enc(K00000001100000,K0000000110)
7d5b1a6ef42253538b6b1dfb81380d4a Enc(K00000001100001,K0000000110)
e7215b57914edff8a3d9930b5a4faa55 Enc(K00000001100010,K0000000110)
24aa87026900960ab3df6a20a9f1ead4 Enc(K00000001100011,K0000000110)
e66453a64523f244e2378b87d3518dc1 Enc(K00000001100100,K0000000110)
be2d2af50cf2a2d9be91769e835e6300 Enc(K00000001100101,K0000000110)
846a3f493e6dd0fddaf83beb59f7c1cf Enc(K00000001100110,K0000000110)
569501035dbdc3e6a579482d76489800 Enc(K00000001100111,K0000000110)
bd7983a89133d9e679210b241f4580e3 Enc(K00000000100000000,KR)
62511ba02562e3166401caa2f4f2eb01 Enc(K0000000010000001010,KR)
67ccc10fef049f9479c7eab249cc0560 Enc(K0000000010000001100,KR)
a1955eeb7bd2fe5d2bb9cef90195c10a Enc(K0000000010000001110,KR)
65d4735bac760a45788f669b26d4c0e0 Enc(K0000000010000010000,KR)
80b14ed5872e3c6b0c987ae5961a9567 Enc(K0000000010000010010,KR)
8a3bff4f583e6a8288cddcb6f5e05228 Enc(K0000000010000010100,KR)
fe2357f456e78ba190db9bf231026a1f Enc(K00000000100000010000,KR)
Significant Tag Length: 0x17 Sig ID: 0x1 Sig Len: 0x28 ECDSA r:
74a60db08631afd1374201938e3425adab577d30 ECDSA s:
deb9c346ac19e889af451905fefd0024e3772cfe verify OK: True </pre>

'''ID subobject:'''

The ID subobject consists of different sub-subobjects formatted like the
keyring object, details unnecessary for key recovery.

'''Signature subobject:'''

The signature subobject is the single-DES CBC-MAC of the ID subobject,
using a key derived from the file master key. You obtain the signature
key by encrypting 8 bytes of 0 with the file master key. You can use
this signature to verify that the key recovery worked.

===EA3 Header=== In encrypted .oma files, the encryption field at offset
6/7 is set to 1 and the last 8 bytes of the header, i.e. offset 0x58 in
that header, are the IV for the data starting at offset 0x60.

==PCM support== Oma files can carry linear PCM data, in this case the
byte at offset 32 in the EA3 header has the value 4. PCM support is
easily integrated with the decryptor and FFmpeg's existing PCM codec.
The only format parameters observed so far are: 44.1 kHz sample rate, 16
bit sample size, stereo mode, big-endian. Other parameters might be
used, but that needs to be tested with a device (the files cannot be
generated with Sonic Stage).

==ATRAC3plus Decoder== The current state of the ATRAC3plus decoder is
unknown. Development has not been started during GSoC, but will
afterwards.

==Repository== [https://github.com/plumbojumbo/FFmpeg
https://github.com/plumbojumbo/FFmpeg]

==Contact==

You can reach me at firstname.lastname@gmail.com or as atuttle on
Freenode. Feel free to get in touch with me if you have any questions.

==Notes== #<span id="ref_anon">The system has been extensively reverse
engineered by an anonymous source on whose results this information and
the implementation is gratefully based on.</span>

==Links==
*http://wiki.multimedia.cx/index.php?title=Oma*\ http://www.waider.ie/hacks/workshop/c/mple/FILE_FORMAT_v2.txt
\*\ https://wiki.physik.fu-berlin.de/linux-minidisc/doku.php?id=dump_ekb
