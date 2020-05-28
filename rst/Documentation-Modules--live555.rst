{{Moduletype=Access demuxsc=live|sc2=livedotcom}}

The <code>--rtsp-caching</code> option was removed prior to VLC 2.0.0
with this commitdiff: {{Commitdiffl=Unify
(ACCESS{{!}}DEMUX)_GET_PTS_DELAY}}

== Options == None. {{Clear}}

== Submodule == {{Moduletype=Accesssc=rtspsc3=live|sc4=livedotcom}}

=== Options === {{Option value=boolean description=Use RTP over RTSP
([[TCP]]) }} {{Option value=integer description=[[Port]] to use for the
RTP source of the session }} {{Option value=boolean description=Force
[[multicast]] RTP via RTSP }} {{Option value=boolean description=Tunnel
RTSP and RTP over [[HTTP]] }} {{Option value=integer description=Port to
use for tunneling the RTSP/RTP over HTTP }} {{Option value=boolean
description=Kasenna servers use an old and nonstandard dialect of RTSP.
With this parameter VLC will try this dialect, but then it cannot
connect to normal RTSP servers }} {{Option value=boolean
description=WMServer uses a nonstandard dialect of RTSP. Selecting this
parameter will tell VLC to assume some options contrary to
[https://tools.ietf.org/html/rfc2326 RFC 2326] guidelines }} {{Option
value=string description=Sets the username for the connection, if no
username or password are set in the url }} {{Option value=password
description=Sets the password for the connection, if no username or
password are set in the url }} {{Option value=integer description=RTSP
start frame buffer size of the video track, can be increased in case of
broken pictures due to too small buffer }}

== Source code == \* {{VLCSourceFile|modules/access/live555.cpp}}

{{Documentation footer}}
