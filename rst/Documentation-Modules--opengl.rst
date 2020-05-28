This module features conditional compilation: `add_module <https://www.videolan.org/developers/vlc/doc/doxygen/html/vlc__plugin_8h.html#a789d7743e2a12bcaef2f0677a81c5c44>`__ monitors USE_OPENGL_ES2 to determine the [e]xtension through which to use the Open Graphics Library (OpenGL).

More simply, ``gl`` is called for desktop computers and ``gles2`` is called for embedded devices (e.g. smartphones).

Neither conditional module accepts options—\ ``add_glopts ()`` is called in for that purpose.

gles2
-----

.. raw:: mediawiki

   {{Module|name=gles2|type=Video output|first_version=2.0.0|description=OpenGL for Embedded Systems 2 video output|sc=opengles2|sc2=gles2}}

.. raw:: mediawiki

   {{Clear}}

gl
--

.. raw:: mediawiki

   {{Module|name=gl|type=Video output|first_version=0.8.0|description=OpenGL video output|sc=opengl|sc2=gl}}

OpenGL (as a plugin) was first introduced for the `macOS <macOS>`__ port in VLC 0.7.1, made the default for macOS in VLC 0.7.2, and later added for all platforms in VLC 0.8.0.

Source code
-----------

-  Git: (main file)
-  Git: (OpenGL and OpenGL ES output common code)
-  Doxygen: `include/vlc_opengl.h <https://www.videolan.org/developers/vlc/doc/doxygen/html/vlc__opengl_8h_source.html>`__
-  Doxygen: `include/vlc_opengl.c <https://www.videolan.org/developers/vlc/doc/doxygen/html/opengl_8c.html>`__
-  Doxygen: `include/vlc_vout_display.h <https://www.videolan.org/developers/vlc/doc/doxygen/html/vlc__vout__display_8h.html>`__

See also
--------

-  

   .. raw:: mediawiki

      {{docmod|opengl}}

-  

   .. raw:: mediawiki

      {{docmod|glwin32}}

   - module for Windows 32-bit OpenGL

-  

   .. raw:: mediawiki

      {{docmod|glx}}

   - module for Linux X11 OpenGL

External links
--------------

-  `opengl.org <https://opengl.org/>`__
-  `www.khronos.org/opengles <https://www.khronos.org/opengles>`__ - developer page for OpenGL ES
-  Wikibook: `OpenGL Programming <wikibooks:OpenGL_Programming>`__

   -  chapter `OpenGL ES Overview <wikibooks:OpenGL_Programming/OpenGL_ES_Overview>`__

.. raw:: mediawiki

   {{Documentation}}
