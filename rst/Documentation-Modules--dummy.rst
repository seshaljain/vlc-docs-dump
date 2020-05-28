`Dummy <Dummy>`__ modules are the VLC equivalent of ``/dev/null`` on GNU/Linux: they represent doing nothing.

List
----

.. table:: Overview of dummy modules

   =================================== =========================== ==============
   Type                                Description                 Shortcut(s)
   =================================== =========================== ==============
   Access                              Dummy input                 dummy, vlc
   Access output                       Dummy stream output         dummy
   Audio output                        Dummy audio output          dummy
   Decoder                             Dummy decoder               dummy, dump
   Encoder                             Dummy encoder               dummy
   Control interface                   Dummy interface             (none)
   Muxer                               Dummy/\ `Raw <Raw>`__ muxer dummy, raw, es
   Stream output                       Dummy stream output         dummy, drop
   Text renderer                       Dummy font renderer         (none)
   Video output                        Dummy video output          dummy, stats
   Video output (legacy video plugins) Dummy window                dummy
   =================================== =========================== ==============

Descriptions
------------

Interface
~~~~~~~~~

A dummy interface works well with `command-line <command-line>`__ usage. It consumes fewer computing resources, something that can be used to reduce a bottleneck effect during `transcoding <transcoding>`__, or simply when opening a window makes little sense.

This will play an `Ogg <Ogg>`__ file with no interface:

``{{$}} vlc -I dummy audio.ogg vlc://quit``

No window is launched, and control is returned to the calling application after the file plays.

This will play a `Schroedinger <Schroedinger>`__ file with a minimalist interface:

``{{$}} vlc -I dummy video.drc vlc://quit``

A window with no buttons or toolbars is launched (no `skin <skin>`__), because `video output <video_output>`__ requires a window. `Hotkeys <Hotkey>`__ may be used to control playback by default, something that can be disabled if necessary with ``--no-keyboard-events``.

Stream output
~~~~~~~~~~~~~

Doesn't do anything. Can be used to test other stream output chain modules without actually streaming anything.

Options
-------

Dummy decoder
~~~~~~~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=dummy-save-es
   |value=boolean
   |default=disabled
   |description=Save the raw [[codec]] data if you have selected/forced the dummy decoder in the main options.
   }}

Video output
~~~~~~~~~~~~

.. raw:: mediawiki

   {{Option
   |name=dummy-chroma
   |value=string
   |default=NULL
   |description=Force the dummy video output to create images using a specific [[chroma]] format instead of trying to improve performances by using the most efficient one.
   }}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access/idummy.c|Access}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/access_output/dummy.c|Access output}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/audio_output/adummy.c|Audio output}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/ddummy.c|Decoder}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/edummy.c|Encoder}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/control/dummy.c|Interface}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/mux/dummy.c|Output muxer}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/stream_out/dummy.c|Stream output}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/text_renderer/tdummy.c|Text rendering}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/video_output/vdummy.c|Video output}}

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/video_output/wdummy.c|Video output for legacy video plugins}}

.. raw:: mediawiki

   {{Documentation}}

`Category:Accesses <Category:Accesses>`__ `Category:Access output <Category:Access_output>`__ `Category:Audio output <Category:Audio_output>`__ `Category:Codecs <Category:Codecs>`__ `Category:Interfaces <Category:Interfaces>`__ `Category:Control VLC <Category:Control_VLC>`__ `Category:Muxers <Category:Muxers>`__ `Category:Stream output <Category:Stream_output>`__ `Category:Video output <Category:Video_output>`__ `Category:Video output <Category:Video_output>`__
