{{Howto|merge and transcode multiple videos with a script}} ==Merge &
Transcode==

If you have more than one source files that need to be merged into a
single output file, the general way is this (no transcoding is necessary
if all streams match):

   {{Promptwindows}} file1.ps file2.ps file3.ps --sout
   "#[[Documentation:Modules/gather|gather]]:std{access=file,mux=ts,dst=all.ts}"
   --no-sout-all --sout-keep'''

NB that whenever you use sout, your video and audio codecs must "be
appropriate" for the mux you use (in this case, ps works with a ts mux,
so we're ok). See [[Transcode#Transcoding_with_the_Wizard]]

If you want to write your files out to a mux that doesn't support the
current audio or video encoding, or if you are wanting to join streams
that do not have matching video/audio, then it is recommended to
transcode as well. Here is an example.

   {{Promptwindows}} -vv FILE1.EXT FILE2.EXT FILE3.EXT ETC.ETC
   --sout-keep
   --sout=#gather:transcode{vcodec=h264,vb=1024,scale=1,acodec=mp4a,ab=192,channels=6}:standard{access=file,mux=ts,dst=out.mpg}'''

   {{Promptwindows}} -vv FILE1.mp3 FILE2.mp3 FILE3.mp3 ETC.ETC
   --sout-keep
   --sout=#gather:transcode{acodec=mp3,ab=128}:standard{access=file,mux=dummy,dst=out.mp3}'''

Next edit the path to vlc, input files, and transcode parameters to meet
your needs.

For Example in Windows (all input files are in the same directory from where the command is executed):
   {{Promptwindows}} -vv FILE1.mp3 FILE2.mp3 FILE3.mp3 --sout-keep
   --sout=#gather:transcode{acodec=mp3,ab=128}:standard{access=file,mux=dummy,dst=combinedout.mp3}'''

Or you can use file appending:

   {{Promptwindows}} go.ps.1 go.ps.2 go.ps.3 vlc://quit --no-sout-all
   --sout-file-append --sout=file/ps:go.ps'''

==Non Interactive Mode==

To do any of this in "non interactive" mode, add '''-I dummy''' and also
"vlc://quit" to the end of your list of inputs. See [[Transcode]] for
more detail.

==Other options==

Overall, none of the ways VLC offers to combine streams appears to merge
them with correct time signatures<ref> even when replayed in VLC
(causing seeking errors), so a non VLC option might work better. Please
update if you find one. Straight concatenation works at times. See also
https://spreadsheets.google.com/ccc?key=0AjWmZ0umsuZHdHNzZVhuMTkxTHdYbUdCQzF3cE51Snc&hl=en
for a list of several various 3rd party "video joining" utilities.
