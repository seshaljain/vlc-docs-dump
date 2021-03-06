.. raw:: mediawiki

   {{Module|name=live555|type=Access demux|description=[[RTP]]/[[RTSP]]/[[SDP]] demuxer (using [[Live555]])|sc=live|sc2=livedotcom}}

The ``--rtsp-caching`` option was removed prior to VLC 2.0.0 with this commitdiff: DEMUX)_GET_PTS_DELAY}}

Options
-------

None.

Submodule
---------

.. raw:: mediawiki

   {{Module|name=live555|type=Access|description=[[RTSP]]/[[RTP]] access and demux|sc=rtsp|sc2=pnm|sc3=live|sc4=livedotcom}}

.. _options-1:

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=rtsp-tcp
   |value=boolean
   |default=disabled
   |description=Use RTP over RTSP ([[TCP]])
   }}

.. raw:: mediawiki

   {{Option
   |name=rtp-client-port
   |value=integer
   |default=-1
   |description=[[Port]] to use for the RTP source of the session
   }}

.. raw:: mediawiki

   {{Option
   |name=rtsp-mcast
   |value=boolean
   |default=disabled
   |description=Force [[multicast]] RTP via RTSP
   }}

.. raw:: mediawiki

   {{Option
   |name=rtsp-http
   |value=boolean
   |default=disabled
   |description=Tunnel RTSP and RTP over [[HTTP]]
   }}

.. raw:: mediawiki

   {{Option
   |name=rtsp-http-port
   |value=integer
   |default=80
   |description=Port to use for tunneling the RTSP/RTP over HTTP
   }}

.. raw:: mediawiki

   {{Option
   |name=rtsp-kasenna
   |value=boolean
   |default=disabled
   |description=Kasenna servers use an old and nonstandard dialect of RTSP. With this parameter VLC will try this dialect, but then it cannot connect to normal RTSP servers
   }}

.. raw:: mediawiki

   {{Option
   |name=rtsp-wmserver
   |value=boolean
   |default=disabled
   |description=WMServer uses a nonstandard dialect of RTSP. Selecting this parameter will tell VLC to assume some options contrary to [https://tools.ietf.org/html/rfc2326 RFC 2326] guidelines
   }}

.. raw:: mediawiki

   {{Option
   |name=rtsp-user
   |value=string
   |default=NULL
   |description=Sets the username for the connection, if no username or password are set in the url
   }}

.. raw:: mediawiki

   {{Option
   |name=rtsp-pwd
   |value=password
   |default=NULL
   |description=Sets the password for the connection, if no username or password are set in the url
   }}

.. raw:: mediawiki

   {{Option
   |name=rtsp-frame-buffer-size
   |value=integer
   |default=250000
   |description=RTSP start frame buffer size of the video track, can be increased in case of broken pictures due to too small buffer
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/live555.cpp}}

.. raw:: mediawiki

   {{Documentation footer}}
