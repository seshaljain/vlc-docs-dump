{{SoCProjectstudent=[[User:Rohityadavmentor=}}

=== Introduction ===

These days widgets are ubiquitous. Not only did they enhance the
functionality, they add dynamic interaction with the user. The VLC
Widget project is aimed to build custom widgets in Qt/C++ using custom
QPainter widgets, or using SVGs and Qt Kinetics (The new Qt 4.6+
Animation framework).

=== Widgets Status === \* VLC MiniMode Widget: '''[DONE]''' Media
Notification and Playback Controlling Widget. \* Beat Analyzer:
[DISCONTINUED] The widget shows beats like a beat analyser in WinAMP.
It'll be further extended to be a new beats visualisation. \* SVG
FullScreen Controller: [DISCONTINUED] Full Screen Controller as in VLC
on Mac OS X, based on SVG like VLC MiniMode. \* Ergonomic
UI/Menu/Buttons using SVGs: [DISCONTINUED]

=== VLC MiniMode Widget === \* About: Media Notification and Playback
Controller Widget \* Status: DONE, to be included in source in future
(may be). \* Specs: - Qt/C++ - SVG (Using Inkscape) - Support: Linux,
Windows and other OS using Qt4 interface \* Source Code: Patch Released
on VLC-devel. \* Features: - Playback Slider. - Volume Control. -
Playback Controls: Play, Pause, Next, Previous. - Album Art Display -
Drag and Drop files to play - Widget Lock/Unlock Feature [To lock the
visibility of widget] - Drag-able across the desktop - Theme-able SVG:
Themes can be made using SVG and CSS.

-  Screenshot:
   http://img208.imageshack.us/img208/7545/screenshot2hzi.png

\* Download: Install both the following deb packages (On Debian based distro -> $sudo dpkg -i <vlc-minimode.deb...> <libvlc.deb...>) featuring MiniMode widget with VLC, made using VLC 1.0.4(stable):
   [VLC-Minimode
   http://www.whatifi.undo.it/gsoc/vlcminimodedebs.zip?attredirects=0&d=1]
   [LibVLC
   http://www.whatifi.undo.it/gsoc/libvlcdebs.zip?attredirects=0&d=1]

{{GSoC}}
