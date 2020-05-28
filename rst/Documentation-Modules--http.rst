The ``--http-caching`` option was removed prior to VLC 2.0.0 with this commitdiff: DEMUX)_GET_PTS_DELAY}}

The option ``--http-proxy`` was removed from the 3.0.x and 4.0.0-dev branches with this commitdiff: with summary *Because win32/netconf is not ready*.

The option ``--http-user-agent`` changed in VLC 1.1.1 (changelog):

| ```libvlc`` <libvlc>`__\ ``_set_user_agent() configures the "``\ ```user``\ ````\ ``agent`` <wikipedia:User_agent>`__\ ``" strings used for some``
| ``protocols (HTTP, PulseAudio...). This replaces the --http-user-agent and``
| ``the former --user-agent libvlc_new() parameters.``

HTTP
----

.. raw:: mediawiki

   {{Module|name=http|type=Access|first_version=0.5.0|description=[[HTTP]] input|sc=http|sc2=unsv|sc3=<abbr title="iTunes Podcast">itpc</abbr>|sc4=icyx}}

HTTP was first supported *before* 0.5.0 (probably from the beginning).

As of VLC 0.9.0 this module accepts gzip compressed data and Digest Access Authentication.

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=http-reconnect
   |default=disabled
   |description=Automatically try to reconnect in case of a sudden disconnect
   }}

.. raw:: mediawiki

   {{Clear}}

HTTPS
-----

.. raw:: mediawiki

   {{Module|name=https|type=Access|first_version=3.0.0|description=[[HTTPS]] input|sc=https}}

HTTPS was first supported in 0.8.1 (for ). This particular sub-module was introduced in 3.0.0 for HTTP 2.0 support.

.. _options-1:

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=http-forward-cookies
   |value=boolean
   |default=enabled
   |description=Forward cookies across HTTP redirections
   }}

.. raw:: mediawiki

   {{Option
   |name=http-referrer
   |value=string
   |default=NULL
   |description=Provide the referral URL, i.e. HTTP "[[wikipedia:HTTP referer|Referer]]" &#x5B;''[[wiktionary:sic#Usage_notes|sic]]''&#x5D;
   }}

.. raw:: mediawiki

   {{Option
   |name=http-user-agent
   |value=string
   |default=NULL
   |description=Override the name and version of the application as provided to the HTTP server, i.e. the HTTP "[[wikipedia:User agent|User-Agent]]". Name and version must be separated by a forward slash, e.g. "FooBar/1.2.3"
   }}

.. raw:: mediawiki

   {{Option
   |name=http-continuous
   |value=boolean
   |default=disabled
   |description=Keep reading a resource that keeps being updated (for example a JPEG file)
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/http.c}}

   (file - HTTP module)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/http/access.c}}

   (file - HTTPS sub-module)

-  

   .. raw:: mediawiki

      {{VLCSourceFolder|modules/access/http}}

   (folder)

.. raw:: mediawiki

   {{Stub}}

.. raw:: mediawiki

   {{Documentation footer}}
