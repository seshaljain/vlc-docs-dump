Intro
-----

We need a better test suite

What exists
-----------

autotools test suite
~~~~~~~~~~~~~~~~~~~~

Currently you can run the following command to run the vlc tests

``$ make check``

/tests
~~~~~~

To run these tests just use the driver shell script in that directory:

``$ ./test.sh``

There are more tests in /modules/misc/tests. -- *How to run them?* `Pdherbemont <User:Pdherbemont>`__ 10:37, 27 February 2008 (CET)

Goals
-----

-  Core tests: Make sure the regular operation from VLC's core don't crash.
-  API tests: Make sure the regular operation from VLC's core don't crash.
-  General stability tests: Run some every day operation and see if it crashes.
-  Codec/muxer/modules test: Perform tests on modules to see if they actually works, that means see if their output is what there are ought to be
-  Interface tests: Run some every day gui operation and see if it crashes.

`Category:Dev Discussions <Category:Dev_Discussions>`__
