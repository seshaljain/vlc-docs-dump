{{lowercase}} == Development environment ==

To develop VLC for iOS, you need: \* OS X 10.10 Yosemite (or later) \*
Latest Xcode version (version 6 works so far) \* A correct shell (we
recommend iTerm2 and zsh) \* [http://cocoapods.org CocoaPods] (for
dependency management)

== Get the source ==

We provide source code packages for every release. You can find the
latest on our [http://www.videolan.org/vlc/download-ios.html Download
VLC for iOS website]. Older releases
[http://download.videolan.org/videolan/vlc-iOS/ are also available].

== Build it ==

Install the dependencies

   pod update

Wait, and grab a coffee.

Open the VLC.xcworkspace and run!

== Deploy ==

Open the .xcworkspace (not .xcodeproj) in Xcode and click on Run.

Buliding release version needs code signing

Before running simulator in Xcode, run .sh with -s first; Before running
iphoneos in Xcode, run .sh without -s first.

== Send patches == You can create patches and send them to our
[http://mailman.videolan.org/listinfo/ios mailing list] ios@v.o, or on
our [[IRC]].

Please see [[Git#Submitting_patches]] on how to send patches...

== Notes == If everything goes well, congratulations to Lucky You! If
not, please report any problem to our
[http://mailman.videolan.org/listinfo/ios mailing list] ios@v.o, on our
[[IRC]] or join us on the [http://forum.videolan.org forum].

=== History === The first version of this howto was written by
[[User:J-b|jb]] on 18 July 2013.

=== Previous Version === The old version of the app can be compiled
using this [[MobileVLC|howto]].

[[Category:Building]] [[Category:iOS]]
