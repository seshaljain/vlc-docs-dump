.. raw:: mediawiki

   {{Back to|Hacker Guide}}

This page lists the directories in the `source tree of VLC <https://git.videolan.org/?p=vlc.git;a=tree>`__ to give an overview of the code. Because VLC has evolved with not so much accumulation in mind, when a new coder looks at the code, s/he is terrified by the abundance of directories. This page was prepared to remedy that situation.

The directories are listed in alphabetical order, with an overview of their contents on the right.

============================== ============================================================================================================================================================================================================
Directory Name                 Directory Explanation
============================== ============================================================================================================================================================================================================
bindings                       Java, CIL and Python bindings
.. raw:: mediawiki             for required libraries (contains Makefiles to automatically download and compile (or cross-compile) and patch those). Please first attempt to get the development headers precompiled for your distribution.
                              
   {{VLCSourceFolder|contrib}}
.. raw:: mediawiki             Documentation (not up-to-date)
                              
   {{VLCSourceFolder|doc}}    
.. raw:: mediawiki             `See below <#Contents_of_extras>`__
                              
   {{VLCSourceFolder|extras}} 
.. raw:: mediawiki             Header files for VLC
                              
   {{VLCSourceFolder|include}}
.. raw:: mediawiki             Contains all `LibVLC <LibVLC>`__ control code
                              
   {{VLCSourceFolder|lib}}    
.. raw:: mediawiki             Macro files needed for automake and autoconf
                              
   {{VLCSourceFolder|m4}}     
.. raw:: mediawiki             The most important directory besides src/. *See*\ `{{#rel2abs:../Modules source tree}} <{{#rel2abs:../Modules_source_tree}}>`__\ *.*
                              
   {{VLCSourceFolder|modules}}
.. raw:: mediawiki             i18n (language translation) files
                              
   {{VLCSourceFolder|po}}     
projects                       Projects based on libvlc, Mozilla plugin, ActiveX plugin and `Mac OS X Framework <Mac_OS_X_Framework>`__
.. raw:: mediawiki             icons, scripts to make VLC the default player etc.
                              
   {{VLCSourceFolder|share}}  
.. raw:: mediawiki             The most important directory besides modules/. *See*\ `src source tree <{{#rel2abs:/src}}>`__\ *.*
                              
   {{VLCSourceFolder|src}}    
.. raw:: mediawiki             scripts to see if everything is OK
                              
   {{VLCSourceFolder|test}}   
============================== ============================================================================================================================================================================================================

Contents of extras
------------------

========================================= ===================================================================================================================
.. raw:: mediawiki                        contains some code style editor (vim, emacs) macro and some valgrind suppressions
                                         
   {{VLCSourceFolder|extras/analyser}}   
.. raw:: mediawiki                        contains alternative buildsystems
                                         
   {{VLCSourceFolder|extras/buildsystem}}
extras/deprecated                         contains deprecated files
.. raw:: mediawiki                        contains files that don't fit into any other category
                                         
   {{VLCSourceFolder|extras/misc}}       
.. raw:: mediawiki                        contains distribution specific files such as ipkg, different rpm spec files, win32 and Mac OS X installation files.
                                         
   {{VLCSourceFolder|extras/package}}    
\                                        
========================================= ===================================================================================================================

.. raw:: mediawiki

   {{Hacker Guide}}

`Category:Building <Category:Building>`__
