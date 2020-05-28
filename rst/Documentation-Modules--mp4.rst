Support for fragmented [[MP4]] muxing/demuxing was added in VLC 3.0.0.

The demux module is planned to support [[wikipedia:High Efficiency Image
File Format|HEIF]] in future versions (currently in 4.0.0-dev) through a
<code>heif</code> submodule.

== Demux == {{Moduletype=Access demuxdescription=[[MP4]] stream
demuxername=mp4-m4a-audioonly default=disabled iTunes audio files]] }}
{{Clear}}

== Mux == {{Moduletype=Muxersc=mp4sc3=3gp}} {{Option value=boolean
description=Create "Fast Start" files. "Fast Start" files are optimized
for downloads and allow the user to start previewing the file while it
is downloading }} {{Clear}} === mp4frag ===
{{Moduletype=Muxerdescription=Fragmented and streamable MP4
muxersc2=mp4stream}} {{Clear}}

== Source code == \* {{VLCSourceFilemodules/mux/mp4/mp4.c}}

{{Documentation}}
