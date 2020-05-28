.. raw:: mediawiki

   {{SoCProject|year=2008|student=[[User:Kuukunen|Aki Jäntti]]|mentor=Alex Izvorski}}

Project Abstract
----------------

The basic idea of a "macroblock tree" is to keep track of macroblock references to try to figure out which macroblocks are the most important ones. The currently planned way of doing this is to think of the macroblocks as nodes of an acyclic graph. ("Tree" is actually a bit misleading, since it will probably be a "forest".)

Each node (mb) has an importance and every mb will start at the same importance. Most likely a big integer, so that everything can be handled as integers, but for the sake of the explanation, let it be 1.0. Then the references are analyzed and if block A references to block B, block B's importance gets increased by approximated amount of information transferred from block A. One mb can refer to four mbs, and the importance is multiplied by a factor determined by how much of the area the reference covers. For example, if block A refers to a position half between block B and block C, A's importance += 0.5*B's importance + 0.5*C's importance. Also, the cost of the residual can be used to approximate the amount of information actually coming from the referenced block, and this will be used as another multiplier. Even though a block is referring to another, it might overwrite most of the information. In this case the reference block is not that important. The trees are traversed starting from the leaves (the mbs that are not referenced) and the importances are accumulated.

After calculating importance for each mb, they can be summed together for importance of the frame. This information can be used for determining the quantizers on frame and block level. They might be also used in frame type decisions, but that would require for a bit more advanced modifications on the whole encoder than just the basic version.

Implementation
--------------

First I will do a rough version to test if the whole thing is even realistic. This involves modifying the first pass so that it will gather statistics on the macroblocks as explained above. For the very first version it might be better to just save the tree/statistics in a file and use that file on the second pass. However this file will probably be very big, so if that gives promising results, the next step is to analyze the statistics during the first pass whenever one GOP is finished, then just write the final weights in the passfile.

The next goal might be implementing this in one pass encoding. Again, working one GOP at a time. As far as I know, this would need some modifications on the basic workings of the encoder and would require buffering a substantial amount of frames.

I have also been pondering the possibility of modifying the whole idea of the first pass into purely searching for references everywhere without caring about frame types. And in the end deciding frame types based on the mb tree. I have no idea how feasible this is, though. Again, this could be modified into one pass encoding too with large buffer.

Timeline
--------

======== ========================================================================================================================================= ===========
Deadline Task                                                                                                                                      Status
======== ========================================================================================================================================= ===========
June 21  Rough test version for getting to know the code, testing feasibility and to get an idea of the level of work needed for the future tasks. In progress
\                                                                                                                                                 
======== ========================================================================================================================================= ===========

Due to the nature of the project, it is hard to know what kind of stages it will contain and how much time they will take. I have discussed this with my mentor and I will update this list once the first task is finished.

Other Schedule
--------------

We have been planning a two week trip to Norway in June. The actual dates are still not completely clear, but I will update this as soon as I can.

Week 1
------

The last university project went over the initial deadline, so it caused some problems. Rest of the week I studied and poked around the x264 code.
