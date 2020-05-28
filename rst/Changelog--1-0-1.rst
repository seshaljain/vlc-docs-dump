= Changes between 1.0.0 and 1.0.1 =

== Demuxers == \* Fix wmv/asf issues that caused audio to drop \*
Various fixes for [[AC3|ac3]], [[mp3]], [[dts]] and stability for
[[wav]] format \* Fix seek in RTSP in conformity to
[https://tools.ietf.org/html/rfc2326 RFC 2326] \* Fix Dailymotion access
script \* Fix crashes in [[xspf]] files handler \* Fix seeking and
timing issues in some [[flv]] files on Windows version

== Access == \* Add extra caching for files on network shares \* Prevent
integer underflow in Real pseudo-RTSP module, discovered by tixxDZ,
DZCORE Labs, Algeria

== Decoders == \* Fix seeking in [[MPEG-2 video|mpeg2 video]] files \*
Improve [[SSA]] subtitles rendering \* Update most codecs for the
Windows and Mac version

== Muxers == \* Fix sound recording of .flv files with mp3 audio

== Qt Interface == \* Possibility to change the opacity level of the
Fullscreen controller \* Fix various crashes and VIDEO_TS folders
opening

== Mac OS X Interface == \* Added options to disable support for Apple
Remote and Media Keys \* Fixed options for Volume, Last.fm password and
Subtitle Encoding \* Fixed redraw issues when autosizing the video
window \* Preferences panel now includes help through tool-tips \* More
reliable Information and Messages panels \* Fix various crashes

== Windows port == \* The ZVBI module is now available for Windows, for
complete [[teletext]] support

== Translation updates == \* Brazillian, French, German, Korean,
Norwegian Nynorsk, Lithuanian

[[Category:Changelog]]
