The schroedinger module replaces the earlier {{docmod|dirac}} module for
decoding and encoding [[Dirac]], a [[video codec]].

== Demux == {{Moduletype=Access demuxdescription=[[Dirac]] video decoder
using libschroedinger|sc=schroedinger}}

=== Options === None. {{Clear}}

== Mux == {{Moduletype=Muxerdescription=[[Dirac]] video encoder using
libschroedingersc2=schro}}

{{Clear}}

=== Options === {{Option value=string
select={constant_noise_threshold,constant_bitrate,low_delay,lossless,constant_lambda,constant_error,constant_quality}
name=sout-schro-quality default=-1. max=10.
name=sout-schro-noise-threshold default=-1. max=100.
name=sout-schro-bitrate default=-1 max=<var>INT_MAX</var>
name=sout-schro-max-bitrate default=-1 max=<var>INT_MAX</var>
name=sout-schro-min-bitrate default=-1 max=<var>INT_MAX</var>
name=sout-schro-gop-structure<span
id="select_sout-schro-gop-structure"></span> default=NULL
{adaptive,intra_only,backref,chained_backref,biref,chained_biref}]]
name=sout-schro-gop-length default=-1 max=<var>INT_MAX</var>
name=sout-schro-chroma-fmt<span
id="select_sout-schro-chroma-fmt"></span> default=420 {420,422,444}]]
name=sout-schro-coding-mode<span
id="select_sout-schro-coding-mode"></span> default=auto
{auto,progressive,field}]] name=sout-schro-mv-precision default=NULL
description=Motion Vector precision in pels }} {{Option value=string
select=[[#appendix_select_sout-schro-intra-waveletdescription=Intra
picture DWT filter }} {{Option value=string
select=[[#appendix_select_sout-schro-inter-waveletdescription=Inter
picture DWT filter }} {{Option value=integer min=-1 description=Also
known as DWT levels }} {{Option value=string
select=[[#appendix_select_sout-schro-filteringdescription=Enable
adaptive prefiltering }} {{Option value=float min=-1. description=Higher
value implies more prefiltering }}

=== Advanced options === {{Option value=string
select=[[#appendix_select_sout-schro-motion-block-sizedescription=Size
of motion compensation blocks }} {{Option value=string
select=[[#appendix_select_sout-schro-motion-block-overlapdescription=Overlap
of motion compensation blocks }} {{Option value=integer min=-1
description=Use chroma as part of the motion estimation process }}
{{Option value=integer min=-1 description=Enable hierarchical Motion
Estimation }} {{Option value=integer min=-1 description=Number of levels
of downsampling in hierarchical motion estimation mode }} {{Option
value=integer min=-1 description=Enable Global Motion Estimation }}
{{Option value=integer min=-1 description=Enable Phase Correlation
Estimation }} {{Option value=integer min=-1 description=Enable multiple
quantizers per subband (one per codeblock) }} {{Option value=string
select=[[#appendix_select_sout-schro-codeblock-sizedescription=Size of
code blocks in each subband }} {{Option value=integer min=-1
description=Enable Scene Change Detection }} {{Option value=string
select={none,ccir959,moo,manos_sakrison}
name=sout-schro-perceptual-distance default=-1 max=100.
name=sout-schro-enable-noarith default=-1 max=1
name=sout-schro-horiz-slices default=-1 max=<var>INT_MAX</var>
name=sout-schro-vert-slices default=-1 max=<var>INT_MAX</var>
name=sout-schro-force-profile<span
id="select_sout-schro-force-profile"></span> default=NULL
{auto,vc2_low_delay,vc2_simple,vc2_main,main}]] \|description=Force
Profile }}

=== Appendix === <span
id="appendix_select_sout-schro-gop-structure"></span> '''For the option
<code>[[#select_sout-schro-gop-structure|--sout-schro-gop-structure]]</code>:'''
;adaptive:No fixed [[GOP]] structure. A picture can be intra or inter
and refer to previous or future pictures. ;intra_only:I-frame only
sequence ;backref:Inter pictures refere to previous pictures only
;chained_backref:Inter pictures refere to previous pictures only
;biref:Inter pictures can refer to previous or future pictures
;chained_biref:Inter pictures can refer to previous or future pictures

----<span id="appendix_select_sout-schro-chroma-fmt"></span> '''For the
option
<code>[[#select_sout-schro-chroma-fmt|--sout-schro-chroma-fmt]]</code>:'''
;420:4:2:0 ;422:4:2:2 ;444:4:4:4

----<span id="appendix_select_sout-schro-coding-mode"></span> '''For the
option
<code>[[#select_sout-schro-coding-mode|--sout-schro-coding-mode]]</code>:'''
;auto:auto - let encoder decide based upon input (Best)
;progressive:force coding frame as single picture ;field:force coding
frame as separate interlaced fields

----<span id="appendix_select_sout-schro-motion-block-size"></span>
'''For the option
<code>[[#select_sout-schro-motion-block-size|--sout-schro-motion-block-size]]</code>:'''
;automatic:automatic - let encoder decide based upon input (Best)
;small:small - use small motion compensation blocks ;medium:medium - use
medium motion compensation blocks ;large:large - use large motion
compensation blocks

----<span id="appendix_select_sout-schro-motion-block-overlap"></span>
'''For the option
<code>[[#select_sout-schro-motion-block-overlap|--sout-schro-motion-block-overlap]]</code>:'''
;automatic:automatic - let encoder decide based upon input (Best)
;none:none - Motion compensation blocks do not overlap ;partial:partial
- Motion compensation blocks only partially overlap ;full:full - Motion
compensation blocks fully overlap

----<span id="appendix_select_sout-schro-intra-wavelet"></span><span
id="appendix_select_sout-schro-inter-wavelet"></span> '''For the options
<code>[[#select_sout-schro-intra-wavelet--sout-schro-inter-wavelet]]</code>:'''
;desl_dubuc_9_7:Deslauriers-Dubuc (9,7) ;le_gall_5_3:LeGall (5,3)
;desl_dubuc_13_7:Deslauriers-Dubuc (13,7) ;haar_0:Haar with no shift
;haar_1:Haar with single shift per level ;fidelity:Fidelity filter
;daub_9_7:Daubechies (9,7) integer approximation

----<span id="appendix_select_sout-schro-codeblock-size"></span> '''For
the option
<code>[[#select_sout-schro-codeblock-size|--sout-schro-codeblock-size]]</code>:'''
;automatic:automatic - let encoder decide based upon input (Best)
;small:small - use small code blocks ;medium:medium - use medium sized
code blocks ;large:large - use large code blocks ;full:full - One code
block per subband

----<span id="appendix_select_sout-schro-filtering"></span> '''For the
option
<code>[[#select_sout-schro-filtering|--sout-schro-filtering]]</code>:'''
;none:No pre-filtering ;center_weighted_median:Centre Weighted Median
;gaussian:Gaussian Low Pass Filter ;add_noise:Add Noise
;adaptive_gaussian:Gaussian Adaptive Low Pass Filter ;lowpass:Low Pass
Filter

----<span id="appendix_select_sout-schro-force-profile"></span> '''For
the option
<code>[[#select_sout-schro-force-profile|--sout-schro-force-profile]]</code>:'''
;auto:automatic - let encoder decide based upon input (Best)
;vc2_low_delay:VC2 Low Delay Profile ;vc2_simple:VC2 Simple Profile
;vc2_main:VC2 Main Profile ;main:Main Profile

== Source code == \* {{VLCSourceFile|modules/codec/schroedinger.c}}

{{Documentation}}
