This is an attempt to reduce confusion about the new terms introduced
with the release of Windows 8 in various modes, for various
architectures and various restrictions.

== Windows 8 == Windows 8 is an Operating System from Microsoft, based
on Windows NT line.

The version of this Windows NT OS has a release number of 6.2 and was
released at the end of 2012.

It has a small kernel evolution from Windows 7, but the big addition of
the Modern Interface mode.

It runs on x86 and x86(64bits) hardware.

== Windows RT / Windows on ARM == This is the port of the Windows 8
operating system on various ARM platforms.

Contrary to popular misconception, Windows RT has both a "Metro" and a
"Desktop" mode and can run
Office.[http://forum.xda-developers.com/showthread.php?t=2092158][http://forum.xda-developers.com/showthread.php?t=2092348]

Windows RT has Win32 APIs too.

No Desktop 3rd party applications are allowed on Windows RT (enforced by
the Kernel).

No 3rd party operating systems are allowed on the Windows RT hardware
(enforced by UEFI).

'''NB:''' Windows RT is not a RunTime.

'''NB:''' <big>'''Not to be confused with WinRT.'''</big>

== Windows 8.1 / Windows Blue == Windows 8(+1). Formerly known as
'''Windows Blue'''.

It is a new version of Windows NT (6.3), but it is a smaller update
above Windows 8 than normal Windows releases, after a short development
cycle.

It was released in October 2013, and is available as a free upgrade from
the Windows Store for Windows 8 PCs.

It deprecates some Win32 and WinRT APIs and adds new ones.

== WP 7 / 7.5 / 7.8 == Windows Phone 7 is an OS for mobile phones that
is based on the Windows CE kernel.

Microsoft only allows Managed applications from 3rd parties. Therefore,
no VLC for WP7 will exist.

== WP8 == Short for ''Windows Phone 8'', WP8 is an OS for mobile phones.

WP8 is quite different from WP7, under the hood. WP8 is based on a
Windows NT kernel, very likely the one from Windows8.

It has most of the same WinRT APIs, and most Win32 APIs too.

== Win32 == The evolving set of APIs and runtime available since Windows
3.11 and still changing these days.

Windows NT 64bits is almost compatible with Win32 and Windows CE was
partly compatible with Win32 APIs.

On 64bits, Windows NT uses the LLP64 model for pointers! Be careful if
you are a Unix developer.

== WinRT == WinRT also called ''Windows Runtime'', is the set of APIs to
develop "Modern" and WP8 applications.

All those are essentially a COM-based set of APIs, written above Win32.

It is not really the low-level runtime, since the Windows runtime is
still Win32 and MSVCRT.

To make the matter more confusing, most (if not all?) APIs from WinRT
are also usable from classic desktop applications.

WinRT APIs is a moving target, depending on the version of Windows
applications are run (the family).

'''NB:''' Not to be confused with Windows RT.

== C++/CX (Component Extensions) ==

C++/CX (Component Extensions) is a language extension of C++11 from
Microsoft that enables C++ programmers to write programs for WinRT,
without fighting with COM.

It makes COM interop with C# transparent.

== Metro Applications ==

''Metro applications'', ''Modern UI style apps'', ''Windows Store apps''
or ''Windows 8 apps'' are applications that are run integrated in the
new Modern interface.

They are only available through the store or can be side-loaded from
your machine.

Metro applications can be run on Windows 8 and Windows RT (after a
recompilation for native apps).

They can use: \* All(?) WinRT COM APIs \* A subset of Win32 authorized
by Microsoft.

Those APIs are supposed to be non-blocking and sandboxable.

=== Conformance === As WinRT is not totally new runtime, the check that
only the correct APIs are called is done during the Store submission,
using WACK, and not at runtime.

This means also that the set of APIs allowed WILL change: WinRT target
is therefore a moving target.

== WP8 Applications ==

Those are almost the same than W8 Metro applications, but not quite,
because of different size of screen and start screen.

They have a different set of APIs allowed, Win32 and WinRT.

For example, WP8 apps are allowed to use Winsock2, not Metro apps.

== Metro (Screen) ==

The new Windows 8 start/smart screen is what used to be called Metro.

It is a "Modern Experience screen", based on tiles, from which you can
start "Modern applications".

== Metro (language) == This is a designer style/visual language that
Microsoft is pushing for the new "Modern UI".

== Desktop == The Windows interface as we know it since Windows 3.11
until Windows 7.

== Desktop Applications == Those are classic applications like {{VLC}}
that use Win32 APIs, HWND, and COM-based APIs (including WinRT APIs).

[[Category:Glossary|*]] [[Category:Windows]]
