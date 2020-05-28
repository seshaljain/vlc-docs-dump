{{Outdated}}<!-- We don't use wxWidgets anymore -->
{{RightMenu|Documentation TOC}} VLC includes a system of ''filters''
that allow you to modify the audio and video.

==Deinterlacement and Post Processing==

VLC is able to [[deinterlace]] a video stream using different
deinterlacement methods. Deinterlacement can be enabled in the ''Video''
menu, ''Deinterlacement'' menu item. The ''Blend'' methods gives the
best results in most cases. The ''discard'' method is a less resource
consuming alternative, although its results may be slightly compromised.

On some particular streams ([[MPEG 4]], [[DivX]], [[Xvid]], [[Sorenson
Video|Sorenson]], etc.), some additional image filtering can be applied
to the video before display, improving its quality in some cases. This
can be enabled by using the ''Post processing'' menu item in ''Video''.
Different levels of post processing can be chosen here. A higher level
means more filtering.

==Video filters==

=== Summary === VLC features several filters able to change the video
(distortion, brightness adjustment, motion blurring, etc.).

In Windows and Linux, the user must go to the ''Effects and Filters'' in
the ''Tools'' menu item. A dialogue box entitled "Adjustments and
Effects" will appear.

[[File:Video effects - essential, with image adjust
selected.pngcenter|alt=Effects and Filters dialogue box as it appears in
a pre-release version of 2.0.0 on Ubuntu Linux]]

In [[macOS]] you can enable these filters through the ''Extended
Controls panel''. Click on the triangle next to ''Video filters'' to
select your filters or expand the ''Adjust Image'' section to change the
contrast, hue, etc.

[[File:intf-osx-vfilters.jpg%7Ccenter%7CFilter dialogue box as it
appears in macOS interface]]

iOS: [[File:VLC for iOS Video Filters.pngFilter dialogue box as it
appears in iOS devices]]

Example of combined effects on a video:

[[File:VLC-combined-effects.png%7Ccenter%7Calt=A striking image of a
video with many effects]]

=== Rotate ===

You can easily rotate a video. Open the ''Effects and Filters'' dialog,
in the ''Tools menu''

[[File:Bbb_rotate.png%7Ccenter%7Calt=A rotated image of a Big Buck Bunny
video]]

Select the ''Video Effects'' tab, then the ''Geometry'' one.

Check the ''Transform'' checkbox to use rotation presets (90°, 180°,
270°) or check the ''Rotate'' checkbox to manually select the angle you
wish to apply.

[[File:Video effects - geometry, with rotate selected.pngalt=The rotate
video dialogue box under the wxWidgets interface]]

==Audio filters==

===Equalizer=== {{Wikipedia|Equalization (audio)}} VLC features a
10-band graphical equalizer, a device used to alter the relative
frequencies of audio (e.g. for a bass boost). You can display it by
activating the advanced GUI on [[wxWidgets]] or by clicking the
''Equalizer'' button on the macOS interface. The following image is the
interface of the audio equalizer in the Windows and GNU/Linux interface.

[[File:Audio Filters.PNGEqualizer dialogue box as it appears in
wxWidgets for Windows and Linux]]

The equalizer in the macOS interface

[[File:Intf-osx-equalizer.jpg%7Ccenter%7Calt=Equalizer dialogue box as
it appears in macOS]]

[[File:VLC for iOS Equalizer.pngalt=Equalizer dialogue box as it appears
in iOS devices]]

Presets are available in all of these dialog boxes.

===Other audio filters===

At the moment, VLC features two other audio filters: a volume normalizer
and a filter providing sound spatialization with a headphone. They can
be enabled in the ''Effects and Filters'' menu item in the ''Tools'' tab
of the Windows and GNU/Linux interface and in the Audio section of the
Extended Controls panel of the macOS interface.

For better control, you need to go to the preferences. To select the
filters to be enabled, go to ''Audio'', then to ''Filters''. In the
"audio filters" box, enter the names of the filters to enable, separated
by commas. Valid names are "equalizer", "normvol" and "headphone".

If you want to tune the behavior of these filters, go to ''Audio,
Filters, [your filter]''. The equalizer and headphone filters can be
tuned.

{{Documentation}}
