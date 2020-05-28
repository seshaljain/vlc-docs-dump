.. raw:: mediawiki

   {{Module|name=clone|type=Video output splitter|description=Clone the video output window|sc=clone}}

You can use this module to play the video in more than one window to test different video outputs or display the same video on multiple screens on the same computer.

Options
-------

Examples
--------

``{{$}} vlc --video-splitter=clone --clone-count=2 video.ogv``

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/video_splitter/clone.c}}

.. raw:: mediawiki

   {{Documentation footer}}
