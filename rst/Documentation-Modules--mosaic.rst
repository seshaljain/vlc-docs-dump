{{Mosaic framework}} {{Moduletype=Video subfilterdescription=Mosaic
video sub source}}

Use this filter to blend videos on top of another video. This can be
used to create TV channels mosaics, setup a weather channel-like stream
(with the {{docmod|bluescreen}} video filter) and lots of other fun
stuff.

Since VLC 0.8.6, you can also use the [[Documentation:Modules/http
intf|HTTP interface]]'s mosaic wizard to configure a mosaic easily.
\__TOC_\_ {{Clear}}

== Options == {{Option value=integer max=255 description=Alpha blending
(transparency) of the mosaic foreground pictures. 0 means transparent,
255 opaque. }} {{Option value=integer max=<var>INT_MAX</var>
description=Total height of the mosaic, in pixels. }} {{Option
value=integer max=<var>INT_MAX</var> description=Total width of the
mosaic, in pixels. }} {{Option value=integer { 0, 1, 2, 4, 8, 5, 6, 9,
10 }]] description=You can enforce the mosaic alignment on the parent
video. }} {{Option value=integer max=<var>INT_MAX</var> description=X
Coordinate of the top-left corner of the mosaic. }} {{Option
value=integer max=<var>INT_MAX</var> description=Y Coordinate of the
top-left corner of the mosaic. }} {{Option value=integer
max=<var>INT_MAX</var> description=Border width between mosaic elements,
in pixels. }} {{Option value=integer max=<var>INT_MAX</var>
description=Border height between mosaic elements, in pixels. }}
{{Option value=integer default=0 mosaic-offsets]]). }} {{Option
value=integer max=<var>INT_MAX</var> description=Number of image rows in
the mosaic (only used if [[#mosaic-positionname=mosaic-cols min=1
default=2 positioning method]] is set to "fixed"). }} {{Option
value=boolean description=Keep the original [[aspect ratio]] when
resizing mosaic elements. }} {{Option value=boolean description=Do not
resize or do any other transformation on the mosaic pictures. Should be
enabled when using the {{docmodname=mosaic-order default=""
mosaic-bridge}} module. }} {{Option value=string description=You can
enforce the <code>(x,y)</code> offsets of the elements on the mosaic
(only used if [[#mosaic-positionname=mosaic-delay default=0
\|description=Pictures coming from the mosaic elements will be delayed
according to this value (in milliseconds). For high values you will need
to raise caching at input. }}

== Source code == \* {{VLCSourceFile|modules/spu/mosaic.c}}

== Appendix == <div class="plainlist"> \*^
[[#select_mosaic-align|--mosaic-align]]<span
id="appendix_select_mosaic-align"></span> </div> {{Alignment mapping}}

{{Documentation footer}}
