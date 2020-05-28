VLC crashes while using DirectShow (eg Webcam)
----------------------------------------------

''This has also been discussed in the `forum <http://forum.videolan.org/viewtopic.php?t=12394>`__.''

There was a bug a while back when you tried to stream using a directshow/webcam it would reboot the computer. The fix was to specify the resolution on the command line or in the "Advanced" section when opening the directshow.

Some things to try for reboot issues for direct show capture devices (it's not VLC crashing but it seems to trigger a driver bug which takes down the Operating System):

| i) Update VLC to latest version (final or a development version from http://nightlies.videolan.org)
| ii) Update DirectX to latest version (Windows Update)
| iii) Update drivers for video and audio to latest versions.
| iv) Disable `hardware acceleration <hardware_acceleration>`__. Rightclick on Desktop, Properties, Settings, Advanced, Troubleshoot. Move the slider to None. Reboot
| v) Use one capture device so only video for starters (no adev and commandline --no-audio) to rule out an audio driver problem (and vice versa)
| vi) Force a dshow-size to something your card supports dshow-size="320x240", if that fails specify resolution with spaces "320 x 240".

.. raw:: mediawiki

   {{VSG}}
