   *Were you looking for , the current module?*

.. raw:: mediawiki

   {{Module|name=Crop|type=Video filter|last_version=2.0.9|description=Remove borders of the video and replace them with black borders}}

Options
-------

Note
----

This must be a typo. Despite the `claim of a range of ``0-255`` <https://git.videolan.org/?p=vlc.git;a=blob;f=modules/video_filter/crop.c;h=2584780d98bb8527f9aacf540721a4ed5b852833;hb=c638a67c52980404d2aa6f6851b455743a898820#l97>`__ in the help text for the ``--autocrop-luminance-threshold`` option, `the call <https://git.videolan.org/?p=vlc.git;a=blob;f=modules/video_filter/crop.c;h=2584780d98bb8527f9aacf540721a4ed5b852833;hb=c638a67c52980404d2aa6f6851b455743a898820#l129>`__ to ```add_integer_with_range`` <https://git.videolan.org/?p=vlc.git;a=blob;f=include/vlc_configuration.h;h=bdbb11026492436f7f7297e096a8c62f8e899b68;hb=c638a67c52980404d2aa6f6851b455743a898820#l344>`__ would have limited this to effectively ``0-128``.

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-2.0.git|modules/video_filter/crop.c}}

.. raw:: mediawiki

   {{Documentation}}
