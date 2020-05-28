-  DRAFT

-  

   -  I backuped your contribution to `Windows <Windows>`__ here before reverting it to the previous English content (as described in your user_talk page)
   -  This page need to be cleaned and merged with `De/Windows <De/Windows>`__ I think
   -  If you can't delete this draft page later, you can ask me.
   -  --`Thannoy <User:Thannoy>`__ 14:47, 13 December 2009 (UTC)

The **Windows port** of VLC usually starts up with the `Qt <Qt>`__ interface which is used in the `Linux <Linux>`__ one as well. The user can decide to use the `Skins <Skins>`__ interface instead to be able to modify the interface according to his or her mood.

Keyboard shortcuts in the Windows (directx) video output
--------------------------------------------------------

   *See also:*\ `QtHotkeys <QtHotkeys>`__

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

How to associate media files to VLC
-----------------------------------

VLC hasn't got a module to associate files so that if you click on a file VLC automatically opens. The developers are working on this, and one should be available in the next full release. But you can do it yourself by choosing one of these three options:

Use Windows Explorer's context menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. In Windows Explorer, *right*-click a file you wish to open.
#. Clicking Open With from the context menu that pops up.
#. Clicking the VLC's program name.

   -  If VLC is not displayed, click Browse to locate it on your hard drive.

Alternatively, you can:

#. In Windows Explorer, *right*-click the file you want to open with VLC.
#. Click Properties in the context menu that pops up.
#. On the General tab, click Change.
#. Click the name of the program (VLC) which you want to be used to open the file.

Either of these options affects all files that have the same filename extension (the letters after the filename's period) as the file you selected. For example, if you change the program that opens *goober.avi*, then all *.avi* files will be opened with VLC.

Rerun the installer
~~~~~~~~~~~~~~~~~~~

#. Reinstall VLC and choose the "associate files" option when it comes up.

Edit the registry
~~~~~~~~~~~~~~~~~

**Warning**: use this technique only if you really know what you are doing! And be sure to back-up your registry first.

#. Open a text editor, like Notepad (but not WordPad).
#. Copy this text below.
#. Modify the strings *C:\\Program Files\\VideoLAN\\VLC\\vlc.exe* to match your VLC installation.
#. Save as *vlc.reg*.
#. Execute *vlc.reg* (adding this data to your registry).
#. Enjoy VLC :)

Text to copy:

::

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

So starten Sie VLC-Server mit HTTP-Interface
--------------------------------------------

VLC wird mit einer kleinen integrierten HTTP-Server. Es ist sowohl zum Streamen über HTTP verwendet, und für den HTTP-Fernbedienung auswählen.

VLC Server-Einstellungen Einstellungen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Richten Sie die HTTP-Schnittstelle Details in den VLC-Server-Anwendung. Open VLC wählen Sie "Einstellungen"> "Einstellungen. Klicken Sie auf die Schaltfläche Erweiterte Einstellungen in der unteren rechten Ecke des Dialogfelds, um alle Optionen, die verfügbar sind.

2. Im linken Fenster klicken Sie auf die Schaltfläche "+" neben dem Interface. Dies zeigt drei Möglichkeiten. Control-Schnittstellen, Hotkeys-Einstellungen, und zu den wichtigsten Schnittstellen. Klicken Sie auf das Plus-Taste neben dem Haupt-Schnittstellen. Dies wird vier Einstellungen HTTP-Display, RC, Skins, wxWidgets. Klicken Sie auf HTTP, um die HTTP-Fernbedienung Interface-Einstellungen Dispaly ".

3. Host-Adresse: Geben Sie die Port-Nummer, die Sie verwenden möchten. Der Standardwert ist 8080.

4. Quelle: C: \\ Program Files \\ VideoLAN \\ VLC \\ http \\ oder geben Sie den Pfad, wo Sie gewählt haben, um die Anwendung zu installieren.

5. Zeichensatz: UTF-8 Standard

6. Wenn Sie nicht mit Handler-oder SSL-Zertifikate die Installation abgeschlossen ist.

7. Klicken Sie auf die Schaltfläche "Speichern" in der linken unteren Ecke.

8. Denken Sie daran, die. Hosts-Datei im VLC / http-Verzeichnis zu bearbeiten, erlaubt nur localhost, bearbeiten, um andere Hosts zu ermöglichen.

Command Line Startup
~~~~~~~~~~~~~~~~~~~~

Die anwendungsspezifischen VLC kann in einem Server-oder Client-Umgebung ausgeführt werden. Bei komplizierten Video-und Audio-Streaming auf einem LAN, sollte man prüfen, widmet eine Maschine zu handeln die VLC-Server.

Um die VLC-Anwendung in einer Server-Modus mit dem HTTP-Interface automatisch starten festzulegen, verwenden Sie die folgende Befehlszeile in Ihrem Desktop-Verknüpfung. Dies setzt den Standard Speicherort für die Installation ausgewählt wurde.

"C: \\ Program Files \\ VideoLAN \\ VLC \\ vlc.exe" - extraintf http - intf wx </ nowiki>

Testen der Schnittstelle
~~~~~~~~~~~~~~~~~~~~~~~~

Von einem anderen Computer eine Verbindung mit dem VLC-Server-Computer mit Ihrem Browser die URL

http://server_ip_address:8080 wie http://192.168.0.186:8080 </ nowiki>

Der Main VLC Interface Seite wird angezeigt,

Siehe `web_interface <web_interface>`__ für weitere Informationen

VLC Plugin for Internet Explorer
--------------------------------

This section will provide guidelines to incorporate the VLC ActiveX plugin to be used to view streaming audio and video from a VLC server.

How to embed the ActiveX Plugin in a Web Page: `ActiveX/HTML <ActiveX/HTML>`__

Supported ActiveX Function Calls: `ActiveX <ActiveX>`__

VLC Plugin for Firefox (Mozilla)
--------------------------------

The Mozilla plugin (Excerpted from the `VLC User Guide <Documentation:Play_HowTo/Advanced_Use_of_VLC#The_Mozilla_plugin>`__)

**Install**

There are at least two ways to install the VLC Mozilla Plugin. One way is to to check the "Install Firefox Plugin" when you install VLC.

If the standard exe installation does not install the mozilla plugin directory then download zip version which includes the required data and continue with the next installation (2nd way of installing of the plugin)

The second way involves several steps:

1. Quit Firefox or Mozilla

2. Copy the two files in VLC_Installation_folder\mozilla (usually C:\Program Files\VideoLAN\VLC\mozilla) to your mozilla plugins directory (Usually C:\Program Files\Mozilla\plugins or C:\Program Files\Mozilla Firefox\plugins).

3. Restart Firefox or Mozilla

**Use the plugin**

If you open a link to a video file handled by the VLC plugin (To get the list of handled types, browse to about:plugins) or a page with an embedded video, the plugin should open and read the video.

**Build HTML pages that use the plugin (VLC version > 0.8.5)**

Check the `WebPlugin <Documentation:WebPlugin>`__ documentation for information on the Javascript API. It's substantially changed since v0.8.5.

**Build HTML pages that use the plugin (VLC version up to 0.8.5)**

Additionally to viewing video on all pages, you can build custom pages that will use the advanced features of the plugin, using Javascript functions to control playback or extract information from the plugin.

The vlc plugin for Firefox/Mozilla supports the following function calls:

| ``     play() : Start playing media in the plugin.``
| ``     pause() : Pause playback.``
| ``     stop() : Stop media playback.``
| ``     fullscreen() : Switch the video to full screen.``
| ``     set_volume(vol) : Set the volume. vol has to be an int in the 0-200 range.``
| ``     get_volume() : Get the current volume setting.``
| ``     mute() : Toggle volume muting.``
| ``     set_int_variable(var_name, value) :``
| ``     set_bool_variable(var_name, value) :``
| ``     set_str_variable(var_name, value) :``
| ``     get_int_variable(var_name) :``
| ``     get_bool_variable(var_name) :``
| ``     get_str_variable(var_name) :``
| ``     clear_playlist() : Clear the playlist.``
| ``     add_item(mrl>) : Append an item whose location is given by the Media Resource Locator to the playlist.``
| ``     next()``
| ``     previous()``
| ``     isplaying() : return true if the plugin is playing something.``
| ``     get_length() : Get the media's length in seconds.``
| ``     get_position() : Get the current position in the media in percent.``
| ``     get_time() : Get the current position in the media in seconds.``
| ``     seek(seconds,is_relative) : If is_relative is true, seek relatively to current time, else seek from beginning of the stream. Seek time is specified in seconds.``

Here are a few examples of HTML pages that use the Mozilla plugin. Example 1

In this example, the plugin will read an HTTP stream inside the web page. If the user goes fullscreen, he will have to press f to go back in normal view.

::

   <html>
   <head><title>Demo of VLC mozilla plugin</title></head>

   <body>

   == Related article ==
   * [[Common Problems]]
   * [[VLC command-line help]]
   * [[VLCSout]] - converting between formats

   [[Category:Operating systems]]

   <h1>Demo of VLC mozilla plugin - Example 2</h1>

   <embed type="application/x-vlc-plugin"
            name="video2"
            autoplay="no" loop="no" hidden="yes"
            target="udp:@239.255.12.42" />
   <br />
     <a href="javascript:;" onclick='document.video2.play()'>Play video2</a>
     <a href="javascript:;" onclick='document.video2.stop()'>Stop video2</a>
     <a href="javascript:;" onclick='document.video2.fullscreen()'>Fullscreen</a>

   </body>
   </html>

More example code, as well as a working implementation using Javascript, XHTML, and PHP that auto-detects browsers (the code is good, but the stream doesn't work) can be found at http://altair.videolan.org/~dionoea/vlc-plugin-demo/

.. raw:: html

   <h1>

Demo of VLC mozilla plugin - Example 2

.. raw:: html

   </h1>

::

    <embed type="application/x-vlc-plugin"
            name="video2"
            autoplay="no" loop="no" hidden="yes"
            target="udp:@239.255.12.42" />
    <br />
    <a href="javascript:;" onclick='document.video2.play()'>Play video2</a>
    <a href="javascript:;" onclick='document.video2.stop()'>Stop video2</a>
    <a href="javascript:;" onclick='document.video2.fullscreen()'>Fullscreen</a>

More example code, as well as a working implementation using Javascript, XHTML, and PHP that auto-detects browsers (the code is good, but the stream doesn't work) can be found at http://altair.videolan.org/~dionoea/vlc-plugin-demo/

Related article
---------------

-  `Common Problems <Common_Problems>`__
-  `VLC command-line help <VLC_command-line_help>`__
-  `VLCSout <VLCSout>`__ how to create a DVD

`Category:Operating systems <Category:Operating_systems>`__
