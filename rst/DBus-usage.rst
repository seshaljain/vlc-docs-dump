.. raw:: mediawiki

   {{See also|DBus|DBus-spec}}

The following is a usage example of how to control VLC though DBUS, by simple using dbus-send. This bash script toggles between Play/Pause:

Stopped -> Play

Playing -> Pause

Pause -> Play

.. code:: bash

   #!/bin/bash
   if dbus-send --print-reply --session --dest=org.mpris.vlc /Player org.freedesktop.MediaPlayer.GetStatus | grep -Fq "int32 2"; then
           # Match found
           dbus-send --print-reply --session --dest=org.mpris.vlc /Player org.freedesktop.MediaPlayer.Play
   else
           # Match not found
           dbus-send --print-reply --session --dest=org.mpris.vlc /Player org.freedesktop.MediaPlayer.Pause
   fi

If you have qt-dbus (or libqt4-dev) installed, you can also use qdbus to toggle between Play/Pause

.. code:: bash

   #!/bin/bash
   qdbus org.mpris.MediaPlayer2.vlc /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause

`Category:Development <Category:Development>`__
