.. raw:: mediawiki

   {{Module|name=display|type=Stream output|description=Display stream output|sc=display}}

Options
-------

.. raw:: mediawiki

   {{Option
   |name=sout-display-audio
   |value=boolean
   |default=enabled
   |description=Enable audio rendering.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-display-video
   |value=boolean
   |default=enabled
   |description=Enable video rendering.
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-display-delay
   |value=integer
   |default=100
   |description=Introduces a delay (ms) in the display of the stream.
   }}

Examples
--------

| `Transcode <Transcode>`__ and stream a file while displaying it locally.
| This will display the transcoded version:

``% ``\ **``vlc``\ ````\ ``somevideo.avi``\ ````\ ``--sout``\ ````\ ``"#transcode{vcodec=mp2v,vb=2048,acodec=mpga,ab=96}:duplicate{dst=std{access=udp,mux=ts{ttl=12},url=239.255.1.1},dst=display}"``**

This will display the original version:

``% ``\ **``vlc``\ ````\ ``somevideo.avi``\ ````\ ``--sout``\ ````\ ``"#duplicate{dst='transcode{vcodec=mp2v,vb=2048,acodec=mpga,ab=96}:std{access=udp,mux=ts{ttl=12},url=239.255.1.1}',dst=display}"``**

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/stream_out/display.c}}

See also
--------

-  `Documentation:Modules/duplicate <Documentation:Modules/duplicate>`__

.. raw:: mediawiki

   {{Documentation footer}}
