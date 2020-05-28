{{Moduletype=Video sub-filterdescription=Overlays [[wikipedia:RSSAtom]]
feeds on the videosc2=atom}}

== Options == {{Option value=string description=Pipe
<code>'''{{!}}'''</code> separated list of [[wikipedia:RSSAtom]] feed
URLs }}

=== Position === {{Option value=integer description=X offset, from the
left screen edge }} {{Option value=integer description=Y offset, down
from the top }} {{Option value=integer {0, 1, 2, 4, 8, 5, 6, 9, 10}]]
description=You can enforce the text position on the video (0=center,
1=left, 2=right, 4=top, 8=bottom; you can also use combinations of these
values, eg 6 = top-right) }}

=== Font === {{Option value=integer default=255 description=Opacity
(inverse of transparency) of overlay text. 0 = transparent, 255 =
totally opaque }} {{Option value=integer default=0xFFFFFF
key]]''')</sup> of the text that will be rendered on the video. This
must be an hexadecimal (like HTML colors). The first two chars are for
red, then green, then blue }} {{Option value=integer default=0
description=Font size, in pixels. Default is 0 (use default font size)
}}

=== Misc === {{Option value=integer description=Speed of the RSS/Atom
feeds in [[wiktionary:&micro;sname=rss-length default=60 name=rss-ttl
default=1800 name=rss-images default=enabled name=rss-title
select={<var>default_title</var>, <var>hide_title</var>,
<var>prepend_title</var>, <var>scroll_title</var>} description=Title
display mode. 0 is hidden if the feed has an image and feed images are
enabled, 1 is always visible, 2 is scroll with feed }}

== Examples == Example command line use '''(VLC 0.9.0 and above)''':
(untested with 3.x.x) % '''vlc somevideo.avi --sub-filter=rss
--rss-urls="http://news.google.com/news?ned=us&topic=h&output=rss"'''

== Source code == \* {{VLCSourceFile|modules/spu/rss.c}}

== See also == \* [[Documentation:Modules/marq]]

== Appendix == <div class="plainlist"> *^
[[#rss-color|--rss-color]]<span id="appendix_rss-color"></span>*\ ^
[[#rss-position|--rss-position]]<span id="appendix_rss-position"></span>
</div> {{Colour mapping}} {{Alignment mapping}}

{{Documentation footer}}
