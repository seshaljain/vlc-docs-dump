== Introduction ==

{{VLC}} is a very popular, but quite large and complex piece of
software.<br /> It uses a large number of [[Contrib Status|3rd party
libraries]].

VLC development is [[open source]], and then a large community of
developers worldwide contribute to it.<br /> However, entering a project
such as VLC can be long and complex for new developers.

This '''guide''' seeks to help understanding the VLC code base and VLC
internals to quickly get up to speed.<br /> ''NB: this guide is
'''not''' about [[compiling]] VLC.''

A very good introduction to VLC can also be found on (an archived copy
of the site)
[//web.archive.org/web/20141204234622/http://www.enjoythearchitecture.com/vlc-architecture.html
enjoythearchitecture].

== The layers of VLC and libVLC ==

=== VLC's Core / libVLCcore ===

The most important (and probably most complex) part of VLC is the core,
located under {{VLCSourceFolder|src}} in the repository.

*[[{{#rel2abs:/Core}}|Introduction to the core]]*\ \* This is a
'''MUST-READ''' for developers. *[[Documentation:VLC Modules Loading|VLC
modules loading]]*\ \* How the numerous VLC modules work and are loaded.
*[[{{#rel2abs:/Input}}|Input]]*\ \* How the main input chain works
(slightly outdated) *[[{{#rel2abs:/Object Management}}|VLC Object
Management]]*\ [[{{#rel2abs:/Variables}}VLM Internals]]

=== Plugins / Modules ===

[[{{#rel2abs:/How To Write a Module}}|How to write a VLC module]].

==== Input ==== *[[{{#rel2abs:/Access}}|Access]]*\ \* An access module
provides a byte stream from a location string [[MRL]], like support for
files, HTTP streams, webcams... *[[{{#rel2abs:/Demux}}|Demuxer]]*\ \* A
demux module parses a byte stream and splits it into [[elementary
stream]]s (tracks). *[[{{#rel2abs:/Access Demux}}|Access-Demuxer]]*\ \*
An access_demux module combines the functionality of access and demux
(and bypass any stream filters), splitting elementary streams directly
from a location string. It's used where the bytestream abstraction is
inadequate. *[[{{#rel2abs:/Stream Filters}}|Stream Filters]]*\ \* A
stream filter module converts a byte stream into another byte stream. It
could be used for file or byte stream decryption, as it is already used
for decompression (gzip, Bzip2, XZ) and multi-part files.
*[[{{#rel2abs:/Decoder}}|Decoder]]*\ \* A decoder takes an elementary
stream and convert into raw video, audio or text data, reading for
output.

==== Audio ====

*[[{{#rel2abs:/Audio Filters}}|Audio Filters]]*\ [[{{#rel2abs:/Audio
Output}}|Audio Output]]

==== Video ====

*[[{{#rel2abs:/Video Filters}}|Video Filters]][[{{#rel2abs:/Video
Filters/Deinterlace}}|Deinterlace]]*\ [[{{#rel2abs:/Video Output}}|Video
Output]]

==== Interfaces ==== \*[[{{#rel2abs:/Interfaces}}|Interfaces]]

==== Modules types not documented (yet) ==== ===== Misc =====
*[[{{#rel2abs:/Visualization}}|Visualization]]*\ [[{{#rel2abs:/Packetizers}}|Packetizers]]

===== Streaming output =====
*[[{{#rel2abs:/Encoder}}|Encoder]]*\ [[{{#rel2abs:/Mux}}Access Output]]

=== libVLC and bindings ===

*Using [[{{#rel2abs:/libvlc}}|libvlc]]*\ bindings

== VLC source code overview ==

*[[{{#rel2abs:/VLC source tree}}]]*\ [[{{#rel2abs:/Modules source
tree}}]] *[[{{#rel2abs:/Preferences}}|VLC
Preferences]]*\ [[{{#rel2abs:/Playlist}}|VLC Playlist and Media
Library]]

== Coding for VLC ==

*[[Patch]]ing ([[Sending Patches|sending]])*\ [[Code Conventions]]
*[[Code Signing]]*\ [[{{#rel2abs:/How To Write a Module}}|Adding a
module]]
*[[Documentation:Unicode]]*\ [https://www.videolan.org/developers/vlc/doc/doxygen/html/index.html
Doxygen Documentation] <span
class="plainlinks">([\ https://www.videolan.org/developers/vlc/doc/doxygen/html/pages.html
pages] &bull;
[https://www.videolan.org/developers/vlc/doc/doxygen/html/modules.html
modules] &bull;
[https://www.videolan.org/developers/vlc/doc/doxygen/html/annotated.html
data structures] &bull;
[https://www.videolan.org/developers/vlc/doc/doxygen/html/files.html
files] &bull;
[https://www.videolan.org/developers/vlc/doc/doxygen/html/group__vlc.html
API])</span> *[[C Types]]*\ [[Strings]]

== User Experience ==

\*[[Playback States]]

== Testing ==

\*[[Test Suite]]

== Mozilla plugins ==

-  [[Plugins/Mozilla|Plugins in Mozilla]]

{{Hacker_Guide}}
