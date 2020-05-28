'''NOTE: this module is in active development and has not made it into
the main tree yet.'''

{{Moduletype=Interfacedescription=control VLC using the MQTT protocol}}

This module will let you send control messages to VLC using the
[http://www.mqtt.org/ MQTT] protocol.

== Options == {{Option value=string description=Hostname of MQTT broker
to connect to }} {{Option value=integer description=Port number of MQTT
broker to connect to }} {{Option value=string description=The username
to connect to the broker with }} {{Option value=string description=The
password to connect to the broker with }} {{Option value=string
description=The topic name prefix to use }} {{Option value=string
description=The client identifier to connect to the broker as }}
{{Option value=string description=The keep alive time for the MQTT
protocol (in seconds) }} {{Option value=string description=The QoS level
to publish and subscribe using (0, 1 or 2) }}

== Protocol ==

=== Commands ===

Sent from client to VLC.

{\| class="wikitable" -\| <big>&#x2192;</big> \|\| vlc/command \|\|
<cmd> <arguments> \|\| Any of the below <big>&#x2192;</big> \|\|
vlc/command/add \|\| <url> \|\| Add <url> to the playlist
<big>&#x2192;</big> \|\| vlc/command/delete \|\| <pos> \|\| delete item
<pos> in playlist <big>&#x2192;</big> \|\| vlc/command/clear \|\| \|\|
clear the playlist <big>&#x2192;</big> \|\| vlc/command/play \|\| <pos>
\|\| Start playing item at <pos> <big>&#x2192;</big> \|\|
vlc/command/pause \|\| \|\| Pause Playback <big>&#x2192;</big> \|\|
vlc/command/stop \|\| \|\| Stop Playback <big>&#x2192;</big> \|\|
vlc/command/goto \|\| <pos> \|\| Goto item at index <pos>
<big>&#x2192;</big> \|\| vlc/command/next \|\| \|\| Start playing next
item in playlist <big>&#x2192;</big> \|\| vlc/command/prev \|\| \|\|
Start playing prev item in playlist <big>&#x2192;</big> \|\|
vlc/command/seek \|\| <time> \|\| Seek to <time> in the current item (in
seconds) <big>&#x2192;</big> \|\| vlc/command/volume \|\| <vol> \|\| Set
volume to <vol> (0 to 255) <big>&#x2192;</big> \|\| vlc/command/volup
\|\| <vol> \|\| Increase volume by <vol> <big>&#x2192;</big> \|\|
vlc/command/voldown \|\| <vol> \|\| Decrease volume by <vol>
<big>&#x2192;</big> \|\| vlc/command/repeat \|\| <mode> \|\| Turn on or
off playlist ''repeat'' mode (0 or 1) <big>&#x2192;</big> \|\|
vlc/command/random \|\| <mode> \|\| Turn on or off playlist ''random''
mode (0 or 1) <big>&#x2192;</big> \|\| vlc/command/loop \|\| <mode> \|\|
Turn on or off playlist ''loop'' mode (0 or 1) }

=== Status ===

Sent from VLC to client.

{\| class="wikitable" -\| <big>&#x2190;</big> \|\| vlc/status/playlist
\|\| <json> \|\| A JSON representation of the playlist is sent whenever
the playlist changes. <big>&#x2190;</big> \|\| vlc/status/state \|\|
<state> \|\| This retained message is sent by VLC whenever the player
changes state: \* opening \* buffering \* playing \* paused \* stopped
\* ended \* error \* notconnected <big>&#x2190;</big> \|\|
vlc/status/playing \|\| <json> \|\| Information about the currently
playing item as JSON is sent whenever a new item starts playing.
<big>&#x2190;</big> \|\| vlc/status/time \|\| <time> \|\| Progress
through the current stream as decimal seconds <big>&#x2190;</big> \|\|
vlc/status/length \|\| <time> \|\| Duration of current stream as decimal
seconds <big>&#x2190;</big> \|\| vlc/status/volume \|\| <vol> \|\| The
current volume between 0 and 255 (inclusive) \|}

[[Category:Interfaces]]
