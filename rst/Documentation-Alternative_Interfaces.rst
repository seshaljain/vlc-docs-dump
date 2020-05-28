.. raw:: mediawiki

   {{Outdated}}

.. raw:: mediawiki

   {{RightMenu|Documentation TOC}}

The HTTP interface
------------------

VLC ships with a little HTTP server integrated. It is used both to stream using HTTP, and for the HTTP remote control interface.

To start VLC with the `HTTP interface <HTTP_interface>`__, use:

``{{%}} ``\ **``vlc``\ ````\ ``-I``\ ````\ ``http``\ ````\ ``[--http-src``\ ````\ ``/directory/]``\ ````\ ``[--http-host``\ ````\ ``host:port]``**

If you want to have both the "normal" interface and the HTTP interface, use **vlc --extraintf http**.

The HTTP interface will start listening at host:port (<all interfaces>:8080 if omitted), and will reproduce the structure of /directory at http://host:port/ ( vlc_source_path/share/http if omitted ).

Use a browser to go to http://your_host_machine:port. You should be taken to the main page.

VLC is shipped with a set of files that should be enough for generic needs. It is also possible to customize pages. See `Documentation:Play HowTo/Building Pages for the HTTP Interface <Documentation:Play_HowTo/Building_Pages_for_the_HTTP_Interface>`__.

Available pages for 1.0.3 :

-  http://host:port - Main Interface
-  http://host:port/vlm.html - VLM Interface
-  http://host:port/mosaic.html - Mosaic Wizard
-  http://host:port/flash.html - Flash based remote playback

Ncurses
-------

This is a text interface, using ncurses library.

Start VLC with **-I ncurses** or **--extraintf ncurses**. You will then get something like that:

https://images.videolan.org/images/documentation/play-howto/intf-ncurses-playlist.jpg

The ncurses interface

Press h to get the list of all available commands, with a short description.

There is also a filebrowser available for the ncurses interface in order to add playlist items. Press 'B' to use it.

https://images.videolan.org/images/documentation/play-howto/intf-ncurses-filebrowser.jpg

The ncurses filebrowser

You can set the filebrowser starting point by launching vlc with the **--browse-dir** option:

``% ``\ **``vlc``\ ````\ ``-I``\ ````\ ``ncurses``\ ````\ ``--browse-dir``\ ````\ ``/filebrowser/starting/point/``**

Other control interfaces
------------------------

VLC includes a number of so-called interfaces that are not really interfaces, but means of controlling VLC. Nevertheless, they are enabled by setting them as interface or extra interface, either in the Preferences, in General/Interface, or using **-I** or **--extraintf** on the command line.

Hotkeys
~~~~~~~

This module allows you to control VLC and playback via hotkeys. It is always enabled by default. You can use hotkeys in the video output window, you can't in the audio dummy interface.

Hotkeys can be hacked by:

``% ``\ **``vlc``\ ````\ ``--key-<function>``\ ````\ ``<code>``**

Code is composed by modifiers keys (Alt, Shift, Ctrl, Meta,Command) separated by a dash (-) and terminated by a key (a...z, +, =, -, ',', +, <, >, \`, /, ;, ', \\, [, ], \*, Left, Right, Up, Down, Space, Enter, F1...F12, Home, End, Menu, Esc, Page Up, Page Down, Tab, Backspace, Mouse Wheel Up and Mouse Wheel Down). Main controls are available from hotkeys, such as : fullscreen, play-pause, faster, slower, next, prev, stop, quit, vol-up, etc. (use the **--longhelp** option for full list of functions). For example, for binding fullscreen to Ctrl-f, run:

``% '''vlc --key-fullscreen 'Ctrl-f' '''``

The list of the default hotkeys is available `here <HotKeys>`__.

RC, Telnet
~~~~~~~~~~

These two interfaces allow you to control VLC from a command shell (possibly using a remote connexion or a Unix socket).

Start VLC with **-I rc** or **--extraintf rc**. When you get the **Remote control interface initialized, \`h' for help** message, press h and Enter to get help about available commands.

To be able to remote connect to your VLC using a TCP socket (telnet-like connexion), use **--rc-host your_host:port**. Then, by connecting (using telnet or netcat) to the host on the given port, you will get the command shell.

To use a UNIX socket (local socket, this does not work for Windows), use **--rc-unix /path/to/socket**. Commands can then be passed using this UNIX socket.

The RTCI interface is an old module merged into the RC interface.

Gestures
~~~~~~~~

Gestures provide a simple `mouse gestures <mouse_gestures>`__ control. TODO

| 
| 

`\* <Category:Control_VLC>`__
