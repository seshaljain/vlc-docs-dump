.. raw:: mediawiki

   {{Back to|Hacker Guide}}

.. raw:: mediawiki

   {{Module|name=deinterlace|type=video filter2|description=Removes interlacing from display}}

This is the `Hacker's Guide <Hacker_Guide>`__ for the deinterlace module. See also the technical summary in the `user documentation <Deinterlace>`__.

Interfacing with the deinterlacer
---------------------------------

This section deals with interfacing other parts of with the deinterlacer. For a description of the internals, skip ahead.

How to prepare input
~~~~~~~~~~~~~~~~~~~~

The deinterlacer assumes that the input consists of full frames (``picture_t``), with \ ``i_nb_fields``\ \ ``== 2`` or ``3`` (depending on repeat_pict flags in the input stream), \ ``b_progressive``\ \ ``== false``, and full vertical resolution (i_visible_lines) of the input stream. The b_top_field_first flag is also optionally used by the deinterlacer, and must be set correctly to guarantee correct operation in all modes.

Each plane is stored linearly, one line at a time, in an uint8_t array of size i_lines*i_pitch, where i_lines and i_pitch can be read off the ``plane_t`` for each plane (e.g. p_pic->p[plane_index].i_lines). In YUV formats, the luma and chroma planes have different resolution.

Note that i_lines may differ from i_visible_lines and i_pitch from i_visible_pitch. The value of i_pitch depends on how the ``picture_t`` was created. The filter picture pool may, and usually does, have a pitch different from that produced by ``picture_NewFromFormat()``, even though the visible pitches are the same.

It is assumed that the active picture area starts at the upper left edge. The first i_visible_lines lines (``0`` through i_visible_lines-1, inclusive), make up the visible lines. The rest of the lines (i_visible_lines through i_lines-1, inclusive) are the (invisible) vertical margin.

Pixels at offsets 0 to i_visible_pitch-1 relative to each visible line start are visible. The rest of the pixels, at offsets i_visible_pitch to i_pitch-1, make up the (invisible) horizontal margin.

It is not necessary to initialize the memory in the invisible parts; writing just the visible part of the picture is enough.

Note that this implies that any processing loops only need to iterate through the part from 0 to i_visible_pitch (and i_visible_lines), but the pixel offsets in the array must be computed using i_pitch.

For any plane that has full vertical resolution, the (macro-)pixels are stored as if the frame was progressive, i.e., the fields are interleaved. Line 0 of the plane comes from the top field, line 1 from the bottom field, line 2 from the top field, and so on. This always holds for the luma plane, and in the 4:2:2 chroma formats (`I422 <I422>`__ and `J422 <J422>`__), also for the chroma planes.

If the chroma format is 4:2:0 (`I420 <I420>`__, `J420 <J420>`__ or `YV12 <YV12>`__), both fields share the same chroma. This kind of chroma is stored as-is, at half resolution (both horizontal and vertical) in the ``U`` and ``V`` planes of the ``picture_t``. The same linear format is used as above (array of size i_lines*i_pitch, first i_visible_lines used, and first i_visible_pitch pixels on each visible line used), but because there is only one "chroma field" in this case, the fields do not alternate. Instead, chroma line 0 corresponds to luma lines 0 and 1, chroma line 1 to luma lines 2 and 3, and so on.

Additionally, if chroma is `YV12 <YV12>`__, the U plane is stored in the array index ``V_PLANE``, and the V plane is stored in the array index ``U_PLANE``. This is because `YV12 <YV12>`__ uses the plane ordering YVU, while the array index constants (see ) are named according to the more common ordering YUV. For all chroma formats using the more common ordering, ``U_PLANE`` refers to the ``U`` component and ``V_PLANE`` to the ``V`` component, as expected.

Example:

::

   p_pic->p[Y_PLANE].p_pixels[23*w+42]

where \ ``w``\ \ ``= p_pic->p[Y_PLANE].i_pitch``, refers to the pixel on the luma plane at x = 42, y = 23 (0-based indexing).

If the chroma is `I420 <I420>`__ or `J420 <J420>`__,

::

   p_pic->p[U_PLANE].p_pixels[11*w+21]

where now \ ``w``\ \ ``= p_pic->p[U_PLANE].i_pitch``, refers to the chroma macropixel on the U plane that corresponds to the above example. Obviously, 11 = floor(23/2).

For 4:2:2 chroma (`I422 <I422>`__ or `J422 <J422>`__), only the horizontal chroma resolution is half that of the luma, and the corresponding macropixel is

::

   p_pic->p[U_PLANE].p_pixels[23*w+21]

How to interpret output
~~~~~~~~~~~~~~~~~~~~~~~

The frames output by the deinterlacer are ``picture_t``'s, with \ ``i_nb_fields``\ \ ``== 2`` and \ ``b_progressive``\ \ ``== true``. The output chroma format and number of visible lines are algorithm-dependent.

Resolution and chroma conversions are allowed, and it should be assumed there is no particular relation between input and output. Currently possible output chroma formats are `I420 <I420>`__, `YV12 <YV12>`__, `J420 <J420>`__, `I422 <I422>`__ and `J422 <J422>`__. Vertical resolution may be original or half. Thus, chroma format and vertical resolution should be read off the output frame metadata (appropriate ``picture_t`` data fields).

From the top-level ``Deinterlace()``, the output pictures go into a linked list (using the "next" pointer in ``picture_t``), which is then given to the caller. What happens to the pictures then, is outside the scope of the module.

Temporally, non-doubling deinterlacers produce exactly one output picture per one input, IVTC produces one or zero (at the dropped frame), and framerate doublers produce two or three (depending on repeat_pict of each input frame).

The timings (presentation timestamp; PTS; ``picture_t`` data field "date") may change arbitrarily between input and output. It is not even guaranteed that calling the deinterlacer for an input frame outputs a frame corresponding to that input frame. Yadif uses the frame offset feature, and IVTC effectively does, too. This means that when frame "2" goes in, what comes out is deinterlaced frame "1" - in the case of Yadif, still with its original PTS! (The offset does NOT introduce a delay; thus it keeps A/V sync intact. This is why it is called i_frame_offset and not i_frame_delay in the code.) In the case of IVTC, the PTS is somewhat like original, but corrected for the 29.97 > 23.976 fps conversion... usually.

The `deinterlace <deinterlace>`__ filter is not required to actually output anything the first few times it is called. Some algorithms keep a history and use it for temporal filtering. Currently, this is 3 input pictures, and the first call to ``Deinterlace()`` always outputs a picture. The second call may drop. From the third call on, the history buffer has filled, and at this point it is guaranteed that normal operation starts as defined by the chosen algorithm.

For generality, it should be assumed that M input pictures map to N output pictures, with arbitrary, different M and N. Note that even though ``repeat_pict`` means "repeat first field", the first and third output pictures from a framerate doubler, for any given input frame, are allowed to be different due to temporal filtering. (Phosphor does this.) Thus, it should also be assumed that each output picture is unique.

It may or may not be safe to display-hold still images, depending on the deinterlacing algorithm. For non-doublers, this is safe. For doublers, it is not. This is because framerate doubling algorithms are often designed based on the illusion of increased perceived resolution that can be achieved by rapidly alternating half-resolution images in an appropriate way.

Thus, "progressive" pictures from framerate doublers are not actually progressive (at least not at full resolution), but only appear so while the filter is constantly producing new pictures at a steady framerate. Unfortunately, currently there is no way to determine from the outside which kind of algorithm has been chosen.

File structure
--------------

This applies to (1st May 2011) and later.

The deinterlace filter is located in .

-  **modules/video_filter/deinterlace/deinterlace.[ch]**

   -  The main files of the filter.
   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/deinterlace.c}}

   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/deinterlace.h}}

-  ****

   -  Common macros (min, max, etc.).

-  ****

   -  Macros for MMX inline assembly support. Safe to include only ``#ifdef CAN_COMPILE_MMXEXT``.

-  **modules/video_filter/deinterlace/helpers.[ch]**

   -  General-use helper functions: interlace detection, motion detection, glueing a field pair to make a frame.
   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/helpers.c}}

   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/helpers.h}}

-  **modules/video_filter/deinterlace/merge.[ch]**

   -  Line-blending functions and (in header) macros for mixing two picture lines into one. (You'll want to use the ``Merge()`` and ``EndMerge()`` macros.)
   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/merge.c}}

   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/merge.h}}

-  **modules/video_filter/deinterlace/algo_basic.[ch]**

   -  Basic algorithms: Discard, Bob, Linear, Mean, Blend.
   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/algo_basic.c}}

   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/algo_basic.h}}

-  **modules/video_filter/deinterlace/algo_*.[ch]**

   -  Advanced algorithms, one algorithm per set of .c and .h.
   -  If the same algorithm has framerate-doubling and non-doubling versions, it counts here as the same algorithm. For example, both yadif and yadif2x are implemented in (in the same render function, even).
   -  As of , the following files exist:
   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/algo_x.c}}

   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/algo_x.h}}

   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/algo_yadif.c}}

   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/algo_yadif.h}}

   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/algo_phosphor.c}}

   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/algo_phosphor.h}}

   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/algo_ivtc.c}}

   -  

      .. raw:: mediawiki

         {{VLCSourceFile|modules/video_filter/deinterlace/algo_ivtc.h}}

The list of files making up the module (for the build system) is in .

Understanding the code
----------------------

It is recommended to look at the existing algorithms:

-  The simple algorithms in make good first examples in getting to know the internals of the deinterlacer. But to avoid becoming confused:

   -  First, make sure to understand the implications of the flags (b_double_rate, b_half_height) for each mode in ``SetFilterMethod()`` ().
   -  Then, understand the implications of the output chroma choosing logic in ``GetOutputFormat()`` (``deinterlace.c``).
   -  Note that these flags are nowhere to be seen inside ``algo_basic.c`` itself!
   -  You can also refer to the technical summary table in `Deinterlacing <Deinterlacing>`__. After reading that, it should all make (more) sense.

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/video_filter/deinterlace/algo_x.c}}

   provides an example of an advanced algorithm with lots of private functions.

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/video_filter/deinterlace/algo_yadif.c}}

   provides an example of gluing an existing algorithm to VLC. The original file from MPlayer is ; and are glue code for VLC.

-  ``ComposeFrame()`` in provides an example of chroma conversions. See for its usage.
-  Soft field repeat, which **must** be supported by all framerate doublers, is handled differently in different filters. What is a sensible way depends on how the algorithm works. See Bob, Yadif, and Phosphor for very different examples.

Also, generally:

-  See the available macros and helper functions in , , , and also .
-  Make sure you understand 4:2:0 and 4:2:2 chroma (explanation and pictures at [//en.wikipedia.org/wiki/Chroma_subsampling#Sampling_systems_and_ratios Wikipedia]).

   -  The filter supports `I420 <I420>`__, `J420 <J420>`__, `YV12 <YV12>`__, `I422 <I422>`__ and `J422 <J422>`__ chroma. See `YUV <YUV>`__ on the VideoLAN wiki.
   -  `YV12 <YV12>`__ is YVU (3 planes), others are YUV (3 planes). Except the plane order, `YV12 <YV12>`__ is identical to `I420 <I420>`__.
   -  The Y component of J has full ("digital") scale 0..255, instead of the "analog" 16..240 of I. Usually you don't need to care about this distinction, if you stay within the same chroma, or only convert between 4:2:0 and 4:2:2, preserving I/J.
   -  Note that if you want to upconvert `YV12 <YV12>`__ into `I422 <I422>`__, you will need to swap the U and V planes. For an example, see ``ComposeFrame()`` in .
   -  See .
   -  Useful constants: ``Y_PLANE``, ``U_PLANE``, ``V_PLANE`` (). For `YV12 <YV12>`__, ``U_PLANE`` actually refers to V, and ``V_PLANE`` to U.

-  Much of the stuff is thoroughly documented. See the comments (and please keep them up to date when you modify things).

Adding a new mode
-----------------

So, you have thought up a new algorithm, or maybe you want to add in an existing one from another GPL-compatible project.

Here is a checklist for implementing a new mode:

-  Choose a unique internal name (for config system and module internal use), and a user label (for GUI).

   -  Update the mode lists in
   -  The internal names must not be localized; use bare strings, e.g. "label"
   -  The user labels should be localized if they contain English, e.g. N_("My Label")
   -  In some special cases, user labels might not need localization, e.g. "X"
   -  If you need unicode characters in the user label, use the \\uxxxx feature of C99 (e.g. \\u00b2 is the superscript two / math squared symbol, so ``static const char* const my_label = "X\u00b2";`` will render as ``X``\ :sup:```2``` in the GUI).

      -  Here unicode = anything that is not 7-bit ASCII
      -  This is especially important if you intend it for translation, since gettext does not allow unicode characters in the original C locale strings.

-  Write support code in :

   -  Need configuration options? Search for *phosphor-chroma* for an example of making one.

      -  If you do add an option, update ``ppsz_filter_options[]``. It is used to validate what options exist.

   -  Update ``SetFilterMethod()``:

      -  Setup the flags for your mode. It is up to you to define how you want your algorithm to behave; certain conversions between input and output are allowed. (Keep this in mind when reading existing modes as examples! Refer to this function if necessary.)

         -  b_double_rate = framerate doubler/field renderer.

            -  If true, it means your mode outputs one frame for each input field.
            -  If false, it means your mode outputs one frame for each input frame.
            -  These two types behave differently; see e.g. ``RenderDiscard()`` (no doubling) and ``RenderBob()`` (doubling) for the simplest examples.
            -  Framerate doublers **must** support soft field repeat (\ ``nb_fields``\ \ ``== 3``). If you're not quite sure how to process the middle field, it's usually safe just to copy the input picture, since a field repeat usually implies no motion during that frame.
            -  Soft field repeat is necessary to support some NTSC film sources correctly. These include anything that is soft-telecined, as well as sources where some space has been saved by using field repeat in some frames with no motion. Examples from anime: Sol Bianca (field repeats; this is a 24p/60i hybrid anime), Silent Mobius (field repeats, soft TC), Angel Links (soft TC), Stellvia of the Universe (soft TC).

         -  b_half_height = halved vertical resolution in output.

            -  If false, the output has as many lines as the input. (This is the usual choice.)
            -  If true, the output has only half the number of lines when compared to input. Useful for some special cases, though it's fair to say all useful ones have already been covered in .
            -  Note that this refers to the data resolution; you can still output a picture with doubled (copied) lines even if you use full resolution (``RenderBob()`` does this).

         -  b_use_frame_history = use the input frame history buffer.

            -  If true, you will have the three (HISTORY_SIZE) latest frames available in the array ``pp_history[]`` in ``filter_sys_t``. You can fetch the frames from there; your render function does not need an input picture parameter. This is useful for temporal filtering. See ``RenderYadif()`` for an example of using the history buffer.
            -  If false, you will need to feed each input picture to your render function directly. This is meant for filters that map the frames in a simple 1 -> 1 (or 1 -> 2) manner, needing no history. See anything in , or ``RenderX()`` (), for an example.
            -  It is up to you to decide which frame you want to output at each call; see ``RenderYadif()`` (outputs second latest frame) and ``RenderPhosphor()`` (outputs latest frame) for examples. See i_frame_offset in .

   -  Update ``GetOutputFormat()``:

      -  Setup which chroma your mode outputs, and under which kind of input.

         -  Usually you just want to pass it through. This is the default for 4:2:0 input, but **do** add your mode into the first switch statement to support 4:2:2 input correctly.
         -  What "correct" means is up to you; see the Phosphor algorithm for an example doing chroma conversions.

      -  Half-heighting is already handled by setting the flag in ``SetFilterMethod()``, so there's no need to touch that part.

   -  ``Deinterlace()`` handles some things for you automatically:

      -  Allocation of output frames (so you can simply render into them).
      -  Setting the correct output timestamps (PTS), also for framerate doublers.

         -  You **can** use \ ``i_frame_offset``\ \ ``= CUSTOM_PTS`` and compute the timestamps yourself, but this is needed only for nontrivial framerate conversions. For an example, see , function ``IVTCOutputOrDropFrame()``.

   -  Update the switch statement in ``Deinterlace()`` to handle your new algorithm. See the existing cases for examples.

-  Create ``algo_``\ \ ``zzz``\ \ ``.c`` and ``algo_``\ \ ``zzz``\ \ ``.h``, where zzz is the internal name of your new mode.

   -  You want to write at least one public function: ``RenderZzz()``, called from ``Deinterlace()``. Most of the parameters of the render functions are self-explanatory, but i_order and i_field may need an explanation.

      -  These two parameters are used only for algorithms, which support framerate doubling.
      -  i_order is the temporal number, inside the current frame, of the current field being rendered: 0 (first), 1 (second) or 2 (repeated first, used only when \ ``nb_fields``\ \ ``== 3``).
      -  i_field indicates which field is being rendered: 0 for top (lines 0, 2, 4, ...), 1 for bottom (lines 1, 3, 5, ...).

         -  This needs to match i_order and the b_top_field_first flag *of the picture you are currently rendering*. (Note that this may not be the latest input picture, if you use the history buffer.)
         -  To automatically get it correct, implement your case in ``Deinterlace()`` like the existing ones, and use i_frame_offset as instructed in . Note that if you set i_frame_offset in your render function, it takes effect at the **next** input frame (defined as the next time ``Deinterlace()`` is called). See the rationale in .

      -  If you want to use a framerate doubling algorithm in non-doubling mode, you can pass \ ``i_order``\ \ ``= 0`` and \ ``i_field``\ \ ``= 0`` (like the existing filters, which have both modes).

   -  If you need to have startup or cleanup code, see the Phosphor and IVTC algorithms for examples.

      -  Phosphor configuration options are read in ``Open()``.
      -  IVTCClearState() is called in ``Open()`` and in ``Flush()``. It initializes/resets IVTC state.
      -  Note that the filter may be flushed while running under some circumstances. If you allocated something upon startup, don't deallocate from ``Flush()``, but make a separate deallocation function and call that from ``Close()``.
      -  Note that the filter chain **never** changes the input format on the fly; it always ``Close()``\ s and ``Open()``\ s again.

   -  Keep in mind that the deinterlacer is low-level code and needs to be fast.

      -  For example, for a 60i stream, a framerate doubler should render one output frame in preferably under 5ms. Note that the field interval in 60i is about 16ms, and some time is needed for decoding, rendering and such. 8ms and above is dangerously slow (will cause skipping).
      -  Consider writing the inner processing loops in vectorized inline assembly, such as MMX. This can often gain a factor of 2-8x in speed, depending on how much and what kind of processing your algorithm needs.

-  Update , so that the build system will compile your new files into the module.

See `new module integration <Hacker_Guide/How_To_Write_a_Module#Git>`__ for additional help.

Finally, inform the rest of VLC about the existence of your new mode. There are some deinterlacer mode lists and validity checking code that is external to the deinterlacer module itself. Some of these contain the internal name, some the user label. Make sure that these match the ones you put in .

As of this writing, these are located in:

-  

   .. raw:: mediawiki

      {{VLCSourceFile|src/libvlc-module.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|src/control/video.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|src/video_output/interlacing.c}}

Search for the string *yadif* to find the relevant parts quickly. The string is unique enough to match even from the whole source tree.

Speaking of which, a pretty good way to keep up to date as to where to find this stuff is to go to the root of the vlc source tree in the terminal, and search for *yadif* recursively:

.. code:: bash

   find . -name "*.[ch]" -exec grep -Hr 'yadif' \{\} \;

Then just note down anything that matches anywhere else except .

.. raw:: mediawiki

   {{Hacker Guide}}
