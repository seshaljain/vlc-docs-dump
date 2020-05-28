.. raw:: mediawiki

   {{SoCProject|year=2010 |student=[[User:Skelet|Casian Andrei]] |mentor=Hugo Beauzee-Luyssen }}

Phonon High-level Capture API
=============================

Abstract
--------

The goal of this project is to enable Phonon applications to access and display input devices, like webcams. The Phonon code-base is well designed and flexible, and apparently no major modifications are needed to the current API. The ease of use for the Phonon application developer is a priority. Features implemented in Phonon will be implemented in the Phonon-VLC back-end in parallel. Various device classes should be supported.

Information
-----------

The exam session lasts here most of June, so I won't be able to work at full capacity during this time (I hope I can achieve 50%-75% of the July work time).

If extra time remains, I will work on improving the overall quality of Phonon.

Timeline
--------

The following timeline may be a bit optimistic, but I will try to respect it. It will be revised during the summer if neccessary. By revised I mean adding smaller tasks, not removing tasks or delaying.

==================== =========== ====================================================================
Date                 Status      Description
==================== =========== ====================================================================
May 10 - May 24      Completed   Setup development environment, test things, play with the code
May 24 - June 15     V4L ok      Setup MediaSource to handle capture devices, implement in Phonon-VLC
June 5 - June 15     V4L ok      Implement API to get information about capture devices
June 15 - June 25    Completed   Link video and audio capture devices in AVCapture
June 25 - July 12    Completed   Test, improve, simplify the classes implemented previously
July 12 - July 25    Completed   Improve Phonon-VLC - document code
July 12 - July 25    In progress Improve Phonon-VLC - implement some lacking API
July 29 - August 9   In progress Implement ALSA or pulse capture
July 25 - August 16  Cancelled   Implement the capture API in other backends
August 9 - August 16 Not started Improve Phonon-VLC or capture
==================== =========== ====================================================================

Repositories
------------

There is one repo for Phonon and one for the Phonon-VLC backend.

-  http://gitorious.org/~skelet/phonon/soc-phonon-capture-api
-  http://gitorious.org/~skelet/phonon/soc-phonon-vlc-capture-api

Status report
-------------

May 31
~~~~~~

One week has passed and I still determining what I can use from Phonon::Experimental. There is capture-api code in there, and I need to see if it works or not and how it works. I can't start writing code around without knowing what is already done. Unfortunately the stupid school keeps throwing stuff at me (until June 2) and progress is slow. However, I want to get over this study and test phase by the start of next week. Now I'm putting together a couple of primitive apps to test things about the existing capture-api code.

June 6
~~~~~~

During this week I've investigated more into what exists regarding capture in Phonon::Experimental. I've created another executable test in phonon/experimental/tests, that retrieves the lists of devices and their properties for audio output, capture, and video capture. I've implemented a couple of simple methods to do this in Phonon::Experimental::GlobalConfig. It appears that the devices and properties are working (they look the same as in the KDE config center). I need to find a way to test this with a more complicated device configuration, perhaps without PulseAudio. After that, I will have to implement getting the capture device list for Phonon-VLC.

Next week I plan to work with the MediaObject / MediaSource classes, to try to make them to use VLC to capture audio.

June 14
~~~~~~~

Unfortunately much of this week I was bogged down in trying to learn for an exam, but I also managed to implement things in Phonon-VLC. Not as much as I hoped, but now the lists of available v4l capture devices appear to be working (with one small device id issue). I should try to step up work this week, by disregarding (a bit) another exam. The small device id's issue will be fixed and I can start working on the fun part.

June 22
~~~~~~~

The primitive testing application using Phonon with Phonon-VLC shows up images from a webcam. But the device list is not easy to use and improvements have to be made. Additional improvements are needed in the other areas of the code. Some cleanup in Phonon::Experimental regarding VideoCaptureDevice should also be done.

I will start working on these various improvements this week.

June 28
~~~~~~~

The improvements have been made. V4L2 devices appear to be working properly with Phonon and Phonon-VLC. The device list now shows a normal device name, and a simple device description, not something like /dev/video0. There are #ifdef's disabling video capture or audio capture or both.

Audio capture is completely untested, but the code is the same as for video, so it should normally work. I need to look for libaudiodevices or something to grab a device list not related to V4L.

I will also start working on the Experimental::AVCapture class. At a first glance, there is not much to do there.

July 12
~~~~~~~

I have documented most of the Phonon-VLC code with Doxygen. I've gained good understanding about how the whole Phonon system works. Previously I was planning to work on AVCapture, but I found out that I had insufficient knowledge about Phonon and Phonon-VLC to do it. That is why I did the documentation stuff.

Now I need to decide on what to work next and start working on it. Options are:

-  Test audio capture / audio data output, fix any issues
-  Work on the AVCapture class and implement AVCaptureInterface in Phonon-VLC
-  Try to fix / implement disabled / incomplete features for Phonon-VLC
-  Fix the Phonon tests
-  Implement more device categories, other than V4L, for other platforms

The initial timeline had to be modified to adapt to the current situation.

By tommorow I should have decided what to do next, and start working.

July 19
~~~~~~~

Now working on the AVCapture class. I have made a simple implementation in Phonon-VLC, and now I am testing and fixing errors and omissions. Ideally, it will be tested at the same time with audio capture. There were some delays induced by me trying to package libglew for Ubuntu on the buildservice by myself :(, and an evil illusive typo :( . Despite this, I am feeling confident.

For working on AVCapture, I have created an experimental subdir in Phonon-VLC with a CMake option to enable it, and a PHONON_VLC_EXPERIMENTAL definition. This can be used when implementing some other experimental classes.

July 26
~~~~~~~

Finished work on AVCapture, but is not of any practical use until audio capture is functional. Now I'm thinking about audio capture. Part of the work implied improvements for the merge request to preserve ABI for Experimental as much as possible. The merge request will be updated soon. I also need to think more about whether to keep v4l2devices.h/cpp or to rename it and include searching for other classes of devices.

August 2
~~~~~~~~

During the last week I spent more time than expected on setting up development stuff on the new system. At least it compiles 10x faster than the old one. One day was for installing and configuring the OS, one day for copying and compiling phonon and phonon-vlc, one day for doing battle with vlc/extras/contrib, one day with kde trunk trouble, one day for issues regarding phonon + kde + pulse + undefined symbol stuff. I also compiled pulseaudio. One day I was too tired from these issues and now I finally started with ALSA capture. The device list for these is in kaudiodevicelist, in kdebase/runtime/phonon, and it has something to do with the platform plugin, which is currently unexplored "territory".

I managed to do some improvements on my work in Phonon-VLC. Ugly looking v4l2 stuff are now only in devicescan.h/cpp.

Currently I need to figure out exactly how this Phonon platform plugin works and use it for ALSA devices in Phonon-VLC.

August 9
~~~~~~~~

Improved the previous work and implemented alsa capture. From the Phonon and Phonon-VLC point of view, it works correctly. However, unfortunately, although VLC sais it has opened the device without problems (both when used from Phonon-VLC or when used normally), but no sound is captured. arecord works fine. I attempted to investigate in VLC's sources and arecord's sources but they are too complex to give me an idea about what happens.

Basically, the work for Phonon and Phonon-VLC regarding capture is completed, I will update the merge request soon. But this no sound issue remains. I need to test this on another system and investigate more deeply.

August 16
~~~~~~~~~

Made final improvements on the merge request. There were a number of small things that shouldn't be there (forgotten from early work). The objectives were completed, in my opinion. It was a great SoC :D
