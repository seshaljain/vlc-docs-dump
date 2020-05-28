<span class="hatnote">This page is about the H.264 encoder. Were you
looking for {{docmodDocumentation:Modules/x265}}
{{Moduletype=Muxerdescription=[[H.264/MPEG-4 AVC|H.264/MPEG-4 Part
10/AVC]] encoder ([[x264]])}}

== Options == === Frame-type === {{Option value=integer
description=Maximum [[GOP]] size }} {{Option value=integer
description=Minimum GOP size }} {{Option value=boolean description=Use
recovery points to close GOPs }} {{Option value=boolean
description=Enable compatibility hacks for Blu-ray support }} {{Option
value=integer min=-1 description=Extra [[I-frame]]s aggressivity }}
{{Option value=integer min=0 description=[[B-frame]]s between I and
[[P-framename=sout-x264-b-adapt default=1 max=2 name=sout-x264-b-bias
default=0 max=100 name=sout-x264-bpyramid default="normal"
description=Keep some B-frames as references }} {{Option value=boolean
description=[[wikipedia:Context-adaptive binary arithmetic
codingname=sout-x264-fullrange default=disabled name=sout-x264-ref
default=3 max=16 name=sout-x264-nf default=disabled
name=sout-x264-deblock default="0:0" name=sout-x264-psy-rd
default="1.0:0.0" name=sout-x264-psy default=enabled
name=sout-x264-level default="0" name=sout-x264-profile default="high"
name=sout-x264-interlaced default=disabled
name=sout-x264-frame-packing<span
id="select_sout-x264-frame-packing"></span> default=-1
{-1,0,1,2,3,4,5,6}]] name=sout-x264-slices default=0
name=sout-x264-slice-max-size default=0 name=sout-x264-slice-max-mbs
default=0 name=sout-x264-hrd default="none" \|description=HRD-timing
information }}

=== Rate control === {{Option value=integer min=-1 description=Set QP }}
{{Option value=integer min=0 description=Quality-based [[VBR]] }}
{{Option value=integer min=0 description=Min QP }} {{Option
value=integer min=0 description=Max QP }} {{Option value=integer min=0
description=Max QP step between [[frame]]s }} {{Option value=float min=0
description=[[Average bitrate]] tolerance }} {{Option value=integer
description=Max local bitrate }} {{Option value=integer description=VBV
buffer }} {{Option value=float min=0 description=Initial VBV buffer
occupancy }} {{Option value=float min=1 description=QP factor between I
and P }} {{Option value=float min=1 description=QP factor between P and
B }} {{Option value=integer description=QP difference between chroma and
luma }} {{Option value=integer
select=[[#appendix_select_sout-x264-passdescription=Multipass
ratecontrol }} {{Option value=float min=0 description=QP curve
compression }} {{Option value=float description=Reduce fluctuations in
QP }} {{Option value=float description=Reduce fluctuations in QP }}
{{Option value=integer
select=[[#appendix_select_sout-x264-aq-modedescription=Defines
bitdistribution mode for AQ, default 1 }} {{Option value=float
description=Strength of AQ }}

=== Analysis === {{Option value=string
select={none,fast,normal,slow,all} name=sout-x264-direct
default="spatial" description=Direct MV prediction mode }} {{Option
value=integer min=-1 description=Direct prediction size }} {{Option
value=boolean description=Weighted prediction for [[B-frame]]s }}
{{Option value=integer min=0 description=Weighted prediction for
[[P-frame]]s }} {{Option value=string select={dia,hex,umh,esa,tesa}
name=sout-x264-merange default=16 max=64 name=sout-x264-mvrange
default=-1 name=sout-x264-mvrange-thread default=-1 name=sout-x264-subme
default=7 max=9 name=sout-x264-mixed-refs default=enabled
name=sout-x264-chroma-me default=enabled name=sout-x264-8x8dct
default=enabled name=sout-x264-trellis<span
id="select_sout-x264-trellis"></span> default=1 {0,1,2}]]
name=sout-x264-lookahead default=40 max=60 name=sout-x264-intra-refresh
default=disabled name=sout-x264-mbtree default=enabled
name=sout-x264-fast-pskip default=enabled name=sout-x264-dct-decimate
default=enabled name=sout-x264-nr default=0 max=1000
name=sout-x264-deadzone-inter default=21 max=32
name=sout-x264-deadzone-intra default=11 max=32 \|description=Intra luma
quantization deadzone }}

=== Input/Output === {{Option value=boolean
description=Non-deterministic optimizations when threaded }} {{Option
value=boolean description=CPU optimizations }} {{Option value=boolean
description=PSNR computation }} {{Option value=boolean description=SSIM
computation }} {{Option value=boolean description=Quiet mode }} {{Option
value=integer description=SPS and PPS id numbers }} {{Option
value=boolean description=Access unit delimiters }} {{Option
value=boolean description=Statistics }} {{Option value=string
description=Filename for 2 pass stats file }} {{Option value=string
description=Default preset setting used }} {{Option value=string
description=Default tune setting used }} {{Option value=string
description=[[x264]] advanced options, in the form
<code>{opt=val,op2=val2}</code> }}

=== Appendix === <span
id="appendix_select_sout-x264-frame-packing"></span> '''For the option
<code>[[#select_sout-x264-frame-packing|--sout-x264-frame-packing]]</code>:'''
;-1: disabled ;0: checkerboard - pixels are alternatively from L and R
;1: column alternation - L and R are interlaced by column ;2: row
alternation - L and R are interlaced by row ;3: side by side - L is on
the left, R on the right ;4: top bottom - L is on top, R on bottom ;5:
frame alternation - one view per frame

<span id="appendix_select_sout-x264-pass"></span> '''For the option
<code>[[#select_sout-x264-pass|--sout-x264-pass]]</code>:''' ;1: First
pass, creates stats file ;2: Last pass, does not overwrite stats file
;3: <var>N</var><sup>th</sup> pass, overwrites stats file

<span id="appendix_select_sout-x264-aq-mode"></span> '''For the option
<code>[[#select_sout-x264-aq-mode|--sout-x264-aq-mode]]</code>:''' ;0:
Disabled ;1: Current x264 default mode ;2: uses
<code>log(var)&sup2;</code> instead of <code>log(var)</code> and
attempts to adapt strength per frame

<span id="appendix_select_sout-x264-trellis"></span> '''For the option
<code>[[#select_sout-x264-trellis|--sout-x264-trellis]]</code>:''' ;0:
disabled ;1: enabled only on the final encode of a MB ;2: enabled on all
mode decisions

== Source code == \* {{VLCSourceFile|modules/codec/x264.c}}

{{Documentation}}
