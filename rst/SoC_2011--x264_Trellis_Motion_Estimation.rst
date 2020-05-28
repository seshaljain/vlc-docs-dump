.. raw:: mediawiki

   {{SoCProject|year=2011|student=[[User:dlarkin|Dan Larkin]]|mentor=[[User:Dark_Shikari|Jason Garret-Glaser]]}}

Abstract
--------

Using trellis optimization for motion estimation promises considerable savings while encoding motion vectors; however, if not done carefully, it can be very expensive. I have coded a vastly simplified standalone prototype. Currently, it uses precomputed SAD values to perform single-row optimization over (SAD + BITS_MVD) cost. The final product will differ in a few respects.

To improve results, we will consider optimizing over an entire frame, using alternating row and column iterations. This can be potentially very slow, especially since optimizing over columns may conflict with the current threading model.

Furthermore, the cost function will need to be determined. A full RDO-cost function may be more expensive to evaluate than we want, especially if we can develop a suitable heuristic.

Lastly, concerns of efficiency. The simplest ways to improve performance draw on techniques already used in x264 for motion estimation. Rather than aiming for full convergence, we can limit the maximum number of iterations. In the cases where we are already near a local minimum, we can enact early termination. We can also practice early termination in the partial sense - identify static prefixes to reduce trellis depth on the fly.
