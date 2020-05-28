{{Back toname=deinterlacedescription=Removes interlacing from display}}

This is the [[Hacker Guideuser documentation]].

== Interfacing with the deinterlacer ==

This section deals with interfacing other parts of {{VLC}} with the
deinterlacer. For a description of the internals, skip ahead.

=== How to prepare input ===

The deinterlacer assumes that the input consists of full frames
(<code>picture_t</code>), with <code><var>i_nb_fields</var> == 2</code>
or <code>3</code> (depending on <var>repeat_pict</var> flags in the
input stream), <code><var>b_progressive</var> == false</code>, and full
vertical resolution (<var>i_visible_lines</var>) of the input stream.
The <var>b_top_field_first</var> flag is also optionally used by the
deinterlacer, and must be set correctly to guarantee correct operation
in all modes.

Each plane is stored linearly, one line at a time, in an
<var>uint8_t</var> array of size <var>i_lines*i_pitch</var>, where
<var>i_lines</var> and <var>i_pitch</var> can be read off the
<code>plane_t</code> for each plane (e.g.
<var>p_pic->p[plane_index].i_lines</var>). In YUV formats, the luma and
chroma planes have different resolution.

Note that <var>i_lines</var> may differ from <var>i_visible_lines</var>
and <var>i_pitch</var> from <var>i_visible_pitch</var>. The value of
<var>i_pitch</var> depends on how the <code>picture_t</code> was
created. The filter picture pool may, and usually does, have a pitch
different from that produced by <code>picture_NewFromFormat()</code>,
even though the visible pitches are the same.

It is assumed that the active picture area starts at the upper left
edge. The first <var>i_visible_lines</var> lines (<code>0</code> through
<var>i_visible_lines-1</var>, inclusive), make up the visible lines. The
rest of the lines (<var>i_visible_lines</var> through
<var>i_lines</var>-1, inclusive) are the (invisible) vertical margin.

Pixels at offsets 0 to <var>i_visible_pitch-1</var> relative to each
visible line start are visible. The rest of the pixels, at offsets
<var>i_visible_pitch</var> to <var>i_pitch-1</var>, make up the
(invisible) horizontal margin.

It is not necessary to initialize the memory in the invisible parts;
writing just the visible part of the picture is enough.

Note that this implies that any processing loops only need to iterate
through the part from 0 to <var>i_visible_pitch</var> (and
<var>i_visible_lines</var>), but the pixel offsets in the array must be
computed using <var>i_pitch</var>.

For any plane that has full vertical resolution, the (macro-)pixels are
stored as if the frame was progressive, i.e., the fields are
interleaved. Line 0 of the plane comes from the top field, line 1 from
the bottom field, line 2 from the top field, and so on. This always
holds for the luma plane, and in the 4:2:2 chroma formats ([[I422]] and
[[J422]]), also for the chroma planes.

If the chroma format is 4:2:0 ([[I420]], [[J420]] or [[YV12]]), both
fields share the same chroma. This kind of chroma is stored as-is, at
half resolution (both horizontal and vertical) in the <code>U</code> and
<code>V</code> planes of the <code>picture_t</code>. The same linear
format is used as above (array of size <var>i_lines*i_pitch</var>, first
<var>i_visible_lines</var> used, and first <var>i_visible_pitch</var>
pixels on each visible line used), but because there is only one "chroma
field" in this case, the fields do not alternate. Instead, chroma line 0
corresponds to luma lines 0 and 1, chroma line 1 to luma lines 2 and 3,
and so on.

Additionally, if chroma is [[YV12]], the U plane is stored in the array
index <code>V_PLANE</code>, and the V plane is stored in the array index
<code>U_PLANE</code>. This is because [[YV12]] uses the plane ordering
YVU, while the array index constants (see
{{VLCSourceFile|include/vlc_picture.h}}) are named according to the more
common ordering YUV. For all chroma formats using the more common
ordering, <code>U_PLANE</code> refers to the <code>U</code> component
and <code>V_PLANE</code> to the <code>V</code> component, as expected.

Example:

<pre>p_pic->p[Y_PLANE].p_pixels[23*w+42]</pre>

where <code><var>w</var> = p_pic->p[Y_PLANE].i_pitch</code>, refers to
the pixel on the luma plane at x = 42, y = 23 (0-based indexing).

If the chroma is [[I420]] or [[J420]],

<pre>p_pic->p[U_PLANE].p_pixels[11*w+21]</pre>

where now <code><var>w</var> = p_pic->p[U_PLANE].i_pitch</code>, refers
to the chroma macropixel on the U plane that corresponds to the above
example. Obviously, 11 = floor(23/2).

For 4:2:2 chroma ([[I422]] or [[J422]]), only the horizontal chroma
resolution is half that of the luma, and the corresponding macropixel is

<pre>p_pic->p[U_PLANE].p_pixels[23*w+21]</pre>

=== How to interpret output ===

The frames output by the deinterlacer are <code>picture_t</code>'s, with
<code><var>i_nb_fields</var> == 2</code> and
<code><var>b_progressive</var> == true</code>. The output chroma format
and number of visible lines are algorithm-dependent.

Resolution and chroma conversions are allowed, and it should be assumed
there is no particular relation between input and output. Currently
possible output chroma formats are [[I420]], [[YV12]], [[J420]],
[[I422]] and [[J422]]. Vertical resolution may be original or half.
Thus, chroma format and vertical resolution should be read off the
output frame metadata (appropriate <code>picture_t</code> data fields).

From the top-level <code>Deinterlace()</code>, the output pictures go
into a linked list (using the "next" pointer in <code>picture_t</code>),
which is then given to the caller. What happens to the pictures then, is
outside the scope of the module.

Temporally, non-doubling deinterlacers produce exactly one output
picture per one input, IVTC produces one or zero (at the dropped frame),
and framerate doublers produce two or three (depending on repeat_pict of
each input frame).

The timings (presentation timestamp; PTS; <code>picture_t</code> data
field "date") may change arbitrarily between input and output. It is not
even guaranteed that calling the deinterlacer for an input frame outputs
a frame corresponding to that input frame. Yadif uses the frame offset
feature, and IVTC effectively does, too. This means that when frame "2"
goes in, what comes out is deinterlaced frame "1" - in the case of
Yadif, still with its original PTS! (The offset does NOT introduce a
delay; thus it keeps A/V sync intact. This is why it is called
<var>i_frame_offset</var> and not <var>i_frame_delay</var> in the code.)
In the case of IVTC, the PTS is somewhat like original, but corrected
for the 29.97 > 23.976 fps conversion... usually.

The [[deinterlace]] filter is not required to actually output anything
the first few times it is called. Some algorithms keep a history and use
it for temporal filtering. Currently, this is 3 input pictures, and the
first call to <code>Deinterlace()</code> always outputs a picture. The
second call may drop. From the third call on, the history buffer has
filled, and at this point it is guaranteed that normal operation starts
as defined by the chosen algorithm.

For generality, it should be assumed that <var>M</var> input pictures
map to <var>N</var> output pictures, with arbitrary, different
<var>M</var> and <var>N</var>. Note that even though
<code>repeat_pict</code> means "repeat first field", the first and third
output pictures from a framerate doubler, for any given input frame, are
allowed to be different due to temporal filtering. (Phosphor does this.)
Thus, it should also be assumed that each output picture is unique.

It may or may not be safe to display-hold still images, depending on the
deinterlacing algorithm. For non-doublers, this is safe. For doublers,
it is not. This is because framerate doubling algorithms are often
designed based on the illusion of increased perceived resolution that
can be achieved by rapidly alternating half-resolution images in an
appropriate way.

Thus, "progressive" pictures from framerate doublers are not actually
progressive (at least not at full resolution), but only appear so while
the filter is constantly producing new pictures at a steady framerate.
Unfortunately, currently there is no way to determine from the outside
which kind of algorithm has been chosen.

== File structure ==

This applies to {{Commit|c7d289cad5c9f73d1bfc5b136b503fc3646b6e41}} (1st
May 2011) and later.

The deinterlace filter is located in
{{VLCSourceFolder|modules/video_filter/deinterlace}}.

\*
'''<nowiki>modules/video_filter/deinterlace/deinterlace.[ch]</nowiki>'''
\*\* The main files of the filter. \*\*
{{VLCSourceFilemodules/video_filter/deinterlace/deinterlace.h}} \*
'''{{VLCSourceFilemodules/video_filter/deinterlace/mmx.h}}''' \*\*
Macros for MMX inline assembly support. Safe to include only
<code>#ifdef CAN_COMPILE_MMXEXT</code>. \*
'''<nowiki>modules/video_filter/deinterlace/helpers.[ch]</nowiki>'''
\*\* General-use helper functions: interlace detection, motion
detection, glueing a field pair to make a frame. \*\*
{{VLCSourceFilemodules/video_filter/deinterlace/helpers.h}} \*
'''<nowiki>modules/video_filter/deinterlace/merge.[ch]</nowiki>''' \*\*
Line-blending functions and (in header) macros for mixing two picture
lines into one. (You'll want to use the <code>Merge()</code> and
<code>EndMerge()</code> macros.) \*\*
{{VLCSourceFilemodules/video_filter/deinterlace/merge.h}} \*
'''<nowiki>modules/video_filter/deinterlace/algo_basic.[ch]</nowiki>'''
\*\* Basic algorithms: Discard, Bob, Linear, Mean, Blend. \*\*
{{VLCSourceFilemodules/video_filter/deinterlace/algo_basic.h}} \*
'''<nowiki>modules/video_filter/deinterlace/`algo <>`__\ *.[ch]</nowiki>'''*\ \*
Advanced algorithms, one algorithm per set of .c and .h. \*\* If the
same algorithm has framerate-doubling and non-doubling versions, it
counts here as the same algorithm. For example, both yadif and yadif2x
are implemented in
{{VLCSourceFilec7d289cad5c9f73d1bfc5b136b503fc3646b6e41}}, the following
files exist: \*\*
{{VLCSourceFilemodules/video_filter/deinterlace/algo_x.h}} \*\*
{{VLCSourceFilemodules/video_filter/deinterlace/algo_yadif.h}} \*\*
{{VLCSourceFilemodules/video_filter/deinterlace/algo_phosphor.h}} \*\*
{{VLCSourceFilemodules/video_filter/deinterlace/algo_ivtc.h}}

The list of files making up the module (for the build system) is in
{{VLCSourceFile|modules/video_filter/Modules.am}}.

== Understanding the code ==

It is recommended to look at the existing algorithms:

\* The simple algorithms in
{{VLCSourceFilemodules/video_filter/deinterlace/deinterlace.c}}). \*\*
Then, understand the implications of the output chroma choosing logic in
<code>GetOutputFormat()</code> (<code>deinterlace.c</code>). \*\* Note
that these flags are nowhere to be seen inside <code>algo_basic.c</code>
itself! \*\* You can also refer to the technical summary table in
[[Deinterlacing]]. After reading that, it should all make (more) sense.
\* {{VLCSourceFilemodules/video_filter/deinterlace/algo_yadif.c}}
provides an example of gluing an existing algorithm to VLC. The original
file from MPlayer is
{{VLCSourceFilemodules/video_filter/deinterlace/algo_yadif.c}} and
{{VLCSourceFilemodules/video_filter/deinterlace/helpers.c}} provides an
example of chroma conversions. See
{{VLCSourceFile|modules/video_filter/deinterlace/algo_phosphor.c}} for
its usage. \* Soft field repeat, which '''must''' be supported by all
framerate doublers, is handled differently in different filters. What is
a sensible way depends on how the algorithm works. See Bob, Yadif, and
Phosphor for very different examples.

Also, generally:

-  See the available macros and helper functions in
   {{VLCSourceFilemodules/video_filter/deinterlace/helpers.h}},
   {{VLCSourceFileinclude/vlc_picture.h}}.

\* Make sure you understand 4:2:0 and 4:2:2 chroma (explanation and
pictures at
[//en.wikipedia.org/wiki/Chroma_subsampling#Sampling_systems_and_ratios
Wikipedia]). \*\* The filter supports [[I420]], [[J420]], [[YV12]],
[[I422]] and [[J422]] chroma. See [[YUV]] on the VideoLAN wiki. \*\*
[[YV12]] is YVU (3 planes), others are YUV (3 planes). Except the plane
order, [[YV12]] is identical to [[I420]]. \*\* The Y component of J has
full ("digital") scale 0..255, instead of the "analog" 16..240 of I.
Usually you don't need to care about this distinction, if you stay
within the same chroma, or only convert between 4:2:0 and 4:2:2,
preserving I/J. \*\* Note that if you want to upconvert [[YV12]] into
[[I422]], you will need to swap the <var>U</var> and <var>V</var>
planes. For an example, see <code>ComposeFrame()</code> in
{{VLCSourceFileinclude/vlc_fourcc.h}}. \*\* Useful constants:
<code>Y_PLANE</code>, <code>U_PLANE</code>, <code>V_PLANE</code>
({{VLCSourceFile|include/vlc_picture.h}}). For [[YV12]],
<code>U_PLANE</code> actually refers to <var>V</var>, and
<code>V_PLANE</code> to <var>U</var>. \* Much of the stuff is thoroughly
documented. See the comments (and please keep them up to date when you
modify things).

== Adding a new mode ==

So, you have thought up a new algorithm, or maybe you want to add in an
existing one from another GPL-compatible project.

Here is a checklist for implementing a new mode:

\* Choose a unique internal name (for config system and module internal
use), and a user label (for GUI). \*\* Update the mode lists in
{{VLCSourceFilemodules/video_filter/deinterlace/deinterlace.c}}: \*\*
Need configuration options? Search for ''phosphor-chroma'' for an
example of making one. **\* If you do add an option, update
<code>ppsz_filter_options[]</code>. It is used to validate what options
exist.** Update <code>SetFilterMethod()</code>: **\* Setup the flags for
your mode. It is up to you to define how you want your algorithm to
behave; certain conversions between input and output are allowed. (Keep
this in mind when reading existing modes as examples! Refer to this
function if necessary.)**\ \*\* <var>b_double_rate</var> = framerate
doubler/field renderer. \*\*\ **\* If true, it means your mode outputs
one frame for each input field.\* If false, it means your mode outputs
one frame for each input frame.\* These two types behave differently;
see e.g. <code>RenderDiscard()</code> (no doubling) and
<code>RenderBob()</code> (doubling) for the simplest examples.\*
Framerate doublers '''must''' support soft field repeat
(<code><var>nb_fields</var> == 3</code>). If you're not quite sure how
to process the middle field, it's usually safe just to copy the input
picture, since a field repeat usually implies no motion during that
frame.\* Soft field repeat is necessary to support some NTSC film
sources correctly. These include anything that is soft-telecined, as
well as sources where some space has been saved by using field repeat in
some frames with no motion. Examples from anime: Sol Bianca (field
repeats; this is a 24p/60i hybrid anime), Silent Mobius (field repeats,
soft TC), Angel Links (soft TC), Stellvia of the Universe (soft
TC).**\ \*\* <var>b_half_height</var> = halved vertical resolution in
output. \*\*\ **\* If false, the output has as many lines as the input.
(This is the usual choice.)\* If true, the output has only half the
number of lines when compared to input. Useful for some special cases,
though it's fair to say all useful ones have already been covered in
{{VLCSourceFile|modules/video_filter/deinterlace/algo_basic.c}}.\* Note
that this refers to the data resolution; you can still output a picture
with doubled (copied) lines even if you use full resolution
(<code>RenderBob()</code> does this).**\ \*\*
<var>b_use_frame_history</var> = use the input frame history buffer.
\*\*\ **\* If true, you will have the three (<var>HISTORY_SIZE</var>)
latest frames available in the array <code>pp_history[]</code> in
<code>filter_sys_t</code>. You can fetch the frames from there; your
render function does not need an input picture parameter. This is useful
for temporal filtering. See <code>RenderYadif()</code> for an example of
using the history buffer.\* If false, you will need to feed each input
picture to your render function directly. This is meant for filters that
map the frames in a simple 1 -> 1 (or 1 -> 2) manner, needing no
history. See anything in
{{VLCSourceFile|modules/video_filter/deinterlace/algo_basic.c}}, or
<code>RenderX()</code>
({{VLCSourceFile|modules/video_filter/deinterlace/algo_x.c}}), for an
example.\* It is up to you to decide which frame you want to output at
each call; see <code>RenderYadif()</code> (outputs second latest frame)
and <code>RenderPhosphor()</code> (outputs latest frame) for examples.
See <var>i_frame_offset</var> in
{{VLCSourceFile|modules/video_filter/deinterlace/filter_sys_t}}.**
Update <code>GetOutputFormat()</code>: **\* Setup which chroma your mode
outputs, and under which kind of input.**\ \*\* Usually you just want to
pass it through. This is the default for 4:2:0 input, but '''do''' add
your mode into the first switch statement to support 4:2:2 input
correctly. \*\ **\* What "correct" means is up to you; see the Phosphor
algorithm for an example doing chroma conversions.**\ \* Half-heighting
is already handled by setting the flag in
<code>SetFilterMethod()</code>, so there's no need to touch that part.
\*\* <code>Deinterlace()</code> handles some things for you
automatically: **\* Allocation of output frames (so you can simply
render into them).**\ \* Setting the correct output timestamps (PTS),
also for framerate doublers. \*\ **\* You '''can''' use
<code><var>i_frame_offset</var> = CUSTOM_PTS</code> and compute the
timestamps yourself, but this is needed only for nontrivial framerate
conversions. For an example, see
{{VLCSourceFile|modules/video_filter/deinterlace/algo_ivtc.c}}, function
<code>IVTCOutputOrDropFrame()</code>.** Update the switch statement in
<code>Deinterlace()</code> to handle your new algorithm. See the
existing cases for examples. \* Create
<code>`algo <>`__\ <var>zzz</var>.c</code> and
<code>`algo <>`__\ <var>zzz</var>.h</code>, where <var>zzz</var> is the
internal name of your new mode. \*\* You want to write at least one
public function: <code>RenderZzz()</code>, called from
<code>Deinterlace()</code>. Most of the parameters of the render
functions are self-explanatory, but <var>i_order</var> and
<var>i_field</var> may need an explanation. **\* These two parameters
are used only for algorithms, which support framerate doubling.**\ \*
<var>i_order</var> is the temporal number, inside the current frame, of
the current field being rendered: 0 (first), 1 (second) or 2 (repeated
first, used only when <code><var>nb_fields</var> == 3</code>). **\*
<var>i_field</var> indicates which field is being rendered: 0 for top
(lines 0, 2, 4, ...), 1 for bottom (lines 1, 3, 5, ...).**\ \*\* This
needs to match <var>i_order</var> and the <var>b_top_field_first</var>
flag ''of the picture you are currently rendering''. (Note that this may
not be the latest input picture, if you use the history buffer.)
\*\ **\* To automatically get it correct, implement your case in
<code>Deinterlace()</code> like the existing ones, and use
<var>i_frame_offset</var> as instructed in
{{VLCSourceFile|modules/video_filter/deinterlace/deinterlace.h}}. Note
that if you set <var>i_frame_offset</var> in your render function, it
takes effect at the '''next''' input frame (defined as the next time
<code>Deinterlace()</code> is called). See the rationale in
{{VLCSourceFile|modules/video_filter/deinterlace/deinterlace.h}}.**\ \*
If you want to use a framerate doubling algorithm in non-doubling mode,
you can pass <code><var>i_order</var> = 0</code> and
<code><var>i_field</var> = 0</code> (like the existing filters, which
have both modes). \*\* If you need to have startup or cleanup code, see
the Phosphor and IVTC algorithms for examples. **\* Phosphor
configuration options are read in <code>Open()</code>.**\ \*
IVTCClearState() is called in <code>Open()</code> and in
<code>Flush()</code>. It initializes/resets IVTC state. **\* Note that
the filter may be flushed while running under some circumstances. If you
allocated something upon startup, don't deallocate from
<code>Flush()</code>, but make a separate deallocation function and call
that from <code>Close()</code>.**\ \* Note that the filter chain
'''never''' changes the input format on the fly; it always
<code>Close()</code>s and <code>Open()</code>s again. \*\* Keep in mind
that the deinterlacer is low-level code and needs to be fast. **\* For
example, for a 60i stream, a framerate doubler should render one output
frame in preferably under 5ms. Note that the field interval in 60i is
about 16ms, and some time is needed for decoding, rendering and such.
8ms and above is dangerously slow (will cause skipping).**\ \* Consider
writing the inner processing loops in vectorized inline assembly, such
as MMX. This can often gain a factor of 2-8x in speed, depending on how
much and what kind of processing your algorithm needs. \* Update
{{VLCSourceFilenew module integration]] for additional help.

Finally, inform the rest of VLC about the existence of your new mode.
There are some deinterlacer mode lists and validity checking code that
is external to the deinterlacer module itself. Some of these contain the
internal name, some the user label. Make sure that these match the ones
you put in
{{VLCSourceFile|modules/video_filter/deinterlace/deinterlace.h}}.

As of this writing, these are located in:

-  {{VLCSourceFile|src/libvlc-module.c}}
-  {{VLCSourceFile|src/control/video.c}}
-  {{VLCSourceFile|src/video_output/interlacing.c}}

Search for the string ''yadif'' to find the relevant parts quickly. The
string is unique enough to match even from the whole source tree.

Speaking of which, a pretty good way to keep up to date as to where to
find this stuff is to go to the root of the vlc source tree in the
terminal, and search for ''yadif'' recursively:

<syntaxhighlight lang="bash"> find . -name "*.[ch]" -exec grep -Hr
'yadif' {} ; </syntaxhighlight>

Then just note down anything that matches anywhere else except
{{VLCSourceFolder|modules/video_filter/deinterlace}}.

{{Hacker Guide}}
