VLC can partially play video, but its playback is choppy.
---------------------------------------------------------

Your system might be too slow to decode all pictures. It might be that your CPU basically is not fast enough, but often the situation can be improved by changing your system configuration to be a bit kinder to VLC. It can also be that the subsystem is misconfigured/misdriven, this happens for example under Redhat Linux. Here are some ways to improve speed:

-  Quit other programs running in the background.
-  Try disabling framedropping. Framedropping allows VLC not to decode some pictures when the CPU is overloaded, but can result in choppier playback under certain conditions. Framedropping behaviour can be configured in the Video preferences of VLC.
-  Enable speed tricks, allowling VLC to decode slightly faster at the possible risk of graphical anomalies. This works with some codecs, such as H.264. Go to Tools → Preferences (All) → Video Codecs → FFmpeg → Allow Speed Tricks → Select 'All'. Save and restart VLC for settings to take effect.
-  Turn on DMA on your DVD device:
   **Linux:** # hdparm -d1 /dev/dvd
   **Windows:** Go to the System section of the control panel, and go to the Hardware manager (it is sometimes in a separate tab, and sometimes, you have to go to the Advanced tab. Then, right-click on your DVD player, and check the DMA checkbox.
-  Upgrade to the latest driver for your video board.
-  In Linux, you can additionally upgrade your drivers to the latest XFree86 version. If supported, check that the xvideo plug-in is effectively used with: % vlc -vvvv

| 
| 
