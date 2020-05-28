== Video output is black, white or garbled; or you see green, blue, or
red lines<br> ==

''If your video output is black, white or garbled; or you see green,
blue, or red lines on your video, then this article is for you.''
[[File:VLC video.jpgthumbnailvlc with Wrong renderer]]

Usually the problem lies in display adapter drivers. If you are too
scared to update your display adapter drivers, you can change VLC
settings to make video work.

<br>

If you are using Windows XP or older the easiest fix is usually to
disable '''Accelerated video output/Overlay''' '''video output''' which
can be found by opening '''Tools &gt; Preferences &gt; Video.&nbsp;'''
After you have unticked the '''Accelerated video output''', press
'''Save''' to save VLC settings and restart VLC to make sure changes are
enabled. If you want a clearer idea about Overlay video
output&nbsp;settings, then follow this
[http://koti.mbnet.fi/raiska/tutorials/vlc092/11a.png link].

<br>

If disabling '''Overlay video output''' doesn't help, then the next step
is to change video output module. Open '''Tools &gt; Preferences'''. Set
Show Settings to All and then choose '''Video &gt; Output''' module.

There are multiple output modules you can use. For Windows XP and
younger you can try '''DirectX 3D, DirectX, OpenGL''' and '''Windows
GDI''' video output modules.

With Windows Vista, DirectX and Windows GDI output modules will disable
Aero. So if you want to use Aero, please use DirectX 3D (should be
default). Remember to press'''Save''' to save VLC settings and restart
VLC after that to make sure changes are enabled.

Click [http://koti.mbnet.fi/raiska/tutorials/vlc092/11b.png here] to
have a better idea of Overlay Video Output Settings.<br>

<br>

<br>

<br>

<br>

{{VSG}}
