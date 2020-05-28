{{SoCProjectstudent=[[User:MessiahAndrwmentor=[[User:j-b|Jean-Baptiste
Kempf]]}}

Stereoscopic, or 3D, video support was implemented into the VLC Media
Player as part of my Google Summer of Code project. It is currently
experimental with a couple of bugs and I'm still actively working on it.
At present you must build it from source, and I'm looking to soon merge
it into the main tree.

I'm in need of hardware, if you would like to help out see
[[#Donations|here]].

== Building from Source ==

At the present state you must acquire the source code of the
stereoscopic 3D branch and build it yourself.
https://github.com/MessiahAndrw/Stereoscopic-VLC

A build (that my be out of date by the time you read this) is available
here:
http://streams.videolan.org/misc/stereo/vlc-1.2.0-git-stereoscopy.zip\ �

There are build instructions in a file named 'STEREOSCOPY README' but
I'll also repeat the instructions here.

=== Build Environment ===

I use 32-bit MSYS/x86 Windows 7. To set up your build environment first
follow through the instructions on [Win32CompileMSYSNew] to make sure
you're able to build VLC successfully on your system.

The following build instructions should work on any Windows system.

=== Building ===

Create a new empty directory somewhere, and at the MSYS terminal type:

   git pull git://github.com/MessiahAndrw/Stereoscopic-VLC.git

To bootstrap the build I use the following:

   cd vlc cp -v /usr/win32/share/aclocal/\* m4/ cp -v
   /usr/share/aclocal/\* m4/ PATH=/usr/win32/bin:$PATH ./bootstrap

Then to configure:

   sh extras/package/win32/configure-msys.sh

Finally to build:

   PATH=/usr/win32/bin:$PATH make package-win32 -j6

(The -j6 switch is optional and tells makefile to use 6 threads, it
speeds up the build time on my 6-core machine.)

'make package-win32' will exit with the following error but that's
normal and VLC has still been built:

   cp: cannot stat \`./npapi-vlc/installed/lib/npvlc.dll': No such file
   or directory

If everything else was successful you will now have built VLC with
stereoscopic support! You will find this build in the directory
'vlc-1.2.0-git'.

=== Note on 3D Vision support ===

nVidia 3D Vision only activates for windowed-mode programs which are
supported by the nVidia driver. At the present state VLC is not
supported by the nVidia driver. However, the driver only performs a
simple file-name check of the application, so as a workaround you can
rename vlc.exe to the same file-name as a supported application. This
can be done simply by:

   cd vlc-1.2.0-git mv vlc.exe wow.exe

== Splitting ==

To play a stereoscopic 3D video you must tell the stereoscopy module how
to get the image for each eye. The stereoscopic module is takes a 2D
input picture, and produces 2 output pictures (one for the left eye, and
one for the right eye).

=== Command line ===

To enable the stereoscopic module you should add the following command
line parameters when you start vlc:

   --video-filter="stereoscopy" --stereoscopy-left="&lt;left&gt;"
   --stereoscopy-right="&lt;right&gt;"

Where &lt;left&gt; and &lt;right&gt; are valid input formats (see the
table below).

=== QT4 ===

You can configure the stereoscopy module through the QT4 interface. To
do this, open the 'Tools' menu and click on 'Effects and Filters'. In
the 'Adjustments and Effects' dialog that opens navigate to the 'Video
Effects' tab. Then find the sub-tab titled 'Stereoscopy'. Check 'Split'
to enable the stereoscopy module to split the image into separate left
and right frames. Select your video's input formats for the 'Left Eye
and the 'Right Eye'.

[[File:StereoscopyoptionsQt4.png]]

<br>

=== Input formats ===

{\| border="1" Source \| Extracted Image \| Format name \| Description
[[File:StereoRb.jpg]] \| [[File:StereoRightb.jpg]] \| blue \| The eye is
encoded into the blue channel of the image and returned as a blue image.
[[File:StereoRc.jpg]] \| [[File:StereoRightc.jpg]] \| cyan \| The eye is
encoded into the blue and green channels of the image returned as a cyan
image. [[File:StereoRg.jpg]] \| [[File:StereoRightg.jpg]] \| green \|
The eye is encoded into the green channel of the image and returned as a
green image. [[File:StereoGm.jpg]] \| [[File:StereoRightm.jpg]] \|
magenta \| The eye is encoded into the red and blue channels of the
image returned as a magenta image. [[File:StereoRc.jpg]] \|
[[File:StereoLeftr.jpg]] \| red \| The eye is encoded into the red
channel of the image and returned as a red image. [[File:StereoBy.jpg]]
\| [[File:StereoRighty.jpg]] \| yellow \| The eye is encoded into the
red and green channels of the image returned as a yellow image.
[[File:StereoRb.jpg]] \| [[File:StereoRightbg.jpg]] \| blue-gray \| The
eye is encoded into the blue channel and returned as a grayscale image.
[[File:StereoRc.jpg]] \| [[File:StereoRightcg.jpg]] \| cyan-gray \| The
eye is encoded into the blue and green channels of the image and
returned as a grayscale image. [[File:StereoRg.jpg]] \|
[[File:StereoRightgg.jpg]] \| green-gray \| The eye is encoded into the
green channel of the image and returned as a grayscale image.
[[File:StereoGm.jpg]] \| [[File:StereoRightmg.jpg]] \| magenta-gray \|
The eye is encoded into the red and blue channels of the image and
returned as a grayscale image. [[File:StereoRc.jpg]] \|
[[File:StereoLeftrg.jpg]] \| red-gray \| The eye is encoded into the red
channel of the image and returned a grayscale image.
[[File:StereoBy.jpg]] \| [[File:StereoRightyg.jpg]] \| yellow-gray \|
The eye is encoded into the red and green channels of the image and
returned as a grayscale image. [[File:StereoRc.jpg]] \|
[[File:StereoRightcf.jpg]] \| cyan-fill \| The eye is encoded into the
blue and green channels of the image and returned as a full colour
image. The missing red channel is filled in with the average of the blue
and green channels. [[File:StereoGm.jpg]] \| [[File:StereoRightmf.jpg]]
\| magenta-fill \| The eye is encoded into the red and blue channels of
the image and returned as a full colour image. The missing green channel
is filled in with the average of the red and blue channels.
[[File:StereoBy.jpg]] \| [[File:StereoRightyf.jpg]] \| yellow-fill \|
The eye is encoded into the red and green channels of the image and
returned as a full colour image. The missing blue channel is filled in
with the average of the red and green channels. [[File:StereoLr.jpg]] \|
[[File:StereoLeft.jpg]] \| left \| The eye is encoded into the left half
of the image. Assumes the source is half-SBS but the aspect ratio will
need to be halved for full-SBS. [[File:StereoLr.jpg]] \|
[[File:StereoRight.jpg]] \| right \| The eye is encoded into the left
half of the image. Assumes the source is half-SBS but the aspect ratio
will need to be halved for full-SBS. [[File:StereoTb.jpg]] \|
[[File:StereoLeft.jpg]] \| top \| The eye is encoded into the top half
of the image. Assumes the source is half-SBS but the aspect ratio will
need to be halved for full-SBS. [[File:StereoTb.jpg]] \|
[[File:StereoRight.jpg]] \| bottom \| The eye is encoded into the bottom
half of the image. Assumes the source is half-SBS but the aspect ratio
will need to be halved for full-SBS. \|}

=== Developer notes ===

picture_t contains a new field i_eye that is the eye the picture
represents. Valid values at the moment are:

{\| border="1" 0 \| The picture is 2D. 1 \| The picture is destined for
the left eye. 2 \| The picture is destined for the right eye. \|}

Flags: {\| border="1" STEREO_WAIT_FOR_NEXT_FRAME_BIT \| Do not present
straight away and instead wait for the next frame. \|}

The default value for i_eye is 0, and all present video codecs output
frames where i_eye is 0. It is up to the stereoscopy module to split it
into left and right. But it's possible for someone to develop a video
codec that output pictures where i_eye&gt;0, for example for a container
format where the data is stored as separate left/right images. In this
case the stereoscopy module does nothing, and forwards the pictures on
as is.

Mask i_eye by STEREO_EYE_MASK to get the eye number without any flags.
It is possible that two images represent the same point in time (this is
only untrue for field sequential video). If the
STEREO_WAIT_FOR_NEXT_FRAME_BIT is set then the vout shouldn't present
the frame straight away, but expect another picture immediately joining
it representing the other eye at the same point of time, and display
them together at once.

== nVidia 3D Vision == The focus of the Google SoC project has been on
nVidia 3D Vision. To use 3D Vision you require the following:

-  A compatible nVidia GPU
-  nVidia 3D Vision Kit (the glasses you wear)
-  A 120Hz LCD or 100Hz CRT monitor
-  Windows

You also have to rename 'vlc.exe' since VLC isn't yet supported by the
nVidia drivers. I'd recommend 'wow.exe' or 'googleearth.exe'. Also, make
sure you have 3D Vision enabled in the nVidia control panel.

3D Vision will work straight out the box with the Direct3D (XP) vout.
You don't need to do anything special, it'll activate as soon as the
Direct3D vout starts receiving stereoscopic frames.

== AMD HD3D == I would really love to start working on supporting AMD
HD3D, but I need your help, see [[#Donations|here]].

== Quad Buffered OpenGL == There is some experimental code for
quad-buffered OpenGL if you build from source. I highly doubt it will
work since I currently lack the hardware needed to test it. Help speed
up development, see [[#Donations|here]].

== Other Planned Features == \* ''A vout-independent anaglyph combining
filter.'' This will combine the images for both eyes into a single
anaglyph image before being passed to the vout. This will make it
possible to display stereoscopic content with non-stereoscopic-aware
vouts. \* ''3D TV output.'' Non-HDMI 1.4 3D outputs - e.g. outputting
side-by-side checkerboard, row interleaved, etc. \* ''Other proprietary
shutter glasses''. For example e-Dimensional. \* ''More input formats''.
Column and row interleaved input sources.

== Donations == The best way you can help me out is by donating
hardware. Any hardware you donate will become my top priority to add
support for. If you do wish to donate, please contact me by e-mail at
messiahandrw-at-gmail-dot-com (my shipping address is in Australia).
I'll accept any hardware that you wish to donate, however the following
will be especially useful:

-  AMD Radeon HD 5xxx or 6xxx.
-  AMD FirePro Vx800, Vx7x0
-  HDMI 1.4 compliant 3D TVs
-  120Hz monitors

If instead you'd like to donate money for me to purchase the above
hardware, see [http://pledgie.com/campaigns/16038 my pledge].

== Troubleshooting & Support == There are several issues I am aware of.
If you need support directly from me or have any enquiries then feel
free to e-mail me directly at messiahandrw-at-gmail-dot-com (also
mention Stereoscopic VLC in the subject so I don't mistake it for spam).

=== VLC Crashes when I click stop === I know about this bug and I'm
trying to fix it, so stay tuned!

=== The frame rate is too slow === The stereoscopy module is alternating
outputting left and right frames, because VLC starts to drop frames when
I start doubling the frame rate. I'm working on a way around this (and
if you're a developer I'd love for some input on this!)

=== My Video is black! === Either there's a bug I don't know about, or
the stereoscopy module doesn't support your particular colour encoding.
Check VLC's messages to see if anything is being reported (Tools >
Messages). Either way, e-mail me and I'll get straight on to it!

=== 3D Vision isn't working === This could be any number of things: \*
3D Vision is not enabled in the nVidia control panel. \* You haven't
renamed vlc.exe (see above). \* You're not using the Direct3D vout. \*
The stereoscopy module is turned off. \* You don't have the latest
nVidia drivers.

I'd love to solve your issue, but please check VLC's messages for any
warnings and errors before contacting me.
