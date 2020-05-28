.. raw:: mediawiki

   {{Module|name=scene|type=Video filter|first_version=1.0.0|description=Send your video to picture files}}

**Note:** Before version 1.0.0, this used to be `image <Documentation:Modules/image>`__.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=scene-format
   |value=string
   |default=png
   |description=Image format. Format of the output images ([[png]], [[jpeg]], ...)
   }}

.. raw:: mediawiki

   {{Option
   |name=scene-width
   |value=integer
   |description=Image width. You can enforce the image width. By default (-1) VLC will adapt to the video characteristics
   |default=-1
   }}

.. raw:: mediawiki

   {{Option
   |name=scene-height
   |value=integer
   |description=Image height. You can enforce the image height. By default (-1) VLC will adapt to the video characteristics
   |default=-1
   }}

.. raw:: mediawiki

   {{Option
   |name=scene-prefix
   |value=string
   |default=scene
   |description=Filename prefix. Prefix of the output images filenames. Output filenames will have the "prefixNUMBER.format" form if <var>scene-replace</var> is not true
   }}

.. raw:: mediawiki

   {{Option
   |name=scene-path
   |value=string
   |default=NULL
   |description=Directory path prefix. Directory path where images files should be saved. If not set, then images will be automatically saved in users homedir
   }}

.. raw:: mediawiki

   {{Option
   |name=scene-replace
   |value=boolean
   |description=Always write to the same file. Always write to the same file instead of creating one file per image. In this case, the number is not appended to the filename
   |default=disabled
   }}

.. raw:: mediawiki

   {{Option
   |name=scene-ratio
   |value=integer
   |default=50
   |min=1
   |max=<var>INT_MAX</var>
   |description=Recording ratio. Ratio of images to record. 3 means that one image out of three is recorded
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/video_filter/scene.c}}

.. raw:: mediawiki

   {{Documentation}}
