.. raw:: mediawiki

   {{Module|name=timeshift|type=Access filter|first_version=0.8.2|last_version=0.9.9|description=enable timeshifting on live streams}}

This access filter will enable timeshifting on live streams. The user will thus be able to pause the stream. Buffered data will be stored in memory for short periods and on the hard drive afterwards.

''' \*\* Warning : the following documentation is deprecated \*\* '''

It is now in the VLC core.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=timeshift-granularity
   |value=integer
   |default=50
   |description=Size of temporary files in MB
   }}

.. raw:: mediawiki

   {{Option
   |name=timeshift-dir
   |value=string
   |description=Directory where temporary files will be stored.
   }}

.. raw:: mediawiki

   {{Option
   |name=timeshift-force
   |default=disabled
   |description=Force use of the timeshift module even if the underlying access claims that it can pause
   }}

Example
-------

``% ``\ **``vlc``\ ````\ ``--access-filter``\ ````\ ``timeshift``\ ````\ **

.. raw:: mediawiki

   {{Documentation footer}}
