.. raw:: mediawiki

   {{SoCProject|year=2011|student=[[User:skelet|Casian Andrei]]|mentor=[[User:etix|Ludovic Fauvet]]}}

Abstract
--------

A nice looking, intuitive, effect-oriented OpenGL interface for the VLC Media Player. It should combine the utility of the current Qt interface with the graphics of media centers. OpenGL will be used for all rendering operations for the interface, bringing a wide range of possibilities to develop pretty graphics. All the user interface elements will be specialized according to the needs of the VLC interface.

Progress
--------

======================================================================== ========
Task                                                                     Progress
======================================================================== ========
Establish a primitive working interface module.                          Done
Create a basic OpenGL "engine" for the interface.                        Done
Additional planning and design                                           Done
Work on the layout system.                                               Done
Develop basic widgets and basic input                                    Done
Basic play functionality (primitive playlist)                            Done
Selector / navigation, media library                                     Done
More work on the media library + playlist view (current item, tree view) Done
Ensure scrolling around the playlist without problems                    Done
Open media dialogs, use a dialog provider                                Done
Text rendering using a VLC text renderer module                          Done
Play video, ensure layout transitions work smoothly                      Done
Implement basic effects for everything                                   Done
Improve playlist item, add details                                       Planned
Add more effects as much as possible                                     No time
Nice play button, volume slider, stop, next, prev buttons                Done
Further improvements on the playlist, display more meta-data             Planned
Lirc input                                                               Planned
Extra buttons, improve media library                                     Planned
Fullscreen mode and search / filter                                      Planned
Implement missing features and general improvements                      Done
======================================================================== ========

Planning and Design
-------------------

The interface has 3 main parts - user input, GUI (widgets in OpenGL), functionality (interaction with VLC).

User -> user input -> GUI <-> VLC

User <- GUI <-> VLC

For video, a vout display submodule is provided. It uses helpers from vout display opengl. But all the drawing must be done by the run thread, the one with the OpenGL context. It looks like it works okay, but there are some problems with it's responsiveness on display requests - needs to be improved.

Classes
~~~~~~~

Main:

-  GLIntf (module code, create main things) (not a class, it's like C code)
-  MainInterface (centralizes the others, issues drawing and updates)

User Input:

-  UserInputMonitor (handles input from multiple possible sources)
-  AbstractUserInput (base class for an input type)
-  SDLUserInput (input from SDL events - touch / mouse, keys)
-  LircInput (buttons from remote control) - planned

Widgets:

-  Widget (base class for every widget)
-  Layout (sets positions, sizes of multiple widgets)
-  DynamicLayout (layout that can transition smoothly)
-  Container (a widget that can contain other widgets and has a layout)
-  ScrollableContainer (a container with scrolling possibilities)
-  ScrollBar
-  PlaylistBrowser (the playlist)
-  PlaylistItem (an item from the playlist)
-  SelectorPanel (choose Media Library, Internet, etc.)
-  SelectorItem (item for selecting media sources ^)
-  Button (base class for a button)
-  Label (draws text)
-  MenuPanel
-  PlayPanel
-  PlayButton, VolumeWidget, StopButton, PrevButton, NextButton
-  SeekSlider
-  VideoWidget ("holds" the video)
-  FilterEdit - planned

Functionality:

-  PlaylistManager (like MainInputManager from Qt interface)
-  InputManager (like InputManager from Qt interface)
-  Dialogs (to handle showing dialogs using a dialog provider)

Effects:

-  AbstractEffect (a generic effect)
-  LinTransitionEffect
-  ExpTransitionEffect
-  ColorTransitionEffect

Other:

-  TextCache
-  TexPicture
-  EventQueue

GUI Sketches
~~~~~~~~~~~~

-  `Normal layout, nothing special. Large playlist items <http://img13.imageshack.us/img13/2203/glvlc.png>`__
-  `Video playing layout <http://img218.imageshack.us/img218/774/glvlcvideo.png>`__
-  `Fullscreen layout <http://img35.imageshack.us/img35/6305/glvlcvideofull.png>`__
-  `Normal layout, small items <http://img35.imageshack.us/img35/6703/glvlcscale.png>`__

Screenshots
~~~~~~~~~~~

-  `Basic media library view <http://img812.imageshack.us/img812/9286/glintf1.png>`__

Repository
----------

Repo
~~~~

http://git.videolan.org/?p=vlc/vlc-skelet.git;a=summary

git://git.videolan.org/vlc/vlc-skelet.git

Backup Repo
~~~~~~~~~~~

git://repo.or.cz/vlc/vlc-skelet.git

http://repo.or.cz/r/vlc/vlc-skelet.git

Contact
-------

You can reach me at skeletk13 at gmail or as skelet on IRC. Any suggestions are welcome.
