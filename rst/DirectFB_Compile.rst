This HOWTO explains howto build and install DirectFB for use with the
VLC {{docmod|directfb}} plugin.

For more details on DirectFB and its requirements you need to check the
Internet site of [http://www.directfb.org/ DirectFB].

== Building DirectFB on Linux ==

=== Download === Download the following DirectFB tarballs:

\* Mandatory tarballs: \*\* DirectFB-0.9.24.tar.gz \*\*
linux-fusion-1.1.tar.gz

\* Optional tarballs: \*\* DirectFBGL-0.9.23.tar.gz \*\*
FusionSound-0.9.23.tar.gz

Read the DirectFB documentation carefully. You will need it to properly
configure your system for use with DirectFB.

Unpack DirectFB-0.9.24.tar.gz:
   $> tar -xzvf DirectFB-0.9.24.tar.gz -C directory_where_to_unpack

=== Build Driver === Build Fusion DirectFB driver

To build the fusion device driver the source for the Linux kernel your
system is running must be installed. If this is the case then continue
with the following sequence of actions. If not then skip this chapter
and continue with building DirectFB itself.

Unpack Linux Fusion driver (linux-fusion-1.1.tar.gz):
   $> tar -xzvf linux-fusion-1.1.tar.gz -C directory_where_to_unpack

Build the DirectFB's fusion driver:
   $> cd /linux-fusion-1.1/ $> make

And as root (hint: su - root):
   $> make install

Copy fusion.h into /usr/include/linux directory:
   $> cp linux/include/linux/fusion.h /usr/include/linux

=== Build DirectFB ===

Unpack DirectFB-0.9.24.tar.gz:
   $> tar -xzvf DirectFB-0.9.24.tar.gz -C directory_where_to_unpack

Configure DirectFB:
   $> cd /DirectFB-0.9.24/

If the Fusion DirectFB driver has been compiled and installed against your running version of the Linux kernel, then the DirectFB configure-line looks like this: (If not the --enable-multi can be omitted.)
   $> ./configure --enable-multi $> make

== Compiling VideoLAN VLC ==

Checkout the [[Git]] version from the trunk directory or download one of the nightly snapshots. Then configure VLC using the following commandline:
   $> ./bootstrap $> ./configure --prefix=/usr --enable-directfb
   --with-directfb=directory_where_to_unpack/DirectFB-0.9.24 $> make

== History == This HOWTO has been written by
[`mailto:jpsaman_at_videolan_dot_org <mailto:jpsaman_at_videolan_dot_org>`__
Jean-Paul Saman]. It has been adapted to this wiki by [[User:J-b\|
Jean-Baptiste Kempf]].

[[Category:Building]] [[Category:Coding]]
