.. raw:: mediawiki

   {{SoCProject|year=2009|student=[[User:ivoire|Rémi Duraffort]]|mentor=[[User:thresh|Pavlov Konstantin]]}}

Abstract
--------

The goal of this Google Summer of Code is to implement two feature that are missing in vlc:

-  visualizations using libprojectM library.
-  p2p access capability

Timeline
--------

========= ==============================================================================
May 26    Begining of the GSoC but work mainly on vlc next release (a lot of bugs fixed)
========= ==============================================================================
June 17   libprojectM module mostly finished, code the p2p access
July 6-12 Mid-term evaluation
August 24 Final evaluation
========= ==============================================================================

Actually
--------

The projectM module is mostly finished and give good results. You can try it (tested only under linux for the moment) from `my git repository <http://git.videolan.org/?p=vlc-ivoire.git>`__ and compiling vlc with the --enable-projectm configure option. You will need libprojectm-dev and an opengl provider module.
