.. raw:: mediawiki

   {{Outdated}}

Introduction
------------

Qt / Qt4 is the default, plain, graphical, `interface <interface>`__ to VLC, made using the `Qt <https://www.qt.io>`__ library (Linux users may need to have this installed). It is used as the default interface on the `Windows <Windows>`__ and `Linux <Linux>`__ versions of from version 0.9.0 and above.

Unless you change the `preferences <preferences>`__, VLC will start up in the Qt4 interface, but you can force this by running

``{{%}} vlc ``\ **``-I``\ ````\ ``qt``**

or

``% qvlc``

If Qt4 is not avaliable, it will probably revert to using the `rc <Console>`__ (console) interface, even if you force it. The most likely reason for this is if Qt4 hasn't been installed, or if it wasn't linked in (using the ./configure). See `compiling VLC <compiling_VLC>`__ for information on compiling.

Please note that the pre-0.9.0 `wxWidgets <wxWidgets>`__ interface is replaced by the Qt interface and will thus not be further developed.

Using
-----

Launching Modes
~~~~~~~~~~~~~~~

Video Modes
~~~~~~~~~~~

Other options
~~~~~~~~~~~~~

Main interface Description
--------------------------

Menu Bar
~~~~~~~~

Status Bar
~~~~~~~~~~

The Status Bar has three distinctive portions displaying information.

-  Name label
-  Speed label
-  Time label

Here are the actions you can do on the status bar:

=========== ================ =============================== ============================== ============================= ============================
\           Select           Left Click                      Right Click                    Middle Click                  Double Click
=========== ================ =============================== ============================== ============================= ============================
Name label  Prepare for copy Give focus for arrows selection Copy menu                      -                             Word selection
Speed label -                -                               Show fine rate speed adjusting -                             reset to normal 1.00x speed
Time label  -                Switch remaining/elapsed time   Switch remaining/elapsed time  Switch remaining/elapsed time Open the "Go To Time" dialog
=========== ================ =============================== ============================== ============================= ============================

Time label
^^^^^^^^^^

The timeLabel shows mm:ss/nn:tt in the statusBar.

If the time is longer that one hour, it shows hh:mm:ss/ii:nn:tt.

If you click on it, it shows remaining time instead of elapsed time. If you double click on it, it opens the open the GOTOTime dialog in order to skip easily.

If VLC doesn't know the total time, like in `AVI <AVI>`__/`HTTP <HTTP>`__, it shows the elapsed time only, and --:-- instead of total time.

System Tray Icon
~~~~~~~~~~~~~~~~

Controller
~~~~~~~~~~

Main Slider
^^^^^^^^^^^

The main slider does control the timeline.

When you click somewhere on the timeline, it skips the movie to that place. When you drag the slider of the timeline, it follows the position on the movie.

When you hover it with your mouse, it shows you where it would go if you click.

Sound Slider
^^^^^^^^^^^^

The sound slider does control the volume.

When you click somewhere on the soundSlider, it changes the volume. When you click and drag on the soundSlider, it changes the volume too. If you release the click really outside of the volume slider, it will reset to your old value.

When you hover it with your mouse, it shows you the volume it would be if you click it.

Sound range
^^^^^^^^^^^

The sound goes from 0% to 125% (previously the sound went from 0% to 200% and could go up to 400%).

100% means normal output of the file without amplification. Above 100% means that it may use software amplification, and it could distort sound (it usually doesn't, but it could).

Video Widget
~~~~~~~~~~~~

Background Widget
~~~~~~~~~~~~~~~~~

Playlist
--------

The `playlist <playlist>`__ display has three views, the Icon view, the Detailed view, and the List view. The view can be changed by clicking on the icon above the playlist window.

The playlist can be cleared or re-sorted by right-clicking on the background of the display pane. It's also possible to change the size of the display from this menu.

Dialogs description
-------------------

Open Dialog
~~~~~~~~~~~

Sout Dialog
~~~~~~~~~~~

Extended Dialog
~~~~~~~~~~~~~~~

The Extended settings dialog box can be brought up by selected the *Ex* button on the main window. Alternatively it can be found in *Tools* menu under *Extended settings...* (Ctrl+E). The extended settings allow effects to be enabled and adjusted in realtime whilst media is playing.

Audio Effects
^^^^^^^^^^^^^

Graphic Equalizer
'''''''''''''''''

The Graphic equalizer enables the equalization of the sound output to be enabled and adjusted. Tick the *Enable* tickbox to enable it. Ticking the *2 pass* will mean the sound is reprocessed through the equalizer again, thus amplifying the changes. Slide the sliders to adjust the output levels for the preamp and each frequency range. There are a number of presets which can be selected from the drop-down box.

Spatializer
'''''''''''

The Spatializer contains several adjustable audio filters to change the perceived environment such as room size and humidity. Tick the *Enable spatializer* tickbox to enable and adjust the sliders.

Video Effects
^^^^^^^^^^^^^

Basic
'''''

Color fun
'''''''''

Some random name
''''''''''''''''

Image modification
''''''''''''''''''

Find a name
'''''''''''

Overlay
'''''''

Advanced video filter controls
''''''''''''''''''''''''''''''

A colon separated list will be generated when filters and effects in the other video tabs are enabled. The list of effect can be modified. Press the *Update* button to apply the changes.

VLM Dialog
~~~~~~~~~~

Interface Hotkeys
-----------------

`Qt Interface Hotkeys <QtHotkeys>`__

Work
----

`QtIntfTODO <QtIntfTODO>`__

`Category:Interfaces <Category:Interfaces>`__ `Category:Qt <Category:Qt>`__
