.. raw:: mediawiki

   {{Module|name=netsync|first_version=0.8.0|type=Video output|description=Synchronise remote VLC instances}}

Introduction
------------

Use this module to keep several clients synchronised on a single VLC stream.

Common uses of this module are:

-  Synchronising lots of loud PC speakers during a party;
-  Synchronising several computers playing parts of a `video wall <Documentation:Modules/wall>`__.

Options
-------

.. raw:: mediawiki

   {{Option|name=netsync-master|default=disabled|description=Act as master}}

.. raw:: mediawiki

   {{Option|name=netsync-master-ip|value=string|default=""|description=Master client ip address}}

Examples
--------

Here's a small example:

   We're going to be listening to a multicast stream.
   Run a client as master syncronisation client (master has IP address 192.168.0.1):

``%''' vlc ``\ ```udp://@239.255.1.1`` <udp://@239.255.1.1>`__\ `` --control netsync --netsync-master '''``

   And on the other clients:

``%''' vlc ``\ ```udp://@239.255.1.1`` <udp://@239.255.1.1>`__\ `` --control netsync --netsync-master-ip 192.168.0.1 '''``

.. raw:: mediawiki

   {{Documentation footer}}
