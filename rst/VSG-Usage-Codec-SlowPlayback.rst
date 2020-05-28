Too slow H.264/MPEG-4 AVC playback
----------------------------------

You can speed up the H.264/MPEG-4 AVC playback by disabling loop filter for H.264 decoding. To do this go to **Tools -> Preferences** (set Show Settings to All) and **Input / Codecs -> Other codecs -> FFmpeg** and in the drop-down box for **Skip the loop filter for H.264 decoding** change it to **All**.

You can also try GPU based video decoding (works on NVIDIA Geforce 9xx0 and newer cards also on ATI Radeon HD 5xx0 and newer ones). You can enable it from **Tools -> Preferences** and **Input & Codecs** and tick **Use GPU acceleration**.

Remember to press **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.
