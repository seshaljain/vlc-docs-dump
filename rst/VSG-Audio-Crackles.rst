\__NOTOC_\_

Crackles, pops, hizzes and other audio anomalies
------------------------------------------------

If you hear some unwanted audio problems you can try another audio output module to see if that solves the issue (Save and restart VLC after changes).

Open **Tools → Preferences** (set Show Settings to All) and then choose **Audio → Output module**.

There are multiple output modules you can use for audio. *'DirectX*\ **and **\ *\ Win32 waveOut*' should work in most cases.

Drivers
~~~~~~~

Be sure that your audio drivers **are up to date** and **compatible**! Out of date and incompatible drivers may cause audio anomalies in VLC.

For example, installing the WDM_A406 driver for a Realtek AC97 chip will cause VLC to clip audio badly. VLC runs perfectly fine when the bad driver is removed and the correct one installed.

ASIO
~~~~

ASIO support in VLC exists, but you will have to enable it by compiling manually.

.. raw:: mediawiki

   {{Anchoring space}}

.. raw:: mediawiki

   {{VSG}}
