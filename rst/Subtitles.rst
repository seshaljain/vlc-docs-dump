{{See also|Documentation:Subtitles}}

Subtitles are textual retranscriptions of audio tracks

== Different kind of subtitles == '''''1) Burned-in subtitles (or "hard
subs")'''''

Which can be compared to "hot iron cow branding" Now that they're burned
in the image, there is no way to make them disappear properly, as
they're totally part of the image. These burned-in subtitles won't
appear in VLC subtitle menu and there is no way to hide them

'''''2) Soft subtitles'''''

Imagine our movie is a single AVI file. Those "soft" subtitles are
hidden somewhere within the AVI file, but they're not burned in the
image. You may find different languages for these soft subtitles (for
example up to 8 different languages in the same AVI !) Those soft
subtitles will appear in VLC subtitle menu (one menu bar = 1 language)
and you can tick the one you want (or untick all if you don't want to
see any subtitle) At least, you know they are embedded in the movie and
you can make them appear or disappear at your wish.

'''''3) External subtitles'''''

These are external individual files: most usual are .srt files (which
contain only 1 language) or the couple of files .sub + .idx that may
contain up to 32 different languages !)

If you want those external subtitles files to be opened automatically
when you double click a movie in Windows Explorer, then you'll have to
give those external subtitles files the same name that your movie, for
example :

'''Dark Star.avi''' <= the movie file

'''Dark Star.srt''' <= the external subtitle file

If both names match, then VLC will automatically open the subtitle file
and display subtitles, as soon as you double click the movie file name.
This 3rd kind of subtitles (external files) will appear in VLC subtitle
menu, and you can tick /untick them, at your wish.

'''''For more information see
[[What_can_vlc_do#How_to_enable.2Fuse_subtitles|how to enable / use
subtitles]]'''''

== Subtitles formats ==

There are a lot of different types of external subtitle files. Most
contain textual data. That is the subtitle and a [[timestamp]] at which
this subtitles is to be shown. Some of these allow for additional
formatting, others don't.

=== Textual subs === \* [[Kate]] \* [[SubRip]] \* [[SubViewer]] \*
[[SAMI]] \* [[MicroDVD]] \* [[VPlayer]] \* [[SubStation Alpha]] \*
[[JacoSub]] \* [[MPsub]] \* [[Teletext]] \* [[USF]]

=== Pictures-based subs === There are also subtitles which are
essentially pictures instead of text. These kind of subtitles are used
in DVDs, VCDs and the external [[VobSub]] files.

-  [[DVD subtitles]]
-  [[DVB subtitles]]
-  [[VobSub]]
-  [[CVD subtitles]]
-  [[OGT]] and
   [https://web.archive.org/web/20070109161927/http://www.vcdimager.org/pub/vcdimager/manuals/0.7/svcd-ogt-subtitles.html
   SVCD Subtitle (OGT) Information (2007 publication)]

=== File Format/Container embedding subtitles === There are also some
fileformats to which you can add subtitles. These include:

-  [[MOV]]
-  [[MP4]]
-  [[OGM]]
-  [[Matroska]]
-  [[AVI]]
-  [[TS]]

It is not easy to stream subtitles. DVB or DVD subtitles encapsulated in
a TS MPEG stream is your best bet.

== Subtitles support in VLC ==
:''[[wikipedia:mw:Help:Magic_words#Transclusion_modifiers|Transcluded]]
from [[Subtitles codecs]]'' <!-- Editors: This page includes content
from Subtitles codecs. Make edits to this section there. -->
{{:Subtitles codecs}}

== Container format == {{Seeid=subtitle|encoder=n}} The subtitles module
is used to read subtitle text files.

== Source code == {{fileinput demuxer}}

== See also == \*
[http://dvd0101.com/blog/how-to-extract-subtitle-from-dvd.html How to
extract subtitles from DVD]

[[Category:Subtitles|*]]
