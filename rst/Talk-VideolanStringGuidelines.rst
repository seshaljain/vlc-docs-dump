== Target / Item == When refering to playlist items, some of the current
strings use "target" (like "Plays the next target in the playlist"), and
some use "item" (like "Go to next item in the playlist"). Which one
should we use (for consistency's sake)? I put my vote for 'item' as it
seems more sensical. --[[User:Tonsofpcs|tonsofpcs]] 07:45, 2 April 2006
(CEST)

: item [[User:J-b|jb]] 00:34, 4 January 2012 (UTC)

Another example: demux vs. demuxer vs. demultiplexer : demuxer
[[User:J-b|jb]] 00:34, 4 January 2012 (UTC)

mux vs. muxer vs. multiplexer : muxer [[User:J-b|jb]] 00:34, 4 January
2012 (UTC)

Or ending with -plexing

Is this referring to the same thing? If so, I would like to have the
same words:

"Playback Rate"

"Playback speed"

"Revert to normal play speed" : it should be speed [[User:J-b|jb]]

Another candidate: <br> modules/access/jack.c:61 <br> "Read the audio
stream at VLC pace rather than Jack pace."

[[User:No se|No se]] 09:38, 4 January 2012 (UTC)

== similar but different... == ... strings were mentioned by somebody.
So I had a look at the pot-file. Note: I did '''not''' check this in a
running vlc, nor do I have that much experience in this field (giving
advices how to translate software, or prepare for translation). So feel
free to comment, state other points of view, or simply say that some
points are wrong.

The best example so far: src/libvlc-module.c:875 - 899 quoted for
possible changes:

   /\* DVD and VCD devices \*/ #define DVD_DEV_TEXT `N <>`__\ ("DVD
   device") #define VCD_DEV_TEXT `N <>`__\ ("VCD device") #define
   CDAUDIO_DEV_TEXT `N <>`__\ ("Audio CD device")

   #if defined( WIN32 ) \|\| defined( \__OS2_\_ ) # define
   DVD_DEV_LONGTEXT `N <>`__\ ( "This is the default DVD drive (or file)
   to use. Don't forget the colon " "after the drive letter (e.g. D:)")
   # define VCD_DEV_LONGTEXT `N <>`__\ ( "This is the default VCD drive
   (or file) to use. Don't forget the colon " "after the drive letter
   (e.g. D:)") # define CDAUDIO_DEV_LONGTEXT `N <>`__\ ( "This is the
   default Audio CD drive (or file) to use. Don't forget the " "colon
   after the drive letter (e.g. D:)") # define DVD_DEVICE NULL # define
   CD_DEVICE "D:"

   #else # define DVD_DEV_LONGTEXT `N <>`__\ ( "This is the default DVD
   device to use.") # define VCD_DEV_LONGTEXT `N <>`__\ ( "This is the
   default VCD device to use." ) # define CDAUDIO_DEV_LONGTEXT
   `N <>`__\ ( "This is the default Audio CD device to use." )

I would suggest a split. Don't think splitting a sentence in more than 3 parts makes sense. Would be even more difficult to build a sentence around a string, because the translators won't even notice that this are parts of the same line. This is my suggestion:
   "This is the default drive (or file) to use. Don't forget the colon
   after the drive letter (e.g. D:)"

respectivly
   "This is the default device to use."

And the short form in the line above. Or in the same line right in
front. Should give something like:

   Audio CD device This is the default device to use.

OR
   Audio CD device: This is the default device to use.

: Disagree. We should just merge this option into one [[User:J-b|jb]]
00:34, 4 January 2012 (UTC)

modules/access/dshow/dshow.cpp:191 This part is used for audio and
video. Could possibly be split, too. Caution: Sentence in line 188 uses
audio and video. Don't know, if this is intentional. : It is normal
[[User:J-b|jb]] 00:34, 4 January 2012 (UTC)

modules/video_filter/panoramix.c:117 and following lines.

src/libvlc-module.c:1213 Previous string is used again with an appended
extra sentence.

== Listing up the choices of a select box == If there is a select box, I
don't see any use in listing the possible choices in a string next to
it. An example is fine, some special hints or a link to
faq/wiki/whatever...

Opening the pot-file and search for ", " (the end of one element, a comma, a space and the beginning of the next element) will give you what I found, too:
   ", "

modules/demux/subtitle.c:56 : will fix [[User:J-b|jb]] 00:34, 4 January
2012 (UTC)

modules/access/dshow/dshow.cpp:172 : will fix [[User:J-b|jb]] 00:34, 4
January 2012 (UTC)

modules/audio_output/file.c:81 : done [[User:J-b|jb]] 00:34, 4 January
2012 (UTC)

Just make sure there really is a select box. If the strings are
displayed elsewhere, they might be of use.

Another way to find interesting parts of the translation:
   vlc -H \| grep "1="

Additionally you will find several "position on the video" which is
another example of similar but different.

On vlc 1.1.13: <br> settings->all->audio->visualizers->visualizer will
show an effects list like modules/visualization/visual/visual.c:44 Does
selecting one here have any effect at all?

When looking at <br> settings->all->audio->filter or <br>
settings->all->video->filter <br> You get a list of filters to apply.
What is the reason for this strings being different from those to the
left?

[[User:No se|No se]] 09:51, 3 January 2012 (UTC)

== Binary variables/flags == Those are fine for translation normally.
With the right text (look at the guidelines here).

modules/audio_filter/audiobargraph_a.c:48 and following lines show several integers instead. I would prefer simple checkboxes.
   "Defines if BarGraph information should be sent (default 1)"

Would become:
   "Send BarGraph information" or similar.

Possibly something similar: modules/video_filter/rss.c:167

[[User:No se|No se]] 15:21, 2 January 2012 (UTC)

== possible typos ==

modules/gui/qt4/dialogs/openurl.cpp:66

"Please enter the URL or path to the media you want to play"

Looks like a complete sentence but misses a period. : will fix
[[User:J-b|jb]] 00:34, 4 January 2012 (UTC)

Missing a space after the period: <br>
modules/audio_filter/audiobargraph_a.c:41 <br>
modules/audio_filter/audiobargraph_a.c:45 <br> : will fix
[[User:J-b|jb]] 00:34, 4 January 2012 (UTC)

What shall be the correct spelling for barGraph vs. BarGraph? <br>

share/lua/http/index.html:274 <br> "Are you sure you wish to create the
stream ?" <br> share/lua/http/mobile_equalizer.html:62 <br> "Preamp: "
<br>

Both may have a not needed space.

[[User:No se|No se]] 14:04, 2 January 2012 (UTC)

== Colon at the end of strings? ==

share/lua/http/dialogs/mosaic_window.html:96 and following lines is an
example. I did not find this messages while running vlc so far.

Is there a general policy whether/when strings should end with a colon?
This will not really bother translators, it's more "for consistency's
sake" (and a bit for "similar but different"). I won't suggest simply
moving the colon at the end to an untranslated colon behind it, since it
may lead to sentences ending in ".:" or similar. On the other hand, I
won't expect translators to put a colon after a single word, if there
isn't a colon in the original string. Complete sentences shall end with
a period anyway (colon will work, too), so using them won't bother me,
either.

== Source is ASCII only - unlike the translation ==

The source is ASCII only (is it?)
[http://www.gnu.org/software/gettext/FAQ.html#nonascii_strings]. The
translation is not restricted that way. So you can use for example …
(ellipsis) instead of ... (three period characters) or locale-dependent
quotes.

== 2.1.0 Rincewind TODO ==

There are several strings differing only in capitalization. But before
deciding the capitalization for each of them, check spelling (one
word/two words).

   msgmerge -v --sort-output emptydummyfile.po vlc.pot > sortedlist.po

Gave a start for finding them.

Typos/spelling:

   "Audio visualizations "

It ends in space.

   Blu-Ray/BluRay

Blu-Ray is a registered trademark; bluray is not; We don't want to use
trademarks.

   Force the DirectShow video input to use a specific frame rate(eg. 0
   means default, 25, 29.97, 50, 59.94, etc.)

and
   Force skipping of idct to speed up decoding for frame types(-1=None,
   0=Default, 1=B-frames, 2=P-frames, 3=B+P frames, 4=all frames).

Missing a space before "("

   Psychadelic/Psychedelic

"Psychadelic is just wrong"

   Network synchronisation/Network synchronization

synchronisation is also a correct spelling; less common in the US, but
still correct in the rest of the world

   Playlist is currently Empty

I will make it empty

   Audiobar Graph

This one is different for "Audio Bar Graph Video" will not match
completely. Just ignore it, like I will.

Those are easy, and I can provide a patch (or several if preferred) of
course.

The next 2 decisions affect the big Capitalization problem

   Aspect-ratio/Aspect ratio/Aspect Ratio

   bitrate/bit rate/Bit rate/Bit Rate (also: aAudio bBit rRate)

could be both; So I want it to be bitrate

[[User:No se|No se]] 07:59, 3 July 2012 (CEST)

== Capitalization. It's possible that keeping both version is
reasonable, but for some cases we could kill one. ==

   Add to playlist Add to Playlist

   Advanced options Advanced Options

   Aspect Ratio Aspect ratio Aspect-ratio

   Audio bitrate Audio Bit Rate

Audio \* There are several example like this: Audio d/Device or Audio
s/Settings

   Bit rate Bitrate

   Brightness Threshold Brightness threshold

   Broadcast: Broadcast

   File Name Filename

   Font Size Font size

   Frames per Second Frames per Second: Frames per second

   General Audio Settings General audio settings

   General Video Settings General video settings

   Go to Time Go to time

   HTML Playlist HTML playlist

"HTML Playlist" → "HTML playlist"

modules/gui/macosx/playlist.m:562 [o_save_accessory_popup itemAtIndex:2]
setTitle

   Hot keys Hotkeys

"Hot keys" → Hotkeys

   Image Adjust Image adjust

"Image [A/a]djust" sounds wrong to me

   Input & Codec settings Input & Codecs Settings

   Jump To Time Jump to time

   Maximal bitrate Maximum bitrate

"Maximal bitrate" → "Maximum bitrate"

   #: modules/gui/qt4/components/controller_widget.cpp:145 msgctxt
   "Tooltip|Mute" msgid "Mute"

The other occurencies of "Mute" don't have msgctxt

   Outline Color Outline color

   Outline Thickness Outline thickness

   Output File Output file

   Playback Speed Playback speed

   Post processing quality Post-Processing Quality

"Post processing quality" → Post-processing quality

   Refresh List Refresh list

   Repeat All Repeat all

"Repeat All" → "Repeat all" Several occurencies, to be checked

   SAP Announce SAP announce

   Save Playlist Save playlist

   Step Backward Step backward

   Step Forward Step forward

   Stream Name Stream name

   Stream Output Stream output

   Subtitles Track Subtitles track

   Track Synchronisation Track Synchronization

   User name Username

   Video Bit Rate Video bitrate

   Video Device Video device

   Video Settings Video settings

   Volume Down Volume down

   Volume Up Volume up

[[User:No se|No se]] 16:31, 2 July 2012 (CEST)
