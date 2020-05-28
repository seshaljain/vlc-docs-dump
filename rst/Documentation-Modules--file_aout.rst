{{Moduletype=Audio output|description=Audio output to write to a file}}

Shortcuts for this module include <code>audiofile</code> and
<code>afile</code>.

== Options == {{Option value=string description=File to which the audio
samples will be written to ("-" for stdout) }} {{Option
select={u8,s16,float32,spdif} description=Output format }} {{Option
value=integer max=6 description=By default (0), all the channels of the
incoming will be saved but you can restrict the number of channels here
}} {{Option value=boolean default=enabled }}

== Source code == \* {{VLCSourceFile|modules/audio_output/file.c}}

{{Documentation}}
