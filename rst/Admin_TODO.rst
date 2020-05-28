.. raw:: mediawiki

   {{Historical}}

Various stuff to do on the servers to improve services or reliability

-  

   .. raw:: html

      <div style="text-decoration:line-through;">

   upgrade Albiero and Sirius to Lenny `jb <User:J-b>`__ 20:48, 15 May 2009 (CEST)

   .. raw:: html

      </div>

   -  Need a reboot to change kernel => beware of eth0 vanishing
   -  Need physical access ?

-  Hardware

   -  Switch gigabit between the eth1 of ganesh, albiero and sirius
   -  way to get albiero and sirius console from ganesh
   -  way to have ganesh console on albiero (iLO \*does\* fail)

-  Database

   -  move them all to albiero (done for trac-vlc \ `jb <User:J-b>`__ 20:48, 15 May 2009 (CEST))\ `jb <User:J-b>`__ 13:04, 22 May 2009 (UTC)
   -  move them all to pg 8.3 (requires lenny). `jb <User:J-b>`__ 20:48, 15 May 2009 (CEST)
   -  do we need/can have a fall back if albiero is down ?

-  Web

   -  optimize pg request
   -  make sure the web work even if the databases are down

      -  important for fastcgi (maybe tweak various time-out)
      -  avoid ugly error on apache

   -  mirroring/reverse-proxying/round-robining

      -  i think sirius is missing some crontab to get the svn and generate certain files\ `xtophe <User:Xtophe>`__
      -  need to create dns entries for {www,images,download}{1,2,3,..} and matching vhost

   -  for when sh**t happens:

      -  prepare "maintenance" pages for www, trac, wiki, forum
      -  prepare simplified pages with only a few links

-  Mail

   -  

      .. raw:: html

         <div style="text-decoration:line-through;">

      create an admin ml. Done `jb <User:J-b>`__

      .. raw:: html

         </div>

   -  make sure the cron send to admin@ if and only if something bad happened

-  Trac

   -  install openid plugin (if it still allow to use normal auth)
   -  send and parse commit log to ganesh
   -  reactivate all the trac
   -  trac2 on sirius/albiero

-  Forum, wiki

   -  forum2, wiki2 on ganesh/albiero

-  Monitoring

   -  Extract health information for disks on ganesh, albiero, skanda, sirius

      -  on albiero and sirius it will help when they are in lenny

-  Bittorent tracker
-  Fix Patchwork
-  Update `VideoLAN_Servers <VideoLAN_Servers>`__

`Category:Roots <Category:Roots>`__ `Category:Proposed deletion <Category:Proposed_deletion>`__
