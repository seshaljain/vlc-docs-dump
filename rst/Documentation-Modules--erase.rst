.. raw:: mediawiki

   {{See also|Documentation:Modules/logo}}

.. raw:: mediawiki

   {{Module|name=erase|type=Video filter|first_version=0.9.0|description=logo erasing video filter}}

Use this filter to erase a logo (or any given area) from the video.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=erase-mask
   |value=string
   |default=NULL
   |description=[[PNG]] file to use as a mask. The alpha channel only will be used to build the mask
   }}

.. raw:: mediawiki

   {{Option
   |name=erase-x
   |value=integer
   |default=0
   |description=X offset from upper left corner
   }}

.. raw:: mediawiki

   {{Option
   |name=erase-y
   |value=integer
   |default=0
   |description=Y offset from upper left corner.
   }}

Example
-------

``{{$}} ``\ **``vlc``\ ````\ ``--video-filter``\ ````\ ``"erase{mask=logo.png,x=100,y=50}"``\ ````\ ``somevideo.avi``**

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/video_filter/erase.c}}

.. raw:: mediawiki

   {{Documentation footer}}
