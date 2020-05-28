{{howto|save bookmarks}}

-  note: loading bookmarks is broken thru version 1.0.5. The last
   working version I know of was in the 0.8 series. See
   http://trac.videolan.org/vlc/ticket/2100\ {{Check}}

If you wish to save bookmarks this is how it can be done.

Set up the Bookmark list and then save a Playlist. From now on, anytime
you open the playlist, VLC will load the bookmarks.

Open the playlist dialog with menu selection View-Playlist. The playlist
window has a menu selection Manage that allows opening and saving
playlists.

Opening a saved playlist will also load an associated bookmark list as
long as the option "Enable parsing of EXTVLCOPT: options" is enabled. To
check this setting choose "Settings -> Preferences -> Input / Codecs ->
Demuxers -> Playlist".

Although more bookmarks can be set up, there seems to be a limit to the
number of bookmarks which can be saved in the playlist. Possibly, the
limit is determined by the number of bytes the bookmark list takes up in
the playlist (m3u) file. Therefore, shorter bookmark names equal more
bookmarks. Also, the m3u file is a text file and can be edited. There is
a bytes parameter which is not necessary if all you want to do is
bookmark locations. (This information is tentative. Conclusions have not
been exhaustively tested.)

The bookmark window's behavior is inconsistent. When loaded with the
playlist, the only way it apparently will display is maximized. This is
somewhat inconvenient because if the playlist (m3u) file format is
associated with VLC, when you click on the m3u file, you can't view the
bookmark list and VLC at the same time. You may get around this by
opening VLC first, then opening the (empty) bookmark list. Then, when
you load the desired playlist, the booklist can be accessed in an
adjustable size.

[[Category:How To]]
