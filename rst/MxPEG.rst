.. raw:: mediawiki

   {{Codec audio|id=MXPG}}

.. raw:: mediawiki

   {{Codec video|id=MXPG}}

**MxPEG** is an audio and video codec developed by Mobotix.

VLC supports this codec **since version 2.0.1** through `FFmpeg <FFmpeg>`__ on Windows, macOS and GNU/Linux.

While mxg video files are auto-detected, live streams require VLC to be run with the option *ffmpeg-format=mxg* because FFmpeg does not auto-detect the mxg codec in live streams.

Usage Examples
--------------

mxg recordings
~~~~~~~~~~~~~~

Simply open the file with VLC.

Live Streams
~~~~~~~~~~~~

-  **Windows:**

``{{%}} vlc.exe --avformat-format=mxg "http://<USER>:<PASSWORD>@<IP>:<PORT>/control/faststream.jpg?stream=MxPEG"``

-  **macOS:**

``{{%}} VLC.app/Contents/MacOS/VLC --avformat-format=mxg "http://<USER>:<PASSWORD>@<IP>:<PORT>/control/faststream.jpg?stream=MxPEG"``

-  **Linux:**

``{{%}} vlc --avformat-format=mxg "http://<USER>:<PASSWORD>@<IP>:<PORT>/control/faststream.jpg?stream=MxPEG"``

-  **GUI:**

   Media → Open Network Stream → Show more options. In **Edit Options**, add ":avformat-format=mxg".

For VLC 2.0.x and older, replace avformat-format with ffmpeg-format.

See also
--------

-  Technical description - https://developer.mobotix.com/docs/mxpeg_frame.html
-  Feature request and discussion in the VideoLAN forums - http://forum.videolan.org/viewtopic.php?f=7&t=97738

`Category:Container <Category:Container>`__
