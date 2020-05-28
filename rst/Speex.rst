{{Codec audioencoder=yfor=[[Ogg]]}} {{Websitehttps://www.speex.org/}}
{{Xiph|Speex}} {{Open}}

'''Speex''' is a deprecated speech-oriented audio codec designed for use
over packet networks (e.g. [[HTTP]], local network use) and [[VoIP]]
applications. As of 2013, Speex.org recommends parties consider [[Opus]]
instead, calling the Opus codec superior.

It supports [[compression]] in a [[lossy]] way. It uses [[CELP]] (Code
Excited Linear Prediction) to compress, meaning it takes advantage of
the frequency patterns of human speech to efficiently compress data;
this also means harmonics that do not follow this pattern will perform
poorly (e.g. electronic music). {{VLC}} has supported decoding and
encoding Speex since version 0.7.0.

== Source code == \* {{VLCSourceFile|modules/codec/speex.c}}
