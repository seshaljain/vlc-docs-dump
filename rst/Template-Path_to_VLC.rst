<includeonly><!---->{{#ifeq:{{{diry<!-- -->windows =
{{#ifeq:{{{qn"%PROGRAMFILES%VideoLANVLC"}}<!-- -->linux = <!-- -->}}<!--
-->windows = "%PROGRAMFILES%VideoLANVLCvlc.exe"<!-- -->linux = vlc<!--
-->}}<!---->}}</includeonly><noinclude>

== Usage == A template for default {{VLC}} locations on desktop
computers by [[operating system]].

Parameters: \* (unnamed) required. One of <code>windows</code>,
<code>mac</code> or <code>linux</code>. No default \*
<code>'''q='''</code> optional (short for ''quotes''). Only checks for
value <code>n</code> (''no''). Default enabled Showcase of various
modes: \*
<code>{{{{PAGENAME}}windows<nowiki>windows<nowiki>q=n}}</nowiki></code>
*: <samp>{{{{PAGENAME}}|windows|dir=y|q=n}}</samp>*
<code>{{{{PAGENAME}}mac<nowiki>linux<nowiki>}}</nowiki></code> *:
<samp>{{{{PAGENAME}}|linux}}</samp>*
<code>{{{{PAGENAME}}dir=y}}</nowiki></code> \*:
<samp>{{{{PAGENAME}}dir=y}}</samp>

== See also == \* {{tlVLC folder}} - simple wrapper template for
directory paths only (no quotes)

[[Category:Templates]] </noinclude>
