{{SoCProjectstudent=[[User:Irockmentor=[[User:Holger|Holger Lubitz]]}}

== Abstract ==

The primary goal for this project is to prepare the code base of x264
for encoding H.264 video with user defined sample depths. This will
involve templating the encoder and migrating existing C code for use
with higher sample depths.

A lot of optimizations are done with assembly, and will thus also need
to be migrated. The secondary goal for this project is therefore to
identify new assembly code to be written.

== Milestones ==

{\| class="wikitable" ! Status !! Deadline !! Description Done \|\| May
30 \|\| 16-bit infrastructure ready for testing No problems encountered
so far \|\| June 6 \|\| Encoding with 16-bit infrastructure produce same
results as 8-bit infrastructure. \|}

== Timeline ==

This schedule is preliminary.

{\| class="wikitable" ! Status !! Date !! Period !! Description Done
\|\| May 17 - May 23 \|\| Week 1 \|\| Identify C code that should be
templated. Done \|\| May 24 - May 30 \|\| Week 2 \|\| Start templating
the encoder for 16-bit infrastructure. In progress \|\| May 31 - June 6
\|\| Week 3 \|\| Test templated encoder. Identify C code that need
modification to support higher sample depth. Not started \|\| June 7 -
June 13 \|\| Week 4 \|\| Start modifying the encoder to support higher
sample depth. Not started \|\| June 14 - June 20 \|\| Week 5 \|\|
Continue work with encoder. Not started \|\| June 21 - June 27 \|\| Week
6 \|\| Continue work with encoder. Not started \|\| June 28 - July 4
\|\| \|\| Vacation / extra time Not started \|\| July 5 - July 11 \|\|
Week 7 \|\| Test encoder with higher sample depths. Not started \|\|
July 12 - July 18 \|\| Week 8 \|\| Fix issues encountered during
testing. Not started \|\| July 19 - July 25 \|\| Week 9 \|\| Modify
build chain to allow compilation for higher sample depth. Add options to
set sample rate. Not started \|\| July 26 - August 1 \|\| Week 10 \|\|
Identify assembly code that needs modification to support higher sample
depth. \|}

== Repository ==

-  http://github.com/irock/x264-high-bit-encoding/tree/high-bit-encoding

How to test the current code:

   $ git clone git://github.com/irock/x264-high-bit-encoding.git $ cd
   x264-high-bit-encoding $ git checkout high-bit-encoding $ ./configure
   --disable-asm --enable-16-bit $ make
