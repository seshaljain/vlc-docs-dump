{{muxencoder=n}} A special codec used mainly for debugging. This saves
the input as a file (specified by ''demuxdump-file''), without decoding
it.

This is a way to "decode" input to VLC. To output data without a
[[container]], use [[dummy]].

For example, saving the raw input of an [[mp3]] [[shoutcast]] stream can be done with:
   {{%}} vlc <nowiki>http://example.org/shoutcast.mp3\ </nowiki>
   :demux=dump :demuxdump-file=output.mp3

== Module options == \* demuxdump-file (file name) *: File to output
data, default: "stream-demux.dump"* demuxdump-append ([[boolean]]) \*:
Append data to file. Set as true to append data, or false (default) to
overwrite the file with the new data.

== Source code == {{fileinput demuxer}}
