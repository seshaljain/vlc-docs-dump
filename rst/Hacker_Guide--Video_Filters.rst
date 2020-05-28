.. raw:: mediawiki

   {{Back to|Hacker Guide}}

This is the `Hacker's Guide <Hacker_Guide>`__ for video filters (**video filter2**, VLC 2.0).

Location in source tree, compilation
------------------------------------

The right place for video filters is in the folder.

See for a list of video filters currently in VLC, and which source files belong to which.

See `new module integration <Hacker_Guide/How_To_Write_a_Module#Git>`__ for additional help on how to integrate a new module in the build system.

Additional documentation
------------------------

Reading `How to write a module <Hacker_Guide/How_To_Write_a_Module>`__ first is highly advised.

Some *video filters* may have their own `Hacker's Guide <Hacker_Guide>`__ sections.

Currently, the **deinterlace** filter has both a `Hacker's Guide section <Hacker_Guide/Video_Filters/Deinterlace>`__ and `user documentation <Deinterlace>`__ with some useful additional technical information.

Programming conventions and tips
--------------------------------

.. raw:: mediawiki

   {{VLC}}

`video filters <video_filters>`__ are usually written in C99, like the rest of VLC. Some use C++, like the AtmoLight plugin.

The usual stuff holds here too:

-  Use **assert()** for checking conditions that, in presence of no bugs, always hold.

   -  *Don't* use **assert()** for checking stuff that may fail at runtime. Handle errors gracefully.

-  Keep your code readable. Make private functions when it simplifies things.
-  Prefer 80 characters per line at maximum, if possible.

**Particularly** for video filters: keep in mind that this is **low-level stuff** and needs to be **fast**.

-  How fast? Note that the source may be interlaced, and someone may have thrown a framerate doubler into the filter chain... this means that for a 60i signal, the entire processing chain from decode to render has about 16ms per output frame.
-  Keep the required memory bandwidth down.

   -  Don't copy whole pictures unless you absolutely must. Moving pixels costs time.
   -  Allocate an output picture and render directly into it.
   -  If you need more than one pass, do in-place processing in the subsequent ones if possible.
   -  If your processing cannot avoid multiple passes, consider doing all passes for a picture line (or a few) at a time, instead of iterating over the whole picture separately for each pass. This will help to keep down the pressure on the CPU cache (since a few picture lines may fit in the L2 cache).

-  Consider writing the inner processing loops in vectorized inline assembly, such as MMX. This can often gain a factor of 2-8x in speed, depending on how much and what kind of processing your algorithm needs.

Some notes on video filter API
------------------------------

**Note**: See and for an example of everything discussed in this section. See also the `Deinterlace Hacker's Guide <Hacker_Guide/Video_Filters/Deinterlace>`__ for some further details.

The video filters use an object-based model. Calls to the filter will come with an instance pointer, so each filter instance can keep local data.

Usually, each filter defines its own internal data structure called **filter_sys_t**. It is completely private to the filter.

The API for video filters in VLC 1.2 is called **video filter2**. This requires the functions **Open()** and **Close()**.

The **Open()** function is expected to allocate private data (if any), and set up the filter structure with pointers to a frame processing function (**p_filter->pf_video_filter**, which is the actual filter), a flush function (**p_filter->pf_video_flush**), and a mouse event function (**p_filter->pf_video_mouse**). The relevant types are defined in .

The **Close()** function should deallocate private data.

See `How to write a module <Hacker_Guide/How_To_Write_a_Module>`__ for details about these functions in modules in general.

The mouse function should convert mouse events, from filter output format to filter input format (note the direction!). This is needed when doing scaling or geometrical distortions, so that the mouse position will map correctly. See for the definition and **Mouse()** in for an example. If you do not need to remap mouse events, you can leave **p_filter->pf_video_mouse** as **NULL**.

Filter work (frame processing function)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The frame processing function takes a frame as input (**picture_t\***, ), and optionally outputs one or more frames (**picture_t\***) as a linked list. The usual case is one frame in, one frame out, but this is not a requirement. (See framerate doublers and IVTC in the `deinterlace <deinterlace>`__ module for counterexamples.)

If you do not wish to output a frame at a particular call to your processing function, you can return **NULL**. If you wish to output several, make a linked list by using the **p_next** member of **picture_t**.

You don't have to necessarily output the *same* frame (after processing) that just came in. You can keep a private input frame history in your **filter_sys_t**, pick the base frame for your output from that, and adjust the PTSs (presentation timestamps, member **date** in **picture_t**) of your output as you deem necessary. The deinterlacer provides an example of how to do this.

Note however that there may be other filters in the chain that already set up a frame offset; this leaves less time (until the designated PTS) for the rest of the filters to do their processing.

The input picture coming in to the processing function is considered as owned by the processing function, and should be released before returning. To do this, use

::

   picture_Release( p_inpic );

Frame allocation
~~~~~~~~~~~~~~~~

Be sure to allocate your output pictures using

::

   picture_t *p_outpic = filter_NewPicture( p_filter );

This function requests a new picture from the private pool (see ). This is very important! Be aware that pictures created like

::

   picture_t *p_temp = picture_NewFromFormat( &p_input_pic->format );

lack a shared memory context (in Linux; or the equivalent in other OS), and thus cannot be passed to the video output logic. If your filter attempts to do so, VLC will crash.

If you need temporary pictures, you can allocate those using **picture_NewFromFormat()**, but remember to *always create output pictures using*\ **filter_NewPicture()**. Here an *output picture* is defined as a picture which goes out from the filter to the caller.

There is a limit to the number of simultaneous picture slots available in the private pool. Currently () this is 3 pictures for the filter layer. See the constant **private_picture** in . If you try to allocate more output pictures than this (during a single processing call), the allocation will fail.

Notes
~~~~~

-  In VLC 1.2, the video format (resolution, chroma) never changes on the fly. The whole filter chain is **Close()**\ d and then **Open()**\ ed again if the format changes.

-  Note that it *is* allowed to flush the filter without closing it. This actually happens under some circumstances, so *don't deallocate stuff in your flush function*. Rather, allocate dynamic resources in **Open()**, and deallocate them in **Close()** (or in private functions called from those). See `How to write a module <Hacker_Guide/How_To_Write_a_Module>`__.

-  Supported input and output formats are decided by each filter. The usual thing is to support `YUV <YUV>`__ formats, e.g. `I420 <I420>`__, `J420 <J420>`__, `YV12 <YV12>`__, `I422 <I422>`__ and `J422 <J422>`__. See . The most important ones to support are `I420 <I420>`__ and `I422 <I422>`__.

Pitch, visible pitch, planes et al.
-----------------------------------

Pitch and visible pitch
~~~~~~~~~~~~~~~~~~~~~~~

Important to know:

-  i_pitch = number of (macro)pixels on one line
-  i_visible_pitch = number of (macro)pixels on one line, adjusted for memory alignment constraints etc. (see below)

Note that the pitches may be different for each plane, and indeed in YUV formats the luma (**Y_PLANE**) and chroma (**U_PLANE**, **V_PLANE**) have different pitches due to chroma subsampling. (In 4:2:0 formats, the number of lines differs, too.)

Pitches also tend to slightly differ depending on how the picture was allocated, even if the visible size is the same. The input picture to the filter may have one pitch, temporary pictures (**picture_NewFromFormat()**) another, and output pictures (**filter_NewPicture()**) yet another.

*Be sure to always use the correct pitch when you handle the pixels of a picture.* That is, always use the **i_pitch** member of the actual **plane_t** you are working on.

If you absolutely need matching pitches (e.g. if you are glueing in processing code from another GPL-compatible project which assumes this and you don't want to rewrite it...), consider making temporary copies with **picture_NewFromFormat()**. See (the history mechanism pp_history[]) and (its usage) for an example.

If you are processing pixels from one picture to another, the safe thing to do is to take the smallest **i_visible_pitch**, and loop from x = 0 until the visible pitch has been reached, but use the individual **i_pitch**\ es for computing the pixel locations. See for examples.

Video_format_t vs. Plane_t
~~~~~~~~~~~~~~~~~~~~~~~~~~

In **video_format_t**, the **i_visible_width** and **i_visible_height** members go with **i_x_offset** and **i_y_offset**, but they are not related to **plane_t::i_visible_\***.

The **plane_t::i_visible_\*** fields are there to know which part of the memory planes can at most be displayed. Usually these are different from the whole surface due to memory alignment constraints (like mod 16 for SSE2 or to be aligned on a macroblock). Those values are decided when the picture is allocated and they usually don't change for a given picture pointer (but they can change, like in direct3d buffers).

The **video_format_t:i_visible_width/height** and **i_x/y_offset** are more a 'hint' regarding what will be actually displayed. A filter should update **filter_t::fmt_out** if needed to ensure that the allocated pictures get the right value. A filter should, however, not limit its processing to this area, because VLC supports dynamic cropping.

Thus, the correct thing to do in a filter is to process the whole picture area, or at least the first i_visible_\* lines and pixels *according to the*\ **plane_t**\ *\ s*. Filters do not need to care about margin positioning or that there even exists such a thing as margins.

About creating and merging pictures
-----------------------------------

This section talks about how to create filters which create and merge a picture onto the top of the already existing video.

What is the difference between picture_t and subpicture_t?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A **picture_t** is a full image, typically a decoded video frame.

A **subpicture_t** is an element (to be exact, a list of elements) which can be overlayed on top of an image. Two types of elements exist: text and images. Text elements are rendered by the VLC core before overlay.

How to create a picture and merge it with the existing picture?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Code-wise the simplest way is to create a video filter of type **subpicture source** (in VLC 2.0). The task of a **subpicture source** is to create a **subpicture_t**, and then let the VLC core deal with blending it on top of the video stream.

Another way is to create a **picture_t** (e.g. with **picture_NewFromFormat()**) and do the blending yourself. See below.

*Note*: in versions of VLC prior to 2.0 (version 1.1 and below), **subpicture sources** were called **subpicture filters**. This video filter type has been renamed in order to allow for the creation of actual **subpicture filters**, which edit (i.e. filter) existing **subpicture_t**\ s.

What is the simplest example I can look at for writing a filter that does this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Such filters can be found in and match the capability **sub source**. Noteworthy examples include:

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/video_filter/logo.c}}

   : overlay an image on top of the video. Note that this is also implemented as a **video filter2** which directly edits the **picture_t**. So that might not be the simplest source to look at. If you wish to take this approach, see also the `deinterlace filter <Hacker_Guide/Video_Filters/Deinterlace>`__, if you need inline assembler optimized 50/50 blending.

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/video_filter/marq.c}}

   : overlay text on top of the video.

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/video_filter/rss.c}}

   : overlay text from an RSS stream on top of the video. This one also includes picture elements sometimes which makes it a good example to understand how composite **subpicture_t** elements can be used.

Disclaimer
----------

The information is mostly based on a few months' hacking on the deinterlacer, with some contributions from fenrir and dionoea.

Please add new relevant stuff to this page as needed.

.. raw:: mediawiki

   {{Hacker_Guide}}
