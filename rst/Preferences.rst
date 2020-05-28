.. raw:: mediawiki

   {{See also|Vlc MacOS VLC Preferences|VSG:ResetPrefs}}

File:ToolsPreferences-Windows 8.png|Location of preferences option|alt= File:Preferences-Windows 8.png|Preferences dialogue under Windows 8|alt= File:Vlcmenu preferences osx.png|Preferences dialogue under macOS|alt=

You can edit settings for VLC by navigating to the menu toolbar, selecting Tools, and selecting Preferences (or by pressing Ctrl+P).

-  To save your preferences, click Save.
-  To show more options, switch the *Show settings* radio button to *All*.

Configuration File
~~~~~~~~~~~~~~~~~~

The preferences stated in the options are stored in a configuration file. There is one configuration file per user, stored at:

-  *Unix, Linux and BSD:* ``~/.config/vlc/vlcrc`` since 0.9. Before it was: ``~/.vlc/vlcrc``
-  *macOS:* ``~/Library/Preferences/org.videolan.vlc/vlcrc``
-  *Windows:* ``%appdata%\vlc\vlcrc`` is generic and is expanded to:

   -  *Windows 95/98/ME:* ``C:\Windows\Application Data\vlc\vlcrc``
   -  *Windows NT/2000/XP:* ``C:\Documents and Settings\``\ \ ``\Application Data\vlc\vlcrc``
   -  *Windows Vista/7/8/10:* ``C:\Users\``\ \ ``\AppData\Roaming\vlc\vlcrc``

-  When used from the command line, sometimes there are unintended conflicts with settings in the config file; to ignore the config file, use: ``--ignore-config``

Your Preferences
----------------

To view/change your Wiki preferences go `here <Special:Preferences>`__.

`Category:Documentation <Category:Documentation>`__
