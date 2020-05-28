.. raw:: mediawiki

   {{website|Windows Media Encoder|http://www.microsoft.com/windows/windowsmedia/forpros/encoder/default.mspx}}

**Windows Media Encoder** allows encoding of live broadcasts and pulled from clients or relays or pushed to servers over the `MMS <MMS>`__ protocol.

Using VLC as a Relay for Live Streams
-------------------------------------

Currently only the pull method is supported for using VLC as a relay. On your server, use the command:

::

   vlc mmsh://encoder-ip:8080 --sout '#std{access=mmsh,mux=asfh,dst=:8080}'

Now `Windows Media Player <Windows_Media_Player>`__ clients can connect to ```mms://server-ip:8080`` <mms://server-ip:8080>`__ to watch the broadcast.

Of course this requires the encoder to be reachable via the `MMSH <MMSH>`__ protocol, with any required firewall or NAT configuration to support it.

Encoder Push Support
~~~~~~~~~~~~~~~~~~~~

Some reverse engineering of the `MMSH <MMSH>`__ encoder push protocol has been done, but not integrated into VLC, for example `wmrelay.pl <http://www.abk.nu/~nabe/prog_down/wmrelay.pl>`__ by nabe@abk and `The SDP Multimedia Website <http://sdp.ppona.com/>`__.

Bugs and Caveats
----------------

VLC may not reflect the source bitrate properly.

`Category:Codecs <Category:Codecs>`__ `Category:Windows <Category:Windows>`__
