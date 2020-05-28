Decoding and encoding (text rendering) are handled by separate modules. Both modules have the same shortcut, ``svg``, though calls them ``svgdec`` and ``svg``.

Decoder
-------

.. raw:: mediawiki

   {{Module|name=svg|type=Input|first_version=2.2.0|description=[[SVG]] video decoder making use of librsvg2}}

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=svg-width
   |value=integer
   |min=1
   |max=65535
   |default=-1
   |description=Specify the width to decode the image to
   }}

.. raw:: mediawiki

   {{Option
   |name=svg-height
   |value=integer
   |min=1
   |max=65535
   |default=-1
   |description=Specify the height to decode the image to
   }}

.. raw:: mediawiki

   {{Option
   |name=svg-scale
   |value=float
   |default=-1.0
   |description=Scale factor to apply to image
   }}

.. raw:: mediawiki

   {{Clear}}

Encoder
-------

.. raw:: mediawiki

   {{Module|name=svg|type=Input|first_version=0.8.0|os=Linux|description=Put [[SVG]] on the video}}

.. _options-1:

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=svg-template-file
   |value=string
   |default=""
   |description=Location of a file holding a SVG template for automatic string conversion
   }}

.. raw:: mediawiki

   {{Clear}}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/svg.c}}

   (decoder)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/text_renderer/svg.c}}

   (encoder)

.. raw:: mediawiki

   {{Documentation footer}}
