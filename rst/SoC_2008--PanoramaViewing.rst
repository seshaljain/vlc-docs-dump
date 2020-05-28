{{SoCProjectstudent=[[User:Ploujmentor=[[User:Dionoea|Antoine
Cellerier]]}}

= Google Summer of Code 2008 = == Panorama Viewing == === Abstract ===
The goal of this project is to make VLC a one-stop solution for viewing
panoramas of various formats. Currently, FreePV is the best/only
cross-platform, non-proprietary solution for viewing QuickTimeVR and
plain image panoramas. However it suffers from a few drawbacks, which
include difficult installation, browser plug-in conflicts and low
popularity. The intent is to integrate the FreePV rendering code with
VLC. This should not only automatically alleviate installation
difficulty and plug-in conflicts, but also bring panorama viewing to a
much larger audience. This project will initially focus on basic support
for QTVR files and equirectangular images.

=== Detailed Description === The way I see it, based on rudimentary
knowledge of the VLC internals, is that technically this project is
about writing a codec to handle QTVR and an output module for viewing
frames projected onto the inside of a rotatable OpenGL sphere.

==== My Commitment ==== I'm committed to work at least 40 hours per week
for the duration of the GSoC on this project except for one week (to be
determined) when I will be gone on vacation.

==== Collaboration with the FreePV dev team ==== Since this project was
born out of an explicit
idea[http://thread.gmane.org/gmane.comp.video.videolan.vlc.devel/35336]
from the FreePV developers and because they promised it in a private
e-mail I am certain that they are willing to help me in this project as
best they can.

==== Plan ==== This plan is based on the dates in the
[http://code.google.com/opensource/gsoc/2008/faqs.html#0.1_timeline GSoC
2008 timeline] \* '''March 31''' - week 1 \* write e-mails to the hugin
and vlc-devel mailing lists asking for suggestions/ideas \* '''April
7''' - week 2 \* study for exams and finish school assignments \* write
a patch for VLC \* '''April 14''' - week 3 \* '''April 21''' - week 4 \*
figure out the interaction requirements for panorama viewing and how
this will affect VLC as a whole \* decide (along with other developers)
how FreePV can be turned into a stand-alone, (separately developed or as
part of the VLC projects) library that can be used by VLC to display
panoramas \* think about how panorama viewing fits in with VLC. Maybe it
should act as a codec for QTVR files, but it should also be able to use
any 2d images/frames for panoramas (act as an output module?). \* make a
list of QTVR functionality present in FreePV - aim to replicate this
list in VLC \* identify which parts of FreePV can be used as a VLC
module \* '''April 28''' - week 5 \* learn to write a codec/demuxer
module \* write a plant of what will need to be changed/added in/to VLC
\* by now I should have a good idea of how things fit together \* '''May
5''' - week 6 \* get an understanding of the QTVR format (possible
start:
http://developer.apple.com/documentation/QuickTime/InsideQT_QTVR/6Chap/chapter_6_section_1.html
and the [http://freepv.sourceforge.net/ FreePV] code) \* '''May 12''' -
week 7 \* '''May 19''' - week 8 \* '''May 26''' - week 9 - Students
begin coding for their GSoC projects; \* '''June 2''' - week 10 \*
'''June 9''' - week 11 \* '''June 16''' - week 12 \* '''June 23''' -
week 13 \* libfreepv should exist and be usable in VLC \* '''June 30'''
- week 14 \* simple QTVRs should be viewable by now \* '''July 7''' -
week 15 \* '''July 14''' - week 16 - Mid-term evaluations deadline; \*
'''July 21''' - week 17 \* should be able to view image (.PNG, .JPG,...)
panoramas \* '''July 28''' - week 18 \* should support a number of
different projections and do everything that FreePV can with QTVR \*
'''August 4''' - week 19 \* '''August 11''' - week 20 \* '''August 18'''

==== Module Options ==== \* type of panorama:
equirectangular,cylindrical,littleplanet,cubic... \* default FOV aka
zoom
