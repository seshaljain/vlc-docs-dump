nVidia playback problem
-----------------------

| Using **nvidia-xconfig** with Debian, the screen may go into standby mode.
| This doesn't seem to be a bug with , but it may occur when using VLC, such as when watching a movie.

The easiest thing to try is disabling the screensaver through **Preferences** → **Video** → **Disable screensaver**.

Another approach is to run

``{{$}} xset dpms 0 0 0 && xset s noblank && xset s off``

which disables DPMS (Display Power Management Signaling).

If the issue does not resolve, and it seems VLC-specific, then `report a bug <report_a_bug>`__.

.. raw:: mediawiki

   {{VSG}}
