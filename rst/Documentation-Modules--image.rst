Video output
------------

.. raw:: mediawiki

   {{Module|name=image|type=Video output|first_version=0.8.2|last_version=0.9.10|description=Outputs the video images to files}}

In VLC 1.0.0 the image video output was rewritten into a video-filter named `scene <Documentation:Modules/scene>`__, and the old image video output was removed.

Trivia: `the help text <https://git.videolan.org/?p=vlc/vlc-0.9.git;a=blob;f=modules/video_output/image.c#l56>`__ was never changed after changed the default values of unsigned integers ``--image-out-width`` and ``--image-out-height`` from ``-1`` to ``0``—there was little point in fixing the help text for a deprecated module in software not yet publicly released! The coding error is absent from the current module, scene.

Option aliases ``--image-width`` for ``--image-out-width`` and ``--image-height`` for ``--image-out-height`` were deprecated in 0.9.0.

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=image-out-format
   |value=string
   |select={png,jpeg}
   |default=png
   |description=Format of the output images
   }}

.. raw:: mediawiki

   {{Option
   |name=image-out-width
   |value=integer
   |default=0
   |description=You can enforce the image width. By default VLC will adapt to the video characteristics
   }}

.. raw:: mediawiki

   {{Option
   |name=image-out-height
   |value=integer
   |default=0
   |description=You can enforce the image height. By default VLC will adapt to the video characteristics
   }}

.. raw:: mediawiki

   {{Option
   |name=image-out-ratio
   |value=integer
   |default=3
   |description=Ratio of images to record. ''3'' means that one image out of three is recorded
   }}

.. raw:: mediawiki

   {{Option
   |name=image-out-prefix
   |value=string
   |default=img
   |description=Prefix of the output images filenames. Output filenames will have the "prefixNUMBER.format" form. Starting with VLC 0.9.0 you can also use [[Documentation:Format String|format time and meta variables]]
   }}

.. raw:: mediawiki

   {{Option
   |name=image-out-replace
   |value=boolean
   |default=disabled
   |description=Always write to the same file instead of creating one file per image. In this case, the number is not appended to the filename
   }}

Demux
-----

.. raw:: mediawiki

   {{Clear}}

.. raw:: mediawiki

   {{Module|name=image|type=Access demux|description=Image demuxer}}

.. _options-1:

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=image-id
   |value=integer
   |default=-1
   |description=Set the ID of the [[elementary stream]]
   }}

.. raw:: mediawiki

   {{Option
   |name=image-group
   |value=integer
   |default=0
   |description=Set the group of the elementary stream
   }}

.. raw:: mediawiki

   {{Option
   |name=image-decode
   |value=boolean
   |default=enabled
   |description=Decode at the [[demux]]er stage
   }}

.. raw:: mediawiki

   {{Option
   |name=image-chroma
   |value=string
   |default=""
   |description=If non empty and <var>image-decode</var> is true, the image will be converted to the specified [[chroma]]
   }}

.. raw:: mediawiki

   {{Option
   |name=image-duration
   |value=float
   |default=10
   |description=Duration in seconds before simulating an end of file. A negative value means an unlimited play time
   }}

.. raw:: mediawiki

   {{Option
   |name=image-fps
   |value=string
   |default=10/1
   |description=[[Frame rate]] of the elementary stream produced
   }}

.. raw:: mediawiki

   {{Option
   |name=image-realtime
   |value=boolean
   |default=disabled
   |description=Use real-time mode suitable for being used as a master input and real-time input slaves
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-0.9.git|modules/video_output/image.c}}

   (video output)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/image.c}}

   (image demuxer)

.. raw:: mediawiki

   {{Documentation footer}}
