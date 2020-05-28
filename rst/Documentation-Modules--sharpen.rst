.. raw:: mediawiki

   {{Module|name=sharpen|type=Video filter|first_version=0.9.0|description=sharpening video filter}}

Use this filter to sharpen the video.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=sharpen-sigma
   |value=float
   |default=0.05
   |description=Sharpen strength (0. to 2.)
   }}

Example
-------

``% ``\ **``vlc``\ ````\ ``--video-filter``\ ````\ ``"sharpen{sigma=0.12}"``\ ````\ ``somevideo.avi``**

See also
--------

-  `Documentation:Modules/gaussianblur <Documentation:Modules/gaussianblur>`__

.. raw:: mediawiki

   {{Documentation footer}}
