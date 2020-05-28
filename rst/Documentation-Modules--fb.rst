.. raw:: mediawiki

   {{Module|name=fb|type=Video output|os=Linux|description=GNU/Linux framebuffer video output|sc=none}}

| Option ``--fb-aspect-ratio`` is deprecated.
| Option ``--fb-hw-accel`` is planned to be deprecated in 4.0.0 (currently 4.0.0-dev).

Options
-------

.. raw:: mediawiki

   {{Option
   |name=fbdev
   |value=string
   |default="/dev/fb0"
   |description=Framebuffer device to use for rendering (usually <code>/dev/fb0</code>)
   }}

.. raw:: mediawiki

   {{Option
   |name=fb-tty
   |value=boolean
   |default=enabled
   |description=Run framebuffer on current [[wiktionary:TTY|TTY]] device (default enabled). (disable tty handling with caution)
   }}

.. raw:: mediawiki

   {{Option
   |name=fb-chroma
   |value=string
   |default=RGB
   |description=Chroma [[fourcc]] used by the framebuffer. Default is [[RGB]] since the fb device has no way to report its [[chroma]]
   }}

.. raw:: mediawiki

   {{Option
   |name=fb-mode
   |value=integer
   |select={0,1,2,3,4}
   |default=4
   |description=Select the resolution for the framebuffer. Currently it supports the values: 0 - QCIF, 1 - CIF, 2 - NTSC, 3 - PAL, 4 - auto
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/video_output/fb.c}}

.. raw:: mediawiki

   {{Documentation}}
