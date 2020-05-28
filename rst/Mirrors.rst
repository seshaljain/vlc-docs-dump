.. raw:: mediawiki

   {{see also|MirrorManagement}}

Mirrors
=======

Our mirrors are kindly operated by sponsors, you can find the complete list `here <https://www.videolan.org/videolan/mirrors.html>`__. If you would like to provide a mirror to the VideoLAN project please read the following sections.

Requirements
------------

-  A public mirror in **HTTPS** (we won't accept new mirrors in HTTP)
-  About 70 GB of disk space at this time
-  At least 1 Gbps connectivity
-  At **least** 4 rsync per day (once every hour is better!)
-  Either an rsync or FTP server access to scan the actual state of your mirror (rsync is preferred)

Setting up a mirror
-------------------

| The first step is to clone the rsync repository using the following command:
| **rsync --verbose --recursive --times --links --hard-links --perms --stats --delete-after --timeout=300**\ rsync://rsync.videolan.org/videolan-ftp\ **/path/to/repository/destination**

| Edit your crontab (crontab -e) to sync the cron every hour:
| **11 \* \* \* \* sleep $(($RANDOM/1024)); rsync --verbose --recursive --times --links --hard-links --perms --stats --delete-after --timeout=300**\ rsync://rsync.videolan.org/videolan-ftp\ **/path/to/repository/destination**

Setup a web server to serve the repository preferably with `nginx <http://wiki.nginx.org/>`__ or `Apache <http://httpd.apache.org/>`__.

Finally setup a read-only rsync daemon using a similar configuration:

| ````
| ``[videolan]``
| ``    path = /path/to/repository/destination``
| ``    comment = VideoLAN repository``
| ``    uid = nobody``
| ``    gid = nogroup``
| ``    read only = yes``

Finally make sure the rsync server daemon is started during system startup!

NOTE: if you're using a CDN in front of the repository be sure to clear the cache at least once a day!

How do we manage mirrors
------------------------

On the VideoLAN side, in order to provide the best service to our users we're running `Mirrorbits <https://github.com/etix/mirrorbits>`__, a mirror management software that will transparently redirect users to the closest mirror.

It is also in charge of scanning the mirrors, ensuring they are up and running and it knows which files are served by your mirror. The system will automatically scan you mirror (using rsync or FTP) every now and then and do some health checks on the HTTP side every minute. If you have any concern related to a high bandwidth usage please tell us, we will reduce the weight of your mirror.

Contact us
----------

Once your mirror is setup, please `contact us <mailto:mirrors@videolan.org>`__ and be sure to send:

-  A name and contact email address
-  HTTP, FTP (if applicable) and rsync URLs to the file tree on your server
-  The name, URL and logo of the operator / organization / sponsor you represent (preferably in 137x54)

After reviewing your application your mirror will be added to our load balancer.

`Category:About VideoLAN <Category:About_VideoLAN>`__
