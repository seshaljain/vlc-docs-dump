This page is about the H.264 encoder. Were you looking for , the H.264 decoder?

Options
-------

Frame-type
~~~~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-x264-keyint
   |value=integer
   |default=250
   |description=Maximum [[GOP]] size
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-min-keyint
   |value=integer
   |default=25
   |description=Minimum GOP size
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-opengop
   |value=boolean
   |default=disabled
   |description=Use recovery points to close GOPs
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-bluray-compat
   |value=boolean
   |default=disabled
   |description=Enable compatibility hacks for Blu-ray support
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-scenecut
   |value=integer
   |default=40
   |min=-1
   |max=100
   |description=Extra [[I-frame]]s aggressivity
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-bframes
   |value=integer
   |default=3
   |min=0
   |max=16
   |description=[[B-frame]]s between I and [[P-frame|P]]
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-b-adapt
   |value=integer
   |default=1
   |min=0
   |max=2
   |description=Adaptive B-frame decision
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-b-bias
   |value=integer
   |default=0
   |min=-100
   |max=100
   |description=Influence (bias) B-frames usage
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-bpyramid
   |value=string
   |default="normal"
   |select={none,strict,normal}
   |description=Keep some B-frames as references
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-cabac
   |value=boolean
   |default=enabled
   |description=[[wikipedia:Context-adaptive binary arithmetic coding|CABAC]]
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-fullrange
   |value=boolean
   |default=disabled
   |description=Use fullrange instead of TV colorrange
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-ref
   |value=integer
   |default=3
   |min=1
   |max=16
   |description=Number of reference frames
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-nf
   |value=boolean
   |default=disabled
   |description=Skip loop filter
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-deblock
   |value=string
   |default="0:0"
   |description=Loop filter AlphaC0 and Beta parameters alpha:beta
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-psy-rd
   |value=string
   |default="1.0:0.0"
   |description=Strength of psychovisual optimization
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-psy
   |value=boolean
   |default=enabled
   |description=Use Psy-optimizations
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-level
   |value=string
   |default="0"
   |description=[[H.264]] level
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-profile
   |value=string
   |default="high"
   |description=H.264 profile
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-interlaced
   |value=boolean
   |default=disabled
   |description=[[Interlaced]] mode
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-frame-packing<span id="select_sout-x264-frame-packing"></span>
   |value=integer
   |default=-1
   |select=[[#appendix_select_sout-x264-frame-packing|{-1,0,1,2,3,4,5,6}]]
   |description=Frame packing
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-slices
   |value=integer
   |default=0
   |description=Force number of slices per frame
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-slice-max-size
   |value=integer
   |default=0
   |description=Limit the size of each slice in bytes
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-slice-max-mbs
   |value=integer
   |default=0
   |description=Limit the size of each slice in macroblocks
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-hrd
   |value=string
   |default="none"
   |description=HRD-timing information
   }}

Rate control
~~~~~~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-x264-qp
   |value=integer
   |default=-1
   |min=-1
   |max=51
   |description=Set QP
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-crf
   |value=integer
   |default=23
   |min=0
   |max=51
   |description=Quality-based [[VBR]]
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-qpmin
   |value=integer
   |default=10
   |min=0
   |max=51
   |description=Min QP
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-qpmax
   |value=integer
   |default=51
   |min=0
   |max=51
   |description=Max QP
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-qpstep
   |value=integer
   |default=4
   |min=0
   |max=51
   |description=Max QP step between [[frame]]s
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-ratetol
   |value=float
   |default=1.0
   |min=0
   |max=100
   |description=[[Average bitrate]] tolerance
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-vbv-maxrate
   |value=integer
   |default=0
   |description=Max local bitrate
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-vbv-bufsize
   |value=integer
   |default=0
   |description=VBV buffer
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-vbv-init
   |value=float
   |default=0.9
   |min=0
   |max=1
   |description=Initial VBV buffer occupancy
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-ipratio
   |value=float
   |default=1.40
   |min=1
   |max=2
   |description=QP factor between I and P
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-pbratio
   |value=float
   |default=1.30
   |min=1
   |max=2
   |description=QP factor between P and B
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-chroma-qb-offset
   |value=integer
   |default=0
   |description=QP difference between chroma and luma
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-pass<span id="select_sout-x264-pass"></span>
   |value=integer
   |default=0
   |select=[[#appendix_select_sout-x264-pass|{0,1,2,3}]]
   |description=Multipass ratecontrol
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-qcomp
   |value=float
   |default=0.60
   |min=0
   |max=1
   |description=QP curve compression
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-cplxblur
   |value=float
   |default=20.0
   |description=Reduce fluctuations in QP
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-qblur
   |value=float
   |default=0.5
   |description=Reduce fluctuations in QP
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-aq-mode<span id="select_sout-x264-aq-mode"></span>
   |value=integer
   |default=<var>X264_AQ_VARIANCE</var>
   |select=[[#appendix_select_sout-x264-aq-mode|{0,1,2}]]
   |description=Defines bitdistribution mode for AQ, default 1
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-aq-strength
   |value=float
   |default=1.0
   |description=Strength of AQ
   }}

Analysis
~~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-x264-partitions
   |value=string
   |default="normal"
   |select={none,fast,normal,slow,all}
   |description=Partitions to consider
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-direct
   |value=string
   |default="spatial"
   |select={none,spatial,temporal,auto}
   |description=Direct MV prediction mode
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-direct-8x8
   |value=integer
   |default=1
   |min=-1
   |max=1
   |description=Direct prediction size
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-weightb
   |value=boolean
   |default=enabled
   |description=Weighted prediction for [[B-frame]]s
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-weightp
   |value=integer
   |default=2
   |min=0
   |max=2
   |description=Weighted prediction for [[P-frame]]s
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-me
   |value=string
   |default="hex"
   |select={dia,hex,umh,esa,tesa}
   |description=Integer pixel motion estimation method
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-merange
   |value=integer
   |default=16
   |min=1
   |max=64
   |description=Maximum motion vector search range
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-mvrange
   |value=integer
   |default=-1
   |description=Maximum motion vector length
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-mvrange-thread
   |value=integer
   |default=-1
   |description=Minimum buffer space between threads
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-subme
   |value=integer
   |default=7
   |min=1
   |max=9
   |description=Subpixel motion estimation and partition decision quality
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-mixed-refs
   |value=boolean
   |default=enabled
   |description=Decide references on a per partition basis
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-chroma-me
   |value=boolean
   |default=enabled
   |description=Chroma in motion estimation
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-8x8dct
   |value=boolean
   |default=enabled
   |description=Adaptive spatial transform size
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-trellis<span id="select_sout-x264-trellis"></span>
   |value=integer
   |default=1
   |select=[[#appendix_select_sout-x264-trellis|{0,1,2}]]
   |description=Trellis RD quantization: This requires CABAC
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-lookahead
   |value=integer
   |default=40
   |min=0
   |max=60
   |description=Framecount to use on frametype lookahead
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-intra-refresh
   |value=boolean
   |default=disabled
   |description=Use Periodic Intra Refresh
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-mbtree
   |value=boolean
   |default=enabled
   |description=Use mb-tree ratecontrol
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-fast-pskip
   |value=boolean
   |default=enabled
   |description=Early SKIP detection on [[P-frame]]s
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-dct-decimate
   |value=boolean
   |default=enabled
   |description=Coefficient thresholding on P-frames
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-nr
   |value=integer
   |default=0
   |min=0
   |max=1000
   |description=Noise reduction
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-deadzone-inter
   |value=integer
   |default=21
   |min=0
   |max=32
   |description=Inter luma quantization deadzone
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-deadzone-intra
   |value=integer
   |default=11
   |min=0
   |max=32
   |description=Intra luma quantization deadzone
   }}

Input/Output
~~~~~~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-x264-non-deterministic
   |value=boolean
   |default=disabled
   |description=Non-deterministic optimizations when threaded
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-asm
   |value=boolean
   |default=enabled
   |description=CPU optimizations
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-psnr
   |value=boolean
   |default=disabled
   |description=PSNR computation
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-ssim
   |value=boolean
   |default=disabled
   |description=SSIM computation
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-quiet
   |value=boolean
   |default=disabled
   |description=Quiet mode
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-sps-id
   |value=integer
   |default=0
   |description=SPS and PPS id numbers
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-aud
   |value=boolean
   |default=disabled
   |description=Access unit delimiters
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-verbose
   |value=boolean
   |default=disabled
   |description=Statistics
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-stats
   |value=string
   |default="x264_2pass.log"
   |description=Filename for 2 pass stats file
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-preset
   |value=string
   |default=NULL
   |description=Default preset setting used
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-tune
   |value=string
   |default=NULL
   |description=Default tune setting used
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-x264-options
   |value=string
   |default=NULL
   |description=[[x264]] advanced options, in the form <code>{opt=val,op2=val2}</code>
   }}

Appendix
~~~~~~~~

**For the option**\ ```--sout-x264-frame-packing`` <#select_sout-x264-frame-packing>`__\ **:**

-1: disabled
0: checkerboard - pixels are alternatively from L and R
1: column alternation - L and R are interlaced by column
2: row alternation - L and R are interlaced by row
3: side by side - L is on the left, R on the right
4: top bottom - L is on top, R on bottom
5: frame alternation - one view per frame

**For the option**\ ```--sout-x264-pass`` <#select_sout-x264-pass>`__\ **:**

1: First pass, creates stats file
2: Last pass, does not overwrite stats file
3: N\ :sup:`th` pass, overwrites stats file

**For the option**\ ```--sout-x264-aq-mode`` <#select_sout-x264-aq-mode>`__\ **:**

0: Disabled
1: Current x264 default mode
2: uses ``log(var)²`` instead of ``log(var)`` and attempts to adapt strength per frame

**For the option**\ ```--sout-x264-trellis`` <#select_sout-x264-trellis>`__\ **:**

0: disabled
1: enabled only on the final encode of a MB
2: enabled on all mode decisions

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/x264.c}}

.. raw:: mediawiki

   {{Documentation}}
