{{codec audioencoder=yfor=[[dummy]] (raw), [[mpeg]], [[avi]],
[[matroska]] and [[mp4]]}} {{wikipedia|MP3}} '''MP3''' is a popular type
of audio [[compression]] described by the [[MPEG-1]] specification
(MP3's full name is ''MPEG-1 Layer 3 Audio'').

VLC can play and create MP3 files. {{clear}}

== Creating mp3 files == : '''Note:''' If you try to create mp3 files it
probably won't use the best compression techniques! A better alternative
is to use the [[wikipedia:LAME|LAME]] MP3 encoder.

You can make mp3 files by using the ''mp3'' audio codec. .mp3 files do
not have a container, so you should use the ''[[dummy]]'' container. You
should also specify the <code>--no-video</code> option if you're taking
audio from a video.

An example of this at the [[command prompt]] is:
   {{%}} vlc "''input_file''" :no-video
   :sout=#transcode{acodec=mp3,ab=128}:std{access=file,mux=dummy,dst="''out_file.mp3''"}

== See also == \* [[ID3]]

== External Links == \*
[http://sound.media.mit.edu/resources/mpeg4/audio/faq/mpeg1.html MPEG 1
Audio FAQ] for details on the differences between the layers.
