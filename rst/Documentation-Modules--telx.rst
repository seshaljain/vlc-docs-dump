.. raw:: mediawiki

   {{Module|name=telx|type=Access demux|first_version=0.8.6b|description=Teletext [[subtitles]] decoder|sc=none}}

Options
-------

.. raw:: mediawiki

   {{Option
   |name=telx-override-page
   |value=integer
   |default=-1
   |description=Override the indicated page, try this if your subtitles don't appear (-1 = autodetect from TS, 0 = autodetect from teletext, >0 = actual page number, usually 888 or 889)
   }}

.. raw:: mediawiki

   {{Option
   |name=telx-ignore-subtitle-flag
   |value=boolean
   |default=disabled
   |description=Ignore the subtitle flag, try this if your subtitles don't appear
   }}

.. raw:: mediawiki

   {{Option
   |name=telx-french-workaround
   |value=boolean
   |default=disabled
   |description=Some French channels do not flag their subtitling pages correctly due to a historical interpretation mistake. Try using this wrong interpretation if your subtitles don't appear
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/telx.c}}

.. raw:: mediawiki

   {{Documentation footer}}
