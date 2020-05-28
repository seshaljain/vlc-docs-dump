{{Moduletype=Audio outputdescription=[[wikipedia:PulseAudio|PulseAudio]]
audio output}}

Shortcuts to this module include <code>pulseaudio</code> and
<code>pa</code>. Basic PulseAudio ''input'' support was added in VLC
2.0.0.

== Introduction == PulseAudio is a sound server associated mainly with
GNU/Linux users, but it can also be used on \*BSD and macOS. The pulse
and {{docmodesd}} and {{docmod|arts}} modules were removed prior to the
release of VLC 1.0.0.

== Options == None.

== Source code == \* {{VLCSourceFilemodules/audio_output/vlcpulse.c}}
(separate module, support library for [[libVLC]] plugins) \*
{{VLCSourceFile|modules/access/pulse.c}}

{{Documentation footer}}
