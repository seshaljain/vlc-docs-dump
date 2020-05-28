.. raw:: mediawiki

   {{Module|name=screen|type=Access|description=screen capture}}

Stream or save a video of your computer screen.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=screen-caching
   |value=integer
   |description=Time in milliseconds
   }}

.. raw:: mediawiki

   {{Option
   |name=screen-fps
   |value=integer
   |default=0
   |description=Capture frames per second
   }}

.. raw:: mediawiki

   {{Option
   |name=screen-fragment-size
   |value=integer
   |default=0
   |description=(Windows only) Optimize the capture by fragmenting the screen in chunks of predefined height (16 might be a good value, and 0 means disabled)
   }}

.. raw:: mediawiki

   {{Option
   |name=screen-top
   |value=integer
   |default=0
   |description=The top edge coordinate of the subscreen. (New in VLC 0.9.0 on x11, New in VLC 1.0.0 on Windows)
   }}

.. raw:: mediawiki

   {{Option
   |name=screen-left
   |value=integer
   |default=0
   |description=The left edge coordinate of the subscreen. (New in VLC 0.9.0 on x11, New in VLC 1.0.0 on Windows)
   }}

.. raw:: mediawiki

   {{Option
   |name=screen-width
   |value=integer
   |default=<full screen width>
   |description=The width of the subscreen. (New in VLC 0.9.0 on x11, New in VLC 1.0.0 on Windows)
   }}

.. raw:: mediawiki

   {{Option
   |name=screen-height
   |value=integer
   |default=<full screen height>
   |description=The height of the subscreen. (New in VLC 0.9.0 on x11, New in VLC 1.0.0 on Windows)
   }}

.. raw:: mediawiki

   {{Option
   |name=screen-follow-mouse, no-screen-follow-mouse
   |default=no-screen-follow-mouse
   |description=Follow the mouse when capturing a subscreen. (New in VLC 0.9.0 on x11, New in VLC 1.0.0 on Windows)
   }}

.. raw:: mediawiki

   {{Option
   |name=screen-mouse-image
   |value=filename
   |default=""
   |description=(Windows only) Mouse pointer image to use. If specified, the pointer will be overlayed on the captured video. (New in VLC 1.0.0)
   }}

**screen-mouse-image notes:** - The registration point is (at least by defualt) at the top left corner of image. - File location is relative to your VLC installation folder

Run...

``% ``\ **``vlc``\ ````\ ``-H``**

...for the definitive options for your version.

Example
-------

Capture a screen:

``% ``\ **``vlc``\ ````\ ``screen://``\ ````\ ``--screen-fps=1``\ ````\ ``--screen-width=100``\ ````\ ``--screen-height=100``**

The screen thus captured is 100x100 pixels in from the top left corner of the active screen.

Show mouse on screen:

``% ``\ **``vlc``\ ````\ ``screen://``\ ````\ ``--screen-fps=30``\ ````\ ``:screen-mouse-image=``\ **\ ```file:///c:/cursorimage.png`` <file:///c:/cursorimage.png>`__

Questions
~~~~~~~~~

How to save? Where is the file saved?

Example of a file save (:file{dst=D:\\savedir.mp4}):

``% ``\ **``vlc``\ ````\ ``screen://``\ ````\ ``:sout=#transcode{vcodec=h264,vb=0,scale=0,acodec=mpga,ab=128,channels=2,samplerate=44100}:file{dst=D:\\savedir.mp4}``\ ````\ ``:sout-keep``\ ````\ ``:screen-mouse-image=``\ **\ ```file:///c:/cursorimage.png`` <file:///c:/cursorimage.png>`__

How to get audio to work?

On a dual head monitor, how to make sure the recording is happening on target monitor?

Commands I've used
~~~~~~~~~~~~~~~~~~

vlc screen:// --dshow-fps=29.950001 --nooverlay --sout #transcode{vcodec=h264,vb=800, scale=0.5,acodec=mp3,ab=128,channels=2} :duplicate{dst=std{access=file, mux=mp4,dst=/home/user/Desktop/test.flv}}

Produced a black screen... on my Fedora 12 machine.

Screenshot
----------

The following screenshot is unrelated to the previous demonstration.

.. figure:: Screen_feed_demo.png
   :alt: One user created a Droste effect with a screen feed of the screen feed. Click the image to view full-size.

   One user created a Droste effect with a screen feed of the screen feed. Click the image to view full-size.

.. raw:: mediawiki

   {{Stub}}

.. raw:: mediawiki

   {{Documentation footer}}
