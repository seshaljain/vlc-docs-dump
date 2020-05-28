== Summary == A demonstration of the [[Documentation:Modules/marq|marq]]
module for VLC 3.0.6, Linux, GNOME Shell 3.22.2. It shows nine
differently-coloured marquees indicating position codes against a simple
512x512 px black background.

This was generated with a single command-line instruction (using
chaining): <syntaxhighlight lang="bash"> vlc Black.png --marq-size=24
"--sub-source=marq{marquee='position
0',position=0,color=0x800000}:marq{marquee='position
1',position=1,color=0xFF0000}:marq{marquee='position
2',position=2,color=0xFF00FF}:marq{marquee='position
4',position=4,color=0xFFFF00}:marq{marquee='position
5',position=5,color=0x808000}:marq{marquee='position
6',position=6,color=0x008000}:marq{marquee='position
8',position=8,color=0x008080}:marq{marquee='position
9',position=9,color=0x00FF00}:marq{marquee='position
10',position=10,color=0x800080}" --width=512 --height=512
--no-video-title-show </syntaxhighlight>

I took the picture myself, releasing under
[https://creativecommons.org/licenses/by/4.0/ CC-BY 4.0] (open to
alternate licensure on request).

[[Category:GNU/Linux images]] [[Category:Qt images]] [[Category:VLC
3.0.x images]] \__NOINDEX_\_ == Licensing == {{CC-BY-4.0}}
