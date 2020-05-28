\__NOTOC_\_

Options
-------

Access Demux
~~~~~~~~~~~~

.. raw:: mediawiki

   {{Module|name=fake|type=Access demux|last_version=0.9.0|description=simulate a fake input|sc=fake}}

.. raw:: mediawiki

   {{Option
   |name=fake-caching
   |value=integer
   |default=<code><var>DEFAULT_PTS_DELAY</var>/1000</code>
   |description=Caching in [[wiktionary:ms|milliseconds]]
   }}

.. raw:: mediawiki

   {{Option
   |name=fake-fps
   |value=float
   |default=25.0
   |description=[[Framerate]] e.g. 24, 25, 29.97, 30
   }}

.. raw:: mediawiki

   {{Option
   |name=fake-id
   |value=integer
   |default=0
   |description=Set the ID of the fake [[elementary stream]] for use in <samp>#{{docmod|duplicate}}{}</samp> constructs
   }}

.. raw:: mediawiki

   {{Option
   |name=fake-duration
   |value=integer
   |default=0
   |description=Duration of the fake streaming (in milliseconds) before faking an end-of-file (default is 0, meaning that the stream is unlimited)
   }}

.. raw:: mediawiki

   {{Clear|right}}

Codec
~~~~~

.. raw:: mediawiki

   {{Module|name=fake|type=Codec|last_version=0.9.0|description=handle a fake input stream|sc=fake}}

.. raw:: mediawiki

   {{Option
   |name=fake-file
   |value=string
   |default=""
   |description=Image to use as video for the fake stream
   }}

.. raw:: mediawiki

   {{Option
   |name=fake-file-reload
   |value=integer
   |default=0
   |description=Number of seconds between each reload of the image
   }}

.. raw:: mediawiki

   {{Option
   |name=fake-width
   |value=integer
   |default=0
   |description=Width
   }}

.. raw:: mediawiki

   {{Option
   |name=fake-height
   |value=integer
   |default=0
   |description=Height
   }}

.. raw:: mediawiki

   {{Option
   |name=fake-keep-ar
   |value=boolean
   |default=disabled
   |description=Keep [[aspect ratio]] when resizing
   }}

.. raw:: mediawiki

   {{Option
   |name=fake-aspect-ratio
   |value=string
   |default=""
   |description=Aspect ratio of the image file (4:3, 16:9). Default is square pixels
   }}

.. raw:: mediawiki

   {{Option
   |name=fake-deinterlace
   |value=boolean
   |default=disabled
   |description=[[Deinterlace]] the image after loading it
   }}

.. raw:: mediawiki

   {{Option
   |name=fake-deinterlace-module
   |value=string
   |default="deinterlace"
   |description=Deinterlace module
   }}

.. raw:: mediawiki

   {{Option
   |name=fake-chroma
   |value=string
   |default="[[I420]]"
   |description=Image [[chroma]]
   }}

Example
-------

``{{$}} ``\ **``vlc``\ ````\ ``fake://``\ ````\ ``--fake-file``\ ````\ ``someimage.png``**

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/fake.c|p=vlc/vlc-0.9.git}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/fake.c|p=vlc/vlc-0.9.git}}

.. raw:: mediawiki

   {{Documentation footer}}
