.. raw:: mediawiki

   {{See also|Documentation:Modules/erase|VLC HowTo/Add a logo}}

The logo filter can be used to add a logo on the video. This logo can be a static image or series of images which will be displayed alternatively. When used as a video output filter, you can move the logo with the mouse.

Video sub-filter
----------------

.. raw:: mediawiki

   {{Module|name=logo|type=Video sub-filter|description=Logo sub source|sc=logo}}

Video output filter
-------------------

.. raw:: mediawiki

   {{Module|name=logo|type=Video output filter|description=Logo video filter|sc=logo}}

.. raw:: mediawiki

   {{Clear}}

Examples
--------

``{{%}} ``\ **``vlc``\ ````\ ``--video-filter``\ ````\ ``"logo{file=cone.png,opacity=128}"``\ ````\ ``somevideo.avi``**

   This command will display image cone.png in the video's upper right corner with 50% transparency.

``{{%}} ``\ **``vlc``\ ````\ ``--video-filter``\ ````\ ``"logo{file='cone1.png,2000,128;cone2.png,3000'}"``\ ````\ ``somevideo.avi``**

   This command will display image cone1.png for 2 seconds with 50% transparency followed by image cone2.png for 3 seconds at default transparency and loop.

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/spu/logo.c}}

Appendix
--------

.. raw:: html

   <div class="plainlist">

-  ^ `--logo-position <#logo-position>`__\ 

.. raw:: html

   </div>

.. raw:: mediawiki

   {{Alignment mapping}}

.. raw:: mediawiki

   {{Documentation footer}}
