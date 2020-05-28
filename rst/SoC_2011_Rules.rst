Those rules are mostly for x264 and VLC.

Those rules are flexible depending on the situation.

Rules
=====

*We don't like rules.*

*We like freedom and having fun with software programming.*

However, we have no choice, seeing past experiences and issues. :'(

Summer Generalities
-------------------

If you are a student, we expect that:

-  You don't have a full-time job during your summer if you are doing SoC at the same time,
-  You are of good will to work within VideoLAN team.

If you are a mentor, we expect that:

-  You are willing to work with one student and answers his questions.

Selection
---------

To be selected, students should:

-  Select an idea,
-  Post a proposal on Google website,
-  Show on IRC,
-  Join the mailing lists (x264-devel or vlc-devel, according to your project),
-  Say hello to the potential mentor and admin.

-  Learn about the code you should modify (where in the source, what is the idea...),
-  Be able to compile a VLC or x264 for your platform and learn how to use `Git <Git>`__.
-  Show the team that you compiled VLC and x264, by probably provide a small patch and a build. You can send the patch to an admin or to vlc-devel@ or x264-devel@

-  Do one of the slection task (can be done after proposing the proposal)
-  Complete the Google admission and give a planning idea.

VLC selection tasks
~~~~~~~~~~~~~~~~~~~

-  Examples of small patches:

   -  ASX playlists improvements, notably port to VLC-XML (see `ticket 20 <http://trac.videolan.org/vlc/ticket/20>`__ and the code there) (easy)
   -  Close a VLC bug on trac, `1.1 issues <http://trac.videolan.org/vlc/query?status=assigned&status=new&status=reopened&group=status&milestone=1.1+bugs>`__ or `general issues <http://trac.videolan.org/vlc/query?status=assigned&status=new&status=reopened&group=status&milestone=Bugs+paradize>`__
   -  Add RMI (RIFF MIDI) support to the SMF demux,
   -  Add KAR support to the SMF demux,
   -  libsox based module,
   -  libmpg123 mp3 decoding module,
   -  port the karaoke filter from MPlayer
   -  port a demuxer from MPlayer or ffmpeg,
   -  Extend the DBus control to activate a video filter on the fly on an already playing video,
   -  Add new audio effects like chorus, reverb or phasing,
   -  Add new video filters,
   -  Fix warnings,
   -  Fix .ra decoding,
   -  Add some simple feature that sounds nice to you.

During the summer
-----------------

Student expectations
~~~~~~~~~~~~~~~~~~~~

-  Student should explain his planning to his mentor and to an admin (not everyone has the same vacations)
-  Student should report with a small mail once a week to both mentor and admin during the time agreed (failure to do that will fail the application)
-  Student should commit on his personal *git branch* once a week, except the first week of your schedule (or more if your project is complex).

**Explaining why you can't work one week is fine. Disappearing without notice is not.**

-  Update wiki status page.

Student rights
~~~~~~~~~~~~~~

-  Ask questions and stupid questions to anyone
-  Bother the mentor with questions
-  Ask the admin for another mentor if the mentor doesn't answer or doesn't fit.

Students will be considered as **full-right** developers.

Mentor expectations
~~~~~~~~~~~~~~~~~~~

-  Mentor should report to admins any problems as soon as noticed,
-  Mentor should tell admins if they can't make it in order to have another mentor for the student.

Mentor rights
~~~~~~~~~~~~~

-  Fail a student :D

Advice
======

To get selected
---------------

-  Be nice.
-  Show us basic skills with checking out and compiling the VLC code base.
-  Show us that you understand the VLC architecture. Code samples are good.
-  Come on IRC. Hang out, talk to us.

During the SoC
--------------

**COMMIT EARLY, COMMIT OFTEN**

-  Please do check that your commits compile. This makes it much easier to find problems later on, as searching for one problem doesn't stumble into broken commits that relate to something else entirely.
-  Ask questions. Don't sit on problems until the GSoC is over.
-  Don't be afraid to start researching your question yourself then check whether you are on the right track with your mentor. He (or others on the mailinglist or in the irc channel) will be happier to answer you if you can show you have done the groundwork. It tends to make explanations shorter and more meaningful, too.
-  Finishing the GSoC project in time is pretty cool too. It's your show! Make it something nice.

.. raw:: mediawiki

   {{GSoC}}

`\* <Category:SoC_2011_Project>`__
