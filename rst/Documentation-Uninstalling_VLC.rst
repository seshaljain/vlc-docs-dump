{{RightMenu|Documentation TOC}} == Windows
[[File:Windows-logo.jpg%7C40x40px]] == You can uninstall VLC from
''Add/Remove Programs'' (''Programs and Features'' in Windows 7) located
in the ''Control Panel''. Search for VLC media player and right click,
then select "Uninstall/Change". Follow the prompts to finish the
uninstallation.

[[File:Remvlc.jpg%7C600x422px%7Ccentre]]

Alternatively, you can browse to VLC's installation directory (for a
typical install, go to your ''C: Drive'' and look for Program Files (if
64-bit, Program Files (x86) )&rarr;VideoLAN&rarr;VLC and double-click on
the ''uninstall'' link and follow the prompts to uninstall.

[[File:Winunvlc.png%7C600x422px%7Ccentre]]

== macOS [[File:Applelogo.jpg%7C40x40px]] == Drag the VLC application to
your trash can. You can also remove the configuration file and the cache
files in '''~/Library/Preferences/VLC/'''. There is an AppleScript on
the disk-image which lets you do this automatically.

If that did not work, you can double-click on the ''Applications'' icon.
This will bring up a list of all applications on your Mac. Scroll
through the list of Applications, then press and hold the ''Ctrl''
button to bring up a table of options and actions. Click on "move to
trash".

Finally, if the previous processes failed, you can try downloading a
third-party uninstaller program to uninstall it, such as
[http://www.macupdate.com/app/mac/25276/appcleaner AppCleaner].

[[File:Appcleaner.png%7C300x200px]]

== Linux == === Debian [[File:Debian.png%7C40x40px]] === Remove the
packages that you installed: # '''apt-get remove --purge vlc
libdvdcss2'''

==== Ubuntu [[File:Ubuntulogo.png%7C45x45px]] ==== Remove ''VLC Media
Player'' by entering this command in the Terminal. $ ''' sudo apt-get
remove vlc ''' Or you can also search ''VLC'' in the ''Ubuntu Software
Center'' and click on ''Remove'' to uninstall it.

[[File:Ubunvlc.png%7C550x500px]]

=== Red Hat and SuSE
[[File:Redhat.jpg%7C40x40px]][[File:Suse-Logo.png%7C35x35px]] ===
Uninstall the RPM packages that you installed: # '''rpm -e vlc-version
vlc-mad-version wxvlc-version libdvdcss2-version libdvdpsi1-version'''

== Compiled the sources by yourself == Go to the directory containing
VLC sources and execute # '''make uninstall''' You can then remove the
VLC sources.

{{Documentation}}
