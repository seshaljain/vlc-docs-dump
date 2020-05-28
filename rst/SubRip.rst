{{Muxmod=subtitle}} {{Wikipedia|SubRip}}

'''SubRip''' is the native subtitle format of the [http://zuggy.wz.cz/
SubRip program], developed by a friend of the creator of [[SubViewer]].
It is one of the most used formats for [[subtitles]].

It may have the [[file extension]] <code>.srt</code>. It can be embedded
in [[Matroska|mkv]] files.

== Specification == === Format === Each frame of a subtitle is formatted
as follows: <!--Begin format code--> <var>n</var> h1:m1:s1,d1 -->
h2:m2:s2,d2 Line 1 Line 2 &hellip;

<!--End format code--> Note the last line is a blank line between
subtitle frames, and the decimal separator is a comma (per
French-style).

;<var>n</var> :sequential number. This may also appear on the same line
as start/stop times ;<nowiki>h1:m1:s1,d1</nowiki> :start time of this
frame, in hours minutes and seconds to three decimal places
;<nowiki>h2:m2:s2,d2</nowiki> :stop time

==== Example ==== A 2-frame subtitle: <!--Begin example code--> 1
00:00:20,000 --> 00:00:24,400 a bla bla ble a bla bla ble a bla bla ble

   2 00:00:24,600 --> 00:00:27,800 a bla bla ble&hellip;

<!--End example code-->

=== Extensions === Some subtitles feature html tags inside the SubRip
text: \* {{Tag pairs}}: strikethrough \* {{Tag pairi}}: italic \*
<code><nowiki>&lt;font color=&hellip; face=&hellip;&gt;</nowiki></code>:
font attributes

== See also == \* [[SongSubtitles.org]] (now defunct)

[[Category:Subtitles]]
