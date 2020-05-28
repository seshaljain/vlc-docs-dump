{{Moduletype=Control interface|description=ncurses console interface}}

== Introduction == This is one of the three command line interfaces
(besides [[Documentation:Modules/rctelnet]]). To force vlc into using
this interface, do the following: vlc -I ncurses

This interface is operated through a set of shortcuts which are listed
in the next section.

== Shortcuts == To get the following list of all available shortcuts in
the interface press 'h'. Use the up and down arrow keys to scroll.

   [Display] h,H Show/Hide help box i Show/Hide info box L Show/Hide
   messages box P Show/Hide playlist box B Show/Hide filebrowser

   [Global] q, Q Quit s Stop <space> Pause/Play f Toggle Fullscreen n, p
   Next/Previous playlist item [, ] Next/Previous title <, >
   Next/Previous chapter <right> Seek +1% <left> Seek -1% a Volume Up z
   Volume Down

   [Playlist] r Random l Loop Playlist R Repeat item o Order Playlist by
   title O Reverse order Playlist by title / Look for an item A Add an
   entry D, <nowiki><del></nowiki> Delete an entry <backspace> Delete an
   entry

   [Filebrowser] <enter> Add the selected file to the playlist <space>
   Add the selected directory to the playlist . Show/Hide hidden files

   [Boxes] <up>,<down> Navigate through the box line by line
   <pgup>,<pgdown> Navigate through the box page by page

   [Player] <up>,<down> Seek +/-5%

   [Miscellaneous] Ctrl-l Refresh the screen

{{Documentation footer}}

[[Category:Interfaces]]
