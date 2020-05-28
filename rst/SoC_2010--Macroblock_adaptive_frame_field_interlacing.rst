{{SoCProjectstudent=[[User:Simonhorlickmentor=[[User:Dark_Shikari|Jason
Garret-Glaser]]}}

== Abstract ==

Currently x264 supports interlaced encoding with MBAFF frame structure
where each macroblock is encoded as interlaced. This project will
implement full adaptive interlacing support where macroblocks are
encoded as progressive or interlaced depending on their content.

== Milestones ==

This list is ''very'' preliminary.

{\| class="wikitable" ! Status !! Deadline !! Description - \|\| July 12
\|\| Mid term evaluations - \|\| August 9 \|\| Suggested "pencils down"
date - \|\| August 16 \|\| Firm "pencils down" date }

== Timeline ==

This schedule is preliminary.

{\| class="wikitable" ! Status !! Date !! Period !! Description Done
\|\| April 12 - April 18 \|\| Qualification \|\| Intra only encoding In
progress \|\| May 31 - June 6 \|\| \|\| Reading and planning In progress
\|\| June 7 - June 13 \|\| Week 1 \|\| Modify cache_load for motion
vector/reference frame information. Hpel filtering. Not started \|\|
June 14 - June 20 \|\| Week 2 \|\| Cabac Not started \|\| June 21 - June
27 \|\| Week 3 \|\| B-frames Not started \|\| June 28 - July 4 \|\| Week
4 \|\| B-frames Not started \|\| July 5 - July 11 \|\| Week 5 \|\|
Deblocking Not started \|\| July 12 - July 18 \|\| Week 6 \|\|
Deblocking Not started \|\| July 19 - July 25 \|\| Week 7 \|\| Initial
MBAFF decision Not started \|\| July 26 - August 1 \|\| Week 8 \|\|
Modify things that assume interlaced/progressive (AQ) Not started \|\|
August 2 - August 8 \|\| Week 9 \|\| Better MBAFF decision Not started
\|\| August 9 - August 15 \|\| Week 10 \|\| Finishing \|}

== Repository ==

[http://github.com/simonhorlick/x264-mbaff
http://github.com/simonhorlick/x264-mbaff]
