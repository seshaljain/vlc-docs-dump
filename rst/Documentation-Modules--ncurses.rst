.. raw:: mediawiki

   {{Module|name=ncurses|type=Control interface|description=ncurses console interface}}

Introduction
------------

This is one of the three command line interfaces (besides `remote control (rc) <Documentation:Modules/rc>`__ and `telnet <Documentation:Modules/telnet>`__). To force vlc into using this interface, do the following:

``vlc -I ncurses``

This interface is operated through a set of shortcuts which are listed in the next section.

Shortcuts
---------

To get the following list of all available shortcuts in the interface press 'h'. Use the up and down arrow keys to scroll.

| ``[Display]``
| ``h,H         Show/Hide help box``
| ``i           Show/Hide info box``
| ``L           Show/Hide messages box``
| ``P           Show/Hide playlist box``
| ``B           Show/Hide filebrowser``
| ``[Global]``
| ``q, Q        Quit``
| ``s           Stop``
| \ ``     Pause/Play``
| ``f           Toggle Fullscreen``
| ``n, p        Next/Previous playlist item``
| ``[, ]        Next/Previous title``
| ``<, >        Next/Previous chapter``
| \ ``     Seek +1%``
| \ ``      Seek -1%``
| ``a           Volume Up``
| ``z           Volume Down``
| ``[Playlist]``
| ``r           Random``
| ``l           Loop Playlist``
| ``R           Repeat item``
| ``o           Order Playlist by title``
| ``O           Reverse order Playlist by title``
| ``/           Look for an item``
| ``A           Add an entry``
| ``D, <del>    Delete an entry ``
| \ `` Delete an entry``
| ``[Filebrowser]``
| \ ``     Add the selected file to the playlist``
| \ ``     Add the selected directory to the playlist``
| ``.           Show/Hide hidden files``
| ``[Boxes]``
| \ ``,``\ \ ``     Navigate through the box line by line``
| \ ``,``\ \ `` Navigate through the box page by page``
| ``[Player]``
| \ ``,``\ \ ``     Seek +/-5%``
| ``[Miscellaneous]``
| ``Ctrl-l          Refresh the screen``

.. raw:: mediawiki

   {{Documentation footer}}

`Category:Interfaces <Category:Interfaces>`__
