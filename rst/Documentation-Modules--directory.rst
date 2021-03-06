.. raw:: mediawiki

   {{Module|name=directory|type=Access|description=recursively add files from a directory into the playlist}}

Options
-------

.. raw:: mediawiki

   {{Option
   |name=recursive
   |value=string
   |default="expand"
   |description=Specify behavior when dealing with subdirectories. Can be "ignore" to ignore sub directories, "collapse" to add sub directories without expanding them and "expand" to add sub directories and expand them
   }}

.. raw:: mediawiki

   {{Option
   |name=ignore-filetypes
   |value=string
   |default="m3u,db,nfo,jpg,gif,sfv,txt,sub,idx,srt,cue"
   |description=Comma seperated list of file extensions to ignore when adding directory items to the playlist
   }}

Example
-------

Open a directory:

``% ``\ **``vlc``\ ````\ ``directory:///path/to/dir``**

You can also use:

``% ``\ **``vlc``\ ````\ ``/path/to/dir``**

or

``% ``\ **``vlc``\ ````\ ``dir:///path/to/dir``**

or even

``% ``\ **``vlc``\ ````\ **\ ```file:///path/to/dir`` <file:///path/to/dir>`__

.. raw:: mediawiki

   {{Stub}}

.. raw:: mediawiki

   {{Documentation footer}}
