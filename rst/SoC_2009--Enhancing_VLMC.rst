.. raw:: mediawiki

   {{SoCProject|year=2009|student=[[User:chouquette|Hugo Beauzee-Luyssen]]|mentor=[[User:etix|Ludovic Fauvet]]}}

Enhancing VLMC
==============

Abstract
--------

The aim of this project is to provide a functionnal workflow for the VLMC project, including the transition and effects API, in order to allow external developpers to create new effects. At the moment, VLMC isn't abble to generate a video output. After this summer, it (hopefully) will :)

The workflow consists of 5 differents workflows :

-  The main workflow
-  The clip workflow
-  The track workflow
-  The effects workflow
-  The transition workflow

Basically, the main workflow will query the track workflow, which will query the clip workflow for each clip contained in the so called track. Transitions and effect workflow will query transition and effects modules at different points, from the precedently described workflows.

Tasks
-----

========================= ======== ===================================================================================== ==============================================
Task name                 End date Dependencies                                                                          Status
========================= ======== ===================================================================================== ==============================================
Clip workflow             06-06-09 Requires a functional preview widget, and a basic timeline                            Completed
Tracks workflow           13-06-09 Requires a functionnal Clip workflow                                                  Completed (Without track editing capabilities)
Main workflow             04-07-09 Requires a functionnal Track workflow                                                 Completed
Effect and Transition API 25-07-09 Requires lots of conception :p                                                        Not started yet
Effect workflow           01-08-09 Requires all the basic workflow to be functionnal, and an effect API to query modules Not started yet
Transition workflow       09-09-09 Requires all the basic workflow to be functionnal, and the transition API             Not started yet
\                                                                                                                       
========================= ======== ===================================================================================== ==============================================

Timeline
--------

**May 26** Here we go !

**June 06** Functionnal clip workflow

**June 13** Functionnal track workflow

**June 19** Some small vacation

**July 01** Let's get back coding !

**July 04** Main workflow

Having a look at the code efficiency would be good. At this point, real time is almost mandatory.

**July 07** Mid term evaluation

**July 25** Effect and transition API

**August 01** Functionnal effect workflow

**August 08** Functionnal transition workflow

**August 11** Check code, write doc, beeing nervous if work isn't done.

**August 18** Keyboard pencil down :(

**August 18/19** Let's party o//

Contact
-------

I blog `websitidae.fr here <http://www.mustelVLMC>`__ and you can contact me at beauze.h@gmail.com :)

Repository
----------

You can find the VLMC Git repository `here <http://github.com/VLMC/vlmc/tree/master>`__

Website
-------

For more informations, please visit the official `VLMC website <http://vlmc.org>`__.

Resources: Building VLMC
------------------------

For information on building VLMC from source visit: `Building VLMC from Source <http://wiki.videolan.org/Building_VLMC>`__
