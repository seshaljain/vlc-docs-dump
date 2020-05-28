.. raw:: mediawiki

   {{Module|name=projectm|type=Visualization|first_version=1.1.0|description=libprojectM effect}}

Additional module options ``--projectm-preset-path``, ``--projectm-title-font`` and ``--projectm-menu-font`` `will not be used <wikipedia:Conditional_compilation>`__ if VLC can find font paths.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=projectm-width
   |value=integer
   |default=800
   |description=The width of the video window, in pixels
   }}

.. raw:: mediawiki

   {{Option
   |name=projectm-height
   |value=integer
   |default=500
   |description=The height of the video window, in pixels
   }}

.. raw:: mediawiki

   {{Option
   |name=projectm-meshx
   |value=integer
   |default=32
   |description=The width of the mesh, in pixels
   }}

.. raw:: mediawiki

   {{Option
   |name=projectm-meshy
   |value=integer
   |default=24
   |description=The height of the mesh, in pixels
   }}

.. raw:: mediawiki

   {{Option
   |name=projectm-texture-size
   |value=integer
   |default=1024
   |description=The size of the texture, in pixels
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/visualization/projectm.cpp}}

.. raw:: mediawiki

   {{Documentation footer}}
