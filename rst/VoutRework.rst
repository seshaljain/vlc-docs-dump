Draft design for the vout rework effort
=======================================

`VoutReworkUserRequirements <VoutReworkUserRequirements>`__

`VoutReworkOrganization <VoutReworkOrganization>`__

Overall architecture
--------------------

The current system (one vout_thread_t per window) will be splitted

-  vout_core that manages all vout instances and windows. also takes care of vout_filters (wall, clone)
-  vout_window object per displayed window. provides a "region for vout_renderers" to draw in.
-  vout_render that renders the actual video, text and image

OSD and subpictures
-------------------

We need to be able to display them either:

-  At video resolution, for DVD subtitles (on the "render")
-  At screen resolution (text subtitles, OSD control) (on the "output")

   -  This will also allow us to draw subtitles outside of the video rendering
   -  Probably needs specific code for each vout

At the moment, subpictures have very annoying timing constraints. subpictures should be timed either on the stream (for subpictures) or absolute, from the vout_core (for subfilters)

We should create two seperate systems. a vout_render level system which basically draws extra things into the region provided by vout_window. This can be both text, images and possibly even video. Material should be drawn in the resolution of the provided region, instead of the resolution of the main video. It should be seperate from the spu streams. However it should be possible to feed SPU based material to the vout_render system instead of the normal SPU stream pipeline and vice versa.

Comments from Gibalou: I agree overall but be aware that rendering on the vout window can be quite tricky. For instance on platforms which only support 1 overlay (already used by the video), we will have to constantly refresh the OSD (to handle resizing / refreshing of the vout window). For this reason I would suggest we keep this feature as simple as possible and only make it support displaying of subpictures (subpicture_t/subpicture_region_t).

Filters
-------

Make a clean separation:

-  vout_filters should not be the same as real vouts anymore (will come from the split)

Comments from Gibalou: they don't really need to be changed since they alreday don't create any window.

-  pic_filter

   -  Currently called video_filter2, should be renamed
   -  Works on a single pic buffer
   -  Can be streamed

Comments from Gibalou: video_filter2 is not just about 1->1 picture conversion. It is actually designed to work on video and could for instance allow for temporal de-interlacing, inverse telecine, etc... So it really is a video_filter and not merely a pic_filter.

Two big areas of work to be able to integrate video_filters into the vout core will be:

- Proper support for direct-rendering. Some filters won't actually modify the video frames directly (eg. auto-cropping) or will do in-place modifications so they will need to be able to allocate their pictures from the next filter in the chain and pass it on to the previous filter when requested. In short, picture allocation needs to be reviewed so it is done in an optimized way.

- Dynamic modification of the filter chain. Again this is tricky because the decoder (which does direct-rendering) will be using pictures allocated from the filter. If this filter changes or is removed, we will need a way replace the pictures in use by the decoder. That could be done by having a mechanism that progressively replaces the picture buffers used by the decoder by indirect buffers and when non of the direct buffers are in use anymore then we switch the filter. That will be a lot better then the current way of stopping/starting the decoder.

-  subpicture_filter

Modularization of specific calls
--------------------------------

For many of the operations we need, OS specific calls exist (OpenGL, Quartz, DirectX). This should be modularized, with a native "C" fallback. OS specific calls are often faster.

There should be only one module for all the calls, if possible. The best module would be loaded by the vout_core singleton, and function pointers set up for each of the functions we need. perhaps a vout_Control type could take care of all these things in the vout_renderer. paramaters that should be handled this way are at least: alignment, AR, crop, pad

Comment from Gibalou: AR, crop (and soon pad) are already implemented in the vouts (see below). Alignment is also already supported and is only about placing the vout subwindow (frame or whatever you call it) into the main window.

Misc
----

-  Vout plugins (that provide vout windows) should allow reusing a vout by reusing it. This would much improve the experience)
-  Vout windows must have a flag to tell if they are "main" or "helper" (audio visualization, ...). Helper vouts should get no OSD (if another vout is present) and should not "steal" the accelerated vout"
-  cropping and padding (do at OS level, but provide a core call to set it up and configure) **=> Done**
-  vout windows should indicate if they are on a 4:3 or 16:9 screen (we can calculate this trough resolution). Note that this can change, because a window could be moved from one screen to another. Use callbacks. '''=> Why would you want to know the AR of the screen ? Aren't you confusing with the PAR ? This information could be used by the core to facilitate selection of cropping/padding etc for instance 4:3 display on a 16:9 screen. you might want to crop the top/bottom or stretch the view by default. Especially when you are also gonna add padding for subtitle rendering for instance, this information might become useful.
-  better hotkeys integration: need hotkey module redesign to act on selected vout and relevant input instead of the first we find
-  pseudo-hotkeys: ability to move the window by clicking on the video and dragging it (in particular for borderless windows).
-  interaction between interfaces and embedded vouts: if the vout window is moved and/or resized (due to a hotkey), how to notify the interface (skins engine in particular)?

'''

cropping padding functionality
------------------------------

-  add padding in order to display subs under the video. what if we have a 4:3 movie in a 4:3 screen? do we create blackbars to the left and right sides? do we crop a part of the video ???
-  4:3 cropping to 16:9 (in order to remove blackbars at top and bottom
-  16:9 cropping to 4:3 (in order to remove blackbars left and right side)
-  4:3 to 16:9 (AR correction)
-  16:9 to 4:3 (AR correction)
-  AR Freeform
-  Support Moviescreen AR? (2.39:1 or 1.85:1)
-  More info on AR: http://en.wikipedia.org/wiki/Aspect_ratio_(image)
-  If we let the window provider pass/calculate the AR of the display, then we can even do some of this automatically if the uses desires.
-  cropping should have priority over padding. Then we can first crop blackbars, then add padding for subs.
-  coordinate specified cropping and padding

Comment from Gibalou: AR / Cropping (and soon Padding) has already been reworked and is now handled directly in the vout module (makes sense since cropping and resizing are supported by most sane graphic APIs). All this is controled from the core by setting the relevant parameters in vout_format_t. Now, what could be done is to add extra logic (eg. in video_filters) to do some clever things like auto-cropping, etc... All they need to do is to modify video_format_t to change the final cropping/padding/AR.

`Category:Dev Discussions <Category:Dev_Discussions>`__
