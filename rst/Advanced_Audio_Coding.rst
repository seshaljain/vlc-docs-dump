{{HydrogenaudioAdvanced Audio Coding|Understanding AAC}} AAC is a set of
codecs designed to provide better compression than [[MP3]]s, and are
improved versions of [[MPEG]] audio.

AAC has many options and profiles available.

== Introduction == AAC actually refers to two similar codecs - MPEG-2
Part 7 (Advanced Audio Coding) and MPEG-4 Part 3. It has many options
and is heavily customisable depending on the desired output

It has some advantages over MP3 - it has a greater range of sample
frequencies, up to 48 channels and higher coding efficiency. It also has
much better handling of frequencies above 16 kHz. Depending on the AAC
profile and the MP3 encoder, 96 kbit/s AAC can give nearly the same or
better perceptional quality as 128 kbit/s MP3.

MPEG-4 AAC is used by [[iTunes]] and [[iPod]] (see also
[https://web.archive.org/web/20031202022159/http://www.apple.com/mpeg4/aac/
Apple webpage on AAC]) and most of the portable devices.

== Profiles and extensions ==

=== Main === The main codec for AAC, as defined in MPEG-2, had 3
profiles: \* Low Complexity profile (LC) \* Main profile (Main) \*
Scalable Sampling Rate (SSR)

In MPEG-4, it combines it with Perceptual Noise Substitution (PNS)
extension.

=== ER - Error Resilience === This is an extension to improve error
resilience on AAC.

=== LD - Low Delay ===

LD is an 2000 extension used to improve AAC for 2-way communication.

=== ELD - Extended Low Delay ===

ELD is a 2008 extension of AAC that improves LD further.

=== LTP === LTP is an extension from 1999 that uses
[[wikipedia:Long_Term_Prediction|Long Term Prediction]].

=== He-AAC / AAC+ === {{wikipedia|HE-AAC}}

'''High Efficiency AAC''' (aka '''aacPlus'''), is a [[lossy]] data
compression scheme for audio streams, and is part of the '''[[MPEG-4]]
Part 3''' specification.

HE-AAC combines [[Advanced Audio Coding]] (AAC) with
[[wikipedia:spectral band replication|spectral band replication]] (SBR)

=== He-AACv2 / eAAC+ ===

Enhanced aacPlus combines SBR and [[wikipedia:Parametric
Stereo|Parametric Stereo]] (PS). The [[codec]] can operate at very low
bitrates and is good for [[internet radio]] streaming. A 48
kilobit-per-second stream is considered to have higher quality than 128
[[kbit/s]] [[MP3]].

=== SLS / HD-AAC === MPEG-4 Scalable to Lossless is a 2006 extension to
add Lossless support to AAC.

It copies the idea of wavpack hybrid to encode and split the difference
between lossy and lossless versions.

Some version of SLS is marketed as HD-AAC

== VLC support == {{codec audioid=mp4a}}

=== Decoding === VLC supports AAC and HE-AAC through the libraries
[[libfaad]] and [[libavcodec]].

The FAAD module supports Main (Main, LC, SSR), LD, ER, LTP, SBR and
PS.<br /> It should decode AAC, HeAAC and HeAACv2 streams. It should not
decode HD-AAC/AAC-SLS or AAC-ELD streams.

The avcodec module supports Main (Main, LC), LTP, SBR and ALS.

=== Encoding === VLC support AAC encoding through the [[libavcodec]]
library.
