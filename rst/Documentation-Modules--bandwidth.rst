.. raw:: mediawiki

   {{Module|name=bandwidth|type=Access filter|first_version=0.9.0|description=limit incoming bandwidth}}

Options
-------

.. raw:: mediawiki

   {{Option
   |name=access-bandwidth
   |value=integer
   |default=65536
   |description=The bandwidth module will drop any data in excess of that many bytes per seconds
   }}

Example
-------

``% ``\ **``vlc``\ ````\ ``--access-filter``\ ````\ ``bandwidth``\ ````\ ``--access-bandwidth``\ ````\ ``131072``\ ````\ **

   Will limit incoming data to 128 kBytes/second (128*1024 Bytes/second).

.. raw:: mediawiki

   {{Stub}}

.. raw:: mediawiki

   {{Documentation footer}}
