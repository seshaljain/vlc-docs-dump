.. raw:: mediawiki

   {{Lowercase}}

The **libVLC** (VLC ) media framework can be embedded into an application to get multimedia capabilities.

Since VLC is based on libVLC, one should be able to have the same features that has.

The libVLC media framework is already used by several applications; see `who uses libVLC? <LibVLC_Users>`__

Documentation
-------------

Please refer to the `Doxygen documentation <https://www.videolan.org/developers/vlc/doc/doxygen/html/group__libvlc.html>`__, which is the reference documentation.

\ *Make sure that the documentation matches the LibVLC version.*\  (if not, you can build it from the source code)

Some further topics are covered here:

-  `LibVLC Memory Management <LibVLC_Memory_Management>`__ explained: covers the basics on the ``_new()``, ``_retain()``, ``_release()``.
-  `LibVLC Media List Management <LibVLC_Media_List_Management>`__ explained: covers the basics on setting up a playlist.
-  `Generate a .lib for using libVLC on Windows <GenerateLibFromDll>`__ (before libVLC 2.1.0)

Compiling
---------

| To build LibVLC you need `VLC source code <VLC_source_code>`__ and follow `VLC compilation instructions <Compile_VLC>`__ since LibVLC it is directly shipped in VLC source code.
| You will find headers in vlc-src/include/vlc and libvlc.so binaries in the *hidden* folder vlc-src/lib/.libs.
| When using your custom LibVLC build you will need to define the environment variable VLC_PLUGIN_PATH pointing to VLC modules located in vlc-src/modules.

Examples
--------

Playback
~~~~~~~~

-  `Current version (1.1.x and later) <LibVLC_Tutorial>`__
-  Gtk Player:
-  Qt Player:
-  WxWidgets Player:

Rendering and streaming
~~~~~~~~~~~~~~~~~~~~~~~

-  `Use LibVLC in an SDL application <LibVLC_SampleCode_SDL>`__
-  `Stream into a memory zone <Stream_to_memory_(smem)_tutorial>`__
-  Generate thumbnails using LibVLC:
-  Quick DVD ripper:

More complex examples
~~~~~~~~~~~~~~~~~~~~~

-  

   .. raw:: mediawiki

      {{VLCSourceFolder|p=libvlc-demos.git|vlcinfo|l=MediaInfo clone}}

-  

   .. raw:: mediawiki

      {{VLCSourceFolder|p=libvlc-demos.git|webcam|l=Webcam / Cheese clone}}

libVLC on Android
~~~~~~~~~~~~~~~~~

-  `LibVLC on Android sample <https://code.videolan.org/videolan/libvlc-android-samples>`__

VLCKit for Cocoa (iOS/macOS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can find details on features and implementation on a `designated page <VLCKit>`__.

macOS
^^^^^

-  `Simple playlist player for macOS <https://code.videolan.org/videolan/VLCKit/tree/master/Examples/macOS/BasicPlayerWithPlaylist>`__.
-  `iPod Converter for macOS <https://code.videolan.org/videolan/VLCKit/tree/master/Examples/macOS/iPodConverter>`__.
-  `Flash Video Downloader for macOS <https://code.videolan.org/videolan/VLCKit/tree/master/Examples/macOS/FlashVideoDownloader>`__.

iOS
^^^

-  `Simple player for iOS <https://code.videolan.org/videolan/VLCKit/tree/master/Examples/iOS/SimplePlayback>`__.
-  `Drop-in player for integration in iOS apps <https://code.videolan.org/videolan/VLCKit/tree/master/Examples/iOS/DropIn-Player>`__.

Crossplatform .NET/Mono support with LibVLCSharp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `Simple playback samples (iOS/Android/Mac/Windows/Xamarin.Forms) <https://code.videolan.org/videolan/LibVLCSharp/tree/master/Samples>`__.
-  `Advanced samples <https://code.videolan.org/mfkl/libvlcsharp-samples>`__.

Outdated samples
~~~~~~~~~~~~~~~~

-  `Versions 0.9.x and 1.0.x <LibVLC_Tutorial_0.9>`__
-  `Version 0.8.6 <LibVLC_Tutorial_086c>`__
-  `Visual C++ <LibVLC_Visual_C++>`__ '' (uses "old" legacy API) ''
-  `VCL component for Delphi <IceVLCPlayer>`__ (out-of-date)

Language & platform bindings
----------------------------

LibVLC is a C library. It has bindings to the following languages and frameworks:

-  C++, using the `libvlcpp <https://code.videolan.org/videolan/libvlcpp>`__ library
-  The `Web plugin <Web_plugin>`__ for ActiveX (e.g. MSIE) and NPAPI (e.g. Firefox)
-  `WebChimera <http://WebChimera.org>`__ browser plugin with `NW.js <http://nwjs.io/>`__ support
-  `WebChimera.js <https://github.com/RSATom/WebChimera.js>`__ - another way to bind libvlc to node.js/io.js/NW.js/Electron
-  `Objective-C/Swift for iOS and macOS <VLCKit>`__
-  `Perl <Perl_bindings>`__
-  `Python <PythonBinding>`__
-  `Phonon (Qt/KDE) in C++ <http://phonon.kde.org/>`__
-  `Java <Java_bindings>`__
-  `Java/Scala/Kotlin/JNI Android <https://code.videolan.org/videolan/vlc-android/tree/master/libvlc/jni>`__
-  `C#/F#/.NET <https://code.videolan.org/videolan/libvlcsharp>`__
-  `C++/CX <https://code.videolan.org/videolan/vlc-winrt/tree/master/modules/libvlcppcx>`__
-  `Go <https://github.com/adrg/libvlc-go>`__
-  `Rust <https://github.com/garkimasera/vlc-rs>`__
-  `QmlVlc <http://github.com/RSATom/QmlVlc>`__ - Qt 5 QML binding
-  `VLC-Qt <https://github.com/vlc-qt/vlc-qt>`__ - Qt bindings
-  `wxWidgets MediaCtrl backend <wxVLCBackend>`__ also in C++
-  `Using libvlc with Delphi <Using_libvlc_with_Delphi>`__
-  `Pascal/Delphi <http://sourceforge.net/projects/paslibvlc/>`__
-  `Tcl <http://wiki.tcl-lang.org/48382>`__
-  `ActiveX <ActiveX>`__ with the built-in VLC browser plugin for MSIE (obsolete)

`\* <Category:LibVLC>`__
