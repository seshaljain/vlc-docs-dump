Video output is black, white or garbled; or you see green, blue, or red lines
-----------------------------------------------------------------------------

*If your video output is black, white or garbled; or you see green, blue, or red lines on your video, then this article is for you.* |vlc with Wrong renderer|

Usually the problem lies in display adapter drivers. If you are too scared to update your display adapter drivers, you can change VLC settings to make video work.

| 
| If you are using Windows XP or older the easiest fix is usually to disable **Accelerated video output/Overlay** **video output** which can be found by opening **Tools > Preferences > Video. ** After you have unticked the **Accelerated video output**, press **Save** to save VLC settings and restart VLC to make sure changes are enabled. If you want a clearer idea about Overlay video output settings, then follow this `link <http://koti.mbnet.fi/raiska/tutorials/vlc092/11a.png>`__.

| 
| If disabling **Overlay video output** doesn't help, then the next step is to change video output module. Open **Tools > Preferences**. Set Show Settings to All and then choose **Video > Output** module.

There are multiple output modules you can use. For Windows XP and younger you can try **DirectX 3D, DirectX, OpenGL** and **Windows GDI** video output modules.

With Windows Vista, DirectX and Windows GDI output modules will disable Aero. So if you want to use Aero, please use DirectX 3D (should be default). Remember to press\ **Save** to save VLC settings and restart VLC after that to make sure changes are enabled.

| Click `here <http://koti.mbnet.fi/raiska/tutorials/vlc092/11b.png>`__ to have a better idea of Overlay Video Output Settings.
| 

.. |vlc with Wrong renderer| image:: VLC_video.jpg
   :width: 400px
