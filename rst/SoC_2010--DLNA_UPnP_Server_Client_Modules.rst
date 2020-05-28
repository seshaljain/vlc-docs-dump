.. raw:: mediawiki

   {{SoCProject|year=2010|student=[[User:Aust|Austin Burrow]]|mentor=[[User:thresh|Konstantin Pavlov]]}}

DLNA UPnP Server/Client Modules
===============================

Abstract
--------

The Digital Living Network Alliance (DLNA) offers a standard that many manufacturers use as a way to keep compatibility across different products that use UPnP. As of 2008, over 5,500 different devices and over 200 million sold products use the DLNA standard. This project will improve the current UPnP model, and apply the DLNA standard as Client/Server modules.

What I'm Working On
-------------------

.. table:: UPnP SD Client

   ==================== ===================================================================================================================================================================================================================================================================================================================================================================================================================================================== ====================
   \                    Description                                                                                                                                                                                                                                                                                                                                                                                                                                           Status
   ==================== ===================================================================================================================================================================================================================================================================================================================================================================================================================================================== ====================
   Item Duplication Bug The current implementation of services_discovery_AddItem does not allow items to be inserted anywhere into any sub-node. The current fix must rebuild the whole UPnP Server directory on every directory update. This is not an optimal solution because it causes a "refresh" to be seen in the playlist. This also causes the users selection to disappear, and the user is required to traverse through the directory tree to find the item again. On Hold (Semi-fixed)
   ==================== ===================================================================================================================================================================================================================================================================================================================================================================================================================================================== ====================

.. table:: UPnP DLNA Server

   ====================== =============================================================================================================================================================================================================================================================================================================================================================== ===========
   \                      Description                                                                                                                                                                                                                                                                                                                                                     Status
   ====================== =============================================================================================================================================================================================================================================================================================================================================================== ===========
   libdlna Implementation Implement the libdlna library, get simple test cases working.                                                                                                                                                                                                                                                                                                   Active
   Special Cases          Implement special cases for certain devices such as the Playstation 3 and XBOX 360. This will require the use of Wireshark, or some other packet sniffer to be able to sort out what's going on between the consoles and a fully supported DLNA server. This is a requirement because I am unable to get my hands on a free specification of the DLNA standard. Not Started
   ====================== =============================================================================================================================================================================================================================================================================================================================================================== ===========

Resources
---------

-  `Full UPnP Specification (Probably the best resource) <http://www.upnp.org/resources/upnpresources.zip>`__
-  `libdlna (by gxben, supports limited DLNA: PS3, XBOX 360) <http://libdlna.geexbox.org/>`__ IRC: `#geebox <irc://irc.freenode.net/geebox>`__
-  `Wikipedia UPnP <http://en.wikipedia.org/wiki/Universal_Plug_and_Play>`__
-  `Wikipedia DLNA <http://en.wikipedia.org/wiki/Digital_Living_Network_Alliance>`__
-  `Basic client implementation for VLC <http://wiki.videolan.org/SoC_2008/UPnP>`__
-  `Official DLNA Page (Requires payment to see spec!) <http://www.dlna.org/>`__
-  `Official UPnP Page (Provides free specification) <http://www.upnp.org/>`__
-  `libupnp (DLNA Support?) <http://pupnp.sourceforge.net/>`__

GSoC Timeline
-------------

Timeline includes GSoC key dates. I will edit this as time goes along.

**May 24** Start UPnP Server implementation

**July 12** Mid-Term Evaluations

**July 16** Mid-Term Evaluation Due Date

**August 9** Suggested Pencils Down - No new features, cleanup code, documentation, etc.

**August 16** Firm Pencils Down

**August 20** Final Evaluation Deadline

Contact
-------

Catch me on freenode as Aust. Email me at atburrow at gmail dot com.
