{{muxencoder=n}}

PVA is the extension denoting [[Packetize]]d Elementary Streams (PES)
containing both video and audio. PES files are muxed [[elementary
stream]]s. By their nature elementary streams are only audio or video
files. However, by recording [[timestamp]]s PVA files can contain both
with a low overhead for [[muxing]] real-time [[MPEG-2 video]] with
[[AC3]] Dolby Digital audio. Such files are often recorded with Digital
Video Broadcast [[DVB]] capturing software.

==Source code== {{fileinput demuxer}}
