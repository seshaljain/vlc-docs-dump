.. raw:: mediawiki

   {{Module|name=gather|type=Stream output|description=Recycle video and audio elementary streams when possible}}

| Makes it possible to stream a `playlist <playlist>`__ without any noticeable interruption on input change on the client side.
| The audio and video streams must all have the same characteristics (codecs, `bit rate <bit_rate>`__, dimensions, etc.). 

Example
-------

``{{%}} ``\ **``vlc``\ ````\ ``playlist.m3u``\ ````\ ``--sout``\ ````\ ``"#gather:std{access=http,mux=asfh,dst=:8080}"``\ ````\ ``--sout-keep``**

If your playlist items use different codecs or have different sizes, it is advised to `transcode <Documentation:Modules/transcode>`__. For example:

``{{%}} ``\ **``vlc``\ ````\ ``playlist.m3u``\ ````\ ``--sout``\ ````\ ``"#transcode{vcodec=DIV3,vb=512,width=640,height=480,acodec=mp3,ab=128,samplerate=44100,channels=2}:gather:std{access=http,mux=asfh,dst=:8080}"``\ ````\ ``--sout-keep``**

It is unclear whether using ``--sout-keep`` automatically sets gather automatically or not http://forum.videolan.org/viewtopic.php?f=14&t=80695

See also `VLC HowTo/Merge videos together <VLC_HowTo/Merge_videos_together>`__

.. raw:: mediawiki

   {{Stub}}

.. raw:: mediawiki

   {{Documentation footer}}
