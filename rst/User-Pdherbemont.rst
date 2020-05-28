(Pdherbemont is Pierre d'Herbemont)

I am currently working on a `Mac OS X VLC Framework <SoC_2007_Project_Mac_OS_X_Framework>`__ for Google Summer of Code 2007.

Random Thoughts
===============

VLC.app proposition
-------------------

The problem
~~~~~~~~~~~

The problem with current implementation of VLC.app and gui/macosx is that it relays on the src/vlc.c common file that set up the interface. This permit to use vlc command line and do cool vlc thing with it. However there are many troubles with gui/macosx:

-  It can't be detached, nor can be attached on the fly. Thus we **can't really say that gui/macosx is a vlc interface module**.
-  There is a technical conflict with Cocoa:

| `` Run()``
| `` {``
| ``     [NSApp run]; /* May not exit however vlc will cleanly ends only if gui/macosx Run() ends, so this won't work */``
| `` }``

We do:

| `` Run()``
| `` {``
| ``     if(setjmp(jmpbuff) == 0)``
| ``         [NSApp run]; /* May not exit */``
| ``     /* Will exit when longjmp(jmpbuff, 1) is called, then vlc will cleanly ends */``
| `` }``

Which is kind of ugly.

Proposed solution
~~~~~~~~~~~~~~~~~

gui/macosx shouldn't be a module interface but instead we should create a new Cocoa application (named here VLCOSX) that links to libvlc. However src/vlc.c would be still be build (named here vlc), and we'll have in the VLC.app bundle the two binary VLCOSX and vlc. VLCOSX would start the Cocoa application whereas vlc would be the real vlc that we can use with command line. VLCOSX could still be hacked to forward vlc option to libvlc, but this is really not is goal.

libvlc advanced configuration processing proposition
----------------------------------------------------

.. _the-problem-1:

The problem
~~~~~~~~~~~

Currently the configuration variable are accessible from the libvlc outside by p_main_module->p_config[item_element]. But p_config (a (config_t \*) ) is a tree in list, that makes it hard to process, especially to build the advanced preferences panel.

.. _proposed-solution-1:

Proposed solution
~~~~~~~~~~~~~~~~~

-  Make config_t a tree node.
-  Add the needed function to process the p_main_module->p_config list

Mac OS X Simple pref proposition
--------------------------------

-  Fullscreen

   -  Display video on screen:

      -  Window screen
      -  Screen 1
      -  Screen 2
      -  ...

   -  Crop video to screen size
   -  Make other screen black in fullscreen

-  Sharing

   -  Enable sharing (enable SAP and Bonjour sharing)
   -  Look for shared playlist (enable SAP and Bonjour service discovery)

-  Subtitle

   -  Color
   -  Size
   -  Effect
