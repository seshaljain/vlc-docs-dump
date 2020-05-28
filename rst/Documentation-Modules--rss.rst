.. raw:: mediawiki

   {{Module|name=rss|type=Video sub-filter|first_version=0.8.4|description=Overlays [[wikipedia:RSS|RSS]] and [[wikipedia:Atom (Web standard)|Atom]] feeds on the video|sc=rss|sc2=atom}}

Options
-------

.. raw:: mediawiki

   {{Option
   |name=rss-urls
   |value=string
   |default=NULL
   |description=Pipe <code>'''{{!}}

''' separated list of `RSS <wikipedia:RSS>`__ and/or `Atom <wikipedia:Atom_(Web_standard)>`__ feed URLs }}

Position
~~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=rss-x
   |value=integer
   |default=0
   |description=X offset, from the left screen edge
   }}

.. raw:: mediawiki

   {{Option
   |name=rss-y
   |value=integer
   |default=0
   |description=Y offset, down from the top
   }}

.. raw:: mediawiki

   {{Option
   |name=rss-position<span id="rss-position"></span>
   |value=integer
   |select=[[#appendix_rss-position|{0, 1, 2, 4, 8, 5, 6, 9, 10}]]
   |default=-1
   |description=You can enforce the text position on the video (0=center, 1=left, 2=right, 4=top, 8=bottom; you can also use combinations of these values, eg 6 = top-right)
   }}

Font
~~~~

.. raw:: mediawiki

   {{Option
   |name=rss-opacity
   |value=integer
   |min=0
   |default=255
   |max=255
   |description=Opacity (inverse of transparency) of overlay text. 0 = transparent, 255 = totally opaque
   }}

.. raw:: mediawiki

   {{Option
   |name=rss-color<span id="rss-color"></span>
   |value=integer
   |select={ 0x000000, 0x808080, 0xC0C0C0, 0xFFFFFF, 0x800000, 0xFF0000, 0xFF00FF, 0xFFFF00, 0x808000, 0x008000, 0x008080, 0x00FF00, 0x800080, 0x000080, 0x0000FF, 0x00FFFF }
   |default=0xFFFFFF
   |description=Color<sup>('''[[#appendix_rss-color|key]]''')</sup> of the text that will be rendered on the video. This must be an hexadecimal (like HTML colors). The first two chars are for red, then green, then blue
   }}

.. raw:: mediawiki

   {{Option
   |name=rss-size
   |value=integer
   |min=0
   |default=0
   |max=4096
   |description=Font size, in pixels. Default is 0 (use default font size)
   }}

Misc
~~~~

.. raw:: mediawiki

   {{Option
   |name=rss-speed
   |value=integer
   |default=100000
   |description=Speed of the RSS/Atom feeds in [[wiktionary:&micro;s|&micro;s]] (bigger is slower)
   }}

.. raw:: mediawiki

   {{Option
   |name=rss-length
   |value=integer
   |default=60
   |description=Maximum number of characters displayed on the screen
   }}

.. raw:: mediawiki

   {{Option
   |name=rss-ttl
   |value=integer
   |default=1800
   |description=Time in seconds between each feed refresh of the feeds. 0 means that the feeds are never updated. 1800 seconds is 30 minutes
   }}

.. raw:: mediawiki

   {{Option
   |name=rss-images
   |value=boolean
   |default=enabled
   |description=Display feed images if available
   }}

.. raw:: mediawiki

   {{Option
   |name=rss-title
   |value=integer
   |select={<var>default_title</var>, <var>hide_title</var>, <var>prepend_title</var>, <var>scroll_title</var>}
   |default=<var>default_title</var>
   |description=Title display mode. 0 is hidden if the feed has an image and feed images are enabled, 1 is always visible, 2 is scroll with feed
   }}

Examples
--------

Example command line use **(VLC 0.9.0 and above)**: (untested with 3.x.x)

``% ``\ **``vlc``\ ````\ ``somevideo.avi``\ ````\ ``--sub-filter=rss``\ ````\ ``--rss-urls="``\ **\ ```http://news.google.com/news?ned=us&topic=h&output=rss`` <http://news.google.com/news?ned=us&topic=h&output=rss>`__\ **\ ``"``**

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/spu/rss.c}}

See also
--------

-  `Documentation:Modules/marq <Documentation:Modules/marq>`__

Appendix
--------

.. raw:: html

   <div class="plainlist">

-  ^ `--rss-color <#rss-color>`__\ 
-  ^ `--rss-position <#rss-position>`__\ 

.. raw:: html

   </div>

.. raw:: mediawiki

   {{Colour mapping}}

.. raw:: mediawiki

   {{Alignment mapping}}

.. raw:: mediawiki

   {{Documentation footer}}
