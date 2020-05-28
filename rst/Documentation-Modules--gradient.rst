.. raw:: mediawiki

   {{Image requested}}

.. raw:: mediawiki

   {{Module|name=gradient|type=Video filter|first_version=0.9.0|description=apply gradients and edge detection filters}}

Use this filter to apply gradients or do simple edge detection algorithms to the video image.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=gradient-mode
   |value=string
   |default=gradient
   |description=One of "gradient", "edge" or "hough".
   }}

.. raw:: mediawiki

   {{Option
   |name=gradient-type
   |value=integer
   |default=0
   |description=0 to discard colors, 1 to keep colors.
   }}

.. raw:: mediawiki

   {{Option
   |name=gradient-cartoon
   |default=enabled
   |description=Apply a cartoon effect.
   }}

Example
-------

``% ``\ **``vlc``\ ````\ ``--video-filter``\ ````\ ``"gradient{type=1}"``\ ````\ ``somevideo.avi``**

Screenshots
-----------

http://photos.cellerier.net/d/406-1/vlcsnap-8120371.png http://photos.cellerier.net/d/397-1/vlcsnap-10589245.png

**Note:** In versions prior to 0.9.0, this was part of the `distort <Documentation:Modules/distort>`__ video filter.

.. raw:: mediawiki

   {{Documentation footer}}
