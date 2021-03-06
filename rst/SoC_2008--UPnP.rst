.. raw:: mediawiki

   {{SoCProject|year=2008|student=[[User:Mr_Mirsal|Mirsal Ennaime]]|mentor=[[User:funman|Rafaël Carré]]}}

.. raw:: html

   <center>

http://people.videolan.org/~mirsal/images/soc_header.png

.. raw:: html

   </center>

--------------

GSoC - DLNA UPnP A/V integration
================================

I will use this page as a placeholder for details and progress information about my SoC 2008 project.

The project
-----------

Abstract
~~~~~~~~

Even if it is controverted, UPnP A/V Is a widely used standard set of protocols for networked digital audio and video equipment interoperability, thus making it almost a requirement digital media software that aim to become real part of the average multimedia home network. This project aims to implement at least the Media Server part in VLC media player, which will enable it to advertise and stream media to DNLA UPnP A/V enabled devices, such as the PlayStation 3.

Goals
~~~~~

At the end of the project, VLC media player will be able to advertise its currently playing stream or playlist / media library / discovered services to UPnP clients, that will be able to play them over the network, using DNLA UPnP A/V protocols. VLC media player will also expose its web based interface to permit FreeBox's FreePlayer[2]-like features for UPnP devices. As a secondary goal, VLC media player's current UPnP capabilities will be improved with room made for future further UPnP support (Media renderer, Control point...). The reference for success will be the ability to be discovered by, and stream to a PlayStation 3 device.

Details
~~~~~~~

There are two possible ways to achieve that goals: Implementing the needed services inside VLC media player as modules, written in C (This is the preferred one, and I'm assuming that it will be used), or integrating the Coherence[3] python UPnP framework. Basic UPnP support will be provided through libupnp[4], which is already used in VLC media player for UPnP devices discovery. The UPnP A/V MediaServer specification[5] will be implemented as a module which will provide the ConnectionManager[6], ContentDirectory[7] and AVTransport[8] services as described in their respective specifications. Media will be streamed using the VLC media player's streaming capabilities. The ConnectionManager service will implement the optional PrepareForConnection() action in order to select a streaming protocol matching with the remote device's capabilities, and to be able to stream to multiple UPnP devices simultaneously. The ContentDirectory service will expose the playlist, the media library and the discovered services for remote playback. The AVTransport service will enable playback control from a remote UPnP device. Libdlna[9] will be given a close look, may it be for linking to it, or to use it as reference code.

Schedule
~~~~~~~~

====================== ========================================================================================================================================================================================================
**May 26 to June 10:** very little work in this period (My vacations start as of June 10) Basically spec reading and current UPnP code hacking.
**June 10 to July 7:** Work work work on the ContentDirectory service (this is the most important part) and if time permits, I'll implement a ConnectionManager service stub in order to have the first real practical results.
**July 7 to July 14:** Mid-term evaluations (and some code too)
**July 14 to Aug 7:**  Work work work ConnectionManager and AVTransport.
**Aug 8:**             My birthday ^^
**Aug 9 to Aug 17:**   Fix bugs / finish what's late.
**Aug 18:**            Official SoC end.
**Aug 19 to Sep 1:**   Final evaluations, party, sleep, code on anything but UPnP
**Sep 1 to October:**  Work on the ControlPoint part ^^
\                     
====================== ========================================================================================================================================================================================================

Footnotes
~~~~~~~~~

-  [1] http://en.wikipedia.org/wiki/Digital_Living_Network_Alliance
-  [2] http://en.wikipedia.org/wiki/Freebox
-  [3] https://coherence.beebits.net/
-  [4] http://pupnp.sourceforge.net/
-  [5] http://www.upnp.org/specs/av/UPnP-av-MediaServer-v2-Device-20060531.pdf
-  [6] http://www.upnp.org/specs/av/UPnP-av-ConnectionManager-v2-Service-20060531.pdf
-  [7] http://www.upnp.org/specs/av/UPnP-av-ContentDirectory-v2-Service-20060531.pdf
-  [8] http://www.upnp.org/specs/av/UPnP-av-AVTransport-v2-Service-20060531.pdf
-  [9] http://libdlna.geexbox.org/

My progress
-----------

Git access
~~~~~~~~~~

You can checkout my git repository this way:

`` $ git clone ``\ ```git://git.videolan.org/vlc-mirsal.git`` <git://git.videolan.org/vlc-mirsal.git>`__

Progress overview
~~~~~~~~~~~~~~~~~

=================================================== ================================================================================================================================================================== ====== ====================
What                                                WHAT!?                                                                                                                                                             When   Status
=================================================== ================================================================================================================================================================== ====== ====================
Spec reading                                        Read the relevant UPnP A/V specifications, understand them fully and eventually become a UPnP A/V semi-god                                                         May    Done.
libupnp / VLC's upnp sd hacking                     Learn how to use libupnp. Hack the current VLC UPnP modules and fix the services discovery part in order to get used to writing UPnP features in VLC media player. May    Done.
Modules architecture / design                       Find the best way to integrate UPnP features in the current VLC architecture                                                                                       June   Done.
ContentDirectory service                            Implement the MediaServer ContentDirectory service                                                                                                                 June   In progress
ConnectionManager service                           Implement the MediaServer ConnectionManager service                                                                                                                July   Done.
AVTransport service                                 Implement the MediaServer AVTransport service                                                                                                                      July   Won't do during SoC.
Be late                                             Finish what needs to (I know I won't manage to stick to the schedule)                                                                                              August In progress
Polish                                              Fix bugs, do performance testing and stuff like that                                                                                                               August Won't do during SoC.
Bonus: start the ControlPoint device implementation If time permits ^^                                                                                                                                                 August Won't do during SoC.
\                                                                                                                                                                                                                            
=================================================== ================================================================================================================================================================== ====== ====================

Wtf am I doing \*right now\* ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Trying to solve problem with the PS3 being a bit too strict on DLNA specs.
