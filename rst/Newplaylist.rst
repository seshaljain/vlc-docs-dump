== New playlist and sources proposal ==

The current playlist is a mix between 'playlists', list of playable
elements (in the M3U way) and list of elements by source. Too many
concurrent subplaylist or playlist like ("Advanced open file") This is
confusing, and does not match the "playlist" definition.

-  split the current playlist in 2 components: "The Playlist" (M3U way)
   and "The sources"
-  The playlist just becomes the interface for
   loading/managing/exporting URI lists (M3U), or subplaylists
-  The sources list is the current playlist window without the "M3U"
   part

\* The sources list has drag & drop & buttons to add URI to the M3U
playlist By extension: \* We drop the current open file/open DVD/capture
interface. We replace it by the sources, and create new sources
accordingly. \* The open file/dvd menus dissapear and is replaced by
"open source/media" \* Each configuration menu is backported into the
sources interface (see schema) split with Qtoolbox like widget. \*
Ideally, each widget is redefined as a qtcreator xml widget.

new sources interface [[File:Newinterface3.jpg]]

new playlist interface [[File:Newplaylist.jpg ]]

Merged playlist [[File:mergedplaylist.jpg ]]

== Prior requirements ==

-  Make sure that every playlist element is reacheable by URI.
-  Media listings must me read on selection (DVD, CD, ...)

[[Category:Dev Discussions]]
