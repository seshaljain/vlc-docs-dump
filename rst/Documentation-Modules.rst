<div style="float: right; margin-left: 1em;">__TOC__</div> This page
lists most of the {{VLCSourceFolderdocumentation]] first.

To list all the available modules in your VLC build, use:
   {{%}} '''vlc --list'''

To list a module's configuration options, use:
   % '''vlc -p <modulename> --advanced --help-verbose'''

== Interfaces ==

=== Graphical === \* [[Documentation:Modules/macosQt4]] \*
[[Documentation:Modules/skins2wxWidgets]] (up to 0.9)

=== Text === <!--The next three tend to be listed in this order--> \*
[[Documentation:Modules/rctelnet]] (until 2.0.0) \*
[[Documentation:Modules/ncurses|ncurses]]

-  [[Documentation:Modules/lua|lua]]

=== Other === \* [[Documentation:Modules/http_intfHotkeys]] \*
[[Documentation:Modules/lircosc]] \*
[[Documentation:Modules/wiimote|Wiimote]]

== Outputs == === Audio Output === \*
[[Documentation:Modules/file_aoutportaudio]] (up to 2.0) \*
[[Documentation:Modules/sdl_aoutOpenSL ES]] Linux specific: \*
[[Documentation:Modules/alsaaRts]] (up to 0.9.10) \*
[[Documentation:Modules/esdjack]] \* [[Documentation:Modules/pulseOSS]]
macOS specific: \* {{docmodauhal}} (HAL AudioUnit) Windows specific: \*
[[Documentation:Modules/directx_aoutWASAPI]] \*
[[Documentation:Modules/waveout|waveout]]

=== Video Output === \* [[Documentation:Modules/aaColored ASCII Art]] \*
[[Documentation:Modules/imageOpenGL]] \*
[[Documentation:Modules/sdl_voutDirect framebuffer]] (up to 2.2.8) \*
[[Documentation:Modules/fbOpenGL (GLX)]] \*
[[Documentation:Modules/x11XVideo]] Windows specific: \*
[[Documentation:Modules/direct3dDirectX]] \*
[[Documentation:Modules/glwin32Windows GDI]]

=== Stream Output === <div class="col3"> \*
[[Documentation:Modules/autodelDelay]] \*
[[Documentation:Modules/descriptionDisplay]] \*
[[Documentation:Modules/dummy_soutDuplicate]] \*
[[Documentation:Modules/esGather]] \*
[[Documentation:Modules/rtpStandard (std)]] \*
[[Documentation:Modules/switcherTranscode]] \*
[[Documentation:Modules/transrate|Transrate]] (up to 1.0.2) </div>

The following are for use in the mosaic framework only: <div
class="col3"> \* [[Documentation:Modules/bridge-inBridge Out]] \*
[[Documentation:Modules/mosaic-bridge|Mosaic Bridge]] </div>

== Filters == === Audio Filters === === Video Filters === <div
class="col3"> \* [[Documentation:Modules/adjustAnaglyph 3D]] \*
[[Documentation:Modules/atmoColor Threshold]] \*
[[Documentation:Modules/distortLogo Erase]] \*
[[Documentation:Modules/extractFreeze]] \*
[[Documentation:Modules/gaussianblurGradfun]] \*
[[Documentation:Modules/gradientInvert]] \*
[[Documentation:Modules/motionblurNoise]] (up to 1.1.13) \*
[[Documentation:Modules/oldmoviePosterize]] \*
[[Documentation:Modules/psychedelicRipple]] \*
[[Documentation:Modules/rotateScene]] \*
[[Documentation:Modules/sepiaSharpen]] \*
[[Documentation:Modules/VHSWave]] </div>

The following video filters are for use in transcode only: \*
[[Transcode#Canvas_and_PaddingCrop Padd]]

The following video filters are for use in the mosaic framework only: \*
[[Documentation:Modules/alphamaskBlue Screen]]

=== Video Sub-Filters === \* [[Documentation:Modules/logoMarq]] \*
[[Documentation:Modules/mosaicRSS]] \*
[[Documentation:Modules/subsdelayTime]] (up to 0.8.6 - merged with marq)

=== Video Output Filters === \*
[[Documentation:Modules/cropDeinterlace]] \*
[[Documentation:Modules/logoMagnify]] \*
[[Documentation:Modules/puzzleTransform]]

==== Video Splitters ==== \* [[Documentation:Modules/clonePanoramix]] \*
[[Documentation:Modules/wall|Wall]]

=== Visualizations === \* [[Documentation:Modules/galaktosGoom]] \*
[[Documentation:Modules/projectmVisual]] \*
[[Documentation:Modules/vsxu|Vovoid VSXu]]

=== Access Filters === \* [[Documentation:Modules/bandwidthDump]] \*
[[Documentation:Modules/recordTimeshift]] (up to 0.9.9 - moved to core)

== Other == === Accesses === <div class="col3"> \*
[[Documentation:Modules/cddaDirectory]] \*
[[Documentation:Modules/dvdnavDVDRead Input]] - DVD without menus \*
[[Documentation:Modules/fakeFile Input]] - for reading local files \*
[[Documentation:Modules/ftpH.264 Video]] \*
[[Documentation:Modules/httpjpeg}} \* {{docmodMatroska stream]] \*
[[Documentation:Modules/mmsRaw Video]] - streams of bitmap images \*
[[Documentation:Modules/rtpRTSP]] \* {{docmodScreen Input]] - screen
feed \* [[Documentation:Modules/udpVCD]] </div>

Linux specific: \* [[Documentation:Modules/dc1394DVB Input]] \*
[[Documentation:Modules/pvrDV]] (through libdv) \*
[[Documentation:Modules/v4lVideo4Linux2 (v4l2)]]

Windows specific: \* [[Documentation:Modules/bdaDirectShow]]

macOS specific: \* [[Documentation:Modules/eyetvqtcapture]] (up to
2.2.8) - reads uncompressed video from internal iSights \*
{{docmodavcapture}}

=== Access Outputs === \* {{docmod|shout}} (shoutcast/icecast)

=== Codecs === ==== Audio ==== \* {{docmodflac}} \* {{docmodogg}} \*
{{docmodwav}}

==== Video ==== \* {{docmodnsv}} \* {{docmodvpx}}

==== Subtitles ==== \* [[Documentation:Modules/katesubtitle]] \*
{{docmod|telx}}

=== Demuxers === \* [[Documentation:Modules/avcodec|avcodec]] ("FFmpeg")

==== Playlist ==== \* {{docmod|playlist}} (formats are read with
sub-modules)

=== Muxers === \* {{docmodavformat}} \* {{docmoddaala}} \*
{{docmodmpjpeg}} \* {{docmodschroedinger}} \* {{docmodwav}}

=== Service Discovery === \* [[Documentation:Modules/bonjourDAAP]] \*
[[Documentation:Modules/halSAP]] \*
[[Documentation:Modules/shoutpodcast]] \*
[[Documentation:Modules/upnp|UPnP]]

=== Misc === \* [[Documentation:Modules/motion_controlNetsync]]

[[Category:Modules|*]] {{Documentation}}
