{{Historical}} WxWidgets was the default, plain, graphical,
[[interface]] to VLC, made using the [http://www.wxwidgets.org
WxWidgets] library (Linux users may need to have this installed). It was
used as the default interface on the [[Windows]] and [[Linux]] versions
of VLC and have been replaced by the [[Qt Interface]] since 0.9.0.

It is known as the "wx" interface, so you can (or was able to) force this by running
   vlc '''-I wx'''

If WxWidgets is not available, it will probably revert to using the
[[Console|rc]] (console) interface, even if you force it. The most
likely reason for this is if WxWidgets hasn't been installed, or if it
wasn't linked in (using the ./configure). See [[compiling VLC]]
[http://developers.videolan.org/vlc/] for information on compiling.

[[Category:Interfaces]]
