.. raw:: mediawiki

   {{Module|name=gaussianblur|type=Video filter|first_version=0.9.0|description=gaussian blur video filter}}

Use this filter to blur the whole video.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=gaussianblur-sigma
   |value=float
   |default=2.
   |description=The gaussian's standard deviation.
   }}

Example
-------

``% ``\ **``vlc``\ ````\ ``--video-filter``\ ````\ ``"gaussianblur{sigma=3.45}"``\ ````\ ``somevideo.avi``**

See also
--------

-  `Documentation:Modules/sharpen <Documentation:Modules/sharpen>`__

.. raw:: mediawiki

   {{Documentation footer}}
