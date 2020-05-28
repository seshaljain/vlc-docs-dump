**NOTE: this module is in active development and has not made it into the main tree yet.**

.. raw:: mediawiki

   {{Module|name=mqtt|type=Interface|os=Any that support the [http://mosquitto.org/ mosquitto] library|description=control VLC using the MQTT protocol}}

This module will let you send control messages to VLC using the `MQTT <http://www.mqtt.org/>`__ protocol.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=mqtt-host
   |value=string
   |default=localhost
   |description=Hostname of MQTT broker to connect to
   }}

.. raw:: mediawiki

   {{Option
   |name=mqtt-port
   |value=integer
   |default=1883
   |description=Port number of MQTT broker to connect to
   }}

.. raw:: mediawiki

   {{Option
   |name=mqtt-username
   |value=string
   |default=none
   |description=The username to connect to the broker with
   }}

.. raw:: mediawiki

   {{Option
   |name=mqtt-password
   |value=string
   |default=none
   |description=The password to connect to the broker with
   }}

.. raw:: mediawiki

   {{Option
   |name=mqtt-prefix
   |value=string
   |default=vlc/
   |description=The topic name prefix to use
   }}

.. raw:: mediawiki

   {{Option
   |name=mqtt-clientid
   |value=string
   |default=random
   |description=The client identifier to connect to the broker as
   }}

.. raw:: mediawiki

   {{Option
   |name=mqtt-keepalive
   |value=string
   |default=10
   |description=The keep alive time for the MQTT protocol (in seconds)
   }}

.. raw:: mediawiki

   {{Option
   |name=mqtt-qos
   |value=string
   |default=1
   |description=The QoS level to publish and subscribe using (0, 1 or 2)
   }}

Protocol
--------

Commands
~~~~~~~~

Sent from client to VLC.

========= =================== ======= ==============================================
Direction Topic               Payload Description
========= =================== ======= ==============================================
→         vlc/command                 Any of the below
→         vlc/command/add             Add to the playlist
→         vlc/command/delete          delete item in playlist
→         vlc/command/clear           clear the playlist
→         vlc/command/play            Start playing item at
→         vlc/command/pause           Pause Playback
→         vlc/command/stop            Stop Playback
→         vlc/command/goto            Goto item at index
→         vlc/command/next            Start playing next item in playlist
→         vlc/command/prev            Start playing prev item in playlist
→         vlc/command/seek            Seek to in the current item (in seconds)
→         vlc/command/volume          Set volume to (0 to 255)
→         vlc/command/volup           Increase volume by
→         vlc/command/voldown         Decrease volume by
→         vlc/command/repeat          Turn on or off playlist *repeat* mode (0 or 1)
→         vlc/command/random          Turn on or off playlist *random* mode (0 or 1)
→         vlc/command/loop            Turn on or off playlist *loop* mode (0 or 1)
\                                    
========= =================== ======= ==============================================

Status
~~~~~~

Sent from VLC to client.

========= =================== ======= ================================================================================================
Direction Topic               Payload Description
========= =================== ======= ================================================================================================
←         vlc/status/playlist         A JSON representation of the playlist is sent whenever the playlist changes.
←         vlc/status/state            This retained message is sent by VLC whenever the player changes state:
                                     
                                      -  opening
                                      -  buffering
                                      -  playing
                                      -  paused
                                      -  stopped
                                      -  ended
                                      -  error
                                      -  notconnected
←         vlc/status/playing          Information about the currently playing item as JSON is sent whenever a new item starts playing.
←         vlc/status/time             Progress through the current stream as decimal seconds
←         vlc/status/length           Duration of current stream as decimal seconds
←         vlc/status/volume           The current volume between 0 and 255 (inclusive)
========= =================== ======= ================================================================================================

`Category:Interfaces <Category:Interfaces>`__
