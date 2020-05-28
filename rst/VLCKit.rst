This page provides a brief overview on the `LibVLC <LibVLC>`__ binding for Objective-C.

Introduction
------------

VLCKit is an Objective-C wrapper for libvlc's external interface, on **macOS**, **iOS** and **tvOS**.

It includes basic classes for playback, playlists, streaming and transcoding. Doing simple media players (comparable to QuickTime Player or MPlayer OS X) is as hard as doing a QuickTime-based one; thus, it is really easy. MobileVLCKit is a subset specifically targeting the iOS platform, enabling a full playback experience with playlists, metadata handling and network streaming. If you require a media database, MediaLibraryKit will get you going within minutes.

Building the framework for macOS
--------------------------------

-  Clone http://code.videolan.org/videolan/VLCKit.git
-  open ``VLCKit.xcodeproj``
-  make sure the "Build libvlc" target is selected
-  build the project
-  Select the "VLCKit" target and build it.

This will automatically fetch and build libvlc as well as accompanying classes. Alternatively and to get access to more options, you can run the "buildVLCKit.sh" script on the terminal manually. Add the "-h" flag to see all available options.

Building the framework for iOS
------------------------------

-  Clone http://code.videolan.org/videolan/VLCKit.git
-  open your favorite terminal application such as Terminal.app or iTerm 2 and navigate to your checkout.
-  execute ``./compileAndBuildMobileVLCKit.sh``
-  check ``-h`` for available options

This will automatically fetch and build libvlc as well as its dependencies and accompanying classes.

If you want to build a library that will work for both the simulator and devices:

-  execute ``./compileAndBuildMobileVLCKit.sh``
-  use xcode command line tools to build a universal library: ``lipo -create Release-iphoneos/libMobileVLCKit.a Release-iphonesimulator/libMobileVLCKit.a -o libMobileVLCKit.a``

Or to build as a static framework with device and simulator support:

-  ``./compileAndBuildMobileVLCKit.sh -f``

Note: the MobileVLCKit Xcode project also allows you to build a dynamic framework (requiring iOS 8 later) after the build script succeeded once.

**Warning:** the current build process produces a **very** large library when using static mode. 90% of the initial size will be stripped on linking.

**Dependencies warning:** The built script fetches dependencies automatically and builds them locally; beware that system-wide installations through Homebrew may interfere with the local build scripts. If you get autoconf-related errors, try removing /usr/local from your PATH, wiping the source tree, and starting the build over.

Building the framework for tvOS
-------------------------------

-  Clone http://code.videolan.org/videolan/VLCKit.git
-  open your favorite terminal application such as Terminal.app or iTerm 2 and navigate to your checkout.
-  execute ``./compileAndBuildMobileVLCKit.sh -t``
-  check ``-h`` for available options

This will automatically fetch and build libvlc as well as its dependencies and accompanying classes.

If you want to build a library that will work for both the simulator and devices:

-  execute ``./compileAndBuildMobileVLCKit.sh``
-  use xcode command line tools to build a universal library: ``lipo -create Release-appletvos/libTVVLCKit.a Release-appletvsimulator/libTVVLCKit.a -o libTVVLCKit.a``

Or to build as a static framework with device and simulator support:

-  ``./compileAndBuildMobileVLCKit.sh -t -f``

Note: the MobileVLCKit Xcode project also allows you to build a dynamic framework after the build script succeeded once.

**Warning:** the current build process produces a **very** large library when using static mode. 90% of the initial size will be stripped on linking.

**Dependencies warning:** The built script fetches dependencies automatically and builds them locally; beware that system-wide installations through Homebrew may interfere with the local build scripts. If you get autoconf-related errors, try removing /usr/local from your PATH, wiping the source tree, and starting the build over.

Basic usage in your application
-------------------------------

The code should speak by itself

| ``  // Set up a videoView by hand. You can also do that in the nib file``
| ``   videoView = [[VLCVideoView alloc] initWithFrame:[[window contentView] bounds]];``
| ``   [[window contentView] addSubview:videoView];``
| ``   [videoView setAutoresizingMask: NSViewHeightSizable|NSViewWidthSizable];``
| ``  ``
| ``   // Init the player object``
| ``   player = [[VLCMediaPlayer alloc] initWithVideoView:videoView];``
| `` ``
| ``   [player setMedia:[VLCMedia mediaWithPath:@"/to/my/movie"]];``
| ``   [player play];``

Sample code
-----------

We offer sample code both for iOS and macOS.

``Examples_OSX`` includes 3 different projects.

-  *BasicPlayerWithPlaylist*: this sum's it up pretty well. drag and drop files, hit play / pause, see them play in the same window in the order you want them to.

.. figure:: List_based_vlckit_player_sample.png
   :alt: Basic Player with Playlist

   Basic Player with Playlist

-  *FlashVideoDownloader*: this exemplifies the basics on how to deploy VLC's URL parsing mechanisms to gain access to the actually played media and how to store it.

.. figure:: Flash_video_downloader_vlckit_sample_project.png
   :alt: Flash Video Downloader

   Flash Video Downloader

-  *iPodConverter*: VLCKit includes streaming and transcoding features including a few pre-defined profiles. In this sample, you see how to use them. Drop a file in the designated area. Hit convert. See the file being converted including a progress bar.

.. figure:: Convert_for_ipad_osx_sample_project.png
   :alt: iPodConverter

   iPodConverter

``Examples_iOS`` includes 2 different projects developed using Xcode 5 and with iOS 7 in mind. With minor modifications, they will also work on iOS 5 and 6.

-  *SimplePlayback*: it's as simple as it sounds. Launch the app to watch a file being streamed live over http from one of our servers to your iOS Simulator or device.

.. figure:: Simple_playback_iOS_sample_project.png
   :alt: Simple Playback

   Simple Playback

-  *DropIn-Player*: this is a more advanced sample project implementing a basic view controller, which could be embedded in your own app. It allows any kind of media playback, subtitles handling, multiple audio track handling, aspect ratio customizations, playback position manipulation and display, volume. All of that, implemented in a self-contained class and a single xib file.

.. figure:: Drop-in_player_sample_project_ios.png
   :alt: Drop-In player

   Drop-In player

Are there apps actually deploying VLCKit on macOS and iOS?
----------------------------------------------------------

This is a selection of apps we are aware of.

-  `Amahi for iOS <https://www.amahi.org/ios>`__ by `Amahi <https://www.amahi.org>`__
-  `Blackbox <http://www.rotapp.com/app/blackbox/>`__ by Rotapp
-  `Dreambox-Live <http://www.rotapp.com/app/dreambox-live/>`__ by Rotapp (discontinued)
-  `Fleex player <http://fleex.tv>`__ by fleex.tv
-  `iMagneto <http://imagneto.sourceforge.net/>`__
-  `Korri player <http://www.korrisoft.com/references/references.php>`__ by `Korrisoft <http://www.korrisoft.com>`__
-  `Lunettes <Lunettes>`__ by the VideoLAN team
-  `Ma TV Star <http://www.korrisoft.com/references/references.php>`__ by `Korrisoft <http://www.korrisoft.com>`__
-  `Movie Player 2 <http://www.domzilla.net/iphone-apps/movieplayer2/>`__ by Dominic Rodemer Online Media
-  `Player multimédia TNT <http://www.korrisoft.com/references/references.php>`__ by `Korrisoft <http://www.korrisoft.com>`__
-  `VLC for iOS <iOS>`__ by the VideoLAN team
-  `VLC Streamer <http://hobbyistsoftware.com/vlcstreamer-more>`__ by `HobbyistSoftware <http://www.HobbyistSoftware.com>`__

Feel free to add your application above in alphabetical order. Note that we don't list apps violating VLCKit's licensing terms - regrettably, there are quite a few.

Compilation tips
----------------

-  If you do not care about the latest, try using the stable branch, e.g. 2.1-stable
-  The build tree has what could be described as "git submodules" and they sometimes can fall out of sync. If the code inside ``MobileVLCKit/ImportedSources/vlc`` falls out of sync or you need to force a rebuild you may want to remove ``contrib/iPhoneOS-armv7*/``
-  In some situations your libtoolize may interfere with the build tools. You may want to add ``$PATH/MobileVLCKit/ImportedSources/vlc/extras/tools/build/bin`` towards the beginning of your PATH and build with it

Related
-------

-  `Compiling VLC on macOS <macOSCompile>`__

External Links
--------------

-  `Introduction to The Objective-C 2.0 Programming Language <http://developer.apple.com/documentation/Cocoa/Conceptual/ObjectiveC/Introduction/introObjectiveC.html>`__
-  `Interface Builder <http://developer.apple.com/documentation/developertools/Conceptual/IB_UserGuide/Introduction/Introduction.html>`__
-  `Mobile VLCKit for Xamarin.iOS <https://github.com/dalexsoto/MobileVLCKit-for-Xamarin.iOS>`__

`Category:Bindings <Category:Bindings>`__ `Category:iOS <Category:iOS>`__ `Category:LibVLC <Category:LibVLC>`__ `Category:macOS <Category:macOS>`__
