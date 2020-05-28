.. raw:: mediawiki

   {{See also|Category:Interfaces|Category:Control VLC}}

Interfaces are the way you interact with . Like anything else in VLC, they are modules, which allows for their interchangeability (`see below <#Using>`__).

Main interfaces
---------------

VLC has four main graphical interfaces:

-  The `Qt Interface <Qt_Interface>`__ (qt) is the default interface on `Linux <Linux>`__ and `Windows <Windows>`__ starting with version 0.9.0.

   Used to be `wxWidgets Interface <wxWidgets_Interface>`__ (wx) before.

-  The `skins2 Interface <Skins>`__ is an interface where you can customize VLC's look (works on Linux and Windows).
-  The `macOS Interface <macOS_Interface>`__ is the default (and only) graphical interface on `macOS <macOS>`__.
-  The `BeOS Interface <BeOS_Interface>`__ is the default (and only) graphical interface on `BeOS <BeOS>`__.

Full list
---------

Besides the above main interfaces, VLC contains many more:

=============================== =============================================================================================================================
**qt**                          Current (>=0.9.0) default `Qt4 <https://www.qt.io/>`__ interface on `Linux <Linux>`__ and `Windows <Windows>`__.
**wx**                          Previous (<0.9.0) default `wxWidgets <http://www.wxwidgets.org/>`__ interface on `Linux <Linux>`__ and `Windows <Windows>`__.
**skins2**                      Load VLC with a `skin <skin>`__. (Linux and Windows only)
**macosx**                      Default `Mac OS X <Mac_OS_X>`__ interface.
**minimal_macosx**              Minimal `Mac OS X <Mac_OS_X>`__ interface.
**beos**                        Default `BeOS <BeOS>`__ interface.
**http**                        `Web Interface <Web_Interface>`__, used for controlling VLC from over a network.
**gestures**                    `Mouse Gestures <Mouse_Gestures>`__, where you can control VLC by moving the mouse
**rc**, **ncurses**, **telnet** `Console Interfaces <Console>`__, non-graphical interfaces.
**showintf**                    Show interfaces module.
**hotkeys** and **joystick**    Control VLC with the keyboard/joystick (see `HotKeys <HotKeys>`__).
**dummy**                       Don't use an interface (`HotKeys <HotKeys>`__ still available).
=============================== =============================================================================================================================

Listing the available interfaces
--------------------------------

To get a list of available interfaces, running VLC with the ``-l`` option:

``{{%}} vlc -l``

This also displays the `muxers <muxers>`__ and `encoders <encoders>`__/`decoders <decoders>`__ and puts it in a file called ``vlc-help.txt``. On Linux, run

``{{%}} vlc -l | grep -iF interface``

to display the interfaces.

 Using an interface
------------------

To run VLC with a different primary interface, use the following command:

``{{%}} vlc --intf ``\ *``name``*

You can also use

``{{%}} vlc -I ``\ *``name``*

You can also change the default in the `Preferences <Preferences>`__.

However, you can also launch more than one interface:

``{{%}} vlc --intf qt --extraintf sap,telnet,http``

This will launch VLC with the default Qt interface, but will also launch the `SAP <SAP>`__, `telnet <telnet>`__ and `web interface <web_interface>`__ in addition to the Qt one. The default for this can also be changed in the preferences.

Note that if you only use the `dummy <dummy>`__ interface, you won't be able to tell vlc to quit (except watching a video). You may have to break it manually with Ctrl+C; or use ``vlc://quit`` as the last item on the playlist.

`\* <Category:Control_VLC>`__ `\* <Category:Interfaces>`__
