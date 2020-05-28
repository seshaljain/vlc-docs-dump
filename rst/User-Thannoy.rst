General presentation
--------------------

Hello! My name is *Anthony Loiseau*.

I worked around with `Remiii <User:Remiii>`__, `Cyril <User:Cmathe>`__, `Sinseman44 <User:Sinseman44>`__ and `Poe <User:Poe>`__ (were workmates in the so called *RatatouilleTeam*) in Actech (Angers, France) on an IP PVR project named Cybervia.

Why does Actech help(ed) VideoLAN? (through us and through `skanda <VideoLAN_Sites#Servers>`__ hosting donation)

Because VLC is a great and free tool, it decodes many formats and can be embed in web pages. We can look into its source code to understand better how we can take advantage of it. We use it and we are proud to promote it in our product (check our `website <http://www.cybervia.com/>`__ for more informations about our IP PVR).

see you!

Contact
-------

email : myNickName @gmail.com

IM : myNickName @jabber.org

IRC : myNickName on freenode and #thannoy on freenode

VLC project
-----------

My work will be mainly focussed on mozilla-plugin and activeX parts of VLC. **Since I didn't worked on VLC lately, most of informations written bellow are out-of-date.**

Mozilla plugin
~~~~~~~~~~~~~~

The file projects/mozilla/control/npolibvlc.cpp describe the API which should be accessible by moz-plugin. The dedicated page for its API is `here <Documentation:Play_HowTo/Advanced_Use_of_VLC#Use_the_mozilla_plugin>`__.

List of methods which should be accessible
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here is the list extracted from the file *projects/mozilla/control/npolibvlc.cpp* by a script(will be given soon, need doc, clean and a little debug maybe) :

(release 0.9 - [rev 25203, 2008-02-20_16h20])

-  .playlist.items.count : INT32
-  .playlist.items.clear([]) : VOID
-  .playlist.items.remove(['number']) : VOID
-  *.playlist.itemCount : INT32*
-  .playlist.isPlaying : BOOLEAN
-  .playlist.play([]) : VOID
-  .playlist.prev([]) : VOID
-  *.playlist.clear([]) : VOID*
-  .playlist.stop([]) : VOID
-  .playlist.next([]) : VOID
-  .playlist.add(['STRING', 'STRING', 'OBJECT']) : INT32
-  .playlist.removeItem(['number']) : VOID
-  .playlist.togglePause([]) : VOID
-  .playlist.playItem(['number']) : VOID
-  .VersionInfo : STRINGN
-  .log.verbosity : DOUBLE
-  .log.messages.count : INT32
-  .log.messages.clear([]) : None
-  .log.messages.iterator([]) : OBJECT
-  .video.fullscreen : BOOLEAN
-  .video.subtitle : INT32
-  .video.crop : STRINGZ
-  .video.height : INT32
-  .video.width : INT32
-  .video.teletext : INT32
-  .video.aspectRatio : STRINGZ
-  .video.toggleTeletext([]) : VOID
-  .video.toggleFullscreen([]) : VOID
-  .input.rate : DOUBLE
-  .input.state : INT32
-  .input.hasVout : BOOLEAN
-  .input.length : DOUBLE
-  .input.fps : DOUBLE
-  .input.time : DOUBLE
-  .input.position : DOUBLE
-  .audio.volume : INT32
-  .audio.track : INT32
-  .audio.channel : INT32
-  .audio.mute : BOOLEAN
-  .audio.toggleMute([]) : VOID
-  .versionInfo([]) : STRINGN

VLC tips
--------

First steps in compile process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First compile attempts are more difficult than further ones, mainly because of missing third-party packages. You can get a list of those packages here : `Contrib_Status <Contrib_Status>`__

The proper way to compile is described in many places (`boostrap, configure, make, make install <UnixCompile>`__). At configure stage, you can be informed of missing needed packages. You should look its output to find many problem origins.

I suggest you to store its output to a file. Like this you will be able to get a look at ".. no" ending lines at anytime. To do such, you can use "tee" command on linux (it archive a copy of the output to a file) : ./configure --all --your --args=here \| tee my_configure.out

When a package is missing, saying for example "ffmpeg/avcodec.h", you have to find a package about it (in fact libavcodec-dev in this case)...

On debian based distros, you can find libavcodec-dev in those ways :

| ``apt-cache search avcodec``
| ``# or with a graphic tool:``
| ``synaptic``

and you can install this package in those ways (with root privileges) :

| ``apt-get install libavcodec-dev``
| ``# or with a graphic tool:``
| ``synaptic``

\ *\\ keywords : compile /*\ 

debian etch gettext and git-core
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On debian etch (4.0r3), some packages are quite old. Too old for videolan. You can get up-to-date packages using `backports <http://backports.org>`__. Its usage is explained on its website.

Packages I have packported are:

-  git-core
-  git-email
-  gitk
-  wine (only needed to work on ActiveX API, IDL cross compiler)
-  wine-dev (only needed to work on ActiveX API, IDL cross compiler)

What about gettext? Only release 0.16.1 is available, even in backports. For now I have modified configure.ac in this way:

``AM_GNU_GETTEXT_VERSION(0.16.1)``

instead of 0.17.

NB : You can use backport inside synaptic GUI through "force version" menu item.

mozilla-sdk under debian Etch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have problems finding mozilla-sdk, try to install package *libxul-dev* and add to your ./configure the parameter *--with-mozilla-sdk-path=/usr/lib/xulrunner/sdk*

Resume :

| ``su``
| ``apt-get install libxul-dev``
| ``exit``

| ``./configure '--with-mozilla-sdk-path=/usr/lib/xulrunner/sdk' ...with-your-other-params...``
| ``# with other-params including "--enable-mozilla", otherwise I don't think mozilla-sdk is useful for you``

\ *\\ keywords : mozilla-sdk mozilla-config.h libxul-dev configure /*\ , \ **not tested**\ 

undefined symbol: XpmReadFileToImage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Recently, I have had a problem running mozilla plug-in. It was because for libvlcplugin.so, ld never tries to find symbol XpmReadFileToImage into the right lib (libXpm.so). Here is a workaround which have worked for me :

| ``1- su # ask for root console``
| ``2- vi /etc/ld.so.preload``
| ``3-   if the file is empty then``
| ``       add /usr/lib/libXpm.so``
| ``     else``
| ``       append /usr/lib/libXpm.so to its content. each libs must be separated by a space``
| ``       ``
| ``     endif``
| ``4- close vi (ESC : w q)``

\ *\\ keywords : undefined symbol: XpmReadFileToImage /usr/lib/libXpm.so /*\ 

Tools
-----

Firebug
~~~~~~~

Having a JS debugger is very useful to test mozilla-plugin. `Firebug <http://www.getfirebug.com/>`__ is a wonderful Firefox extension for that stuff.

Links
-----

Contributions
~~~~~~~~~~~~~

For you to better understand what I am focused on.

-  `wiki contribution <Special:Contributions/Thannoy>`__
-  `trac activity <http://trac.videolan.org/vlc/search?q=thannoy&noquickjump=1&ticket=on&changeset=on&wiki=on>`__

Inner pages
~~~~~~~~~~~

Some large (and some unuseful) data/pages are in inner-pages to let main pages readable. Here a some of them.

-  `User:Thannoy/stripped_Libvlc_API <User:Thannoy/stripped_Libvlc_API>`__

(feel free to copy/move them if you think it is useful)

Usefull internal links
~~~~~~~~~~~~~~~~~~~~~~

-  `Documentation:Play_HowTo/Advanced_Use_of_VLC#Use_the_mozilla_plugin <Documentation:Play_HowTo/Advanced_Use_of_VLC#Use_the_mozilla_plugin>`__

Usefull external links
~~~~~~~~~~~~~~~~~~~~~~

-  http://www.getfirebug.com/ : Very usefull JS, HTML debugger and tool-set.
-  http://code.revolunet.com/VLCjs/EN : JS libraries to help using VLC HTML plugins
