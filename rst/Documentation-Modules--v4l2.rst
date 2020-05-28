.. raw:: mediawiki

   {{Module|name=v4l2|type=Access demux|first_version=0.9.0|os=Linux|description=Video for Linux 2 input}}

Options
-------

.. raw:: mediawiki

   {{Option
   |name=v4l2-caching
   |value=integer
   |description=Caching in ms
   }}

Video input
~~~~~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=v4l2-dev
   |value=string
   |default="/dev/video0"
   |description=Primary device name
   }}

.. raw:: mediawiki

   {{Option
   |name=v4l2-standard
   |value=integer
   |default=0
   |description=Video standard
   }}

.. raw:: mediawiki

   {{Option
   |name=v4l2-chroma
   |value=string
   |default=""
   |description=Force use of a specific video chroma (Use MJPG here to use a webcam's MJPEG stream)
   }}

.. raw:: mediawiki

   {{Option
   |name=v4l2-input
   |value=integer
   |default=0
   |description=Card input to use for video
   }}

.. raw:: mediawiki

   {{Option
   |name=v4l2-audio-input
   |value=integer
   |default=0
   |description=Card input to use for audio
   }}

.. raw:: mediawiki

   {{Option
   |name=v4l2-io
   |value=integer
   |default=0
   |description=IO method
   }}

.. raw:: mediawiki

   {{Option
   |name=v4l2-width
   |value=integer
   |default=0
   |description=Prefered video width (if non zero)
   }}

.. raw:: mediawiki

   {{Option
   |name=v4l2-height
   |value=integer
   |default=0
   |description=Prefered video height (if non zero)
   }}

.. raw:: mediawiki

   {{Option
   |name=v4l2-fps
   |value=float
   |default=0
   |description=Frames per second (if non zero)
   }}

Audio input
~~~~~~~~~~~

These options do not apply to audio streams in compressed data.

Tuner
~~~~~

.. raw:: mediawiki

   {{Option
   |name=v4l2-tuner
   |value=integer
   |default=0
   |description=Tuner to use
   }}

.. raw:: mediawiki

   {{Option
   |name=v4l2-tuner-frequency
   |value=integer
   |default=-1
   |description=Tuner frequency in Hz or MHz depending on the underlying v4l2 driver
   }}

.. raw:: mediawiki

   {{Option
   |name=v4l2-tuner-audio-mode
   |value=integer
   |default=-1
   |description=Tuner audio mode
   }}

Controls
~~~~~~~~

These controls will be used only if they are supported by the v4l2 driver.

Example
-------

Open a video device with default settings:

``% ``\ **``vlc``\ ````\ ``v4l2:///dev/video0:width=640:height=480``**

Get information about a video device's capabilities:

``% '''vlc -vvv --color v4l2:///dev/video0 --run-time 1 vlc://quit -I dummy -V dummy -A dummy``

Command line for Hauppauge PVR 250 to get France 2 (at ECP) and encode as MPEG2 and stream using UDP multicast:

``% ``\ **``vlc``\ ````\ ``-I``\ ````\ ``dummy``\ ````\ ``-vvv``\ ````\ ``'v4l2c://:audio-method=0:controls-reset:set-ctrls={video_bitrate_mode=1,video_bitrate=4000000,video_peak_bitrate=4000000}:width=720:height=576:tuner=0:tuner-frequency=478550'``\ ````\ ``--sout``\ ````\ ``"#std{access=udp{ttl=12},mux=ts,url=239.255.1.1}"``**

Note: v4l2c is an alias used to force VLC to use the v4l2 module in it's Access variant without probing the Access Demux version first (the c stands for compressed).

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/v4l2/v4l2.c}}

See also
--------

-  `Documentation:Modules/v4l <Documentation:Modules/v4l>`__
-  `Documentation:Modules/dshow <Documentation:Modules/dshow>`__

.. raw:: mediawiki

   {{Documentation footer}}

`Category:GNU/Linux <Category:GNU/Linux>`__
