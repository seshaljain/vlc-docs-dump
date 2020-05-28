.. raw:: mediawiki

   {{SoCProject|year=2008|student=[[User:keram|Joey Degges ]]|mentor=Jason Garrett-Glaser}}

Abstract
--------

The goal of this project is to improve heuristics and decision-making for inter refinement in order to improve efficiency given average encoding settings. This will involve various early termination heuristics along with methods of deciding which partition modes need to be searched while performing minimal actual searching on them. I also plan to experiment with different methods that can be used to improve psycho-visual optimizations for mode decisions and quantization. This will include improving variance adaptive quantization by experimenting with different methods which could be used to weight the variance in order to select a more optimized quantizer.

Goals
-----

Goals:

-  Improve inter prediction algorithms through the addition of early termination heuristics

#. Analyze the costs of using the different reference frames and partition modes.
#. Uses these results to create rules for early termination in order to avoid exhaustive searches.

-  Explore the usage of texture and shape in inter prediction

#. Implement curvature/first derivative algorithms (edge detection).
#. Compare edge count with the costs associated with the reference frames and partition modes.
#. Explore other metrics of texture/shape and their usefulness in this situation.
#. Implement early termination heuristics that depend on these texture and shape metrics.

-  Improve psycho-visual optimizations for mode decisions and quantization

#. Explore methods for SSIM-QNS optimization.
#. Adaptive dead zone / lambda.
#. Make improvements upon the Adaptive Quantization algorithms to achieve higher visual quality.

   #. Investigate the usage of NSSE and noise shaping techniques.
   #. Explore the usage of curvature as a means of weighting the variance in order to achieve a more optimized quantizer.
   #. Determine the most effective metric or combination of metrics.

Weekly Progress
---------------

Week 4
^^^^^^

Due to university commitments this was my first real week working on the project. I have primarily spent this week getting more familiar with the x264 code. To help familiarize myself with the code I have implemented a fast inter mode search algorithm which was inspired from an IEEE conference paper.

Here is the pseudo code for the search method. The patch can be found `here <http://jdegges.googlepages.com/x264-fast-inter-decision.patch>`__

| `` analyse_mode_16x16()``
| `` threshold1 = 48 * pow(1.12246,qp)``
| `` threshold2 = threshold1 + lambda2*192``
| `` if ( cost_16x16 < threshold1 )``
| `` {``
| ``   done``
| `` }``
| `` else if ( cost_16x16 < threshold2 )``
| `` {``
| ``   analyse_mode_16x8()``
| ``   analyse_mode_8x16()``
| `` }``
| `` else``
| `` {``
| ``   analyse_mode_8x8()``
| ``   if ( cost_8x8 < cost_16x16 )``
| ``   {``
| ``     if( frame_type == B_FRAME )``
| ``         done``
| ``     else``
| ``         analyse_mode_sub8x8()``
| ``   }``
| ``   else``
| ``   {``
| ``     analyse_mode_16x8()``
| ``     analyse_mode_8x16()``
| ``   }``
| `` }``

I am currently running many tests comparing the current algorithm with the proposed algorithm to see where it can be improved. Overall I am conducting 36 tests which are being driven with `this <http://jdegges.googlepages.com/x264-bench.sh>`__ bash script. The script compares the results of a patched x264 and an unmodified x264 on two different sources with 3 different bitrates (1500,1000,500), 3 different numbers of reference frames (8,4,1), as well as with and without mixed-refs. Results will be posted shortly!

Week 5
^^^^^^

The tests have finished and below is a graph comparing the execution time and bitrate between the two algorithms. As you can see, the proposed algorithm does not provide any bitrate improvement over the original algorithm. This with the combined with a quality improvement analysis (the second graph) which shows a maximum quality decrease of 3.5% further proves that this method is not a viable method for making inter mode decisions.

|bitrate-time-t1.png| |quality-test-t1.png|

Although this method does decrease the overall execution time, the effective bitrate increase and quality loss do not justify the savings in time.

Next I attempted to come up with a method for speeding up the ref search in x264_mb_analyse_inter_p8x8_mixed_ref. After looking at some of the reference costs I came up with a very simple method for skipping searches: if the cost of the current ref is greater than the previous ref two times in a row then stop searching. `Here <http://jdegges.googlepages.com/x264-mixed-ref.patch>`__ is a link to the patch.

To compute the effectiveness of this method I first compute the percentage of compression improvement gained by using mixedrefs Y% = 100 \* (1 - sum satd for best ref / sum satd for ref 0). Then the time saved using the proposed method T% = 100 \* (1 - # of ref searches / max refs) and the compression cost C% = 100 \* (sum of satd for selected refs / sum of satd for best ref - 1).

For the LosslessTouhou source I have found Y% = 6.6, T% = 74, and C% = .4.

Upon further analysis I found that it is somewhat likely that the best ref is two away from the selected ref. When tested I found T% = 73 and C% = .1

Week 6
^^^^^^

I have explored a few fast reference search approaches this week. Each method uses a different metric for signaling early termination. The first method uses a moving average of the cost of the best ref to predict a low cost point of termination. The second method is similar to the first except it maintains a moving average of the slope between the references to signal termination.

The first method, `moving averages <http://jdegges.googlepages.com/x264-mref-avg.patch.txt>`__, relies on the tendency of the best ref to be ref-0. Many sources have been examined (touhou,300,pirates) and on average 70% of the time the best reference frame is ref-0. This means that 70% of the time it is pointless to search the remaining references. To exploit this tendency a moving average is computed for all searched blocks where the best ref is ref-0. Every 10,000 blocks the average is updated with the cost of a best ref-0. When the average is not being updated the search will be terminated if the cost of ref-0 is within 3 standard deviations of the average.

Relative to the current method of early termination this method increases PSNR/SSIM/bitrate by ~40% and offers from ~15% to 35% speed increase. Ideally the speedup should be larger than the cost of the speedup so this method is suboptimal.

The third method, `average slope <http://jdegges.googlepages.com/x264-mref-slope.patch.txt>`__, keeps a moving average of the difference between ref-0 and ref-1 in the same manner as the first method. Other metrics can be used in a similar fashion. For example a ratio between ref-0 and ref-1 could be used.

Week 7
^^^^^^

After running some of my ideas past Dark_Shikari he advised me to try his '4 step' algorithm:

| `` 1. Check all possibilities with $fastmetric``
| `` 2. If better than $closethreshold, check with $slowmetric``
| `` 3. If worse than $farthreshold, don't check at all``
| `` 4. Take all the remaining modes in between the thresholds, sort, pick the best ones, and $slowmetric them``

Here the $fastmetric is the p16x16 search, and the slow metric is p8x8.

| `` p16x16_search();``
| `` for( i_ref = 0; i_ref <= i_maxref; i_ref++ ) {``
| ``   if( cost16x16[i_ref] < $C * bcost16x16 )``
| ``     c_ref8x8[h++] = i_ref;``
| ``   else if ( cost16x16[i_ref] < $F * bcost16x16 )``
| ``     f_ref8x8[k++] = i_ref;``
| `` }``
| `` pick_best(f_ref8x8);``
| `` p8x8_search( c_ref8x8, f_ref8x8 );``
| `` ``

This method relies heavily upon the selection of adequate thresholds and the method of picking the best far refs. On some sources a threshold of 200 can achieve an overall improvement in quality (0-5%) with minimal speedups (0-5%). On the other hand with thresholds closer to the mean more dramatic speedups can be seen with much higher costs. Here is a table with rough relative costs and speedup percentages:

| `` Threshold   Cost      Speedup``
| `` 200         0 - -5%   0 - 5%``
| `` 150         0 - 8%    0 - 11%``
| `` 112         0 - 35%   0 - 22%``

The 4-step patch can be found `here <http://jdegges.googlepages.com/x264-mref-4step.patch.txt>`__.

In addition to the 4-step algorithm I noticed that some parallels can be drawn between the 4 partitions in the p8x8 search. Currently all 4 partitions search the same set of references without taking advantage of the exhaustive search of the previous partition. Here all refs are searched in the first partition and the best $A percentage of those refs are used in the second partition. Then the p8x8[0] costs are averaged with the p8x8[1] costs and the best $B percentage are used in the third partition. The costs are then again averaged/sorted and the best $C percentage are used in the fourth partition. `Here <http://jdegges.googlepages.com/x264-mref-4part.patch.txt>`__ is the patch to the 4-part algorithm.

As with the 4-step algorithm this one can perform very differently depending on the selected thresholds. Thresholds 75-50-25 give relatives speedups from 0-16% and costs from 0-25%.

Week 8
^^^^^^

I have attempted to merge some search methods together to create a hybrid algorithm that can give better results. For preliminary testing the average bref was computed between 8 threshold intervals.

| `` for( i = 0; i < 9; i++ ) {``
| ``   if( cost16x16[bref]/bcost16x16 < threshold[i] ) {``
| ``     average_values[i] += bref;``
| ``     break;``
| ``   }``
| `` }``

The threshold[0] is the difference between bcost16x16 and cost16x16[bref8x8]. The other seven thresholds are each half a standard deviation greater than the previous threshold.

Similar to the original 4-step algorithm this one uses similarities between the costs/refs from the p16x16 search. If a ref cost is within one of the threshold intervals and the ref is close to the average ref for that interval then it will be searched. If any threshold intervals were not represented in the p16x16 costs then all of the refs will be searched:

| `` p16x16_search();``
| `` for( i_ref = 0; i_ref <= i_maxref; i_ref++ ) {``
| ``   if( aint != bint && aint != bint+1 ) {``
| ``     for( i = i_ref; i <= i_maxref; i++ )``
| ``       s_ref[k++] = ref16x16[i];``
| ``     break;``
| ``   }``
| ``   for( i = 0; i < 9; i++ ) {``
| ``     if( cost16x16[i_ref]/bcost16x16 <= threshold[i][0] && i_ref <= threshold[i][1] ) {``
| ``       s_ref[k++] = ref16x16[i_ref];``
| ``       bint = aint;``
| ``       aint = i;``
| ``     }``
| ``   }``
| `` }``
| `` p8x8_search( s_ref );``

This method is somewhat more robust than the previous methods in that it does not rely on any static thresholds. All of the thresholds can be computed live with moving averages. Using thresholds computed over the entire source (touhou) the results look very good when compared to other methods. Below is a graph showing the relative cost and speedups with a different number of references and at different target bitrates.

.. figure:: wk8-time_vs_bitrate.png
   :alt: wk8-time_vs_bitrate.png

   wk8-time_vs_bitrate.png

As you can see the cost/speedup scales with the number of references used and the cost/speedup ratio is close to 1. It is not clearly marked on the graph, but the number of references used at different bitrate are 16, 12, 8, 4, and 1. As the number of references is increased so are the cost and time savings.

Schedule
--------

All finals will be finished June 10th and starting June 11th I will be working full time. I will be camping sometime in late June for 1.5 days and possibly once more later in the summer. Other than that I do not plan to take any more vacation.

School starts back up ~28th of September so if all goes as planned my project will be completed by then :]

.. |bitrate-time-t1.png| image:: bitrate-time-t1.png
.. |quality-test-t1.png| image:: quality-test-t1.png

