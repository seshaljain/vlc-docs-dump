This page is a list of the `bounties <https://en.wikipedia.org/wiki/Bounty_%28reward%29>`__ that `VideoLAN <VideoLAN>`__ will pay for features developed on or 3rd party libraries.

Rules
=====

#. One must contact us before starting a bounty.
#. Sending a reasonable patch on a public mailing-list gives a temporary lock for the task.

WIP
~~~

This list is always **Work In Progress**. It is NOT a definitive list, nor are the prices!

Therefore, ask before doing anything. Or suggest ideas.

Payment
~~~~~~~

The bounties are paid to a legal entity that can create an **invoice**. It can be done by an independent worker too.

Money is paid by the VideoLAN non-profit organization in **Euros**. VideoLAN does not have a VAT number, so the prices are what VideoLAN will pay.

Money is paid on code **merge** in the relevant project.

Join our effort
~~~~~~~~~~~~~~~

If you feel like adding some money to a special bounty, please `Contact us <http://www.videolan.org/contact.html>`__.

List of bounties
================

VLC Features
------------

libVLC API for filters
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|2000}}

This task consist on doing a **correct** set of libVLC API for audio filters and video filters.

This would be useful for phonon, tomahawk and other libVLC applications.

See `#5603 <https://trac.videolan.org/vlc/ticket/5603>`__

libVLC API for sout and smem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|2000}}

Create a libVLC API to be able to use smem. This will include a libVLC API for sout.

This is very difficult, and needs extended knowledge of VLC.

See `#5037 <https://trac.videolan.org/vlc/ticket/5037>`__

Webdav support
~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|700}}

This is *readdir* implementation for webdav for the HTTP access, with Basic Authentication.

See `#9065 <https://trac.videolan.org/vlc/ticket/9065>`__

Demuxdump2
~~~~~~~~~~

.. raw:: mediawiki

   {{Price|2000}}

This is a new module to dump the incoming streams, like demuxdump, but with more use cases reported.

The important use cases that are not supported for now are:

-  so that we can "download" from a Network source in the libVLC mobile ports (for example, copy from upnp drive to the local phone)
-  so that we can "record" adaptive streaming, like Dash, HLS, MMS or other complex streaming formats.

UPnP/DLNA renderer
~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|2000}}

Same as ChromeCast, but for UPnP/DLNA

See `#17365 <https://trac.videolan.org/vlc/ticket/17365>`__ and `#1441 <https://trac.videolan.org/vlc/ticket/1441>`__.

Subtitles under the video
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1500}}

Develop the feature so that we get subtitles under the video, in the black bars, for GPU blending video output (D3D, OpenGL)

Price is for core + one module. One extra module is 500 each.

See `#2591 <https://trac.videolan.org/vlc/ticket/2591>`__.

Dual subtitles support
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1000}}

See the "video-es" variable in the core.

See `#824 <https://trac.videolan.org/vlc/ticket/824>`__.

RTP packetization
~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|Each item: 250}}

Do the packetization of ONE of those items:

-  WMA
-  WMV
-  VC-1

See `#1289 <https://trac.videolan.org/vlc/ticket/1289>`__, `#1323 <https://trac.videolan.org/vlc/ticket/1323>`__, and `#6505 <https://trac.videolan.org/vlc/ticket/6505>`__.

DVB scanning
~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1000}}

In order to compete with TV software, we need some DVB scanning, working on one platform using the DTV module.

See `#7248 <https://trac.videolan.org/vlc/ticket/7248>`__.

See http://nate.dynalias.net/dev/scanchannelsbda.rails and http://nate.deepcreek.org.au/svn/ScanChannelsBDA/trunk/

DVB Scanning²
^^^^^^^^^^^^^

.. raw:: mediawiki

   {{Price|500}}

Extending the DVB scan to another platform than the main one.

HTTP POST support
~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1000}}

In order to support webservices, it would be nice to have support for POST in the normal HTTP stack and provide a suitable API for modules.

HTTP Pool for DASH
~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|2000}}

In order to support adaptive streaming, it would be nice to have support for a shared pool between multiple streams in the normal HTTP stack and use it in the adaptive module.

Also

-  Real byterange support. (Download should respect byterange limit)
-  Self metrics (more or less accurate) or ability to toggle prefetch.

Preferences for LUA extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|2500}}

Be able to add preferences for LUA extensions.

Add RTP with FEC
~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1200}}

Input and output modules (SMPTE 2022).

Working RealMedia Demuxer
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1000}}

This task consist in writing a **correct** and working demuxer for real media format, to avoid crashing and playing all videos from China...

ARM optimizations
~~~~~~~~~~~~~~~~~

ARM optimisation for core and important filters. This is TBD.

Ideas:

-  Audio conversions
-  Chroma conversions
-  Transform filter

Convert deinterlacer x86 optimizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|500}}

What? Convert x86 assembler code in the deinterlacer to proper out-of-line (.s/.S) assembler.

Why? The inline existing assembler (esp. Yadif) breaks depending on compiler options (e.g. -O0, -flto) and versions.

For yadif, updating it from upstream is probably the best idea.

Support DVD Audio
~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|2000}}

See the dvdcpxm and the http://avisynth.nl/index.php/DVDAGuide page

Support HD-DVD
~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|2000}}

If you have the hardware :)

See `#10273 <https://trac.videolan.org/vlc/ticket/10273>`__.

VLC bugs
--------

Screencast
~~~~~~~~~~

Audio Loopback for Mac
^^^^^^^^^^^^^^^^^^^^^^

.. raw:: mediawiki

   {{Price|500}}

To record the desktop sounds.

-  It also requires to *check that all input are using mdate()-based PTS*

UI for better screencasting
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: mediawiki

   {{Price|250}}

See `#4535 <https://trac.videolan.org/vlc/ticket/4535>`__ and `#5988 <https://trac.videolan.org/vlc/ticket/5988>`__.

RTSP/UDP issue
~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|2000}}

Fix the RTSP output so that the UDP transfers work across client NATs (android clients). This will require interleaving support.

Asynchronous demuxer end-of-stream
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|250}}

An (access_)demux can set pf_demux to NULL. This avoids blocking the input thread when doing I/O. But there are no ways to emit an end-of-stream if the pf_demux function is not set. A callback should be defined for this purpose. (FWIW, this limitation is already affecting the out-of-tree Spotify plugin.)

Separate video converters from video filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|500}}

Video conversion filters and "normal" post-processing filters all expose the same capability. It makes a mess in the preferences panel, and the semantics for probing are under-specified.

Conversion filters should not touch their input and output formats. Post-processing filters should be able to change either or both input and output formats, but must be requested explicitly. The filter chain should be improved accordingly.

NVENC encoder
~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1000}}

(excl. NVIDIA affiliates)

A plugin could encode video on capable (Kepler/Maxwell) NVIDIA GPUs. At minimum H.264 is needed; MPEG2 would be nice to have. Some level of interface compatibility/similarity with the x264 plugin is highly desirable.

This may need to be out-of-tree depending on the ability to redistribute the header file. The run-time should be dynamically loaded.

Allow video filters to provide a picture pool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1500}}

Only video output display plugins are currently able to supply a custom picture pool. Filters are forced to use generic picture buffers allocated from main memory. This is a major impediment to support hardware acceleration. This is somewhat orthogonal to the previous bounty, but they cannot be done in parallel due to obvious conflicts.

This needs changes in the video output and in the filter chain to allow filters (both conversion and post-processing) to provide an optional pool callback for their \*input\* pictures. Support for video splitters pool and removal of picture_t.context would be nice bonuses.

Libavcodec bugs
---------------

Multi-threaded hw decoding
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|500}}

To fix the issue that you cannot have MT hw decoding.

Libavcodec features
-------------------

MVC
~~~

.. raw:: mediawiki

   {{Price|6000}}

Add a MVC Decoder in libavcodec and wire it to VLC.

Cineform features
~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1000}}

Now that the cineform SDK is open source, implement mission features, like temporal transform, (maybe bayer), bottom-line-bug fixing, alpha channel fixing, interlacing fixing.

VoxWare MetaSound
~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|500}}

Add a VoxWare MetaSound Decoder in libavcodec.

X-AVC-S decoder
~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|600}}

Sony second version of AVC-S, which is just a rebranded H.264, although with different sps/pps management. Unfortunately no specifications are available, so some time of reverse engineering is required.

Microsoft VC1 Progressive
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|600}}

Microsoft VC1 Progressive segmented frame mode

AAC
~~~

- AACE (aac enhanced with low delay)

- xHE-AAC

Other decoder
~~~~~~~~~~~~~

We are interested in other decoders. Assume price of 500€ for each variant.

general purpose codecs
^^^^^^^^^^^^^^^^^^^^^^

| ``- AmaRecTV AMV2, AMV3, AMV4``
| ``- AmuseGraphics - AGM2, AGM3``
| ``- AIMV, CNGA, RGGB (Powerpoint?)``

cctv software
^^^^^^^^^^^^^

| ``- Verint RFB (RFBW)``
| ``- IMM family of DVR codecs (IMM5, IMM6)``

Past bounties
=============

AC-3 Volume
~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1000}}

Fix correctly the AC-3 volume issue. See `#3994 <https://trac.videolan.org/vlc/ticket/3994>`__.

The issue can come from a mis-integration with liba52, or could come from some channels being wrongly discarded.

This **must** work on Windows.

Bug -mt on Mpeg-4 video
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|500}}

Fix the Mpeg-4 resolution change for -mt in libavcodec. See `#6579 <https://trac.videolan.org/vlc/ticket/6579>`__ and `#6533 <https://trac.videolan.org/vlc/ticket/6533>`__.

Bug -mt on H.264 video
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|500}}

Fix the H.264 resolution change for -mt in libavcodec. See `#7306 <https://trac.videolan.org/vlc/ticket/7306>`__.

Support OGG length calculation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|???}}

See `#6983 <https://trac.videolan.org/vlc/ticket/6983>`__.

MSS2
~~~~

.. raw:: mediawiki

   {{Price|1000}}

Add a MSS2 Decoder in libavcodec. See `#750 <https://trac.videolan.org/vlc/ticket/750>`__.

VC-1 interlaced
~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1000}}

Fix VC-1 interlaced and adding missing B-frames support in libavcodec. See `#5887 <https://trac.videolan.org/vlc/ticket/5887>`__.

G2M
~~~

.. raw:: mediawiki

   {{Price|1000}}

Add a G2M2/G2M3/G2M4 Decoder in libavcodec. See `#2327 <https://trac.videolan.org/vlc/ticket/2327>`__.

DTS-HD Master Audio
~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|4000}}

Add a `DTS-HD Master Audio Decoder <DTS>`__.

This can be either in libavcodec or in libdca, but it must work in VLC in the end, including 8 channels. This is probably the XLL extension to code.

BD-J
~~~~

.. raw:: mediawiki

   {{Price|2000}}

Work on libbluray integration to play BD-J BD in libbluray.

Auto-Rotation of the video
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|2000}}

As many MP4 videos and JPEG files we need to rotate those when we detect it.

So far, the demuxer has the info, but that is it.

The core should ask the video output if it can do the transformation (OpenGL) else it should load the transform filter with the right parameter.

See `#2882 <https://trac.videolan.org/vlc/ticket/2882>`__.

libVLCcore SD API and Upnp
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|800}}

The Upnp SD is very slow because it needs to fetch recusively all nodes. This needs to change.

This task will likely need a change of API for the Service Discoveries.

See `#4437 <https://trac.videolan.org/vlc/ticket/4437>`__.

Fallback on multi-threaded decoding if hardware decoding fails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1000}}

At present, libavcodec will fall back on single-threaded decoding if hardware decoding is enabled and fails during its initialization due to unsupported pixel formats, profiles, etc.. Add support to fallback on multi-threaded decoding if supported by the respective codec.

.. _rtp-packetization-1:

RTP packetization
~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|Each item: 200}}

Do the packetization of ONE of those items:

-  RGB
-  YUV

libVLC API for imem
~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1000}}

Create a libVLC API for imem to map to a libvlc_media_t object, in order to use it like the rest of libVLC. Notably libvlc_media_player_new_from_media

Audio Loopback for Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|500}}

To record the desktop sounds.

-  It also requires to *check that all input are using mdate()-based PTS*

Access module I/O interruption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|2000}}

Access modules need to wake up from waiting for I/O events when the user stops or seeks the input. Thread cancellation is not practical for access modules, and inapplicable to seeking. net_*() helper functions are limited to the input thread, not working with stream_Url*() or stream_Demux*(), and not supporting more than one file descriptor and event. A more flexible solution is necessary; stopping should always work; provisions for seeking would be nice to have, but not expected to work without additional demuxer changes. Support for multiple file descriptors (DVB) and condition variables (UDP) is a must.

HTTPS 2.0 input
~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|2000}}

Connection reuse when seeking and opening multiple files would speed up seeking and segmented streaming respectively. FWIW, I believe a fully functional implementation of this depends on the access I/O interruption feature above.

AAC encoder
~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|?}}

Add a native AAC encoder matching the quality of existing implementations by Apple (QuickTime) or Nero (libfaac). Adding support for more channels than just 2.0 is supposed to be covered by an additional bounty.

HDMI pass-through
~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1000}}

Notably for other codecs than the ones we have over S/PDIF.

We need:

-  DTS extensions over HDMI, notably DTS HD MA
-  E-AC3
-  Dolby TrueHD
-  MPGA

The price is for at least the first 3.

See `#4940 <https://trac.videolan.org/vlc/ticket/4940>`__ and other.

ARMv8 NEON mean
~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|750}}

What? add unrolled ARMv8 SIMD assembler optimizations for both so-called "merge" operations in the deinterlacing filter.

Why? because there is x86 and ARMv7 and no ARMv8 support.

Local resampling
~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|2000}}

Stop resampling the audio when playing local files.

This is extremely difficult, and needs extended knowledge of VLC.

Airplay renderer
~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1000}}

Same as ChromeCast, but for AirPlay. See the RAOP module too!

See `#17366 <https://trac.videolan.org/vlc/ticket/17366>`__.

VLM improvements
~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|3000}}

This tasks consists in improving the VLM API, in order to get closer to something like a Plex Server: on demand VoD, with transcoding for the specific device.

In scope is:

-  simplification of the VLM code
-  commonification of the VLM input and playlist (or media player) code, to reduce VLM specific code
-  API to remove the weird vlm parsing from the core (the vlm file parsing should be a module)
-  preparation of VoD for non-RTSP cases (read HTTP streaming)

Out of scope are:

-  HTTP interface changes
-  profiles for transcoding

**NB:** small reduction of VLM features is accepted.

VA video output
~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|500}}

(excl. Intel affiliates)

A video capable of scaled rotated YUV output with blending similar should support Intel cards to complement the VDPAU output. X11 support is necessary. The two usual CSC matrices should be supported; image adjust would be nice.

Hardware decoding pass-through could be added later. Wayland support is a possible future extension.

screen capture
~~~~~~~~~~~~~~

``- Fox Magic Screen Capture``

DXV decoder
~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|2000}}

Published by Resolume, there are two codecs identified by DXDI and DXD3. Completely closed source, no specifications and available for Windows and OSX only. Binary decoder should not be too hard to reverse, although it is something that will take a considerable effort.

VLC Android Features
--------------------

Support USB OTF
~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Price|1000}}

New framework for USB from Android is quite complex, but is doable, since many example exist.

`Category:Coding <Category:Coding>`__
