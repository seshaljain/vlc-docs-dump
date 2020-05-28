This module provided compatibility in accessing `iTunes <iTunes>`__ shares. It was removed with the note:

| ``- Remove broken daap plugin (unmaintained ``\ \ ``wrt``\ \ `` VLC API changes, relies on``
| `` an unmaintained library, probably unable to read content from new itunes,``
| `` ...). Implementations exist in rhythmbox, xmms2 and``
| `` daap-sharp, we should see if a proper lib exists or if we could``
| `` make one``

The library it depended upon was `libopendaap <https://linux.die.net/man/3/libopendaap>`__.

Services discovery
------------------

.. raw:: mediawiki

   {{Module|name=daap|type=Services discovery|first_version=0.8.2|last_version=0.9.?|description=[[wikipedia:Digital Audio Access Protocol|DAAP]] shares|sc=none}}

Options
~~~~~~~

None.

Access
~~~~~~

.. raw:: mediawiki

   {{Module|name=daap|type=Access|first_version=0.8.2|last_version=0.9.?|description=[[wikipedia:Digital Audio Access Protocol|DAAP]] access|sc=none}}

.. _options-1:

Options
^^^^^^^

None.

Source code
-----------

-  `[024fa1c48391bdcff9f3ca3f19f8ebb03a6db1f8] <https://git.videolan.org/?p=vlc/vlc-0.8.git;a=commitdiff;h=024fa1c48391bdcff9f3ca3f19f8ebb03a6db1f8>`__ (introduction)
-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-0.8.git|modules/services_discovery/daap.c}}

-  `[0900f11014557ea895a290d2c1518d739f97a8b6] <https://git.videolan.org/?p=vlc/vlc-0.9.git;a=commitdiff;h=0900f11014557ea895a290d2c1518d739f97a8b6>`__ (removal)

.. raw:: mediawiki

   {{Documentation}}
