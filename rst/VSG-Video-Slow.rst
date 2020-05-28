\__NOTOC_\_

Video displays first frames and black/grey only
-----------------------------------------------

This is the symptom of a slow decoding, and this is especially the case with high bitrate H264 or HEVC.

If you're using VLC < 3.0, you need turn on hardware acceleration. Preferences -> Input Codecs -> Hardware Acceleration.

Is your Graphic card able to accelerate decoding ?

| 
| For 4K H264

-  Quick Sync 4 (Intel Broadwell ~)
-  PureVideo HD 5 cards (Nvidia GT 520 ~)
-  UVD 5.0 cards (AMD Radeon R9 ~)

| 
| For HEVC

-  Quick Sync 5 (Intel Skylake ~)
-  PureVideo HD 7 cards (Nvidia GTX 950 ~, or GTX 750 SE)
-  UVD 6.0 cards (AMD Radeon Rx300 ~)

| 
| For HEVC 10bit

-  Quick Sync 6 (Intel Kaby Lake ~)
-  PureVideo HD 7 cards (Nvidia GTX 950 ~, or GTX 750 SE)
-  UVD 6.0 Fiji/Carrizo cards (AMD Radeon Rx400 ~)

| 
| All information per chip
| https://en.wikipedia.org/wiki/Intel_Quick_Sync_Video
| https://en.wikipedia.org/wiki/Unified_Video_Decoder
| https://en.wikipedia.org/wiki/Nvidia_PureVideo
| 
