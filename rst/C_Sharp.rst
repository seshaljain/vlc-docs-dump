{{See alsolibVLCSharp\ https://code.videolan.org/videolan/LibVLCSharp}}
This page refers to all the Work using the .Net platform interaction
with VLC.

You can find HowTos and other informations.

== Approaches ==

-  You can incorporate the VideoLAN ActiveX control like any other
   ActiveX Control (generating an Interop Assembly using aximp.exe,
   etc). In practice this is Windows-only.
-  You can use a .NET wrapper for libVLC (see below). Compatible with
   more platforms.
-  You can write your own wrapper. Writing a wrapper to LibVlc from .NET
   should not be that hard. Or adjust an existing wrapper to your
   liking.

== Related projects dealing with a .Net wrapper for libvlc: ==

Vlc.DotNet is the most advanced as of January 2016.

-  [[.Net Interface to VLC]] (actually LibVLC)
-  [http://forum.videolan.org/viewtopic.php?f=32&t=58438 libvlcnet -
   .NET library based on libvlc]
-  [http://forum.videolan.org/viewtopic.php?f=32&t=52021
   Videolan.Interop for libvlc 0.9.0]
-  [http://forum.videolan.org/viewtopic.php?f=32&t=47385 Marx C# wrapper
   for libvlc 0.9.0]
-  [http://forum.videolan.org/viewtopic.php?f=32&t=57555 Vlc.DotNet for
   WinForms & WPF], moved to [https://github.com/ZeBobo5/Vlc.DotNet
   Vlc.DotNet] and still maintained as of January 2016.
-  [http://forum.videolan.org/viewtopic.php?f=14&t=36249 VLC Element for
   WPF]

== License considerations ==

-  Using ActiveX API allows any license for your caller code.
-  Since LibVLC is LGPL, using it directly allows proprietary code (but
   watch out respecting LGPL, which includes letting end user replace
   the LGPL library with their own variant).
-  Some wrappers have a permissive licence (e.g. MIT) which also allows
   proprietary code.

[[Category:Bindings]]
