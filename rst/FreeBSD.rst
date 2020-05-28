== Installing VLC Media Player under FreeBSD ==

Make sure you have upto date Ports collection or Just CVSup your Ports:

   cd /usr/ports make update

Once you have your ports collection up to date, proceed with the
install:

   cd /usr/ports/multimedia/vlc make install clean

If you would prefer to simply install the already-compiled binary
package, with a common set of default compile-time settings, use the
following command:

   pkg_add -r vlc

== Spanish language support ==

VLC compiles and installs correctly from ports, but it has been reported
that the Spanish interface doesn't work properly. There is a Spanish
language file
[https://web.archive.org/web/20071018000700/http://mexinetica.com:80/~lanjoe9/vlc/spanish/vlc.mo
here] from a previous installation that works correctly with the
"20051102 Janus Snapshot".

To use the vlc.mo file provided from the link above, you need to
download it and then (as root), move it to the following location:

"/usr/X11R6/share/locale/{Your Language abbreviation
here}/LC_MESSAGES/vlc.mo"

So in the case of the spanish locale file, you would use the following
command

   mv /downloads/vlc.mo /usr/X11R6/share/locale/es/LC_MESSAGES/vlc.mo

to overwrite the erroneous vlc.mo file.

[[Category:Operating systems]] [[Category:Building]]
