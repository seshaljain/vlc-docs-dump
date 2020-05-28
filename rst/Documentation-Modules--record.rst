.. raw:: mediawiki

   {{Module|name=record|type=Access filter|first_version=0.8.2|description=toggle recording incoming data to disk}}

This access filter will enable recording incoming data to disk when the user presses the r key. Note that this is very unlikely to work for sources using an encapsulation method other than ts.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=record-path
   |value=string
   |default=""
   |description=Directory where recorded that will be stored.
   }}

Example
-------

``% ``\ **``vlc``\ ````\ ``--access-filter``\ ````\ ``record``\ ````\ **

   VLC will toggle recording when you press the r hotkey.

.. raw:: mediawiki

   {{Documentation footer}}
