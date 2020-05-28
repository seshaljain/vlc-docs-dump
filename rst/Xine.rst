{{websitehttp://www.xinehq.de}} {{open}}

'''xine''' is a [[media player]] for Unix released under the GNU General
Public License. It can play [[CD]]s, [[DVD|DVD-Video]], and [[VCD]], as
well as common computer multimedia formats like [[AVI]], [[WMV]],
[[MOV]], [[MP3]], [[FLAC]], [[Theora]], [[Speex]], and [[Vorbis]].

xine is built as a [[library|shared library]] ('''xine-lib''') that
supports different frontend player applications. To decode multimedia
data xine uses libraries from the [[FFmpeg]] project or binary
[[codec]]s.

At present, xine has the most complete [[SVCD]] and [[VCD]] support.
(Anyone want to beef up support in vlc to make this not true?)

xine can handle VCD/SVCD menus, mouse hot spots, navigation (called PBC
or playback control), and multiple audio channels. Many of these are
missing or incomplete in vlc version 0.8.4. (Actually, pretty much all
VCD/SVCD handling is broken in vlc version 0.8.4.) But one area where
vlc may be a little ahead of xine is in SVCD and [[CVD]] subtitle
handling. SVCD and CVD subtitles in xine however require a
[http://subhandler.sourceforge.net separate plugin] which is not part of
xine whereas in vlc it is part of the main code base.

== Compatibility == {{compat}}

== Web links == \* [http://xinehq.de/ Home Page] \*
[http://kaffeine.sourceforge.net/ Kaffeine] (xine-based frontend player)
\* [http://xineplayer.berlios.de/ XinePlayer] ([[macOS]] frontend) \*
[http://subhandler.sourceforge.net/ xine plugin for handling SVCD and
CVD subtitles]

[[Category:Player]]
