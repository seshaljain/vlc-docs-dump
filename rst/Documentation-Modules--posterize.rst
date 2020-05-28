.. raw:: mediawiki

   {{Module|name=posterize|type=Video filter|first_version=2.0.0|description=Posterize video by lowering the number of colors}}

Options
-------

.. raw:: mediawiki

   {{Option
   |name=posterize-level
   |value=integer
   |default=6
   |min=2
   |max=256
   |description=Posterize level (number of colors is cube of this value)
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/video_filter/posterize.c}}

.. raw:: mediawiki

   {{Documentation footer}}
