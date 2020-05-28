So I am a newbie and it's possible I missed some things that are obvious
to more seasoned linux/vlc/c coders- but there is lots of information
missing here in regards to successfully cross-compiling an out-of-tree
module against the latest released VLC, from Linux with windows target

Here's what ended up working for me- please consider integrating
whatever is correct here into the main page (and correcting what isn't,
;))

1) This line is misleading: "On Debian/Ubuntu, you can simply install
   them: sudo apt-get install libvlc-dev. On Windows, you can find those
   files within the vlc-\ *-win*.zip file, inside the sdk/ directory."

First of all, it's not clear whether we're talking about the host or
target system. Secondly, the zip file for 2.2.1 (latest release as of
this writing) does not contain all the correct folders, while the .7z
does!

2) Hint to compiler install - basically, some of the info needs to be
   grafted from the main compiling for windows32 page. Specifically, the
   requirement to get the mingw cross-compile toolchain setup.
3) The Makefile here is only for Linux, would be great to provide one
   for cross-compiling. I'm too embarrassed to admit how long it took me
   to figure out, but for example when cross-compiling it should use
   x86_64-w64-mingw32-gcc (or whatever the target host is -gcc and -ld).
   Also the -z and defs flags threw errors for me and I needed to change
   the output from .so to .dll (cosmetic but important). Overall I was
   just sortof taking what worked on linux natively, and slowly adjusted
   piece by piece till it compiled on windows. Would be good to know
   what a proper Makefile would look like though :)
4) This took me forever to figure out since tons of googling yielded
   nothing- and was ultimately the clincher for what put everything
   together- so I'm guessing there's a more automatic way, but like I
   said above I'm describing what worked for me and it could be thought
   of more as a hint than the ultimate way to do it: essentially,
   PKG_CONFIG_PATH envrironment variable must be set to the *windows*
   sdk (the one that comes via the 7zip)/lib/pkgconfig - and also the
   \*.pc files in there need to be edited!

Edited means that the paths should be changed from /home/funman/etc. to
the actual location of the sdk. The -I includes are also hardcoded, and
even repeated..all and all the .pc files need to be cleaned and edited
for a few easy lines (this is one reason I'm guessing I missed something
and maybe this is automated somewhere)

5) I did all this and was then able to compile the old time filter with
   a new name/description on linux and export it as dll to be brought
   over to a windows machine, targeting windows 64 bit. Yay!

--[[User:Dmkotalk]]) 23:57, 1 June 2015 (CEST)
