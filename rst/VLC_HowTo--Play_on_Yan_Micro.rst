.. raw:: mediawiki

   {{howto|Make your Video Files playable on an Play-Yan Micro}}

A Play-Yan Micro is a Nintendo peripheral for Nintendo portable game devices. See `Nintendo's official page (Japanese) <https://www.nintendo.co.jp/n08/play_yan_micro/index.html>`__ for more info.

(The rest of the page follow the format/tone set by the Ipod howto article.)

To play on this device, the file you copy to it needs to be of the correct format. This format is summarised below:

========================= =============================================================
Video Codec               **mp4v**
Audio Codec               **mp4a** (`MP4 audio <MP4_audio>`__), **aac** (`AAC <AAC>`__)
`Container <Container>`__ **mp4** (`MPEG4/MOV <MPEG-4>`__)
Size                      240x174
========================= =============================================================

To make the video the correct size, you can edit the `preferences <preferences>`__, or run vlc from a `command prompt <command_prompt>`__. For Windows, make a batch file as shown:

.. code:: dos

   set INPUT=V:\media\sample.avi
   set OUTPUT=V:\transcode output\sample.mp4
   set VLC=F:\app\VideoLAN\VLC\vlc.exe
   %VLC% "%INPUT%" :sout=#transcode{vcodec=mp4v,vb=1024,scale=1,acodec=mp4a,audio-sync}:std{access=file,mux=mp4,url="%OUTPUT%"} --sout-transcode-width=240 --sout-transcode-height=176 --aspect-ratio=16:9

Fill in the input and output filenames. (FIXME: Aspect Ratio does not seem to be working)

Note: Some videos can be transcoded, some can't. This info is still a work in progress.
