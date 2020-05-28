{{See alsoOutreachy May 2016}} This wiki page covers the work of the
[[VideoLAN]] project as a mentoring organization for
[http://gnome.org/opw/ Outreach Program for Women], in order to improve
{{VLC}}.

=== VLC media player ===

{{VLC}} is a cross-platform multimedia player, encoder and streamer
application. It is one of the most successful
[http://www.videolan.org/videolan/ open-source projects without any
professional structure] underneath.

{{VLC}} is downloaded at an approximate monthly rate of 40 millions from
the main website and that's not including third-party distributions
(like Linux, BSD, Android or iOS)!

You can find more information on
[http://en.wikipedia.org/wiki/VLC_media_player VLC on Wikipedia] or on
this [[Main Page|wiki]].

=== Outreach Program for Women ===

If selected and developed, OPW projects for VLC will be included in
later releases.

All projects are covered by the GPL (v2+) or LGPL (v2.1+) licenses
depending on the module.

=== VLC Ideas categories ===

''''' You should really read this'''''

This page is split in three lists of ideas:

#The ''main ideas'' are what seem to be ''key projects'' for VLC and
should be more ''thrilling'' than the other ones; we have assigned a
potential mentor to each of these. #The other ideas are less detailed
but could be good ideas too. #[[Mini Projects]] are short-span projects
which can be given as Qualification tasks or extended to be a full
project.

'''Original good ideas will be valued'''. We don't want to impose
anything. This is Free and Open Source software.

If you don't want to apply for OPW but want other ideas to develop on,
check the [[Mini Projects]] page!

And on the IRC channel ''#videolan'' on the ''Freenode Network'', you
can have even more ideas.

== Getting started ==

=== Compile VLC === This may sound trivial, but it's harder than many
expect. VLC's compilation chain is different for every operating system.
It doesn't really use the default toolchains on Windows or OS X, but a
simple \*nix like ./configure && make doesn't really do the trick
either. We have plenty of information available on this wiki and we will
happily provide help on our IRC channel.

=== Provide a small patch === To demonstrate your skills, share a small
patch with us. This will let you become familiar with [[Git]], in case
you don't know it already and our process on [[Sending Patches
VLC|merging patches]].

=== Let's get in touch === We have 3 major communication channels at
VideoLAN. Our [https://mailman.videolan.org/mailman/listinfo
mailing-lists] to discuss patches and further development related
topics. Furthermore, we have our [http://forum.videolan.org web forums]
for end-user support. This means 2 things: 1) people using VLC media
player on any operating system 2) people using libvlc or the VLC web
plugin in their own applications or installations. Finally, there is our
IRC channel ''#videolan'' on the ''Freenode'' network. It's open to any
kind of discussion. Usage issues, questions how to compile VLC, getting
to know the fellow developers, etc.

== Key ideas for VLC ==

=== CC EIA-708 Closed Caption support === Following up with the recent
developments in the US, we need full support for
[http://en.wikipedia.org/wiki/CEA-708 CEA-708].

We will extend our [http://www.youtube.com/watch?v=1WhMEWIb2S4 support
for EIA-608 in VLC 2.1], so a base is laid, which needs to be expanded
and improved.

Requires good C experience.

''Proposed mentor: [[User:J-b|jb]]''

=== Timed Text TTML support === Based on the W3C specification, we need
support for [http://www.w3.org/TR/ttaf1-dfxp/ Timed Text Markup
Language] to display widely formatted text in time with video or / and
audio. If time allows, this project should be expanded to add support
for SMPTE-TT's additional elements.

Requires good C experience and a feeling for web technologies.

''Proposed mentor: [[User:J-b|jb]]''

=== Chrome OS' NaCl support for VLC's core === We want to add support
for Google's Chrome OS. As a base, libvlccore, VLC's cross-platform
compatibility core needs to be adapted to add support for Chrome OS'
NaCl runtime environment. A base was laid internally last fall, but it
is far from being complete. As time allows, this project should be
expanded to add video and audio output modules for this platform as well
as a basic, HTML-driven UI to test.

Requires strong C knowledge, good networking knowledge and a basic
understanding of Native Client applications on Chrome OS.

''Proposed Mentor: [[User:Fkuehne|feepk]]''

=== UPNP DLNA Server and Client ===

Test and fix service discovery module for UPNP/DLNA shares done by
software (mediatomb, xbmc, etc) and hardware implementations.

Provide DLNA plugin for DLNA server compliant with opensource (xbmc,
djmount, etc) and proprietary (PS3, xbox360, etc) DLNA clients. Some of
the work is already done by previous SoC students.

The plugin must be smart enough to provide "presets" for known DLNA
media clients with limited features (PS3 or XBOX360 for starters) which
require additional quirks or hacks or items to be transcoded or
streamed.

Requires some VLC knowledge as the project will involve using Media
Library and transcoding with VLC API.

''Proposed mentors: thresh, mirsal''

=== Assembly optimizations in VLC ===

If you are fond of writing ASM and you are fluent in MMX/SSE2/SSE4,
there are many interesting things in VLC to speed up.

-  Profiling VLC
-  video filters ASM speedups (see modules/video_filter/blend.c)
-  audio filters ASM speedups (see modules/audio_filter/equalizer.c)
-  Porting other ASM video filters to VLC.

This project needs some good ASM knowledge and good C experience.

\*Stuff to read: http://www.agner.org/optimize/

''Proposed mentor: [[User:J-b|jb]], flx42''

=== Advanced Audio Filters ===

We are looking for a skilled '''audiophile''' that knows a lot about
audio theory and practice to work on new audio filters.

Notably: \* SRS WoW like or other 3D effects; \* channels mixing,
notably upmixing, like Prologic-II; \* tracks mixing, and transitions;
\* scriptable new audio filters in lua and enable users to create
whatever audio filtering function they want in a Lua script; \* LADSPA
or other libraries integration.

This project needs some good audio knowledge and good C experience.

''Qualification task'': port any audio filter from MPlayer

''Proposed mentor: [[User:Geal|geal]]''

=== VLC Test Suite ===

This project aims at making automatic tests to improve VLC quality.

*Write a series of tests for vlc-internal*\ Integrate a framework for
automated plugins testing with the automake build system *Automate the
different codec playback/mux/etc tests*\ Automate the subtitles tests
\*Write tests for the different bindings: Mac OS X Framework/Python
Bindings... etc.

This project is a code project, require good knowledge of C

''Proposed mentor: Rémi''

=== VLC Personal Cloud Project 2.0 ===

The personal cloud project is a simple project to allow people to play
their media files anywhere in the world.

Through the http interface of VLC, a user can:

*list the medias from the Media Library,*\ play those medias, *those
medias get transcoded and streamed in:FlashSilverlightiPhone
formatAndroid formathtml5*\ \*A VLC webplugin

A good example of the aim is http://www.vodobox.c.la/

This project has to work on the configuration and NAT traversal.

This projects needs knowledge in HTML and JS; it might require C coding.

''Proposed mentor: [[User:J-b|jb]]''

=== Playlist improvements ===

We need to reinforce the media library capabilities and its integration
with external metadata sources, notably for TV shows.

''Proposed mentor: ??''

=== AirPlay streaming ===

We need to be able to stream everything to your Google TV, Apple TV or
raspberrypi powered shairport service. Airport is an non-open protocol
that allows wireless streaming of audio, video, multimedia to supported
devices.

The tasks would consist of: \* Understanding how AirPlay works, try with
any device if available. \* Configure a test setup using raspberrypi or
your own computer or any TV device if available, play with couple of
available players who support AirPlay. This is just to get a feel of
what it is you will be trying to implement for vlc-android. \* Study
couple of opensource implementations like shairport \* Run/test/deploy
VLC on simulator or android device \* Implement an AirPlay aout that
would stream audio to your AirPlay supported device (shairport with
rpi/computer or Apple TV or Google TV) \* Test with couple of android
devices if available, ask mentors and community to test, report bugs,
suggestions \* Study how video works, vout for vlc works, if have time
implement video streaming as well.

''Proposed mentor: bhaisaab/rohityadav''

=== VLC Sync Play across devices === By leveraging zeroconf and rtsp
make possible to decode in sync in multiple devices a video stored in
one. Tasks: \* Implement a simple protocol for discovery and announce \*
Implement the discovery system \* At least one of the following \*\*
Provide a UI for Qt (Windows / Linux) \*\* Provide a UI for Android \*\*
Provide a UI for OS X ''Proposed mentor: lu_zero''

=== Native Emotion integration === Emotion is the Evas multimedia
widget. It currently uses a number of backends and has a partial
integration with VLC. Tasks: \* Improve the integration to be on par
with the gstreamer one \* Write an example player using EmotionVLC
''Proposed mentor: lu_zero''

=== XML fast and small implementation ===

The goal of this project is to write a new XML backend, based on a
smaller library than the full libxml2. Speed would be nice, but code
size matters here. Beware: we need to have a stream-XML based API, not a
DOM one.

This project requires good knowledge of C.

''Proposed mentor: [[User:etix|etix]]''

=== Port VLC's NPAPI web plugin to PPAPI === We need to support the
PPAPI interfaces this summer to keep playback support within Google
Chrome, since they will drop for the existing NPAPI architecture.

Requires good C or/and C++ knowledge and a basic understanding of web
browser internals. The ability to test on more than one platform would
be a very strong plus.

''Proposed Mentor: [[User:Fkuehne|feepk]]''

== Other Ideas for VLC ==

=== WTV support === Wtv format support ''Proposed mentor: ???''

=== DVD audio support === Very difficult project for Audio fans
''Proposed mentor: [[User:J-b|jb]]''

=== Device synchronisation=== Sync your mp3 player with the media
library ''Proposed mentor: ???''

=== HD DVD support === Very difficult project for someone having the
right hardware ''Proposed mentor: [[User:J-b|jb]]''

=== Multi-Angle DVD support === We need multi-angle DVD support
''Proposed mentor: Meuuh''

=== VLM UI for the Mac OS X interface === Implement an easy-to-use, yet
customizable and complete UI for the VideoLAN Media Manager, which
allows VLC to stream multiple unicast, multicast and Video-on-Demand
streams within a single instance. You will need a Mac running OS X 10.6
or later and Cocoa programming experience. A basic understanding of
media streams is definitely preferable. Note that this task is too small
for an entire summer and should be combined with another topic.
''Proposed mentor: [[User:Fkuehne|feepk]]''

=== Improve messages display === When VLC has a problem opening or
playing files it shows a messages window on top of the player with the
error. This can be annoying if the screen is being controlled remotely
as the user has to manually dismiss the message. There are various ways
this could be improved: #Update UI so that messages window will
auto-dismiss after x seconds unless it is clicked on (this could be
optional behaviour). Clicking on the window would cancel the countdown.
If the window was selected from the menu, it would not auto-dismiss.
#Mac OS: Display messages using notification system (if available).
Clicking on the notification would open the messages window. Suggested
by : Confused Vorlon. ''Proposed mentor: [[User:Fkuehne|feepk]]''

=== BD-J / BD-Live VLC integration ===

This is a project to work on Bly-Ray menus and interactivity
improvements.

This project requires a correct C and Java knowledge

Proposed mentor: hpi and [[User:J-b|j-b]].

=== Support for HTTP Dynamic Streaming (F4M) ===

We need to be able to read Flash Media Manifests (also known as F4M)
according to this spec.

Proposed mentor: fyhuel

=== Porting Audio Filters ===

We are looking for a skilled '''audiophile''' that knows a lot about
audio theory and practice: \* to port open source algorithm for audio
filters to VLC.

This project needs some good audio knowledge and good C experience.

''Proposed mentor: [[User:Geal|geal]]''

[[Category:Mentorings]]
