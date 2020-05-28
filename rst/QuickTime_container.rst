.. raw:: mediawiki

   {{Mux|id=mov|mod=mp4|encoder=y|altid=mov|altid2=3gp}}

.. raw:: mediawiki

   {{Wikipedia|QuickTime File Format}}

.. raw:: mediawiki

   {{Mmwiki|QuickTime container}}

`QuickTime <QuickTime>`__ natively uses this container (`described <https://developer.apple.com/standards/classic-quicktime/>`__ as *QuickTime File Format* by Apple), which can store other data, including video, audio and text. The advantage of this container format is the separation of data from metadata: writes to metadata do not necessitate a re-write of the entire media file. QuickTime video files have the extension .mov (presumably for movie) or .qt (presumably for QuickTime).

The QuickTime container was made into a standard "ISO base media file format", the basis for `MPEG-4 <MPEG-4>`__ (part 14) and `3GP <3GP>`__.

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/mux/mp4/mp4.c}}

   (MOV/MP4 muxer)
