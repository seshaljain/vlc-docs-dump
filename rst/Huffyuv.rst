.. raw:: mediawiki

   {{Codec video|id=HFYU}}

.. raw:: mediawiki

   {{Mmwiki|HuffYUV}}

**Huffyuv** (also known as Huffman `YUV <YUV>`__) is a very fast, `lossless <lossless>`__ video encoder/decoder. VLC can play Huffyuv encoded videos. If you want VLC to output Huffyuv encoded video, then the right `fourCC <fourCC>`__ is **HFYU**.

For example encode `MP4 <MP4>`__ file to `AVI <AVI>`__ with Huffyuv video and `MP3 <MP3>`__ audio:

``{{%}} vlc input.mp4 :sout=#transcode{vcodec=HFYU,scale=1,acodec=mp3,ab=128,channels=2,samplerate=44100}:file{dst=output.avi}``

Because Huffyuv is a lossless encoder, filesize is huge. e.g. two minutes of 640x360 resolution video will be near 700 megabytes.
