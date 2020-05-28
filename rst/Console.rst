{{See also|Command line}} VLC has three terminal [[interface]] modules.
These are ''rc'', ''telnet'' and ''ncurses''.

== <span id="rc"></span> rc interface == {{See
also|Documentation:Modules/rc}}

The '''rc''' module is a interactive command line interface. It allows
you to type commands to make VLC do things. To start it, run <code>vlc
--intf rc</code>. This is the default interface if no [[GUI]]
environment is available. To get started type "help" followed by enter.
Starting with VLC 0.8.0 you can access this interface through a network
with a telnet-client by using the <code>--rc-host localhost:port</code>
option.

== <span id="ncurses"></span> ncurses interface == {{See
also|Documentation:Modules/ncurses}}

The '''ncurses''' module is something like a text-mode GUI, built with
the well-known ncurses library. Linux users should be familiar with this
kind of interface. This interface is not built by default, you need to
add <code>--enable-ncurses</code> to the configure call. To start VLC
with this interface run <code>vlc --intf ncurses</code>.

== <span id="telnet"></span> telnet interface == {{See
also|Documentation:Modules/telnet}}

The '''telnet''' interface will allow you to use the telnet command to
connect to VLC remotely from the network. It is comparable to the rc
interface, but less advanced. It can be launched by running VLC like:
<code>vlc --intf telnet</code>. Starting with the VLC 0.7.x-series, you
can control VLC's VLM-module with this interface to manage multiple
simultaneous streams. Notice that you should use the rc-interface if you
don't need this feature.

to launch VLC with telnet interface:
   {{%}} vlc -I telnet --telnet-password test

The telnet interface is essentially over a "raw [[TCP]] socket." To
interact with the instance at the command line (assuming the telnet
interface's address is <code>10.0.0.100:4212</code>):

   {{%}} nc 10.0.0.100 4212

[[Category:Interfaces]]
