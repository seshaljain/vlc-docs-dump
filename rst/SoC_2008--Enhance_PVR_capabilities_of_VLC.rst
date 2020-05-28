{{SoCProjectstudent=[[User:Dylanmentor=[[User:Pdherbemont|Pierre
d'Herbemont]]}}

==Intro== This is the page I will use to document the progress of my
Summer of Code 2008 project. Feel free to send me ideas, comments or any
inspiration.

==Project Abstract== VLC has fast become one of the most common video
players available for 'non-technical' users. The ability to watch
streams easily and efficiently is a huge advantage for VLC. The ability
to timeshift streams has been added to the latest unstable builds,
however it is vastly underfeatured and not nearly ready for release. The
features would enhance VLC to a new level which would allow a new set of
users to use it.

I propose to extend & improve the PVR capabilities of VLC. The current
version is severely lacking in functionality and performance. There is a
very basic timeshift capability already. To this I will add the ability
to randomly seek through the buffer (fast forward, rewind, etc ). The
ability to save buffers and continue recording to the new file will be
added. These recordings will be in any chosen format. These features
will help anyone who uses VLC to watch TV shows to easily turn their
client into a MythTV/Media Centre style client. I will tie the module in
with the user interface properly so that the state of the buffer and the
current position can be easily seen. I then plan to begin work on a
framework that combines all of these features into a simple interface
easily accessible with a remote control. The interface will combine VLM
and the media library into a single easily accesible place. The
interface will have the ability to 'talk' to the server sending commands
such as changing tv channel or switching input source.

With this and the completion of VLM and the playlist managing system VLC
will have the capabilities to become a fully featured PVR system with
the massive advantage of it being run off a streaming server if need be.
==Current Status== End of Week 8

[http://git.videolan.org/?p=vlc-dylanza.git&a=search&h=intmodst=author&s=Dylan
Latest patches]

===Timeshift=== \* Mostly Done - Testing Phase!

===Interface=== \* Now we have a full on menu system (see screenshots).
\* Can control most VLC things from the system. \* It could(should?)
work if you pull it off the git repository. hit F5 during movie play and
a menu should slide into view with some functionality. Command line vlc
--vout=pvrvout -I pvrgui <file> \* Now is time to make it all functional
and nice. Beginning with the text.

===Current Problems=== \* Image drawing STILL isnt working. I hate this
bug. (loading works I think). \* When the movie is paused the thread
priority drops and the animations dont work well anymore. \* Major
problem with closing GLX. Traced to an nvidia driver problem. I have
found a work around thought, so that will be an option. Hopefully they
fix the drivers one day. \* got to remove FTGL

=== Screenshots === ==== End Week 8 ====
http://git.videolan.org/?p=vlc-dylanza.git;a=blob_plain;h=1899e7ba751c70853c7bce1dfbd771a396d6c34a;f=modules/gui/pvr/pvrvout/screens/1.png
\* Base Menu
http://git.videolan.org/?p=vlc-dylanza.git;a=blob_plain;h=ac55fac905819f02f1cb44a94700cb20b7232107;f=modules/gui/pvr/pvrvout/screens/2.png
\* Playlist modifications
http://git.videolan.org/?p=vlc-dylanza.git;a=blob_plain;h=e767ff186de5b2a48bbb7cdfb077420bfc982a05;f=modules/gui/pvr/pvrvout/screens/3.png
\* Modifying an number variable

==Details== The plan is to work on two parts. ===Timeshift Module===
Initially the timeshift access module will be improved considerably.
Bugs ironed out and additional functionality added. This is beign done a
bit at a time throughout. ===PVR Interface=== Then a new interface will
be added. My current idea (still to be discussed with more knowledgable
developers) is to build onto the QT interface. Firstly a good fullscreen
interface (potentially to be worked on with the summer of code project
focusing on that) that clearly displays the current buffer state. ie.
where we are in the current buffer, buffer size, recording information
etc... In addition a new widget will be created that contains the
PVR-style menus. These will be nice and big for use on a tv. There will
be screens to access music & videos (from the library still to be
finished), streams, options, pictures & VLM. There will potentially also
be a new sort of hotkeys interface specifically for the PVR, so that you
can have specific hotkeys linked to a remote control when watching
fullscreen.

==Project Timeline== ===Time Planning=== Basically

'''Pre-May 26''' Because of my excellent southern-hemisphere timetable
have started working on code a bit. see status for progress.

'''May 26:''' Program Start. Also the start of my exams. Will not be
working this week.

'''June 1 -> 13:''' Still have exams, but only 2 in this long period and
its not very busy with them. Will start working properly on the project.

'''June 14 - July 7:''' Work Work

''' July 7:''' Mid term evaluations

''' July 8 -> Beginning of August:''' Work nice and hard.

'''Beginning of August -> August 11:''' Finish off. could have tests
here as well depending on university. 11 August is googles suggested
pencils down date.

'''August 11 -> August 18:''' Make code excellent.

'''August 19:''' no more coding

===Timeline=== This will be expanded upon, specifically the PVR
Interface section will be much more detailed closer to the time, when a
specific plan is developed. {\| class="wikitable" ! Task Description !!
Date Finished (or planned Finish)!! Status Planning \|\| 26 May \|\|
style="background: #00ff00"-\| style="background: #ffffdd"-\| Not
Started PVR Interface \|\| 11 August \|\| Not Started }
