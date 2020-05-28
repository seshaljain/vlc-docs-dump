Introduction
------------

.. raw:: mediawiki

   {{VLC}}

| is a very popular, but quite large and complex piece of software.
| It uses a large number of `3rd party libraries <Contrib_Status>`__.

| VLC development is `open source <open_source>`__, and then a large community of developers worldwide contribute to it.
| However, entering a project such as VLC can be long and complex for new developers.

| This **guide** seeks to help understanding the VLC code base and VLC internals to quickly get up to speed.
| *NB: this guide is*\ **not**\ *about*\ `compiling <compiling>`__\ *VLC.*

A very good introduction to VLC can also be found on (an archived copy of the site) [//web.archive.org/web/20141204234622/http://www.enjoythearchitecture.com/vlc-architecture.html enjoythearchitecture].

The layers of VLC and libVLC
----------------------------

VLC's Core / libVLCcore
~~~~~~~~~~~~~~~~~~~~~~~

The most important (and probably most complex) part of VLC is the core, located under in the repository.

-  `Introduction to the core <{{#rel2abs:/Core}}>`__

   -  This is a **MUST-READ** for developers.

-  `VLC modules loading <Documentation:VLC_Modules_Loading>`__

   -  How the numerous VLC modules work and are loaded.

-  `Input <{{#rel2abs:/Input}}>`__

   -  How the main input chain works (slightly outdated)

-  `VLC Object Management <{{#rel2abs:/Object_Management}}>`__
-  `VLC variables <{{#rel2abs:/Variables}}>`__
-  `VLM Internals <{{#rel2abs:/VLM_Internals}}>`__

Plugins / Modules
~~~~~~~~~~~~~~~~~

`How to write a VLC module <{{#rel2abs:/How_To_Write_a_Module}}>`__.

Input
^^^^^

-  `Access <{{#rel2abs:/Access}}>`__

   -  An access module provides a byte stream from a location string `MRL <MRL>`__, like support for files, HTTP streams, webcams...

-  `Demuxer <{{#rel2abs:/Demux}}>`__

   -  A demux module parses a byte stream and splits it into `elementary streams <elementary_stream>`__ (tracks).

-  `Access-Demuxer <{{#rel2abs:/Access_Demux}}>`__

   -  An access_demux module combines the functionality of access and demux (and bypass any stream filters), splitting elementary streams directly from a location string. It's used where the bytestream abstraction is inadequate.

-  `Stream Filters <{{#rel2abs:/Stream_Filters}}>`__

   -  A stream filter module converts a byte stream into another byte stream. It could be used for file or byte stream decryption, as it is already used for decompression (gzip, Bzip2, XZ) and multi-part files.

-  `Decoder <{{#rel2abs:/Decoder}}>`__

   -  A decoder takes an elementary stream and convert into raw video, audio or text data, reading for output.

Audio
^^^^^

-  `Audio Filters <{{#rel2abs:/Audio_Filters}}>`__
-  `Audio Output <{{#rel2abs:/Audio_Output}}>`__

Video
^^^^^

-  `Video Filters <{{#rel2abs:/Video_Filters}}>`__

   -  `Deinterlace <{{#rel2abs:/Video_Filters/Deinterlace}}>`__

-  `Video Output <{{#rel2abs:/Video_Output}}>`__

Interfaces
^^^^^^^^^^

-  `Interfaces <{{#rel2abs:/Interfaces}}>`__

Modules types not documented (yet)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Misc
''''

-  `Visualization <{{#rel2abs:/Visualization}}>`__
-  `Packetizers <{{#rel2abs:/Packetizers}}>`__

Streaming output
''''''''''''''''

-  `Encoder <{{#rel2abs:/Encoder}}>`__
-  `Mux <{{#rel2abs:/Mux}}>`__
-  `Stream Output <{{#rel2abs:/Stream_Output}}>`__
-  `Access Output <{{#rel2abs:/Access_Output}}>`__

libVLC and bindings
~~~~~~~~~~~~~~~~~~~

-  Using `libvlc <{{#rel2abs:/libvlc}}>`__
-  bindings

VLC source code overview
------------------------

-  `{{#rel2abs:/VLC source tree}} <{{#rel2abs:/VLC_source_tree}}>`__
-  `{{#rel2abs:/Modules source tree}} <{{#rel2abs:/Modules_source_tree}}>`__
-  `VLC Preferences <{{#rel2abs:/Preferences}}>`__
-  `VLC Playlist and Media Library <{{#rel2abs:/Playlist}}>`__

Coding for VLC
--------------

-  `Patching <Patch>`__ (`sending <Sending_Patches>`__)
-  `Code Conventions <Code_Conventions>`__
-  `Code Signing <Code_Signing>`__
-  `Adding a module <{{#rel2abs:/How_To_Write_a_Module}}>`__
-  `Documentation:Unicode <Documentation:Unicode>`__
-  `Doxygen Documentation <https://www.videolan.org/developers/vlc/doc/doxygen/html/index.html>`__ (`pages <https://www.videolan.org/developers/vlc/doc/doxygen/html/pages.html>`__ • `modules <https://www.videolan.org/developers/vlc/doc/doxygen/html/modules.html>`__ • `data structures <https://www.videolan.org/developers/vlc/doc/doxygen/html/annotated.html>`__ • `files <https://www.videolan.org/developers/vlc/doc/doxygen/html/files.html>`__ • `API <https://www.videolan.org/developers/vlc/doc/doxygen/html/group__vlc.html>`__)
-  `C Types <C_Types>`__
-  `Strings <Strings>`__

User Experience
---------------

-  `Playback States <Playback_States>`__

Testing
-------

-  `Test Suite <Test_Suite>`__

Mozilla plugins
---------------

-  `Plugins in Mozilla <Plugins/Mozilla>`__

.. raw:: mediawiki

   {{Hacker_Guide}}
