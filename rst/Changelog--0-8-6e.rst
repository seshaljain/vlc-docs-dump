<!--{{BasedOnRevfile=branches/0.8.6-bugfix/NEWS}}-->

= Changes between 0.8.6d and 0.8.6e =

== Various bugfixes == \* Resume playback for viewing content over
[[Documentation:Modules/ftpX11]]

== Security updates == \* [[Subtitle]] demuxers overflow ({{CVEHTTP
listener]] format string injection ({{CVESDL_image]] library
({{CVE2008-0225}}, {{CVE2008-0296}}, {{VideoLAN-SA0802}})

== Audio filter == \* Fixed [[DTS]] to S/PDIF converter

== Audio output == \* Fixed 5.1 audio on ALSA

== Access == \* Fixed some [[RTSP]] hanging and user/password passing
through [[RTSP]] URLs

== Stream output == \* Fixed waiting for SPS/PPS problem in [[H.264]]
packetizer

== Encoders == \* Improved compatibility for creating [[H.264]] video
files playable on iPhones \* Improved detection of optimal amount of
threads for multi-threaded [[H.264]] encoding on multi-cpu systems \*\*
Note that this is used when [[transcode]] threads is set to 0 (default)
\*\* Not supported on Windows (multiple threads require manual
configuration)

== Mac OS X Interface & Port == \* Restored compatibility with Mac OS X
10.3.9 \* Corrected behavior of the [[Preferences]] panel \* VLC no
longer crashes on quit while playing

== Localization == \* Updated Romanian and Polish translations

[[Category:Changelog]]
