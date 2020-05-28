{{See alsotranscode awkward file types}} This tutorial will walk you
through converting certain kinds of Windows Media audio/video files to a
more useful format such as a [[Quicktime]] or [[MPEG-4]]. It is aimed at
a particular problem: making usable the .[[ASF]] [[WMV]]/MS files
produced by a (terrible) Mustek "DV" camera. We assume that the reader
knows the [[Documentation:Play_HowTo/Basic_Use|basics]] of VLC.

-  Launch VLC
-  From the File menu, select '''File > Open File''' (Apple + Shift + O
   ("oh"))

'''The Open Source window'''

:\* In the Open Source window which opens, click Browse, find the file
you want to convert and click Open. Check the Advanced Output checkbox
and click the Settings button. Try the following settings first. (If
they don't work, experiment. Work by process of elimination — keep notes
on [[codec]]s you've tried.)

'''The Advanced Settings sheet'''

:\* In the Output Options section, leave "Play locally" unchecked. :\*
Select File and click Browse. Choose a name and location to save your
file. (We recommend making a new folder called "converted" to keep your
videos organized, which is especially useful if you need to re-convert
some files with different settings.) Add the extension .mov if you're
making a Quicktime or .mp4 if you're making an MPEG-4. :\* From the
Encapsulation method dropdown box, choose Quicktime or MPEG-4. :\* In
the [[Transcode]] options section, check Video and select "mp4v" from
the dropdown box. For videos taken with the Mustek "DV" cameras, set the
[[Bitrate]] to 768.

'''Note:''' If you are planning to use this video in a VJ program on a
not-so-powerful computer and the original video size is 640 by 480, set
Scale to 0.5 to shrink it down to 320 by 240. Your VJ program will run
faster. :\* Leave the Audio checkbox unchecked. At the time of this
writing, VLC can't transcode from the "MS Audio" codec. Yes, that's "MS"
as in "Micro$oft". :-X :\* Click the OK button (ignore the Stream
Announcing section). \* Back in the Open Source window, click the OK
button to start the transcoding.

VLC will start transcoding the file immediately. The video will not play
in a window because we left "Play locally" unchecked. If we had, our
conversion time would be limited to 1:1, i.e., realtime. We have better
things to do with our time than watch these videos while they're
converting.

'''Note:''' An Error window may pop up to tell you something highly
technical. If, when the transcoding is done, you can play the file in
Quicktime, then you can safely ignore the Error window. If not, go back
to step one and experiment. If you fail entirely, make a note of the
error message and ask for help.

To this author's knowledge, VLC cannot currently batch process a group
of files, i.e., do them all at once automatically. You're going to have
to repeat the steps above manually.
