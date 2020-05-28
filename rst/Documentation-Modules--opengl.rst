This module features conditional compilation:
[https://www.videolan.org/developers/vlc/doc/doxygen/html/vlc__plugin_8h.html#a789d7743e2a12bcaef2f0677a81c5c44
add_module] monitors <var>USE_OPENGL_ES2</var> to determine the
<samp>[e]xtension through which to use the Open Graphics Library
(OpenGL)</samp>.

More simply, <code>gl</code> is called for desktop computers and
<code>gles2</code> is called for embedded devices (e.g. smartphones).

Neither conditional module accepts options&mdash;<code>add_glopts
()</code> is called in {{VLCSourceFilel=vout_helper.h}} for that
purpose.

== gles2 == {{Moduletype=Video outputdescription=OpenGL for Embedded
Systems 2 video outputsc2=gles2}} {{Clear}}

== gl == {{Moduletype=Video outputdescription=OpenGL video
outputsc2=gl}} OpenGL (as a plugin) was first introduced for the
[[macOS]] port in VLC 0.7.1, made the default for macOS in VLC 0.7.2,
and later added for all platforms in VLC 0.8.0. {{Clear}}

== Source code == \* Git:
{{VLCSourceFilemodules/video_output/opengl/vout_helper.h}} (OpenGL and
OpenGL ES output common code) \* Doxygen:
[https://www.videolan.org/developers/vlc/doc/doxygen/html/vlc__opengl_8h_source.html
include/vlc_opengl.h] \* Doxygen:
[https://www.videolan.org/developers/vlc/doc/doxygen/html/opengl_8c.html
include/vlc_opengl.c] \* Doxygen:
[https://www.videolan.org/developers/vlc/doc/doxygen/html/vlc__vout__display_8h.html
include/vlc_vout_display.h]

== See also == \* {{docmodglwin32}} - module for Windows 32-bit OpenGL
\* {{docmod|glx}} - module for Linux X11 OpenGL

== External links == \* [https://opengl.org/ opengl.org] \*
[https://www.khronos.org/opengles www.khronos.org/opengles] - developer
page for OpenGL ES \* Wikibook: [[wikibooks:OpenGL ProgrammingOpenGL ES
Overview]]

{{Documentation}}
