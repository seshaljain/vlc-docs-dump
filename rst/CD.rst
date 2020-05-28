{{wikipedia|Compact disc}} A '''CD''' or '''Compact Disc''' is a
circular disk with a silver look to it.
[[File:CD.png%7C100px%7Cthumb%7Calt=%7Cright%7CA CD]]

== Audio CDs == {{protocolinfo=Usage: cdda://\ device@track}}

'''Audio CDs''' contain audio data, and can be read by a CD player. Any
CD marked with the CDDA mark can be played in any player also marked
with a CDDA mark.

Audio CDs can be played with [[VLC media player]] if you have a CD drive on your PC. After inserting the CD, run VLC and select ''Open Disc'' from the ''File'' menu. Then click on the ''Audio CD'' option and press OK. If you prefer, you can use the [[command prompt]] to run an audio CD:
   vlc cdda://D: vlc cdda:///dev/cdrom

Where <code>D:</code> (windows) or <code>/dev/cdrom</code> (Linux) is the location of your CD drive. To play a single track, append <kbd>@</kbd> followed by the track number. For example, to play track 3, type
   vlc cdda://D:@3

Audio CDs contain [[uncompress]]ed [[lossless]] audio, which takes up a
lot of space on the disk but is ''very'' good quality. The format for
this is stereo audio (has both left and right audio channels) in 44100Hz
16-bit [[PCM]] [[WAV]] format.

=== Module options === :''See [[Documentation:Modules/cdda]]''

== Data CDs == '''Data CDs''' contain programs or files which can be
read by your PC&nbsp;&ndash; you can only use these with your PC.

CDs can also contain other data and program code. When you insert a CD
in some versions of [[Windows]], programs on the CD may run without
asking you first&nbsp;&ndash; you may wish to
[https://www.howtogeek.com/236241/how-to-enable-disable-and-customize-autoplay-in-windows-10/
turn off autorun] or hold the <kbd>Shift</kbd> key when inserting a CD
to prevent this from happening.

=== Playing media files on a data CD === You can play files from a data
CD, in exactly the same way as playing them from your hard drive (note:
Linux users will need to [[wikipedia:Mount (computing)|mount]] the CD
drive first).

See the [[file]] access module for details of playing files from your
computer.

== CDs with both audio and data (Mixed CDs) == '''Mixed CDs''' contain
both audio and data, for example a CD may come with a music video as a
"bonus feature". The data part (such as the music video) can only be
used on your PC, but the audio is able to be played on your PC or CD
player.

Some mixed CDs come with programs which will try to install [[copy
protection]] on your computer&nbsp;&ndash; see [[wikipedia:2005 Sony BMG
CD copy protection scandal|2005 Sony BMG CD copy protection scandal]].

To play the audio CD part, follow the [[#Audio CDsinstructions for a
data CD]].

==See also== \* [[CD]] \* [[DVD]] \* [[VCD]]/SVCD <hr style="width:8em;"
/> \* [[FLAC]] \* [[wikipedia:ISO image]]: an obscure format that can
store e.g. an operating system on a disc

== Source code == {{fileaccess module}}

[[Category:Physical media]]
