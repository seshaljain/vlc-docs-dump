** has basic support for mouse gestures.**

Activation
----------

To activate this feature, go to Preferences > All > Interface > Control Interfaces and check "Mouse gestures control interface". Then restart VLC.

Alternatively you can add "gestures" to the extraintf list (like this "vlc --extraintf gestures" ) when starting VLC from the command line, or manually write "gestures" in the "extra interface modules" field in the configuration window.

Settings
--------

You can select which button you want to hold down while using the gestures in the preferences panel (Control Interfaces > Gestures).

The following gestures are supported:

0.9.0 and over
~~~~~~~~~~~~~~

-  **left** : Short time skip backward (10sec by default)
-  **right** : Short time skip forward (10sec by default)
-  **left-up** : Faster
-  **right-up** : Slower
-  **left-down** : Go to previous entry in playlist
-  **right-down** : Go to next entry in playlist
-  **left-right** : Play/Pause
-  **right-left** : Play/Pause

-  **up** : Volume up
-  **down** : Volume down
-  **up-down** : Mute Volume
-  **down-up** : Mute Volume
-  **up-right** : Change Audio track
-  **down-right** : Change Subtitle track
-  **up-left** : Enter fullscreen mode
-  **down-left** : Quit VLC

0.8.x
~~~~~

-  **left** : Go to previous entry in playlist
-  **right** : Go to next entry in playlist
-  **up-right** : Enter fullscreen mode
-  **down-right** : Quit VLC

Related topic
~~~~~~~~~~~~~

`Interfaces <Interfaces>`__

`Category:Interfaces <Category:Interfaces>`__
