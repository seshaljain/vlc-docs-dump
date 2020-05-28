.. raw:: mediawiki

   {{See also|VLC command-line help|Console|label2=Console interfaces|Documentation:Command line}}

This page describes how to access the terminal and start VLC in it.

A terminal is a text-based way to run programs. It is normally pre-installed on your computer. The command prompt may also be called the "Command Prompt", "Console", "Terminal", "MS-DOS Prompt", or something similar.

Running VLC from the terminal gives you access to many commands and features in VideoLAN which you would not otherwise have: see the `VLC command-line help <VLC_command-line_help>`__ page to find out more about options from the command line.

| Note that **%** is used on many of the examples on the VLC Wiki to represent the prompt, so you don't need to type that in.
| Depending on your `operating system <operating_system>`__, the prompt could appear as a >, %, $ or # symbol. Read on for a detailed explanation.

Tip: For extended command-line work (or play) it may be worth changing to the directory of VLC. Most command-line interpreters will understand ``vlc`` or ``vlc.exe`` to be the program in that directory.

Windows
-------

In Windows, this is called the **command prompt**. To open the command prompt:

-  Click on the Start Menu and select Run.
-  In the Run box, type **cmd** (or **command** for older versions of Windows) and press enter.

The command prompt will look something like this:

``C:\>``

To run VLC, you will need to know where you installed VLC; the default is ****. So to start VLC, type the full path to VLC and the options:

\ `` ``\ *``options``*

replacing *options* with the name of the file to play and its options.

macOS
-----

You can run VLC on `macOS <macOS>`__ using a terminal application, such as **Terminal.app** in **/Applications/Utilities**. In the terminal window type

\ `` ``\ *``options``*

replacing *options* with VLC options, commands, the name of the file to play, and so on.

| To suppress the launch of any Mac-like interface, you have to add the Option ``-I`` or ``--intf`` followed by the interface you want to use instead.
| Available interfaces are:

-  *rc* (remote control)
-  *ncurses* (command-line-gui)
-  *http* (web interface, usually on `port <port>`__ 8080)—this interface will prevent VLC from appearing even in the Dock.

In older versions you could replace the "VLC" at the end of the path with "`clivlc <clivlc>`__" to suppress the launch of any Mac-like interface.

Linux/Unix
----------

How to get a Linux terminal varies by distribution (for any desktop setup it will be somewhere in the applications; these are merely shortcuts). If you use Ubuntu or Linux Mint, gnome-terminal can be opened with the key combination Ctrl+Alt+T. If you use RHEL/Fedora/CentOS, gnome-terminal can be opened by right-clicking on the desktop and selecting Open terminal.

By convention:

-  The **standard user** prompt may appear as $ or % or something else.
-  The **root user** prompt is represented with a #. This is an indication that you must either log in as root (potential security risk) or prefix the command with ``sudo`` and enter your password.

To run VLC, you can normally type

\ `` ``\ *``options``*

replacing *options* with the name of the file to play and its options.

`Category:Documentation <Category:Documentation>`__ `Category:Coding <Category:Coding>`__
