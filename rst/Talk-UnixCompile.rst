Could anyone clarify this scentence in the current version a little:
   '''Be careful!''' Some of the libraries are better not to be
   installed (at all, beware of old installations) and should be linked
   to directly. These are mostly ffmpeg and liveMedia.

What does that mean? You shall fetch the source code and compile it
(make) but not install (make install) it, but leave it in the source
tree? --[[User:Rabenschwinge|Rabenschwinge]] 12:28, 31 August 2007
(CEST) ----

Exactly. Don't make install on them. [[User:J-b|jb]] 19:41, 31 August
2007 (CEST)

== About compilation in Fedora ==

In the wiki, it's said about preparating compilation to install
libraries

   "sudo yum install git libtool pkg-config"

There is no problem with git and libtool but pkg-config does'nt seem to
exist, is it necessary to use so special repo for it ?
