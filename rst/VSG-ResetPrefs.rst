Many problems with VLC are due to incorrect settings or a broken plugin cache. You can solve these by deleting VLC's `preferences <preferences>`__ and cache.

Reset preferences from VLC
--------------------------

Using VLC within preferences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you can launch VLC, in the preferences dialog, from the Tools menu, you can hit the "Reset preferences" button.

**NB:** This might not solve all your issues, all the time; so if you still have issues, then see the rest of this article.

Reset preferences and cache
---------------------------

Windows
~~~~~~~

Using the shortcut in the start menu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you installed VLC properly you can delete the preferences and cache by simply opening the shortcut you can find in your start menu:

*All programs > VideoLAN > Reset VLC media player preferences and cache files*

Deleting the files manually
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open the explorer and type *%APPDATA%* into the address bar and hit enter. This should lead you to the AppData folder of your user.

Therein you should find a folder named *vlc*. Delete that folder and you're done. |Windows_Deleting_Prefs_Folder.png|

macOS
~~~~~

Using VLC
^^^^^^^^^

In case VLC still launches, open it. Select "VLC" menu -> "Preferences" and hit "Reset All" in the bottom left corner. VLC will ask for confirmation, reset and restart itself.

Manual deletion
^^^^^^^^^^^^^^^

1) Quit the VLC application.

2) Use a Terminal and enter the following command: *defaults delete org.videolan.vlc*

3) Remove everything from ~/Library/Preferences called "org.videolan.vlc.*". Use "Go To Folder" within the Finder's "Go" menu to show this folder.

GNU/Linux
~~~~~~~~~

Delete the ``~/.config/vlc`` and ``~/.cache/vlc`` folders or execute **vlc --reset-config** in a terminal.

*Old versions of VLC had the data stored in ``~/.vlc``*

BeOS
~~~~

Delete the ``config/settings/vlcrc`` folders.

iOS
~~~

Delete the app from SpringBoard and re-download it from the App Store to fully reset the media library and settings.

Android
~~~~~~~

From the settings
^^^^^^^^^^^^^^^^^

In *Settings*, go to *Applications* → *VLC* → **Clear data**.

Within the application
^^^^^^^^^^^^^^^^^^^^^^

Go to *Preferences* → *Other* to clean the history and the media database.

See also
--------

-  `VLC HowTo <VLC_HowTo>`__
-  `VLC Support Guide <VSG:Main>`__

`Category:How To <Category:How_To>`__

.. |Windows_Deleting_Prefs_Folder.png| image:: Windows_Deleting_Prefs_Folder.png

