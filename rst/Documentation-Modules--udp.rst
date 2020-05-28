== Access == {{Moduletype=Accesssc=udpsc3=udp4|sc4=udp6}}

The options <code>--server-port</code> and <code>--udp-buffer</code>
were deprecated in 2.0.0 and 3.0.0. <code>--udp-timeout</code> was added
in 3.0.0.

{{Option value=integer description=[[UDP]] Source timeout (sec) }}
{{Clear}}

== Access output == {{Moduletype=Access outputsc=udp}}

{{Option value=integer description=Default caching value for outbound
[[UDP]] streams. This value should be set in milliseconds }} {{Option
value=integer description=Packets can be sent one by one at the right
time or by groups. You can choose the number of packets that will be
sent at a time. It helps reducing the scheduling load on heavily-loaded
systems }} {{Clear}}

== Source code == \* {{VLCSourceFilemodules/access_output/udp.c}}

{{Documentation}}
