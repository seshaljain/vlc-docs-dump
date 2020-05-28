{{Moduletype=Video output filter|description=[[Deinterlacing]] video
filter}}

== Options == <onlyinclude>{{Option value=string description=Streaming
[[deinterlace mode]]. Deinterlace method to use for streaming }}
{{Option value=integer description=Phosphor [[chroma]] mode for 4:2:0
input. Choose handling for colours in those output frames that fall
across input frame boundaries. \*\* Latest (1): take chroma from new
(bright) field. Good for interlaced input, such as videos from a
camcorder \*\* AltLine (2): take chroma line 1 from top field, line 2
from bottom field, etc. Default, good for NTSC telecined input (anime
DVDs, etc.) \*\* Blend (3): average input field chromas. May distort the
colours of the new (bright) field, too \*\* Upconvert (4): output in
4:2:2 format (independent chroma for each field). Best simulation, but
requires more CPU and memory bandwidth
name=sout-deinterlace-phosphor-dimmer select={1,2,3,4} default=2
}}</onlyinclude>

{{Documentation footer}}
