(comments withdrawn)

First of all, this wiki isn't the correct place to discuss this kind of questions. vlc-devel at videolan is a far better place. Anyway, it's correct that you can use the 10.4u SDK as well. In fact, VLC obviously automatically does so on Intel-based Macs. Concerning your 2nd comment
   no further tool beside the default installation to /usr/local is
   required to build VLC (excepting svn/subversion in rare cases). Any
   other 3rd party library, which would usually end up in that directory
   is built and installed inside VLC's code base, in extras/contrib to
   be precise. That's clearly stated on this HOWTO page. Please mail the
   mailing list mentioned above for further feedback. Additionally, when
   complaining about VLC in general or particularly documentation, keep
   in mind that we're doing this in our spare time and that we aren't
   required to answer your requests, especially when strangers to this
   project get demanding and impolite. [[User:Fkuehne|feepk]] 01:27, 1
   February 2007 (CET)

== Git from other Sources ==

If you don't have git, then it can also be installed using MacPorts:

   sudo port install git-core

== With latest changes to build for x86_64...
--[[User:Pdherbemont|Pdherbemont]]== I think we need
--host=x86_64-apple-darwin10 (and --build=x86_64-apple-darwin10 is not
mandatory)

== Change how the build intruction are shown
--[[User:Pdherbemont|Pdherbemont]] 20:34, 31 May 2007 (CEST) == I would
suggest we put the build command in some form easier to read, like :

-  Build the third party libraries cd vlc/extras/contrib ./bootstrap
   make

\* Now build vlc
   ./bootstrap ./configure make

(By the way, the current instruction to use make src doesn't work. make
alone is sufficient and necessary. --[[User:Chjones|Chjones]] 00:59, 18
June 2008 (CEST))

== Please don't link to subversion --[[User:Pdherbemont|Pdherbemont]]
12:15, 2 May 2008 (CEST) ==

= Compiling VLC on Mac OS X (draft) = Compiling {{VLC}} on Mac OS X is
different from normal compilation on Linux and Mac OS X. We do not use
Xcode, nor a simple <code>./configure</code> and <code>make</code>.
Below you will find instructions for how to compile VLC on Mac OS X -
remember to check the prerequisites before taking the plunge.

If you wish to develop or test please join the vlc-devel mailinglist.

Please do not publish any of the non-released test binaries or
svn-compiles on software sites or on user-forums. We have had bad
experiences with this before and we do not appreciate it.

== Prerequisites == \* Mac OS X 10.4.x (Tiger) or 10.5.x (Leopard) \*
Xcode 2.4.x or Xcode 2.5

Optional: \* Subversion

Mac OS X 10.4 (Universal) SDK (a part of Xcode) is required to build the
external libraries of VLC.

Your GCC version should be set to 4 (the default setting).

Xcode can be found online or on the Developer Tools disc, which
accompanied Mac OS X.

Compiling with earlier releases of Mac OS X and/or Xcode will not work.

''If building {{VLC}} on Mac OS X 10.5 Leopard, be sure to read the
paragraph on this specific version below, before proceeding.''

=== Mac OS X 10.5 Leopard === Note, that only VLC's current development
trunk can be compiled on Mac OS X 10.5 Leopard. While the 0.8.6 series,
when compiled on Tiger, works on Leopard (as expected), no current
stable branch compiles on Mac OS X 10.5 Leopard.

As widely published, this version of Mac OS X includes a new release of
Xcode, called Xcode 3, which includes many cool new features, but
unfortunately, it is incompatible with VLC. You need Xcode 2.5 to
compile VLC on Leopard, which can easily be installed in addition to
your Xcode 3 tools. However, you need to edit your PATH variable before
doing anything with VLC's source. In case that you installed to to the
default location (<code>/Xcode2.5</code>) and you are using the default
shell (<code>bash</code>), this is pretty simple:

<code>export
PATH=/Xcode2.5/bin:/Xcode2.5/sbin:/Xcode2.5/usr/bin:/Xcode2.5/usr/sbin:$PATH</code>

Note that you need to repeat this PATH edit every time you relaunch the
shell. You can avoid this by editing your bashrc file. Once Apple
releases a fixed linker for Mac OS X Leopard, this work-around will not
be necessary anymore and you can use Xcode 3 as expected.

Starting with Leopard, Xcode may be installed to a custom location on
the administrator's choice. While this is non-problematic for ordinary
Xcode projects, VLC needs a little help. You have to place extra
symbolic links in /Developer pointing to your custom location for these
folders:

<code>usr, Headers, Private, SDKs, Tools, Makefiles</code>

You can easily create these links by executing the following command for
each folder (whereas theFolder is one of these six):

<code>ln -s /full/path/to/Developer/theFolder
/Developer/theFolder</code>

=== Regarding Fink === If you have Fink installed, then you will need to
disable it. {{VLC}} has it's own form of Fink (in the extras/contrib
subdir) and it can conflict with Fink. We use this system to generate a
reliable, consistent and known amount of packages that {{VLC}} requires.

''To disable Fink comment the line: #source /sw/bin/init.csh in your
.cshrc file or . /sw/bin/init.csh in your .bashrc file in your
home-directory.''

== Steps ==

Please follow these steps for compiling:

=== Get the source === Download the {{VLC}} [[GetTheSource "Get the
source"]] page) or get a recent source tarball. Note that the 3rd party
libraries will probably break a few months after the release's
publication.

These instructions below are always for the currently unstable,
non-released code.

If you compile from [[Subversion]] then please remember that this code
can often be in an unstable state.

=== Build external libs ===

We now need to build the [[Contrib_Status\| 3rd party libs]]. For that,
you will need to: \* cd to the source directory with your Terminal
application. \* cd to the extras/contrib subdir of VLC and execute
<code>./bootstrap</code> \* Now execute <code>make src</code>. This will
download and compile all the required external libraries and programs.
You will only have to do this once. (You can do it again if required
libraries are added or updated by the team.) ''If bootstrap exits with
an error message on Mac OS X Leopard, check the paragraph on this
version above.''

=== Prepare the VLC build === Now we return to VLC itself. Go back to
the top level VLC source directory. If you use Subversion (which you
really should), then run <code>./bootstrap</code>.

This will create configure and Makefiles for {{VLC}} (snapshots and
releases already include this).

=== Configure the VLC build ===

The next step is to configure, in the top level VLC source directory.

In current trunk revisions, you can simply run <code>./configure
--enable-debug --with-macosx-sdk</code> to get VLC in its default
configuration. If do not want to use VLC's default configuration for
Mac, be sure to add <code>--disable-macosx-defaults</code> to your
custom set.

When compiling earlier revisions or the 0.8.6 branch, you need to give a
wide variety of configure flags to achieve a useful build. We used to
use this set: <code> ./configure --enable-debug --disable-x11
--disable-xvideo --disable-glx --enable-sdl --enable-mad
--enable-libdvbpsi --enable-a52 --disable-dvdplay --enable-dvdnav
--enable-dvdread --enable-ffmpeg --enable-faad --enable-flac
--enable-vorbis --enable-speex --enable-theora --enable-ogg
--enable-shout --enable-cddb --disable-cddax --enable-vcdx
--disable-skins --disable-skins2 --disable-wxwidgets --enable-freetype
--enable-fribidi --enable-caca --enable-live555 --enable-dca
--enable-goom --enable-modplug --enable-gnutls --enable-daap
--enable-ncurses --enable-libtwolame --enable-x264 --enable-png
--enable-realrtsp --enable-lua --disable-libtool</code>

You can add <code>--with-mozilla-sdk-path=./extras/contrib/gecko-sdk
--enable-mozilla</code> to the configure-line to enable the compilation
of VLC's Safari/Firefox plugin.

=== Build VLC === After configure is finished, we can finally build
{{VLC}}. A simple <code>make</code> will do the trick. If you want to
use the resulting application package on a different Mac or a different
account on the same Mac, run <code>make VLC-release.app</code>
afterwards. Use the resulting ''VLC-release.app'' for these purposes.

== History == Written by Jean-Alexis Montignies,
[[User:FkuehneJean-Baptiste Kempf]]. Edited by Jesper Stemann Andersen.

[[Category:Building]] [[Category:Coding]]

== regarding "How to disable Fink" ==

On 10.5.6 with current fink I found the fink initialization in .profile
as <code>test -r /sw/bin/init.sh && . /sw/bin/init.sh</code>

Suggested new wording:

''To disable Fink comment the line: ''<code>#source
/sw/bin/init.csh</code>'' in your .cshrc file or ''<code> .
/sw/bin/init.csh</code>'' in your .bashrc file or ''<code> test -r
/sw/bin/init.sh && . /sw/bin/init.sh</code>'' in your .profile file in
your home-directory.''

== Proper way to initialize the environment ==

On my point of view its not a good idea to skip

<code> export CFLAGS="-arch \*"

export CXXFLAGS="-arch \*"

export LDFLAGS="-arch \*"

export OBJCFLAGS="-arch \*" </code>

Without, my system will get confused and secondary its the most proper
way to initialize the environment.

Greets

== Compiling MobileVLCKit error ==

While trying to compile MobileVLCKit contained in
vlc/projects/macosx/framework i get a "missing vlc-plugins.h" error. I
don't know where to get this file, since it is not cantained in any
package I've seen... Does somebody know what can i do?

== When I built on OS X 10.6.8 ==

the bootstrap script alerted me that it was building a 32-bit version:
<blockquote> \* VLC will be compiled in 32bit mode. *<br>* *<br>* Re-run
with the x86_64-apple-darwin\* argument to turn on *<br>* 64bit
compilation for Intel-based Macs, whereas \* is either *<br>* 9 or 10
depending on your Darwin version. *<br>* There is NO PPC64 support right
now. <br> </blockquote> Now that didn't work:<br> <blockquote> cat:
src/Distributions/x86_64-apple-darwin10.mak: No such file or directory
</blockquote> in ./src there is darwin64 and darwin or macos32 and
macosx64. I used ./bootstrap macosx64 and it worked. Perhaps there could
be something about this, especially as the script give the user
incorrect instructions.

<br>
