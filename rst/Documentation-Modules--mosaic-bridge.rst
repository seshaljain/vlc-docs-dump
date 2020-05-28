.. raw:: mediawiki

   {{Mosaic framework}}

.. raw:: mediawiki

   {{Module|name=mosaic-bridge|type=Stream output|first_version=0.8.2|description=Send a picture to the mosaic framework|sc=mosaic-bridge}}

Use this filter to send a picture to the mosaic framework. Processing can be applied before sending the picture, such as resizing, `chroma <chroma>`__ conversion and video filters. \__TOC_\_

Options
-------

.. raw:: mediawiki

   {{Option
   |name=sout-mosaic-bridge-id
   |value=string
   |default="Id"
   |description=Specify an identifier string for this subpicture. Used by clients of the mosaic framework to identify the picture's source.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-mosaic-bridge-width
   |value=integer
   |default=0
   |description=Resize video to this width if value is non-zero. Make sure to use the '''mosaic-keep-picture''' option to prevent the mosaic filter from resizing a second time.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-mosaic-bridge-height
   |value=integer
   |default=0
   |description=Resize video to this height if value is non-zero. Make sure to use the '''mosaic-keep-picture''' option to prevent the mosaic filter from resizing a second time.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-mosaic-bridge-sar
   |value=string
   |default="1:1"
   |description=Sample [[aspect ratio]] of the destination.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-mosaic-bridge-chroma
   |value=string
   |default="[[I420]]"
   |description=Force the use of a specific [[chroma]]. Use [[YUVA]] if you're planning to use the {{docmod|alphamask}} or {{docmod|bluescreen}} video filter.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-mosaic-bridge-vfilter
   |value=string
   |default=""
   |description=Video filter chain to apply after resizing and chroma conversion.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-mosaic-bridge-alpha
   |value=integer
   |default=255
   |min=0
   |max=255
   |description=Transparency of the mosaic picture.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-mosaic-bridge-x
   |value=integer
   |default=-1
   |description=X coordinate of the upper left corner in the mosaic if non-negative.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-mosaic-bridge-y
   |value=integer
   |default=-1
   |description=Y coordinate of the upper left corner in the mosaic if non-negative.
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/stream_out/mosaic-bridge.c}}

.. raw:: mediawiki

   {{Documentation footer}}
