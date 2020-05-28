.. raw:: mediawiki

   {{Module|name=sdl|type=Video output|last_version=2.2.8|description=[[wikipedia:Simple DirectMedia Layer|SDL]] video output}}

.. raw:: mediawiki

   {{Historical}}

This module had a single shortcut: ``sdl``. Information on this page was `adapted <https://git.videolan.org/?p=vlc/vlc-1.1.git;a=blob;f=modules/video_output/sdl.c;h=beb01eff60081b4b1e8f6872a132fa30ee21359b;hb=HEAD>`__ from the 1.1 branch of vlc.git. ``sdl-video-driver`` was marked as deprecated since 1.1.0.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=sdl-chroma
   |value=string
   |description=Force the SDL renderer to use a specific chroma format instead of trying to improve performances by using the most efficient one
   }}

.. raw:: mediawiki

   {{Option
   |name=sdl-video-driver
   |value=string
   |description=Force a specific SDL video output driver
   }}

.. raw:: mediawiki

   {{Documentation}}
