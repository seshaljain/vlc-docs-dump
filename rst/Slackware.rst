Installing VLC on Slackware
---------------------------

You can find up-to-date Slackware packages for VLC in `Alien's SlackBuilds <http://www.slackware.com/~alien/slackbuilds/vlc/>`__ repository. These packages are built without adding the ACC encoding libray which has patent issues. However you can easily re-build the package to include the AAC encoder - individuals should not be bothered with patent claims.

External dependencies for VLC
-----------------------------

VLC 3.x and newer use Qt5 for the graphical user interface (GUI). Older versions use Qt4 which has been included in Slackware for many years. The same is not true for Qt5. Slackware versions before 15.0 do not include Qt5.

| This means that in order to run VLC (and to compile it if you want) on any release of Slackware before 15.0 you'll have to install Qt5 and its dependencies first.
| Slackware 14.2 and -current (pre-15.0) are supported through pre-built dependency packages in Alien's repository. These are `libxkbcommon <http://www.slackware.com/~alien/slackbuilds/libxkbcommon/>`__, `qt5 <http://www.slackware.com/~alien/slackbuilds/qt5/>`__ and `qt-webkit <http://www.slackware.com/~alien/slackbuilds/qt-webkit/>`__.
| Additionally, and only for Slackware 14.2, you need `libinput <http://www.slackware.com/~alien/slackbuilds/libinput/>`__ and `libwacom <http://www.slackware.com/~alien/slackbuilds/libwacom/>`__ packages. These were added to Slackware, only after the release of 14.2.

There is one optional dependency: if you want to play encrypted DVD's this requires the DeCSS library. A Slackware package can be found `in Alien's 'restricted' repository <http://slackware.nl/people/alien/restricted_slackbuilds/libdvdcss/>`__.

Building VLC from source
------------------------

-  To rebuild the VLC package and include all *non-free* codecs, download the build directory and then run the SlackBuild script, like this:

::

   mkdir -p ~/slackbuilds/vlc
   cd ~/slackbuilds/vlc
   lftp -c "open http://www.slackware.com/~alien/slackbuilds/vlc/ ; mirror build"
   cd build
   USE_PATENTS=YES sh vlc.SlackBuild

The *SlackBuild* script will automatically download the missing source-code archives and build a new VLC package. After the compilation finishes, you will find a package in the */tmp* directory which you can install using the

::

   installpkg

command. If you already have a *vlc* package installed, then please use the

::

   upgradepkg

command to upgrade that package with the new one.

-  If you do not want the Mozilla plugin to be built you should start the SlackBuild script with an extra variable added in front:

::

   MOZPLUGIN=NO sh vlc.SlackBuild

Mirror sites
------------

You can find my VLC package on the following mirror sites:

-  `slackware.org.uk <http://slackware.org.uk/3rd-party/alien/slackbuilds/vlc/>`__ (thanks to Tadgy for the mirror!)
-  `slackware.org.uk <http://slackware.org.uk/3rd-party/alien/restricted_slackbuilds/vlc/>`__ (version of the package with **all** codecs as well as the DeCSS library already built-in)

--`Alien Bob <User:Alienbob>`__ (`talk <User_talk:Alienbob>`__) 22:01, 16 February 2018 (CET)

`Category:GNU/Linux distros <Category:GNU/Linux_distros>`__
