.. raw:: mediawiki

   {{Back to|Hacker Guide}}

Libvlc Startup
--------------

Introduction
~~~~~~~~~~~~

`Libvlc <Libvlc>`__ represents the underlying of . VLC itself is just a wrapper around libvlc. By utilizing libvlc developers can take advantage of all the complex functionalities of vlc. Libvlc is generated as a shared library and can be wrapped up with numerous interfaces, including both Python and Java bindings. This allows the end user to build applications around the vlc code base and take advantage of all the plugins available to vlc instead of writing everything from scratch.

This document will explain how to get started using libvlc. It will step through the instantiation of a libvlc instance and explain the typical startup procedure of libvlc.

Libvlc Instantiation
~~~~~~~~~~~~~~~~~~~~

Libvlc is a singleton. For each application wrapped around libvlc, only one libvlc instance should be running. In order to create an instance of libvlc, you must call ``libvlc_new()``. This function initializes the thread system and allocates a libvlc instance. ``libvlc_new()`` resides in .

``libvlc_new()`` calls ``libvlc_InternalInit()`` which handles command line parsing, loads the module bank, and spawns a number of threads to handle various vlc subsystems. The threads are spawned from inside the function ``playlist_ThreadCreate()``. Below is a list of thread start functions that are run for playlist processing. The threads corresponding to these functions are spawned in the order listed.

-  ``RunPreparse()`` - Perform initial parsing of the playlist
-  ``RunFetcher()`` - load artwork associated with playlist item
-  ``RunControlThread()`` - perform playlist scheduling and playing

See `Playlist <{{#rel2abs:../Playlist}}>`__ for more details.

.. raw:: mediawiki

   {{Hacker_Guide}}

`\* <Category:libVLC>`__
