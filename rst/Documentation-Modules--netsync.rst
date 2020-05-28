{{Modulefirst_version=0.8.0description=Synchronise remote VLC
instances}} ==Introduction== Use this module to keep several clients
synchronised on a single VLC stream.

Common uses of this module are: \* Synchronising lots of loud PC
speakers during a party; \* Synchronising several computers playing
parts of a [[Documentation:Modules/wall|video wall]].

==Options==
{{Optiondefault=disabledname=netsync-master-ipdefault=""|description=Master
client ip address}}

==Examples== Here's a small example: :We're going to be listening to a
multicast stream. :Run a client as master syncronisation client (master
has IP address 192.168.0.1): %''' vlc udp://@239.255.1.1 --control
netsync --netsync-master ''' :And on the other clients: %''' vlc
udp://@239.255.1.1 --control netsync --netsync-master-ip 192.168.0.1 '''

{{Documentation footer}}
