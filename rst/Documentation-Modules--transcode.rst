.. raw:: mediawiki

   {{Stub}}

.. raw:: mediawiki

   {{Module|name=stream_out_transcode|type=Stream output|first_version=0.6.0|description=[[Transcode]] content on the fly}}

The only shortcut to this module is ``transcode``.

Options
-------

Note: Since `supported <supported>`__ codecs are dynamically assigned by the running program, ``sout-transcode-venc``, ``sout-transcode-aenc`` and ``sout-transcode-senc`` have been left blank.

Looking at the source code for 4.0.0-dev it seems no checks are directly performed limiting ``sout-transcode-samplerate`` beyond ``0 <= samplerate <= 48000``.

As of 2.2.0 ``sout-transcode-fps`` accepts fps as rationals e.g. ``30000/1001``.

Deprecated options:

-  ``hurry-up`` (since 2.2.0), ``sout-transcode-high-priority`` seems to be equivalent
-  ``audio-sync`` (since 2.2.0)

Video
~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-venc
   |value=string
   |select=
   |description=This is the video encoder module that will be used (and its associated options)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-vcodec
   |value=string
   |default=NULL
   |description=This is the video codec that will be used
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-vb
   |value=integer
   |default=0
   |description=Target bitrate of the transcoded video stream
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-scale
   |value=float
   |default=0
   |description=Scale factor to apply to the video while transcoding (eg: 0.25)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-fps
   |value=string
   |default=NULL
   |description=Target output frame rate for the video stream
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-deinterlace
   |value=boolean
   |description=Deinterlace the video before encoding
   |default=disabled
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-deinterlace-module
   |value=string
   |default=deinterlace
   |select={deinterlace,ffmpeg-deinterlace}
   |description=Specify the deinterlace module to use
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-width
   |value=integer
   |default=0
   |description=Output video width
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-height
   |value=integer
   |default=0
   |description=Output video height
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-maxwidth
   |value=integer
   |default=0
   |description=Maximum output video width
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-maxheight
   |value=integer
   |default=0
   |description=Maximum output video height
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-vfilter
   |value=string
   |description=Video filters will be applied to the video streams (after overlays are applied). You can enter a colon-separated list of filters
   }}

Audio
~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-aenc
   |value=string
   |select=
   |description=This is the audio encoder module that will be used (and its associated options)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-acodec
   |value=string
   |default=NULL
   |description=This is the audio codec that will be used
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-ab
   |value=integer
   |default=96
   |description=Target bitrate of the transcoded audio stream
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-alang
   |value=string
   |default=NULL
   |description=This is the language of the audio stream
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-channels
   |value=integer
   |default=0
   |min=0
   |max=9
   |description=Number of audio channels in the transcoded streams
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-samplerate
   |value=integer
   |default=0
   |min=0
   |max=48000
   |description=Sample rate of the transcoded audio stream (11250, 22500, 44100 or 48000)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-afilter
   |value=string
   |description=Audio filters will be applied to the audio streams (after conversion filters are applied). You can enter a colon-separated list of filters
   }}

Overlays/Subtitles
~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-senc
   |value=string
   |select=
   |description=This is the subtitle encoder module that will be used (and its associated options)
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-scodec
   |value=string
   |default=NULL
   |description=This is the subtitle codec that will be used
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-soverlay
   |value=boolean
   |default=disabled
   |description=This is the subtitle codec that will be used
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-sfilter
   |value=string
   |description=This allows you to add overlays (also known as "subpictures") on the transcoded video stream. The subpictures produced by the filters will be overlayed directly onto the video. You can specify a colon-separated list of subpicture modules
   }}

Miscellaneous
~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-threads
   |value=integer
   |default=0
   |min=1
   |max=32
   |description=Number of threads used for the transcoding
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-pool-size
   |value=integer
   |default=10
   |min=1
   |max=1000
   |description=Defines how many pictures we allow to be in pool between decoder/encoder threads when threads > 0
   }}

.. raw:: mediawiki

   {{Option
   |name=sout-transcode-high-priority
   |default=disabled
   |value=boolean
   |description=Runs the optional encoder thread at the OUTPUT priority instead of VIDEO
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/stream_out/transcode/transcode.c}}

.. raw:: mediawiki

   {{Documentation}}

`Category:Transcoding <Category:Transcoding>`__
