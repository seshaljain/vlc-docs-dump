.. raw:: mediawiki

   {{Historical}}

WxWidgets was the default, plain, graphical, `interface <interface>`__ to VLC, made using the `WxWidgets <http://www.wxwidgets.org>`__ library (Linux users may need to have this installed). It was used as the default interface on the `Windows <Windows>`__ and `Linux <Linux>`__ versions of VLC and have been replaced by the `Qt Interface <Qt_Interface>`__ since 0.9.0.

It is known as the "wx" interface, so you can (or was able to) force this by running

``vlc ``\ **``-I``\ ````\ ``wx``**

If WxWidgets is not available, it will probably revert to using the `rc <Console>`__ (console) interface, even if you force it. The most likely reason for this is if WxWidgets hasn't been installed, or if it wasn't linked in (using the ./configure). See `compiling VLC <compiling_VLC>`__ `1 <http://developers.videolan.org/vlc/>`__ for information on compiling.

`Category:Interfaces <Category:Interfaces>`__
