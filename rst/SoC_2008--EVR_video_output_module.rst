.. raw:: mediawiki

   {{SoCProject|year=2008|student=[[User:VLC_help|Kaarlo Räihä]]|mentor=[[User:atmo|Andre Weber]]}}

SoC 2008/EVR video output module
--------------------------------

As part of `SoC_2008 <SoC_2008>`__ I (Kaarlo Räihä aka VLC_help) will try to implement EVR (Enhanced Video Renderer) video output module for . EVR will hopefully be default video output module for Windows Vista but it might also work with Windows XP if the .NET Framework 3.0 is installed (it seems that no XP support is coming). EVR should guarantee tearing free output that also works with Aero.

If I have some extra time, I will try to add some features to Direct3D and OpenGL output module (shaders, rotating video etc.) and possible fix other Windows (Vista) related issues/bugs. I will continue on shader support after SoC.

Current status of project
~~~~~~~~~~~~~~~~~~~~~~~~~

Stage 3 under work.

Git
^^^

http://git.videolan.org/?p=vlc-vlchelp.git;a=summary Doesn't compile or work, so the only useful stuff is in contribs folder.

Statistics
^^^^^^^^^^

-  Code: 0.379 kloc (for the output module only, doesn't include random patches, contribs or proto code)
-  Comments: 0.179 kloc
-  Total: 0.677 kloc

Planned absence / Vacations / Holidays
--------------------------------------

Midsummer days (19.6.2008 - 22.6.2008)

Timetable
---------

Planned
~~~~~~~

Coding will start on 26th of May. There should be working module hopefully on first week of July (1st July - 6th July). Coding ends on 1st of September. Documentation and some support will continue after GSoC.

Stage 1: Use Visual Studio to create EVR sample code (one image, nothing fancy).

Stage 2: Get that same code compile under Cygwin environment (and make sure someone else can also compile it).

Stage 3a: Implement EVR module to VLC. Stage 3b: Test EVR implementation (include various stress tests)

Week 21 (19.5.2008 - 25.5.2008)

-  Soft start (GIT stuff, serious IRC chatting, random patches, recruit beta testers)

Week 22 (26.5.2008 - 1.6.2008)

-  Start planning
-  make/build changes
-  Write some proto code for EVR test
-  test some EVR samples found around internet (mostly MSDN)

Week 23 (2.6.2008 - 8.6.2008)

-  Get stage 1 done
-  Finish Win32 http proxy patch
-  Write better proto code
-  Get my git branch basecode updated

Week 24 (9.6.2008 - 15.6.2008)

-  Complete stage 1
-  Start stage 2
-  test more EVR samples found around internet and Windows SDK

Week 25 (16.6.2008 - 22.6.2008)

-  Complete stage 2
-  Start stage 3a

Week 26 (23.6.2008 - 29.6.2008)

-  Complete stage 2
-  Start stage 3a

Week 27 (30.6.2008 - 6.7.2008)

-  Complete stage 2
-  Start stage 3a

Week 28 (7.7.2008 - 13.7.2008)

-  Complete stage 2
-  Start stage 3a

Week 29 (14.7.2008 - 20.7.2008)

-  Start stage 3a

Week 30 (21.7.2008 - 27.7.2008)

-  Continue stage 3a

Week 31 (28.7.2008 - 3.8.2008)

-  Continue stage 3a

Week 32 (4.8.2008 - 10.8.2008)

-  Continue stage 3a

Week 33 (11.8.2008 - 17.8.2008)

-  Continue stage 3a

Week 34 (18.8.2008 - 24.8.2008)

-  Continue stage 3a

Reality (aka what did I do)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Coding started on 26th of May. Currently working on stage 3 (about 20% done).

Week 21 (19.5.2008 - 25.5.2008)

-  GIT repo obtained
-  IRC chatting with devs
-  Two random patches sent to mailing list (sorry about the mess I caused)
-  One beta tester recruited
-  Issues related to build environment found which I have to fix

Week 22 (26.5.2008 - 1.6.2008)

-  Wiki updated
-  Stage 1 started
-  Simple proto test (failed)
-  First git push

Week 23 (2.6.2008 - 8.6.2008)

-  Wiki updated
-  Finished Win32 IE http proxy patch
-  Updated Windows SDK and Visual studio to get more EVR sample code (no simple code available)
-  Second git push

Week 24 (9.6.2008 - 15.6.2008)

-  Completed stage 1
-  Started stage 2

Week 25 (16.6.2008 - 22.6.2008)

-  Wiki updates
-  Stage 2 compile marathon

Week 26 (23.6.2008 - 29.6.2008)

-  Wiki updates
-  Stage 2 compile marathon part II (no linking yet)

Week 27 (30.6.2008 - 6.7.2008)

-  Wiki updates
-  Stage 2 linking marathon

Week 28 (7.7.2008 - 13.7.2008)

-  Wiki updates
-  Stage 2 linking marathon partII (works!)

Week 29 (14.7.2008 - 20.7.2008)

-  Wiki updates
-  Stage 3 started

Week 30 (21.7.2008 - 27.7.2008)

-  Wiki updates
-  Stage 3 continues

Week 31 (28.7.2008 - 3.8.2008)

-  Wiki updates
-  Stage 3 continues

Week 32 (4.8.2008 - 10.8.2008)

-  Stage 3 continues

Week 33 (11.8.2008 - 17.8.2008)

-  Stage 3 continues

Week 34 (18.8.2008 - 24.8.2008)

-  Stage 3 continues
