This module allows {{VLC}} to connect to [[JACK Audio Connection Kit]].

== Access == {{Moduletype=Accessos=Unix, Linux, BSDsc=jack}}

The option <code>--jack-input-caching</code> no longer exists, removed
with a commitdiff entitled {{Commitdiffl=Unify
(ACCESS{{!}}DEMUX)_GET_PTS_DELAY}}. <!--{{Option value=integer
name=jack-input-use-vlc-pace default=disabled
name=jack-input-auto-connect default=disabled
\|description=Automatically connect VLC input [[port]]s to available
output ports }} {{Clear}}

== Audio output == {{Moduletype=Audio outputos=Unix, Linux, BSDsc=none}}
{{Option value=boolean description=If enabled, this option will
automatically connect sound output to the first writable JACK clients
found }} {{Option value=string description=If automatic connection is
enabled, only JACK clients whose names match this [[wikipedia:regular
expressionname=jack-name default="" \|description=JACK client name }}
{{Clear}}

== Source code == \* {{VLCSourceFilemodules/audio_output/jack.c}}

{{Documentation}}
