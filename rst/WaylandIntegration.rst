Due to fundamental differences between X11 and Wayland protocols, the exact work split between video output (render) and video window provider (GUI) must change in Wayland. We need to define the interface between output and window plugins, and the LibVLC interface for video embedding in external apps.

Most particularly, nested windows (i.e. subsurfaces) must use the same display connection as their parent. Nesting windows or manipulating windows across multiple display connections is not allowed in Wayland. Thus the wl_display pointer must be shared between the UI and the video output.

A subsurface will be created for the video output to render into.

Video window
------------

-  Connects to the Wayland compositor.
-  Runs the Wayland display connection main loop.
-  Provides the wl_display pointer to the video output.
-  Provides a wl_surface pointer to the video output.

Video output
------------

-  Must not access the Wayland display connection socket directly.
-  May create its own event queue (or more) on the same Wayland display connection.
-  Attaches a buffer of adequate size to the surface.

Open issues
-----------

Subsurface
~~~~~~~~~~

The video output will typically render into a subsurface of the GUI. Which component should talk to the subcompositor and create the subsurface?

Video size
~~~~~~~~~~

Unlike X11, the size of a surface cannot be specified externally; it is always equal to the size of the content of the surface. How should the application supply the desired size to the video output?

Synchronized mode
~~~~~~~~~~~~~~~~~

Should the video output support synchronized mode for the subsurface? If so, how shall the application be notified of an updated surface content (i.e. new video frame):

-  (advance) render callback with desired play time stamp?
-  (advance) render callback and (on-time) display callback?
-  (on-time) display callback only?

See also
--------

Similar issues affect EGL. The EGL Wayland platform API may be used as a source of inspiration.

`Category:Dev Discussions <Category:Dev_Discussions>`__
