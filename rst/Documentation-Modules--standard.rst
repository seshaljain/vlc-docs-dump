{{Moduletype=Stream outputsc=standard|sc2=std}}

The option <code>sout-standard-group</code> was deprecated in 2.1.0. The
option <code>sout-standard-phone</code> was deprecated in 3.0.0.

{{Option value=string description=Output method to use for the stream.
}} {{Option value=string description=[[Muxer]] to use for the stream. }}
{{Option value=string description=Destination (URL) to use for the
stream. Overrides path and bind parameters. }} {{Option value=string
description=Address to bind to (helper setting for dst) address:[[port]]
to bind vlc to listening incoming streams. Helper setting for dst,
<code>dst{{=}}bind+'/'+path</code>. dst-parameter overrides this. }}
{{Option value=string description=Filename for stream. Helper setting
for dst, <code>dst{{=}}bind+'/'+path</code>. dst-parameter overrides
this. }} {{Option value=boolean description=Announce this session with
[[SAP]]. }} {{Option value=string description=This is the name of the
session that will be announced in the [[SDP]] (Session Descriptor). }}
{{Option value=string description=This allows you to give a short
description with details about the stream, that will be announced in the
SDP (Session Descriptor). }} {{Option value=string description=This
allows you to give a URL with more details about the stream (often the
website of the streaming organization), that will be announced in the
SDP (Session Descriptor). }} {{Option value=string description=This
allows you to give a contact mail address for the stream, that will be
announced in the SDP (Session Descriptor). }}

== Source code == \* {{VLCSourceFile|modules/stream_out/standard.c}}

{{Documentation footer}}
