{{SoCProjectstudent=[[User:Leonoxmentor=[[User:Dionoea|Antoine
Cellerier]]}}

==Project Abstract== [http://freepv.sf.net FreePV] is a panoramic viewer
that was initially developed due to the lack of an implementation of
QuickTime and Shockwave for Linux and VLC is a cross platform media
player widely used, both work with QuickTime files and the problem arise
from that, since both videos and VR contents share the same Mime Type
this ends in a conflict for web explorers such as Firefox which should
decide which plug-in to load based on the Mime Type of the file. To
solve this problem the main goal of this project is to integrate the
[http://freepv.sf.net FreePV] library into VLC to enable it to play
QuickTime VR contents; the second goal would be to improve
[http://freepv.sf.net FreePV].

--[[User:Leonox|Leonox]] 02:59, 25 March 2009 (CET)

==Previous works== The problem was identified during the realization of
the [http://wiki.panotools.org/Interactive_Panoramic_Viewer Interactive
Panoramic Viewer] project proposed for SoC 2007. There was the
[[SoC_2008/PanoramaViewing|Panorama Viewing]] proposal for [[SoC_2008]]
based in the same idea. There is also a
[http://wiki.panotools.org/SoC2007_projects#Interactive_panoramic_viewer
page] about this in the Panotools' Wiki.

==Description==

Since main proble is that both videos and VR contents share the same
Mime Type this ends in a conflict for web explorers such as Firefox
which should decide which plug-in to load based on the Mime Type of the
file, thusthe first step of the project would be to distinguish between
videos and VR contents, based on this I could create a demux and a
decoder in VLC or use the existing functions inside FreePV, I would say
that we should analysis this, since there are some decoders already
implemented in VLC that would be useful. The whole file or the samples
of a track should be given to FreePV in order to build and display the
panorama, thus there will be the need to analyze how we will display the
panorama, probably we will have to modify some code on how VLC handle
the images, then the the basic interaction with panoramas should be
supported and it should be easy, since VLC already support some
interaction with the DVD menus.

The second part of the project would be the advanced interactive part by
exploring the use of Wiimote, we will need to check which library out
there will fit our needs to get advantage of the Wiimote's
accelerometer, then we will experiment with the interaction with
panoramas and finally using it to control other VLC's functionalities.

===Main goal===

-  Display Quicktime panoramas with VLC media player.

====Project goals====

-  VLC will be able to distinguish between video and vr content.
-  VLC will be able to display panoramas.
-  VLC should be able to handle the interaction required for panoramas.
-  Control VR with the Wiimote.
-  Control other media using Wiimote.
-  Keep improving FreePV.

== Schedule ==

Here is a tentative plan for the project, this schedule was the one
submitted with the original project proposal, for a more accurate
Schedule you can check this
[http://www.google.com/calendar/embed?src=seiotbl75rd4rj4sf74vslns0o%40group.calendar.google.com&ctz=America/Mexico_City
Google Calendar].

'''April 3th'''

I could start getting familiar with the VLC code, since April 3th,
because I will have more than 2 free weeks and I should have plenty of
time to do it, after April 22th I will be with exams and giving projects
away, but I will try to keep working in the project.

'''May 20th'''

I will be able to work full time in the project after this day.

'''May 23th'''

Official Start date for Google Summer of Code 2009.

'''May 25th'''

Send report to my mentors (Week 0).

Goal: Check if a file is a QTVR.

'''June 1st'''

Send report to my mentors (Week 1).

Goal: Use FreePV to demux and decode QTVR files.

'''June 8th'''

Send report to my mentors (Week 2).

Goal: Use VLC does better to decode to be able to play QTVR that use
other encoding than JPEG.

'''June 15th'''

Send report to my mentors (Week 3).

Goal: Display and add basic interaction.

'''June 22th'''

Send report to my mentors (Week 4).

Goal: Test and Debug

'''June 29th'''

Send report to my mentors (Week 5).

Goal: Work with Wiimote.

'''July 6th'''

Send report to my mentors (Week 6).

Goal: Get everything prepared for the mid-term evaluation.

'''July 13th'''

Mid-term evaluation.

'''July 20th'''

Send report to my mentors (Week 8).

Goal: Add Wiimote interaction.

'''July 27th'''

Send report to my mentors (Week 9).

Goal: Test and Debug.

'''August 3th'''

Send last report to my mentors (Week 10).

Goal: Prepare everything for the “Pencils down day”.

\*I would like to go to SIGGRAPH in New Orleans, but this is just a
crazy idea that I have.

'''August 10th'''

Pencils down day!!!.

==Project Status== Project Accepted --[[User:Leonox|Leonox]] 23:51, 20
April 2009 (CEST)

===Git===

You can checkout my repository by:

   $ git clone git://git.videolan.org/vlc-leonox.git

If you want to test QTVR...

   $ git checkout qtvr

to compile the qtvr decoder module you need to add the following
argument:

   $ --enable-qtvr

... or if you want to test the Wiimote

   $ git checkout wiimote

to compile the wiimote control module you need to add the following
argument:

   $ --enable-wiimote

===Reports===

*[http://docs.google.com/View?id=d86k47t_24g3s6n6c5 Report
0]*\ [http://docs.google.com/View?id=d86k47t_25fkc2rwhf Report 1]
*[http://docs.google.com/View?id=d86k47t_27hmfjvwgg Report
2]*\ [http://docs.google.com/View?id=d86k47t_30dxwt27hj Report 3]
\*[\ http://docs.google.com/View?id=d86k47t_31hh6kzrcq Report 4]
