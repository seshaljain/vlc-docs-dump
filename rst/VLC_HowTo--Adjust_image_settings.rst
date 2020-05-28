.. raw:: mediawiki

   {{howto|adjust image settings including brightness and contrast|nosort=yes}}

.. raw:: mediawiki

   {{see also|Documentation:Video and Audio Filters}}

Graphical
---------

Graphical approaches are the easiest but also the most variable because you have to look in different places depending on your `interface <interface>`__. What this approach will do is globally change the hue, brightness, contrast, saturation or gamma for *every* video you play in VLC, perhaps for color-correction purposes. If you want to play a single video with different image settings, you should look at the `command-line <command-line>`__ approach.

Older versions of VLC required different steps (VLC versions <= 0.9.0 used `wxWidgets Interface <wxWidgets_Interface>`__). **Modern VLC installations for Windows and Linux use**\ `Qt <Qt_interface>`__\ **, Mac installations use the OS X interface.**

Qt Interface
~~~~~~~~~~~~

#. In the menu bar, select "Tools" and then "Effects and Filters".
#. Select the "Video Effects" tab and then "Essential" subtab.
#. Tick the "Image adjust" checkbox and move the slider for the setting you want to change.
#. Hue, Brightness, Contrast, Saturation, and Gamma may be adjusted.

Changes take effect immediately for every video.

OS X Interface
~~~~~~~~~~~~~~

#. Go to the "Extended controls" panel.
#. Select the "Video" section and then "Adjust Image" subtab.
#. Tick the "Enable" checkbox and move the slider for the setting you want to change.
#. Hue, Contrast, Brightness, Saturation, Gamma, Opaqueness may be adjusted.

Command-line
------------

A command-line approach will run VLC with adjusted hue, brightness, contrast, saturation or gamma for *one session* (the adjustments will not be preserved later). To learn how to get a command-line, see `command-line interface <command-line_interface>`__.

The module you will be working with is `adjust <Documentation:Modules/adjust>`__. As given by ``vlc --module adjust``:

::

         --contrast <float [0.000000 .. 2.000000]> 
                                    Image contrast (0-2)
         --brightness <float [0.000000 .. 2.000000]> 
                                    Image brightness (0-2)
         --hue <float [-180.000000 .. 180.000000]> 
                                    Image hue (-180..180)
         --saturation <float [0.000000 .. 3.000000]> 
                                    Image saturation (0-3)
         --gamma <float [0.010000 .. 10.000000]> 
                                    Image gamma (0-10)
         --brightness-threshold, --no-brightness-threshold 
                                    Brightness threshold
                                    (default disabled)

The defaults are 1.0 for contrast and brightness, 0 for hue, 1.5 for saturation, 1 for gamma.

You can make a video (or still image) 10% brighter with:

``vlc --video-filter adjust --brightness 1.1 ``\ 

and make a video (or still image) black-and-white with:

``vlc --video-filter adjust --saturation 0 ``\ 

And this works too:

| ``vlc --brightness 1.1 ``\ 
| ``vlc --saturation 0 ``\ 

Permanent changes
~~~~~~~~~~~~~~~~~

You cannot save your preference for adjusted image settings with VLC (VLC doesn't seem to have any field that "remembers" your preferences).

You can, potentially, stream the video through a filter using the above method to an output file, and overwrite the original.

In other words, to make foo.ogv 10% brighter you adjust foo.ogv:

``vlc --video-filter adjust --brightness 1.1 foo.ogv``

And then save the result into foo.ogv.tmp (sorry, I don't have a command line for this), saving over foo.ogv.

Now when you play foo.ogv the video will be brighter.

.. raw:: mediawiki

   {{VSG}}

.. raw:: mediawiki

   {{DEFAULTSORT:Image}}
