{{SoCProjectstudent=[[User:barrywardellmentor=[[User:ILEoo|Ilkka
Ollakka]]}}

== Project Abstract == While it is easy to use and functional, the
existing default, Qt based GUI for VLC is targeted towards use on the
desktop. I propose to develop a new "Media Center" style GUI. This GUI
will be based on Qt and OpenGL and will aim to be aesthetically
pleasing, while remaining easy to use and functional. It will draw on
many nice features of other popular media center software such as Front
Row, Windows Media Center and XBMC.

There was a Summer of Code project last year by Dylan Yudaken to work on
PVR improvements. This project included some work on a PVR-style
interface using OpenGL. My project could potentially build on this work
to develop a fully fledged media center interface.

== Compiling the GUI == The media center GUI was created with the
intention of being able to make use of the many cutting edge
improvements that have come to Qt in recent versions, some of which are
not yet available in the most recent Qt release. As a result, compiling
it is a bit more involved than compiling the standard version of VLC.
These instructions assume that you are already able to compile the VLC
master branch and will just discuss the extra steps required for
compiling the Media Center GUI. Once Qt 4.6 is released, some of this
will become redundant.

=== Dependencies ===

==== Recent version of SQLite 3 ==== The media library requires a recent
version of SQLite (I think 3.6 or newer). Ubuntu 9.04 (Jaunty) already
includes a sufficiently recent version, although older operating systems
may not.

In particular, the version of SQLite included in the latest version of
OS X Leopard is 3.4.0, which is too old. It's relatively straightforward
to install a more recent version using [http://www.macports.org
MacPorts]. Just install MacPorts and then do <code>'sudo port install
sqlite3'</code>.

==== Qt 4.6 ==== The Media Center GUI makes use of the Qt
[http://doc.trolltech.com/4.6-snapshot/animation-overview.html
animation] and
[http://doc.trolltech.com/4.6-snapshot/statemachine-api.html state
machine] frameworks from the
[http://labs.trolltech.com/page/Projects/Graphics/Kinetic Kinetic]
project. These frameworks were previously available as Qt solutions
([http://www.qtsoftware.com/products/appdev/add-on-products/catalog/4/Utilities/qtanimationframework/
animation],
[http://www.qtsoftware.com/products/appdev/add-on-products/catalog/4/Utilities/qt-state-machine-framework/
state machine]), were recently
[http://labs.trolltech.com/blogs/2009/05/25/animations-and-state-machine-apis-in-qtmaster/
merged] into Qt's master branch and are scheduled for inclusion in the
next version, Qt 4.6, scheduled for release later this year. It also
requires the QtOpenGL and QtSVG modules, which are already included in
Qt 4.5 and above.

To get a sufficiently recent Qt version, you need to checkout the code
from their Git repository and compile it yourself. This isn't as
difficult as expected, but does it take some time to compile. The basic
steps are:

-  Checkout the git repository: <code>git clone
   git://gitorious.org/qt/qt.git\ </code>
-  (optional) Switch to the master-stable branch: <code>git checkout -b
   master-stable origin/master-stable</code>. This branch was designed
   to give you code that is guaranteed to at least compile, whereas the
   master branch doesn't guarantee anything. See
   [http://labs.trolltech.com/blogs/2009/07/28/getting-the-best-out-of-two-worlds/
   this] blog post for more details.
-  <code>./configure</code>
-  <code>make</code>
-  <code>sudo make install</code>

This will install Qt into <code>/usr/local/Trolltech/Qt-4.6.0/</code>.

==== OpenGL ==== It is required that OpenGL be working on your system.
Any OpenGL implementation that works with Qt's OpenGL module (which I
think most do) should be fine.

=== Getting the code === All of the code for this project is available
in the
[http://git.videolan.org/?p=vlc-barry.git;a=shortlog;h=refs/heads/qtmc
qtmc] branch of [http://git.videolan.org/?p=vlc-barry.git my git
repository]. The code can be checked out using:

<code>git clone git://git.videolan.org/vlc-barry.git\ </code>

and then switching to the qtmc branch:

<code> cd vlc-barry

git checkout -b qtmc origin/qtmc </code>

=== Compiling === Compiling follows the normal VLC compilation process,
but we need to make sure the new version of Qt gets used:

<code> export PATH=/usr/local/Trolltech/Qt-4.6.0/bin:${PATH}

export PKG_CONFIG_PATH=/usr/local/Trolltech/Qt-4.6.0/lib/pkgconfig/
</code>

and also need to give a few extra options to configure (the last two are
optional):

<code>../configure --enable-qtmc --enable-media-library --enable-sqlite
--enable-debug --disable-nls</code>

If SQLite has been installed in a non-standard place (as is the case in
OS X), you also need to direct configure to that location:

<code>../configure --enable-qtmc --enable-media-library --enable-sqlite
--enable-debug --disable-nls --with-sqlite=/opt/local/</code>

=== Running === The code is run in the usual way, but you specify that
the media center interface and opengl vout should be used:

<code>./vlc -Iqtmc -Vopengl</code>

or on OS X

<code>./VLC.app/Contents/MacOS/VLC -Iqtmc</code>

Before any media will appear in the browsing screens, make sure to
configure the Media Library search paths in the settings.

== Status == I will post regular status updates to
[http://www.barrywardell.net/gsoc/gsoc-blog my blog].

== Projected Timeline == April 20 Accepted for summer of code!

April 20 - May 23 Familiarise myself with the VLC code and the PVR code
in the vlc-dylanza git repository. Meet with my mentor and the
developers on IRC and the mailing list to discuss plans for the project.
Determine a realistic set of goals to aim towards.

May 23 - June 6 Begin planning of the interface. Collect the best ideas
from other media centers and determine what will be involved to
implement each of these ideas. Start writing code to implement the GUI,
either building on top of the existing PVR code or starting anew.

June 7 - June 15 I will aim to have some initial code incorporating VLC
into a full screen window. This will allow for basic control of playback
of audio and video.

June 15 - June 21 I will be attending the conference "12th Capra Meeting
on Radiation Reaction" and will take a break from Summer of Code.

June 21 - July 6 I will aim to have at least a minimal Qt/OpenGL Media
Center GUI fully up and running with at least basic functionality of
video playback and playlist support. I will then continue to refine the
interface, adding functionality and documentation.

July 6 - July 13 I will prepare for the mid term review and will aim to
have completed any tasks my mentor has deemed necessary for me to pass.

July 12 - July 18 I will attend the conference "Twelfth Marcel Grossmann
Meeting".

July 20 - Aug 7 I will aim towards a functioning Media Center GUI
running on at least one Operating System (ideally, the code will be
written in a cross-platform way since it will make use of Qt/OpenGL). It
may not be as fully featured as existing media center software, but will
provide a good base for future work to build on. It will support
browsing for media and playing back of video and audio.

Aug 8 I will aim to have my project completed ahead of the suggested
pencils down date and will take a holiday.
