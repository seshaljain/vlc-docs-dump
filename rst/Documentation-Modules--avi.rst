Demux
-----

.. raw:: mediawiki

   {{Module|name=avi|type=Access demux|description=[[AVI]] demuxer|sc=none}}

.. raw:: mediawiki

   {{Option
   |name=avi-interleaved
   |value=boolean
   |default=disabled
   |description=Force interleaved method
   }}

.. raw:: mediawiki

   {{Option
   |name=avi-index
   |value=integer
   |default=0
   |select={0,1,2,3}
   |description=Recreate a index for the AVI file. Use this if your AVI file is damaged or incomplete (not seekable). 0 ("Ask for action"), 1 ("Always fix"), 2 ("Never fix"), 3 ("Fix when necessary")
   }}

.. raw:: mediawiki

   {{Clear}}

Mux
---

.. raw:: mediawiki

   {{Module|name=avi|type=Muxer|description=[[AVI]] muxer|sc=avi}}

.. raw:: mediawiki

   {{Option
   |name=sout-avi-artist
   |value=string
   |default=NULL
   |description=Artist
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-avi-date
   |value=string
   |default=NULL
   |description=Date
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-avi-genre
   |value=string
   |default=NULL
   |description=Genre
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-avi-copyright
   |value=string
   |default=NULL
   |description=Copyright
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-avi-comment
   |value=string
   |default=NULL
   |description=Comment
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-avi-name
   |value=string
   |default=NULL
   |description=Name
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-avi-subject
   |value=string
   |default=NULL
   |description=Subject
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-avi-encoder
   |value=string
   |default="VLC Media Player - " <var>VERSION_MESSAGE</var>
   |description=Encoder
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-avi-keywords
   |value=string
   |default=NULL
   |description=Keywords
   }}

.. raw:: mediawiki

   {{Clear}}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/avi/avi.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/mux/avi.c}}

-  

   .. raw:: mediawiki

      {{VLCSourceFolder|modules/demux/avi}}

.. raw:: mediawiki

   {{Documentation}}
