{{websitehttps://ffmpeg.org/}} {{open}}

'''FFmpeg''' is an [[open source]] library for encoding and decoding
different types of media files, generally [[MPEG]] and MPEG-based files.

FFmpeg supports lots of [[codec]]s: the main ones are included on the
codecs page. If you want the full list, (including different spellings
for the same codec), the [[source code]] lists them all (there's way too
many to list them all here <span title="wink">;-)</span>. In
{{VLCSourceFile|modules/codec/avcodec/fourcc.c}} look under ''Codec
fourcc -> ffmpeg_id mapping'' (that bit changes the codecs you type in
to vlc to ffmpeg's internal codec names).

== Avcodec == {{See|Documentation:Modules/avcodec}}

== Avformat == {{See also|Documentation:Modules/avformat}}

The libavformat [[module]] is a [[mux]] and a [[demux]] module for
{{VLC}}, based on the libavformat library.

It can decode and encode most of the containers supported in VLC, but is
not usually the default one, except for a few ones, listed under.

{{muxmod=avformatid=mxfencoder=n}} {{muxmod=avformatid=nutencoder=y}}
{{muxmod=avformatid=rmencoder=n}}

==Source code== {{filecodec}}

[[Category:Libraries]] [[Category:Third parties]]

{{stub}}
