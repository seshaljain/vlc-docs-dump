.. raw:: mediawiki

   {{Module|name=kate|type=Access demux|first_version=0.9.0|description=[[Kate]] overlay decoder|sc=kate}}

The help text for this module:

::

   Kate is a codec for text and image based overlays.
   The Tiger rendering library is needed to render complex Kate streams, but VLC can still render static text and image based subtitles if it is not available.
   Note that changing settings below will not take effect until a new stream is played. This will hopefully be fixed soon.

Options
-------

Basic
~~~~~

.. raw:: mediawiki

   {{Option
   |name=kate-formatted
   |value=boolean
   |default=enabled
   |description=Kate streams allow for text formatting. VLC partly implements this, but you can choose to disable all formatting. Note that this has no effect if rendering via Tiger is enabled
   }}

Tiger
~~~~~

.. raw:: mediawiki

   {{Option
   |name=kate-use-tiger
   |value=boolean
   |default=enabled
   |description=Kate streams can be rendered using the Tiger library. Disabling this will only render static text and bitmap based streams
   }}

.. raw:: mediawiki

   {{Option
   |name=kate-tiger-quality
   |value=float
   |min=0.0f
   |max=1.0f
   |default=1.0
   |description=Select rendering quality, at the expense of speed. 0 is fastest, 1 is highest quality
   }}

Tiger rendering defaults
^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: mediawiki

   {{Option
   |name=kate-tiger-default-font-desc
   |value=string
   |description=Which font description to use if the Kate stream does not specify particular font parameters (name, size, etc) to use. A blank name (default) will let Tiger choose font parameters where appropriate
   }}

.. raw:: mediawiki

   {{Option
   |name=kate-tiger-default-font-effect
   |value=integer
   |default=0
   |description=Add a font effect to text to improve readability against different backgrounds
   }}

.. raw:: mediawiki

   {{Option
   |name=kate-tiger-default-font-effect-strength
   |value=float
   |min=0.0f
   |max=1.0f
   |default=0.5
   |description=How pronounced to make the chosen font effect (effect dependent)
   }}

.. raw:: mediawiki

   {{Option
   |name=kate-tiger-default-font-color
   |value=integer
   |default=0x00ffffff (white)
   |description=Default font color to use if the Kate stream does not specify a particular font color to use
   }}

.. raw:: mediawiki

   {{Option
   |name=kate-tiger-default-font-alpha
   |value=integer
   |min=0x00
   |max=0xff
   |default=0xff
   |description=Transparency of the default font color if the Kate stream does not specify a particular font color to use (0x00 is fully transparent, 0xff is fully opaque)
   }}

.. raw:: mediawiki

   {{Option
   |name=kate-tiger-default-background-color
   |value=integer
   |default=0x00ffffff (white)
   |description=Default background color if the Kate stream does not specify a background color to use
   }}

.. raw:: mediawiki

   {{Option
   |name=kate-tiger-default-background-alpha
   |value=integer
   |min=0x00
   |max=0xff
   |default=0x00
   |description=Transparency of the default background color if the Kate stream does not specify a particular background color to use (0x00 is fully transparent, 0xff is fully opaque)
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/kate.c}}
