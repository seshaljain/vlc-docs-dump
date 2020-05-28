(`Jump to pages in category <#mw-pages>`__) |VLMa.png|

What is VLMa?
-------------

`VLMa <https://www.videolan.org/projects/vlma/>`__ means VideoLAN Manager

VLMa is a Java application which provides a daemon and a web interface to manage several VLC streamers.

It is being used in École Centrale Paris to broadcast Satellite and TNT channels over the network.

Its source code is available under GPLv2 or later in VideoLAN's `Git <Git>`__, browsable on the web via `gitweb <https://git.videolan.org/?p=vlma.git;a=summary>`__.

``{{$}} git clone ``\ ```git://git.videolan.org/vlma.git`` <git://git.videolan.org/vlma.git>`__

The daemon is in charge of managing the streamers:

-  give orders using the telnet interface,
-  fallback whenever a server fails,
-  monitor streamers' state using SNMP,
-  draw RRD graphs.

The web module provides a user-friendly interface to communicate with the daemon. The communication between the daemon and the web interface is done using `RMI <wikipedia:Remote_Method_Invocation>`__.

Usage
-----

VLMa is not the right tool if what you want is a graphical front-end to VLM. You should only consider using VLMa if you have several streamers to manage simultaneously.

History
-------

VLMa development started in January 2006 under the impulsion of Sylvain Cadilhac, who was network administrator at `VIA Centrale Réseaux <http://www.via.ecp.fr>`__ and `VideoLAN <VideoLAN>`__ treasurer. There were around 10 servers in charge of streaming television and radio over the campus network, and the aim of the project was to provide a web interface to manage every server.

See also
--------

-  `VLMa documentation index <VLMa/Documentation>`__
-  `Ideas of interesting projects <VLMa/Projects>`__

Related links
-------------

-  `VLMa Trac <http://trac.videolan.org/vlma>`__.
-  `Nightly builds <http://nightlies.videolan.org/vlma/>`__.
-  `Project details <https://www.openhub.net/p/vlma>`__ at Open Hub.

`Category:VideoLAN projects <Category:VideoLAN_projects>`__

.. |VLMa.png| image:: VLMa.png

