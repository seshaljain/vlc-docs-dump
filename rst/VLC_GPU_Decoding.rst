== Introduction ==

The {{VLC}} framework can use your '''''graphics chip''''' (a.k.a. GPU)
to accelerate decoding of video streams depending on the video codec,
graphic card model and operating system. In some cases, it can let the
graphic card perform post-processing and rendering of the decoded video.
In any case, this frees the main processor (i.e. CPU) of some of the
most computationally heavy sub-tasks involved in playing digital video.

== Activation == {{See also|VLC HowTo/Hardware acceleration}} To enable
hardware accelerated decoding, use the VLC preferences. By default,
[[hardware acceleration]] is disabled (and consequently, hardware
acceleration is not yet available to external application via
[[libVLC]]).

In VLC version 2.1, you can select which acceleration method you wish to
use among those available for your operating system (if any). In earlier
versions, there was simply a check box as shown below:

[[File:VLC_GPU.png]]

== Operating system support ==

=== <span id="Windows"></span> Windows === <!-- Anchor for incoming
links from [[VLC Features Formats]], [[VLC VAAPI]], [[HD-Discs]],
[[HD-Discs codecs]] via [[VLC DxVA2]] --> {{Wikipedia|DirectX Video
Acceleration}}

Since VLC version 1.1.0, DirectX Video Acceleration (DxVA) is supported
in
[https://docs.microsoft.com/en-us/windows/desktop/medfound/about-dxva-2-0
DxVA 2.0]. It is available in ''Windows Vista'' (or ''Windows 2008'') or
any later Windows version; it is '''not''' available for Windows XP/2003
(and never will be).

{{Forum|9421}}

The following video codecs are supported: [[MPEG-1]], [[MPEG-2]],
[[Windows_MediaVC-1]] and [[H.264|H.264 (MPEG-4 AVC)]].

=== X11 (GNU/Linux, FreeBSD, etc.) ===

On Linux/X11, there are two competing interfaces for hardware video
decoding, VA-API from [http://www.intel.com/ Intel], and VDPAU from
[http://www.nvidia.com/ NVIDIA]. Generally, VAAPI is used for Intel and
Broadcom graphic cards, while VDPAU is used for AMD/ATI and NVIDIA
cards.

==== VA-API ==== VA-API is supported for decoding only since VLC version
'''1.1.0'''. Refer to [[VLC VAAPI]] for more details.

On modern Ubuntu distributions, first install the hardware support
(packages '''i965-va-driver''', '''libva-intel-vaapi-driver''' and
'''vainfo''') and then activate GPU hardware acceleration in Preferences
→ Input&Codecs.

Install via the terminal command:
   sudo apt-get install i965-va-driver libva-intel-vaapi-driver vainfo

The following video codecs are supported: [[MPEG-1]], [[MPEG-2]],
[[MPEG-4WMV3]], [[Windows_MediaH.264 (MPEG-4 AVC)]].

==== VDPAU ==== VDPAU is supported for decoding since VLC version
'''2.1.0''', and for post-processing and rendering since VLC '''2.2.0'''
(still in development as of late 2013).

VDPAU will be enabled automatically by default in VLC version 2.2.0
onward. Refer to http://www.remlab.net/op/vlc-vdpau.shtml for technical
details.

The following video codecs are supported for decoding: [[MPEG-1]],
[[MPEG-2]], [[MPEG-4WMV3]], [[Windows_MediaH.264 (MPEG-4 AVC)]]. Almost
all video codecs are supported for post-processing and rendering.

=== macOS === Video Decoding Acceleration (VDA) comes with macOS X.6.3
and later (see
[https://developer.apple.com/library/archive/technotes/tn2267/_index.html
API]). This is somewhat supported in VLC 2.1.0.

Only [[H.264|H.264 (MPEG-4 AVC)]] is supported currently.

== Graphic card compatibility ==

=== Windows ===

To check your DxVA compatibility, please '''download
[http://bluesky23.yukishigure.com/en/DXVAChecker.html DxVA Checker]'''

==== nVidia ====

For nVidia GPU, you are '''required''' to use a GPU supporting
[[wikipedia:Nvidia_PureVideoION]], [[wikipedia:GeForce_8_SeriesGeForce
9]] (recommended), [[wikipedia:GeForce_200_Series|GeForce 200]] or
newer.

We strongly '''recommend''' a VP3 or VP4 GPU.

To be sure, check your GPU against
[[wikipedia:Nvidia_PureVideo#Table_of_GPUs_containing_a_PureVideo_SIP_block|this
table on Wikipedia]] and check if you are VP2 or newer.

==== ATI ====

For ATI GPUs, you '''NEED''' Catalyst 10.7, that is just out.

Then, you are required to use a GPU supporting
[[wikipedia:Unified_Video_Decoder|Unified Video Decoder]].

We believe you need a [[wikipedia:Unified_Video_Decoder#GPUs|GPU
supporting UVD2]], like HD4xxx, 5xxx, 6xxx or 3200. One might have
success with UVD+ GPU, like some HD 3xxx, but this isn't tested.

==== Intel ====

Latest Intel GMA should work. Tested on GNU/Linux (Ubuntu 13.10) and
hardware acceleration definitely works for Intel HD Graphics 3000
(dropped CPU usage for HD720 (1280 x 720, H.264, 24fps) from 12-13% to
6%).

[[Category:Documentation]]
