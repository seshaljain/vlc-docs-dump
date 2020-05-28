{{Historical|Support for the WinCE compile was removed in
[http://git.videolan.org/?p=vlc.git;a=commitdiff;h=a7b2dcf0ee052630b5469fb2dac652d307e0784c
a7b2dcf0ee052630b5469fb2dac652d307e0784c]. If you still want to compile
for WinCE, either checkout an older revision, or revert the necessary
removals.}}

=Introduction=

This is a guide for cross-compiling VLC for Windows CE on Linux with a
step-by-step instruction to download, install, configure and build your
VLC.

First, you might want to take a look at [[Win32Compile|compiling
instructions for Win32]], as the process is roughly the same, and it
includes useful discussion and explanations.

= Building VLC =

==Prepare your environment== VLC uses automake, autoconf and friends for
compilation. Make sure they are up to date and usable for your system.

===Get mingw32ce=== To compile VLC, we use Mingw32CE, a
cross-development environment for Windows CE. Download the latest
version on [http://cegcc.sourceforge.net/ Sourceforge].

Go the the directory where you dowloaded CeGCC, and untar it, for example:
   % tar xjf arm-mingw32ce-0.59.1.tar.bz2 -C /

You should now see the folder /opt/mingw32ce.

==Get the source== Start by [[GetTheSource|getting the source]], using
FTP for releases, or using [[Git]] for development. If your are using
the release, download source code and extract the archive and go into
your VLC directory. % cd /path/to/your/vlc/folder/

If you are using the [[Git]] version, start by bootstrapping your VLC.
   % cd /path/to/your/vlc/folder/ % ./bootstrap

==Get the contribs== You can get official WinCE contribs on
[http://download.videolan.org/pub/testing/contrib/
http://download.videolan.org/pub/testing/contrib/], for example
[http://download.videolan.org/pub/testing/contrib/contrib-20091114-wince-bin-gcc-4.1.0-runtime-3.15.2-only.tar.bz2
contrib-20091114-wince-bin-gcc-4.1.0-runtime-3.15.2-only.tar.bz2].
Uncompress them in <code>/usr/wince</code>

== Configuration ==

You need to tweak your configure line.

<tt>./configure</tt> is used to check whether your system is able to
compile VLC. Also you choose the functionalities of your build. %
./configure --help will show you the various options

Create a new file named conf-vlc.sh and add in it:

   PATH=/opt/mingw32ce/bin:$PATH CPPFLAGS="-I/usr/wince/include
   -D_WIN32_WCE=0x0500" LDFLAGS="-L/usr/wince/lib"
   PKG_CONFIG_LIBDIR=/usr/wince/lib/pkgconfig ./configure
   --host=arm-mingw32ce --enable-optimize-memory --disable-directx
   --disable-dvdnav --disable-libgcrypt --disable-mad
   --disable-remoteosd --disable-sdl --disable-skins2

You will probably want to add more options like <code>--disable-sout
--disable-httpd --disable-vlm</code> to remove stuff that you won't need
if your device is limited in storage space and memory.

Save the file and make it executable:
   % chmod u+x conf-vlc.sh

== Compiling source code == Now run your configuration script and build
VLC: % ./conf-vlc.sh % make

== Creating self contained packages ==

Once the compilation is done, you can build self-contained VLC packages
with the following command:

   make package-wince

This will create a vlc-x.x.x.zip archive. Transfer it on your device,
uncompress it and enjoy!

There is not (yet) an option to build a .cab file.

= Using and Debugging VLC =

== Interacting with your device ==

Use [http://www.synce.org SynCE] to synchronize your device with Linux.
Or find an Windows machine with ActiveSync installed and download your
fresh new VLC build.

== Debugging VLC ==

CeGCC provides a stub for GDB to permit remote debugging on Windows CE. To use it, go in the vlc folder:
   % cd vlc-1.0.0 % arm-mingw32ce-gdb vlc.exe

This GDB will upload vlc.exe to /gdb/ on the device. Make sure you
uploaded all the VLC directory on your device.

Then, follow the [http://cegcc.sourceforge.net/docs/debugging.html demo
of a debugging session] for Windows CE.

== Known issues ==

\* There is '''no usable GUI''' for WinCE. There used to be a WinCE GUI
module up to the 1.0 branch, however, it was unmaintained and badly
broken, so it was removed in the 1.1 branch. Yes, not having a GUI makes
VLC pretty useless, so contributions from developers are badly welcome.
\*: The diffs in which the WinCE GUI was removed are
[http://repo.or.cz/w/vlc.git/commitdiff/745cf118bbab187333d581b692f93cd4ca2da898
this one] and
[http://repo.or.cz/w/vlc.git/commitdiff/ba2736f415a73cc336663387e2d3b9225635a8e9
this one]. The module may compile, load and show up when you launch VLC,
but it doesn't work (clicking on buttons doesn't do anything etc).

-  When launching VLC, if you get an error saying "<code>vlc.exe is not
   a valid PocketPC application</code>" (and you use Windows Mobile
   6.1), read
   [http://cegcc.sourceforge.net/docs/faq.html#DllDoesNotWorkWithWindowsMobile6.1
   this] and set up your registry accordingly (yes, that's one entry for
   <code>libvlc.dll</code>, one for <code>libvlccore.dll</code>, and one
   for every DLL in the plugins directory; good luck).
-  If an error message appears about missing DLLs, it might be due to
   mingw32ce dynamically linking against libgcc. The build system of VLC
   doesn't fetch and include this library when it creates the package,
   which is why it is missing. Try looking for <code>libgcc*.dll</code>
   files in <code>/opt/mingw32ce</code> and copying them in the
   directory where you extracted VLC. For the same reason, some C++
   plugins might refuse to load due to a missing libstdc++ DLL, so
   you'll want to copy <code>libstdc++-6.0.dll</code> onto your device
   too.
-  Up to Windows CE 5.0, the memory model limits each process to 32 MB
   of virtual address space. If you compiled VLC with too many plugins,
   they will quickly fill up those 32 MB, which leads too missing
   features, or VLC simply freezing. In any case, check the
   <code>vlc-log.txt</code> file in the root directory for <code>Error
   14</code> logs. If you find some, you can try reducing the memory
   footprint of VLC by disabling some modules during the
   <code>./configure</code> and/or removing them from the plugins
   directory. In my experience, VLC can load a maximum of roughly 16 MB
   of plugins.
-  If the colors are wrong when playing a video (red and blue swapped),
   try removing the libswscale plugin.

See also [[WindowsCE]] [[Category:Building]] [[Category:Windows]]
