.. raw:: mediawiki

   {{Module|name=colorthres|type=Video filter|first_version=0.9.0|description=Turn the picture black and white except for some colors}}

This filters turns most of the picture black and white except for some colors. This could be called a "Schindler's List" effect.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=colorthres-color
   |value=integer
   |default=0xFF0000 (red)
   |description=Colors similar to this will be kept, others will be grayscaled.
   }}

.. raw:: mediawiki

   {{Option
   |name=colorthres-saturationthres
   |value=integer
   |default=20
   |description=Saturation threshold
   }}

.. raw:: mediawiki

   {{Option
   |name=colorthres-similaritythres
   |value=integer
   |default=15
   |description=Similarity threshold
   }}

Example
-------

``% ``\ **``vlc``\ ````\ ``--video-filter``\ ````\ ``colorthres``\ ````\ ``somevideo.avi``**

See also
--------

-  `Schindler's List, Red dress <http://en.wikipedia.org/wiki/Image:Schindlers_list_red_dress.JPG>`__ on wikipedia

.. raw:: mediawiki

   {{Documentation footer}}
