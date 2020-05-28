{{Howto|Listen to online radio in VLC through [[Icecast]]}}

The current version is '''{{VLC:latest version}}'''.

<onlyinclude>For the [[Qt Interface]] on 3.0.6: # If not already
visible, open the playlist sidebar through ''View'' → ''Playlist'' #
Scroll down the sidebar, if necessary, to the section ''Internet'' #
Click the entry ''Icecast Radio Directory'' # Select a listing #
[[File:Musical note.pnglink=|20px]]</onlyinclude>

== Old guides == === 0.8.2 === You can of course always simply find a
link to a radiostream and then open it as you would any other network
stream in VLC. But if you would like to '''browse a list of online
radios''', you can try the list of '''shoutcast''' radio stations VLC
can download for you: \* First you need to open the playlist window:
View->Playlist. \* Once you have the playlist window open choose:
''Manage->Service discovery->Shoutcast radio listings''. After 10
seconds or so the playlist should have become populated by radio station
entries. You obviously require an Internet connection for this to work!
\* If you want the stations sorted alphabetically, you can choose:
''Sort->Sort by title''. Also note shoutcast have many thousands of
streams available, per default in 0.8.2 250 stations are downloaded,
this can be changed in the preferences under: <u>Playlist->Service
discovery->Shoutcast</u>.<br />Note that the more stations you want to
add, the longer delay you will see when the station list is downloaded,
parsed, and added to the playlist.<br />Also note you should see 2
"Folder nodes" in the playlist under shoutcast called Genres and bitrate
where the stations will be listed under their respective areas. Note
that most stations claim to be multi-genre, so a station might be listed
under both Top40, pop and rock.

=== 1.0.2 === For VLC 1.0.2 "Goldeneye" under Linux, I got the Shoutcast
listing by (from the VLC tools) Media/Services Discovery/Shoutcast Radio
listings. After checking that option, the playlist was populated with
the Shoutcast list.

=== 1.1.11 === For version 1.1.11 the following works fine:

-  If not already visible, open the playlist window through
   ''View''->''Playlist''. On the left side you see the '''Media
   Browser''' on the right side the '''Playlist''' window which is
   probably empty.
-  In the '''Media Browser''' double-click the entry ''Internet'' which
   will unfold a few options, one them being the ''Icecast Directory''.
   Of course, using any of these Internet options requires an active
   Internet connection.
-  Double-click the entry ''Icecast Directory'' and after a few seconds
   a list of radio stations will be displayed in the '''Playlist'''
   window, which now has been renamed to '''Icecast Directory'''.

The other Internet-related stream sources work similarly, except the
''Podcasts'' which require you to enter the URL of a podcast you wish to
subscribe to.
