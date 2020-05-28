.. raw:: mediawiki

   {{Module|name=marq|type=Video sub-filter|first_version=0.8.0|description=Overlays text on the video|sc=marq|sc2=time}}

The *marq* subtitle filter can be used to display text on a video. The filter was merged with this filter in version 0.9.0, adding time `format string <Documentation:Format_String>`__ recognition. There are two methods of specifying position: coordinate and (since VLC 0.9.0) `numbered positions <#marq-position>`__.

Options
-------

Position
~~~~~~~~

Font
~~~~

transparent, 255 {{=}} totally opaque. }}

Misc
~~~~

Examples
--------

Versions 2.0 and later
~~~~~~~~~~~~~~~~~~~~~~

Example command line use **(VLC 2.0.0 and newer)**:

``{{%}} vlc '--sub-source=marq{marquee="%Y-%m-%d,%H:%M:%S",position=9,color=0xFFFF00,size=12}' somevideo.avi``

This example displays the current date and time in yellow in the top left corner of video.

The equivalent long form would be;

``{{%}} vlc --sub-source=marq --marq-marquee="%Y-%m-%d,%H:%M:%S" --marq-position=9 --marq-color=0xFFFFFF --marq-size=12 somevideo.avi``

Versions 0.9.0 to 1.1.13
~~~~~~~~~~~~~~~~~~~~~~~~

``{{$}} vlc --sub-filter 'marq{marquee=$t ($P%%),color=0xFFFF00}:marq{marquee=%H:%M:%S,position=6}' somevideo.avi``

| This command line will show the stream's title (``$t``) and current position (``$P``) in the upper left corner and the current time in the upper right corner. The \ *single*\  quotes ``'`` enclose our ``$`` characters to prevent them from being interpreted as Bash variables.
| On Windows the command line would be:

\ `` ``\ \ `` --sub-filter=marq{marquee=$t ($P%%),color=0xFFFF00}:marq{marquee=%H:%m%s,position=6} somevideo.avi``

Gallery
-------

File:Marq demonstration - VLC 3.0.6 Linux.png|Marq can be chained, allowing several marquees to be displayed at the same time.|alt=Marq can be chained, allowing several marquees to be displayed at the same time. Nine positions and text colours are shown against a black background.

See also
--------

-  `Documentation:Format String <Documentation:Format_String>`__
-  `Documentation:Modules/rss <Documentation:Modules/rss>`__

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/spu/marq.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-0.8.git|modules/video_filter/marq.c}}

Appendix
--------

.. raw:: html

   <div class="plainlist">

-  ^ `--marq-color <#marq-color>`__\ 

.. raw:: html

   </div>

.. raw:: mediawiki

   {{Colour mapping}}

.. raw:: mediawiki

   {{Documentation footer}}
