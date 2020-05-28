.. raw:: mediawiki

   {{protocol|dc1394}}

.. raw:: mediawiki

   {{Module|name=dc1394|type=Access demux|first_version=0.9.0|os=Linux|description=IIDC (DCAM) FireWire input module}}

Introduction
------------

This is an access module for `IIDC (firewire) cameras <wikipedia:IIDC>`__. It uses libdc1394 version 1 libraries. Seems to have been written for an Apple iSight, as there is support for 320x240 and 640x480, but no other sizes. Only supported on `Linux <Linux>`__.

Installation
------------

-  Before installation ensure that raw1394, dc1394, and all other necessary libraries for these. libdc1394_control.so.13 is needed either in /usr/lib or /usr/local/lib.
-  Ensure that the modules are loaded. (should happen automatically)
-  During the `configure <configure>`__ stage add: --enable-dc1394

Usage
-----

Various examples of how to use the dc1394 module are shown below. You can try some new options yourself, but many have defaults and will work without.

| ``vlc dc1394:cameraindex=3:size=640x480:fps=30:brightness=100``
| ``vlc dc1394:/dev/video1394/0:capture=raw1394``
| ``vlc dc1394:/dev/video1394/0:adev=/dev/audio``
| ``vlc dc1394:/dev/video1394/0:size=640x480:fps=30:brightness=200:adev=/dev/dsp:channel=2``
| ``vlc dc1394:/dev/video1394/0:size=320x240:fps=15:brightness=200 \``
| ``   --sout='#transcode{vcodec=mp4v,vb=3000,keyint=30}:std{access=udp,mux=ts,url=192.168.150.79}'``

Future Modifications
--------------------

Unsure of plans to support the upcoming libdc1394 v2 library. As the library is designed to be configurable it would be ideal that the user can input any sizes, formats, and framerates (and other features) supported by the camera. Most cameras with larger frame sizes are more expensive cameras thus demand is likely not high, however, may be useful for some. Will create problems as it requires the user to be sure of the cameras supported features (however almost all support 640x480 and 320x240, so we will never exit poorly).

Source code
-----------

.. raw:: mediawiki

   {{file|modules/access/dc1394.c|access module}}

`Category:GNU/Linux <Category:GNU/Linux>`__
