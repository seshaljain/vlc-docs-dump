.. raw:: mediawiki

   {{See also|M3U}}

This page is from **May 2012**. It is probably out of date.

====================== ============ ===================
http access            vlc git      vlc git + bom patch
====================== ============ ===================
BOM with #EXTM3U       doesnt parse parse ok
BOM without #EXTM3U    doesnt parse doesnt parse
No BOM with #EXTM3U    parse ok     parse ok
No BOM without #EXTM3U doesnt parse doesnt parse
====================== ============ ===================

====================== ======== ===================
file access access     vlc git  vlc git + bom patch
====================== ======== ===================
BOM with #EXTM3U       parse ok parse ok
BOM without #EXTM3U    parse ok parse ok
No BOM with #EXTM3U    parse ok parse ok
No BOM without #EXTM3U parse ok parse ok
====================== ======== ===================

`Category:Dev Discussions <Category:Dev_Discussions>`__
