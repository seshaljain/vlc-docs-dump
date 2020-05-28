{{RightMenu|Documentation TOC}} A playlist is a customised list of media
files you might want to watch or listen to. Using a playlist, you can
specify the media files you want to listen each time you start the VLC
media player. You can add tracks from CDs, radio stations, and movies to
a playlist. To access the playlist, click on the ''Playlist'' button in
the main interface.

[[File:Basic_playlist_default.png]]

The default playlist view.

== Additional Sources ==

In addition to audio and video files, you can play other formats. The
additional formats supported by VLC media player are described in the
following sections:

*'''Podcasts''' - Podcast (Personal On Demand broadCASTING) is a series
of audio or video digital media files which is distributed over the
Internet and downloaded to media players. If consumers subscribe to
Podcasts, whenever new content is added the content gets automatically
added to the playlist. You can customise Podcasts. To add a Podcast URL
#Select the [[File:VLC - playlist.png]] ''Playlist'' button. #Click on
the ''Internet'' button to select it in the left pane. The ''Podcasts''
menu item will appear under ''Internet''. #Select a Podcast stream in
the main dialog box. Then right-click the stream and select ''Play''
from the popup menu.*'''SAP Announcements''' – Helps to advertise your
stream over the network.

To play a SAP announcement:

#Select the [[File:VLC - playlist.png]] ''Playlist'' button. #Click on
the ''Local Area Network'' to select it in the left pane. The ''Network
Streams (SAP)'' menu item will appear under ''Local Area Network''.
#Select an SAP announcement and right-click. Select ''Play'' from the
popup menu.

\*'''Shoutcast Radio Listings''' – Shoutcast is a server for streaming
the media developed by Nullsoft. Digital audio content can be broadcast
from and to media players, and this helps individuals to create Internet
radio networks. Using VLC media player, you can listen to your favourite
radio stations and you can also create bookmarks to listen to these
radio stations in future.

To customize a Shoutcast radio listing:

#Select the [[File:VLC - playlist.png]] ''Playlist'' button. #Select
''Icecast Directory'' under ''Internet'' in the ''Playlist'' menu. A
list of radio stations appears in the right hand panel. If nothing
appears in the right hand panel try double-clicking the ''Shoutcast
Radio'' option and wait. It may take a few minutes the first time. After
a while, the right hand panel displays a list of titles.

[[File:Shoutcastdirectory.PNG]]

#Scroll down and select a radio station. #Right-click on a radio station
and: ##Select ''Play'' if you want to listen to the radio station.
##Select ''Remove Selected'' if you want to delete the radio station.
##Select the ''Stream'' option. The Stream output dialog box is
displayed. Refer to the Specifying
[[#Specifying_Streaming_OptionsSpecifying Streaming options]] section
for more details. ##Select the Information option. The Media Information
dialog box is displayed with details of the media being played. ##Select
''Title'' to alphabetically sort the radio stations. ##Click to select a
title in the Playlist dialog box and right-click. Select ''Open Folder''
from the popup menu. A folder is opened to show all sub nodes within a
title. ##Select ''Add Node'' to add a node. ##Click to select a title in
the Playlist dialog box and right-click. Select ''Information'' from the
popup menu to view the details of the selected title. Refer to the
''Media Information'' section for more details on options.

*''Shoutcast TV stream'' – You can watch streaming TV using the VLC
media player. Shoutcast TV stream refers to a stream transmitted by
Nullsoft. The procedure of customising the TV stream and the options are
similar to that of the Shoutcast Radio.*''Freebox TV listing'' – Refers
to television service over ADSL accessible by Freebox Free Zone
unbundled.

''Note:'' You should be connected to the Internet to access these
streams.

== Add Media Files to Playlist ==

You can add several media files to a playlist. The media files could be
selected from the media library, additional sources, and some other
source.

To add files to a playlist:

#Select the [[File:VLC - playlist.png]] ''Playlist'' button.
#Right-click on the dialog box and click and a short list appears with
two options: Add file and Add directory. ##Select ''Add file'' to add a
file to the playlist. ##Select ''Add directory'' to add a directory
containing media files to the playlist. #Click on the
[[File:Random.JPG]] '''Random''' icon. This icon toggles between
''Random'' and ''Random Off''. Click on [[File:Random.JPG]] to play
files at random. Click on [[File:Random.JPG]] and the files are played
in an order. #Click on the [[File:Repeat.JPG]] ''Repeat'' icon. This
icon toggles between ''Repeat One'' and ''Repeat All''. If you want to
listen to a track several times, click on [[File:Repeat.JPG]] icon. If
you want to listen to all tracks, click on [[File:Repeat.JPG]] again.
#To search for a media file, enter the name in the ''Search'' box. To
search for media files with certain names or formats, enter a word or
phrase in the ''Search'' box. All files with the specified name are
listed. #Click on the [[File:Skip.JPG]] icon. This icon is used to skip
to the current item when you have a very long list. #Click the ''Remove
Selected'' button to clear a track from the playlist.

== Load Playlist ==

This option is used to add a playlist created in some other media
player. You can load playlists of the ''.xspf, .asx, .b4s'' and ''.m3u''
formats. To load a playlist:

#Select the ''Open'' option from the ''Media'' menu. The ''Open file''
dialog box is displayed. #In the bottom right, change the format to
''Playlist Files'' in the selector. #Locate a playlist file and click on
''Open''.

The selected playlist is added in the current playlist dialog box.

<br>

== Save Playlist ==

You can save playlists using the VLC media player in format of your
choice. To save a playlist:

#Create a playlist. Refer to [[#Add_Media_Files_to_Playlist|Add Media
Files to Playlist]] for creating a playlist. #Select ''Save Playlist to
File'' from the ''Media'' menu. The ''Choose a filename to save
playlist'' dialog box is displayed. #Select a name for the playlist.
#Select a format in which the playlist must be saved from the ''Files of
type'' list. The Files of type list contains the ''.xspf'' and ''.m3u''
formats. #Click on ''Save'' to save the playlist in the selected format.

== Play a file ==

To play a file, open the Media menu, and select the Open File menu item.
An Open File dialog box will appear. Select the file you want to open,
and click Open. VLC will start playing the selected file. An alternative
is to drag 'and' drop your file onto the VLC main interface or playlist
window from the file explorer (Finder on MacOS X).

[[File:VLC - open file.png]]

VLC 0.9.8a version Windows XP mode

https://images.videolan.org/images/documentation/play-howto/intf-osx-file-menu.jpg

The File menu - MacOS X interface'''- needs verifying for 0.9'''

[[File:Vlc-mediaopenfileselected-vistaclassic-en.png]]

The Open file dialog - wxWidgets interface

(FIXME need 0.9 screenshot for MacOS) The Open file dialog - MacOS X
interface

== Naming Files ==

You can change the original file name to one you would like before
adding the file to VLC. When adding files from the menu bar, the new
file name will show in the playlist. However, when dropping the file
using the "add/drop" option, VLC may not recognize the name change
depending on the file type. In that case, you can right click the header
of the playlist column and select "URL," you will then see the original
file path for the file.

== Sorting ==

In the wxWidgets interface, ''Sort'' allows you to sort the playlist
according to several criteria, or to shuffle it. You can also sort by
clicking the header of the column.

In the MacOS X interface, sorting can be done by clicking the header of
the column matching the criteria you want to use for sorting.

== Playlist modes ==

The playlist supports several playback modes.

In the wxWidgets interface, the toolbar contains three playlist mode
buttons. They allow you to enable random mode, to repeat the whole
playlist or to repeat one item.

In the MacOS X interface, random mode can be enabled by selecting the
''Random'' box. A drop down menu allows you to enable playlist and item
repeat modes.

== Misc ==

=== Search ===

You also have a search tool. Enter a search string and hit search. The
next item to match the string will be highlighted. Keep hitting Search
to cycle between all matching items.

[[File:Basic_playlist_search.png]]

=== Moving items ===

In the wxWidgets interface, the ''Up'' and ''Down'' buttons at the
bottom of the playlist window allow you to move an item. Select an item
and use these buttons to move it.

In the MacOS X interface, you can easily move an item with the mouse,
using drag-and-drop.

=== Contextual menu ===

By right-clicking or control-clicking an item, a contextual menu will
appear, giving access to a number of functions (for example, play the
item, disable it, delete it, or get info on it).

[[File:Basic_playlist_contextual.png]]

=== Example finding a Shoutcast radio stream ===

This example was verified as working on 15 October 2008, using VLC 0.9.4
under Windows Vista. ''This needs reproducing by other people on other
versions and other operating systems.''

1. Ensure your firewall is set to allow the VideoLan program to make
   outgoing connections.
2. Click ''Tools'' then ''Preferences'', click Interface and then click
   All under "Show settings". Then click the "-" next to "Playlist" in
   order to show the "Services discovery" submenu. If the shoutcast
   radio listings box is empty, click it so that a check-mark appears.
   The text field underneath should now show the word "shout". Click the
   Save button to save and close the Preferences window:

[[File:Vlc-preferencesservicesdiscoveryshoutcrop-en.png]]

3. Restart VLC media player to make it take notice of the changed
   preferences.
4. On the VLC interface click ''Playlist'', then click ''Show
   Playlist''. Select the "Shoutcast Radio" in the left hand panel. If
   nothing appears in the righthand panel, try double-clicking
   "Shoutcast Radio" and waiting, it may take a few minutes the first
   time. After a while the righthand panel displays a long list of
   titles.

[[File:Vlc-playlistshoutcastradio-en.png]]

5. Scroll down the radio stations in the right-hand panel and select
   one. Click the mouse right button and click the "Play" item.

[[File:Vlc-playlistshoutcastradioplay-en.png]]

6. It may take some time for the connection to the radio station to
   establish (and it may fail if the station's outgoing streams are all
   occupied). When it does connect, VLC should start playing the audio
   stream from the station:

[[File:Vlc-playlistshoutcastradioplayingsmall-en.png]]

=== Example playing a known Shoutcast radio stream ===

Go to http://www.shoutcast.com/ and search for a radio station of your
choice. On Windows, right-click your mouse over Shoutcast's "Tunein"
button and click "Save Link As..." to save the playlist on your
computer. Remember where you saved the playlist, rename it to something
that makes sense.

At any time later, you can use VLC to open the saved playlist and listen
to that radio station.

For example, to find a BBC World Service radio stream, use a browser to
go to:
http://www.shoutcast.com/directory/search_results.jsp?searchCrit=simple&s=bbc

One of the stations listed may be playing the World Service, if so move
your mouse over the "TUNEIN!" webicon and click the right mouse button
and click "Save Link As...", as described above.

{{Documentation}}

[[Category:Playlist|*]]
