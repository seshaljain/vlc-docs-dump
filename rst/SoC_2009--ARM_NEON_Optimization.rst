.. raw:: mediawiki

   {{SoCProject|year=2009|student=David Conrad|mentor=Holger Lubitz}}

Abstract
--------

Formerly used primarily in PDAs and cellphones, ARM is starting to target netbooks and laptops with its new Cortex-A series of processors. One key feature of these new processors is the NEON SIMD unit, the use of which will massively boost the performance of many multimedia applications. This project will consist of writing NEON/ARMv6 SIMD assembly for all of the major DSP functions in x264, ideally speeding x264 up by over 4-5 times.

Goals
-----

=== ================================ =========== =====================================================================================================================================================================
No. Task Description                 Status      Comment
=== ================================ =========== =====================================================================================================================================================================
1   ARM framework                    Mostly Done Waiting on more info on CPUID emulation
2   SAD/SATD                         Done        Qualifying task
3   SSD                              Done       
4   Luma MC                          In progress get_ref_neon complete
5   Chroma MC                        In progress Ported ffmpeg's and the general case works, but not the special cases
6   (I)DCT                           Done        4x4 (I)DCT and 8x8 IDCT done, 8x8 DCT not started
7   (De)quant                        In Progress 4x4 quant done, rest not started
8   SSIM                             Done       
9   Zigzag                           In Progress 4x4 scan/sub frame done, rest in progress
10  Hadamard AC                      Done       
11  Intra Prediction                 In Progress Simpler functions done
12  sa8d                             Done       
13  pixel variance                   Done       
14  lowres_init                      Done       
15  hpel_filter                      Not Started
16  Loop Filter                      Not Started
17  intra sad/satd/sa8d              Not Started
18  Integral init                    Not Started
19  Denoise                          Not Started
20  Decimate score                   Not Started
21  Coeff last/level_run             Not Started
22  cabac                            Not Started
23  ARMv6 optimizations              In progress For smaller functions, write code using ARMv6's simd extensions. For instance, ARMv6 SAD width 4 is faster on Cortex-A8.
24  Cortex-A9 optimizations          In progress Primarily consists of running checkasm --bench on an A9, noting whether ARMv6 or NEON is faster, figuring out why, and ensuring that the faster function is selected.
25  gcc optimization                 Not Started Investigate what gcc produces for important C functions and attempt to optimize it for ARM
26  Performance Counter Optimization Not Started Utilize the ARMv7 performance counters to optimize stalls, cache usage, NEON->ARM data hazards, and more
=== ================================ =========== =====================================================================================================================================================================

Repository
----------

I'm currently using gitorious to publish my work `1 <http://gitorious.org/projects/x264-arm>`__

Timeline
--------

This is an estimation.

**March-April** Qualifying task, work on the more important (>5% in profiles) functions

**May** Final projects and exams

*' May 23*' Program Starts

*' May 23 - June 14*' Code

*' June 15 - June 21*' Vacation on Chincoteague

*' June 22 - July 12*' Code

*' July 13*' Mid Term deadline. Specific goals pending, but I'd like to have none of the functions without asm equivalents to be more than about 2% of common profiles. In other words, all the major functions would have been written in NEON ASM

*' July 13 - August 17*' Code

**August 17** Program end
