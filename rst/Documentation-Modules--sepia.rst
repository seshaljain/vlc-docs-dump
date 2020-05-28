.. raw:: mediawiki

   {{Module|name=sepia|type=Video filter|first_version=2.0.0|description=Gives video a warmer tone by applying sepia effect}}

Options
-------

.. raw:: mediawiki

   {{Option
   |name=sepia-intensity
   |value=integer
   |default=120
   |min=0
   |max=255
   |description=Intensity of sepia effect
   }}

Examples
--------

| ``{{%}} --video-filter "sepia" video.ogv``
| ``{{%}} --video-filter "sepia{intensity=100}" video.ogv``

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/video_filter/sepia.c}}

.. raw:: mediawiki

   {{Documentation footer}}
