{{Moduletype=Stream outputdescription=Delay a [[stream]]|sc=delay}}

== Options == {{Option value=integer description=Specify an identifier
integer for this [[elementary stream]]. }} {{Option value=integer
description=Specify a delay (in [[wiktionary:ms|ms]]) for this
elementary stream. Positive means delay and negative means advance. }}

== Examples == From the changelog:
<code><nowiki>#delay{id=12,delay=500}:standard...</nowiki></code>

== Source code == \* {{VLCSourceFile|modules/stream_out/delay.c}}

{{Documentation footer}}
