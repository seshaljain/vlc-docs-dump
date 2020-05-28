Decoding and encoding (text rendering) are handled by separate modules.
Both modules have the same shortcut, <code>svg</code>, though
{{VLCSourceFile|modules/MODULES_LIST}} calls them <code>svgdec</code>
and <code>svg</code>.

== Decoder == {{Moduletype=Inputdescription=[[SVG]] video decoder making
use of librsvg2}}

=== Options === {{Option value=integer max=65535 description=Specify the
width to decode the image to }} {{Option value=integer max=65535
description=Specify the height to decode the image to }} {{Option
value=float description=Scale factor to apply to image }} {{Clear}}

== Encoder == {{Moduletype=Inputos=Linux|description=Put [[SVG]] on the
video}}

=== Options === {{Option value=string description=Location of a file
holding a SVG template for automatic string conversion }} {{Clear}}

== Source code == \* {{VLCSourceFilemodules/text_renderer/svg.c}}
(encoder)

{{Documentation footer}}
