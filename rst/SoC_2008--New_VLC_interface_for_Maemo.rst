.. raw:: mediawiki

   {{SoCProject|year=2008|student=[[User:Phytos|Antoine Lejeune]]|mentor=Rafaël Carré}}

New VLC interface for Maemo
===========================

Abstract
--------

The goal is to create a new interface for VLC with Maemo, a Debian-based development platform for handheld devices used by Nokia N800 and N810 devices and to package VLC for this platform.

The main constraint are the small size of the screen which means the GUI must be thought specifically for this platform and the fact that the devices is not very powerful.

Details
-------

I will use Maemo 4 which is the last version and which is only compatible with the last version of the operating system of the internet tablet : OS2008 (http://nokia.com/os2008).

The application framework of Maemo is called Hildon and it is partially based on the same technologies that GNOME framework is built on. Hildon had several additions and enhancements to GNOME/GTK+ including his own widget set and other things.

At first, I intend to install Maemo SDK on my computer and to port and compile every essential dependencies of VLC to be able to build VLC core and try to play medias without any GUI.

Then, I will start the development of the new GUI with Hildon framework.

In the end, I will have to package VLC and its dependencies for Maemo which use the same packaging system as Debian.

Ideas
-----

Here are some quick ideas :

-  Interact with the built-in webcam easily
-  streaming
-  easy-playing of youtube video
-  other internet stream/radios

Optimizations
-------------

-  Display in framebuffer (the framebuffer vout of vlc needs some work to work correctly on the devices)
-  Better framedropping

Quick planning
--------------

-  **June 16** : start of the project (end of school term)
-  **July 1st** : first results --> http://phytos.dinauz.org/VideoLAN/Maemo/screenshots/maemo-vlc-embedded-video.png
-  **July 15th** : a usable interface
-  **End of July** : Webcam support + optimizations
-  **away from a internet connection** : first week of August
-  **End of project** : A Maemo package of the project :)
