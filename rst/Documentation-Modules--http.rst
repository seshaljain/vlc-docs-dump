The <code>--http-caching</code> option was removed prior to VLC 2.0.0
with this commitdiff: {{Commitdiffl=Unify
(ACCESS{{!}}DEMUX)_GET_PTS_DELAY}}

The option <code>--http-proxy</code> was removed from the 3.0.x and
4.0.0-dev branches with this commitdiff: {{Commitdiffl=HTTP win32: use
http-proxy options to setup the proxy}} with summary ''Because
win32/netconf is not ready''.

The option <code>--http-user-agent</code> changed in VLC 1.1.1 (changelog):
   [[libvlc]]_set_user_agent() configures the "[[wikipedia:User
   agent|user agent]]" strings used for some protocols (HTTP,
   PulseAudio...). This replaces the --http-user-agent and the former
   --user-agent libvlc_new() parameters.

== HTTP == {{Moduletype=Accessdescription=[[HTTP]]
inputsc2=unsvsc4=icyx}}

HTTP was first supported ''before'' 0.5.0 (probably from the beginning).

As of VLC 0.9.0 this module accepts gzip compressed data and Digest
Access Authentication.

=== Options === {{Option default=disabled \|description=Automatically
try to reconnect in case of a sudden disconnect }}

{{Clear}} == HTTPS == {{Moduletype=Accessdescription=[[HTTPS]]
input|sc=https}}

HTTPS was first supported in 0.8.1 (for {{docmod|http_intf}}). This
particular sub-module was introduced in 3.0.0 for HTTP 2.0 support.

=== Options === {{Option value=boolean description=Forward cookies
across HTTP redirections }} {{Option value=string description=Provide
the referral URL, i.e. HTTP "[[wikipedia:HTTP referersic]]''&#x5D; }}
{{Option value=string description=Override the name and version of the
application as provided to the HTTP server, i.e. the HTTP
"[[wikipedia:User agentname=http-continuous default=disabled
\|description=Keep reading a resource that keeps being updated (for
example a JPEG file) }}

== Source code == \* {{VLCSourceFilemodules/access/http/access.c}} (file
- HTTPS sub-module) \* {{VLCSourceFolder|modules/access/http}} (folder)

{{Stub}}

{{Documentation footer}}
