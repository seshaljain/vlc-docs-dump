{{Moduletype=Muxer|description=[[ASF]] muxer}}

Shortcuts to this module are <code>asf</code> and <code>asfh</code>.
Support for demuxing was added in 0.5.0. Support for muxing was added
sometime prior to 0.8.0, as the changelog says "Improved ASF muxer" for
0.8.0. Support for images/cover art was added in 2.0.0.

== Options == <onlyinclude> {{Option value=string description=Title to
put in ASF comments }} {{Option value=string description=Author to put
in ASF comments }} {{Option value=string description=Copyright string to
put in ASF comments }} {{Option value=string description=Comment to put
in ASF comments }} {{Option value=string description="Rating" to put in
ASF comments }} {{Option value=integer description=ASF packet size }}
{{Option value=integer description=Do not try to guess ASF [[bitrate]].
Setting this, allows you to control how [[Windows Media Player]] will
cache streamed content. Set to audio+video bitrate in bytes
}}</onlyinclude>

== Source code == \* {{VLCSourceFilemodules/demux/asf}} \*
{{VLCSourceFilemodules/demux/asf/libasf.c}} (stream demuxer)

{{Documentation}}
