{{SoCProjectstudent=[[User:Austmentor=[[User:thresh|Konstantin
Pavlov]]}}

=DLNA UPnP Server/Client Modules=

==Abstract== The Digital Living Network Alliance (DLNA) offers a
standard that many manufacturers use as a way to keep compatibility
across different products that use UPnP. As of 2008, over 5,500
different devices and over 200 million sold products use the DLNA
standard. This project will improve the current UPnP model, and apply
the DLNA standard as Client/Server modules.

==What I'm Working On== {\| class="wikitable" -! Item Duplication Bug \|
The current implementation of services_discovery_AddItem does not allow
items to be inserted anywhere into any sub-node. The current fix must
rebuild the whole UPnP Server directory on every directory update. This
is not an optimal solution because it causes a "refresh" to be seen in
the playlist. This also causes the users selection to disappear, and the
user is required to traverse through the directory tree to find the item
again. \|\| style="background-color: yellow; font-weight: bold;" \| On
Hold (Semi-fixed) \|}

{\| class="wikitable" -! libdlna Implementation \| Implement the libdlna
library, get simple test cases working. \|\| style="background-color:
green; font-weight: bold;" \| Active Implement special cases for certain
devices such as the Playstation 3 and XBOX 360. This will require the
use of Wireshark, or some other packet sniffer to be able to sort out
what's going on between the consoles and a fully supported DLNA server.
This is a requirement because I am unable to get my hands on a free
specification of the DLNA standard. \|\| style="background-color: red;
font-weight: bold;" \| Not Started \|}

==Resources== *[http://www.upnp.org/resources/upnpresources.zip Full
UPnP Specification (Probably the best
resource)]*\ [http://libdlna.geexbox.org/ libdlna (by gxben, supports
limited DLNA: PS3, XBOX 360)] IRC: [irc://irc.freenode.net/geebox
#geebox] *[http://en.wikipedia.org/wiki/Universal_Plug_and_Play
Wikipedia
UPnP]*\ [http://en.wikipedia.org/wiki/Digital_Living_Network_Alliance
Wikipedia DLNA] *[http://wiki.videolan.org/SoC_2008/UPnP Basic client
implementation for VLC]*\ [http://www.dlna.org/ Official DLNA Page
(Requires payment to see spec!)] *[http://www.upnp.org/ Official UPnP
Page (Provides free specification)]*\ [http://pupnp.sourceforge.net/
libupnp (DLNA Support?)]

==GSoC Timeline== Timeline includes GSoC key dates. I will edit this as
time goes along.

'''May 24''' Start UPnP Server implementation

'''July 12''' Mid-Term Evaluations

'''July 16''' Mid-Term Evaluation Due Date

'''August 9''' Suggested Pencils Down - No new features, cleanup code,
documentation, etc.

'''August 16''' Firm Pencils Down

'''August 20''' Final Evaluation Deadline

==Contact== Catch me on freenode as Aust. Email me at atburrow at gmail
dot com.
