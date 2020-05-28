.. raw:: mediawiki

   {{Module|name=wall|type=Video output splitter|description=Splits the video output in several windows}}

You can use this module to split a video output in several small windows. This is especially useful if you want to display parts of the same video on several computers to make a big video wall.

The option ``--wall-element-aspect`` is to fix and . The option is redundant, and there will still be a way to select a custom ratio.

For the option ``--wall-active``, list the integers of the windows. To select windows 2, 3 and 5 specify --wall-active=2,3,5.

Options
-------

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/video_splitter/wall.c}}

.. raw:: mediawiki

   {{Documentation footer}}
