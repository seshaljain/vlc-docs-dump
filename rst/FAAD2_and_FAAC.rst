{{Websitehttps://www.audiocoding.com}} {{FOSS}}

'''FAAD2''' or '''Freeware Advanced Audio Decoder''' is a project for
''decoding'' [[AAC]] in [[MPEG-4]] and [[MPEG-2]].

'''FAAC''' or '''Freeware Advanced Audio Codec''' is a project for
''encoding'' AAC in MPEG-4 and MPEG-2.

Both projects are released under the GPLv2, making them
[[open-source]].<span
id="Note-backlink"></span><sup>[[#Note|&dagger;]]</sup> SourceForge
hosts [[Git]] (source code) for both components, and there are
respective GitHub mirrors. SourceForge also hosts binaries (executable
code) for Windows (<code>*.exe</code>) and Linux
(<code>*.tar.gz</code>).

{{VLC}} uses the FAAD2 [[library]], libfaad, in the
{{VLCSourceFilel=faad.c}} module; but VLC no longer uses the FAAC
library, libfaac.

== Note == <big><sup>[[#Note-backlink|&dagger;]]</sup></big> When
audiocoding.com says it supports DRM, it does not mean ''[[Digital
Restrictions Management]]'' but rather ''Digital Radio Mondiale''.
Supporting Digital Restrictions Management might (arguably) cast doubt
on whether the project is truly open-source.

== Links == \* [https://www.audiocoding.com/ Audiocoding.com] \*\*
[https://www.audiocoding.com/faad2.html FAAD2 page] \*\*
[https://www.audiocoding.com/faac.html FAAC page] \*
[https://sourceforge.net/projects/faac/ SourceForge - FAAC project] \*\*
[https://sourceforge.net/p/faac/faad2/ci/master/tree/ FAAD2 Git]
<small>([https://github.com/knik0/faad2 GitHub mirror])</small> \*\*
[https://sourceforge.net/p/faac/faac/ci/master/tree/ FAAC Git]
<small>([https://github.com/knik0/faac GitHub mirror])</small> \*
[https://git.videolan.org/?p=vlc.git&a=search&h=HEAD&st=commit&s=faac
Git commit search for faac in VLC] \*\* {{Commitdiffl=contribs: disable
libfaac on Darwin (as part of ffmpeg) as it considered nonfree now}}
\*\* {{Commitdiffl=Contrib: remove faac from ffmpeg. Without this,
ffmpeg refuses to build due to licensing problems.}} \*\*
{{Commitdiffl=Faac is NOT compatible with VLC. Too bad for your AAC
encoding, but, well.}}

[[Category:Third parties]]
