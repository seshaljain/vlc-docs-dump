.. raw:: mediawiki

   {{See also|DBus-spec|DBus-usage}}

TODO for DBus integration
-------------------------

VLC implements `DBus-spec <DBus-spec>`__, a desktop-neutral document, that aims to be suitable for every Media Players.

Decide service behaviour
~~~~~~~~~~~~~~~~~~~~~~~~

Could vlc be a on-demand startable service, would it be useful ?

We just have to create a /usr/share/dbus-1/org.freedesktop.MediaPlayer.service:

.. code:: ini

   [D-BUS Service]

   Name=org.freedesktop.MediaPlayer

   Exec=/usr/bin/vlc -I dummy --control dbus

`Category:Development <Category:Development>`__
