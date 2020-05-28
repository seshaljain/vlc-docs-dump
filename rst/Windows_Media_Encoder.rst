{{websitehttp://www.microsoft.com/windows/windowsmedia/forpros/encoder/default.mspx}}

'''Windows Media Encoder''' allows encoding of live broadcasts and
pulled from clients or relays or pushed to servers over the [[MMS]]
protocol.

==Using VLC as a Relay for Live Streams==

Currently only the pull method is supported for using VLC as a relay. On
your server, use the command:

<pre> vlc mmsh://encoder-ip:8080 --sout
'#std{access=mmsh,mux=asfh,dst=:8080}' </pre>

Now [[Windows Media Player]] clients can connect to
<code>mms://server-ip:8080\ </code> to watch the broadcast.

Of course this requires the encoder to be reachable via the [[MMSH]]
protocol, with any required firewall or NAT configuration to support it.

===Encoder Push Support===

Some reverse engineering of the [[MMSH]] encoder push protocol has been
done, but not integrated into VLC, for example
[http://www.abk.nu/~nabe/prog_down/wmrelay.pl wmrelay.pl] by nabe@abk
and [http://sdp.ppona.com/ The SDP Multimedia Website].

==Bugs and Caveats==

VLC may not reflect the source bitrate properly. {{forum|18087}}

[[Category:Codecs]] [[Category:Windows]]
