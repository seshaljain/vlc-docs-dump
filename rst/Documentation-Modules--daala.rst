{{Moduletype=Muxerdescription=[[Daala]] video encoder}}

Support for this module comes from the libdaala [[library]].

== Options == {{Option value=integer min=0 description=Enforce a quality
between 0 (lossless) and 511 (worst) }} {{Option value=integer min=1
description=Enforce a [[keyframe]] interval between 1 and 1000 }}
{{Option value=string select={420,444} \|description=Picking [[chroma]]
format will force a conversion of the video into that format.
<code>420</code> means <code>[[4:2:0]] Y'CbCr</code> and
<code>444</code> means <code>[[4:4:4]] Y'CbCr</code> }}

== Source code == \* {{VLCSourceFile|modules/codec/daala.c}}

{{Documentation}}
