{{SoCProjectstudent=[[User:Sephiroth87mentor=[[User:Dionoea|Antoine
Cellerier]]}}

==Project Abstract== As MTP (Media Transfer Protocol) devices become
more and more popular, and the protocol itself is about to become a
standard, using them is still a problem for some people, since they
cannot be mounted or opened as disks, but can be natively used only on
Vista and Windows XP with WMP10, or using other programs.

Adding the MTP support to VLC would not only give the opportunity to use
these device on almost every platform, but also allow to have a free,
open source and largely diffuse program to manage them.

My work on the MTP support will enable VLC not only to play music from
the device, but also to add new music, manage the content of the device,
edit tags, playlists and anything else that would be needed by an Mp3
player user.

The coding would be done in C, mainly as a service discovery for
VLC,with an access module to enable the reproduction of files;
everything will be done using libmtp (POSIX compliant, so it should work
nice on almost every system) as a base, and probably HAL to allow the
program to detect the devices as soon as they plugged into the pc.

==Schedule== *Linux/POSIX version :*\ Service Discovery: recognize
device connections, create a playlist :*Access Module: play files from
the device :*\ Playlist Management: view/edit tags, transfer files
from/to device :*Other: try to manage more than one device at time (not
sure about this)*\ Windows version :*Try to port the POSIX one using
libmtp (it should work without need to change the code, maybe just some
fixes) :*\ Rewrite all using some other API (if the above doesn't work)
*Make sure everything is well integrated in the UI*\ Ipods (if there's
time and it's not too difficult)

==Timeline== {\| class="wikitable" '''Coding begins''' Examination
period, will work with no problem '''Mid-term evaluation''' On
holiday... '''"Pencil down"''' '''Final evaluation''' '''Submitting
required code samples to Google''' \|} The planning is still a little
vague, i still don't know examination dates, so it's just a guess, but i
don't think to have big problems on working during that period (probably
just a break the day of the exam or the day before...)

==Current Status==

===Git===

You can checkout to my repository by:
   $ git clone git://git.videolan.org/vlc-sephiroth87.git

Remember to switch to branch "work".

===Progress===

{\| class="wikitable" ! What !! When !! Status Study libmtp, services
discovery and playlist API, VLC internals \|\| May \|\|
style="background: #ddffdd"-\| June \|\| style="background: #ddffdd"-\|
June \|\| style="background: #ddffdd"-\| June \|\| style="background:
#ddffdd"-\| June \|\| style="background: #ddffdd"-\| June \|\|
style="background: #ddffdd"-\| June \|\| style="background: #ddffdd"-\|
June \|\| Not started MTP Service Discovery: detect device (real-time),
playlist creation (Win) \|\| July \|\| style="background: #ffffdd"-\|
July \|\| Not started MTP management: Modify services discovery API and
interface to add tracks to a device (Win) \|\| July \|\| Not started MTP
management: Delete tracks in the device (Win) \|\| July \|\| Not started
MTP management: Save tracks from the device (Win) \|\| July \|\| Not
started MTP management: Tags (?) (Win) \|\| July \|\| Not started
Multi-MTP: Detect more than one device (still not sure about this) (Win)
\|\| July \|\| Not started Be late: Finish what needs to (I know I won't
manage to stick to the schedule) \|\| August \|\| Not started Polish:
Fix bugs, do performance testing and stuff like that \|\| August \|\|
Not started Bonus: iPods... If there's time and it's not too
different... \|\| August \|\| not started }

===Right now?===

Fixing things around... Finishing something... Setting up a
cross-compiling environment...

==Sample Version==
[http://mailman.videolan.org/pipermail/vlc-devel/2008-March/041288.html]
Here's the first version of my work, the one i submitted to get started
with SoC. It's a basic support, can read one device at time, and you can
play files on it, nothing more, just a proof of concept...
