.. raw:: mediawiki

   {{Outdated}}

.. raw:: mediawiki

   {{RightMenu|Documentation TOC}}

VLC includes a system of *filters* that allow you to modify the audio and video.

Deinterlacement and Post Processing
-----------------------------------

VLC is able to `deinterlace <deinterlace>`__ a video stream using different deinterlacement methods. Deinterlacement can be enabled in the *Video* menu, *Deinterlacement* menu item. The *Blend* methods gives the best results in most cases. The *discard* method is a less resource consuming alternative, although its results may be slightly compromised.

On some particular streams (`MPEG 4 <MPEG_4>`__, `DivX <DivX>`__, `Xvid <Xvid>`__, `Sorenson <Sorenson_Video>`__, etc.), some additional image filtering can be applied to the video before display, improving its quality in some cases. This can be enabled by using the *Post processing* menu item in *Video*. Different levels of post processing can be chosen here. A higher level means more filtering.

Video filters
-------------

Summary
~~~~~~~

VLC features several filters able to change the video (distortion, brightness adjustment, motion blurring, etc.).

In Windows and Linux, the user must go to the *Effects and Filters* in the *Tools* menu item. A dialogue box entitled "Adjustments and Effects" will appear.

.. figure:: Video_effects_-_essential,_with_image_adjust_selected.png
   :alt: Video_effects_-_essential,_with_image_adjust_selected.png
   :width: 600px

   Video_effects_-_essential,_with_image_adjust_selected.png

In `macOS <macOS>`__ you can enable these filters through the *Extended Controls panel*. Click on the triangle next to *Video filters* to select your filters or expand the *Adjust Image* section to change the contrast, hue, etc.

.. figure:: intf-osx-vfilters.jpg
   :alt: Filter dialogue box as it appears in macOS interface

   Filter dialogue box as it appears in macOS interface

iOS: |Filter dialogue box as it appears in iOS devices|

Example of combined effects on a video:

.. figure:: VLC-combined-effects.png
   :alt: VLC-combined-effects.png

   VLC-combined-effects.png

Rotate
~~~~~~

You can easily rotate a video. Open the *Effects and Filters* dialog, in the *Tools menu*

.. figure:: Bbb_rotate.png
   :alt: Bbb_rotate.png

   Bbb_rotate.png

Select the *Video Effects* tab, then the *Geometry* one.

Check the *Transform* checkbox to use rotation presets (90°, 180°, 270°) or check the *Rotate* checkbox to manually select the angle you wish to apply.

.. figure:: Video_effects_-_geometry,_with_rotate_selected.png
   :alt: Video_effects_-_geometry,_with_rotate_selected.png

   Video_effects_-_geometry,_with_rotate_selected.png

Audio filters
-------------

Equalizer
~~~~~~~~~

.. raw:: mediawiki

   {{Wikipedia|Equalization (audio)}}

VLC features a 10-band graphical equalizer, a device used to alter the relative frequencies of audio (e.g. for a bass boost). You can display it by activating the advanced GUI on `wxWidgets <wxWidgets>`__ or by clicking the *Equalizer* button on the macOS interface. The following image is the interface of the audio equalizer in the Windows and GNU/Linux interface.

.. figure:: Audio_Filters.PNG
   :alt: Equalizer dialogue box as it appears in wxWidgets for Windows and Linux

   Equalizer dialogue box as it appears in wxWidgets for Windows and Linux

The equalizer in the macOS interface

.. figure:: Intf-osx-equalizer.jpg
   :alt: Intf-osx-equalizer.jpg

   Intf-osx-equalizer.jpg

.. figure:: VLC_for_iOS_Equalizer.png
   :alt: VLC_for_iOS_Equalizer.png

   VLC_for_iOS_Equalizer.png

Presets are available in all of these dialog boxes.

Other audio filters
~~~~~~~~~~~~~~~~~~~

At the moment, VLC features two other audio filters: a volume normalizer and a filter providing sound spatialization with a headphone. They can be enabled in the *Effects and Filters* menu item in the *Tools* tab of the Windows and GNU/Linux interface and in the Audio section of the Extended Controls panel of the macOS interface.

For better control, you need to go to the preferences. To select the filters to be enabled, go to *Audio*, then to *Filters*. In the "audio filters" box, enter the names of the filters to enable, separated by commas. Valid names are "equalizer", "normvol" and "headphone".

If you want to tune the behavior of these filters, go to *Audio, Filters, [your filter]*. The equalizer and headphone filters can be tuned.

.. raw:: mediawiki

   {{Documentation}}

.. |Filter dialogue box as it appears in iOS devices| image:: VLC_for_iOS_Video_Filters.png

