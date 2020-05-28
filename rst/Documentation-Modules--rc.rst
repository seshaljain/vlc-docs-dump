.. raw:: mediawiki

   {{Module|name=rc|type=Interface|description=Text based command interface}}

Introduction
------------

The remote control interface (rc for short) is one of the three console interfaces provided by VLC. The other two being `ncurses <Documentation:Modules/ncurses>`__ and `telnet <Documentation:Modules/telnet>`__.

To force VLC into using this interface, do the following:

``{{%}} vlc -I rc``

This interface is operated through textual commands typed into the invoking terminal window.

This is the default interface if no `GUI <GUI>`__ environment is available.

Command reference
-----------------

Type ``help`` followed by enter for a terse list of commands or ``longhelp`` for the complete list.

Command line options
--------------------

There are several options you can use in conjunction with the rc interface:

==================== =============================================================================================================================================================================================================== ======================
**Option**           **Description**                                                                                                                                                                                                 **Enabled by default**
``--rc-show-pos``    Show stream position                                                                                                                                                                                            No
``--no-rc-show-pos`` Show the current position in seconds within the stream from time to time.                                                                                                                                       No
``--rc-fake-tty``    Fake TTY                                                                                                                                                                                                        No
``--no-rc-fake-tty`` Force the rc module to use stdin as if it was a TTY.                                                                                                                                                            No
``--rc-unix=``\      UNIX socket command input. Accept commands over a Unix socket rather than stdin.                                                                                                                                -
``--rc-host=``\      TCP command input. Accept commands over a socket rather than stdin. You can set the address and port the interface will bind to.                                                                                -
``--rc-quiet``       Do not open a DOS command box interface                                                                                                                                                                        
``--no-rc-quiet``    By default the rc interface plugin will start a DOS command box. Enabling the quiet mode will not bring this command box but can also be pretty annoying when you want to stop VLC and no video window is open. No
==================== =============================================================================================================================================================================================================== ======================

To get this list run

``vlc -p rc --advanced --help-verbose``

Miscellaneous
-------------

Starting with VLC 0.8.0 you can access this interface through a network with a telnet-client by using the ``--rc-host localhost:port`` option.
