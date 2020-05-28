.. raw:: mediawiki

   {{Module|name=switcher|type=Stream output|last_version=2.0.9|description=[[MPEG-2 video]] switcher stream output|sc=switcher}}

This module used the library.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=sout-switcher-files
   |value=string
   |default=""
   |description=Full paths of the files separated by colons
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-switcher-sizes
   |value=string
   |default=""
   |description=List of sizes separated by colons (720x576:480x576)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-switcher-aspect-ratio
   |value=string
   |default=4:3
   |description=[[Aspect ratio]] (4:3, 16:9)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-switcher-port
   |value=integer
   |default=5001
   |description=[[UDP]] port to listen to for commands
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-switcher-command
   |value=integer
   |default=0
   |description=Initial command to execute
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-switcher-gop
   |value=integer
   |default=8
   |description=Number of [[P-frame]]s between two [[I-frame]]s
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-switcher-qscale
   |value=integer
   |default=5
   |description=Fixed quantizer scale to use
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-switcher-mute-audio
   |value=boolean
   |default=enabled
   |description=Mute audio when command is not 0
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-2.0.git|modules/stream_out/switcher.c}}

.. raw:: mediawiki

   {{Documentation}}
