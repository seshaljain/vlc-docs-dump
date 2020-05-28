.. raw:: mediawiki

   {{SoCProject|year=2008|student=[[User:Geal|Geoffroy Couprie]]|mentor=Jérôme Decoodt}}

WinCE Port of VLC
=================

Abstract
--------

The VLC media player has been port to many different platforms, but it lacks Windows CE support since some versions. This project aims at making VLC work on a Windows CE platform, with a few features:

-  RTSP
-  H264
-  Snapshots
-  Playlist
-  Rebuild of interface to adapt it to small screens

Calendar
--------

**May 26 :** Beginning of SoC

**May 27 :** Beginning of holidays

**June 23 :** Final exams

**June 25 :** What is done so far: the LibVLC and nearly all modules are compiled. I run some tests on LibVLC, to make sure that it will look good. I've begun the cross compilation of libs, like ffmpeg. The graphical interface is running, but is uglier than anyone could imagine. Working on VLC is fun, and I enjoy my summer :)

**July 14 :** Mid-term evaluations deadline

**September 1 :** Final evaluation deadline

**September 15 :** Starting the third year at the "Ecole Centrale de Lille"

TODO list
---------

=================== ================================================================================================================================ ============================= ===========
What                WHAT!?                                                                                                                           When                          Status
=================== ================================================================================================================================ ============================= ===========
Learning            Read materials about Windows CE, subtle things, little bit of hacking                                                            May-June                      In progress
Compilation process Design an easy compilation, deployment, debugging process, and make a doc about it                                               May-June                      In progress
Contribs            Build a contrib package for Windows CE                                                                                           All Summer long               In progress
Naked VLC           Build a minimalistic VLC, with an ugly interface and very few libraries                                                          May, June                     In progress
Adding features     Add one feature, release a version; add one feature, release a version; make a cup of coffee; add one feature, release a version All Summer long               In progress
Interfaces          Write a nice looking and intuitive interface for phones, and one for other types of Windows CE devices                           July                          not started
Cleaning the code   Fixes, finish the interface, hoping there are no crash, resetting my phone                                                       August                        not started
Let's play          Add funny features: making a Windows CE streaming server, add support of Camera, GPS                                             August(if I have enough time) not started
Build bot           Add the Windows CE port to buildbot                                                                                              September                     not started
Community           Develop for VLC, and not only on Windows CE                                                                                      Post GSoC                     In progress
=================== ================================================================================================================================ ============================= ===========

Contrib package
---------------

Actual state of the contrib package for VLC on Windows CE:

-  libiconv
-  ffmpeg

What will be used
-----------------

This is the list of the tools that will be used to achieve this project:

-  `Cygwin <http://www.cygwin.com/>`__, a Linux-like environment for Windows
-  `CeGCC <http://cegcc.sourceforge.net/>`__, a cross-compiler for Windows CE based devices
-  `Microsoft Visual Studio 2008 <http://msdn2.microsoft.com/fr-fr/vstudio/default.aspx>`__ as IDE
-  `Microsoft Device Emulator <http://msdn2.microsoft.com/fr-fr/library/aa188148.aspx>`__, an emulator for Windows CE and Windows Mobile devices
-  a `HTC P3600 Trinity <http://www.htc.com/FR/Product.aspx?id=16394>`__, for the tests on real hardware
