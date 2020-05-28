== Installing VLC under Redhat/Fedora ==

Set up Yum Repositories such as Livna http://rpm.livna.org etc.After you
have followed the instructions there.

   [root@x32.fedora.prudhvi.in]# yum install vlc

will install VLC Media Player.

If you have any issues inputting from an external device to the
"line-in" under Redhat, be sure to check the /etc/.aumixrc file. By
default, it doesn't contain an entry for recording from the line-in
device. Add one and reload the mixer settings (the command can be found
in /etc/modules.conf) and you're good to go.

--[[User:Prudhvi|Prudhvi]] 07:43, 6 April 2006 (CEST)

== Installing VLC under CentOS (EL5) ==

# download and install the latest rpmforge-release rpm (e.g.
rpmforge-release-0.3.6-1.el5.rf.i386.rpm) # either;

   yum install vlc

or (if you have epel-release installed);

   yum --disablerepo='epel' install vlc

(otherwise you may receive the error;
   Missing Dependency: libdvdread.so.3 is needed by package
   vlc-0.9.9a-4.el5.rf.i386)

[[Category:GNU/Linux distros]]
