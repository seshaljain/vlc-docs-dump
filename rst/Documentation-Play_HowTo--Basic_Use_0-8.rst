{{Historical}} {{RightMenu|Documentation TOC}}

'''Note: this documentation is for versions older than 0.9. For help
with 0.9 please see [[Documentation:VLC for dummies\| VLC for dummies:
an introduction to VLC]] and
[[Documentation:Play_HowTo/Basic_Use_0.9|Basic Use for 0.9]].'''

==General interface description==

VLC has several interfaces: *A cross-platform interface, for Windows and
GNU/Linux, called wxWidgets,*\ A native Mac OS X interface, and \*A
skinnable interface for Windows and GNU/Linux. Screenshots below are
drawn from the various interfaces, but VLC's functions work essentially
the same on all operating systems.

===Windows and GNU/Linux (wxWidgets)===

This is the default interface on Windows and GNU/Linux (the screenshot
is done on GNU/Linux, but it would look quite the same on Windows).

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx.jpg
The wxWidgets interface

This interface also features an ''Extended GUI'' which contains many
additional features. To display or hide it, go to the ''Settings'' menu
and click ''Extended GUI''.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-extended.jpg
The wxWidgets interface with extended GUI

===Native Mac OS X (Cocoa)===

This is the default interface on Mac OS X.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-osx.jpg
The Mac OS X interface

This interface features an ''Extended GUI'' as well. It is called
"Extended Controls" and can be opened through the Window menu.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-osx-extended.jpg
The Mac OSX interface with with the extended controls panel

==Basic playback==

===Play a file===

To play a file, open the ''File'' menu, and select the ''Quick Open
File'' menu item. An Open File dialog box will appear. Select the file
you want to open, and select Open. VLC will start playing the selected
file.

An alternative is to drag 'n' drop your file on the VLC main interface
or playlist window from the file explorer (Finder on MacOS X).

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-file-menu.jpg
The File menu - wxWidgets interface

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-osx-file-menu.jpg
The File menu - MacOS X interface

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-open-file.jpg
The Open file dialog - wxWidgets interface

http://wwww.videolan.org/doc/play-howto/en/images/play-howto/intf-osx-open-file.jpg
The Open file dialog - MacOS X interface

===Play a CD/DVD/VCD===

To Play a CD, VCD or a DVD, open the ''File'' menu, and select the
''Open Disc...'' menu item. In the Open Disk Dialog Box, select the type
of media (DVD, VCD or Audio CD). When reading a DVD, you can enable DVD
menus by selecting the ''DVD (menus)'' disc type in the wxWidgets
Interface. In the MacOS X interface, this can be done by selecting the
"Use DVD menus" dialog box.

You can select the drive from which the media should be read by giving
the appropriate drive letter or device name in the "Device Name" text
input. This should be auto-detected on MacOS X.

If you want to start the DVD or VCD playback from a given title and
chapter instead of from the beginning, you can set it using the
''Title'' and ''Chapter'' selectors.

You can start playback by selecting the ''Ok'' button.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-open-disk.jpg
The Open disk dialog - wxWidgets interface

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-osx-open-disk.jpg
The Open disk dialog - MacOS X interface

===Play a network stream (WebRadio, WebTV, etc.)===

To open a network stream, open the "File" menu and select the "Open
Network Stream" menu item.

*To open a UDP unicast stream, select ''UDP/RTP'', and set the
appropriate UDP port in the selector (it is 1234 for streams sent by a
VLC or VLS server).*\ To open a UDP multicast stream, select ''UDP/RTP
multicast''. Give the address of the multicast group in the "Address"
text input, and select the appropriate UDP port. *To open a stream sent
over http (Webradios, WebTVs, Shoutcast, Icecast...), ftp, or mms
(Microsoft Media Server), select "HTTP/FTP/MMS", and give the
corresponding complete URL, (such as http://live.stream.org:8080/live or
mms://live.ms.stream.net:8080/live.asf) in the corresponding text input.
This also the way to open a RTSP stream with the MacOS X interface.*\ To
open a RTSP stream (sent by Darwin Streaming Server, VLC, etc), in the
wxWidgets interface, select "RTSP" and give the URL in the text input.

You can start playback by selecting the ''Ok'' button.

If you get some stuttering during playback, you can try to increase the
size of the read buffer. This can be done in the ''Open Network Stream''
dialog box, by selecting the ''Caching'' box. You can then choose the
amount time (in milliseconds) VLC should store data in its buffer before
starting playback.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-open-net.jpg
The Open network dialog - wxWidgets interface

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-osx-open-net.jpg
The Open network dialog - MacOS X interface

===Play from an acquisition card===

This currently only possible on Linux and Windows. Open the File menu,
and select "Open Capture Device..."

On Windows, supported cards include webcams, TV cards, acquisition
cards... provided they come with directshow compatible drivers (Almost
all acquisition cards do). You can choose the device to use for video
and audio capture using the "Video device name" and "Audio device name"
selectors. If your device doesn't appear in the list, try to select the
"Refresh list" button. You can access the settings of your acquisition
device by selecting the ''configure'' button. Options here depend on the
driver of the device. You can select the "Device Proprieties" box if you
want the configuration dialog box of every device to be displayed after
having pressed the ''Ok'' button. Select the ''Tuner properties'' box to
be prompted for tuner settings (PAL/NTSC standard, frequency...) for TV
cards. The ''Advanced options...'' button allows to select some further
settings useful in some rare cases, such as the chroma of the input (the
way colors are encoded) and the size of the input buffer.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-open-capture.jpg
The Open Capture device dialog and a device configuration windows-
wxWidgets interface

On Linux, supported cards include webcams, TV cards, acquisition cards,
provided they are supported by the Video4Linux architecture. Haupaugge
PVR 250/350 cards are also supported, using the
[http://ivtv.sourceforge.net/ IVTV drivers].

\*For Video4Linux devices, you can set the name of the video and audio
devices using the "Video device name" and "Audio device name" text
inputs. The "Advanced options..." button allows to select some further
settings useful in some rare cases, such as the chroma of the input (the
way colors are encoded) and the size of the input buffer.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-open-v4l.jpg
The Open Video4Linux dialog- wxWidgets interface

\*To use a Hauppauge PVR card, select the PVR tab in the "Open" dialog
box. Use the "Device" text input to set the device of the card you want
to use. You can set the Norm of the tuner (PAL, SECAM or NTSC) by using
the "Norm" Drop Down. The Frequency selector allows you to set the
frequency of the tuner (in kHz), the bitrate selector to set the bitrate
of the resulting encoded stream (in bit/s). The "Advanced Options button
allows to set some more settings, such as the size of the encoded video
(in pixels), its framerate (in frame per second), the interval between 2
key frames, etc.

After having set all the required parameters, you can start the capture
by selecting the "Ok" button.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-open-pvr.jpg
The Open PVR dialog- wxWidgets interface

==Playlist==

VLC can store a list of several files to play one after the other, using
its playlist system. To access the playlist, click on the ''Playlist''
button on the main interface.

Each time you use the Open dialog box, the stream you select is appended
at the end of the playlist and started.

The playlist window shows all the available streams. Double-click one to
play it.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-playlist.jpg
The Playlist - wxWidgets interface

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-osx-playlist.jpg
The Playlist - MacOS X interface

===Adding items, saving and loading playlists===

In the wxWidgets interface, the ''Manage'' menu allows you to append an
item at the end of the playlist (its playback won't start immediately),
to save the playlist as a M3U or PLS file, or to import a playlist file.

In the MacOS X interface, saving a playlist can be done using the ''Save
Playlist...'' function in the ''File'' menu. To import a playlist file,
open it the same way as any other media file, using the ''Quick Open
File...'' menu item.

===Sorting===

In the wxWidgets interface, ''Sort'' allows you to sort the playlist
according to several criteria, or to shuffle it. You can also sort by
clicking the header of the column.

In the MacOS X interface, sorting can be done by clicking the header of
the column matching the criteria you want to use for sorting.

===Playlist modes===

The playlist supports several playback modes.

In the wxWidgets interface, the toolbar contains three playlist mode
buttons. They allow to enable random mode, to repeat the whole playlist
or to repeat one item.

In the MacOS X interface, random mode can be enabled by selecting the
''Random'' box. A drop down menu allows you to enable playlist and item
repeat modes.

===Misc===

====Search====

You also have a search tool. Enter a search string and hit search. The
next item to match the string will be highlighted. Keep hitting Search
to cycle between all matching items.

====Moving items====

In the wxWidgets interface, the ''Up'' and ''Down'' buttons at the
bottom of the playlist window allow you to move an item. Select an item
and use these buttons to move it.

In the MacOS X interface, you can easily move an item with the mouse,
using drag-and-drop.

====Contextual menu====

By right-clicking or control-clicking an item, a contextual menu will
appear, giving access to a number of functions (for example, play the
item, disable it, delete it, or get info on it).

If you ask for info, an ''item info'' dialog box will appear. This
dialog box also allows you to change the name, the author and the
location of the item to play.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-iteminfo.jpg
Item Info Dialog - wx Interface

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-osx-iteminfo.jpg
Item Info Dialog - MacOS X interface

==Subtitles==

VLC supports many kinds of subtitles.

===Media with included subtitles===

Many types of media can have embedded subtitles. VLC can read subtitles
for the following media: *DVD*\ SVCD *OGM files*\ Matroska (MKV) files

Subtitles are disabled by default. To enable them, go to the ''Video''
menu, and to ''Subtitles track''. All available subtitles tracks will be
listed. Select one to get the subtitles. Depending on the media, a
description (language, for example) might be available for the track.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-select-sub.jpg
Select a subtitles track under Windows or Linux

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-osx-select-sub.jpg
Select a subtitles track under MacOS X

DVD and SVCD subtitles are merely images, so you won't be able to change
anything for them. OGM and Matroska subtitles are rendered text, so you
will be able to change several options.

Text rendering options can be changed in the Preferences. In the
''Modules'' section, ''text renderer'' subsection, open the ''freetype''
page. You can then set the font and its size. For the font, you have to
select a font file. Under Windows, they can be found in
''C:WindowsFonts''. Under MacOS X, they are in
''/System/Library/Fonts''. Size can be set either relatively or as a
number of pixels.

You need to restart your stream for the font modifications to take
effect.

===Subtitles files===

While modern file formats like Matroska or OGM can handle subtitles
directly, older formats like AVI can't. Therefore, a number of subtitles
files formats have been created. You need two files: the video file and
the subtitles files that only contains the text of the subtitles and
timestamps.

VLC can handle these types of subtitles files: *MicroDVD*\ SubRIP
*SubViewer*\ SSA *Sami*\ Vobsub (this one is quite special: it is not
made from text but from images, which means that you can't change the
fonts)

To open a subtitles file, use the Advanced Open dialog box (Menu File,
Open file). Select your file by clicking on the ''Browse'' button. Then,
check the ''Subtitle options'' checkbox and click on the Settings
button.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-sub-file.jpg
Select a subtitles file under Windows or Linux

You can then select the subtitles file by clicking the ''Browse''
button. You can also set a few options like character encoding,
alignment and size. The delay option allows you to delay the subtitles
against the video if they are not in sync. If they are not at the same
speed, you might also want to adjust the subtitles framerate.

Note: For Vobsub subtitles, you need to select the '''.idx''' file, not
the '''.sub''' file. Encoding, alignment and size won't have any effect
for Vobsub subtitles.

Font can be changed as explained in the previous section.

==Video and audio filters==

VLC includes a system of ''filters'' that allow you to modify the audio
and video.

===Deinterlacement and Post Processing===

VLC is able to deinterlace a video stream using different
deinterlacement methods. Deinterlacement can be enabled in the ''Video''
menu, ''Deinterlacement'' menu item. The ''Blend'' methods gives the
best results in most cases. The ''discard''method is a less resource
consuming alternative.

On some particular streams (MPEG 4, DIVX, XVID, Sorenson, etc.), some
additional image filtering can be applied to the video before display,
improving its quality in some cases. This can be enabled in the
''Video'' menu, ''Post processing'' menu item. Different levels of post
processing can be chosen here. A higher level means more filtering.

===Video filters===

VLC features several filters able to change the video (distortion,
brightness adjustment, motion blurring, etc.).

With the wxWidgets interface, filters can be easily enabled using the
Extended GUI. In the Video tab, simply select the filters to enable.
Image settings can be easily adjusted.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-vfilters.jpg
Video filters selection in the wxWidgets interface

You can enable these filters through the ''Extended Controls panel'' on
Mac OS X. Click on the triangle next to ''Video filters'' to select your
filters or expand the ''Adjust Image'' section to change the contrast,
hue, etc.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-osx-vfilters.jpg
Video filters selection in the Mac OS X interface

For better control, you need to go to the preferences. To select the
filters to be enabled, go to ''Video'', then to ''Filters''. In the
"video filter module" box, enter the names of the filters to enable,
separated by semicommas. Filters will be applied in the selected order.
Valid names are "clone", "wall", "transform", "adjust", "crop",
"deinterlace", "distort", "motionblur" and "logo".

If you want to tune the behavior of these filters, go to ''Video,
Filters, [your filter]''. For each filter, you will find a short
description and the options.

===Audio filters===

====Equalizer====

VLC features a 10-band graphical equalizer. You can display it by
activating the advanced GUI on wxWidgets or by clicking the
''Equalizer'' button on the MacOS X interface.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-equalizer.jpg
The equalizer in the wxWidgets interface

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-osx-equalizer.jpg
The equalizer in the MacOS X interface

Presets are available in the Audio menu in wxWidgets, or in the
Equalizer window in the MacOS X interface.

====Other audio filters====

At the moment, VLC features two other audio filters: a volume normalizer
and a filter providing sound spatialization with a headphone. They can
be enabled in the Audio tab of the extended GUI for the wxWidgets
interface and in the Audio section of the Extended Controls panel of the
Mac OS X interface.

For better control, you need to go to the preferences. To select the
filters to be enabled, go to ''Audio'', then to ''Filters''. In the
"audio filters" box, enter the names of the filters to enable, separated
by commas. Valid names are "equalizer", "normvol" and "headphone".

If you want to tune the behavior of these filters, go to ''Audio,
Filters, [your filter]''. The equalizer and headphone filters can be
tuned.

==Snapshots (aka, screenshots)== There are two ways to take snapshots
(i.e., screenshots or frame grabs) with VLC: #Go to Video -> Snapshot,
or #Press the snapshot hotkey #*Windows / Linux / Unix: Ctrl-Alt-s #*Mac
OS X: Command-Alt-s

When a snapshot is taken, it will briefly preview as a thumbnail with
its filename and then fade away.

To change the hotkey, go to Preferences -> Interface -> Hotkeys
settings. Check Advanced options, and set Take video snapshot.

===Snapshot location, format and name=== The snapshot location depends
upon your operating system: *Windows: My DocumentsMy Pictures*\ Linux /
Unix: $(HOME)/.vlc/ \*Mac OS X: Desktop/

The default format for snapshots is PNG, but this may be changed to
JPEG. Also, the default name for snapshots is ''vlcsnap-'' followed by a
timestamp that is ''not'' the time of the frame in the video you're
viewing.

The location, format and name of snapshots may be changed in the
Preferences. Also, you may substitute other text for ''vlcsnap-'' in the
''Video snapshot file prefix'' and you may choose to have snapshots
numbered sequentially (i.e., 000001, 000002, 000003, and so on) instead
of with a timestamp. As of version 0.9.0, you may even use
[[Documentation:Play HowTo/Format String|variables]] in the text used
for the filename. For example, ''$T'' (must be upper case) will insert
the video's time code into the file name. If you were to change the
prefix to ''Friends-$T-'' while watching a DVD of ''Friends'', then the
snapshot filenames would look something like this:
Friends-00_05_21-00004.png . This indicates a snapshot taken at 5
minutes and 21 seconds into the video; and it was the number 00004
snapshot of the day.

For a full list of variables, please see [[Documentation:Play
HowTo/Format String]].

==Hotkeys==

Most of VLC functions are accessible using hotkeys.

The list of the available hotkeys and their functions can be retrieved
and altered in the preferences panel of the player. In the wxWidgets
interface, preferences are available in the "Settings" menu,
"Preferences" menu item. In the MacOS X interface, open the "VLC" menu,
and select "Preferences". Select the "Hot keys" panel in the dialog.

As of version 0.9, a list of hotkeys is presented in a drop-down window.
To change one, double-click its name to select it. Then, press the new
key that will trigger the specified action. Modifier keys (such as
Control/Command and Alt) may also be used.

In earlier versions, several boxes give the list of modifiers for the
hotkey. To trigger an action using a hotkey, you need to press
simultaneously the keys corresponding to the different selected
modifiers as well as the key set in the dropdown.

To change the binding of a hotkey, select or deselect boxes
corresponding to the different modifiers, and change the key by using
the drop-down menu. Select the ''Save'' button to apply the changes.

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-hotkeys.jpg
The Hotkeys Panel - wxWidgets interface

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-osx-hotkeys.jpg
The Hotkeys Panel - MacOS X interface

==Basic troubleshooting==

===File does not play, only sound or only video===

Maybe the file you are trying to read is not fully supported. VLC does
not use the codec packs (the software that decodes video signals) you
might have installed. It comes with its own codecs. If there is no
open-source decoder for the format you are trying to read, it won't be
supported. (There is an exception, under Windows, for codecs that use
the DirectShow framework.)

To find out, open the Messages Window (View menu) and restart your
stream. Look for error messages (red messages)

http://www.videolan.org/doc/play-howto/en/images/play-howto/intf-wx-messages.jpg
The wxWidgets messages window

In this example, the file contains a IV41 video stream, a codec that is
not supported by VLC.

You may of course have other messages. If you post to a VideoLAN mailing
list or in the forum, please include such a log. It is very valuable in
troubleshooting.

===Weird VLC behavior and crashes===

A very common thing is a corrupted VLC preferences file. Don't hesitate
to delete it if problems appear suddenly. You will find in the FAQ
details on [http://www.videolan.org/doc/faq/en/index.html#id2470084 how
to delete your preferences file].

===Computer crashes / Video is corrupted===

Another common problem is buggy video drivers. Try upgrading them from
the website of your video card's manufacturer.

Also, you can try disabling Overlay (Preferences/General/Video, untick
"Overlay video output")

{{Documentation}}
