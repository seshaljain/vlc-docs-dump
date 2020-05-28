.. raw:: mediawiki

   {{Module|name=motion|type=Control interface|first_version=0.9.0|os=Linux|description=motion control interface}}

Use this control interface to rotate the video when moving a laptop using HDAPS or AMS sensors.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=motion-use-rotate
   |default=enabled
   |description=Use the [[Documentation:Modules/rotate|rotate]] video filter instead of the [[Documentation:Modules/transform|transform]] video ouput filter to rotate the video
   }}

Examples
--------

Using the `transform <Documentation:Modules/transform>`__ video output filter (possible rotation angles are -90°, 0° and +90°):

``% ``\ **``vlc``\ ````\ ``--control``\ ````\ ``motion``\ ````\ ``somevideo.avi``**

Using the `rotate <Documentation:Modules/rotate>`__ video filter (possible rotation angles theoretically range from -180° to +180°, depending on your sensor):

``% ``\ **``vlc``\ ````\ ``--control``\ ````\ ``motion``\ ````\ ``--motion-use-rotate``\ ````\ ``--video-filter``\ ````\ ``rotate``\ ````\ ``somevideo.avi``**

.. raw:: mediawiki

   {{Documentation footer}}
