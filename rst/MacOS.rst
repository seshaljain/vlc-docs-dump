{{Lowercase}} <div style="width:820px;border: 1px solid #ffc9c9>
{{vlc_MacOS_toc}} <div style="padding: .4em .9em .9em">

== Graphical Interface ==

Many people who want to use [[VLC media player]] on macOS will be
intending to use the standard graphical interface that is provided by
VLC. The standard interface consists of the eight menus in the menu bar
and the 'VLC - Controller' window that opens up by default. This section
outlines what VLC can do for you (at V0.8.6a current active is
V{{VLC:latest version}}) and will be completed as I check the use of
menu options.

The ten menu bar options are listed below along with the main
interesting capabilities under each menu item:

-  [[vlc_MacOS_VLC|VLC]] which allows you to check for an updated
   application, to access the preferences, and to add an interface.
-  [[vlc_MacOS_File|File]] which allows you to open a media file, or an
   associated file (such as subtitles). It also has a wizard to allow
   the streaming of video, or the capturing of a streamed video to a
   file.
-  [[vlc_MacOS_Edit|Edit]] which does nothing VLC-specific.
-  [[vlc_MacOS_View|View]] which allows you to hide or show various
   options like previous/next buttons, shuffle and repeat, audio
   effects, sidebar, as well as customize what you see in 'playlist
   table columns'.
-  [[vlc_MacOS_Playback|Playback]] allows you do do all the things you
   might expect from a video player; some of these features are
   duplicated graphically in the 'Controller' window.
-  [[vlc_MacOS_Audio|Audio]] allows you to control the audio level, as
   well as the output device and the audio track to use from the input.
-  [[vlc_MacOS_Video|Video]] allows you to control the video display on
   your screen, as well as which device to display on, and which video
   source to show in that display.
-  [[vlc_MacOS_Subtitles|Subtitles]] allows you to add subtitle files to
   your video, as well as change the appearance of subtitle text for
   your video.
-  [[vlc_MacOS_Window|Window]] allows you to display seven helper
   windows that will display information about VLC's activity, and
   control more detail of that activity.
-  [[vlc_MacOS_Help|Help]] gives access to the help that came with the
   installation, the help info on the VideoLAN site, and access to
   interaction mechanisms with the VLC developers.

In general, many users find that they can get what they want from VLC
"straight out of the box", and may only want more advanced controls
after becoming familiar with the regular interface.

== Keyboard Shortcuts ==

You can find most of the keyboard shortcuts by taking a look at the
menus. Additional hotkeys are defined in the section "Hotkeys" of your
VLC preferences.

Some handy key combos are:

-  Spacebar – pause/unpause the video
-  {{Apple key}} + F – toggle fullscreen (Escape will also exit
   fullscreen)
-  {{Apple key}} + Shift + left/right arrow keys – jump the video
   back/forward about a minute
-  {{Apple key}} + Ctrl + left/right arrow keys – jump the video
   back/forward about ten seconds
-  When watching a DVD, and the video window is the front-most window,
   arrow keys and the enter key will allow you to navigate the DVD menus
-  F key – Decrease Audio Delay in milliseconds
-  G key – Increase Audio Delay in milliseconds
-  H key – Decrease Subtitle Delay
-  J key – Increase Subtitle Delay

== Latest developments == === Streaming Wizard ===

A streaming wizard has been available since the VLC media player 0.8.4
release. This is available under the "File" menu.

=== Command line ===

You can run VLC on macOS using a terminal application (for example Terminal.app in /Applications/Utilities) with the following command:
   {{$}} {{Path to VLC|mac}} [your options, "--intf=rc" for example]

On most Bourne-like shells, you can set an alias to just vlc with the following command:
   {{$}} alias vlc='{{Path to VLC|mac}}'

It can be helpful to add this command to your shell setup file.

This option can also be activated from the "VLC" menu.

==== Command line examples ==== <kbd>~</kbd> will expand to
<samp>/Users/&lt;username&gt;</samp>

Following command does this: Transform video-filter (flip vertically),
transcode (save) to file.

   {{$}} {{Path to VLC|mac}} -I rc --vout-filter=transform
   --transform-type=vflip /Movie.mov
   --sout='#transcode{vcodec=h264,vb=800,scale=1,acodec=mp4a,ab=128,channels=2,samplerate=44100}:std{access=file,mux=ts,dst=/output.mp4}

-I rc is so that it doesn't open the GUI, but stays on the command line
version --vout-filter defines the filter to use --transform-type defines
the attributes of the transform filter /Movie.mov is the file to convert
--sout= is the stream output chain /output.mp4 is the output file name

==== Another Example ====

I had a heck of a time getting this to work the way I wanted it. I kept attempting a command-line execution of VLC to only get the following response (not what I wanted):
   VLC media player 2.0.2 Twoflower (revision 2.0.2-9-gd1b4a63)
   [0x100283cd0] [cli] lua interface: Listening on host "*console". VLC
   media player 2.0.2 Twoflower Command Line Interface initialized. Type
   \`help' for help.

What I wasn't doing apparently was specifying the location of the source
movie.

Eventually I ran this:

   {{$}} vlc ~/Desktop/my_movie.mp4 --intf=rc --sout
   "#transcode{vcodec=VP80,vb=800,scale=1,acodec=vorbis,ab=128,channels=2}:std{access=file,mux="ffmpeg{mux=webm}",dst=my_first_transcoded_movie.webm}"

'''HINT''':<br> This would be the same as if you didn't have an alias
for vlc that pointed to the actual Applications executable:

   {{$}} {{Path to VLC|mac}} ~/Desktop/mymovie.mp4 --intf=rc --sout
   "#transcode{vcodec=VP80,vb=800,scale=1,acodec=vorbis,ab=128,channels=2}:std{access=file,mux="ffmpeg{mux=webm}",dst=my_first_transcoded_movie.webm}"

Hopefully, I'll add to this post when the transcoding finishes and I see
my results (I have no idea if I've got the correct options for
vp8/vorbis webm-container transcoding).....

=== <span id="clivlc"></span> No Dock ===

In previous versions you can replace the <code>VLC</code> at the end of
the path with <code>clivlc</code> to suppress the launch of any Mac-like
interface (VLC wouldn't even appear in the Dock then) or if
[[transcoding]] from the command-line crashed with a <samp>Bus
error</samp>.

'''This does not work anymore''' (see {{forumlabel=Forum thread
#58378}})

As given by [[Command-line interface#macOS]], specify the option
<code>-I</code> followed by the interface you want to add e.g. <code>VLC
-Idummy</code>.

== Need Help? ==

See the [[macOSFAQ|FAQ on macOS only issues]] or the [[Common Problems]]
pages.

</div> </div>

[[Category:macOS|*]] <!-- This page will be in this category already;
this modifies the sortkey -->
