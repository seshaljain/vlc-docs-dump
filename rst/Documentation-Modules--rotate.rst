.. raw:: mediawiki

   {{Module|name=rotate|type=Video filter|first_version=0.9.0|description=rotate video filter}}

Use this filter to rotate the video using any angle you want.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=rotate-angle
   |value=float
   |min=-340282346638528859811704183484516925440.000000
   |max=340282346638528859811704183484516925440.000000
   |default=0
   |description=Rotation angle in degrees (0 to 359)
   }}

.. raw:: mediawiki

   {{Option
   |name=rotate-use-motion
   |value=boolean
   |description=Use HDAPS, AMS, APPLESMC or UNIMOTION motion sensors to rotate the video
   |default=disabled
   }}

Example
-------

``% ``\ **``vlc``\ ````\ ``--video-filter``\ ````\ ``"rotate{angle=123}"``\ ````\ ``somevideo.avi``**

See also
--------

-  `Documentation:Modules/motion_control <Documentation:Modules/motion_control>`__

.. raw:: mediawiki

   {{Documentation footer}}
