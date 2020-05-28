{{Moduletype=InterfaceLua]] interpreter|sc=luaintf}}

== Options == {{Option value=string description=[[wikipedia:Lua
(programming language)name=lua-config default="" \|description=Lua
interface configuration string. Format is: <code><nowiki>'["<interface
module name>"] = { <option> = <value>, ...}, ...'</nowiki></code>. }}
{{Clear}}

== Lua HTTP == {{Moduletype=Interfacesc=luahttpname=http-password
default=NULL name=http-src default=NULL name=http-index default=disabled
\|description=Allow to build directory index }} {{Clear}}

== Lua Telnet == {{Moduletype=Interfacesc=luatelnetname=telnet-host
default="localhost" 127.0.0.1]]". }} {{Option value=integer max=65535
description=This is the [[TCP]] [[port]] on which this interface will
listen. It defaults to 4212. }} {{Option value=password description=A
single password restricts access to this interface. }} {{Clear}}

== Lua SD Module == {{Moduletype=Services discoverysc=luasd}} {{Option
value=string description= }} {{Clear}}

== Other submodules == {\| class="mw-datatable sortable" ! scope="col"
\| Name !! scope="col" \| Description !! scope="col" \| Capability !!
scope="col" \| Shortcut Lua Meta Fetcher \|\| Fetch meta data using lua
scripts \|\| meta fetcher \|\| (none) Lua Meta Reader \|\| Read meta
data using lua scripts \|\| meta reader \|\| (none) Lua Playlist \|\|
Lua Playlist Parser Interface \|\| stream_filter \|\| luaplaylist Lua
Art \|\| Fetch artwork using lua scripts \|\| art finder \|\| (none) Lua
Extension \|\| Lua Extension \|\| extension \|\| luaextension \|}

== Source code == \* {{VLCSourceFilemodules/lua}}

== See also == \* [[Documentation:Building Lua Playlist Scripts]] \*
[[Interfaces]] \* {{docmod|ncurses}}

{{Documentation}}
