.. raw:: mediawiki

   {{See also|Documentation:Modules/ncurses|Documentation:Modules/http intf}}

.. raw:: mediawiki

   {{Module|name=telnet|type=Control interface|description=Control VLC via a telnet connection}}

The telnet module `communicates with VLC <Control_VLC_instance>`__ over a network connection using the `telnet <wikipedia:telnet>`__ protocol. The original module was provided until 1.1.0, when it was re-written in `Lua <wikipedia:Lua_(programming_language)>`__. The old module was renamed to oldtelnet and removed in 2.0.0.

Telnet should not be used for sensitive applications.

To find module information on the command-line for VLC 2.0.0 and above, use ``vlc -p lua --advanced --help-verbose`` and look for the *Lua Telnet* section.

Options as of 3.0.6 are listed below:

.. raw:: mediawiki

   {{Documentation footer}}
