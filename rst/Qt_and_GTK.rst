[[What is cool in 0.9|VLC media player 0.9]] introduces a new interface
based on the Qt toolkit.

Some of you, using GNOME or Xfce, seem reticent to that change, but let
us explain a few things:

== VLC media player interface is a PLUGIN == \* You can use VLC in
command line, with the http interface, or even the old wx interface,
that you can compile.

== VLC media player '''DOES NOT DEPEND''' on kdelibs ==

VLC media player Qt module needs: \* libQtCore, \* libQtGui, \* libvlc

That's it.

== How to have a Native look of VLC using Qt inside GTK environnement ==

You can use trolltech's QGtkStyle project to get a native GTK look. See
http://labs.trolltech.com/page/Projects/Styles/GtkStyle for more
information.

[[Category:Changelog]] [[Category:Qt]]
