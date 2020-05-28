The schroedinger module replaces the earlier module for decoding and encoding `Dirac <Dirac>`__, a `video codec <video_codec>`__.

Demux
-----

.. raw:: mediawiki

   {{Module|name=schroedinger|type=Access demux|first_version=0.9.0|description=[[Dirac]] video decoder using libschroedinger|sc=schroedinger}}

Options
~~~~~~~

None.

Mux
---

.. raw:: mediawiki

   {{Module|name=schroedinger|type=Muxer|first_version=1.1.8|description=[[Dirac]] video encoder using libschroedinger|sc=schroedinger|sc2=schro}}

.. raw:: mediawiki

   {{Clear}}

.. _options-1:

Options
~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-schro-rate-control
   |value=string
   |default=NULL
   |select={constant_noise_threshold,constant_bitrate,low_delay,lossless,constant_lambda,constant_error,constant_quality}
   |description=Method used to encode the video sequence
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-quality
   |value=float
   |default=-1.
   |min=-1.
   |max=10.
   |description=Quality factor to use in constant quality mode
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-noise-threshold
   |value=float
   |default=-1.
   |min=-1.
   |max=100.
   |description=Noise threshold to use in constant noise threshold mode
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-bitrate
   |value=integer
   |default=-1
   |min=-1
   |max=<var>INT_MAX</var>
   |description=Target [[bitrate]] in kbps when encoding in constant bitrate mode
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-max-bitrate
   |value=integer
   |default=-1
   |min=-1
   |max=<var>INT_MAX</var>
   |description=Maximum bitrate in kbps when encoding in constant bitrate mode
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-min-bitrate
   |value=integer
   |default=-1
   |min=-1
   |max=<var>INT_MAX</var>
   |description=Minimum bitrate in kbps when encoding in constant bitrate mode
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-gop-structure<span id="select_sout-schro-gop-structure"></span>
   |value=string
   |default=NULL
   |select=[[#appendix_select_sout-schro-gop-structure|{adaptive,intra_only,backref,chained_backref,biref,chained_biref}]]
   |description=[[GOP]] structure used to encode the video sequence
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-gop-length
   |value=integer
   |default=-1
   |min=-1
   |max=<var>INT_MAX</var>
   |description=Number of pictures between successive sequence headers i.e. length of the group of pictures
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-chroma-fmt<span id="select_sout-schro-chroma-fmt"></span>
   |value=string
   |default=420
   |select=[[#appendix_select_sout-schro-chroma-fmt|{420,422,444}]]
   |description=Picking chroma format will force a conversion of the video into that format
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-coding-mode<span id="select_sout-schro-coding-mode"></span>
   |value=string
   |default=auto
   |select=[[#appendix_select_sout-schro-coding-mode|{auto,progressive,field}]]
   |description=Field coding is where [[interlaced]] fields are coded separately as opposed to a pseudo-progressive frame
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-mv-precision
   |value=string
   |default=NULL
   |select={1,1/2,1/4,1/8}
   |description=Motion Vector precision in pels
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-intra-wavelet<span id="select_sout-schro-intra-wavelet"></span>
   |value=string
   |default=NULL
   |select=[[#appendix_select_sout-schro-intra-wavelet|{desl_dubuc_9_7,le_gall_5_3,desl_dubuc_13_7,haar_0,haar_1,fidelity,daub_9_7}]]
   |description=Intra picture DWT filter
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-inter-wavelet<span id="select_sout-schro-inter-wavelet"></span>
   |value=string
   |default=NULL
   |select=[[#appendix_select_sout-schro-inter-wavelet|{desl_dubuc_9_7,le_gall_5_3,desl_dubuc_13_7,haar_0,haar_1,fidelity,daub_9_7}]]
   |description=Inter picture DWT filter
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-transform-depth
   |value=integer
   |default=-1
   |min=-1
   |max=<var>SCHRO_LIMIT_ENCODER_TRANSFORM_DEPTH</var>
   |description=Also known as DWT levels
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-filtering<span id="select_sout-schro-filtering"></span>
   |value=string
   |default=NULL
   |select=[[#appendix_select_sout-schro-filtering|{none,center_weighted_median,gaussian,add_noise,adaptive_gaussian,lowpass}]]
   |description=Enable adaptive prefiltering
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-filter-value
   |value=float
   |default=-1.
   |min=-1.
   |max=100.0
   |description=Higher value implies more prefiltering
   }}

Advanced options
~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-schro-motion-block-size<span id="select_sout-schro-motion-block-size"></span>
   |value=string
   |default=NULL
   |select=[[#appendix_select_sout-schro-motion-block-size|{auto,small,medium,large}]]
   |description=Size of motion compensation blocks
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-motion-block-overlap<span id="select_sout-schro-motion-block-overlap"></span>
   |value=string
   |default=NULL
   |select=[[#appendix_select_sout-schro-motion-block-overlap|{automatic,none,partial,full}]]
   |description=Overlap of motion compensation blocks
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-me-combined
   |value=integer
   |default=-1
   |min=-1
   |max=1
   |description=Use chroma as part of the motion estimation process
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-enable-hierarchical-me
   |value=integer
   |default=-1
   |min=-1
   |max=1
   |description=Enable hierarchical Motion Estimation
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-downsample-levels
   |value=integer
   |default=-1
   |min=-1
   |max=8
   |description=Number of levels of downsampling in hierarchical motion estimation mode
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-enable-global-me
   |value=integer
   |default=-1
   |min=-1
   |max=1
   |description=Enable Global Motion Estimation
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-enable-phasecorr-me
   |value=integer
   |default=-1
   |min=-1
   |max=1
   |description=Enable Phase Correlation Estimation
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-enable-multiquant
   |value=integer
   |default=-1
   |min=-1
   |max=1
   |description=Enable multiple quantizers per subband (one per codeblock)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-codeblock-size<span id="select_sout-schro-codeblock-size"></span>
   |value=string
   |default=NULL
   |select=[[#appendix_select_sout-schro-codeblock-size|{automatic,small,medium,large,full}]]
   |description=Size of code blocks in each subband
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-enable-scd
   |value=integer
   |default=-1
   |min=-1
   |max=1
   |description=Enable Scene Change Detection
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-perceptual-weighting
   |value=string
   |default=NULL
   |select={none,ccir959,moo,manos_sakrison}
   |description=perceptual weighting method
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-perceptual-distance
   |value=float
   |default=-1
   |min=-1.
   |max=100.
   |description=perceptual distance to calculate perceptual weight
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-enable-noarith
   |value=integer
   |default=-1
   |min=-1
   |max=1
   |description=Use variable length codes instead, useful for very high bitrates
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-horiz-slices
   |value=integer
   |default=-1
   |min=-1
   |max=<var>INT_MAX</var>
   |description=Number of horizontal slices per [[frame]] in low delay mode
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-vert-slices
   |value=integer
   |default=-1
   |min=-1
   |max=<var>INT_MAX</var>
   |description=Number of vertical slices per frame in low delay mode
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-schro-force-profile<span id="select_sout-schro-force-profile"></span>
   |value=string
   |default=NULL
   |select=[[#appendix_select_sout-schro-force-profile|{auto,vc2_low_delay,vc2_simple,vc2_main,main}]]
   |description=Force Profile
   }}

Appendix
~~~~~~~~

**For the option**\ ```--sout-schro-gop-structure`` <#select_sout-schro-gop-structure>`__\ **:**

adaptive:No fixed `GOP <GOP>`__ structure. A picture can be intra or inter and refer to previous or future pictures.
intra_only:I-frame only sequence
backref:Inter pictures refere to previous pictures only
chained_backref:Inter pictures refere to previous pictures only
biref:Inter pictures can refer to previous or future pictures
chained_biref:Inter pictures can refer to previous or future pictures

--------------

**For the option**\ ```--sout-schro-chroma-fmt`` <#select_sout-schro-chroma-fmt>`__\ **:**

420:4:2:0
422:4:2:2
444:4:4:4

--------------

**For the option**\ ```--sout-schro-coding-mode`` <#select_sout-schro-coding-mode>`__\ **:**

auto:auto - let encoder decide based upon input (Best)
progressive:force coding frame as single picture
field:force coding frame as separate interlaced fields

--------------

**For the option**\ ```--sout-schro-motion-block-size`` <#select_sout-schro-motion-block-size>`__\ **:**

automatic:automatic - let encoder decide based upon input (Best)
small:small - use small motion compensation blocks
medium:medium - use medium motion compensation blocks
large:large - use large motion compensation blocks

--------------

**For the option**\ ```--sout-schro-motion-block-overlap`` <#select_sout-schro-motion-block-overlap>`__\ **:**

automatic:automatic - let encoder decide based upon input (Best)
none:none - Motion compensation blocks do not overlap
partial:partial - Motion compensation blocks only partially overlap
full:full - Motion compensation blocks fully overlap

--------------

**For the options**\ ```--sout-schro-intra-wavelet`` <#select_sout-schro-intra-wavelet>`__\ **and**\ ```--sout-schro-inter-wavelet`` <#select_sout-schro-inter-wavelet>`__\ **:**

desl_dubuc_9_7:Deslauriers-Dubuc (9,7)
le_gall_5_3:LeGall (5,3)
desl_dubuc_13_7:Deslauriers-Dubuc (13,7)
haar_0:Haar with no shift
haar_1:Haar with single shift per level
fidelity:Fidelity filter
daub_9_7:Daubechies (9,7) integer approximation

--------------

**For the option**\ ```--sout-schro-codeblock-size`` <#select_sout-schro-codeblock-size>`__\ **:**

automatic:automatic - let encoder decide based upon input (Best)
small:small - use small code blocks
medium:medium - use medium sized code blocks
large:large - use large code blocks
full:full - One code block per subband

--------------

**For the option**\ ```--sout-schro-filtering`` <#select_sout-schro-filtering>`__\ **:**

none:No pre-filtering
center_weighted_median:Centre Weighted Median
gaussian:Gaussian Low Pass Filter
add_noise:Add Noise
adaptive_gaussian:Gaussian Adaptive Low Pass Filter
lowpass:Low Pass Filter

--------------

**For the option**\ ```--sout-schro-force-profile`` <#select_sout-schro-force-profile>`__\ **:**

auto:automatic - let encoder decide based upon input (Best)
vc2_low_delay:VC2 Low Delay Profile
vc2_simple:VC2 Simple Profile
vc2_main:VC2 Main Profile
main:Main Profile

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/schroedinger.c}}

.. raw:: mediawiki

   {{Documentation}}
