{{See alsoOutreachy Summer 2015}} This wiki page covers the work of the
[[VideoLAN]] project as a mentoring organization for
[https://wiki.gnome.org/Outreachy Outreachy the successor of the
Outreach Program for Women], in order to improve {{VLC}} and [[VLMC]].

To find generic information about the Outreachy program, please see the
'''[https://wiki.gnome.org/Outreachy official website]'''.

'''Eligibility''': The program is open internationally to women (cis and
trans), trans men, and genderqueer people in addition to people of color
from groups underrepresented in technology in the United States.

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

=== VideoLAN Movie Creator === [[VLMC]] is a cross-platform non-linear
video editing software based on VLC technology. It was started as a
final year student project at the French IT school
[http://www.epitech.eu EPITECH].

[[VLMC]] currently awaits a transition to the current libvlc API and
it's actual 1.0 release!

=== Outreachy May 2016 ===

If selected and developed, Outreachy projects for VLC or VLMC will be
included in later releases.

All projects are covered by the GPL (v2+) or LGPL (v2.1+) licenses
depending on the module.

=== VLC and VLMC Idea categories ===

''''' You should really read this'''''

This page is split in three lists of ideas:

#The ''main ideas'' are what seem to be ''key projects'' for VLC or VLMC
and should be more ''thrilling'' than the other ones; we have assigned a
potential mentor to each of these. #The other ideas are less detailed
but could be good ideas too. #[[Mini Projects]] are short-span projects
which can be given as Qualification tasks or extended to be a full
project.

'''Original good ideas will be valued'''. We don't want to impose
anything. This is Free and Open Source software.

If you don't want to apply for Outreachy but want other ideas to develop
on, check the [[Mini Projects]] page!

And on the IRC channel ''#videolan'' on the ''Freenode Network'', you
can have even more ideas.

== Getting started ==

=== Compile VLC or VLMC === This may sound trivial, but it's harder than
many expect. VLC's and VLMC's compilation chains are different for every
operating system. They don't really use the default toolchains on
Windows or OS X, but a simple \*nix like ./configure && make doesn't
really do the trick either. We have plenty of information available on
this wiki and we will happily provide help on our IRC channel.

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
kind of discussion. Usage issues, questions how to compile VLC or VLMC,
getting to know the fellow developers, etc.

=== How to apply? === The application process for the May 2016 rout will
open on February 16, 2015 and '''application deadline''' is '''March
22''' (no exceptions!). Please submit your application on the
[https://outreachy.gnome.org official program website]. Previously,
please check the [https://wiki.gnome.org/Outreachy#Eligibility
eligibility requirements] :-)

== Key ideas for VLC ==

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

''Proposed mentor: ivoire''

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

''Proposed mentor: ??''

=== VLC Sync Play across devices === By leveraging zeroconf and rtsp
make possible to decode in sync in multiple devices a video stored in
one. Tasks: \* Implement a simple protocol for discovery and announce \*
Implement the discovery system \* At least one of the following \*\*
Provide a UI for Qt (Windows / Linux) \*\* Provide a UI for Android \*\*
Provide a UI for OS X ''Proposed mentor: lu_zero''

=== Port VLC's NPAPI web plugin to PPAPI === We need to support the
PPAPI interfaces this summer to keep playback support within Google
Chrome, since they dropped the existing NPAPI architecture. A
proof-of-concept was developed already, but needs refactoring, polishing
and testing.

Requires good C or/and C++ knowledge and a basic understanding of web
browser internals. The ability to test on more than one platform would
be a very strong plus.

''Proposed Mentor: [[User:Fkuehne|feepk]]''

=== Add Owncloud, MEGA and Yandex.Disk cloud support to VLC for iOS ===
Following the success of our native integration with Google Drive,
Dropbox, OneDrive and Box, we want to integrate with Owncloud, MEGA and
Yandex.disk, which are the last remaining major cloud services left to
add! :)

Requires good Objective-C and optionally swift knowledge as well as a
basic understanding of cloud services and network programming.
Additionally, requires a Mac running OS X 10.10 or later.

''Proposed Mentor: [[User:Fkuehne|feepk]]''

=== Add proper audio playback UI to VLC for iOS === VLC for iOS is a
recognized and well known video player. Few people know that it is
actually capable of playing music and podcasts, too and there is a
reason for that. The UI is not really suitable for it. Make it so!

Requires good Objective-C and optionally swift knowledge as well as
basic design skills. Additionally, requires a Mac running OS X 10.10 or
later.

''Proposed Mentor: [[User:Fkuehne|feepk]]''

== Other Ideas for VLC ==

=== DVD audio support === Very difficult project for Audio fans
''Proposed mentor: [[User:J-b|jb]]''

=== Device synchronisation=== Sync your mp3 player with the media
library ''Proposed mentor: ???''

=== HD DVD support === Very difficult project for someone having the
right hardware ''Proposed mentor: [[User:J-b|jb]]''

=== Multi-Angle DVD support === We need multi-angle DVD support
''Proposed mentor: Meuuh''

== Key ideas for VLMC ==

=== Implement a real Audio/Video sync ===

So far, the lip-syncing strategy used by VLMC is pretty much "hope it
works".

As you would think, this quite often leads to desync, and thus makes
VLMC unusable.

We need to come up with a real synchronization strategy, quite likely
based on an abstract clock & PTS

''Proposed mentor: chouquette''

=== Plug-in new libvlcpp & medialibrary ===

VLMC uses a from-sratch C++ binding to libvlc, which is stuck a few
years in the past. Meanwhile, a new binding got written
(https://code.videolan.org/videolan/libvlcpp/tree/master), and needs to
be plugged in.

We also started working on a cross-platform media library, to replace
the low-featured one, present in VLMC.

This media library will handle discovering media for the used, instead
of having to manually importing every single file. This should also
allow us to kill some of the "Backend" code, as a fair share of it is
designed to create thumbnails. This is now done by the medialibrary, and
can go away from the VLMC source code.

This probably requires a good C++ knowledge, as both libvlcpp &
medialibrary make a heavy use of C++11 & templates meta-programming.

''Proposed mentor: chouquette''

=== Import/Save to/from cloud services ===

It would be a great addition to VLMC to be able to import some medias
from a cloud service, and being able to export the result to another.

Since there are so many different cloud providers, we would like to have
a "libcloudstorage" that would handle all the boilerplate out of VLMC's
source code.

This lib can then easily be used to allow the user to use multiple
service.

The cherry on the top would be to integrate this lib cloud storage into
the medialibrary project, in order to automatically discover & analyze
media stored on the cloud.

''Proposed mentor: jb, chouquette''

=== Remote UI ===

We would like to have a way to use VLMC from a web browser. You can
easily imagine having a nice, shiny & simple UI for minimal movie
edition, which would go hand in hand with the cloud storage feature.

This task aims toward the uncoupling of the rendering backend & UI, as
the renderer will run server side, while the UI runs on the client side.

The idea is to be able to have a UI interacting with the renderer
without having to be in the same process, or even machine.

''Proposed mentor: jb, chouquette, fkuehne''

=== Unit tests ===

VLMC is *not* tested.

Well, it is, but manually, which is not good enough. There are many race
conditions, crash, deadlocks yet to be discovered.

The UI also has some fairly funky behavior when being stressed out, and
that needs to be tested as well.

This task is about writing a unit test suite for both the renderers &
the UI. Most likely, this will mean adding some mocking machinery, and
therefor hiding all our classes behind an API.

This task is definitely a requirement before we are able to clean &
modernize the code base!

''Proposed mentor: chouquette''

[[Category:Mentorings]]
