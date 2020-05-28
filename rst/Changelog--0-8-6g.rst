= Changes between 0.8.6f and 0.8.6g =

== Security updates == \* Removed VLC variable settings from Mozilla and
ActiveX ({{CVE0804}}) \* Removed loading plugins from the current
directory ({{CVE0805}}) \* Updated libpng on Windows and Mac OS X
({{CVE2008-2109}}) \* Fixed libvorbis vulnerabilities ({{CVE2008-1420}},
{{CVE|2008-1423}}) \* Fixed speex insufficient boundary check
(CVE-2008-1686, oCERT-2008-004)

== Various bugfixes == \* Fixed various memory leaks, improving
stability when running as a server \* Fixed compilation with recent
versions of [[FFmpeg]] \* Correctly parses SAP announcements from
[[MPEG]]-TS \* Fixed AAC resampling \* The Fullscreen Controller appears
correctly on [[Mac OS X]], if the 'Always-on-top' video option was
selected.

[[Category:Changelog]]
