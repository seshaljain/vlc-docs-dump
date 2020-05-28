.. raw:: mediawiki

   {{Module|name=extract|type=Video filter|first_version=0.9.0|description=extract a color component from the video}}

.. raw:: mediawiki

   {{Option
   |name=extract-component
   |value=integer
   |default=0xFF0000 (red)
   |description=Color component to extract (0xRRGGBB)
   }}

Example
-------

Extract the yellow component from a video:

``% ``\ **``vlc``\ ````\ ``--video-filter``\ ````\ ``"extract{component=0xFFFF00}"``\ ````\ ``somevideo.avi``**

Typical use
-----------

You can create a live Andy Warhol display.

.. raw:: mediawiki

   {{Stub}}

.. raw:: mediawiki

   {{Documentation footer}}
