{{Historical}} Various stuff to do on the servers to improve services or
reliability

\* <div style="text-decoration:line-through;">upgrade Albiero and Sirius
to Lenny [[User:J-b|jb]] 20:48, 15 May 2009 (CEST)</div> \*\* Need a
reboot to change kernel => beware of eth0 vanishing \*\* Need physical
access ? *HardwareSwitch gigabit between the eth1 of ganesh, albiero and
siriusway to get albiero and sirius console from ganeshway to have
ganesh console on albiero (iLO*\ does\* fail)

\* Database **<span style="text-decoration:line-through;">move them all
to albiero (done for trac-vlc [[User:J-b|jb]] 20:48, 15 May 2009
(CEST))</span>[[User:J-b|jb]] 13:04, 22 May 2009 (UTC)**\ <span
style="text-decoration:line-through;">move them all to pg 8.3 (requires
lenny). [[User:J-b|jb]] 20:48, 15 May 2009 (CEST)</span> \**do we
need/can have a fall back if albiero is down ?

\* Web **optimize pg request**\ make sure the web work even if the
databases are down **\*important for fastcgi (maybe tweak various
time-out)**\ *avoid ugly error on
apachemirroring/reverse-proxying/round-robining*\ **<span
style="text-decoration:line-through;">i think sirius is missing some
crontab to get the svn and generate certain
files</span>[[User:Xtophe|xtophe]]**\ \* need to create dns entries for
{www,images,download}{1,2,3,..} and matching vhost **for when sh**\ t
happens: **\*prepare "maintenance" pages for www, trac, wiki,
forum**\ \*prepare simplified pages with only a few links

\* Mail **<div style="text-decoration:line-through;">create an admin ml.
Done [[User:J-b|jb]] </div>** make sure the cron send to admin@ if and
only if something bad happened

*Tracinstall openid plugin (if it still allow to use normal auth)send
and parse commit log to ganeshreactivate all the trac*\ \*trac2 on
sirius/albiero

*Forum, wiki*\ \*forum2, wiki2 on ganesh/albiero

*MonitoringExtract health information for disks on ganesh, albiero,
skanda, sirius*\ \**on albiero and sirius it will help when they are in
lenny

*Bittorent tracker*\ Fix Patchwork \*Update [[VideoLAN_Servers]]

[[Category:Roots]] [[Category:Proposed deletion]]
