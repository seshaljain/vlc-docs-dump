{{SoCProjectstudent=[[User:VladimirBmentor=[[User:thresh|Pavlov
Konstantin]]}}

Thanks to everyone who pays attention to my project. I received several
letters concerning the idea and I see that it excites many people. I am
open to your suggestions.

== About the project == The goal is to add GUI to the Firefox plug-in
“in order to have, in the web pages embedded mode, buttons to control
VLC media player as in WMP or Youtube player”. Next step is to develop
similar plug-in for Internet Explore. Also “a replacement for all
preconfigured media players embedded in web pages” should be provided.
More detailed description (but a little bit outdated) can be found at
the application information page
http://code.google.com/soc/2008/videolan/appinfo.html?csaid=CD2BD85FF24811F4.

----Requirements: \* toolbar at the bottom of the video drawing area \*
toolbar vissible by default \* toolbar should be possible to disable by
webdesigner with JS API. \* toolbar should not be autohiding (think
users won't understand) \* toolbar should have nicely designed buttons
\* toolbar should work under Firefox windows \* toolbar should work
under Firefox linux \* toolbar should work under Mozilla windows? \*
toolbar should work under Safari MacOS X (pdherbemont) \* toolbar should
have same JS API on all browsers (IE/Firefox) The idea is that we need
to use native code to design it: <br> On linux, there is already a code
that uses libX11 to show a toolbar on top of the video. <br> On windows,
GDI is the way to go (as the demo shows it). <br> On mac, well, :D <br>
There are two things to show: a toolbar and a left-click menu. <br> Most
of the code must be cross platform, except the drawing part, which means
that controls should be common, and drawing may not be. <br> For
designers that design explicitely a page for VLC, they must be able to
deactivate menu and toolbar. The JS to control that has to be the same
on ActiveX and Netscape/Mozilla.

== Who I am == My name is Vladimir Belousov. I’m a third-year university
student of Moscow Institute of Physics and Technology
(http://phystech.edu).

== Progress == Current desight of the toolbar: [[Image:Toolbar.png]]

It has play/pause button, seek bar, volume control (it pops up a bar
like system volume control does), about button.

''I think that the toolbar should be extremely simple and have only a
few controls like other players have, because it mustn't occupy much
place on the screen and allow user to understand the functionality fast.
But if someone wants extended functionality – this is where context menu
comes to play.''

There are three operating modes: \* Always Show - the toolbar is always
shown \* Auto Hide - the toolbar gets hidden when user moves mouse
pointer out of the window \* Hidden - the toolbar is always hidden

== TODO == Here are my plans on near future: \* Port on Windows
(approximately a few days) \* Extend GUI with hints/tips and context
menu \* Fix bugs \* …

== Bugs :-( == If you noticed the bug, please, add that to this list. I
update [http://git.videolan.org/?p=vlc-vbelousov.git my git] repo from
time to time, so you can test the project state.

-  FF вызывает NPP_SetWindow не в соответствии с документацией

== Timeline (planning) == {\| class="wikitable"
[http://code.google.com/opensource/gsoc/2008/faqs.html#0.1_timeline May
26] \| '''Coding begins''' May 26 \| Test of English (state exam) May 30
\| Examination in Equations of Mathematical Physics (written form) June
2 \| ''Week 2'' June 5 \| Examination in Equations of Mathematical
Physics June 9 \| ''Week 3'' June 10 \| Examination in theoretical
physics June 14 \| Examination in general physics June 16 \| ''Week 4''
June 23 \| ''Week 5'' June 21-24 \| Sorry, unable to work (making a trip
to home town) June 30 \| ''Week 6'' July 7 \| ''Week 7''
[http://code.google.com/opensource/gsoc/2008/faqs.html#0.1_timeline July
7-14] \| '''Mid-term evaluation''' ''Week 8'' ''Week 9'' ''Week 10''
Some short trips are planned (exact dates are still unknown) ''Week 11''
''Week 12'' '''"Pencil down"''' ''Week 13'' ''Week 14'' ''Week 15''
'''Final evaluation''' '''Submitting required code samples to Google'''
\|} Please, give me three days of free time before each exam to get
prepared for it.
