.. raw:: mediawiki

   {{Mosaic framework}}

.. raw:: mediawiki

   {{Module|name=mosaic|type=Video subfilter|first_version=0.8.2|description=Mosaic video sub source}}

Use this filter to blend videos on top of another video. This can be used to create TV channels mosaics, setup a weather channel-like stream (with the video filter) and lots of other fun stuff.

Since VLC 0.8.6, you can also use the `HTTP interface <Documentation:Modules/http_intf>`__'s mosaic wizard to configure a mosaic easily. \__TOC_\_

Options
-------

.. raw:: mediawiki

   {{Option
   |name=mosaic-alpha
   |value=integer
   |min=0
   |max=255
   |default=255
   |description=Alpha blending (transparency) of the mosaic foreground pictures. 0 means transparent, 255 opaque.
   }}

.. raw:: mediawiki

   {{Option
   |name=mosaic-height
   |value=integer
   |min=0
   |max=<var>INT_MAX</var>
   |default=100
   |description=Total height of the mosaic, in pixels.
   }}

.. raw:: mediawiki

   {{Option
   |name=mosaic-width
   |value=integer
   |min=0
   |max=<var>INT_MAX</var>
   |default=100
   |description=Total width of the mosaic, in pixels.
   }}

.. raw:: mediawiki

   {{Option
   |name=mosaic-align<span id="select_mosaic-align"></span>
   |value=integer
   |select=[[#appendix_select_mosaic-align|{ 0, 1, 2, 4, 8, 5, 6, 9, 10 }]]
   |default=5
   |description=You can enforce the mosaic alignment on the parent video.
   }}

.. raw:: mediawiki

   {{Option
   |name=mosaic-xoffset
   |value=integer
   |min=0
   |max=<var>INT_MAX</var>
   |default=0
   |description=X Coordinate of the top-left corner of the mosaic.
   }}

.. raw:: mediawiki

   {{Option
   |name=mosaic-yoffset
   |value=integer
   |min=0
   |max=<var>INT_MAX</var>
   |default=0
   |description=Y Coordinate of the top-left corner of the mosaic.
   }}

.. raw:: mediawiki

   {{Option
   |name=mosaic-borderw
   |value=integer
   |min=0
   |max=<var>INT_MAX</var>
   |default=0
   |description=Border width between mosaic elements, in pixels.
   }}

.. raw:: mediawiki

   {{Option
   |name=mosaic-borderh
   |value=integer
   |min=0
   |max=<var>INT_MAX</var>
   |default=0
   |description=Border height between mosaic elements, in pixels.
   }}

.. raw:: mediawiki

   {{Option
   |name=mosaic-position<span id="mosaic-position"></span>
   |value=integer
   |select={ 0, 1, 2 }
   |default=0
   |description=Positioning method of the mosaic elements. Use <kbd>0</kbd> to position the elements automatically on the grid, <kbd>1</kbd> to position the elements in fixed positions on the grid (see mosaic-order) and <kbd>2</kbd> to use grid-independent offsets (see [[#mosaic-offsets|mosaic-offsets]]).
   }}

.. raw:: mediawiki

   {{Option
   |name=mosaic-rows
   |value=integer
   |min=1
   |max=<var>INT_MAX</var>
   |default=2
   |description=Number of image rows in the mosaic (only used if [[#mosaic-position|positioning method]] is set to "fixed").
   }}

.. raw:: mediawiki

   {{Option
   |name=mosaic-cols
   |value=integer
   |min=1
   |max=<var>INT_MAX</var>
   |default=2
   |description=Number of image columns in the mosaic (only used if [[#mosaic-position|positioning method]] is set to "fixed").
   }}

.. raw:: mediawiki

   {{Option
   |name=mosaic-keep-aspect-ratio
   |value=boolean
   |default=disabled
   |description=Keep the original [[aspect ratio]] when resizing mosaic elements.
   }}

.. raw:: mediawiki

   {{Option
   |name=mosaic-keep-picture
   |value=boolean
   |default=disabled
   |description=Do not resize or do any other transformation on the mosaic pictures. Should be enabled when using the {{docmod|mosaic-bridge}}'s resizing options.
   }}

.. raw:: mediawiki

   {{Option
   |name=mosaic-order
   |value=string
   |default=""
   |description=You can enforce the order of the elements on the mosaic. You must give a comma-separated list of picture ID(s) (For example: <kbd>tf1,fr2,fr3,m6</kbd>). These IDs are assigned in the {{docmod|mosaic-bridge}} module.
   }}

.. raw:: mediawiki

   {{Option
   |name=mosaic-offsets<span id="mosaic-offsets"></span>
   |value=string
   |default=""
   |description=You can enforce the <code>(x,y)</code> offsets of the elements on the mosaic (only used if [[#mosaic-position|positioning method]] is set to "offsets"). You must give a comma-separated list of coordinates. For example: <kbd>10,10,150,10</kbd> if you want to position the first picture at coordinates <code>(10,10)</code> and the second one at coordinates <code>(150,10)</code>.
   }}

.. raw:: mediawiki

   {{Option
   |name=mosaic-delay
   |value=integer
   |default=0
   |description=Pictures coming from the mosaic elements will be delayed according to this value (in milliseconds). For high values you will need to raise caching at input.
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/spu/mosaic.c}}

Appendix
--------

.. raw:: html

   <div class="plainlist">

-  ^ `--mosaic-align <#select_mosaic-align>`__\ 

.. raw:: html

   </div>

.. raw:: mediawiki

   {{Alignment mapping}}

.. raw:: mediawiki

   {{Documentation footer}}
