{{RightMenu|documentation streaming howto toc}}

==Stream a file with VLC==

   {{%}} '''vlc -vvv video1.xyz --sout udp:192.168.0.42 --ttl 12'''

where: \* '''video1.xyz''' is the file you want to stream, \*
'''192.168.0.42''' is either: \*\* the [[IP address]] of the machine you
want to [[unicast]] to; \*\* or the DNS name the machine you want to
unicast to; \*\* or a [[multicast]] IP address. \* '''12''' is the value
of the [[TTL]] (Time To Live) of your IP packets (which means that the
stream will be able to cross 11 routers).

If you want to stream the file continuously, add the '''--loop'''
option.

Of course, you can add more options (like [[transcoding]], or streaming
to a TCP port, etc.), but this should get you started.

{{Documentation}}
