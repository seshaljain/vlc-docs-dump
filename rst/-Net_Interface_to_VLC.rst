.. raw:: mediawiki

   {{See also|C Sharp}}

.. raw:: mediawiki

   {{Outdated}}

Main Idea
---------

I started with Odysee's work `1 <http://forum.videolan.org/viewtopic.php?t=28553>`__ and wrote a .Net user control that uses libvlc interfaces to do what the ActiveX control does and more, like getting info about and getting/setting audio and subtitle tracks, aspect ratios, deinterlacing filters and more. This compiles in Visual C#.Net Express, free from Microsoft `2 <http://msdn2.microsoft.com/en-us/vcsharp>`__.

I should say this works with VLC 0.8.6 and 0.8.6a, no guarantees for other versions. Any dll or exe you create with this code needs to be in the same directory as libvlc.dll and have the plugins sub-directory below it (copy libvlc.dll and plugins to the bin/Debug and bin/Release directories when developing C# projects). One common error is to forget to call Initialize() on the NativeLibVlc instance (only a problem if you're using NativeLibVlc without the VlcUserControl wrapper control). Initialize() is best called in this case from the form_OnLoad or control_OnLoad event, not in the constructor of its owner window, (see VlcUserControl.cs's constructor and function OnLoad for an example of properly initializing a NativeLibVlc object).

**More hints:** Except for Volume and State, most Vlc properties like AudioTrack can't be set until media is actually playing in the control. This is because Vlc is multi-threaded, so even after AddToPlaylist is called nothing will be playing for up to several seconds. A programmer needs to poll the State property of the control waiting for Play state to set the other properties. This isn't as big a problem as it seems, since nearly all the properties can be set using the option flags when calling AddToPlaylist or AddAndPlay. For example if you knew you wanted the 2nd audio track of a file you could add the option ":audio-track=1" when calling AddToPlaylist or AddAndPlay (see Vlc command-line options for the full list).

Tappen

Updates
-------

Update Jan. 16, 2007:

| ``- removed Browsability from all native Vlc properties of VlcUserControl.cs.  This allows placing the control on Forms without errors in Design mode.``
| ``- files changed: VlcUserControl.cs only``

Update Jan. 11, 2007:

| ``- added ActiveX functionality``
| ``- added redundant interfaces to support Javascript programming because Javascript doesn't support ActiveX arrays or Out parameters``
| ``- fixed install directory dependence.  Now the directory the assembly exists in is always used as the install directory.``
| ``- fixed PlaylistIndex and PlaylistCount properties``
| ``- fixed Cropping``
| ``- added NowPlaying event, and ProducingEvents property which controls it``
| ``- added Contrast, Brightness, Hue, Saturation, Gamma properties and AllowVideoAdjustments property which controls them``
| ``- added GetConfigVariable method``
| ``- added VLanControl.snk file to allow the control to be signed, required by ActiveX ``
| ``- added .Net_Test.html file to demonstrate ActiveX usage with Javascript``

Install
-------

Register the dll for use as an ActiveX component by running:

``   %WINDIR%\Microsoft.net\Framework\v2.0.50727\regasm VLanControl.dll /codebase``

If you DON'T want to use this code as an ActiveX component, for example if you're writing a C# program, remove VLanControl.snk from the project and in the project properties, Signing tab, uncheck "Sign the assembly".

Files
~~~~~

Most of those files are licenced under the `GNU General Public License <http://www.gnu.org/copyleft/gpl.html>`__. See `Intellectual_Properties <Intellectual_Properties>`__.

`IPlayer.cs <IPlayer>`__ is the main Interface supported by VlcUserControl, since something like this deserves the Bridge pattern treatment. `IPlayer.cs <IPlayer>`__ should really be in a different assembly from the control to allow other controls to support it and be used interchange-ably with VlcUserControl but that's up to you developers.

`NativeLibVlc.cs <NativeLibVlc.cs>`__ contains the .Net Interop versions of the native VLC C++ structures and functions, and a class which wraps these calls in C#.

`VlcUserControl.cs <VlcUserControl.cs>`__ contains the non-designer part of the VlcUserControl class, derived from System.Windows.Forms.UserControl, which can be used either directly on C# forms, or as an ActiveX control if wrapped and registered in a dll. VlcUserControl acts mostly as a wrapper for the `NativeLibVlc.cs <NativeLibVlc.cs>`__ functions, but also has a few complications such as allowing multiple playback position moves in quick succession or when paused, since VLC, as an asynchronous player, will not return the correct position for a significant part of a second after a move. VlcUserControl also handles (optionally, default is on, variable bool useVlcCrop) cropping instead of using the VLC cropping feature, (see InnerVlcWindow.cs comment below for explanation). Thirdly, VlcUserControl attempts to minimize the inaccuracy of moving by timestamp in Mpeg-2 files since VLC doesn't do this well (optional, default is off, variable bool useMpegVbrOffset).

`VlcUserControl.Designer.cs <VlcUserControl.Designer.cs>`__ contains the designer part of the VlcUserControl class.

`VlcUserControl.resx <VlcUserControl.resx>`__ contains the layout and resource definition of the VlcUserControl class.

`InnerVlcWindow.cs <InnerVlcWindow.cs>`__ is an essentially empty class. One instance is created as a child window by each VlcUserControl class instance where VLC will actually draw the video. This allows VlcUserControl to act as a "viewport" and crop the VLC output since the cropping filter of VLC leaves something to be desired when used in a player application (it can't co-exist with DeInterlace filters most importantly).

`InnerVlcWindow.Designer.cs <InnerVlcWindow.Designer.cs>`__ contains the designer part of the InnerVlcWindow class.

`AssemblyInfo.cs <AssemblyInfo.cs>`__ is an optional file containing sample assembly information if the above classes are placed in a separate dll module in your code hierarchy. As usual in .Net 2.0 projects, it should be placed in a sub-directory named "Properties".

`VLanControl.csproj <VLanControl.csproj>`__ is an optional project file for all the above files.

`VLanControl.snk <VLanControl.snk>`__ is an optional key file for use in signing the dll.

`.Net_Test.html <.Net_Test.html>`__ is an optional ActiveX demonstration file.

.Net HTTP connector
-------------------

There is a .Net lib for remote connexion with HTTP protocol. https://github.com/jurion/.NET-VLC-remote-http-control- Content : Lib, Win8.1 app and WP8.1 App

`Category:Bindings <Category:Bindings>`__
