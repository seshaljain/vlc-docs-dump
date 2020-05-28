.. raw:: mediawiki

   {{Module|name=subtitle|type=Access demux|description=Text [[subtitle]] parser|sc=subtitle}}

Option ``sub-delay`` was removed in and option ``sub-fps`` was removed in . They are now in `libVLC <libVLC>`__.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=sub-type
   |value=string
   |select={ auto, microdvd, subrip, subviewer, ssa1, ssa2-4, ass, vplayer, sami, dvdsubtitle, mpl2, aqt, pjs, mpsub, jacosub, psb, realtext, dks, subviewer1, sbv }
   |default=auto
   |description=Force the subtiles format. Selecting "auto" means autodetection and should always work
   }}

.. raw:: mediawiki

   {{Option
   |name=sub-description
   |value=string
   |default=NULL
   |description=Override the default track description
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/subtitle.c}}

.. raw:: mediawiki

   {{Documentation}}

`Category:Subtitles <Category:Subtitles>`__
