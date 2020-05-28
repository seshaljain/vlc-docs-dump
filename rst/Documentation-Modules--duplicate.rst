.. raw:: mediawiki

   {{Module|name=stream_out_duplicate|type=Stream output|first_version=1.1.0|description=Duplicate stream output|sc=duplicate|sc2=dup}}

Options
-------

None.

Examples
--------

From the changelog: ``--sout "#duplicate{dst=transcode{vcodec=mp2v},select=es=0,dst=transcode,select=es=1}:std{...}"``

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/stream_out/duplicate.c}}

.. raw:: mediawiki

   {{Documentation}}
