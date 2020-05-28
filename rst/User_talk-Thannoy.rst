easy discuss/talk here
----------------------

-  Welcome ! `jb <User:J-b>`__ 10:44, 19 February 2008 (CET)
-  Will attend the dev days 08 (on Saturday) :)

TODO list
---------

Wiki Pages
~~~~~~~~~~

-  `Trac <Trac>`__ or `Bug Tracker <Bug_Tracker>`__ explanation (account validation, etc)

   -  @see `Report_bugs <Report_bugs>`__ `VLC_report <VLC_report>`__

-  Backtraces with those chapters (for now, inside `debug <debug>`__ page)

   -  What backtraces are

      -  Rely on accurate release/commit ID

   -  get backtraces

      -  Requirements
      -  Basic use of `gdb <gdb>`__ to debug
      -  Windows gdb how to
      -  libvlc and web plugins debug how to

   -  How to embed backtraces in (trac, wiki, IRC, emails)
   -  links (gdb, `Report bugs <Report_bugs>`__, etc)

-  NB: asked page: "-enable-`debug <debug>`__"

global
~~~~~~

(the newest the upper)

============= =========================================================================== ================== ===========================================
Category      Actions                                                                     States             comment
============= =========================================================================== ================== ===========================================
feature       add a "ts-pid-pmt=pid" CLI option                                           .. raw:: mediawiki  To easily support streams without PAT, etc
                                                                                                            
                                                                                             {{no}}         
doc           improve `Win32Compile <Win32Compile>`__ to add NSI chapter                  .. raw:: mediawiki
                                                                                                            
                                                                                             {{no}}         
devel         don't fail in NSI (Windows installer generation) when a feature is disabled .. raw:: mediawiki to be tested and proposed
                                                                                                            
                                                                                             {{ok}}         
doc           update `OSXCompile <OSXCompile>`__ page (from discuss at least)             maybe won't do    
devel         compile for MacOS X                                                         maybe won't do    
documentation webplugin HTML params                                                       .. raw:: mediawiki
                                                                                                            
                                                                                             {{no}}         
priv          Understand fetch, pull, merge, branch under Git                             .. raw:: mediawiki
                                                                                                            
                                                                                             {{ok}}         
feature       enable fullscreen control on web plugins                                    .. raw:: mediawiki
                                                                                                            
                                                                                             {{no}}         
feature       allow hiding control toolbar (for mozplug X11)                              .. raw:: mediawiki
                                                                                                            
                                                                                             {{ok}}         
test          Test activeX API                                                            .. raw:: mediawiki
                                                                                                            
                                                                                             {{partial}}    
test          Test mozplug API                                                            .. raw:: mediawiki
                                                                                                            
                                                                                             {{Partial}}    
test          List APIs for ActiveX                                                       .. raw:: mediawiki
                                                                                                            
                                                                                             {{no}}         
test          List APIs for mozplug                                                       .. raw:: mediawiki
                                                                                                            
                                                                                             {{Ok}}         
devel         Suscrib to the MailingList and the Wiki (create account...)                 .. raw:: mediawiki
                                                                                                            
                                                                                             {{yes}}        
devel         Suscrib to the Google group (vlc-mozplug-friends)                           .. raw:: mediawiki
                                                                                                            
                                                                                             {{yes}}        
devel         Go to the IRC channel (#videolan)                                           .. raw:: mediawiki
                                                                                                            
                                                                                             {{yes}}        
devel         Build the latest git version of VLC (0.9) (windows & debian Etch)           .. raw:: mediawiki
                                                                                                            
                                                                                             {{yes}}        
============= =========================================================================== ================== ===========================================

clipboard/reminder
------------------

public clipboard
~~~~~~~~~~~~~~~~

*Feel free to past some links you seems interesting for me.*

'' not yet seen :''

--------------

*seen :*

private clipboard
~~~~~~~~~~~~~~~~~

-  irc, to avoid sec policy --security-policy=1

-  `HowTo_Integrate_VLC_plugin_in_your_webpage <HowTo_Integrate_VLC_plugin_in_your_webpage>`__
-  `Documentation:Play_HowTo/Advanced_Use_of_VLC#The_Mozilla_plugin <Documentation:Play_HowTo/Advanced_Use_of_VLC#The_Mozilla_plugin>`__

| ``./include/vlc_messages.h:148:#define msg_Dbg( p_this, ... ) \``
| ``msg_Dbg( p_libvlc, COPYRIGHT_MESSAGE );``
| ``msg_Dbg( p_libvlc, "libvlc was configured with %s", CONFIGURE_LINE );``
| ``msg_Info( p_this, ... )``
| ``msg_Err( p_this, ... )``
| ``msg_Warn( p_this, ... )``
| ``msg_Dbg( p_this, ... )``

ideas
-----

Isn't madness the origin of our lives?

-  **bash completion** config for VLC command line :p

   -  something exists in extra/ for zsh completion.
   -  begin from a docbok to generate a man page t

-  stable **unit-tests for web plugins** (Javascript?) usable in command-line *(doesn't have the "how" yet in mind)*
-  environment to help using **automated git bissect**, "pluggable" to webplugins unit-test CLI *(wahoo yeah, dreaming :) )*
-  (low) **split file sout** parameter (roll files with an index and a max time/size for each chunk)
-  on mozplug X11, conditional embedded controls (play, pause, ..): done, optionnal now.
