.. raw:: mediawiki

   {{codec audio|id=mp3|encoder=y|mod=avcodec|for=[[dummy]] (raw), [[mpeg]], [[avi]], [[matroska]] and [[mp4]]}}

.. raw:: mediawiki

   {{wikipedia|MP3}}

**MP3** is a popular type of audio `compression <compression>`__ described by the `MPEG-1 <MPEG-1>`__ specification (MP3's full name is *MPEG-1 Layer 3 Audio*).

VLC can play and create MP3 files.

Creating mp3 files
------------------

   **Note:** If you try to create mp3 files it probably won't use the best compression techniques! A better alternative is to use the `LAME <wikipedia:LAME>`__ MP3 encoder.

You can make mp3 files by using the *mp3* audio codec. .mp3 files do not have a container, so you should use the `dummy <dummy>`__ container. You should also specify the ``--no-video`` option if you're taking audio from a video.

An example of this at the `command prompt <command_prompt>`__ is:

``{{%}} vlc "``\ *``input_file``*\ ``" :no-video :sout=#transcode{acodec=mp3,ab=128}:std{access=file,mux=dummy,dst="``\ *``out_file.mp3``*\ ``"}``

See also
--------

-  `ID3 <ID3>`__

External Links
--------------

-  `MPEG 1 Audio FAQ <http://sound.media.mit.edu/resources/mpeg4/audio/faq/mpeg1.html>`__ for details on the differences between the layers.
