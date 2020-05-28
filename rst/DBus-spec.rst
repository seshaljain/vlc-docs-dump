{{See alsoDBus-usage}} {{Historical}} Specification for a Common,
Desktop neutral, Media Player D-Bus interface

'''Please note this document is not specific to VLC and is a work in
progress.'''

MPRIS discussion is at
http://wiki.xmms2.xmms.se/index.php/Media_Player_Interfaces

MPRIS specification is at
https://specifications.freedesktop.org/mpris-spec/latest/

What follows has been largely stolen from
http://bmpx.beep-media-player.org/site/MPRIS_Interfacing_Specification

This is an attempt to create a specification for media players to use,
for '''YOUR''' applications to be able to interact with '''ANY''' Media
Player '''YOU''' want to use on '''ANY''' desktop '''YOU''' want to use.

This is in the spirit of http://www.freedesktop.org and uses code and
ideas from this project, most notably D-Bus :
http://dbus.freedesktop.org and uses ideas from
http://www.musicbrainz.org

= Other players =

How other "Media Players" interact with D-Bus

== bmpx ==

http://bmpx.beep-media-player.org/site/MPRIS_Interfacing_Specification

== banshee ==

http://cvs.gnome.org/viewcvs/*checkout*/banshee/src/Banshee.Base/DBusPlayer.cs

== rhythmbox ==

http://cvs.gnome.org/viewcvs/rhythmbox/remote/dbus/rb-client.c?view=markup

== muine ==

http://cvs.gnome.org/viewcvs/muine/DBusLib/Player.cs?view=markup

== amarok ==

http://amarok.kde.org/wiki/DCOP_Functions (D-Bus will replace DCOP in
KDE4, Amarok 2.0)

== xmms 2 ==

http://wiki.xmms2.xmms.se/index.php/MPRIS

= Definitions =

== "Media Player" ==

An application, either with GUI or GUI-less (or which allows for both
modes of operation) which is capable of playing back audio/video
streams. The means by which it does accomplish that (e.g. which audio
backend to use, and which output method) is out of the scope of this
document.

The "Media Player" '''must''': \* Be able to play back at least local
storage file streams. \* Be able to play back at least one stream at a
time.

== "Client" ==

The Client is an unspecified application that will interact with the
"Media Player" using D-Bus protocol. For example:

-  A softphone, that pauses, or step the volume down, when a call is
   being received.
-  An applet that nicely integrates in your desktop environment, to
   control your "Media Player".
-  An instant messaging client which informs your buddies of what you're
   listening to.
-  A monitor that stores in a database what you are listening to, for
   statistics purpose.
-  A video editing software that calls an external "Media Player" to
   preview your work.

== "Tracklist" ==

A list of media files which resides within the "Media Player", and whose
implementation is opaque to the remote interface.

The "Tracklist" '''must''': \* Hold an ordered list of locations of the
media files as URIs (e.g. file:// or <nowiki>http://\ </nowiki>). The
implementation of this can be opaque, which means, it does not
neccesarily need to store URIs, but upon remote request, it must be able
to return an URI for a given media file. \* Keep the list in an ordered
fashion. The order can be changed at any time trough e.g. sorting
algorithms, in which case the "Media Player" must send information about
the reordering trough it's remote interface

The "Tracklist" '''can''', but does not '''need''' to: \* Hold
"Metadata" about media files

== "Metadata" ==

"Metadata" is data that the files carry within themselves as a means of
self-identification (commonly known as "tags"), or data that has been
retrieved about the files trough other means, e.g. an internet service
that provides additional data about particular media files. "Metadata"
is an array of dict entries, like ("length", 253), ("name", "Bolero"),
("video-codec", "DIVX"). The dict entry is in the form (string, variant)
eg: {sv}.

Furthermore, "Metadata" can be split into two categories:

1) Technical metadata: \* "URI":"s" \* "length":"i" (length in seconds)
\* "video-codec":"s" (video codec as a fourcc) \* "audio-codec":"s"
(audio codec as a fourcc) \* "video-bitrate":"i" video bitrate \*
"audio-bitrate":"i" audio bitrate \* "audio-samplerate":"i" (audio
samplerate)

2) Informational metadata \* "name":"s" \* "artist":"s" \* "album":"s"
\* "unique-id":"s" : Musicbrainz Track Identifier as specified on
http://musicbrainz.org/docs/specs/metadata_tags.html \* "genre":"s"

This list is informative, and can be extended up to your needs, for
example: "age of the captain":"i"

Only Required fields are: "URI" and "length"

= D-Bus =

== The Service ==

org.freedesktop.MediaPlayer

All "Media Players" '''must''' request this name and do not let other
"Media Players" 'steal' this name. Using libdbus, that would be:

   DBusConnection \*dbus_connection; DBusError dbus_error;
   dbus_bus_request_name( dbus_connection,
   "org.freedesktop.MediaPlayer", 0, &dbus_error );

To be able to request the name, and so, be able to communicate via
D-Bus, no "Media Player" must be running. The "Media Player" may call
the Quit method, and wait till the name is unregistered, to ensure this
is the case.

: I think this is a bad idea, it's not the place for a interop Spec to
force single instance behaviour without a good reason (i run amarok all
the time and use vlc to play videos or streams...). Why not suggest that
mediaplayers register with the well known service name
("org.freedesktop.MediaPlayer") with the options QueueService and
suggest the media player should register an application specific service
in addition?

: if done that way we gain the feature to query the dbus daemon for all
clients queued for that dbus name, so enumerating all current
musicplayers that support the Spec is not problem. Contacting the
players is not problem to because every client on dbus has a unique name
anyway. DBus signal do AFAIK carry the dbus service name of the sending
client, so there is no trouble knowing which player send a signal.
[[User:textshell|textshell]]

== The Object Hierarchy ==

-  / : Media Player identification
-  /Player : Playback control
-  /TrackList : TrackList management

== The interface ==

All methods must be accessed through the interface
org.freedesktop.MediaPlayer

i.e. calling Quit with qdbus would be:
   $ qdbus org.freedesktop.MediaPlayer /Player
   org.freedesktop.MediaPlayer.Quit

== The Methods ==

What's missing: we could use musicbrainz unique identifier to identify
current element in the playlist From fd.o : GetTrackList (using xspf?),
ClearTrackList

-  /

Identity : Identify the "Media Player" as in "VLC 0.9.0", "bmpx 0.34.9",
"Totem 2.16.2" ...

   <method name="Identity">
      <arg type="s" direction="out"/>

   </method>

-  /TrackList

GetMetadata : Gives all meta data available for element at given
position in the "TrackList"

   <method name="GetMetadata">
      <arg type="i" direction="in" /> <arg type="a{sv}" direction="out"
      />

   </method>

GetCurrentTrack : Position of Current URI in the "TrackList"

   <method name="GetCurrentTrack">
      <arg type="i" direction="out" />

   </method>

GetLength : Number of elements in the "TrackList"

   <method name="GetLength">
      <arg type="i" direction="out" />

   </method>

AddTrack : Appends an URI in the "TrackList", play it immediately if the
2nd argument is TRUE

   <method name="AddTrack">
      <arg type="s" /> <arg type="b" />

   </method>

DelTrack : Removes an URI from the "TrackList", given its position

   <method name="DelTrack">
      <arg type="i" />

   </method>

-  /Player

Next : Goes to the next element (what if we're at the end?)

   <method name="Next"> </method>

Prev : Goes to the previous element (what if we're at the beginning?)

   <method name="Prev"> </method>

Pause : If playing : pause. If paused : unpause. If stopped : start
playing

   <method name="Pause"> </method>

Stop : Stop playing.

   <method name="Stop"> </method>

Play : If playing : rewind to the beginning of current track, else :
start playing.

   <method name="Play"> </method>

Quit : Makes the "Media Player" exit.

   <method name="Quit"> </method>

GetStatus : Return the status of "Media Player": 0 = Playing, 1 =
Paused, 2 = Stopped.

   <method name="GetStatus"> <arg type="i" direction="out"/> </method>

VolumeSet : Sets the volume (argument must be in [0;100])

   <method name="VolumeSet"> <arg type="i"/> </method>

GetVolume : Returns the current volume (must be in [0;100])

   <method name="VolumeGet"> <arg type="i" direction="out"/> </method>

PositionSet : Sets the playing position (argument must be in [0;100])

   <method name="PositionSet"> <arg type="i"/> </method>

PositionGet : Returns the playing position (must be in [0;100])

   <method name="PositionGet"> <arg type="i" direction="out"/> </method>

== The signals ==

TrackChange : Signal is emitted when the "Media Player" plays another
"Track". Argument of the signal is the metadata attached to the new
"Track"

   <signal name="TrackChange">
      <arg type="a{sv}"/>

   </signal>

StatusChange : Signal is emitted when the status of the "Media Player"
change. The argument has the same meaning than the value returned by
GetStatus.

   <signal name="StatusChange">
      <arg type="i"/>

   </signal>

CapabilityChange : [TODO] Signal is emitted when the "Media Player"
changes capabilities, Flags are CAN_GO_NEXT CAN_GO_PREV CAN_PAUSE
CAN_PLAY CAN_SEEK CAN_PROVIDE_METADATA PROVIDES_TIMING

   <signal name="CapabilityChange">
      <arg type=TODO />

   </signal>

= See Also = \*
[http://bmpx.beep-media-player.org/site/MPRIS_Interfacing_Specification
MPRIS Interfacing Specification] (BMPx wiki) \*
[http://wiki.xmms2.xmms.se/index.php/Media_Player_Interfaces Media
Player Interfaces] (XMMS2 wiki)

[[Category:Dev Discussions]] [[Category:Development]]
