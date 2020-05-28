Here is a list of the accepted projects for the [[SoC 2007|Google Summer
of Code 2007]].

== List of current projects ==

=== Advanced subtitle support for VLC ===

-  '''Project page: [[SoC 2007 Project Advanced Subtitle
   Support|Advanced Subtitle Support]]'''
-  '''Student''': Philip David Lamparter
-  '''Mentor''': Sigmund Augdal
-  '''Abstract''':

: Nowadays, with international shipping and multi-cultural nations, an
increasing number of people prefers to watch videos with the original
audio track. However, since most people wouldn't be fluent with all the
source languages they come across, subtitles are in widespread use to
overcome this.

: The set of subtitling formats supported by the VLC player currently
covers simple formats. One of the rather widely used formats, SSA/ASS,
is not properly supported though - probably due to its capabilities for
advanced styling, animation effects, and even drawing commands.

My goal for this Summer of Code project is to provide VLC with rendering capabilities for this format. Ultimately, I'm desiring 99% compatibility with what's considered the reference for it
   the Windows renderer "VSFilter".

To achieve this goals, I already started implementing a standalone filter for this purpose, called asa. Therefore, a rough outline of my plans is

: 1. Create bindings between VLC and asa. : 2. Fix the remaining bugs
and missings in asa. : 3. Look for and cover extended usage cases in
both VLC and asa (subtitle picture streaming, drawing mode, OpenType
glyph substitution support)

=== VLC Mac OS X Framework Implementation ===

-  '''Project page: [[SoC 2007 Project Mac OS X Framework|Mac OS X
   Framework]]'''
-  '''Student''': [[User:Pdherbemont|Pierre d'Herbemont]]
-  '''Mentor''': [[User:Fkuehne|Felix Paul Kühne]]
-  '''Abstract''':

Proposition
   Write a Cocoa Mac OS X (and possibly GNUStep) Framework that would
   serve as a foundation to the 2 differents Mac OS X VLC binaries.

: Those binaries are the standard VLC.app executable, and the VLC web
browser plugin.

: This Framework could also be used as a library for other applications
that need a video output.

=== Matroska Muxer for VLC ===

-  '''Project page: [[SoC 2007 Project Matroska Muxer|Matroska
   Muxer]]'''
-  '''Student''': Hugo de Jesús Garza Gómez
-  '''Mentor''': Steve Lhomme
-  '''Abstract''':

: In recent years the digital video industry has seen a boom in the
number of users; thanks originally to the DVD for bring digital video in
mass quantities, but more recently to innovative websites such as
YouTube and peer to peer applications where users can share their
videos. The reason that these applications are successful is because
their users use a standard container for video files which for years has
been the AVI container. However as time went on the AVI container was
outgrown by the rapid pace of change and the needs of the consumer. To
satisfy these needs new containers were created with more features such
as menus, chapters, and multiple audio streams.

: The AVI format was originally created by Microsoft as an extension to
the RIFF format for its video for windows technology thus establishing
it as the standard format for distributing video files. In recent years
newer audio and video codecs have been released which brought to light
many deficiencies in the AVI format. As a solution to this problem the
matroska container was created to be an opensource flexible and
cross-platform Audio/Video container format. In order to play matroska
streams it is necessary to use a media player capable of reproducing
them, such as VLC by the VideLAN project. VLC is a cross-platform media
player, but is unique in that it supports a large number of multimedia
formats without the need for additional codecs. One of the major
strength of VLC is also that it can receive and broadcast videos
streams, which is where Matroska could find a new use.

The proposal for this project is to create a matroska muxer for the VLC media player in C++ using the libmatroska library which would allow the creation of new matroska streams and modification of existing streams. The muxer would support various audio/video codecs and most of the features of the matroska spec
   multiple audio streams and multiple subtitles.

=== RTSP Streaming Server in VLC ===

-  '''Project page: [[SoC 2007 Project RTSP Streaming Server|RTSP
   Streaming Server]]'''
-  '''Student''': Sourav Pal
-  '''Mentor''': [[User:Jpsaman|Jean-Paul Saman]]
-  '''Abstract''':

: The main goal as mentioned in the project listing is to enable VLC
with RTCP features, interleave RTP stream over RTSP when firewall is
encountered, perform rtsp tunneling over http and perform per account
options. If time permits follow-up with a performance evaluation of the
streaming server code and pinpoint bottleneck issues.

=== Fullscreen Controller and Advanced Subtitle Support on VLC media
player ===

-  '''Project page: [[SoC 2007 Project Fullscreen Controller and
   Advanced Subtitle Support|Fullscreen Controller and Advanced Subtitle
   Support]]'''
-  '''Student''': Richard Guo
-  '''Mentor''': [[User:Yoann|Yoann Peronneau]]
-  '''Abstract''':

: VLC is known as a lightweight media player that shines in playing
files regardless of format. However, its UI is underdeveloped in
comparison to competitors. While a revamped UI might not be first and
foremost on the developers' minds, adding a basic control interface in
fullscreen mode would greatly enhance VLC's adoption.

: From a usability standpoint, it is a hassle for users to exit
fullscreen mode just to operate the controls controlling pause, play,
fast forward, and the position of playback. Power users and developers
usually have customized keybindings for use in fullscreen mode, but the
vast majority of users expect a controller in fullscreen mode. Moreover,
it is inconsistent to support fullscreen controls on the Mac OSX version
but not on \*nix or Windows.

The second proposal concerns displaying and rendering subtitles. VLC's current subtitle capabilities is rather rudimentary. Work on this aspect of VLC will consist of three parts
   detection of subtitle streams (either with DVD input on disc or in a
   file in the same directory as the video), automated parsing (must
   handle all formats and errors in syntax), and display (smart
   rendering, advance rendering, positioning, size, shape, font, colour,
   HTML tags, etc.).

=== Audio Extensions for VLC media player ===

-  '''Project page: [[SoC 2007 Project Audio Extensions|Audio
   Extensions]]'''
-  '''Student''': Biodun Osunkunle
-  '''Mentor''': Derk-Jan Hartman
-  '''Abstract''':

: The VLC media player's audio post processing capabilities can be
improved. Currently, preset equalizer values, an option for a graphic
equalizer with the extended GUI, and a headphone virtualization option.

: The goal of this project is to extend these audio capabilities to
include such features as Dolby Prologic 2 like features, (psycho
acoustic audio processing), and other effects such as artificial
reverberation.

=== Overlay Video Filter for VLC ===

-  '''Project page: [[SoC 2007 Project Dynamic Video Overlays|Dynamic
   Video Overlays]]'''
-  '''Student''': [[User:Avacore|Søren Bøg]]
-  '''Mentor''': [[User:Dionoea|Antoine Cellerier]]
-  '''Abstract''':

: The goal for this project to develop a video filter for VLC to allow
third party applications to overlay static and dynamic alpha-blended
images ontop of a VLC video. The idea here is to provide VLC with a
video filter that is comparable to what bmovl and bmovl2 provide for
MPLayer. What that is, is a video filter that enables third party
applications to get access to a piece of shared memory or similar, in
which the third party application can draw something. The third party
application can then notify VLC that the shared memory has been updated,
and VLC will then composite the image into subsequent frames.

{{GSoC}}

[[Category:SoC 2007 Project|*]]
