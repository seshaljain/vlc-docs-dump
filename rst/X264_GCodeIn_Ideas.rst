.. raw:: mediawiki

   {{Lowercase}}

Google Code In
==============

This page is about gathering **ideas** for the x264 project for acceptance in the `Google Code In 2010-2011 <http://code.google.com/opensource/gci/2010-11/index.html>`__ program.

x264 has been part of Videolan's `Google Summer of Code <http://code.google.com/soc/>`__ in `2008 <SoC_2008>`__, `2009 <SoC_2009>`__ and `2010 <SoC_2010>`__.

Ideas for x264
==============

Warning
-------

This is a temporary page for listing ideas for Google Code-in tasks.

The final tasks will be moved to melange, when needed.

Tools
-----

| **Category**: Quality Assurance
| **Description**: Automated regression test tool
| **Details**: x264 has no standard regression test tool, and all the developers rely on their own scripts. An automated regression test tool should be able to:

-  Test any two revisions against each other.
-  Test a wide variety of x264 settings combinations. We can help you here by giving you some of the existing scripts.
-  Report the status of a revision: working (basic regression test passes), broken (basic regression test fails), crash, etc.
-  Report the difference between any two revisions (output differs, output is identical, which tests' output differs, etc).

| **Outcome**: A regression test script (in Bash, Perl, Python, or similar)
| **Difficulty**: medium-hard
| **Tools**: x264, JM, ffmpeg, Linux, git
| **Time**: 5 days
| **Possible Mentors**: Jason Garrett-Glaser (Dark Shikari)

CLI Development
---------------

| **Category**: Video filtering
| **Description**: Port *any* video filter to x264
| **Details**: x264 recently got a filtering system that allows users to process video before encoding -- resizing, cropping, and so forth. We'd like to add fancier filters by porting them from other projects, like mplayer's libmpcodecs. These could include denoising, sharpening, blurring, and so forth.
| You can pick *any filter you want* and port it -- just make sure to ask first to make sure that it would make sense in the context of x264.
| Do note all filters must reach the code quality standards of x264, so in some cases you may need to do more than just copy-pasting: reformatting code, etc.
| **Outcome**: A new filter in x264.
| **Difficulty**: hard
| **Tools**: x264
| **Time**: 7 days
| **Possible Mentors**: Jason Garrett-Glaser (Dark Shikari), James Darnley (J_Darnley), Steven Walters (kemuri-_9)
| **Category**: Add a --device option
| **Description**: Add a new option to x264cli so users can specify a particular device
| **Details**: Edit x264.c to change the input settings for a particular device in a similar way to --preset and --tune
| Most of the settings for specific devices (e.g iPod, Xbox, AppleTV) can be found online. x264 developers can help with more complex devices such as Blu-Ray.

| **Outcome**: Users can specify a specific device to x264.
| **Difficulty**: medium
| **Tools**: x264
| **Time**: 3-5 days
| **Possible Mentors**: Jason Garrett-Glaser (Dark Shikari), James Darnley (J_Darnley), Steven Walters (kemuri-_9), Kieran Kunhya (kierank)

libx264 Core Development
------------------------

| **Category**: Assembly Optimization
| **Description**: Write *any* assembly function: x86 (MMX/SSE), PowerPC (Altivec), or ARM (ARMv6/NEON)
| **Details**: x264 has boatloads of C functions with assembly versions that haven't been written yet. Assembly functions are really great for Google Code-In because they can be written without any knowledge of the overall program. Most functions are only a few lines long in C, making an assembly implementation relatively easy. In many cases, some (but not all) versions of a function are already written in assembly, providing good examples for future versions.
| If you pick this task, it's highly recommended that you have some experience in assembly coding already. Writing a single function is not too difficult if you already have some experience, but if you've never done it before, it will take significantly more time. Of course, if you're interested in learning, we'd be happy to teach you--Jason has taught many many students before. It usually takes a couple hours to learn the basics.
| **Outcome**: A new assembly function in x264.
| **Difficulty**: hard
| **Tools**: x264, yasm (for x86) or gas (for ARM)
| **Time**: 0.5-7 days, depends heavily on function complexity
| **Possible Mentors**: Jason Garrett-Glaser (Dark Shikari), Holger Lubitz (holger), Loren Merritt (pengvado)

Contact
-------

For ANY question, contact `User:Dark Shikari <User:Dark_Shikari>`__, preferably on IRC.

IRC channel: #x264dev on irc://irc.freenode.net

`Category:x264 <Category:x264>`__
