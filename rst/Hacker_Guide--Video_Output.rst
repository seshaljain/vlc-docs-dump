{{Back to|Hacker Guide}} This page is about the video output layer ==
Data structures and main loop ==

Important data structures are defined under
{{VLCSourceFolderinclude/vlc_picture.h}},
{{VLCSourceFileinclude/vlc_vout.h}}.

=== picture_t ===

The main data structure is ''picture_t'', which describes everything a
video decoder thread needs. Please, refer to those files for more
information. Typically, p_data will be a pointer to [[YUV]] planar
picture.

=== subpicture_t and SPU ===

Note also the ''subpicture_t'' structure. In fact the VLC SPU
(''SubPicture Unit'') decoder only parses the SPU header, and converts
the SPU graphical data to an internal format which can be rendered much
faster. So a part of the "actual" SPU decoder lies in
{{VLCSourceFile|src/video_output/vout_subpictures.c}}.

=== vout_thread_t ===

The ''vout_thread_t'' structure is much more complex, but you needn't
understand everything. Basically the video output thread manages a heap
of pictures and subpictures (5 by default). Every picture has a status
(displayed, destroyed, empty...) and eventually a presentation time. The
main job of the video output is an infinite loop to&nbsp;: [this is
subject to change in the near future]

#Find the next picture to display in the heap. #Find the current
subpicture to display. #Render the picture (if the video output plug-in
doesn't support YUV overlay). Rendering will call an optimized YUV
plug-in, which will also do the scaling, add subtitles and an optional
picture information field. #Sleep until the specified date. #Display the
picture (plug-in function). For outputs which display RGB data, it is
often accomplished with a buffer switching. p_vout-&gt;p_buffer is an
array of two buffers where the YUV transform takes place, and
p_vout-&gt;i_buffer_index indicates the currently displayed buffer.
#Manage events.

== Methods used by video decoders ==

The video output exports a bunch of functions so that decoders can send
their decoded data. The most important function is vout_CreatePicture
which allocates the picture buffer to the size indicated by the video
decoder. It then just needs to feed (void \*) p_picture-&gt;p_data with
the decoded data, and call vout_DisplayPicture and vout_DatePicture upon
necessary.

{{fnReturns an allocated picture buffer. i_type will be for instance
YUV_420_PICTURE, and i_width and i_height are in pixels.}}

{{Warning|If no picture is available in the heap, vout_CreatePicture
will return NULL.}}

{{fnIncreases the refcount of the picture, so that it doesn't get
accidently freed while the decoder still needs it. For instance, an I or
P picture can still be needed after displaying to decode interleaved B
pictures.}} {{fnDecreases the refcount of the picture. An unlink must be
done for every link previously made.}} {{fnGives the picture a
presentation date. You can start working on a picture before knowing
precisely at what time it will be displayed. For instance to date an I
or P picture, you must wait until you have decoded all previous B
pictures (which are indeed placed after - decoding order&nbsp;!=
presentation order). }} {{fnTells the video output that a picture has
been completely decoded and is ready to be rendered. It can be called
before or after vout_DatePicture. }} {{fnMarks the picture as empty
(useful in case of a stream parsing error). }} {{fnMarks the subpicture
as empty.}}

== How to write a video output plug-in ==

A video output takes care of the system calls to display the pictures
and manage the output window. For the most minimalistic framework, look
at vmem.c, which just "renders" to dummy internal memory. From there, go
on to directfb.c and svgalib.c, and finally go for x11 and windows.

<br> Video outputs reside in the
{{VLCSourceFolder|modules/video_output}} directory.
modules/video_output/x11/xcommon.c gives example of functions you must
write&nbsp;:

{{fnvoid Deactivate ( vlc_object_t \*p_this )|Called to destroy the
module: Deactivate needs to free all allocated memory and destroys
cleanly the video output thread}}

The callback functions you need to implement are (callback name,
function prototype)&nbsp;:

{{fnCalled at the beginning of the output thread and each time the
window is resized, it creates a buffer of output pictures }}
{{fnDestroys output pictures created by InitVideo }} {{fnManage X11
events, and handle window resizing }} {{fnOptional (set
p_vout-&gt;pf_render to NULL if not implemented); Used when pictures
from the decoder need to be rendered before display }} {{fnDoes the
actual display of pictures onto screen }} {{fnControl facility for the
video output}}

== How to write a YUV plug-in ==

Look at the C source plugins/yuv/transforms_yuv.c. You need to redefine
just the same transformations. Basically, it is a matrix multiply
operation. Good luck.

{{Hacker_Guide}}

[[Category:Pages to check]]
