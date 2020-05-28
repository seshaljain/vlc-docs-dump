{{Moduletype=Video sub-filterdescription=Overlays text on the
videosc2=time}}

The ''marq'' subtitle filter can be used to display text on a video. The
{{docmodformat string]] recognition. There are two methods of specifying
position: coordinate and (since VLC 0.9.0) [[#marq-position|numbered
positions]].

== Options == <onlyinclude>{{Option value=string description=Marquee
text to display. }} {{Option value=string description=File to read the
marquee text from. }}<noinclude> === Position === </noinclude> {{Option
value=integer description=X offset, from the left screen edge. }}
{{Option value=integer description=Y offset, down from the top. }}
{{Option value=integer description=Marquee position: 0=center, 1=left,
2=right, 4=top, 8=bottom, you can also use combinations of these values,
eg 6 = top-right. }}<noinclude> === Font === </noinclude>{{Option
value=integer max=255 description=Opacity (inverse of transparency) of
overlaid text. 0 {{=}} transparent, 255 {{=}} totally opaque. }}
{{Option value=integer default=0xFFFFFF key]]''')</sup></noinclude> of
the text that will be rendered on the video. This must be an hexadecimal
(like HTML colors). The first two chars are for red, then green, then
blue. }} {{Option value=integer max=4096 description=Font size, in
pixels. 0 uses the default font size. }}<noinclude> === Misc ===
</noinclude>{{Option value=integer description=Number of milliseconds
the marquee must remain displayed. 0 means forever. }} {{Option
value=integer description=Number of milliseconds between string updates.
This is mainly useful when using meta data or time
[[Documentation:Format String|format string]] sequences.
}}</onlyinclude>

== Examples ==

=== Versions 2.0 and later ===

Example command line use '''(VLC 2.0.0 and newer)''':
   {{%}} vlc
   '--sub-source=marq{marquee="%Y-%m-%d,%H:%M:%S",position=9,color=0xFFFF00,size=12}'
   somevideo.avi

This example displays the current date and time in yellow in the top
left corner of video.

The equivalent long form would be;
   {{%}} vlc --sub-source=marq --marq-marquee="%Y-%m-%d,%H:%M:%S"
   --marq-position=9 --marq-color=0xFFFFFF --marq-size=12 somevideo.avi

=== Versions 0.9.0 to 1.1.13 ===
   {{$}} vlc --sub-filter 'marq{marquee=$t
   ($P%%),color=0xFFFF00}:marq{marquee=%H:%M:%S,position=6}'
   somevideo.avi

This command line will show the stream's title (<code>$t</code>) and
current position (<code>$P</code>) in the upper left corner and the
current time in the upper right corner. The <u>''single''</u> quotes
<code>'</code> enclose our <code>$</code> characters to prevent them
from being interpreted as Bash variables.<br /> On Windows the command
line would be: {{Promptwindows}} --sub-filter=marq{marquee=$t
($P%%),color=0xFFFF00}:marq{marquee=%H:%m%s,position=6} somevideo.avi

== Gallery == <gallery> File:Marq demonstration - VLC 3.0.6
Linux.pngalt=Marq can be chained, allowing several marquees to be
displayed at the same time. Nine positions and text colours are shown
against a black background. </gallery>

== See also == \* [[Documentation:Format String]] \*
[[Documentation:Modules/rss]]

== Source code == \*
{{VLCSourceFilep=vlc/vlc-0.8.git|modules/video_filter/marq.c}}

== Appendix == <div class="plainlist"> \*^
[[#marq-color|--marq-color]]<span id="appendix_marq-color"></span>
</div> {{Colour mapping}}

{{Documentation footer}}
