Issue
-----

VLMa has been architectured assuming that VLC would be the only streaming facility it would use and the telnet interface is the way it communicates with VLC.

With `DVBlast <DVBlast>`__ coming as a better solution than VLC for broadcasting `DVB <DVB>`__ channels, this assumption is not right anymore, and DVBlast has no telnet interface (and the README clearly states the DVBlast will keep as simple as possible which means it will probably never implement

The idea behind this project is to provide a facade for communicating from the master (VLMa) to the slaves (the streamers: VLC, DVBlast, etc.).

Solution
--------

There already is a little piece of code in charge of doing process management in the Git repository which can probably be reused.

Required features
~~~~~~~~~~~~~~~~~

-  Monitoring of the server (CPU load, Incoming/Outgoing traffic, etc.)
-  Monitoring of the streamer (restarting of the process when needed, CPU & memory used, etc.)
-  Extensibility, it should be very easy to add the support of another streaming tool,
-  Information retrieval (logs, uptime, version of the software installed)

Implementation
~~~~~~~~~~~~~~

Python programming language (to reuse some code which has already been written).

REST/XML API:

-  Applications only need XML and HTTP bindings (which are prensent in almost every serious programming language) to use the API,
-  XML is human-readable (on the contrary to protobuf, etch or thrift).

Paths
~~~~~

I'm not very good at finding resources' names, feel free to modify them.

-  GET **/server/monitoring** monitoring metrics of the whole server (CPU load, etc.)
-  GET **/streamers** list of the streaming programs running (VLC, DVBlast)
-  GET **/streamers/<id>** description of the streamer whose id is <id>
-  GET **/streamers/<id>/channels** channels currently handled by streamer <id>
-  PUT **/streamers/<id>/channels/<channel>** add/modify the channel whose id is <channel>
-  DELETE **/streamers/<id>/channels/<channel>** remove the channel whose id is <channel>
-  GET **/streamers/<id>/monitoring** monitoring metrics specific to streamer <id>
-  GET **/streamers/<id>/logs** logs of streamer <id>
-  GET **/streamers/<id>/restart** restart the streamer whose id is <id>

`Category:VLMa <Category:VLMa>`__
