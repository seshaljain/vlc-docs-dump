{{RightMenu|documentation streaming howto toc}}

==Streaming over IPv6==

This chapter covers the specifics of streaming over IPv6. You should
still read the previous chapters if you are not comfortable with
streaming in general.

===Requirements===

You will obviously need an IPv6-aware operating system. That includes
Windows XP/2003, Linux 2.6, Mac OS X (starting from version 10.2).
Windows 2000 and Linux 2.4 are supported too, but their IPv6 stacks are
not as good, so upgrade if you can. IPv6 must be properly configured and
working on your system and network.

On Linux, the ''ipv6'' kernel module must be loaded (or compiled-in). On
Windows, the IPv6 protocols suite can be installed by running "ipv6
install" from the command line, or through the Network configuration
panel.

Note: Under Windows 2000, you must add by hand a default multicast IPv6 route, with the following command:
   # '''ipv6 rtu ff::/8 4'''

where the last number (''4'' in this example) is the number of your true
IPv6 interface. To have a list of your IPv6 interfaces, run '''ipv6
if'''

Warning: Under Windows XP SP1, you may have problems with a hidden IPv6
firewall. To solve the problem, go to the list of Windows Services and
stop the IPv6 firewalling service. You should consider upgrading to
Service Pack 2 which provides an integrated IPv4/IPv6 firewall that can
be configured through the GUI.

Warning: If you are using VMware under Linux, you will have to stop
VMware and unload the VMware kernel modules, because we noticed it
prevented IPv6 streaming!

===Limitations===

There are still some features of the VLC media player which do not
support IPv6. In particular, it is not possible to use RTSP over IPv6
because the underlying library, Live.com, does not support IPv6 at the
time of writing.

Additionally, note that at the moment, VLC defaults to using IPv4 mostly
every, as it is what most people uses. That might be changed to
something more transparent in future versions.

===Streaming with VLC===

====With the Streaming Wizard (GUI)====

The streaming wizard accepts IPv6 addresses between braces, for example:
'''[2002:8ac3:802d:1242:211:11ff:fe25:e6b4]'''. If you specify a
link-local address, you will most likely need to specify the networking
interface to use. On Unix, that can be done this way:
'''[fe80::211:11ff:fe25:e6b4%eth0]''' to attach to eth0. Similarly, on
Windows, you may specify '''[fe80::211:11ff:fe25:e6b4%1]''' where 1 is
the number of the network interface as defined by the operating system.

If you're streaming over HTTP, note that IPv6 is automatically used by
default (so that both IPv6 and IPv4 clients will be allowed).

If you want to specify DNS hostname, keep in mind that the VLC defaults
to IPv4 resolution. You must either specify hostnames that only resolves
to IPv6 addresses, or enable the "Force IPv6" ''advanced'' option in
''Preferences / General Settings / Input''.

====From the command-line====

The '''--ipv6''' command line option force the use of IPv6 by default
(ie. IPv6 is always attempted before IPv4).

   % '''vlc -vvv video1.xyz --ipv6 --sout udp:%5Bff08::1] --ttl 12'''

where: \* '''video1.xyz''' is the file you want to stream (you can also
put '''dvdsimple:/dev/dvd''' to stream a DVD or any other input
configuration), \* '''ff08::1''' is either: \*\* the IPv6 address of the
machine you want to unicast to; \*\* or the multicast IPv6 address. \*
'''12''' is the value of the TTL (Time To Live) of your IP packets
(which means that the stream will be able to cross 11 routers).

Note: Under Unix/Linux, you may have to protect the square brackets around the IPv6 address:
   % '''vlc -vvv video1.xyz --ipv6 --sout
   `udp:\[ff08 <udp:\%5Bff08>`__::1] --ttl 12'''

Note: You may have to specify the output network interface:
   % '''vlc -vvv video1.xyz --ipv6 --sout udp:%5Bff08::1%eth0] --ttl
   12'''

where '''eth0''' is the name of the network interface (under Linux the
network interfaces are named '''ethX''', under Mac OS X it's '''enX'''
and under Windows it's '''X''', where '''X''' is the appropriate
number).

===Receiving an IPv6 stream===

====With the graphical user interface====

Select File / Open Network Stream. To receive an UDP/RTP unicast stream
sent to your system, you should select the Force IPv6 option (and
possibly adjust the destination UDP port). To receive an UDP multicast
stream, select the UDP/RTP Multicast option, and specify the multicast
address to subscribe to inside square brackets. The IPv6 addresses
syntax is the same as that explained in the ''Streaming over IPv6''
section of this chapter.

====From the command line====

As for streaming, the '''--ipv6''' command line option force the use of
IPv6 by default (i.e., IPv6 is always attempted before IPv4).

   % '''vlc -vvv --ipv6 udp:@%5Bff08::1]'''

Under Unix/Linux, you may have to protect the square brackets around the IPv6 address:
   % '''vlc -vvv --ipv6 `udp:@\[ff08 <udp:@\%5Bff08>`__::1]'''

You may have to specify the output network interface:
   % '''vlc -vvv video1.xyz --ipv6 --sout udp:%5Bff08::1%eth0] --ttl
   12'''

where '''eth0''' is the name of the network interface (under Linux the
network interfaces are named '''ethX''', under Mac OS X it's '''enX'''
and under Windows it's '''X''', where '''X''' is the appropriate
number).

{{Documentation}}
