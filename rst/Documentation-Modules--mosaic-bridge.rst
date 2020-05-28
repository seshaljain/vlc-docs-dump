{{Mosaic framework}} {{Moduletype=Stream outputdescription=Send a
picture to the mosaic framework|sc=mosaic-bridge}}

Use this filter to send a picture to the mosaic framework. Processing
can be applied before sending the picture, such as resizing, [[chroma]]
conversion and video filters. \__TOC_\_ {{Clear}}

== Options == {{Option value=string description=Specify an identifier
string for this subpicture. Used by clients of the mosaic framework to
identify the picture's source. }} {{Option value=integer
description=Resize video to this width if value is non-zero. Make sure
to use the '''mosaic-keep-picture''' option to prevent the mosaic filter
from resizing a second time. }} {{Option value=integer
description=Resize video to this height if value is non-zero. Make sure
to use the '''mosaic-keep-picture''' option to prevent the mosaic filter
from resizing a second time. }} {{Option value=string description=Sample
[[aspect ratio]] of the destination. }} {{Option value=string
description=Force the use of a specific [[chroma]]. Use [[YUVA]] if
you're planning to use the {{docmodbluescreen}} video filter. }}
{{Option value=string description=Video filter chain to apply after
resizing and chroma conversion. }} {{Option value=integer min=0
description=Transparency of the mosaic picture. }} {{Option
value=integer description=X coordinate of the upper left corner in the
mosaic if non-negative. }} {{Option value=integer description=Y
coordinate of the upper left corner in the mosaic if non-negative. }}

== Source code == \*
{{VLCSourceFile|modules/stream_out/mosaic-bridge.c}}

{{Documentation footer}}
