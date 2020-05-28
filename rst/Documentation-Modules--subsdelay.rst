.. raw:: mediawiki

   {{Module|name=subsdelay|type=Video sub-filter|first_version=1.2.0|description=Change [[subtitles]] delay}}

| The subsdelay filter can help slow readers to keep up with the subtitles.
| It extends the subtitles duration without changing their original appearance time, so the subtitles are piled up on the video. To help keep track of the appearance order, existing subtitles gets more transparent as new subtitles arrive.

The subtitles duration factor `is configurable through the synchronization dialog <VLC_HowTo/Adjust_subtitle_delay>`__. Other options can be set through the `preferences <preferences>`__ (*show all settings* → Video → Subtitles/OSD → Subsdelay).

Options
-------

.. raw:: mediawiki

   {{Option
   |name=subsdelay-mode<span id="subsdelay-mode"></span>
   |value=integer
   |select=[[#appendix_subsdelay-mode|{ 0, 1, 2 }]]
   |default=1
   |description=Delay calculation mode
   }}

.. raw:: mediawiki

   {{Option
   |name=subsdelay-factor
   |value=float
   |min=0.0
   |max=20.0
   |default=2.0
   |description=The delay calculation parameter
   }}

.. raw:: mediawiki

   {{Option
   |name=subsdelay-overlap
   |value=integer
   |min=1
   |max=4
   |default=3
   |description=Maximum number of subtitles allowed at the same time
   }}

.. raw:: mediawiki

   {{Option
   |name=subsdelay-min-alpha
   |value=integer
   |min=0
   |max=255
   |default=70
   |description=Alpha value of the earliest subtitle, where 0 is fully transparent and 255 is fully opaque.<br>Subtitles alpha is somewhere between fully opaque and this value according to the appearance order and the maximum overlapping allowed
   }}

Overlap fix
~~~~~~~~~~~

These rules help fixing some "flickering" effects caused by the overlapping. They are applied after the initial delay is calculated in the following order:

Examples
--------

Example command line use **(VLC 1.2.0 and above)** :

``% ``\ **``vlc``\ ````\ ``--sub-filter``\ ````\ ``subsdelay``\ ````\ ``--subsdelay-mode``\ ````\ ``1``\ ````\ ``--subsdelay-factor``\ ````\ ``2``\ ````\ ``--subsdelay-overlap``\ ````\ ``3``**

   Multiply subtitles duration by 2, up to 3 subtitles can be overlapped at a given time.

``% ``\ **``vlc``\ ````\ ``--sub-filter``\ ````\ ``subsdelay``\ ````\ ``--subsdelay-mode``\ ````\ ``0``\ ````\ ``--subsdelay-factor``\ ````\ ``0``\ ````\ ``--subsdelay-overlap``\ ````\ ``1``\ ````\ ``--subsdelay-min-stop-start``\ ````\ ``0``**

   Don't change subtitles duration but fix any existing overlaps.

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/spu/subsdelay.c}}

Appendix
--------

For option --`subsdelay-mode <#subsdelay-mode>`__:

0:\ ``new_delay = original_delay + factor``
Absolute delay - add an absolute delay to each subtitle.
In this mode the factor represents seconds
1:\ ``new_delay = original_delay * factor``
Relative to source delay - multiply subtitles delay.
2:\ ``new_delay = f(original_text, factor)``
Relative to source content - determine subtitles delay from its content.
The delay calculation is based on the number and length of the words in the subtitle.
This mode could only work for plain subtitles sources (like `SubRip <SubRip>`__, `MicroDVD <MicroDVD>`__, etc), for other formats the "relative to source delay" mode is used instead

.. raw:: mediawiki

   {{Documentation}}

`Category:Subtitles <Category:Subtitles>`__
