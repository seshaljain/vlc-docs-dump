{{See alsoname=a52description=ATSC [[A/52]] (AC-3) audio
decoder|sc=none}}

{{Clear}}

There is a comment in the code:
   /*************************************************************************\***\*
   \* NOTA BENE: this module requires the linking against a library
   which is \* known to require licensing under the GNU General Public
   License version 2 \* (or later). Therefore, the result of compiling
   this module will normally \* be subject to the terms of that later
   license.**\ \***************************************************************************/

== Options == {{Option value=boolean description=Dynamic range
compression makes the loud sounds softer, and the soft sounds louder, so
you can more easily listen to the stream in a noisy environment without
disturbing anyone. If you disable the dynamic range compression the
playback will be more adapted to a movie theater or a listening room }}

== Source code == \* {{VLCSourceFilemodules/packetizer/a52.c}}

{{Documentation}}
