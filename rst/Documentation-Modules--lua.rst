.. raw:: mediawiki

   {{Module|name=lua|type=Interface|description=[[wikipedia:Lua (programming language)|Lua]] interpreter|sc=luaintf}}

Options
-------

.. raw:: mediawiki

   {{Option
   |name=lua-intf
   |value=string
   |default="dummy"
   |description=[[wikipedia:Lua (programming language)|Lua]] interface module to load
   }}

.. raw:: mediawiki

   {{Option
   |name=lua-config
   |value=string
   |default=""
   |description=Lua interface configuration string. Format is: <code><nowiki>'["<interface module name>"] = { <option> = <value>, ...}, ...'</nowiki></code>.
   }}

.. raw:: mediawiki

   {{Clear}}

Lua HTTP
--------

.. raw:: mediawiki

   {{Module|name=luahttp|type=Interface|description=Lua [[HTTP]]|sc=luahttp|sc2=http}}

.. raw:: mediawiki

   {{Option
   |name=http-password
   |value=password
   |default=NULL
   |description=A single password restricts access to this interface.
   }}

.. raw:: mediawiki

   {{Option
   |name=http-src
   |value=string
   |default=NULL
   |description=Source directory
   }}

.. raw:: mediawiki

   {{Option
   |name=http-index
   |value=boolean
   |default=disabled
   |description=Allow to build directory index
   }}

.. raw:: mediawiki

   {{Clear}}

Lua Telnet
----------

.. raw:: mediawiki

   {{Module|name=luatelnet|type=Interface|description=Lua [[Telnet]]|sc=luatelnet|sc2=telnet}}

.. raw:: mediawiki

   {{Option
   |name=telnet-host
   |value=string
   |default="localhost"
   |description=This is the host on which the interface will listen. It defaults to all network interfaces (0.0.0.0). If you want this interface to be available only on the local machine, enter "[[wikipedia:localhost|127.0.0.1]]".
   }}

.. raw:: mediawiki

   {{Option
   |name=telnet-port
   |value=integer
   |min=1
   |max=65535
   |default=4212
   |description=This is the [[TCP]] [[port]] on which this interface will listen. It defaults to 4212.
   }}

.. raw:: mediawiki

   {{Option
   |name=telnet-password
   |value=password
   |default=NULL
   |description=A single password restricts access to this interface.
   }}

.. raw:: mediawiki

   {{Clear}}

Lua SD Module
-------------

.. raw:: mediawiki

   {{Module|name=luasd|type=Services discovery|description=Lua SD Module|sc=luasd}}

.. raw:: mediawiki

   {{Option
   |name=lua-sd
   |value=string
   |default=""
   |description=
   }}

.. raw:: mediawiki

   {{Clear}}

Other submodules
----------------

================ ================================= ============= ============
Name             Description                       Capability    Shortcut
================ ================================= ============= ============
Lua Meta Fetcher Fetch meta data using lua scripts meta fetcher  (none)
Lua Meta Reader  Read meta data using lua scripts  meta reader   (none)
Lua Playlist     Lua Playlist Parser Interface     stream_filter luaplaylist
Lua Art          Fetch artwork using lua scripts   art finder    (none)
Lua Extension    Lua Extension                     extension     luaextension
================ ================================= ============= ============

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/lua/vlc.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFolder|modules/lua}}

See also
--------

-  `Documentation:Building Lua Playlist Scripts <Documentation:Building_Lua_Playlist_Scripts>`__
-  `Interfaces <Interfaces>`__
-  

   .. raw:: mediawiki

      {{docmod|ncurses}}

.. raw:: mediawiki

   {{Documentation}}
