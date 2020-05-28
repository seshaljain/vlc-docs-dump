.. raw:: mediawiki

   {{Howto|jump to a certain time in a video}}

Graphical
---------

`framed|right|The dialogue box as shown in VLC 3.0.6 (Linux)|alt= <File:Go_to_time_-_VLC_3.0.6_Linux.png>`__

In the menu bar select **Playback** → **Jump to Specific Time**. Alternatively, press Ctrl+T. Enter the hours, minutes, and seconds.

Command-line
------------

To seek from the command-line, use ``--start-time``\  to skip the beginning or ``--stop-time``\  to skip the end. As of VLC version 1.0.0 sub-second values are accepted. Example:

``{{%}} vlc --start-time=83.4 --stop-time=300 BigBuckBunny.ogv``

Plays an open-source movie starting at 1 minute 23.4 seconds and ending at 5 minutes.

Advanced users: playback control is documented in ``vlc --module=core --advanced``

.. raw:: mediawiki

   {{VSG}}

`Category:GNU GPL Licensed pages <Category:GNU_GPL_Licensed_pages>`__
