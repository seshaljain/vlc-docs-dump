[[Dummy]] modules are the VLC equivalent of <code>/dev/null</code> on
GNU/Linux: they represent doing nothing.

== List == <!-- Editors: category wikicode must be entered manually. -->
{\| class="wikitable sortable cellpadding-3px" Type !! scope="col" \|
Description !! scope="col" \| Shortcut(s) Access [[Category:Accesses]]
\|\| Dummy input \|\| dummy, vlc Access output [[Category:Access
output]] \|\| Dummy stream output \|\| dummy Audio output
[[Category:Audio output]] \|\| Dummy audio output \|\| dummy Decoder
[[Category:Codecs]] \|\| Dummy decoder \|\| dummy, dump Encoder \|\|
Dummy encoder \|\| dummy Control interface [[Category:Interfaces]]
[[Category:Control VLC]] \|\| Dummy interface \|\| (none) Muxer
[[Category:Muxers]] \|\| Dummy/[[Raw]] muxer \|\| dummy, raw, es Stream
output [[Category:Stream output]] \|\| Dummy stream output \|\| dummy,
drop Text renderer \|\| Dummy font renderer \|\| (none) Video output
[[Category:Video output]] \|\| Dummy video output \|\| dummy, stats
Video output (legacy video plugins) [[Category:Video output]] \|\| Dummy
window \|\| dummy \|}

== Descriptions == === Interface === A dummy interface works well with
[[command-line]] usage. It consumes fewer computing resources, something
that can be used to reduce a bottleneck effect during [[transcoding]],
or simply when opening a window makes little sense.

This will play an [[Ogg]] file with no interface:
   {{$}} vlc -I dummy audio.ogg vlc://quit

No window is launched, and control is returned to the calling
application after the file plays.

This will play a [[Schroedinger]] file with a minimalist interface:
   {{$}} vlc -I dummy video.drc vlc://quit

A window with no buttons or toolbars is launched (no [[skin]]), because
[[video output]] requires a window. [[Hotkey]]s may be used to control
playback by default, something that can be disabled if necessary with
<code>--no-keyboard-events</code>.

=== Stream output === Doesn't do anything. Can be used to test other
stream output chain modules without actually streaming anything.

== Options == === Dummy decoder === {{Option value=boolean
description=Save the raw [[codec]] data if you have selected/forced the
dummy decoder in the main options. }}

=== Video output === {{Option value=string description=Force the dummy
video output to create images using a specific [[chroma]] format instead
of trying to improve performances by using the most efficient one. }}

== Source code == \* {{VLCSourceFileAccess}} \* {{VLCSourceFileAccess
output}} \* {{VLCSourceFileAudio output}} \* {{VLCSourceFileDecoder}} \*
{{VLCSourceFileEncoder}} \* {{VLCSourceFileInterface}} \*
{{VLCSourceFileOutput muxer}} \* {{VLCSourceFileStream output}} \*
{{VLCSourceFileText rendering}} \* {{VLCSourceFileVideo output}} \*
{{VLCSourceFileVideo output for legacy video plugins}}

{{Documentation}}
