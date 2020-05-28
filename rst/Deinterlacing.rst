[[`File:VLC <>`__-_Deinterlace_action_options.pngthumbdeinterlace switch
menu]]

'''Deinterlacing''' is the process of converting source material that
contains alternating half-pictures to a computer screen that displays a
full picture at a time. This is a fundamentally impossible process that
must always produce some image degradation, since it ideally requires
"temporal interpolation" which involves guessing the movement of every
object in the image and applying motion correction to every object.

== Description == Traditional TVs do not display one picture-frame at a
time. Instead, they display alternately all the odd lines and all the
even lines of the picture. That way, they can get a fast display rate of
50 or 60 half-pictures per second, without the bandwidth requirements
that full pictures have.

Computers however, do display full pictures, typically at a rate of at
least 60 pictures per second. So to get optimum quality when displaying
TV-material (such as DVDs) on a computer, the player can convert the
alternating half-pictures to full pictures. That is called
''deinterlacing''.

Modern HDTVs operate much like computers in that they display full
pictures. Much like computer-based video players, they have
deinterlacing built in so that they can display traditional TV material.

A very good description of the problem and the various ways of
deinterlacing can be found at [http://www.100fps.com/ 100fps.com].

== VLC settings == {{VLC}} has deinterlacing off by default.

You can enable it for the currently playing video by using the main
menus, the right-click menus or by using [[hotkey]] (by default:
'''D'''). It switches deinterlacing on and off (using the mode selected
in the [[Preferences]]).

To change the settings, go to the Video section in the Simple
Preferences. You can choose from On, Automatic or Off. This setting
controls whether VLC enables deinterlacing when you open a video. You
can also choose the mode (algorithm). See below for available modes and
mode recommendations.

In the mode ''Automatic'', VLC will check the stream flags (technical
term for information embedded in the video) and automatically set
deinterlacing on or off, depending on if the current video is marked as
interlaced even in animated movies on DVDs. However, the detection is
not always reliable. If the setting is ''On'', VLC will apply
deinterlacing even if the original is not interlaced (which is a really
bad idea). The setting ''Off'', respectively, always keeps deinterlacing
off.

The most reliable choice is to switch deinterlacing on/off manually when
needed.

'''For advanced users'''

In All Preferences, the settings for deinterlacing can be found in
Preferences > Video > Filters > Deinterlace. The available settings are
the mode (algorithm), and in v1.2.0+ also some algorithm-specific
settings.

Note that if you enable deinterlacing from the menu, the setting will
only take effect for the currently playing video. When the video ends,
both the on/off/automatic and the mode settings will return to the
values set in the preferences. If you want to always enable
deinterlacing on every video, type "Deinterlace" in the Video Filter
preferences.

The keyboard shortcut to switch deinterlacing on and off can be
configured in the [[Hotkeys]] section of the Simple Preferences. Its
name is ''Cycle deinterlace modes''.

If you use VLC from the command line, you can also set the deinterlace
options in your command. To get a list and short description of the
available options, run <pre>vlc -p deinterlace --advanced</pre> Note
that the deinterlace command-line options are prefixed by "sout" for
historical reasons only; they are intended for normal playback use. For
more information on using VLC from the command line, see [[VLC
command-line help]].

'''Technical detail about Automatic mode'''

The version control history (git log) says the following about the
''Automatic'' mode (see
{{Commitdiff|f96b075043c421fb6466829a15ae0c8792b8ffe8}}):

''The detection is based on the progressive/interlaced flags transported
at the codec level. As such, it is not really reliable (for 25fps at
least).''

''As soon as a picture is detected as interlaced, the configured
deinterlace mode is applied. After 30s of progressive video, the filter
is removed. The hysteresis helps with unreliable interlaced flags.''

== Interlaced or telecined? == In addition to true interlaced signals,
there exists also a process called ''telecine'' which produces
interlacing. It is a type of artificial interlacing that may be added to
sources that were originally progressive. Telecine produces a
characteristic look, with a repeating sequence of 3 progressive frames
followed by 2 artificially interlaced frames.

Why would anyone want to do that? The answer lies in different
[[framerate]]s, and in transfer of film sources to television and video.
Film is commonly shot at 24 pictures per second, while NTSC television
and video equipment operates at 60 half-pictures per second. Telecine
inserts extra half-pictures so that films can be stored in the NTSC
format (for example on DVDs in Japan and USA).

For more on telecine, see for example the following links:
*[//en.wikipedia.org/wiki/Telecine Telecine (in
Wikipedia)]*\ [http://arbor.ee.ntu.edu.tw/~jackeikuo/dvd2avi/ivtc/
Inverse Telecine] *[http://neuron2.net/LVG/telecining1.html NTSC
Telecine - Luke's Video
Guide]*\ [http://users.softlab.ece.ntua.gr/~ttsiod/ivtc.html NTSC,
telecine, and how to cope (using telecide and decimate)]

== <span id="types"></span> Which type of interlacing do I have? == This
depends on the format (PAL, NTSC) and the content of the source. PAL is
used in Europe and Australia, NTSC in USA and Japan. This also applies
to the DVDs produced in those regions.

Live-action movies in the PAL format typically are not interlaced at
all. This is because it is easier to transfer film to PAL than to NTSC.

Home movies shot on a camcorder are typically true interlaced.

Telecine is very common in Asia and especially in Japan. Anything
originating in Asia is likely to be telecined. For example, with very
few exceptions, all anime in the NTSC format is telecined. This includes
the corresponding North American releases.

Source material that was converted from a different format is a special
case. Producing a correct transfer for pure video material from NTSC to
PAL or vice versa is very difficult, due to the differences in framerate
and number of lines. Whether a deinterlacer is needed depends on the
details of the transfer. In the particular case of anime, a PAL
conversion usually spells disaster for deinterlacing; see
[http://www.animemusicvideos.org/guides/avtech/videogetb2a.html].

== Algorithm types ==

In {{VLC}}, there are several deinterlacing algorithms to choose from.
This section presents a general classification. Skip ahead for an
individual description of each mode.

Algorithms available from a specific VLC version onward are marked with
Name(vx.y.z+).

=== Doublers ===

'''VLC modes''': Bob, Linear, Yadif (2x) (v1.1.0+), Phosphor(v1.2.0+)

These algorithms display the video at the original half-picture rate,
which is typically 50 (PAL) or 60 (NTSC) half-pictures per second. This
is double the full picture rate, hence the name. This approach to
deinterlacing is also known as field rendering.

This group takes into account that the half-pictures of a true
interlaced video were intended to be displayed at different times. This
can make the motion look very smooth.

Simple doublers (Bob and Linear) display only one half-picture at a
time. Nevertheless, the quick alternating display produces a convincing
illusion of full vertical resolution while playback is running.

Some more advanced doublers (such as Yadif (2x)) are based on
interpolators (see below), and attempt to generate full pictures to
display. When interpolators are used in this way, which field is kept,
alternates just like in the simple doublers.

The last doubler (Phosphor) does not fit into either of these
categories, but attempts to simulate a traditional CRT TV.

All doublers can be used with both true interlaced and telecined video.

=== Interpolators ===

'''VLC modes''': X, Yadif(v1.1.0+), (Discard)

These algorithms analyze the picture, detecting progressive and
interlaced parts. Typically the progressive parts of the picture are
passed through unchanged, although in some algorithms various kinds of
filtering may be used.

For the interlaced parts, one half-picture is kept, while the other is
generated out of thin air with various mathematical methods, based on
the information in one or both of the original half-pictures.

The Discard algorithm is a degenerate case of this type, which does not
analyze the picture. It simply keeps one half-picture and discards the
other one.

The output runs at the full-picture rate, which is typically 25 (PAL) or
30 (NTSC) pictures per second. The different intended display times for
the half-pictures in a true interlaced video are ignored.

Interpolators are designed for use with true interlaced video only. They
will stutter if applied to telecined video.

Some doublers exist, such as Yadif (2x), which are based on
interpolators. These hybrid algorithms behave like doublers (see above).
They may be able to improve the picture quality compared to simple
doublers, at the cost of more CPU cycles (requiring a faster processor).

=== Blenders ===

'''VLC modes''': Mean, Blend

These algorithms mix information from both half-pictures to produce a
blended (mixed) full picture. This is simple and removes interlacing,
but causes ghostlike trails for fast motion.

The output runs at the full-picture rate, which is typically 25 (PAL) or
30 (NTSC) pictures per second. The different intended display times for
the half-pictures in a true interlaced video are ignored.

Blenders are designed for use with true interlaced video only, and will
stutter with telecined video.

=== Inverse telecine ===

'''VLC modes''': IVTC(v1.2.0+)

This group of algorithms is specifically designed for removing telecine
from NTSC telecined video. Inverse telecine is also known as ''IVTC'',
''film mode'' and ''3:2 reverse pulldown''.

Inverse telecine algorithms try to extract the original progressive film
frames and to display them at the original framerate (24 pictures per
second). In the ideal case, this perfectly restores the progressive
signal. There is no loss of information and no need to generate anything
out of thin air.

Due to practical reasons, these algorithms are always based on analyzing
the picture. They are not and cannot be perfectly accurate, but in
practice they work well for most telecined sources.

== <span id="Modes"></span> VLC deinterlace modes ==
[[`File:VLC <>`__-_Deinterlace_Mode.pngthumbThe deinterlace options
selection]] VLC has the following deinterlace modes. Refer to 100fps.com
for illustrations. VLC does not have anything like what 100fps.com calls
Motion blur, Hybrid, and Motion compensation.

=== Disabled === This is what 100fps.com calls "do nothing". Other
names: "weave" or "no deinterlacing". Should be used for PsF
([//en.wikipedia.org/wiki/Progressive_segmented_Frame]) content.

=== Blend === Blender (full resolution). Each line of the picture is
created as the average of a line from the odd and a line from the even
half-pictures. This ignores the fact that they are supposed to be
displayed at different times.

=== Bob === Doubler. Display each half-picture like a full picture, by
simply displaying each line twice. Preserves temporal resolution of
interlaced video.

=== Discard === Only display one of the half-pictures, discard the
other. Other name: "single field". Both temporal and vertical spatial
resolutions are halved. Can be used for slower computers or to give
interlaced video movie-like look with characteristic judder.

=== Linear === Doubler. Bob with linear interpolation: instead of
displaying each line twice, line 2 is created as the average of line 1
and 3, etc.

=== Mean === Blender (half resolution). Display a half-picture that is
created as the average of the two original half-pictures.

=== X === Interpolator. Generates a full picture taking the odd lines
from the odd half-picture, and creating the even lines through a
complicated algorithm (involving ME, MC, edge-oriented interpolation)
that uses information from both half-pictures.

This is similar to what 100fps.com calls Area based.

=== Yadif (v1.1.0+)=== Interpolator. The ''Yet Another DeInterlacing
Filter'' from the [[MPlayer]] project. Generates a full picture taking
the odd lines from the odd half-picture, and creating the even lines
through a complicated algorithm that includes both temporal and spatial
interpolation.

=== Yadif (2x) (v1.1.0+)=== Doubler. Bob with Yadif interpolation. <span
style="color:red">'''Caution''': Very heavy on the CPU.</span>

=== Phosphor (v1.2.0+) === Doubler. This filter attempts to simulate the
rendering mechanism of a traditional CRT TV. The latest two
half-pictures are displayed, the old one fading out. The strength of the
fade effect can be configured in All Preferences, see Video > Filters >
Deinterlace.

=== IVTC (v1.2.0+) === Inverse telecine. Removes telecine from NTSC
telecined video in realtime, [[lossless]]ly recovering the progressive
signal. '''Note''': Only applicable to telecined sources. Particularly
useful for NTSC anime DVDs.

== Examples ==

<gallery> File:Example- Disabled Deinterlace.pngDiscard File:Example-
Blend Deinterlace.pngMean File:Example- Bob Doubler.pngLinear
File:Example-X interpolate.pngYadif File:Example-Yadif 2.pngPhosphor
File:Example-Invert Telecine.png|IVTC </gallery>

== Recommendation == For telecined sources, use '''IVTC'''.

For true interlaced sources, use a doubler. Which one is a matter of
taste. Try '''Linear''' first; it is pretty good while simple and light
on the CPU.

The classic '''Bob''' gives the lowest CPU load and is very simple.

You can use '''Yadif (2x)''' if you have a very fast CPU or fastest
graphics cards such as NVIDIA Geforce, AMD Radeon or other best graphics
cards.

The '''Phosphor''' (v1.2.0+) mode is different, and may be worth a try
if you want a "TV look".

== Disclaimer == Please update this page if it contains any errors, is
incomplete, or when it goes out of date.

== Appendix: Technical summary == {{See
also|Documentation:Modules/deinterlace}}

This table summarizes various technical information on the algorithms.
Don't be afraid to dive in - it's intended for users.

If you are a developer looking for more detailed technical
understanding, this module also has a section in the [[Hacker
Guide/Video Filters/Deinterlace|Hacker Guide]].

'''Terminology'''

-  "field" = half-picture
-  "top field" = "odd lines" in other sections above (note that the
   numbering started from 1)
-  "bottom field" = "even lines"

'''Legend'''

-  Column 4:2:0 in the table = "if input has 4:2:0 chroma, then..." See
   [//en.wikipedia.org/wiki/Chroma_subsampling#Sampling_systems_and_ratios]
   for an explanation and pictures. This format is common on DVDs.
-  Column 4:2:2 in the table = "if input has 4:2:2 chroma, then..."
-  C, H, FR = output Chroma, Height, Framerate
-  0 = output has 4:2:0 chroma
-  2 = output has 4:2:2 chroma
-  h = half height; output has as many lines as an input half-picture
-  f = full height; output has as many lines as an input full picture
-  1x = output has original framerate (original full-picture rate;
   typically 25 (PAL) or 30 (NTSC) times per second)
-  2x = output has double framerate (original half-picture rate;
   typically 50 (PAL) or 60 (NTSC) times per second)
-  '''n)''' = numbered note, read below for details

Note that the picture will be scaled before being displayed, so the
number of lines just tells us how detailed the picture could potentially
be.

{\| style="text-align:left; vertical-align:center;" border="1" ! Algo !
4:2:0 ! 4:2:2 ! Algo type ! Interpolation (if applic.) ! Notes \| C, H,
FR \| C, H, FR \| \| \| Discard \| 0, h, 1x \| 0, f, 1x \| interpolator
\| none \| keeps only top field; each line is repeated Mean \| 0, h, 1x
\| 2, h, 1x \| blender \| \| half-resolution blender; '''1)''' Blend \|
0, f, 1x \| 0, f, 1x \| blender \| \| full-resolution blender; '''2)'''
Bob \| 0, f, 2x \| 0, f, 2x \| doubler \| none \| each line is repeated;
'''3)''' Linear \| 0, f, 2x \| 2, f, 2x \| doubler \| simple linear \|
first/last line copied; others interpolated; '''3)''' X \| 0, f, 1x \|
2, f, 1x \| interpolator \| MC + edge-oriented \| keeps only top field
in interlaced parts; '''4)''' Yadif \| 0, f, 1x \| 2, f, 1x \|
interpolator \| spatial/temporal \| keeps only top field in interlaced
parts Yadif (2x) \| 0, f, 2x \| 2, f, 2x \| doubler \| spatial/temporal
\| Yadif and Yadif (2x) come from MPlayer Phosphor \| '''5)''', f, 2x \|
2, f, 2x \| doubler \| \| CRT TV simulator; '''6)''' IVTC \| 0, f,
'''7)''' \| 2, f, '''7)''' \| inverse telecine \| \| \|}

The luma (Y) component scale I ("analog", 16..240) vs. J (full scale,
"digital", 0..255) is preserved in all format conversions.

'''Notes'''

'''1)''' The Mean algorithm simply pairs the original lines, and
averages each pair into one output line. Line 1 of output is the mean of
lines 1 and 2 in input, line 2 of output is the mean of lines 3 and 4 in
input, and so on.

'''2)''' Blend is slightly more sophisticated than Mean. The first line
of output is copied from the first line of input. For any other output
line N, the line is the mean of input lines N and N-1. That is, the
second line of output is the mean of lines 1 and 2 in input, the third
line is the mean of lines 2 and 3, ... and finally, the last line of
output is the mean of the last two lines in input. The sliding averaging
procedure preserves the original vertical resolution.

'''3)''' Bob converts the half-pictures to full-pictures by simply
showing each line twice; so while the full number of lines are
displayed, the true resolution is only half. The same goes for Linear
and Yadif (2x), though it's a bit smarter about the process. Though, it
can also change frame rate on special effects such as the Psychedelic
effect if filter is turned on.

Still, even the basic Bob is slightly more clever than just a 2x version
of Discard. In the output, the bottom field is offset by one line with
respect to the top field. This is the technical reason behind the
perceived full resolution magic. (As a side effect, it also causes
perfectly horizontal lines to flicker in a way characteristic to the Bob
algorithm. The other doublers try to overcome this.)

'''4)''' The X algorithm divides the video into blocks of 8x8 pixels,
and analyzes them. It blurs the progressive blocks lightly. In the
interlaced blocks, it keeps only the top field, and uses MC and
edge-oriented interpolation to create the bottom field.

'''5)''' Output from Phosphor is 4:2:2 if the Upconvert mode is chosen
in the settings, otherwise 4:2:0 is used.

'''6)''' Phosphor displays the latest two fields, regardless of temporal
frame boundaries. To simulate phosphor light output decay, the old field
is darkened by an amount that can be configured in All settings > Video
> Filters > Deinterlace.

'''7)''' IVTC outputs at (4/5)x of original framerate, when inverting
telecine on a locked-on cadence, and at 1x while trying to acquire
lock-on.

[[Category:Glossary]] {{Documentation}}
