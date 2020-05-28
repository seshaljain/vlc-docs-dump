.. raw:: mediawiki

   {{SoCProject|year=2009|student=Dylan Yudaken|mentor=Jason Garrett-Glaser}}

Abstract
--------

x264 is a highly popular h264 encoder. It currently does not implement the entire spec of h264. Currently weighted P-frames are not used to assist in prediction. If implemented this would give huge benefits in cases where the scene fades or where there are flashes. I am proposing to implement an implementation of this that is good enough and fast enough to warrant inclusion in most video encodings.

Code
----

My patches (and codebase) are `here <http://repo.or.cz/w/x264/x264-p-frames.git?a=shortlog;h=refs/heads/gsoc>`__ for now, but they may soon move to videolan's server

Goals
-----

=== ========================================================================= =========== =========================================================================================
No. Task Description                                                          Status      Comment
=== ========================================================================= =========== =========================================================================================
1   Build weighting framework                                                 done        .
2   Brute Force Optimal Weights                                               done       
3   Try use these new weights for some interesting things to improve quality  done       
4   Find Optimal Weights in a fast way (probably based on the findings in 3.) done       
5   DSP Functions                                                             Done       
6   Try duplicating reference frames                                          Done       
7   Other weird uses                                                          done        Implemented a k-means cluster algorithm to find a number (k) of good weights and use them
8   Finish off small things                                                   Working     Todo: Finish multipass, cleanup k-means a bit
9   Optimize algorithms and test like crazy                                   Not started
10  Cleanup and code review                                                   Not started
=== ========================================================================= =========== =========================================================================================

Current Issues
~~~~~~~~~~~~~~

Timeline
--------

This is an estimation.

**March 20th or so - April 3** Qualifying task. Was a first attempt at goal 1.

**April 20** Students announce

**April 21 - May** Goal 1 redone better and acceptably.

**May 1 - May 20** Work on goal 2

*' May 23*' Program Starts

''' May 26 - June 12 ''' Exams

*' June 13 - July 13*' Code

*' July 13*' Mid Term deadline. Goals for here have not been set but personally I would like to have goal 2 & 4 finished with goal 3 having a decent chunk of work done. This weird out of order thing is because goal 3 can be worked on continuously as it is not really set, more the trying of ideas.

*' July 13 - August 17*' Code

**August 17** Program end
