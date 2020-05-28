.. raw:: mediawiki

   {{Howto|make VLC the default media player}}

Windows
-------

   *See also:*\ `How to associate media files with VLC <Windows#How_to_associate_media_files_with_VLC>`__.

XP
~~

The simplest way to set VLC as the default media player for Windows is `during installation of VLC <Documentation:Play_HowTo/Installing_VLC>`__. During set-up, VLC will ask you if you want to associate certain media file types (such as .mp3, .flv, .wav) with VLC; for each "association" chosen opening that file type will launch it in VLC. By default, all are selected, though you might (or might not) want to un-check file types you'd like to open with another programme.

| If you've missed this chance at making it the default media player during set-up, perhaps the easiest way is to un-install it and then install it again.
| A word of caution regarding re-installation—be sure to un-check the box that deletes your preferences and cache, or all your customisations will be gone!

Vista, 7, 8
~~~~~~~~~~~

Open VLC player, click on **Tools** in the menu, and from there select **Preferences**.

.. figure:: ToolsPreferences-Windows_8.png
   :alt: ToolsPreferences-Windows_8.png

   ToolsPreferences-Windows_8.png

Click on the **Interface** button on the left panel and then click on **Set up associations...** (it's close to the bottom).

.. figure:: Preferences-Windows_8.png
   :alt: Preferences-Windows_8.png

   Preferences-Windows_8.png

Select *types of files* from the list that appears. Check any file types for which you want VLC to be the default player, or just check the *select all* option.

.. figure:: set-programme-associations.png
   :alt: set-programme-associations.png

   set-programme-associations.png

Mac
---

Right-click on the type of file you want to always open with VLC. Click 'Get Info'. In the 'Open With' section, select VLC from the drop-down menu. To apply this change to all files of this type, click the 'Change All' button.

For optical media, like CDs or DVDs, go to Apple -> System Preferences and choose "CDs/DVDs" in the Hardware section. Choose "Other Application" from the respective popup menu button. The list is alphabetical, so VLC should be near the bottom of the list.

Linux
-----

Fedora
~~~~~~

GNOME
^^^^^

| Gnome uses two lists (located at **/usr/share/applications/**) – **mimeinfo.cache** and **defaults.list** – to register applications to file types.
| You can either edit these manually or use the tools that GNOME has for this.

Instructions on how to do it in GNOME
'''''''''''''''''''''''''''''''''''''

Changing the default application for videos using menus (the easy way):
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

| Using Nautilus 2.30.1, from the top menu bar choose "Places", then Home Folder -> Edit menu -> Preferences -> choose Media tab -> and in the drop-down list next to "DVD Video" choose "Open VLC media player".
| Voilà.

Alternatively, try: System -> Preferences -> Personal -> Preferred Applications -> Multimedia -> Custom -> Type this: vlc %U

(P.S.: this alternative hasn't been tested yet).

Changing the default application for videos using menus (the not-so-easy way):
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

=========================================================================================================================================
-  Right-click on the video file that you want VLC to open by default.
-  Choose properties.
-  Now in the properties window, click on the tab named **Open With**.

https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Properties_window.png/800px-Properties_window.png
| 
| \* In the tab **Open With** just choose VLC as your player for that type of file.

   Just remember that you will have to do this *for each and every type of video/audio file* (e.g., mpg, avi, rm, mkv, ogg, mp3, etc.)

https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Open_with_tab.png/800px-Open_with_tab.png
| 
| \* If the VLC icon doesn't show up on the **Open With** tab, click on the **add** button in the lower corner to the right of the window
| that has a plus sign, and locate VLC on the window that pops up that is called *Add Application*.
| https://upload.wikimedia.org/wikipedia/commons/5/51/Add_app.png
=========================================================================================================================================

Changing the default application for videos manually (the hard way):
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

| In Fedora 10 the path /usr/share/applications/ will take you to these 2 files that configure what application opens a type of file.
| **defaults.list**
| **mimeinfo.cache**
| P.S.: Both files will point to a Desktop Entry file ([name of the file].desktop) that is inside the *applications* folder, and the 2 important things inside that file are the configurations for what MIME Types the application can handle, and how to launch the application.

| A *Desktop Entry* file is a data file that provides information about an item in a menu. The desktop entry specification describes desktop entries as files describing information about an application such as the name, MIME Types it handles, icon, and description. These files are used for application launchers and for creating menus of applications that can be launched.
| If you don't have the VLC *Desktop Entry* file, or it disappears for some reason you will have to make one. Look `here <http://library.gnome.org/admin/system-admin-guide/stable/menustructure-desktopentry.html.en>`__ for some pointers.
| You only need to modify **mimeinfo.cache**, I hope. It works for me. If it doesn't work for you, please edit this!
| So what you have to do is:

#. Open *mimeinfo.cache* as root.
#. Search for the MIME Types for video.
#. Change all of them to use VLC.

| For example:
| Registry of MIME Type (video/quicktime) in *mimeinfo.cache* to use VLC.
| video/quicktime=livna-vlc.desktop;totem.desktop;miro.desktop;
| The format is:
| [MIME Type]=[Name of the Desktop Entry file]
| **Note:** You can put more than one *Desktop Entry*, but they need to be separated by a semi-colon (;), see the example above.
| Those extra entries will appear as options when you right-click on the video file and go to the *Open With* submenu.
| **Tip:** Nautilus don't show the real names of the *Desktop Entry* files. Either drag and drop it on gedit so you see the name on the tab, or use **ls** to list the files on the command line.

References
''''''''''

-  `Desktop Entry Files <http://library.gnome.org/admin/system-admin-guide/stable/menustructure-desktopentry.html.en>`__
-  `Registering Applications for MIME Types <http://library.gnome.org/admin/system-admin-guide/stable/mimetypes-registering.html.en>`__ (Editing defaults.list and mimeinfo.cache)

KDE
^^^

[TODO]
