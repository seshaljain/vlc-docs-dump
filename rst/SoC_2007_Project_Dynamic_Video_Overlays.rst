.. raw:: mediawiki

   {{SoCProject|year=2007|student=[[User:Avacore|Søren Bøg]]|mentor=[[User:Dionoea|Antoine Cellerier]]}}

Intro
-----

I (`Søren Bøg <User:Avacore>`__) will be using this area to describe and track my progress, on implementing dynamic overlays in VLC, for Google Summer of Code 2007.

Goal
----

The goal of this is to create a video filter for VLC, allowing third party applications to overlay dynamic images on top of the VLC video output.

Details
-------

The idea here is to provide VLC with a video filter that allows a third party application (hereafter the controller) to request an overlay on top of the video that VLC is displaying. The controller is then handed a piece of shared memory with a specified pixel format. The controller may then draw all that it desires to this shared memory, Finally when the shared memory has been written to, the controller will notify VLC of the change, and VLC will then composite the overlay into subsequent frames, or at least until instructed to do something else by the controller.

This is somewhat similar the the roles that bomvl, bmovl2 and vf_overlay play for MPlayer.

Why
---

Well, because I can, why else? More seriously I can see two practical use-cases for this. The first case is my primary motivation for working on this project.

The first use case is a computer gaming website which would like to broadcast computer game tournaments over the internet using VLC. This gaming site would then be able to overlay match statistics and other information onto the streamed video.

Additionally it may be useful for HTPC projects which can then use VLC as a canvas to draw user interfaces on. Such as the MeBox does with MPlayer and bmovl2.

Tasks
-----

================================================================================== ===========
Task Description                                                                   Status
================================================================================== ===========
Make simple no-op video filters                                                    Done
Define controller protocol                                                         Done
Implement full video filter                                                        In progress
Implement bmovl/bmovl2 compatibility                                               Undecided
Implement interface library                                                        Undecided
Implement `kaa <http://freevo.sourceforge.net/cgi-bin/freevo-2.0/Kaa>`__ interface Undecided
Speed up VLC blending (Using assembly or GCC intrinsics)                           In progress
\                                                                                 
================================================================================== ===========

Protocol
--------

It is assumed that all messages return an indication of success or failure, which is not mentioned in the descriptions below.

Allocation
~~~~~~~~~~

GenImage
^^^^^^^^

Creates an image used for overlay.

Returns:

-  A numeric ID for referring to this particular image.

DeleteImage
^^^^^^^^^^^

Deletes an image, and frees any resources

Parameters:

-  The image ID to be freed

Atomicity
~~~~~~~~~

StartAtomic
^^^^^^^^^^^

Starts an atomic action. Any image parameter modifying commands sent until the next EndAtomic, will first be executed at the EndAtomic. Any returns will first be available at this point.

EndAtomic
^^^^^^^^^

Ends an atomic action. Any image parameter modifying commands since the last StartAtomic will be executed at this point, and any returns made available.

Image data
~~~~~~~~~~

DataSharedMem
^^^^^^^^^^^^^

Sends image data to an overlay, using shared memory. The controlling program MAY NOT modify the shared memory, until a return has been received for this command.

Parameters:

-  The image ID to send the data to
-  The width of the image data
-  The height of the image data
-  The format of the data (FOURCC code)
-  The (system-specific) identifier for the shared memory.

Image parameters
~~~~~~~~~~~~~~~~

SetPosition
^^^^^^^^^^^

Set the position of an overlay image.

Parameters:

-  The ID of the image to reposition
-  The X-coordinate of the new position
-  The Y-coordinate of the new position

SetAlpha
^^^^^^^^

Sets an general transparency for a given image.

Parameters:

-  The ID of the image to set transparency for.
-  The new transparency

SetVisibility
^^^^^^^^^^^^^

Sets an images visibility.

Parameters:

-  The ID of the image to set transparency for.
-  The boolean indicating of the image is visible.

Blending
--------

As a part of my work on this, I have looked at speeding up vlc's blending routines.

Benchmarking
~~~~~~~~~~~~

I've done some benchmarking for blending various colorspaces. The format for the tables is / . Each result is the average of 10 test, with the standard deviation in parenthesis. The result is the number of megapixels blended per second. For refences a SD frame is 0.44 MPix (PAL) or 0.37 MPix (NTSC), 720i/p is 0,92 MPix and 1080i/p is 2,07 MPix.

Test 1
^^^^^^

Image Dimensions: 128x128 Loops: 10000

============ ============================= =============================
Input\Output I420                          RV24
============ ============================= =============================
I420         137.3 (10.04) / 299.2 (99.36) 25.06 (1.357) / 28.70 (1.047)
YUVA         81.84 (4.023) / 79.56 (5.392) 38.09 (2.104) / 37.29 (2.832)
RGBA         220.6 (15.53) / 230.3 (10.13) 263.6 (9.678) / 254.5 (21.75)
\                                         
============ ============================= =============================

Test 2
^^^^^^

Image Dimensions: 2048x2048 Loops: 200

============ ============================= =============================
Input\Output I420                          RV24
============ ============================= =============================
I420         208.8 (6.933) / 1083. (75.65) 26.81 (.3689) / 31.45 (.3413)
YUVA         99.37 (1.981) / 98.55 (2.984) 39.55 (.7752) / 39.88 (.5518)
RGBA         268.3 (6.393) / 269.3 (4.213) 302.9 (8.844) / 303.0 (6.622)
\                                         
============ ============================= =============================
