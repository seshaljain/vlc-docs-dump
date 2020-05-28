{{RightMenu|Documentation TOC}}

Miscellaneous other [[Uncommon uses|cool things]] you can do with VLC.

== Snapshot Tool ==

Did you know you can use [[Documentation:Format String|special codes]]
to automatically generate filenames in the [[Snapshot Tool]]?

== Audio Bar Graph over Video ==

This section specifies how to enable the audiobargraph audio filter and
video overlay, (mostly) via the {{GUI}}. This displays an audio meter
overlaid on the video.

There are three parts: '''an audio filter''', which sends its output via
TCP to the '''Remote Control''' ([[RC]]) Interface. This information is
then picked up and displayed by the '''Audio Bar Graph video subpicture
filter''' (OSD).

To enable this, VLC needs to be started with the '''<code>--rc-host</code>''' command-line switch e.g.
   {{Prompt|cmd}} "%PROGRAMFILES%VideoLANVLCvlc.exe" --rc-host
   localhost:12345

In the {{GUI}}, set the following (this example from VLC v1.1.9 on
Windows 7): \* Preferences:Show settings:All \* '''Audio → Filters'''
Enable "Audio part of the BarGraph function" \* '''Audio → Filters →
Audiobar Graph''' Use defaults, change "Sends the barGraph information
every n audio packets" to 1 to enable viewing a more accurate display \*
'''Interface → Main interfaces''' Enable "Remote control interface" \*
--'''Interface → Main interfaces → RC''' Enable "Do not open a DOS
command box interface"{{Check|for=Check this &mdash; outdated ?}} \*
'''Video → Subtitles-OSD''' Enable "Audio Bar Graph Video sub filter" \*
'''Video → Subtitles-OSD → Audio Bar Graph''' Set the following
settings: \*\* '''Value of the audio channels levels = 0''' (setting
this to 0:1 crashes VLC v1.1.9) \*\* '''X coordinate = 0''' \*\* '''Y
coordinate = 0''' (this doesn't seem to affect anything) \*\*
'''Transparency of the bargraph = 128''' for 50% transparency which
looks ok \*\* '''Bargraph position = Left''' (seems to only work
Left,Center,Right&mdash;can't go top or bottom) \*\* '''Alarm = 1'''
(enables the silence alarm: puts a red border around the bargraph if
silent for too long) \*\* '''Bar width in pixel = 10''' (20 if you want
it to be really visible)

== How to show album art ==

# Close the VLC media player. # Open the config file (Windows:
<code>"%APPDATA%vlcvlcrc"</code>) with your preferred text editor. #
Search for: <pre>#metadata-network-access=0</pre> # Delete the leading
hash sign and change '''<code>0</code>''' to '''<code>1</code>'''. #
Save the file. # Open a MP3- or a M3U-File in a folder there a file like
Folder.jpg, AlbumArtSmall.jpg, AlbumArt.jpg, Album.jpg, .folder.png,
cover.jpg or thumb.jpg exists. The player should show the album art.

If you have none of the files above but any other file you can put this
filename in [[vlcrc]]. Search for '''<code>album-art-filename</code>'''.

{{Documentation}} [[Category:Stubs]]
