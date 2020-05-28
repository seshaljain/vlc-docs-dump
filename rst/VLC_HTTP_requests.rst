There is a set of remote-control commands for VLC over `HTTP <HTTP>`__.

This is probably the most convenient and reliable `interface <interface>`__ for developers to use to control VLC.

The commands ARE listed - but the list is tucked away in a README file, in the http subfolder of the little HTTP server under the VLC executables folder.

How the Commands & Status Queries Work
--------------------------------------

The commands below are all applied by submitting an HTTP-GET for one of the `XML <XML>`__ files stored in the VLC http/requests folder. For example, VLC will report back the current playlist when you submit a `MRL <MRL>`__ of the form

`` ``\ ```http://127.0.0.1:9090/requests/playlist.xml`` <http://127.0.0.1:9090/requests/playlist.xml>`__\ ``     (that is for a VLC which was started, listening on port 9090). ``

Similarly,

`` ``\ ```http://127.0.0.1:9090/requests/status.xml`` <http://127.0.0.1:9090/requests/status.xml>`__

will report back the player status. Commands TO the player are sent by appending a trailing command parameter (following a '?' separator) to this latter status query command.

Examples
--------

SHOW CURRENT PLAYLIST:

`` ``\ ```http://127.0.0.1:9090/requests/playlist.xml`` <http://127.0.0.1:9090/requests/playlist.xml>`__

SHOW STATUS:

`` ``\ ```http://127.0.0.1:9090/requests/status.xml`` <http://127.0.0.1:9090/requests/status.xml>`__

STOP

`` ``\ ```http://127.0.0.1:9090/requests/status.xml?command=pl_stop`` <http://127.0.0.1:9090/requests/status.xml?command=pl_stop>`__

CLEAR PLAYLIST

`` ``\ ```http://127.0.0.1:9090/requests/status.xml?command=pl_empty`` <http://127.0.0.1:9090/requests/status.xml?command=pl_empty>`__

PLAY AN RTSP STREAM URL:

`` ``\ ```http://127.0.0.1:9090/requests/status.xml?command=in_play&input=rtsp://user:pass@somewebcameraaddress.com:9552/cam1/mpeg4`` <http://127.0.0.1:9090/requests/status.xml?command=in_play&input=rtsp://user:pass@somewebcameraaddress.com:9552/cam1/mpeg4>`__

By the bye: to start VLC's control HTTPD service on a specific port, use the syntax

`` vlc --intf http --http-host 10.1.1.156:9090``

Full command list
-----------------

HERE IS the FULL http-remote-control command list (as listed in README.txt in the VLC http subfolder) :-

Commands available through the requests/ path:

Lines starting with < describe what the page sends back

Lines starting with > describe what you can send to the page

All parameters need to be `URL encoded <https://en.wikipedia.org/wiki/URL_encoded>`__. Examples:

| ``# -> %23``
| ``% -> %25``
| ``+ -> %2B``
| ``space -> +``
| ``...``

**status.xml:**

< Get VLC status information, current item info and meta.

> add to playlist and start playback:

`` ?command=in_play&input=``\ 

> add to playlist:

`` ?command=in_enqueue&input=``\ 

> play playlist item :

`` ?command=pl_play&id=``\ 

NB: ?command=pl_play also works (no ID needed).

> toggle pause. If current state was 'stop', play item :

`` ?command=pl_pause&id=``\ 

NB: ?command=pl_pause NB: seems largely ignored ? stream often continues. (May depend on whether camera obeys pause command - NB this command may only cause a PAUSE to be sent out to the video stream source, so result will depend on whether source obeys.)

> stop playback:

| `` ?command=pl_stop``
| ``                           NB:   seems not to clear the playlist.    If in doubt clear the playlist and reload to start.``

> jump to next item:

`` ?command=pl_next``

> jump to previous item:

`` ?command=pl_previous``

> delete item from playlist:

`` ?command=pl_delete&id=``\ 

> empty playlist:

`` ?command=pl_empty``

> sort playlist using sort mode and order :

| `` ?command=pl_sort&id=``\ \ ``&val=``\ 
| `` If id=0 then items will be sorted in normal order, if id=1 they will be``
| `` sorted in reverse order``
| `` A non exhaustive list of sort modes:``
| ``   0 Id``
| ``   1 Name``
| ``   3 Author``
| ``   5 Random``
| ``   7 Track number``

> toggle random playback:

`` ?command=pl_random``

> toggle loop:

`` ?command=pl_loop``

> toggle repeat:

`` ?command=pl_repeat``

> toggle enable service discovery module :

| `` ?command=pl_sd&val=``\ 
| `` Typical values are:``
| ``   sap``
| ``   shoutcast``
| ``   podcast``
| ``   hal``

> toggle fullscreen:

`` ?command=fullscreen``

> set volume level to (can be absolute integer, percent or +/- relative value):

| `` ?command=volume&val=``\ 
| `` Allowed values are of the form:``
| ``   +``\ \ ``, -``\ \ ``, ``\ \ `` or ``\ \ ``%``

> seek to :

| `` ?command=seek&val=``\ 
| `` Allowed values are of the form:``
| ``   [+ or -][``\ \ ``:][``\ \ ``<M or m or '>:][``\ \ ``<nothing or S or s or ">]``
| ``   or [+ or -]``\ \ ``%``
| ``   (value between [ ] are optional, value between < > are mandatory)``
| `` examples:``
| ``   1000 -> seek to the 1000th second``
| ``   +1H:2M -> seek 1 hour and 2 minutes forward``
| ``   -10% -> seek 10% back``

**playlist.xml:**

< get the full playlist tree

**browse.xml:**

< ?dir=

.. raw:: html

   <dir>

> get

.. raw:: html

   <dir>

's filelist

*' vlm.xml:*'

< get the full list of VLM elements

**vlm_cmd.xml:**

< execute VLM command

`` ?command=``\ 

> get the error message from

`Category:Control VLC <Category:Control_VLC>`__
