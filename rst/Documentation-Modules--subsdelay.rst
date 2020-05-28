{{Moduletype=Video sub-filterdescription=Change [[subtitles]] delay}}

The subsdelay filter can help slow readers to keep up with the
subtitles.<br> It extends the subtitles duration without changing their
original appearance time, so the subtitles are piled up on the video. To
help keep track of the appearance order, existing subtitles gets more
transparent as new subtitles arrive.

The subtitles duration factor [[VLC HowTo/Adjust subtitle delay|is
configurable through the synchronization dialog]]. Other options can be
set through the [[preferences]] (''show all settings'' → Video →
Subtitles/OSD → Subsdelay).

== Options == {{Option value=integer { 0, 1, 2 }]] description=Delay
calculation mode }} {{Option value=float max=20.0 description=The delay
calculation parameter }} {{Option value=integer max=4
description=Maximum number of subtitles allowed at the same time }}
{{Option value=integer max=255 description=Alpha value of the earliest
subtitle, where 0 is fully transparent and 255 is fully
opaque.<br>Subtitles alpha is somewhere between fully opaque and this
value according to the appearance order and the maximum overlapping
allowed }}

=== Overlap fix === These rules help fixing some "flickering" effects
caused by the overlapping. They are applied after the initial delay is
calculated in the following order: {{Option value=integer
description=Minimum time (in milliseconds) that a subtitle should stay
after its predecessor has disappeared (subtitle delay will be extended
to meet this requirement) }} {{Option value=integer description=Minimum
time (in milliseconds) between subtitle disappearance and a newer
subtitle appearance (earlier subtitle delay will be extended to fill the
gap) }} {{Option value=integer description=Minimum time (in
milliseconds) that a subtitle should stay after a newer subtitle has
appeared (earlier subtitle delay will be shortened to avoid the overlap)
}}

== Examples == Example command line use '''(VLC 1.2.0 and above)''' : %
'''vlc --sub-filter subsdelay --subsdelay-mode 1 --subsdelay-factor 2
--subsdelay-overlap 3''' :Multiply subtitles duration by 2, up to 3
subtitles can be overlapped at a given time.

   % '''vlc --sub-filter subsdelay --subsdelay-mode 0 --subsdelay-factor
   0 --subsdelay-overlap 1 --subsdelay-min-stop-start 0'''

:Don't change subtitles duration but fix any existing overlaps.

== Source code == \* {{VLCSourceFile|modules/spu/subsdelay.c}}

== Appendix == <span id="appendix_subsdelay-mode"></span> For option
--[[#subsdelay-mode|subsdelay-mode]]: ;0:<code>new_delay =
original_delay + factor</code><br>Absolute delay - add an absolute delay
to each subtitle.<br>In this mode the factor represents seconds
;1:<code>new_delay = original_delay \* factor</code><br>Relative to
source delay - multiply subtitles delay. ;2:<code>new_delay =
f(original_text, factor)</code><br>Relative to source content -
determine subtitles delay from its content.<br>The delay calculation is
based on the number and length of the words in the subtitle.<br>This
mode could only work for plain subtitles sources (like [[SubRip]],
[[MicroDVD]], etc), for other formats the "relative to source delay"
mode is used instead

{{Documentation}}

[[Category:Subtitles]]
