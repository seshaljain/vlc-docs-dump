.. raw:: mediawiki

   {{RightMenu|documentation streaming howto toc}}

Note: Under Unix/Linux, you must have write access to the device corresponding to your DVD drive. For that, you should be in the *disk* or *cdrom* group (look at the permissions in **/dev**). If you're not, add yourself to the group:

```#`` <terminal>`__\ `` adduser your_login disk_or_cdrom``

and then restart your session.

Stream a DVD with VLC
---------------------

``{{%}} vlc -vvv --color dvdsimple:/dev/dvd --sout ``\ ```udp://192.168.0.12`` <udp://192.168.0.12>`__\ `` --ttl 12 --sout-all``

where:

-  **/dev/dvd** is the name of your DVD drive (put **D:** under Windows if **D** is the letter of your DVD drive) or the directory where you copied your DVD,
-  **192.168.0.42** is either:

   -  the IP address of the machine you want to unicast to;
   -  or the DNS name the machine you want to unicast to;
   -  or a multicast IP address.

-  **12** is the value of the TTL (Time To Live) of your IP packets (which means that the stream will be able to cross 11 routers).
-  **sout-all** allows you to stream all soundtracks and subtitles

If you want to stream the DVD continuously, add the **--loop** option.

.. raw:: mediawiki

   {{Documentation}}
