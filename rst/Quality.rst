**Quality Assurance**

This section of the wiki is about helping to increase the quality of different versions of VideoLAN's products, mainly `VLC media player <VLC_media_player>`__.

Why this page ?
---------------

Main idea
~~~~~~~~~

There is not much on this page yet, but the idea is to develop *test protocols*, regroup *test files*, and at the end improve the whole quality of VLC, to avoid *regressions* and check *roadmaps.*

Who is concerned
~~~~~~~~~~~~~~~~

The community of VideoLAN's numerous users and developers can enforce the project by doing systematic tests and reporting bugs and regressions. Some projects rely on a lot of external code that evolves a lot. Being **numerous** can help to make it better.

Bugs
~~~~

The **bugs** should be tracked down and killed using `trac <http://trac.videolan.org>`__.

Why should you get involved ?
-----------------------------

The **more** we are, the more bugs are spotted, the better VLC is ! Easy, ain't it ?

So if **you** help, everyone will be a winner.

How can you get involved ?
--------------------------

Use this talk page or contact; for a start `User_talk:J-b <User_talk:J-b>`__ (this will change). Then, just run the tests and modify this wiki's pages.

Bug reporting
~~~~~~~~~~~~~

   *Main article:*\ `Report bugs <Report_bugs>`__

Use trac to do these. If you compile yourself, please enable `debug <debug>`__ to get readable bactraces if any.

Urgent
------

-  Gather original and references video and audio files

VLC
===

Motto: *Let's improve VLC !!!*

Tests to run
------------

You want to help by testing VLC ? There are a few tests that you can handle:

-  VLC playback tests (codecs and files related) Win32 and MacOS focused.
-  VLC functionality tests
-  VLC transcode and streaming tests
-  VLC fundamental tests in src/test (run *make check*)

There is a small test suite for the `Android <Android>`__ port located at `Android test suite <Android_test_suite>`__.

Files
-----

Official files
~~~~~~~~~~~~~~

All those files should be tested inside the reference FTP.

ftp://streams.videolan.org/streams/

Use that structure to create the reports.

More files
~~~~~~~~~~

Where to search for more files:

-  MPlayer's `MPlayer's FTP <http://samples.mplayerhq.hu/>`__
-  References codecs pages usually, linking to those should be enough...

Nightly builds
--------------

In general, use the latest nightly build when you run your tests and report, available at http://nightlies.videolan.org/.

`Category:Coding <Category:Coding>`__
