.. raw:: mediawiki

   {{Historical|This filter has been merged with the [[Documentation:Modules/marq|marq]] filter in version 0.9.0.}}

.. raw:: mediawiki

   {{Module|name=time|type=Video sub-filter|first_version=0.8.0|last_version=0.8.6|description=Overlays date and time on the video|sc=time}}

Allows overlaying date and time information on the video.

Options
-------

The option for the time picture subfilter in version 0.8.6 are the following:

Usage
-----

There are two ways to use the time module: over screen output or display; and over transcoded output.

Screen output or display
~~~~~~~~~~~~~~~~~~~~~~~~

To overlay the current time over vlc screen output or display, use the --time-? options (where ? means "format," "x", "y" etc; i.e. --time-format).

In this example, the time will be displayed in white on the lower right hand corner of the viewable output of a transcoded stream and sent to a multicast IP address with the associated SAP announce.

``% ``\ **``vlc``\ ````\ ``input_stream``\ ````\ ``--sub-filter=time``\ ````\ ``--time-format``\ ````\ ``%Y-%m-%d,%H:%M:%S``\ ````\ ``--time-position``\ ````\ ``9``\ ````\ ``--time-color``\ ````\ ``16777215``\ ````\ ``--time-size``\ ````\ ``12``\ ````\ ``--sout``\ ````\ ``"#transcode{venc=ffmpeg,vcodec=mp4v}:duplicate{dst=display,dst=rtp{mux=ts,dst=239.255.12.42,sdp=sap,name="TestStream"}}"``**

In this example, the time will be displayed as 2007-6-19,10:09:33. In addition, the time will only be displayed on the visual display of the input_stream. It will not be part of the transcoded output.

Transcoded output
~~~~~~~~~~~~~~~~~

To overlay the current time over the transcoded output, enable the transcode module subpicture filter or sfilter option.

In this example, the time will be displayed in white on the lower right only in the transcoded output.

``% ``\ **``vlc``\ ````\ ``input_stream``\ ````\ ``--time-format``\ ````\ ``%Y-%m-%d,%H:%M:%S``\ ````\ ``--time-position``\ ````\ ``9``\ ````\ ``--time-color``\ ````\ ``16777215``\ ````\ ``--time-size``\ ````\ ``12``\ ````\ ``--sout``\ ````\ ``"#transcode{venc=ffmpeg,vcodec=mp4v,sfilter=time}:duplicate{dst=display,dst=rtp{mux=ts,dst=239.255.12.42,sdp=sap,name="TestStream"}}"``**

Note that this is accomplished by removing the --sub-filter=time command line option and adding the sfilter transcode module option. If the --sub-filter=time is included vlc will overlay the time over the overlay transcode time, essentially overlapping it.

Also note that the --time-? command line options are "global;" i.e., they affect the way the time overlays both the display and the transcoded output.

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|p=vlc/vlc-0.8.git|modules/video_filter/time.c}}

Appendix
--------

.. raw:: html

   <div class="plainlist">

-  ^ --`time-position <#time-position>`__\ 
-  ^ --`time-color <#time-color>`__\ 

.. raw:: html

   </div>

.. raw:: mediawiki

   {{Alignment mapping}}

.. table:: Colour key

   ====== ============== =======
   Sample Integer code   Colour
   ====== ============== =======
   \      ``-268435456`` Default
   \      ``0``          Black
   \      ``8421504``    Gray
   \      ``12632256``   Silver
   \      ``16777215``   White
   \      ``8388608``    Maroon
   \      ``16711680``   Red
   \      ``16711935``   Fuchsia
   \      ``16776960``   Yellow
   \      ``8421376``    Olive
   \      ``32768``      Green
   \      ``32896``      Teal
   \      ``65280``      Lime
   \      ``8388736``    Purple
   \      ``128``        Navy
   \      ``255``        Blue
   \      ``65535``      Aqua
   ====== ============== =======

.. raw:: mediawiki

   {{Documentation}}
