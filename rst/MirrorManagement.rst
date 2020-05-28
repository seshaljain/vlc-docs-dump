.. raw:: mediawiki

   {{see also|Mirrors}}

Infrastructure
==============

The current infrastructure is made of:

-  The master rsync server
-  The distribution server (aka the redirector)
-  The actual mirrors (few dozens)

The master rsync server always contains all the latest version of each file available.

The distribution server replicates the master server via rsync every 15 minutes and also scan the content of each mirrors and their current state every so often.

The mirrors are configured to scan the master at regular interval (at least 4th times a day for most of them).

Requests handling
-----------------

As soon as a request hits the distribution server, a mirror is chosen depending on the IP address of the client. The selected mirror must contain the latest version of the file and be up at the moment of the request to be selected. The distribution server then issues a 3xx redirection code to the client.

List of mirrors
---------------

The most recent list of mirrors can be accessed `here <https://www.videolan.org/videolan/mirrors.html>`__. It is updated after any modification of the mirror list on the distribution server.

Statistics
==========

Files availability
------------------

You can access the current file availability on each mirror by appending **?mirrorlist** to any URL of a file served by the get.videolan.org domain.

For instance the following link will return the list of mirrors handling this file sorted by the most appropriate for the caller (you!).

https://get.videolan.org/vlc/\ /win32/vlc--win32.exe?mirrorlist

To get the view from any other IP address append **&fromip=x.x.x.x** to the last URL.

https://get.videolan.org/vlc/\ /win32/vlc--win32.exe?mirrorlist&fromip=80.237.216.0

This will return the same list as the previous call but from the point of view of the *80.237.216.0* network (located somewhere in Germany).

Mirrors statistics
------------------

A global map of all mirrors, the number of downloads and the total size served by each mirror can be accessed on the following URL:

https://get.videolan.org/?mirrorstats (Beware: URL subject to change)

Downloads statistics
--------------------

Downloads statistics for each file are available as *json* by appending **?stats** to any URL of a file served by the get.videolan.org domain.

You can even specify a period if you'd like to:

| https://get.videolan.org/vlc/\ /win32/vlc--win32.exe?stats= (for the whole year)
| https://get.videolan.org/vlc/\ /win32/vlc--win32.exe?stats=- (for )
| https://get.videolan.org/vlc/\ /win32/vlc--win32.exe?stats=--01 (for the 1st of )

`Category:About VideoLAN <Category:About_VideoLAN>`__
