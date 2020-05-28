.. raw:: mediawiki

   {{Lowercase}}

**x264** is a free software library for encoding `H.264/MPEG-4 AVC <H.264/MPEG-4_AVC>`__ video streams.

The code is written by Loren Merritt, Laurent Aimar, Eric Petit, Min Chen, Justin Clay, Måns Rullgård, Radek Czyz, Alex Izvorski, Alex Wright, Jason and Christian Heine from scratch.

**x264** is one of the most popular video compression libraries in the world, used worldwide for applications such as web video, television broadcast, and Blu-ray authoring. It outclasses practically all commercial implementations both speed and compression-wise. While not actually part of or `FFmpeg <FFmpeg>`__, it is a major library used by both, licensed under the GPL. Due to its popularity in the commercial world (for example, Youtube and Facebook rely on it), many companies have offered bounties in the past for features and improvements that they found useful.

**x264** has a strong user community based at `Doom9 <http://www.Doom9.org>`__ where discussions for improved development take place.

Developers
----------

-  `x264 home page <https://www.videolan.org/developers/x264.html>`__
-  `x264 Development Newsletters <x264_Development_Newsletters>`__
-  `x264 Development Notes <x264_Development_Notes>`__
-  `x264 TODO <x264_TODO>`__
-  `x264 asm intro <x264_asm_intro>`__

An overview of x264's structure and algorithms can be found `here <http://akuvian.org/src/x264/overview_x264_v8_5.pdf>`__. It is somewhat outdated, but still mostly accurate. Do note that understanding this is not necessary for developing on x264.

On a lighter note, feel free to check out the `x264 developer quotes page <http://www.x264.nl/developers/Dark_Shikari/loren.html>`__.

Start developping on x264
-------------------------

Guide to getting involved
~~~~~~~~~~~~~~~~~~~~~~~~~

-  Hop on IRC--whenever! We have a friendly community that's happy to help and to talk about pretty much whatever. #x264 is the general discussion/user help channel and #x264dev is the development-only channel (Freenode server). If you've never used IRC, grab Chatzilla. There is no such thing as a stupid question--only stupid people--so don't worry about sounding dumb. Just get involved!
-  Ask questions--I cannot stress this enough. We've had students who couldn't get anywhere because they were stuck--but didn't ask questions! There's no shame in asking questions; that's how everyone here got involved.
-  **Stay on IRC**. Even if you have nothing to say, being around lets you get to know the community, get a feel for what's going on, and even sometimes help out by pointing the semicolon I left at the end of my if statement. This applies during the project period too: we expect all students to **always be on IRC**. This doesn't mean you have to be actually active all the time, but whenever you're free, you should be at least pingable on IRC, and whenever you're working on Summer of Code, you should be active on IRC.

   -  The best option for staying online is to get a remote shell account of some sort and leave an IRSSI client on 24/7 in a screen. This lets you easily come back in the morning and see if you missed anything important. checkers can provide you with a shell if you end up being accepted as a student.

-  Even if you don't get a slot as a student, or you don't qualify for Summer of Code, we will happily provide you with the exact same support that we would give a student: it is quite reasonable and not at all uncommon for us to have projects of similar scale to Summer of Code be done by students who are not part of the Summer of Code program.

Skills needed
~~~~~~~~~~~~~

These are required for all listed projects and probably anything not listed, too.

-  Basic C programming.
-  Basic understanding of video encoding, or at least willingness to do the appropriate reading up on the topic before the summer begins. Most people who get involved don't know much to start with; we don't expect you to!
-  To work on anything related directly to the encoder core (not all projects), you'll need to do some significant background reading on relevant topics.

Demos
-----

`flyingskunk.mkv <http://lives.rm.org/demos/flyingskunk.mkv>`__ demo encoded with x264/vorbis/matroska - (96 MB, 640x480, 25 fps, 6 minutes), created using `LiVES <http://lives.sourceforge.net>`__

`Category:VideoLAN projects <Category:VideoLAN_projects>`__
