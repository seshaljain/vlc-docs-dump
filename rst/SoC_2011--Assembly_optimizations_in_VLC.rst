{{SoCProjectstudent=[[User:Bizonmentor=[[User:j-b|Jean-Baptiste
Kempf]]}}

= Repository =

http://git.videolan.org/?p=vlc/vlc-bizon.git;a=summary

= Abstract =

The main goal is to optimize video and audio filters of VLC, add SIMD
x86 instruction using functions and clean their C code up. Next step is
profiling of main VLC.

Optimization of functions that process huge amount of data with the same
algorithm at the same time with SIMD instructions, so better performance
can be achieved. Main focus will be on video and audio filters of VLC
and after these are done, profiling of other parts of the application
will be the next step.

Side effect of the work will be clean up and improvement of algorithms
used (same as in sepia.c - change from RGB to YUV, to not lose time
converting the format).

= Progress =

=== Weeks 1 and 2 (May 23 - June 5) ===

Exams, no activity on the project

=== Week 3 (June 6 - 12) ===

Acclimatization, starting work on YUV to RGB converting function from
filter_picture.h to use it in plugins using it. I experienced few minor
problems, which unfortunately ended up in me searching for bug where it
was not.

At the moment (as of 13th of June), I'm working on posterization filter.
As SSE doesn't provide integer division, I have to find solution which
will really speed up the computation.

=== Week 4 (June 13 - 19) ===

Working on posterization filter, YUV <-> RGB function were written to be
used in other modules. Code isn't very clear, definitely not to be
commited to the main repo.

=== Week 5 (June 20 - 26) ===

Started working on adjust filter. Work was slowed down by the fact, I
had to leave home to arrange some stuff about school (college room
etc.). I have cleared my work that has been done in sepia filter in
spring to be more clear, MUCH faster and mainly - using SSE2 instead of
SSE4.1

=== Week 6 (June 27 - July 3) ===

Finished working on adjust and cleaned posterize. After showing the code
on the IRC channel and discussion with j-b and Dark_Shikari (which was
really helping), I decided to rewrite them in a much better way, which I
couldn't see before.

=== Week 7 (July 4 - 10) ===

Currently in progress.

= Additional information =

May 9 - June 10 are exams on our school, so I won't start coding exactly
at the start of the coding period. I'll keep you updated on when I have
finished.<br>
