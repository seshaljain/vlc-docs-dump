.. raw:: mediawiki

   {{SoCProject|year=2011|student=[[User:AlexanderS|Alexander Sulfrian]]|mentor=Ilkka Ollakka}}

Porting PythonNetMD to C to build a new libnetmd
================================================

Abstract
--------

The idea is to port the `NetMD python scripts <https://wiki.physik.fu-berlin.de/linux-minidisc/doku.php?id=netmdpython>`__ from the `linux-minidisc <https://wiki.physik.fu-berlin.de/linux-minidisc>`__ project (for communication with Sony NetMD MiniDisc devices) to a C-based library that could be used by VLC and any free media application.

Back in 2001 `1 <http://minidisc.org/part_Sony_MZ-N1.html>`__, Sony started equipping their MiniDisc Walkman and decks with an USB socket and called the technology NetMD. NetMD is basically an AV/C-over-USB-based protocol which allows to send audio data to compatible devices to record them at speeds faster than realtime while remaining backwards compatible with previous MiniDisc equipment. The motivation behind NetMD was to make MiniDisc more attractive with the advent of mass-storage-based portable music players like the iPod.

Since NetMD devices still kept the old MiniDisc format, it is not possible to transfer audio data to the device without additional software. On Windows, this is achieved with the infamous software SonicStage `2 <http://en.wikipedia.org/wiki/SonicStage>`__. Naturally, this software was released for Windows only and development has ceased around 2007 with version 4.3 (4.4 in Japan). People who want to continue using their NetMD equipment are thus stuck using a compatible version of Windows. Since SonicStage uses a lot of dirty hacks (it has to be run as Administrator for full access to the Windows registry) and the NetMD devices require special drivers, the list of compatible Windows versions is quite narrow, namely 32-bits only. Naturally, Linux and MacOS aren't supported at all.

A project on Sourceforge called *libnetmd* `3 <http://sourceforge.net/projects/libnetmd/>`__, was started in 2004 to start developing a free implementation of the NetMD protocol. Since the NetMD protocol is based on a standard (AV/C-over-USB), the protocol can be implemented right a away. However, libnetmd always suffered from the fact, that music transfers to the NetMD devices are encrypted. The original libnetmd therefore never allowed to transfer any tracks to the devices. However, the implementation allowed things like renaming tracks or remote-controlling the NetMD devices.

In 2009, a new attempt for a free implementation of not only the NetMD protocol but also for HiMD support, the mass-storage-based successor to NetMD, was started. The project is called linux-minidisc `4 <https://wiki.physik.fu-berlin.de/linux-minidisc>`__ and has made great progress in completely reverse-engineering the NetMD protocol and the HiMD format, as well as the underlying encryption mechanisms.

While HiMD support has been implemented in a C library called *libhimd*, NetMD can be used only through a number of inconvenient Python scripts `5 <https://wiki.physik.fu-berlin.de/linux-minidisc/doku.php?id=netmdpython>`__. In fact, the Python implementation of the NetMD is complete and works on all devices. However, many parts of the code are highly experimental even though they work and most average users prefer easy-to-use GUI-based software, which will run on their platform of choice. For that, Python is not very eligible, as it is not available by default on the largest platform, Windows.

The goal of this GSoC task shall therefore be porting the PythonNetMD code from the linux-minidisc project into a C library which is supposed to replace the no longer maintained libnetmd `6 <https://wiki.physik.fu-berlin.de/linux-minidisc/doku.php?id=portingnetmd>`__. Eventually, both HiMD and NetMD will be readily available from the linux-minidisc project and can be easily adopted to software applications like VLC and other free media players.

Background and motivation
-------------------------

Python NetMD is

-  command line interface only
-  difficult to integrate with QHiMDTransfer (graphical transfer application for HiMD)
-  requires Python (version dependency)
-  requires some basic knowledge on setting up Python
-  not intuitively usable
-  code is in some parts highly experimental

Current status
--------------

The current Python NetMD implementation allows both downloads (all NetMD models) as well digital uploads (MZ-RH1/MZ-RH200 models only) as well as titling, listing and editing of tracks as well as remote controlling NetMD units. Analog capture for upload is supported for models other than MZ-RH1/MZ-RH200. Download code contains a valid but unencumbered root key to allow necessary encryption during transfers. The download code itself is highly experimental, however.

There is already a recent attempt to port the Python code to C. The resulting tarball can be downloaded `here <http://users.physik.fu-berlin.de/~glaubitz/linux-minidisc/mdlib.tar.gz>`__. However, it is highly recommend to use the old, much more complete *libnetmd* (see `7 <http://libnetmd.sourceforge.net/>`__) as a basis and extend it with transfer capabilities.

Overview Python NetMD
---------------------

The current NetMD implementation `8 <https://wiki.physik.fu-berlin.de/linux-minidisc/doku.php?id=netmdpython>`__ in Python is divided into several scripts

Utilities:

-  *lsmd.py* - list the contents of any NetMD
-  *upload.py* - transfer tracks from NetMD to the computer (works with MZ-RH1 Walkman only)
-  *downloadhack.py* - allows transfer of tracks from the computer to NetMD (using unencumbered keys)
-  *dump_md.py* - allows \**analogue*\* transfers of tracks from NetMD to the computer (any NetMD Walkman)
-  *lsusb.py* - sample implementation of lsusb command using usb1.py
-  *mdctl.py* - pdb-based command line to test libnetmd.py methods

Libraries:

-  *libnetmd.py* - implementation of a NetMD library in Python (core module)
-  *libusb1.py* - Ctypes-based python wrapper around libusb1
-  *usb1.py* - object definitions for libusb1.py functions

Proposed project plan
---------------------

Since there is already a C library for NetMD available (`9 <http://sourceforge.net/projects/libnetmd/>`__), it would be good idea to use this as a basis for a new implementation instead reinventing the wheel. This old implementation already allows renaming, moving, deleting tracks and so on (see `10 <http://libnetmd.sourceforge.net/>`__) but lacks the capabilities to transfer tracks *to the device* (in Sony terminology this is referred to as **download**) and to transfer tracks *from the device* (Sony calls this **upload**; upload is supported by the MZ-RH1/200 devices **only**).

Considering the old *libnetmd* is used as a basis, the first step would be to import the source code of this library into the git repository of *linux-minidisc*. Then, since the library has already been without maintenance since 2004, the second step would be compiling the library on a current Linux installation and fix any compiler issues that might arise. After the library has been verified to work in a current environment, it should be tested to work with Sony's MZ-RH1 MiniDisc Walkman (the latest and also last MiniDisc device available) and any problems that might arise should be patched.

After the previous rejuvenation steps, *libnetmd* is now ready to be extended with download and upload capabilities (note the terms mentioned above), with the help of the PythonNetMD code `11 <https://wiki.physik.fu-berlin.de/linux-minidisc/doku.php?id=netmdpython>`__ which serves as sample code for an implementation of both download and upload capabilities (see above summary of the Python scripts available). Since there is with the MZ-RH1 (the MZ-RH200 is a RH1 with different accessoires shipped) essentially only one MiniDisc model available which supports uploads, it's preferred to work on the implementation of the download code first.

While the upload code works unencrypted and thus without the need of any encryption keys, downloads are encrypted and require the data to be encrypted with a key accepted by the NetMD device. Since the keys are proprietary secrets of Sony Corp., we cannot use the original keys for the encryption. Luckily, the keys accepted by the NetMD hardware for an encrypted transfer can be calculated dynamically. In fact, the root key used by the *downloadhack.py* was encrypted with the help of a secret Sony master key. However, it is not necessary to know the secret Sony key, but it is enough to use the key that is already provided by *downloadhack.py*. Since we created this key ourselves, we do not have to fear any issues regarding copyright infringement of proprietary code and/or information from Sony Corp.

Summary
-------

To summarize the proposed steps for the port:

#. import *libnetmd* `12 <http://sourceforge.net/projects/libnetmd/>`__ into *linux-minidisc*, subfolder *libnetmd* (analogous to *libhimd*)

      Done

#. get *libnetmd* compile and work on a current release of any Linux distribution (might already work without patching)

      Done

#. get *libnetmd* to work properly with the Sony MZ-RH1 Walkman (see `13 <http://libnetmd.sourceforge.net/>`__ for required functionality)

      Working: rename tracks, move tracks, play, fforward, rewind, pause, stop, setplaymode, delete tracks, print TOC
      NOT Working: everything with groups (upload/download as expected)

#. with the help of the PythonNetMD code `14 <https://wiki.physik.fu-berlin.de/linux-minidisc/doku.php?id=netmdpython>`__ (*downloadhack.py*), extend *libnetmd* with download capabilities
#. **optional**: implement upload capabilities for MZ-RH1 Walkman with the help of *upload.py*
#. **bonus level**: adapt *qhimdtransfer* to work with the new *libnetmd*

For documentation, please refer to the the wiki page `15 <https://wiki.physik.fu-berlin.de/linux-minidisc/doku.php?id=netmdlinux>`__ with many extremely **helpful** links for further reading regarding NetMD (includes specifications and patents) and ask any questions on the list `16 <https://lists.fu-berlin.de/listinfo/linux-minidisc>`__ and/or the IRC channel (#linux-mindisc on FreeNode).
