.. raw:: mediawiki

   {{See also|Documentation:Modules/dvdread}}

.. raw:: mediawiki

   {{Module|name=dvdnav|type=Access demux|first_version=0.7.1|description=[[DVD]] with menus}}

This module uses `libdvdnav <libdvdnav>`__.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=dvdnav-angle
   |value=integer
   |default=1
   |description=Default DVD angle
   }}

.. raw:: mediawiki

   {{Option
   |name=dvdnav-menu
   |value=boolean
   |default=enabled
   |description=Start the DVD directly in the main menu. This will try to skip all the useless warning introductions
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/dvdnav.c}}

.. raw:: mediawiki

   {{Documentation}}
