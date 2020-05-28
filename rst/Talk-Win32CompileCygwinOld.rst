('''Aaron''') There appears to be a good chance that if you follow these
instructions you will not be able to easily run your compiled program.
The easy fix is to delete (or rename) vlc.exe.manifest and then you
should be able to run your compiled code.

Any chance we can get this added to the instructions?

I'm noticing some spelling errors and other minor issues. Lateron is two
words for example. What does it take to be able to make minor
modifications to these pages? [[User:Daniel.CardenasXtophe]] 15:56, 23
April 2007 (CEST)

=General: - I would suggest a sample dir structure:

~/vlc ~/vlc/downloads ~/vlc/scripts ~/vlc/SVN ~/vlc/SVN/x264-trunk
~/vlc/SVN/vlc-trunk ~/vlc/SVN/ffmpeg-trunk

reason: '~' always exists, even in the broken-nest installs. No need to
start talking about c:downloads and c:cygwinadminstratorhomewhatever.
One work dir: ~/vlc

= I would suggest making this document more intuitive by putting the
reccomended build way in one page, and putting all 'optional' things in
a side document (for example the way to download a nightly as
alternative to download from SVN)

= Add 'scripts' to the path variable, perhaps in a script.

= Running through the document step by step my comments:

= Its called pkg-config not pkgconfig

= Reorder: I would first describe the reccommended option to download
latest (SVN) then below that, add some OPTIONAL: paragraphs. Now its the
'optional' way fisrt.

= The SVN section suggests to make a 'scripts' directory and then copy
the created scripts to the 'root' directory. I would suggest adding a
'cd /home/admin/vlc/SVN' command to the scripts instead.

= While it lists 'gcc-3.4.5' as the right version, this one isn't
available. Additionally, the prebuilt
contrib-20060730-win32-bin-gcc-3.4.5-only.tar.bz2 (example) should also
work with 3.4.4 so maybe this should be renamed.

= Contrib downloads to some directory fine, but later on it says 'copy
to /home/administrator.. why not directly cd to ~/vlc/downloads and
untar from there

= Suggested addition to AMR directory unpacking:
   -  This results in dirs like:
      'C:cygwinhomeAdministratorffmpeg-trunklibavcodecamr' that just
      contain files, no subdirs.'

= Reasons should be added for enabling QT. (extra work eek).. so mention
the reason. (better interface?)

= The 'Configure script for compiling VLC' itself is mentioned too
early. I think that you should FIRST mention the optional configuring of
ffmpeg/x264 and when those are done (and compiled!) then start to talk
about main vlc. Chronology!

= ffmpeg (trunk svn): --enable-mingw32 doesnt work anymore - remove =
ffmpeg (trunk svn): --enable-faac doesnt work. --enable-libfaac works =
ffmpeg (trunk svn): --enable-mp3lame doesnt work. --enable-libmp3lame
works = ffmpeg (trunk svn): --enable-amr_nb --enable-amr_wb doesnt work.
--enable-amr-nb --enable-amr-wb works BUT - amr installation in ffmpeg
works differently now. Check: http://www.penguin.cz/~utx/amr -> download
http://ftp.penguin.cz/pub/users/utx/amr/amrnb-6.1.0.2.tar.bz2 -
./configure;make;make install -> download
http://ftp.penguin.cz/pub/users/utx/amr/amrwb-6.0.0.1.tar.bz2 -
./configure;make;make install

= I would suggest the extra --enable-xvid too

== When & Where the file "configure" comes out in
"C:cygwinhomeAdministrator"? ==

When & Where the file "configure" comes out in
"C:cygwinhomeAdministrator"? Thanks
