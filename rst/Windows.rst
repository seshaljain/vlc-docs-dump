.. raw:: mediawiki

   {{Languages}}

The **Windows port** of VLC usually starts up with the `Qt <Qt>`__ interface which is used in the `Linux <Linux>`__ one as well. The user can decide to use the `Skins <Skins>`__ interface instead to be able to modify the interface according to his or her mood. |Main window|

Frequently Asked Questions
--------------------------

There are some user-maintained FAQs (as distinct from the official VLC FAQ that may be found `here <https://www.videolan.org/support/faq.html>`__):

-  `Version 2.1 and newer <WindowsFAQ-2.1.x>`__
-  `Version 2.0.x <WindowsFAQ-2.0.x>`__
-  `Version 1.1.x <WindowsFAQ-1.1.x>`__
-  `Version 1.0.x <WindowsFAQ-1.0.x>`__
-  `Version 0.9.x <WindowsFAQ-0.9.x>`__
-  `Version 0.8.x <WindowsFAQ-0.8.x>`__

Keyboard shortcuts in the Windows (DirectX) video output
--------------------------------------------------------

.. raw:: mediawiki

   {{See also|QtHotkeys|How to set global hotkeys}}

Note: these shortcuts are only default settings and can be customized (along with many others). To tweak hotkeys settings, go to Settings->Preferences->Interface->Hotkeys settings

============================ ========================
F                            Fullscreen
Space                        Play/Pause
T                            Show position (time)
S                            Stop
Ctrl+Q                       Quit
+/-                          Faster/Slower
N/P                          Next/Previous
Shift+Left/Shift+Right       Jump very short
Alt+Left/Alt+Right           Jump short
Ctrl+Left/Ctrl+Right         Jump medium
Ctrl+Alt+Left/Ctrl+Alt+Right Jump long
Ctrl+Up/Ctrl+Down            Volume up/down
M                            Mute
Ctrl+M                       Show DVD-menu
| Left/Right                 DVD-menu navigation keys
| Up/Down                   
| Enter                     
============================ ========================

How to store streaming station presets
--------------------------------------

To use VLC as a streaming client, store your station presets under the Media Library on the Playlist panel (*not* the bookmarks and *not* the actual playlist itself).

#. Open the playlist panel (Ctrl-L or click on the Playlist button).
#. Click on the Plus button at the bottom of the panel. (A dropdown menu will appear.)
#. Select "Advanced Open" from the dropdown menu. (A new panel, named Open Media, will appear.)
#. Select the "Networking" tab on the Open Media panel.
#. Enter the full URL of the streaming station in the Address field. e.g. http://mystation.org:8000/mystream.ogg
#. Click the Enqueue button at the bottom of the panel.

How to associate media files with VLC
-------------------------------------

.. raw:: mediawiki

   {{See also|VLC HowTo/Make VLC the default player#Windows}}

This should be done through the VLC settings interface, choose "Tools \| Preferences " and then click on the "Set up Associations..." button. Select any file extension that you wish to open with VLC, then click "Apply". This should change all media files icons to the VLC cone, and double-clicking any of them should open VLC and immediately start playing the media.

If this seems to have no effect on the UI, and/or double-clicking the file icon does not start VLC, check that you have correctly set Windows preferences through "Start \| Default Programs" (on Vista; see the relevant item on Windows XP or newer Windows OS; possibly this is not applicable to Windows 2000). In that UI click on "Set default programs", select the "VLC media player" item and check the description (it will usually say "All default settings for this program are active"). Then choose your own course of actions by either clicking on "Set this program as default" or "Choose default settings for this program".

Other ways to achieve the same effects are as follows (not really recommended).

Use Windows Explorer's context menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. In Windows Explorer, *right*-click a file you wish to open.
#. Click "Open With" in the context menu that pops up.
#. Click "VLC media player" to use VLC just this once, or click "Default program..."
#. Click the name of the program (VLC) which you want to be used to open the file.

   -  If VLC is not displayed, click Browse to locate it on your hard drive.

Alternatively:

#. In Windows Explorer, *right*-click the file you want to open with VLC.
#. Click Properties in the context menu that pops up.
#. On the General tab, click Change.
#. Click the name of the program (VLC) which you want to be used to open the file.

Either of these options affects all files that have the same filename extension (the letters after the filename's period) as the file you selected. For example, if you change the program that opens *goober.avi*, then all *.avi* files will be opened with VLC.

Rerun the installer
~~~~~~~~~~~~~~~~~~~

#. Reinstall VLC and choose the "associate files" option when it comes up. \ **Please note**\  that on Vista and newer systems this will not cure the 'Windows Media Player won't go away' symptom, and you should go the "Set default program" route instead, as described above.

Edit the registry
~~~~~~~~~~~~~~~~~

**Warning**: this instruction set is outdated and should *not* be used. Direct registry editing should be avoided anyway unless you're desperate and you really *really* know what you're doing.

**Warning**: use this technique only if you really know what you are doing! And be sure to back-up your registry first.

#. Open a text editor, like Notepad (but not WordPad).
#. Copy this text below.
#. Modify the strings ``C:\\Program Files\\VideoLAN\\VLC\\vlc.exe`` to match your VLC installation.
#. Save as *vlc.reg*.
#. Execute *vlc.reg* (adding this data to your registry).
#. Enjoy VLC :)

Text to copy:

.. code:: ini

   Windows Registry Editor Version 5.00

   [HKEY_CLASSES_ROOT\.ASF]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\.ASX]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\.AVI]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\.DIVX]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\.MPEG]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\.MPG]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\.VOB]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\.WMV]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\VlcFile]
   @="VLC File"

   [HKEY_CLASSES_ROOT\VlcFile\DefaultIcon]
   @="C:\\Program Files\\VideoLAN\\VLC\\vlc.exe,0"

   [HKEY_CLASSES_ROOT\VlcFile\shell\Open]
   [HKEY_CLASSES_ROOT\VlcFile\shell\Open\command]
   @="C:\\Program Files\\VideoLAN\\VLC\\vlc.exe \"%L\""

**Note**: This associates *asf*, *asx*, *avi*, *divx*, *mpeg*, *mpg*, *vob* and *wmv* files. If you get the idea, you can associate any file you want.

How To Start VLC Server with http Interface
-------------------------------------------

VLC ships with a little HTTP server integrated. It is used both to stream using HTTP, and for the HTTP remote control interface.

Step 1: VLC Server Preferences Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Set up the http interface details in the VLC server application: Open VLC, then select Tools > Preferences. In the bottom left corner of the window, under "Show settings", click "All".
#. In the left-hand menu click on the + button next to Interface. This will display three choices: Control interfaces, Hotkeys settings, and Main Interfaces. Click "Main Interfaces". Select "HTTP remote control interface".
#. Click on the plus button next to "Main interfaces". This will display four settings: HTTP, Qt, RC, and Skins. Click on HTTP to display the "HTTP remote control interface" settings.
#. Host address: Address and port the HTTP will listen on, defaults to 0.0.0.0:8080. Set to 127.0.0.1 (a.k.a. localhost) if you want only the local machine.
#. Source directory: If you have installed VLC in a different folder than the default, enter **path\to\VLC\\**\\http.
#. If you are NOT using handlers or SSL certificates the setup is complete.
#. Click on the Save button in the lower right hand of the window.
#. If needed, edit the .hosts file in the vlc/http directory. By default only "localhost" is allowed, edit to enable other hosts.
#. Exit and restart VLC

Step 2: Command Line Startup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The VLC application can be run in a server or client environment. For complicated video and audio streaming on a LAN, one should consider dedicating a machine to act as the VLC server.

To start the VLC application in a server mode with the http interface automatically set, use the following command line in your desktop shortcut. This assumes the default location for installation was selected.

``{{%}} "C:\Program Files\VideoLAN\VLC\vlc.exe" --extraintf http --intf wx``

Step 3: Testing the Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From another computer, connect to the VLC server computer using your browser to the URL

http://server_ip_address:8080, such as http://192.168.0.186:8080

The Main VLC Interface page will be displayed,

See `Web Interface <Web_Interface>`__ for additional information

VLC Plugin for Internet Explorer
--------------------------------

This section will provide guidelines to incorporate the VLC ActiveX plugin to be used to view streaming audio and video from a VLC server.

-  How to embed the ActiveX Plugin in a Web Page: `ActiveX/HTML <ActiveX/HTML>`__
-  Supported ActiveX Function Calls: `ActiveX <ActiveX>`__

VLC Plugin for Firefox (Mozilla)
--------------------------------

.. raw:: mediawiki

   {{See also|Plugins/Mozilla}}

Install
~~~~~~~

There are at least two ways to install the VLC Mozilla Plugin. One way is to to check the "Install Firefox Plugin" when you install VLC.

If the standard exe installation does not install the mozilla plugin directory, then download zip version which includes the required data, and continue with the next installation (2nd way of installing of the plugin)

The second way involves several steps:

#. Quit Firefox or Mozilla
#. Copy the two files in ``VLC_Installation_folder\mozilla`` (usually ``C:\Program Files\VideoLAN\VLC\mozilla``) to your mozilla plugins directory (Usually ``C:\Program Files\Mozilla\plugins`` or ``C:\Program Files\Mozilla Firefox\plugins``).
#. Restart Firefox or Mozilla

Use the Mozilla plugin
~~~~~~~~~~~~~~~~~~~~~~

If in the browser you open a link to an audio or video URL handled by the VLC plugin, or if a web page has HTML code that embeds audio or video handled by the VLC plugin, then the plugin should start and play the audio/video. Note the plugin (as of version 1.1.9) does not present any user interface — it has no default control panel and no keyboard shortcuts.

To get the list of the media types handled by the VLC plugin, browse to about:plugins. Conflicts will arise if you have more than one plugin installed that supports the same media type.

See the `Web plugin documentation <Documentation:WebPlugin>`__ to create HTML pages that use JavaScript to control the plugin.

More example code, as well as a working implementation using JavaScript, XHTML, and PHP that auto-detects browsers (the code is good, but the stream doesn't work) can be found at https://web.archive.org/web/20170830175009/http://altair.videolan.org:80/~dionoea/vlc-plugin-demo/

Portable VLC
------------

| A version of VLC in a portable format exists. It is useful, for example, if you want to put it on a USB stick and use it on computers you don't own. It can also be very useful on your own computer: if you have to reinstall Windows, you won't need to reinstall VLC, it will be up and running almost instantly:
| http://portableapps.com/apps/music_video/vlc_portable

Related articles
----------------

-  `Common Problems <Common_Problems>`__
-  `VLC command-line help <VLC_command-line_help>`__
-  `VLC HowTo/Make a DVD <VLC_HowTo/Make_a_DVD>`__

`\* <Category:Windows>`__

.. |Main window| image:: VLC_-_main.png

