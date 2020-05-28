Roadmap
=======

For more on the concepts (not very formalized) please see `VoutRework <VoutRework>`__

-  Make a SVN branch (0.8.5-vout)
-  Make the vout singleton that manages windows and inputs

   -  Create the singleton
   -  Create the notion of vout_window , vout_region, vout_input. See `VoutRework <VoutRework>`__

-  Make the Great Unified Crop/Pad/AR thing

   -  Core part
   -  Modular part (standard C, or using OS capabilities)

-  Rework SPU Unit

   -  Allow "absolute timing" (OSD) or "stream timing" (subs)
   -  Ability to work at video resolution (DVD Subs) or output resolution (OSD, text subs) (handled in vout)

-  Sort the filters mess
-  Add ability to add "video_filter2" in the chain

-  Add additionnal flags to windows
-  Fix hotkeys so they act on the selected window
-  Fix subtitles

`Category:Dev Discussions <Category:Dev_Discussions>`__
