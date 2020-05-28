This page still needs some fixing and updating. `Dionoea <User:Dionoea>`__ 00:12, 7 November 2006 (CET)

Advanced Installation: Portable / Networked / Sandboxed / etc (Debian)
----------------------------------------------------------------------

The syntax here is for Debian (and thus Ubuntu etc too: this was tested on Ubuntu 10.04), but it should be trivial to translate it to any other modern distro.

There are times a normal install just isn't desirable or even possible, and you need something a little bit more funky. (Maybe you could be working on any of a number of virtualised machines and any point, and putting VLC in the base image isn't an option; or you want to use an app server, etc).

If you start with a "genuinely clean" machine and look at what will be sucked in for a VLC install, it can be quite shocking: \*72\* base packages, plus another 14 recommends/suggests, and ~100MB. That's more than a 12% increase to the total size of the VM base image. More importantly, it's 69 libraries that I have absolulely no use for outside of VLC, and in fact explicitly **don't** want on the system where things like nautilus will try to suck them in and use them (and they represent 69 new attack vectors).

Don't misunderstand: this is the 'right' way to write software. But it's not what I actually want in this case. What I want is a walled garden for VLC, with only VLC allowed to use this (massive collection of) libs.

So, how do we manage that? Turns out it's actually really easy...

First we need to get the files 'somewhere': we just don't want them in the "normal" package list.

::

   ~/$ mkdir vlc && cd vlc && mkdir -p archives/partial
   ~/vlc$ sudo apt-get -d -o Dir::Cache=. install vlc

That will grab the packages from the repo, complete with all the dependencies (if you have apt set to default to --no-recommends, you'll need to add "vlc-plugin-pulse" or anything else you want as well) and put them in our working directory.

Take a look at what's actually in a package, if you're curious:

::

   ~/vlc$ dpkg -c archives/libxcb-randr0_1.5-2_i386.deb

   -rw-r--r-- root/root   34124 2010-01-20 03:11 ./usr/lib/libxcb-randr.so.0.1.0
   lrwxrwxrwx root/root       0 2010-01-20 03:10 ./usr/lib/libxcb-randr.so.0 -> libxcb-randr.so.0.1.0

There's a bunch of noise like manpages etc too, but these are the only pieces that are actually important. There's the lib itself, a symlink for versioning, and that's it. But here's what's brilliant: the files are 'relative' paths, and that's what makes this so trivial...

::

   ~/vlc$ find archives/*.deb -print |xargs -t -I {} dpkg -x {} .

That pulls all the libs out and drops them in our sandbox, and then running vlc is as simple as:

::

   ~/vlc$ export LD_LIBRARY_PATH=usr/lib/
   ~/vlc$ usr/bin/vlc

and that's all there is to it. :D

You can use this to install vlc on an app share, without "polluting" any of the clients and still allowing them to each keep their own configuration in ~/.config/vlc/ 'Very' handy if e.g. you work on a virtual machine where the base image is immutable and your home dir is the only thing that persists between sessions; or a real machine that's maintained by an IT dept.

A trivial variation on it will also let you create a "portable" version of VLC that you can stick on a USB drive along with some music / videos / whatever and use on any machine.
