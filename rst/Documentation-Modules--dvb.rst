{{See alsoname=dvbfirst_version=0.6.2description=[[DVB]] input with
[[v4l2]] support|sc=dvb}}

Shortcuts: \* <code>dvb</code> (Generic name) \*\* <code>dvb-s</code>,
<code>qpsk</code>, <code>satellite</code> (Satellite) \*\*
<code>dvb-c</code>, <code>cable</code> (Cable) \*\* <code>dvb-t</code>,
<code>terrestrial</code> (Terrestrial)

== Options == {{Option value=boolean description=Some [[DVB]] cards do
not like to be probed for their capabilities, you can disable this
feature if you experience some trouble. }} {{Option value=string
description=Filename of config file in share/dvb/dvb-s. }} {{Option
value=string description=Filename containing initial scan tuning data.
}} {{Option value=boolean description=Use NIT for scanning services }}

== See also == \* {{docmod|dvbsub}}

== Source code == \* {{VLCSourceFilemodules/access/dvb}} (folder) \*
{{VLCSourceFileplaylist}})

{{Documentation}}
