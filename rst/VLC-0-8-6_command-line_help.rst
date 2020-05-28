{{See alsoConsole|label2=Console interfaces}} {{WindowsCLI}} Here's the
output of ''vlc --longhelp --advanced --help-verbose'' of the version
0.8.6i in Windows.

   <nowiki>

Usage: vlc [options] [stream] ... You can specify multiple streams on
the commandline. They will be enqueued in the playlist. The first item
specified will be played first.

Options-styles:
   --option A global option that is set for the duration of the program.
      -option A single letter version of a global --option. :option An
      option that only applies to the stream directly before it and that
      overrides previous settings.

Stream MRL syntax:
   [[access][/demux]://]URL[@[title][:chapter][-[title][:chapter]]]
   [:option=value ...]

   Many of the global --options can also be used as MRL specific
   :options. Multiple :option=value pairs can be specified.

URL syntax:
   [file://%5Dfilename Plain media file
   `http://ip:port/file <http://ip:port/file>`__ HTTP URL
   `ftp://ip:port/file <ftp://ip:port/file>`__ FTP URL
   `mms://ip:port/file <mms://ip:port/file>`__ MMS URL screen:// Screen
   capture [dvd://][device][@raw_device] DVD device [vcd://][device] VCD
   device [cdda://][device] Audio CD device udp:[[<source
   address>]@[<bind address>][:<bind port>]] UDP stream sent by a
   streaming server vlc:pause:<seconds> Special item to pause the
   playlist for a certain time vlc:quit Special item to quit VLC

Help options
   -h, --help print help for VLC (can be combined with
      --advanced)

   -H, --longhelp print help for VLC and all its modules (can
      be combined with --advanced)

   --advanced print help for the advanced options
      --help-verbose ask for extra verbosity when displaying help

   -l, --list print a list of available modules -p, --module <string>
   print help on a specific module (can be combined with --advanced)
   --save-config save the current command line options in the config
   --reset-config reset the current config to the default values
   --config <string> use alternate config file --reset-plugins-cache
   resets the current plugins cache --version print version information

Audio
   --audio, --no-audio Enable audio (default enabled)
      You can completely disable the audio output. The audio decoding
      stage will not take place, thus saving some processing power.
      (default enabled)

   --volume <integer> Default audio volume
      You can set the default audio output volume here, in a range from
      0 to 1024.

   --spdif, --no-spdif Use S/PDIF when available (default disabled)
      S/PDIF can be used by default when your hardware supports it as
      well as the audio stream being played. (default disabled)

   --force-dolby-surround {0 (Auto), 1 (On), 2 (Off)}
      Force detection of Dolby Surround

   Use this when you know your stream is (or is
      not) encoded with Dolby Surround but fails to be detected as such.
      Even if the stream is not actually encoded with Dolby Surround,
      turning on this option might enhance your experience, especially
      when combined with the Headphone Channel Mixer.

   --audio-filter <string> Audio filters
      This adds audio post processing filters, to modify the sound
      rendering.

   --audio-visual <string> Audio visualizations
      This adds visualization modules (spectrum analyzer, etc.).

Video
   -f, --fullscreen, --no-fullscreen
      Fullscreen video output (default disabled)

   Start video in fullscreen mode (default
      disabled)

   --overlay, --no-overlay Overlay video output (default disabled)
      Overlay is the hardware acceleration capability of your video card
      (ability to render video directly). VLC will try to use it by
      default. (default disabled)

   --video-on-top, --no-video-on-top
      Always on top (default disabled)

   Always place the video window on top of other
      windows. (default disabled)

   --snapshot-path <string> Video snapshot directory (or filename)
      Directory where the video snapshots will be stored.

   --snapshot-prefix <string> Video snapshot file prefix
      Video snapshot file prefix

   --snapshot-format {png,jpg}
      Video snapshot format

   Image format which will be used to store the
      video snapshots

   --snapshot-preview, --no-snapshot-preview
      Display video snapshot preview (default enabled)

   Display the snapshot preview in the screen's
      top-left corner. (default enabled)

   --snapshot-sequential, --no-snapshot-sequential
      Use sequential numbers instead of timestamps (default disabled)

   Use sequential numbers instead of timestamps
      for snapshot numbering (default disabled)

   --crop <string> Video cropping
      This forces the cropping of the source video. Accepted formats are
      x:y (4:3, 16:9, etc.) expressing the global image aspect.

   --custom-crop-ratios <string>
      Custom crop ratios list

   Comma seperated list of crop ratios which
      will be added in the interface's crop ratios list.

   --aspect-ratio <string> Source aspect ratio
      This forces the source aspect ratio. For instance, some DVDs claim
      to be 16:9 while they are actually 4:3. This can also be used as a
      hint for VLC when a movie does not have aspect ratio information.
      Accepted formats are x:y (4:3, 16:9, etc.) expressing the global
      image aspect, or a float value (1.25, 1.3333, etc.) expressing
      pixel squareness.

   --custom-aspect-ratios <string>
      Custom aspect ratios list

   Comma seperated list of aspect ratios which
      will be added in the interface's aspect ratio list.

   --vout-filter <string> Video filter module
      This adds post-processing filters to enhance the picture quality,
      for instance deinterlacing, or to clone or distort the video
      window.

Subpictures
   --osd, --no-osd On Screen Display (default enabled)
      VLC can display messages on the video. This is called OSD (On
      Screen Display). (default enabled)

   --sub-file <string> Use subtitle file
      Load this subtitle file. To be used when autodetect cannot detect
      your subtitle file.

   --sub-autodetect-file, --no-sub-autodetect-file
      Autodetect subtitle files (default enabled)

   Automatically detect a subtitle file, if no
      subtitle filename is specified (based on the filename of the
      movie). (default enabled)

   --sub-filter <string> Subpictures filter module
      This adds so-called "subpicture filters". These filters overlay
      some images or text over the video (like a logo, arbitraty
      text...).

   --audio-language <string> Audio language
      Language of the audio track you want to use (comma separated, two
      or three letter country code).

   --sub-language <string> Subtitle language
      Language of the subtitle track you want to use (comma separated,
      two or tree letter country code).

   --input-repeat <integer> Input repetitions
      Number of time the same input will be repeated

   --dvd <string> DVD device
      This is the default DVD drive (or file) to use. Don't forget the
      colon after the drive letter (eg. D:)

   --vcd <string> VCD device
      This is the default VCD device to use.

   --cd-audio <string> Audio CD device
      This is the default Audio CD device to use.

   --server-port <integer> UDP port
      This is the default port used for UDP streams. Default is 1234.

-6, --ipv6, --no-ipv6 Force IPv6 (default disabled)
   IPv6 will be used by default for all connections. (default disabled)

-4, --ipv4, --no-ipv4 Force IPv4 (default disabled)
   IPv4 will be used by default for all connections. (default disabled)

Input
   --access-filter <string> Access filter module
      Access filters are used to modify the stream that is being read.
      This is used for instance for timeshifting.

   --high-priority, --no-high-priority
      Increase the priority of the process (default disabled)

   Increasing the priority of the process will
      very likely improve your playing experience as it allows VLC not
      to be disturbed by other applications that could otherwise take
      too much processor time. However be advised that in certain
      circumstances (bugs) VLC could take all the processor time and
      render the whole system unresponsive which might require a reboot
      of your machine. (default disabled)

Playlist
   -Z, --random, --no-random Play files randomly forever (default disabled)
      VLC will randomly play files in the playlist until interrupted.
      (default disabled)

   -L, --loop, --no-loop Repeat all (default disabled)
      VLC will keep playing the playlist indefinitely. (default
      disabled)

   -R, --repeat, --no-repeat Repeat current item (default disabled)
      VLC will keep playing the current playlist item. (default
      disabled)

   --play-and-stop, --no-play-and-stop
      Play and stop (default disabled)

   Stop the playlist after each played playlist
      item. (default disabled)

   --open <string> Default stream
      This stream will always be opened at VLC startup.

   --auto-preparse, --no-auto-preparse
      Automatically preparse files (default enabled)

   Automatically preparse files added to the
      playlist (to retrieve some metadata). (default enabled)

   -S, --services-discovery <string>
      Services discovery modules

   Specifies the services discovery modules to
      load, separated by semi-colons. Typical values are sap, hal, ...

   -v, --verbose <integer> Verbosity (0,1,2)
      This is the verbosity level (0=only errors and standard messages,
      1=warnings, 2=debug).

   --language {auto,en,en_GB,ar,ca,cs,da,de,es,fa,fr,gl,he,hu,it,ja,ka,ko,ms,ne,nl,oc,pl,pt_BR,ro,ru,sk,sl,sr,sv,th,tr,zh_CN,zh_TW}
      Language

   You can manually select a language for the
      interface. The system language is auto-detected if "auto" is
      specified here.

   --advanced, --no-advanced Show advanced options (default enabled)
      When this is enabled, the preferences and/or interfaces will show
      all available options, including those that most users should
      never touch. (default enabled)

   --interact, --no-interact Interface interaction (default enabled)
      When this is enabled, the interface will show a dialog box each
      time some user input is required. (default enabled)

   --show-intf, --no-show-intf
      Show interface with mouse (default disabled)

   When this is enabled, the interface is shown
      when you move the mouse to the edge of the screen in fullscreen
      mode. (default disabled)

   -I, --intf <string> Interface module
      This is the main interface used by VLC. The default behavior is to
      automatically select the best module available.

   --extraintf <string> Extra interface modules
      You can select "additional interfaces" for VLC. They will be
      launched in the background in addition to the default interface.
      Use a comma separated list of interface modules. (common values
      are "rc" (remote control), "http", "gestures" ...)

   --control <string> Control interfaces
      You can select control interfaces for VLC.

Hot keys
   --key-fullscreen <integer> Fullscreen
      Select the hotkey to use to swap fullscreen state.

   --key-play-pause <integer> Play/Pause
      Select the hotkey to use to swap paused state.

   --key-faster <integer> Faster
      Select the hotkey to use for fast forward playback.

   --key-slower <integer> Slower
      Select the hotkey to use for slow motion playback.

   --key-next <integer> Next
      Select the hotkey to use to skip to the next item in the playlist.

   --key-prev <integer> Previous
      Select the hotkey to use to skip to the previous item in the
      playlist.

   --key-stop <integer> Stop
      Select the hotkey to stop playback.

   --key-jump-extrashort <integer>
      Very short backwards jump

   Select the hotkey to make a very short
      backwards jump.

   --key-jump+extrashort <integer>
      Very short forward jump

   Select the hotkey to make a very short
      forward jump.

   --key-jump-short <integer> Short backwards jump
      Select the hotkey to make a short backwards jump.

   --key-jump+short <integer> Short forward jump
      Select the hotkey to make a short forward jump.

   --key-jump-medium <integer>
      Medium backwards jump

   Select the hotkey to make a medium backwards
      jump.

   --key-jump+medium <integer>
      Medium forward jump

   Select the hotkey to make a medium forward
      jump.

   --key-jump-long <integer> Long backwards jump
      Select the hotkey to make a long backwards jump.

   --key-jump+long <integer> Long forward jump
      Select the hotkey to make a long forward jump.

   --key-quit <integer> Quit
      Select the hotkey to quit the application.

   --key-vol-up <integer> Volume up
      Select the key to increase audio volume.

   --key-vol-down <integer> Volume down
      Select the key to decrease audio volume.

   --key-vol-mute <integer> Mute
      Select the key to mute audio.

   --key-audio-track <integer>
      Cycle audio track

   Cycle through the available audio
      tracks(languages).

   --key-subtitle-track <integer>
      Cycle subtitle track

   ..

      Cycle through the available subtitle tracks.

   --key-aspect-ratio <integer>
      Cycle source aspect ratio

   Cycle through a predefined list of source
      aspect ratios.

   --key-crop <integer> Cycle video crop
      Cycle through a predefined list of crop formats.

   --key-deinterlace <integer>
      Cycle deinterlace modes

   ..

      Cycle through deinterlace modes.

   --extrashort-jump-size <integer>
      Very short jump length

   ..

      Very short jump length, in seconds.

   --short-jump-size <integer>
      Short jump length

   ..

      Short jump length, in seconds.

   --medium-jump-size <integer>
      Medium jump length

   ..

      Medium jump length, in seconds.

   --long-jump-size <integer> Long jump length
      Long jump length, in seconds.

   --bookmark1 <string> Playlist bookmark 1
      This allows you to define playlist bookmarks.

   --bookmark2 <string> Playlist bookmark 2
      This allows you to define playlist bookmarks.

   --bookmark3 <string> Playlist bookmark 3
      This allows you to define playlist bookmarks.

   --bookmark4 <string> Playlist bookmark 4
      This allows you to define playlist bookmarks.

   --bookmark5 <string> Playlist bookmark 5
      This allows you to define playlist bookmarks.

   --bookmark6 <string> Playlist bookmark 6
      This allows you to define playlist bookmarks.

   --bookmark7 <string> Playlist bookmark 7
      This allows you to define playlist bookmarks.

   --bookmark8 <string> Playlist bookmark 8
      This allows you to define playlist bookmarks.

   --bookmark9 <string> Playlist bookmark 9
      This allows you to define playlist bookmarks.

   --bookmark10 <string> Playlist bookmark 10
      This allows you to define playlist bookmarks.

ATSC A/52 (AC-3) audio decoder
   --a52-dynrng, --no-a52-dynrng
      A/52 dynamic range compression (default enabled)

   Dynamic range compression makes the loud
      sounds softer, and the soft sounds louder, so you can more easily
      listen to the stream in a noisy environment without disturbing
      anyone. If you disable the dynamic range compression the playback
      will be more adapted to a movie theater or a listening room.
      (default enabled)

Standard filesystem directory input
   --recursive {none,collapse,expand}
      Subdirectory behavior

   Select whether subdirectories must be
      expanded.

none: subdirectories do not appear
   in the playlist.

collapse: subdirectories
   appear but are expanded on first play.

expand: all subdirectories are
   expanded.

--ignore-filetypes <string>
   Ignored extensions

Files with these extensions will not be added
   to playlist when opening a directory.

This is
   useful if you add directories that contain playlist files for
   instance. Use a comma-separated list of extensions.

Dump
   --dump-force, --no-dump-force
      Force use of dump module (default disabled)

   Activate the dump module even for media with
      fast seeking. (default disabled)

   --dump-margin <integer> Maximum size of temporary file (Mb)
      The dump module will abort dumping of the media if more than this
      much megabyte were performed.

Timeshift
   --timeshift-dir <string> Timeshift directory
      Directory used to store the timeshift temporary files.

   --timeshift-force, --no-timeshift-force
      Force use of the timeshift module (default disabled)

   Force use of the timeshift module even if the
      access declares that it can control pace or pause. (default
      disabled)

FTP input
   --ftp-user <string> FTP user name
      User name that will be used for the connection.

   --ftp-pwd <string> FTP password
      Password that will be used for the connection.

   --ftp-account <string> FTP account
      Account that will be used for the connection.

HTTP input
   --http-proxy <string> HTTP proxy
      HTTP proxy to be usesd It must be of the form
      http://%5Buser\ [:pass]@]myproxy.mydomain:myport/ ; if empty, the
      http_proxy environment variable will be tried.

Microsoft Media Server (MMS) input
   --mms-maxbitrate <integer> Maximum bitrate
      Select the stream with the maximum bitrate under that limit.

IceCAST output
   --sout-shout-name <string> Stream name
      Name to give to this stream/channel on the icecast server.

   --sout-shout-description <string>
      Stream description

   Description of the stream content or
      information about your channel.

..

   UDP stream output

   SMB input
      --smb-user <string> SMB user name
         User name that will be used for the connection.

      --smb-pwd <string> SMB password
         Password that will be used for the connection.

      --smb-domain <string> SMB domain
         Domain/Workgroup that will be used for the connection.

   Image properties filter
      --contrast <float> Image contrast (0-2)
         Set the image contrast, between 0 and 2. Defaults to 1.

      --brightness <float> Image brightness (0-2)
         Set the image brightness, between 0 and 2. Defaults to 1.

      --hue <integer> Image hue (0-360)
         Set the image hue, between 0 and 360. Defaults to 0.

      --saturation <float> Image saturation (0-3)
         Set the image saturation, between 0 and 3. Defaults to 1.

      --gamma <float> Image gamma (0-10)
         Set the image gamma, between 0.01 and 10. Defaults to 1.

      --brightness-threshold, --no-brightness-threshold
         Brightness threshold (default disabled)

      When this mode is enabled, pixels will be
         shown as black or white. The threshold value will be the
         brighness defined below. (default disabled)

   File audio output
      --audiofile-file <string> Output file
         File to which the audio samples will be written to.

   AVI demuxer
      --avi-index {0 (Ask), 1 (Always fix), 2 (Never fix)}
         Force index creation

      Recreate a index for the AVI file. Use this
         if your AVI file is damaged or incomplete (not seekable).

   Clone video filter
      --clone-count <integer> Number of clones
         Number of video windows in which to clone the video.

   Crop video filter
      --crop-geometry <string> Crop geometry (pixels)
         Set the geometry of the zone to crop. This is set as <width> x
         <height> + <left offset> + <top offset>.

      --autocrop, --no-autocrop Automatic cropping (default disabled)
         Automatic black border cropping. (default disabled)

   Deinterlacing video filter
      --deinterlace-mode {discard,blend,mean,bob,linear,x}
         Deinterlace mode

      ..

         Deinterlace method to use for local playback.

      --sout-deinterlace-mode {discard,blend,mean,bob,linear,x}
         Streaming deinterlace mode

      ..

         Deinterlace method to use for streaming.

   File dumpper
      --demuxdump-file <string> Dump filename
         Name of the file to which the raw stream will be dumped.

      --demuxdump-append, --no-demuxdump-append
         Append to existing file (default disabled)

      If the file already exists, it will not be
         overwritten. (default disabled)

   Distort video filter
      --distort-mode {wave,ripple,gradient,edge,hough,psychedelic}
         Distort mode

      Distort mode, one of "wave", "ripple",
         "gradient", "edge", "hough" and "psychedelic".

      --distort-gradient-type <integer>
         Gradient image type

      Gradient image type (0 or 1). 0 will turn the
         image to white while 1 will keep colors.

      --distort-cartoon, --no-distort-cartoon
         Apply cartoon effect (default enabled)

      Apply cartoon effect. It is only used by
         "gradient" and "edge". (default enabled)

   DirectShow input
      --dshow-vdev {,none} Video device name
         Name of the video device that will be used by the DirectShow
         plugin. If you don't specify anything, the default device will
         be used.

      --dshow-adev {,none} Audio device name
         Name of the audio device that will be used by the DirectShow
         plugin. If you don't specify anything, the default device will
         be used. You can specify a standard size (cif, d1, ...) or
         <width>x<height>

      --dshow-size <string> Video size
         Size of the video that will be displayed by the DirectShow
         plugin. If you don't specify anything the default size for your
         device will be used.

   DTS Coherent Acoustics audio decoder
      --dts-dynrng, --no-dts-dynrng
         DTS dynamic range compression (default enabled)

      Dynamic range compression makes the loud
         sounds softer, and the soft sounds louder, so you can more
         easily listen to the stream in a noisy environment without
         disturbing anyone. If you disable the dynamic range compression
         the playback will be more adapted to a movie theater or a
         listening room. (default enabled)

   Dummy interface function
      --dummy-quiet, --no-dummy-quiet
         Do not open a DOS command box interface (default disabled)

      By default the dummy interface plugin will
         start a DOS command box. Enabling the quiet mode will not bring
         this command box but can also be pretty annoying when you want
         to stop VLC and no video window is open. (default disabled)

   DVB subtitles decoder
      --dvbsub-x <integer> Decoding X coordinate
         X coordinate of the rendered subtitle

      --dvbsub-y <integer> Decoding Y coordinate
         Y coordinate of the rendered subtitle

      --sout-dvbsub-x <integer> Encoding X coordinate
         X coordinate of the encoded subtitle

      --sout-dvbsub-y <integer> Encoding Y coordinate
         Y coordinate of the encoded subtitle

   DVDnav Input
      --dvdnav-angle <integer> DVD angle
         Default DVD angle.

      --dvdnav-menu, --no-dvdnav-menu
         Start directly in menu (default enabled)

      Start the DVD directly in the main menu. This
         will try to skip all the useless warning introductions.
         (default enabled)

   DVDRead Input (DVD without menu support)
      --dvdread-angle <integer> DVD angle
         Default DVD angle.

   Equalizer with 10 bands
      --equalizer-preset {flat,classical,club,dance,fullbass,fullbasstreble,fulltreble,headphones,largehall,live,party,pop,reggae,rock,ska,soft,softrock,techno}
         Equalizer preset

      ..

         Preset to use for the equalizer.

   Fake video decoder
      --fake-file <string> Image file
         Path of the image file for fake input.

      --fake-deinterlace, --no-fake-deinterlace
         Deinterlace video (default disabled)

      Deinterlace the image after loading it.
         (default disabled)

      --fake-deinterlace-module {deinterlace,ffmpeg-deinterlace}
         Deinterlace module

      ..

         Deinterlace module to use.

   FFmpeg audio/video decoder/encoder ((MS)MPEG4,SVQ1,H263,WMV,WMA)
      --ffmpeg-workaround-bugs <integer>
         Workaround bugs

      ..

         Try to fix some bugs:

1 autodetect 2 old msmpeg4 4 xvid interlaced 8 ump4 16 no padding 32 ac
vlc 64 Qpel chroma. This must be the sum of the values. For example, to
fix "ac vlc" and "ump4", enter 40. --ffmpeg-hurry-up,
--no-ffmpeg-hurry-up Hurry up (default disabled) The decoder can
partially decode or skip frame(s) when there is not enough time. It's
useful with low CPU power but it can produce distorted pictures.
(default disabled) --ffmpeg-pp-q <integer> Post processing quality
Quality of post processing. Valid range is 0 to 6 Higher levels require
considerable more CPU power, but produce better looking pictures.
--sout-ffmpeg-hq {rd,bits,simple} Quality level Quality level for the
encoding of motions vectors (this can slow down the encoding very much).
--sout-ffmpeg-keyint <integer> Ratio of key frames Number of frames that
will be coded for one key frame. --sout-ffmpeg-bframes <integer> Ratio
of B frames Number of B frames that will be coded between two reference
frames. --sout-ffmpeg-hurry-up, --no-sout-ffmpeg-hurry-up Hurry up
(default disabled) The encoder can make on-the-fly quality tradeoffs if
your CPU can't keep up with the encoding rate. It will disable trellis
quantization, then the rate distortion of motion vectors (hq), and raise
the noise reduction threshold to ease the encoder's task. (default
disabled)

   Freetype2 font renderer
      --freetype-font <string> Font
         Filename for the font you want to use

      --freetype-color {0 (Black), 8421504 (Gray), 12632256 (Silver), 16777215 (White), 8388608 (Maroon), 16711680 (Red), 16711935 (Fuchsia), 16776960 (Yellow), 8421376 (Olive), 32768 (Green), 32896 (Teal), 65280 (Lime), 8388736 (Purple), 128 (Navy), 255 (Blue), 65535 (Aqua)}
         Text default color

      The color of the text that will be rendered
         on the video. This must be an hexadecimal (like HTML colors).
         The first two chars are for red, then green, then blue. #000000
         = black, #FF0000 = red, #00FF00 = green, #FFFF00 = yellow (red
         + green), #FFFFFF = white

      --freetype-rel-fontsize {20 (Smaller), 18 (Small), 16 (Normal), 12 (Large), 6 (Larger)}
         Relative font size

      This is the relative default size of the
         fonts that will be rendered on the video. If absolute font size
         is set, relative size will be overriden.

      --freetype-effect {1 (Background), 2 (Outline), 3 (Fat Outline)}
         Font Effect

      It is possible to apply effects to the
         rendered text to improve its readability.

   Mouse gestures control interface
      --gestures-button {left,middle,right}
         Trigger button

      ..

         Trigger button for mouse gestures.

   GnuTLS TLS encryption layer
      --tls-check-cert, --no-tls-check-cert
         Check TLS/SSL server certificate validity (default enabled)

      This ensures that the server certificate is
         valid (i.e. signed by an approved Certification Authority).
         (default enabled)

      --tls-check-hostname, --no-tls-check-hostname
         Check TLS/SSL server hostname in certificate (default enabled)

      This ensures that the server hostname in
         certificate matches the requested host name. (default enabled)

   Goom effect
      --goom-width <integer> Goom display width
         This allows you to set the resolution of the Goom display
         (bigger resolution will be prettier but more CPU intensive).

      --goom-height <integer> Goom display height
         This allows you to set the resolution of the Goom display
         (bigger resolution will be prettier but more CPU intensive).

      --goom-speed <integer> Goom animation speed
         This allows you to set the animation speed (between 1 and 10,
         defaults to 6).

   Growl Notification Plugin
      --growl-server <string> Growl server
         This is the host to which Growl notifications will be sent. By
         default, notifications are sent locally.

      --growl-password <string> Growl password
         Growl password on the server.

   Headphone virtual spatialization effect
      --headphone-dim <integer> Characteristic dimension
         Distance between front left speaker and listener in meters.

   Image video output
      --image-out-format {png,jpeg}
         Image format

      ..

         Format of the output images (png or jpg).

      --image-out-ratio <integer>
         Recording ratio

      Ratio of images to record. 3 means that one
         image out of three is recorded.

      --image-out-prefix <string>
         Filename prefix

      Prefix of the output images filenames. Output
         filenames will have the "prefixNUMBER.format" form.

      --image-out-replace, --no-image-out-replace
         Always write to the same file (default disabled)

      Always write to the same file instead of
         creating one file per image. In this case, the number is not
         appended to the filename. (default disabled)

   File logging
      --logfile <string> Log filename
         Specify the log filename.

      --logmode {text,html} Log format
         Specify the log format. Available choices are "text" (default)
         and "html".

   Logo video filter
      --logo-file <string> Logo filenames
         Full path of the image files to use. Format is <image>[,<delay
         in ms>[,<alpha>]][;<image>[ ,<delay>[,<alpha>]]][;...]. If you
         only have one file, simply enter its filename.

      --logo-transparency <integer>
         Transparency of the logo

      Logo transparency value (from 0 for full
         transparency to 255 for full opacity).

      --logo-position {0 (Center), 1 (Left), 2 (Right), 4 (Top), 8 (Bottom), 5 (Top-Left), 6 (Top-Right), 9 (Bottom-Left), 10 (Bottom-Right)}
         Logo position

      Enforce the logo position on the video
         (0=center, 1=left, 2=right, 4=top, 8=bottom, you can also use
         combinations of these values, eg 6 = top-right).

   Marquee display
      --marq-marquee <string> Text
         Marquee text to display.

      --marq-position <integer> Marquee position
         You can enforce the marquee position on the video (0=center,
         1=left, 2=right, 4=top, 8=bottom, you can also use combinations
         of these values, eg 6 = top-right).

      --marq-opacity <integer> Opacity
         Opacity (inverse of transparency) of overlayed text. 0 =
         transparent, 255 = totally opaque.

      --marq-color {-268435456 (Default), 0 (Black), 8421504 (Gray), 12632256 (Silver), 16777215 (White), 8388608 (Maroon), 16711680 (Red), 16711935 (Fuchsia), 16776960 (Yellow), 8421376 (Olive), 32768 (Green), 32896 (Teal), 65280 (Lime), 8388736 (Purple), 128 (Navy), 255 (Blue), 65535 (Aqua)}
         Color

      Color of the text that will be rendered on
         the video. This must be an hexadecimal (like HTML colors). The
         first two chars are for red, then green, then blue. #000000 =
         black, #FF0000 = red, #00FF00 = green, #FFFF00 = yellow (red +
         green), #FFFFFF = white

      --marq-size <integer> Font size, pixels
         Font size, in pixels. Default is -1 (use default font size).

      --marq-timeout <integer> Timeout
         Number of milliseconds the marquee must remain displayed.
         Default value is 0 (remains forever).

   M-JPEG camera demuxer
      --mjpeg-fps <float> Frames per Second
         This is the desired frame rate when playing MJPEG from a file.
         Use 0 (this is the default value) for a live stream (from a
         camera).

   MOD demuxer (libmodplug)
      --mod-noisereduction, --no-mod-noisereduction
         Noise reduction (default enabled)

      Enable noise reduction algorithm (default
         enabled)

      --mod-reverb, --no-mod-reverb
         Reverb (default disabled)

      ..

         Enable reverberation (default disabled)

      --mod-megabass, --no-mod-megabass
         Mega bass (default disabled)

      ..

         Enable megabass mode (default disabled)

      --mod-surround, --no-mod-surround
         Surround (default disabled)

      ..

         Surround (default disabled)

   Mosaic video sub filter
      --mosaic-alpha <integer> Transparency
         Transparency of the mosaic foreground pictures. 0 means
         transparent, 255 opaque (default).

      --mosaic-height <integer> Height
         Total height of the mosaic, in pixels.

      --mosaic-width <integer> Width
         Total width of the mosaic, in pixels.

      --mosaic-position {0 (auto), 1 (fixed)}
         Positioning method

      Positioning method for the mosaic. auto:
         automatically choose the best number of rows and columns.
         fixed: use the user-defined number of rows and columns.

      --mosaic-rows <integer> Number of rows
         Number of image rows in the mosaic (only used if positionning
         method is set to "fixed".

      --mosaic-cols <integer> Number of columns
         Number of image columns in the mosaic (only used if
         positionning method is set to "fixed".

      --mosaic-keep-aspect-ratio, --no-mosaic-keep-aspect-ratio
         Keep aspect ratio (default disabled)

      Keep the original aspect ratio when resizing
         mosaic elements. (default disabled)

      --mosaic-keep-picture, --no-mosaic-keep-picture
         Keep original size (default disabled)

      Keep the original size of mosaic elements.
         (default disabled)

      --mosaic-order <string> Elements order
         You can enforce the order of the elements on the mosaic. You
         must give a comma-separated list of picture ID(s).These IDs are
         assigned in the "mosaic-bridge" module.

      --mosaic-delay <integer> Delay
         Pictures coming from the mosaic elements will be delayed
         according to this value (in milliseconds). For high values you
         will need to raise caching at input.

      --mosaic-bs, --no-mosaic-bs
         Bluescreen (default disabled)

      This effect, also known as "greenscreen" or
         "chroma key" blends the "blue parts" of the foreground images
         of the mosaic on the background (like wheather forecast
         presenters). You can choose the "key" color for blending (blue
         by default). (default disabled)

      --mosaic-bsu <integer> Bluescreen U value
         "U" value for the bluescreen key color (in YUV values). From 0
         to 255. Defaults to 120 for blue.

      --mosaic-bsv <integer> Bluescreen V value
         "V" value for the bluescreen key color (in YUV values). From 0
         to 255. Defaults to 90 for blue.

      --mosaic-bsut <integer> Bluescreen U tolerance
         Tolerance of the bluescreen blender on color variations for the
         U plane. A value between 10 and 20 seems sensible.

      --mosaic-bsvt <integer> Bluescreen V tolerance
         Tolerance of the bluescreen blender on color variations for the
         V plane. A value between 10 and 20 seems sensible.

   Motion blur filter
      --blur-factor <integer> Blur factor (1-127)
         The degree of blurring from 1 to 127.

   Motion detect video filter
      --motiondetect-history <integer>
         History parameter

      ..

         The umber of frames used for detection.

      --motiondetect-description <string>
         Description file

      ..

         A file containing a simple playlist

   MusePack demuxer
      --mpc-replaygain-type {0 (None), 1 (Title), 2 (Album)}
         Replay Gain type

      Musepack can have a title-specific replay
         gain (volume control) or an album-specific one. Choose which
         type you want to use

   MSN Now-Playing
      --msn-format <string> MSN Title format string
         Format of the string to send to MSN {0} Artist, {1} Title, {2}
         Album. Defaults to "Artist - Title" ({0} - {1}).

   OpenGL video output
      --opengl-effect {none,cube,transparent-cube}
         Effect

      ..

         Several visual OpenGL effects are available.

   On Screen Display menu
      --osdmenu-x <integer> X coordinate
         You can move the OSD menu by left-clicking on it.

      --osdmenu-y <integer> Y coordinate
         You can move the OSD menu by left-clicking on it.

      --osdmenu-position {0 (Center), 1 (Left), 2 (Right), 4 (Top), 8 (Bottom), 5 (Top-Left), 6 (Top-Right), 9 (Bottom-Left), 10 (Bottom-Right)}
         Menu position

      You can enforce the OSD menu position on the
         video (0=center, 1=left, 2=right, 4=top, 8=bottom, you can also
         use combinations of these values, eg. 6 = top-right).

      --osdmenu-file <string> Configuration file
         Configuration file for the OSD Menu

      --osdmenu-file-path <string>
         Path to OSD menu images

      Path to the OSD menu images. This will
         override the path defined in the OSD configuration file.

      --osdmenu-timeout <integer>
         Menu timeout

      OSD menu pictures get a default timeout of 15
         seconds added to their remaining time. This will ensure that
         they are at least the specified time visible.

   Parametric Equalizer
      --param-eq-lowf <float> Low freq (Hz)
         --param-eq-lowgain <float> Low freq gain (Db) --param-eq-highf
         <float> High freq (Hz) --param-eq-highgain <float> High freq
         gain (Db) --param-eq-f1 <float> Freq 1 (Hz) --param-eq-gain1
         <float> Freq 1 gain (Db) --param-eq-q1 <float> Freq 1 Q
         --param-eq-f2 <float> Freq 2 (Hz) --param-eq-gain2 <float> Freq
         2 gain (Db) --param-eq-q2 <float> Freq 2 Q --param-eq-f3
         <float> Freq 3 (Hz) --param-eq-gain3 <float> Freq 3 gain (Db)
         --param-eq-q3 <float> Freq 3 Q

   Playlist
      --playlist-autostart, --no-playlist-autostart
         Auto start (default enabled)

      Automatically start playing the playlist
         content once it's loaded.

   (default enabled)
      --m3u-extvlcopt, --no-m3u-extvlcopt
         Enable parsing of EXTVLCOPT: options (default disabled)

      Enable parsing of EXTVLCOPT: options in m3u
         playlists. This option is default disabled to prevent untrusted
         sources using VLC options without the user's knowledge.
         (default disabled)

      --shoutcast-show-adult, --no-shoutcast-show-adult
         Show shoutcast adult content (default disabled)

      Show NC17 rated video streams when using
         shoutcast video playlists. (default disabled)

   Podcasts
      --podcast-urls <string> Podcast URLs list
         Enter the list of podcasts to retrieve, separated by '|'
         (pipe).

   PORTAUDIO audio output
      --portaudio-device <integer>
         Output device

      ..

         Portaudio identifier for the output device

   DV (Digital Video) demuxer
      --rawdv-hurry-up, --no-rawdv-hurry-up
         Hurry up (default disabled)

      The demuxer will advance timestamps if the
         input can't keep up with the rate. (default disabled)

   Remote control interface
      --rc-quiet, --no-rc-quiet Do not open a DOS command box interface
         (default disabled)

      By default the rc interface plugin will start
         a DOS command box. Enabling the quiet mode will not bring this
         command box but can also be pretty annoying when you want to
         stop VLC and no video window is open. (default disabled)

   RSS and Atom feed display
      --rss-urls <string> Feed URLs
         RSS/Atom feed '|' (pipe) seperated URLs.

      --rss-position {0 (Center), 1 (Left), 2 (Right), 4 (Top), 8 (Bottom), 5 (Top-Left), 6 (Top-Right), 9 (Bottom-Left), 10 (Bottom-Right)}
         Text position

      You can enforce the text position on the
         video (0=center, 1=left, 2=right, 4=top, 8=bottom; you can also
         use combinations of these values, eg 6 = top-right).

      --rss-opacity <integer> Opacity
         Opacity (inverse of transparency) of overlay text. 0 =
         transparent, 255 = totally opaque.

      --rss-color {-268435456 (Default), 0 (Black), 8421504 (Gray), 12632256 (Silver), 16777215 (White), 8388608 (Maroon), 16711680 (Red), 16711935 (Fuchsia), 16776960 (Yellow), 8421376 (Olive), 32768 (Green), 32896 (Teal), 65280 (Lime), 8388736 (Purple), 128 (Navy), 255 (Blue), 65535 (Aqua)}
         Color

      Color of the text that will be rendered on
         the video. This must be an hexadecimal (like HTML colors). The
         first two chars are for red, then green, then blue. #000000 =
         black, #FF0000 = red, #00FF00 = green, #FFFF00 = yellow (red +
         green), #FFFFFF = white

      --rss-size <integer> Font size, pixels
         Font size, in pixels. Default is -1 (use default font size).

      --rss-speed <integer> Speed of feeds
         Speed of the RSS/Atom feeds (bigger is slower).

      --rss-length <integer> Max length
         Maximum number of characters displayed on the screen.

      --rss-ttl <integer> Refresh time
         Number of seconds between each forced refresh of the feeds. 0
         means that the feeds are never updated.

      --rss-images, --no-rss-images
         Feed images (default enabled)

      Display feed images if available. (default
         enabled)

   Shoutcast radio listings

   Skinnable Interface
      --skins2-systray, --no-skins2-systray
         Systray icon (default disabled)

      ..

         Show a systray icon for VLC (default disabled)

      --skins2-taskbar, --no-skins2-taskbar
         Show VLC on the taskbar (default enabled)

      ..

         Show VLC on the taskbar (default enabled)

      --skins2-transparency, --no-skins2-transparency
         Enable transparency effects (default disabled)

      You can disable all transparency effects if
         you want. This is mainly useful when moving windows does not
         behave correctly. (default disabled)

      --skinned-playlist, --no-skinned-playlist
         Enable skinned playlist (default enabled)

      You can choose whether the playlist window is
         rendered using the skin or the default GUI. (default enabled)

   Bridge stream output
      --sout-bridge-out-id <integer>
         ID

      Integer identifier for this elementary
         stream. This will be used to "find" this stream later.

      --sout-bridge-in-delay <integer>
         Delay

      Pictures coming from the picture video
         outputs will be delayed according to this value (in
         milliseconds, should be >= 100 ms). For high values, you will
         need to raise caching values.

      --sout-bridge-in-id-offset <integer>
         ID Offset

      Offset to add to the stream IDs specified in
         bridge_out to obtain the stream IDs bridge_in will register.

   Mosaic bridge stream output
      --sout-mosaic-bridge-id <string>
         ID

      Specify an identifier string for this
         subpicture

      --sout-mosaic-bridge-sar <string>
         Sample aspect ratio

      Sample aspect ratio of the destination (1:1,
         3:4, 2:3).

   RTP stream output
      --sout-rtp-mp4a-latm, --no-sout-rtp-mp4a-latm
         MP4A LATM (default disabled)

      This allows you to stream MPEG4 LATM audio
         streams (see RFC3016). (default disabled)

   Standard stream output
      --sout-standard-access <string>
         Output access method

      This is the output access method that will be
         used.

      --sout-standard-mux <string>
         Output muxer

      ..

         This is the muxer that will be used.

      --sout-standard-dst <string>
         Output destination

      This is the destination (URL) that will be
         used for the stream.

   Transcode stream output
      --sout-transcode-venc <string>
         Video encoder

      This is the video encoder module that will be
         used (and its associated options).

      --sout-transcode-vcodec <string>
         Destination video codec

      ..

         This is the video codec that will be used.

      --sout-transcode-vb <integer>
         Video bitrate

      ..

         Target bitrate of the transcoded video stream.

      --sout-transcode-scale <float>
         Video scaling

      Scale factor to apply to the video while
         transcoding (eg: 0.25)

      --sout-transcode-fps <float>
         Video frame-rate

      ..

         Target output frame rate for the video stream.

      --sout-transcode-hurry-up, --no-sout-transcode-hurry-up
         Hurry up (default enabled)

      The transcoder will drop frames if your CPU
         can't keep up with the encoding rate. (default enabled)

      --sout-transcode-deinterlace, --no-sout-transcode-deinterlace
         Deinterlace video (default disabled)

      Deinterlace the video before encoding.
         (default disabled)

      --sout-transcode-deinterlace-module {deinterlace,ffmpeg-deinterlace}
         Deinterlace module

      ..

         Specify the deinterlace module to use.

      --sout-transcode-vfilter <string>
         Video filter

      Video filters will be applied to the video
         streams (after overlays are applied). You must enter a
         comma-separated list of filters.

      --sout-transcode-canvas-aspect <string>
         Video canvas aspect ratio

      This sets aspect (like 4:3) of the video
         canvas and letterbox the video accordingly.

      --sout-transcode-aenc <string>
         Audio encoder

      This is the audio encoder module that will be
         used (and its associated options).

      --sout-transcode-acodec <string>
         Destination audio codec

      ..

         This is the audio codec that will be used.

      --sout-transcode-ab <integer>
         Audio bitrate

      ..

         Target bitrate of the transcoded audio stream.

      --sout-transcode-channels <integer>
         Audio channels

      Number of audio channels in the transcoded
         streams.

      --sout-transcode-audio-sync, --no-sout-transcode-audio-sync
         Synchronise on audio track (default disabled)

      This option will drop/duplicate video frames
         to synchronise the video track on the audio track. (default
         disabled)

      --sout-transcode-senc <string>
         Subtitles encoder

      This is the subtitles encoder module that
         will be used (and its associated options).

      --sout-transcode-scodec <string>
         Destination subtitles codec

      ..

         This is the subtitles codec that will be used.

      --sout-transcode-soverlay, --no-sout-transcode-soverlay
         Destination subtitles codec (default disabled)

      This is the subtitles codec that will be
         used. (default disabled)

      --sout-transcode-sfilter <string>
         Overlays

      This allows you to add overlays (also known
         as "subpictures" on the transcoded video stream. The
         subpictures produced by the filters will be overlayed directly
         onto the video. You must specify a comma-separated list of
         subpicture modules

      --sout-transcode-osd, --no-sout-transcode-osd
         OSD menu (default disabled)

      Stream the On Screen Display menu (using the
         osdmenu subpicture module). (default disabled)

   Text subtitles decoder
      --subsdec-align {0 (Center), 1 (Left), 2 (Right)}
         Subtitles justification

      ..

         Set the justification of subtitles

      --subsdec-encoding {Default,ASCII,UTF-8,,ISO-8859-1,CP1252,MacRoman,MacIceland,ISO-8859-15,,ISO-8859-2,CP1250,MacCentralEurope,MacCroatian,MacRomania,,ISO-8859-5,CP1251,MacCyrillic,MacUkraine,KOI8-R,KOI8-U,KOI8-RU,,ISO-8859-6,CP1256,MacArabic,,ISO-8859-7,CP1253,MacGreek,,ISO-8859-8,CP1255,MacHebrew,,ISO-8859-9,CP1254,MacTurkish,,ISO-8859-13,CP1257,,ISO-2022-JP,ISO-2022-JP-1,ISO-2022-JP-2,EUC-JP,SHIFT_JIS,,ISO-2022-CN,ISO-2022-CN-EXT,EUC-CN,EUC-TW,BIG5,BIG5-HKSCS,,ISO-2022-KR,EUC-KR,,MacThai,KOI8-T,,ISO-8859-3,ISO-8859-4,ISO-8859-10,ISO-8859-14,ISO-8859-16,,CP850,CP862,CP866,CP874,CP932,CP949,CP950,CP1133,CP1258,,Macintosh,,UTF-7,UTF-16,UTF-16BE,UTF-16LE,UTF-32,UTF-32BE,UTF-32LE,C99,JAVA,UCS-2,UCS-2BE,UCS-2LE,UCS-4,UCS-4BE,UCS-4LE,,HZ,GBK,GB18030,JOHAB,ARMSCII-8,Georgian-Academy,Georgian-PS,TIS-620,MuleLao-1,VISCII,TCVN,HPROMAN8,NEXTSTEP}
         Subtitles text encoding

      ..

         Set the encoding used in text subtitles

      --subsdec-autodetect-utf8, --no-subsdec-autodetect-utf8
         UTF-8 subtitles autodetection (default enabled)

      This enables automatic detection of UTF-8
         encoding within subtitles files. (default enabled)

      --subsdec-formatted, --no-subsdec-formatted
         Formatted Subtitles (default enabled)

      Some subtitle formats allow for text
         formatting. VLC partly implements this, but you can choose to
         disable all formatting. (default enabled)

   Theora video decoder
      --sout-theora-quality <integer>
         Encoding quality

      Enforce a quality between 1 (low) and 10
         (high), instead of specifying a particular bitrate. This will
         produce a VBR stream.

   Time display sub filter
      --time-position {0 (Center), 1 (Left), 2 (Right), 4 (Top), 8 (Bottom), 5 (Top-Left), 6 (Top-Right), 9 (Bottom-Left), 10 (Bottom-Right)}
         Text position

      You can enforce the text position on the
         video (0=center, 1=left, 2=right, 4=top, 8=bottom, you can also
         use combinations of these values, e.g. 6 = top-right).

      --time-opacity <integer> Opacity
         Opacity (inverse of transparency) of overlay text. 0 =
         transparent, 255 = totally opaque.

      --time-color {-268435456 (Default), 0 (Black), 8421504 (Gray), 12632256 (Silver), 16777215 (White), 8388608 (Maroon), 16711680 (Red), 16711935 (Fuchsia), 16776960 (Yellow), 8421376 (Olive), 32768 (Green), 32896 (Teal), 65280 (Lime), 8388736 (Purple), 128 (Navy), 255 (Blue), 65535 (Aqua)}
         Color

      Color of the text that will be rendered on
         the video. This must be an hexadecimal (like HTML colors). The
         first two chars are for red, then green, then blue. #000000 =
         black, #FF0000 = red, #00FF00 = green, #FFFF00 = yellow (red +
         green), #FFFFFF = white

      --time-size <integer> Font size, pixels
         Font size, in pixels. Default is -1 (use default font size).

   Video transformation filter
      --transform-type {90,180,270,hflip,vflip}
         Transform type

      ..

         One of '90', '180', '270', 'hflip' and 'vflip'

   MPEG Transport Stream demuxer
      --ts-dump-file <string> Filename of dump
         Specify a filename where to dump the TS in.

      --ts-dump-append, --no-ts-dump-append
         Append (default disabled)

      If the file exists and this option is
         selected, the existing file will not be overwritten. (default
         disabled)

   Libtwolame audio encoder
      --sout-twolame-quality <float>
         Encoding quality

      Force a specific encoding quality between 0.0
         (high) and 50.0 (low), instead of specifying a particular
         bitrate. This will produce a VBR stream.

      --sout-twolame-mode {0 (Stereo), 1 (Dual mono), 2 (Joint stereo)}
         Stereo mode

      ..

         Handling mode for stereo streams

      --sout-twolame-vbr, --no-sout-twolame-vbr
         VBR mode (default disabled)

      Use Variable BitRate. Default is to use
         Constant BitRate (CBR). (default disabled)

      --sout-twolame-psy <integer>
         Psycho-acoustic model

      ..

         Integer from -1 (no model) to 4.

   Visualizer filter
      --effect-width <integer> Video width
         The width of the effects video window, in pixels.

      --effect-height <integer> Video height
         The height of the effects video window, in pixels.

   Vorbis audio decoder
      --sout-vorbis-quality <integer>
         Encoding quality

      Enforce a quality between 1 (low) and 10
         (high), instead of specifying a particular bitrate. This will
         produce a VBR stream.

      --sout-vorbis-max-bitrate <integer>
         Maximum encoding bitrate

      Maximum bitrate in kbps. This is useful for
         streaming applications.

      --sout-vorbis-min-bitrate <integer>
         Minimum encoding bitrate

      Minimum bitrate in kbps. This is useful for
         encoding for a fixed-size channel.

      --sout-vorbis-cbr, --no-sout-vorbis-cbr
         CBR encoding (default disabled)

      Force a constant bitrate encoding (CBR).
         (default disabled)

   Wall video filter
      --wall-cols <integer> Number of columns
         Number of horizontal windows in which to split the video.

      --wall-rows <integer> Number of rows
         Number of vertical windows in which to split the video.

      --wall-element-aspect <string>
         Element aspect ratio

      Aspect ratio of the individual displays
         building the wall.

   wxWidgets interface module
      --wx-embed, --no-wx-embed Embed video in interface (default enabled)
         Embed the video inside the interface instead of having it in a
         separate window. (default enabled)

      --wx-bookmarks, --no-wx-bookmarks
         Bookmarks dialog (default disabled)

      Show bookmarks dialog at startup (default
         disabled)

      --wx-taskbar, --no-wx-taskbar
         Taskbar (default enabled)

      ..

         Show VLC on the taskbar (default enabled)

      --wx-extended, --no-wx-extended
         Extended GUI (default disabled)

      Show extended GUI (equalizer, image adjust,
         video filters...) at startup (default disabled)

      --wx-playlist-view {0 (Normal), 1 (Embedded), 2 (Both)}
         Playlist view

      There are two possible playlist views in the
         interface : the normal playlist (separate window), or an
         embedded playlist (within the main interface, but with less
         features). You can select which one will be available on the
         toolbar (or both).

      --wx-systray, --no-wx-systray
         Systray icon (default disabled)

      ..

         Show a systray icon for VLC (default disabled)

   H.264/MPEG4 AVC encoder (using x264 library)
      --sout-x264-keyint <integer>
         Maximum GOP size

      Sets maximum interval between
         IDR-frames.Larger values save bits, thus improving quality for
         a given bitrate at the cost of seeking precision.

      --sout-x264-min-keyint <integer>
         Minimum GOP size

      Sets minimum interval between IDR-frames. In
         H.264, I-frames do not necessarily bound a closed GOP because
         it is allowable for a P-frame to be predicted from more frames
         than just the one frame before it (also see reference frame
         option). Therefore, I-frames are not necessarily seekable.
         IDR-frames restrict subsequent P-frames from referring to any
         frame prior to the IDR-frame.

If
   scenecuts appear within this interval, they are still encoded as
   I-frames, but do not start a new GOP.

--sout-x264-scenecut <integer>
   Extra I-frames aggressivity

Scene-cut detection. Controls how
   aggressively to insert extra I-frames. With small values of scenecut,
   the codec often has to force an I-frame when it would exceed keyint.
   Good values of scenecut may find a better location for the I-frame.
   Large values use more I-frames than necessary, thus wasting bits. -1
   disables scene-cut detection, so I-frames are inserted only every
   other keyint frames, which probably leads to ugly encoding artifacts.
   Range 1 to 100.

--sout-x264-bframes <integer>
   B-frames between I and P

Number of consecutive B-frames between I and
   P-frames. Range 1 to 16.

--sout-x264-b-adapt, --no-sout-x264-b-adapt
   Adaptive B-frame decision (default enabled)

Force the specified number of consecutive
   B-frames to be used, except possibly before an I-frame. (default
   enabled)

--sout-x264-b-bias <integer>
   Influence (bias) B-frames usage

Bias the choice to use B-frames. Positive
   values cause more B-frames, negative values cause less B-frames.

--sout-x264-bpyramid, --no-sout-x264-bpyramid
   Keep some B-frames as references (default disabled)

Allows B-frames to be used as references for
   predicting other frames. Keeps the middle of 2+ consecutive B-frames
   as a reference, and reorders frame appropriately. (default disabled)

--sout-x264-cabac, --no-sout-x264-cabac
   CABAC (default enabled)

CABAC (Context-Adaptive Binary Arithmetic
   Coding). Slightly slows down encoding and decoding, but should save
   10 to 15% bitrate. (default enabled)

--sout-x264-ref <integer> Number of reference frames
   Number of previous frames used as predictors. This is effective in
   Anime, but seems to make little difference in live-action source
   material. Some decoders are unable to deal with large frameref
   values. Range 1 to 16.

--sout-x264-nf, --no-sout-x264-nf
   Skip loop filter (default disabled)

Deactivate the deblocking loop filter
   (decreases quality). (default disabled)

--sout-x264-deblock <string>
   Loop filter AlphaC0 and Beta parameters alpha:beta

Loop filter AlphaC0 and Beta parameters.
   Range -6 to 6 for both alpha and beta parameters. -6 means light
   filter, 6 means strong.

--sout-x264-level <string> H.264 level
   Specify H.264 level (as defined by Annex A of the standard). Levels
   are not enforced; it's up to the user to select a level compatible
   with the rest of the encoding options. Range 1 to 5.1 (10 to 51 is
   also allowed).

--sout-x264-interlaced, --no-sout-x264-interlaced
   Interlaced mode (default disabled)

Pure-interlaced mode. (default disabled)
   --sout-x264-qp <integer> Set QP
      This selects the quantizer to use. Lower values result in better
      fidelity, but higher bitrates. 26 is a good default value. Range 0
      (lossless) to 51.

   --sout-x264-crf <integer> Quality-based VBR
      1-pass Quality-based VBR. Range 0 to 51.

   --sout-x264-qpmin <integer>
      Min QP

   Minimum quantizer parameter. 15 to 35 seems
      to be a useful range.

   --sout-x264-qpmax <integer>
      Max QP

   ..

      Maximum quantizer parameter.

   --sout-x264-qpstep <integer>
      Max QP step

   ..

      Max QP step between frames.

   --sout-x264-ratetol <float>
      Average bitrate tolerance

   Allowed variance in average bitrate (in
      kbits/s).

   --sout-x264-vbv-maxrate <integer>
      Max local bitrate

   ..

      Sets a maximum local bitrate (in kbits/s).

   --sout-x264-vbv-bufsize <integer>
      VBV buffer

   Averaging period for the maximum local
      bitrate (in kbits).

   --sout-x264-vbv-init <float>
      Initial VBV buffer occupancy

   Sets the initial buffer occupancy as a
      fraction of the buffer size. Range 0.0 to 1.0.

   --sout-x264-ipratio <float>
      QP factor between I and P

   ..

      QP factor between I and P. Range 1.0 to 2.0.

   --sout-x264-pbratio <float>
      QP factor between P and B

   ..

      QP factor between P and B. Range 1.0 to 2.0.

   --sout-x264-chroma-qp-offset <integer>
      QP difference between chroma and luma

   ..

      QP difference between chroma and luma.

   --sout-x264-qcomp <float> QP curve compression
      QP curve compression. Range 0.0 (CBR) to 1.0 (QCP).

   --sout-x264-cplxblur <float>
      Reduce fluctuations in QP

   This reduces the fluctuations in QP before
      curve compression. Temporally blurs complexity.

   --sout-x264-qblur <float> Reduce fluctuations in QP
      This reduces the fluctations in QP after curve compression.
      Temporally blurs quants.

   --sout-x264-partitions {none,fast,normal,slow,all}
      Partitions to consider

   ..

      Partitions to consider in analyse mode:

- none :
   -  fast : i4x4
   -  

      normal:
         i4x4,p8x8,(i8x8)

   -  

      slow : i4x4,p8x8,(i8x8),b
         8x8

   -  all : i4x4,p8x8,(i8x8),b8x8,p4x4

(p4x
   4 requires p8x8. i8x8 requires 8x8dct).

--sout-x264-direct {none,spatial,temporal,auto}
   Direct MV prediction mode

Direct MV prediction mode.
   --sout-x264-direct-8x8 <integer>
      Direct prediction size

   ..

      Direct prediction size: - 0: 4x4

- 1:
   8x8

- -1: smallest possible according to
   level

--sout-x264-weightb, --no-sout-x264-weightb
   Weighted prediction for B-frames (default disabled)

Weighted prediction for B-frames. (default
   disabled)

--sout-x264-me {dia,hex,umh,esa}
   Integer pixel motion estimation method

Selects the motion estimation algorithm: - dia: diamond search, radius 1 (fast)
   -  

      hex:
         hexagonal search, radius 2

   -  

      umh: uneven
         multi-hexagon search (better but slower)

   -  esa: exhaustive search (extremely slow, primarily for testing)

         --sout-x264-merange <integer>
            Maximum motion vector search range

         Maximum distance to search for motion
            estimation, measured from predicted position(s). Default of
            16 is good for most footage, high motion sequences may
            benefit from settings between 24 and 32. Range 0 to 64.

         --sout-x264-subme <integer>
            Subpixel motion estimation and partition decision quality

         This parameter controls quality versus speed
            tradeoffs involved in the motion estimation decision process
            (lower = quicker and higher = better quality). Range 1 to 7.

         --sout-x264-b-rdo, --no-sout-x264-b-rdo
            RD based mode decision for B-frames (default disabled)

         RD based mode decision for B-frames. This
            requires subme 6 (or higher). (default disabled)

         --sout-x264-mixed-refs, --no-sout-x264-mixed-refs
            Decide references on a per partition basis (default
            disabled)

         Allows each 8x8 or 16x8 partition to
            independently select a reference frame, as opposed to only
            one ref per macroblock. (default disabled)

         --sout-x264-chroma-me, --no-sout-x264-chroma-me
            Chroma in motion estimation (default enabled)

         Chroma ME for subpel and mode decision in
            P-frames. (default enabled)

         --sout-x264-bime, --no-sout-x264-bime
            Jointly optimize both MVs in B-frames (default disabled)

         Joint bidirectional motion refinement.
            (default disabled)

         --sout-x264-8x8dct, --no-sout-x264-8x8dct
            Adaptive spatial transform size (default disabled)

         SATD-based decision for 8x8 transform in
            inter-MBs. (default disabled)

         --sout-x264-trellis <integer>
            Trellis RD quantization

         ..

            Trellis RD quantization:

   -  0: disabled
   -  1: enabled only on the final encode of a MB

         -  2: enabled on all mode decisions

This
   requires CABAC.

--sout-x264-fast-pskip, --no-sout-x264-fast-pskip
   Early SKIP detection on P-frames (default enabled)

Early SKIP detection on P-frames. (default
   enabled)

--sout-x264-dct-decimate, --no-sout-x264-dct-decimate
   Coefficient thresholding on P-frames (default enabled)

Coefficient thresholding on P-frames.Eliminate
   dct blocks containing only a small single

coefficient. (default enabled)
   --sout-x264-nr <integer> Noise reduction
      Dct-domain noise reduction. Adaptive pseudo-deadzone. 10 to 1000
      seems to be a useful range.

   --sout-x264-deadzone-inter <integer>
      Inter luma quantization deadzone

   Set the size of the intra luma quantization
      deadzone. Range 0 to 32.

   --sout-x264-deadzone-intra <integer>
      Intra luma quantization deadzone

   Set the size of the intra luma quantization
      deadzone. Range 0 to 32.

   --sout-x264-asm, --no-sout-x264-asm
      CPU optimizations (default enabled)

   Use assembler CPU optimizations. (default
      enabled)

   --sout-x264-psnr, --no-sout-x264-psnr
      PSNR computation (default disabled)

   Compute and print PSNR stats. This has no
      effect on the actual encoding quality. (default disabled)

   --sout-x264-ssim, --no-sout-x264-ssim
      SSIM computation (default disabled)

   Compute and print SSIM stats. This has no
      effect on the actual encoding quality. (default disabled)

   --sout-x264-quiet, --no-sout-x264-quiet
      Quiet mode (default disabled)

   ..

      Quiet mode. (default disabled)

   --sout-x264-sps-id <integer>
      SPS and PPS id numbers

   Set SPS and PPS id numbers to allow
      concatenating streams with different settings.

   --sout-x264-aud, --no-sout-x264-aud
      Access unit delimiters (default disabled)

   Generate access unit delimiter NAL units.
      (default disabled)

   --sout-x264-verbose, --no-sout-x264-verbose
      Statistics (default disabled)

   ..

      Print stats for each frame. (default disabled)

</nowiki>
