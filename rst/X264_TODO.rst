.. raw:: mediawiki

   {{Lowercase}}

.. raw:: mediawiki

   {{Back to|Category:x264}}

This page contains an incomplete list of things available in x264 for you to do. It's organized into sections covering various parts of x264.

Some useful resources: `Dark Shikari's pile of junk <http://www.x264.nl/developers/Dark_Shikari/?dir=./src>`__, `Pengvado's pile of junk <http://akuvian.org/src/x264/>`__.

If you're interested in doing any of this, drop by #x264dev on Freenode IRC. There are no experience or educational requirements for doing any of this, though you are expected to know how to code.

Bolded features may have companies willing to sponsor or provide bounties. This is not complete either; just because it's not bolded doesn't mean there aren't resources out there. If your company is interested in offering a bounty, drop by IRC.

Motion Estimation
~~~~~~~~~~~~~~~~~

-  Sequential elimination (SEA), used for exhaustive search, might be more generally applicable to algorithms like UMH, by letting us skip a lot of SADs. The downside is we won't be able to use SAD_X4 anymore.
-  (T)ESA is currently wrong for motion searches done on weightp duplicates. This effect is miniscule, but it still should be fixed.
-  Hierarchical motion estimation might be a useful way to catch very long motion vectors without the cost of UMH or ESA. It might also help regularize motion.

   -  I have a patch for this in the lookahead, but it didn't help much, since it only added predictors.

-  Somehow take into account the effect of motion vector decision on future blocks.

   -  Hierarchical motion estimation
   -  Approximations from lookahead MVs
   -  Iterative ME (as per Snow)
   -  Trellis motion estimation

-  We don't need to check all 11 predictors all the time for 16x16 fullpel motion search.

   -  But how do we know which ones we can afford to skip, and when?
   -  Xvid and libtheora have algorithms for this, but the former's is almost surely 100% useless and the latter doesn't seem impressive either.

-  libtheora does fullpel motion estimation on the source pixels instead of decoded pixels. Does this give a better starting point for the subpel search and discourage "weird" MVs?
-  With extremely fast encoding settings (subme 0), can we rip off lookahead MVs instead of doing a real search?

   -  This seems to be awful from my testing, but maybe there's something we can do?

-  Try sub-8x8 partitions in B-frames. Is it at all useful?
-  Try bidir motion estimation for fullpel. That is, considering L1's MV when doing L0 (or vice versa). Xvid does this. How much does it help?
-  Fullpel chroma ME?

   -  For TESA?

Intra Analysis
~~~~~~~~~~~~~~

-  Make the early terminations smarter. Currently they're just hacks -- some statistical analysis might be useful.

   -  With the SSSE3-based fast intra analysis, we no longer do any early terminations for different modes, at least in SAD/SATD analysis. But there might still be improvements to be made.

-  SAD (subme 1) i8x8 vs i4x4 decision is a bit bad. Can it be improved without significant speed loss?

Mode Decision
~~~~~~~~~~~~~

-  Can we find more ways to skip more motion searches in multiref?

   -  A while back, I tried using weaker motion searches on older refs. This helped a bit for speed-vs-compression, but is ironically the opposite of what one wants; older refs will be harder to find good MVs in, and therefore really need better searches.

-  On extremely fast encoding settings, fast skip is actually kind of slow. But anything dumber (e.g. SAD) is completely useless. Is there some better balance that can be achieved here?

   -  Can we do something smart by analyzing fenc? It's impossible to tell whether a block is motionless by looking at fdec, but looking at the source pixels is useful. There's still complexity such as lower-QP-than-reference though.

-  See the TODOs for deblock-aware RD in common/deblock.c.

   -  I tried correcting weightp references for deblock RDO, but it didn't help.
   -  I tried chroma, too, and again, it didn't help measurably.

-  Is there a faster way than SA8D/SATD to do 8x8dct vs 4x4dct mode decision? At very fast settings, the time this uses is nontrivial.

   -  Doing a merged 4x4/8x8 SATD would help here, but would require new asm.

-  Is there a faster way than RD to do 8x8dct vs 4x4dct mode decision that's still better than SATD? RD takes over an order of magnitude more time than SATD, so it might be useful to have something in the middle.
-  Is there some value to swapping the mode decision metric from SATD to SA8D if we think that the macroblock will use 8x8dct? `This has been tried before <http://akuvian.org/src/x264/x264_dct8_guess.diff>`__, but only helped if our guess was extremely good (better than we could get in reality).
-  With trellis 2, can we skip most of CABAC and CAVLC bit cost calculation?
-  How about saving CABAC state between each trellis call, rather than basing them all on the CABAC state at the start of the macroblock?
-  Make subme=11 not do thresholding in qpel RD and bidir RD.

Psy
~~~

-  Psy-RD is a hack. It works, but it's a hack. If you apply QNS with Psy-RD as the metric, it goes way overboard and gives terrible results. This means that Psy-RD only works because normal mode decision is limited in the way it can modify the image to better suit the metric. Is there a way to make it better?
-  Should RD be linear at all? Perhaps we should weight more heavily against low quality blocks and also try to ignore minuscule distortion that viewers can't see.
-  Psy-trellis (and maybe psy-RD?) are too strong at very high QPs.
-  Psy-trellis should be merged with Psy-RD. There are patches for this, but they probably won't be committed until psy-RD itself is fixed.
-  RD should take into account local variance.
-  Lambda should be varied on a per-DCT-block basis instead of a per-macroblock basis.
-  Lambda should be picked independent of quantizer (i.e. with greater precision).
-  Classic problem: a block is mostly high complexity but has a small area of low complexity. How do we judge whether that area is important? Good example: sharp text on background with film grain; grain gets blurred out because of the text.

   -  If we think it's important all the time, we ruin the quality of many clips that rely on raising complexity on edges (Touhou).

-  Should motion estimation lambda be as high as it is at very high quantizers? There's some value to capturing "true motion"...
-  Macroblock tree correlates pretty well with visual perception in that its concept of a "high complexity" matches well with the visual concept. Except for local illumination changes. Talk to Dark Shikari for a patch.

Lookahead
~~~~~~~~~

-  Temporal MV predictors in lookahead? There's a patch for these somewhere, but they biased heavily in favor of B-frames, likely by improving the motion search.
-  Should lookahead use variable lambda based on quantizer (esp. due to adaptive quant)? If so, should it take into account estimated ratecontrol quantizer, too? If so, how?
-  B-adapt 1 could be made quite a bit better -- it's important because it's used on all the fast speed modes (and even the defaults). "Harbour 4CIF" is a good example of a clip where it does noticeably badly.

Quantization
~~~~~~~~~~~~

-  CAVLC "trellis" is a hack. It works, but it's a hack. Make it better. See the TODOs in encoder/rdo.c.

   -  This is doubly important now, as CABAC trellis has been made way faster, but CAVLC hasn't. Many of the CABAC trellis improvements can be backported.

-  There's room for something between trellis and deadzone in terms of complexity. libvpx has a good example -- it biases towards zero-runs in its "medium speed" quantizer. This can't be SIMD'd easily, but is still vastly faster than trellis. A nonlinear quantizer (be more likely to round up larger coefficients) might also be useful.

   -  How useful is this with an entropy coder that doesn't really bias towards zero-runs, as in CABAC?

-  Floyd-Steinberg for quantization? Try pushing quantization error to nearby DCT coefficients. Should this go from high to low or low to high?
-  Energy-preserving quantizer -- maintain L1 (or maybe L2? I'm not sure) energy. Should we maintain it in the spatial domain (post-iDCT) or residual domain? Probably the former.

   -  See [https://github.com/saintdev/x264-devel/compare/enquant-base...energy-quant saintdev's github] for one attempt at this.

-  Decimation is currently just a ripoff of the JVT recommended algorithm. Can we do this more optimally? With RD?

Transform
~~~~~~~~~

-  Analyze the error characteristics of the fDCT. Is there any way to make it more accurate without much speed loss? Particularly at extremely low quantizers, this might help.
-  Before forward transform, run a "blocking filter" that acts as the approximate inverse of the deblock filter. See `this paper <http://akuvian.org/src/x264/Shwang_loopfilter_thesis.pdf>`__.

Interlacing
~~~~~~~~~~~

-  Lookahead currently blend-deinterlaces to get the lowres. Is this a good idea? Is there something better that isn't much slower?
-  Constrained intra + adaptive MBAFF. Does anyone care about this?
-  PAFF + MBAFF adaptive - PAFF performs better than Adaptive MBAFF on high motion scenes because it can predict from the previous field.

Weighted Prediction
~~~~~~~~~~~~~~~~~~~

-  **Make weightp work with interlacing. Preferably abuse reference duplication to make it useful for MBAFF.**
-  Finish K-means decision for weightp. Talk to DylanZA about getting his current patch for this one.
-  Add explicit weighting for B-frames, too. This helps in nonlinear fades, among other cases.
-  Improve weighted prediction analysis to do more searching based on an estimated offset vs scale gradient.

Ratecontrol
~~~~~~~~~~~

-  Current per-frame VBV is a hack. It only adapts per row and is O(N^2), where N is the number of rows. An O(N) solution would be able to react more often and thus be more accurate.
-  Make the frame size and row size predictors better. They currently are kind of crappy.
-  Ratecontrol code as a whole is a bit of a mess. It could be improved. There's a lot of cruft left over that is probably not needed now, like qblur.
-  1-pass ratecontrol often can't adapt fast enough when there are lots of threads (12, 16, 24, etc), especially with smallish VBV buffers. Improve this?
-  2-pass VBV is actually a bit more likely to underflow than 1-pass because it doesn't adapt as aggressively and trusts first pass data a lot. This trust is often misplaced if the first pass was a fast one. This should be improved.

   -  2-pass is still better in the case of many threads, due to the above.

-  2-pass macroblock-tree: if we added the ability to do macroblock-tree on real encoded data, we'd get better results (particularly with repeating patterns and multiref, such as an anime character's mouth moving).
-  Macroblock-tree: make it more psy-aware. Maybe we should cap how much it lowers the quantizer on extremely static scenes? This might tie into the "just-noticeable error" issue in RD.

GPU
~~~

-  Motion estimation?

   -  Methods

      -  Hierarchical?
      -  2D Wave?
      -  Something else?

   -  "Easy": lookahead motion estimation

      -  Extremely high parallelism, hundreds of frame searches (each with thousands of searches) at once.

   -  "Hard": main motion estimation

      -  Difficult synchronization issues, not as heavily parallel in terms of number of macroblocks, but far more partition sizes and refs to search.
      -  But potentially more useful...

-  Other things?

Other assembly
~~~~~~~~~~~~~~

-  A lot of ARM assembly is done. Missing is mostly for Hi-Depth bitrate.
-  Altivec assembly is very lacking.

Other CPU optimizations
~~~~~~~~~~~~~~~~~~~~~~~

-  x264 needs more prefetching. How many L1 and L2 cache misses (particularly L1) can we get rid of via smart prefetching in the right places? Warning: this is often hard to benchmark.
-  Different CPUs take different relative times for some functions. Is this enough (particularly across architectures) to justify different encoding settings for different CPUs?

Other features
~~~~~~~~~~~~~~

-  MPEG-2 encoding support

   -  `x262 <https://github.com/kierank/x262/wiki/TODO>`__

-  Support for SMPTE timecodes
-  Merge speedcontrol
-  Mixed lossless/lossy encoding.
-  Segment re-encoding

x264CLI
~~~~~~~

-  Finish audio support. Talk to Kovensky about this one.
-  Make the filtering system aware of BT.601 vs BT.709.
-  Use libavfilter instead of duplicating the filters in x264.
-  Add --device support.
-  Add automatic --level restriction support.

`Category:x264 <Category:x264>`__
