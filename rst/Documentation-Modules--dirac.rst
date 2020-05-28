:''Were you looking for the current module, {{docmod|schroedinger}}?''

The dirac demuxer will be removed. It has already been
{{Commitdiffl=removed}} in 4.0.0-dev.

== Demux == {{Moduletype=Access demuxdescription=[[Dirac]] video
demuxer|sc=dirac}}

=== Options === {{Option value=integer description=Value to adjust dts
by }} {{Clear}}

== Mux == {{Moduletype=Muxerlast_version=2.1.6sc=none}}

A few notes (of no real importance as this is a removed module): \* the
option <code>--sout-dirac-cpd</code> is, unusually, a float with an
integer range \* the option <code>--sout-dirac-me-combined</code> is
[[wikipedia:Conditional compilation|dependent]] on Dirac research
version of at least 1.0.1 \* the options
<code>--sout-dirac-multi-quant</code> and
<code>--sout-dirac-spartition</code> are disabled when set to
<code>-1</code>. They have a code comment: *: /* NB, unforunately vlc
doesn't have a concept of 'don't care' */* the options
<code>--sout-dirac-mc-blk-xblen</code> and
<code>--sout-dirac-mc-blk-yblen</code> were originally aliases for
<code>--sout-dirac-mc-blk-width</code> and
<code>--sout-dirac-mc-blk-height</code> prior to 1.0.0

=== Options === {{Option value=float min=0. description=If
[[bitrate]]=0, use this value for constant quality }} {{Option
value=integer min=-1 description=A value > 0 (in kbps) enables constant
bitrate mode }} {{Option value=boolean description=[[Lossless]] coding
ignores bitrate and quality settings, allowing for perfect reproduction
of the original }} {{Option value=string default=diaglp
name=sout-dirac-prefilter-strength default=1 max=10
name=sout-dirac-chroma-fmt select={420,422,444} description=Picking
[[chroma]] format will force a conversion of the video into that format:
"[[4:2:0]]", "[[4:2:2]]" or "[[4:4:4]]" }} {{Option value=integer min=-1
description=Distance between ''[[P-frame]]s'' }} {{Option value=integer
min=-1 description=Number of ''P-frames'' per [[GOP]] }} {{Option
value=string default=auto name=sout-dirac-mv-prec select={1,1/2,1/4,1/8}
description=Motion vector precision in pels }} {{Option value=integer
min=-1 description=Width of motion compensation blocks }} {{Option
value=integer min=-1 description=Height of motion compensation blocks }}
{{Option value=integer min=-1 description=Amount (%) that each motion
block should be overlapped by its neighbours }} {{Option value=string
description=(Not recommended) Perform a simple (non hierarchical block
matching motion vector search with search range of &plusmn;<var>x</var>,
&plusmn;<var>y</var>) }} {{Option value=boolean description=Use chroma
as part of the motion estimation process }} {{Option value=integer
min=-1 description=Intra picture DWT filter }} {{Option value=integer
min=-1 description=Inter picture DWT filter }} {{Option value=integer
min=-1 description=Number of DWT iterations (Also known as DWT levels)
}} {{Option value=boolean description=Disable arithmetic
coding&mdash;Use variable length codes instead, useful for very high
bitrates }}

==== Advanced options ==== {{Option value=integer min=-1
description=Total horizontal block length including overlaps }} {{Option
value=integer min=-1 description=Total vertical block length including
overlaps }} {{Option value=integer min=-1 description=Enable multiple
quantizers per subband (one per codeblock) }} {{Option value=integer
min=-1 description=Enable spatial partitioning }} {{Option value=float
min=-1 description=cycles per degree }}

== Source code == \* {{VLCSourceFilemodules/demux/dirac.c}} (demux) \*
{{VLCSourceFilemodules/codec/dirac.c}} (mux)

{{Documentation}}
