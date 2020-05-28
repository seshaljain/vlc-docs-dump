.. raw:: mediawiki

   {{Module|name=h26x|type=Access demux|description=Raw [[H264]] and [[HEVC]] Video demuxers}}

The `H.265 <H.265>`__ video demuxer is a sub-module.

The H264 video demuxer has a shortcut of ``h264`` and the HEVC/H.265 video demuxer has shortcuts of ``hevc`` and ``h265``.

Options
-------

H264 video demuxer
~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=h264-fps
   |value=float
   |default=0.0f
   |description=Desired [[frame rate]] for the stream
   }}

HEVC/H.265 video demuxer
~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=hevc-fps
   |value=float
   |default=0.0f
   |description=Desired frame rate for the stream
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/mpeg/h26x.c}}

.. raw:: mediawiki

   {{Documentation footer}}
