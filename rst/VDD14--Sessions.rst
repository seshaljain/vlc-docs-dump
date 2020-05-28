<noinclude> '''<big>[[{{#rel2abs:..}}|← Back to the VDD14
page]]</big>''' </noinclude>

=== Rooms ===

==== 11th floor ==== \* Ocean's eleven, large room with talks, for ~80
people. \* Kitchen11, coffee, for ~30 people. \* Outdoor deck, beautiful
views. '''Absolutely no smoking!!!!''' Now open

==== 12th floor ==== \* PepperClip, small meeting rooms for ~10 people.
\* FiloFax, small meeting rooms for ~10 people. \* Kitchen12, coffee and
cool layout for ~20 people.

==== 13rd floor ====

-  Kitchen13, coffee and cool layout for ~20 people.
-  Galileo, meeting room, for ~20 people.
-  Docks view, for ~8 people.

=== Etherpad to take Notes === https://beta.etherpad.org/

*Videolan etherpad https://beta.etherpad.org/TdHZGbVbSg* VLC Technical
meeting notes https://beta.etherpad.org/XjEL1HPKek *libav meeting
https://beta.etherpad.org/Libav*\ ffmpeg.
https://beta.etherpad.org/ffmpeg \* VLC for iOS meetup
https://beta.etherpad.org/iOS \* Media Library session notes
https://beta.etherpad.org/W2XfSp8lUD

=== Scheduled VDD sessions ===

==== Saturday, September 20th 2014 ==== {\| class="wikitable" -! 14:00 -
15:00 \| VLC technical discussion \| libav FFmpeg discussion \| \| \|
VLC technical discussion \| libav technical discussion \| FFmpeg
technical discussion \| \| colspan="5" \| Coffee Break Android \| iOS \|
\| Linux \| \| \| WinRT \| \| colspan="5"\| Wrapping up \|}

==== Sunday, September 21th 2014 ==== {\| class="wikitable" -! 11:00 -
12:00 \| Libav 12 and 13 \| Chromecast \| \| daala \| Hacking Libav 12
and 13 continued \| EBU-TT-D \| \| daala continued \| Hacking
colspan="5" \| Lunch + PHOTO Libav whining \| Media library for Mobile
\| broadcasting things \| arm64/AArch64 \| Hacking colspan="5" \| coffee
break Libav infrastructure discussion \| x264 \| testing \| Wayland \|
Hacking colspan="5" \| coffee break road towards HWAccel 2 \| FFmpeg
whining \| opus in mp4/Binary art extension for ogg \| JB's secret
project , in the matrix \| Hacking }

== Proposed VDD sessions ==

=== Saturday === ==== VLC 2.2 and 3.0 ==== What's left to be done for
2.2? What are our goals for 3.0? What's the time frame for the next
major release? How can we avoid to repeat the 2.2 delay?

==== VLC Mobile Remotes ==== There is a major feature missing in VLC's
mobile apps, which is currently provided through third party apps.
Control VLC remotely running on a desktop. What needs to be done both on
client and server-side to provide an advanced and seamless integration
between the platforms?

==== VLC Subpicture Framework improvements for hwaccel rendering ==== As
of today for picture type subpictures (DVB Subtitles, VBI pages, ...) a
software scale step is forced into the pipeline. To make better use of
hardware being able to render scaled overlays this shall be omitted. But
it seems some significant changes in the VLC core are required to
support this in a common way, which some brainstorming on would be
required.

==== Android ====

==== iOS ====

==== WinRT ====

==== libav/FFmpeg discussion ==== Better understanding leads to better
cooperation.

=== Sunday ===

==== Libav 12 and 13 ==== Roadmap, [http://wiki.libav.org/Blueprint
Blueprints] and so on.

==== Libav whining ==== You have complaints: do voice them! (we will
listen and will address them)

==== Libav infrastructure discussion ==== Bugzilla customizations,
gitlab, gogs, plaid, and other tools to make our life easier by making
some admin life miserable.

==== Road towards HWAccel 2 ==== During this year we moved two steps
towards version [[https://wiki.libav.org/Blueprint/HWAccel2 2]]:

-  1.2 -> default context allocators
-  1.3 -> bitstream-oriented hwaccel support

During this session we will discuss about how to provide an uniform
structure to avoid even more boilerplate code and still allow full
control to the people needing it.

==== ChromeCast ==== How do we achieve VLC using Chromecast?

==== Media Library ==== Current state and conception of needed
functionality for a cross-platform library to collect meta data,
thumbnails and so on for use within media handling applications based on
libvlc. Written in C++.

==== EBU-TT-D ==== integration in VLC and/or ffmpeg ?

==== x264 meeting ====

==== Opus in MP4 ==== We should sit down and design this mapping.

==== Binary Album Art extensions for Ogg ==== We've had a proposal to
include binary (not base64-encoded) album art for Ogg in the context of
Ogg Opus:
<http://www.ietf.org/mail-archive/web/codec/current/msg03061.html>. This
session would determine if there is interest from players in supporting
such an extension and working on the design.

==== Testing ==== Seems like everybody is doing the same very flaky or
very manual thing when testing video processing and player software. Can
we do better? :like a fate suite of tests for players? Maybe with an
scriptable mouse click? Assuming your player can be launched in a set
coordinates.

==== Broadcasting things ==== An attempt to justify what broadcasters
are doing.

==== arm64 / AArch64 ==== CPU specific optimizions for iOS devices,
upcoming android devices, arm based servers

==== The bare basics of special relativity ==== An brief introduction to
the basic concepts and consequences of special relativity.

==== Chocolate ====

[[VDD14/Chocolate|Chocolate orders delivery]]

==== Daala ==== Open to anyone curious about Daala, and if you want to
win a T-shirt we'll help you write your first patches! See also
https://wiki.xiph.org/Daala_Quickstart

==== Wayland ==== Principles, challenges, progress and way forward with
multimedia on Wayland

[[Category:VDD]]
