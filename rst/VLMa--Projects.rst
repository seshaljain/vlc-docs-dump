This are ideas of projetcs if you want to start coding on VLMa.

You can contact `Adrien Grand (jpountz) <User:Jpountz>`__ if you are interested in one of them.

Automated deployment
--------------------

VLMa aims at automating as many operations required to setup a farm of streaming servers as possible. A painful operation which is not covered is the start of VLC on every streaming server.

VLMa is provided with a wrapper script around VLC which provides some services that VLC's telnet interface does not. The aim of this project is to set up an automated deployment capability in VLMa by providing mechanisms to deploy this script and running it on hosts which have been identified as streaming servers.

Remote diagnostic
-----------------

It can be frustrating to notice that some channels are not broadcasted without knowing why.

Currently, to know wether a channel is broadcasted or not, VLMa either joins the multicast group (in case of multicast streaming) or connects the the builtin server in VLC (HTTP or RTSP) so it has no access to debug information that would be useful to trace problems VLC encountered which could explain the fact that the channel is not broacasted.

For other issues (mainly retrieving metrics concerning the running VLC instance), a wrapper around VLC has been written (in Python). This wrapper is able to:

-  restart VLC,
-  expose metrics such as Memory usage of VLC / CPU load / etc.,
-  get the last lines of logs of VLC,
-  get VLC uptime,
-  get VLC version.

The idea would be to write a log listener for VLC in this wrapper that would be able to analyze errors reported by VLC and expose some methods related to this analysis. Then VLMa daemon could query the wrapper to try to guess why the channel is not broadcasted.

DVBlast and Darwin streaming server handling
--------------------------------------------

Being able to deal with non-VLC streaming servers would be a plus. See http://www.videolan.org/projects/dvblast.html and http://developer.apple.com/opensource/server/streaming/index.html.

See also
--------

-  `VLMa overview <VLMa>`__
-  `VLMa/Projects/DVBlast integration <VLMa/Projects/DVBlast_integration>`__

`Category:VLMa <Category:VLMa>`__
